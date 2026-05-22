#!/usr/bin/env python3
"""Head-to-head model comparison for the Phase-C results-draft task.

Reuses the production prompt, extraction, and gates from
``batch_generate_results_drafts.py`` and runs the SAME prompt against several
chat-completions providers/models. Captures latency, token usage, the draft
contract gate, the verbatim-quote gate, and the style lint, then writes a
side-by-side report. This is a throwaway evaluation harness, not a pipeline.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import time
from pathlib import Path
from urllib import request
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import batch_generate_results_drafts as B  # noqa: E402

OUT_DIR = ROOT / "corpus_inventory" / "track_b_drafts" / "_model_compare"

# (label, model, base_url, env-var-name-for-key)
CANDIDATES = [
    ("deepseek-v4-pro (baseline)", "deepseek-v4-pro", "https://api.deepseek.com/v1", "DEEPSEEK_API_KEY"),
    ("qwen3.7-max", "qwen3.7-max", "https://dashscope.aliyuncs.com/compatible-mode/v1", "QWEN_API_KEY"),
    ("qwen3.6-plus", "qwen3.6-plus", "https://dashscope.aliyuncs.com/compatible-mode/v1", "QWEN_API_KEY"),
    ("qwen-flash", "qwen-flash", "https://dashscope.aliyuncs.com/compatible-mode/v1", "QWEN_API_KEY"),
]


def chat(base_url, api_key, model, prompt, temperature, max_tokens, timeout):
    """Like B.chat_completion but returns (content, usage_dict, raw_error)."""
    url = base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": B.SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    def _send(extra):
        body = json.dumps({**payload, **extra}).encode("utf-8")
        req = request.Request(
            url, data=body, method="POST",
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        )
        with request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace")

    try:
        raw = _send({})
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        # qwen3 hybrid models reject non-stream when thinking is on -> retry off
        if "enable_thinking" in detail or "thinking" in detail.lower():
            try:
                raw = _send({"enable_thinking": False})
            except HTTPError as exc2:
                return "", {}, f"HTTP {exc2.code}: {exc2.read().decode('utf-8','replace')[:600]}"
            except URLError as exc2:
                return "", {}, f"URL error: {exc2}"
        else:
            return "", {}, f"HTTP {exc.code}: {detail[:600]}"
    except URLError as exc:
        return "", {}, f"URL error: {exc}"

    data = json.loads(raw)
    try:
        content = data["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError, TypeError):
        return "", {}, f"unexpected shape: {raw[:600]}"
    return content, data.get("usage", {}), ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--papers", default="23-PSZ,22-FHKF", help="Comma-separated codes.")
    ap.add_argument("--models", default=None,
                    help="Comma-separated model names to restrict CANDIDATES (e.g. qwen3.7-max).")
    ap.add_argument("--temperature", type=float, default=0.2)
    ap.add_argument("--max-tokens", type=int, default=8000)
    ap.add_argument("--api-timeout", type=int, default=300)
    ap.add_argument("--min-quotes", type=int, default=12)
    ap.add_argument("--max-quote-words", type=int, default=25)
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    papers = B.parse_gold_set(B.GOLD_SET)
    B.resolve_sources(papers)
    by_code = {p.code: p for p in papers}
    wanted = [c.strip() for c in args.papers.split(",") if c.strip()]

    candidates = CANDIDATES
    if args.models:
        keep = {m.strip() for m in args.models.split(",") if m.strip()}
        candidates = [c for c in CANDIDATES if c[1] in keep]

    results_patterns = B.read_text(B.RESULTS_PATTERNS, 6000)
    contract, contract_src = B.load_pdf_reader_contract(2500)

    rows = []  # dicts for the report
    for code in wanted:
        paper = by_code[code]
        ok, results_text, _ = B.extract_results(paper.pdf_path, 180)
        if not ok:
            print(f"!! extraction failed for {code}; skipping")
            continue
        prompt = B.build_prompt(paper, results_text, results_patterns, contract, contract_src)
        print(f"\n=== {code} (results section: {len(results_text)} chars, prompt: {len(prompt)} chars) ===")
        for label, model, base_url, key_env in candidates:
            api_key = B.get_env_var(key_env)
            if not api_key:
                print(f"  [{label}] no key in {key_env}; skip")
                continue
            t0 = time.time()
            content, usage, err = chat(
                base_url, api_key, model, prompt,
                args.temperature, args.max_tokens, args.api_timeout,
            )
            elapsed = time.time() - t0
            if err:
                print(f"  [{label}] ERROR after {elapsed:.0f}s: {err}")
                rows.append(dict(code=code, label=label, model=model, error=err, elapsed=elapsed))
                continue
            content = B.normalize_api_markdown(content)
            out_path = OUT_DIR / f"{code}__{model.replace('/', '_')}.md"
            out_path.write_text(content.rstrip() + "\n", encoding="utf-8")

            contract_errs = B.draft_contract_errors(content, args.min_quotes)
            quotes = B.extract_quote_cells(content)
            q_status, q_detail = B.verify_quotes(
                out_path, paper.txt_path, results_text,
                args.min_quotes, args.max_quote_words, 120,
            )
            l_status, l_detail = B.run_lint(out_path, 120)
            row = dict(
                code=code, label=label, model=model, elapsed=elapsed,
                chars=len(content), quotes=len(quotes),
                prompt_tokens=usage.get("prompt_tokens"),
                completion_tokens=usage.get("completion_tokens"),
                contract="OK" if not contract_errs else "; ".join(contract_errs),
                quote=q_status, quote_detail=q_detail,
                lint=l_status, lint_detail=l_detail,
                out=out_path.name,
            )
            rows.append(row)
            print(f"  [{label}] {elapsed:5.0f}s  {len(content):5d} chars  "
                  f"q={len(quotes):2d}  contract={'OK' if not contract_errs else 'X'}  "
                  f"quote={q_status}  lint={l_status}")

    # Write report
    report = [
        "# Model comparison: results-draft task",
        "",
        f"Generated: {dt.datetime.now().isoformat(timespec='seconds')}",
        f"Papers: {', '.join(wanted)}  |  temp={args.temperature}  max_tokens={args.max_tokens}",
        f"Gate thresholds: >= {args.min_quotes} quotes, <= {args.max_quote_words} words/quote",
        "",
        "| Paper | Model | Latency | Out chars | Quotes | Prompt tok | Compl tok | Contract | Quote gate | Lint |",
        "|---|---|--:|--:|--:|--:|--:|---|---|---|",
    ]
    for r in rows:
        if r.get("error"):
            report.append(f"| {r['code']} | {r['label']} | {r['elapsed']:.0f}s | ERROR | - | - | - | "
                          f"{r['error'][:60]} | - | - |")
            continue
        report.append(
            f"| {r['code']} | {r['label']} | {r['elapsed']:.0f}s | {r['chars']} | {r['quotes']} | "
            f"{r['prompt_tokens']} | {r['completion_tokens']} | "
            f"{'OK' if r['contract']=='OK' else 'FAIL: '+r['contract'][:40]} | "
            f"{r['quote']} | {r['lint']} |"
        )
    report.append("")
    report.append("## Gate details")
    for r in rows:
        if r.get("error"):
            continue
        report.append(f"- **{r['code']} / {r['label']}** -> `{r['out']}`")
        report.append(f"  - quote: {r['quote_detail']}")
        report.append(f"  - lint: {r['lint_detail']}")
        if r["contract"] != "OK":
            report.append(f"  - contract: {r['contract']}")
    (OUT_DIR / "REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"\nWrote {OUT_DIR / 'REPORT.md'}")


if __name__ == "__main__":
    raise SystemExit(main())

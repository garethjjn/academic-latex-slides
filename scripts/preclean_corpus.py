#!/usr/bin/env python3
"""Pre-clean audit-paper source text into normalized ASCII companions.

For each pilot paper, read the raw companion ``<stem>.txt`` (or PyMuPDF-extract
the PDF), apply *line-preserving* cleaning, and write ``<stem>.clean.txt`` next
to the PDF. Both the section splitter (pdf_section_split.find_companion_txt) and
the batch generator (batch_generate_results_drafts.find_txt) prefer the cleaned
companion, so the model receives clean ASCII prose and the verbatim-quote gate
matches it.

Cleaning is deliberately CONSERVATIVE (default):
  - character normalization: ligatures (fi/fl/...), unicode dashes + MINUS SIGN,
    curly quotes, ellipsis, exotic spaces, zero-width chars  -> plain ASCII;
  - drop CLEAR non-prose lines only: bare page numbers, frequently-repeated
    running heads/footers, download/JSTOR/SSRN boilerplate, and numeric-dominant
    table rows (e.g. "AI (-3, 0) -0.050 -0.014 -0.019").
Prose is always kept, including sentences that contain numbers ("a 4.5% increase").
Section-header lines and blank-line paragraph structure are preserved so section
detection still works.

Originals are never modified. Re-run with --overwrite to regenerate.

Usage:
  python scripts/preclean_corpus.py [--only 23-PSZ,22-FHKF] [--limit N]
                                    [--overwrite] [--dry-run]
                                    [--repeat-threshold 4] [--no-drop-tables]
                                    [--no-drop-repeated] [--no-drop-boilerplate]
                                    [--verify-extract]
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from collections import Counter
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import batch_generate_results_drafts as B  # noqa: E402

REPORT_PATH = ROOT / "corpus_inventory" / "track_b_drafts" / "_preclean_report.md"

# --- character normalization (whole-text, length-preserving in line count) ----
CHAR_MAP = {
    # ligatures
    "ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi",
    "ﬄ": "ffl", "ﬅ": "ft", "ﬆ": "st",
    # dashes + minus sign -> ASCII hyphen
    "‐": "-", "‑": "-", "‒": "-", "–": "-",
    "—": "-", "―": "-", "−": "-",
    # quotes
    "“": '"', "”": '"', "„": '"', "‟": '"',
    "‘": "'", "’": "'", "‚": "'", "‛": "'",
    "′": "'", "″": '"',
    # ellipsis
    "…": "...",
    # exotic spaces -> normal space
    " ": " ", " ": " ", " ": " ", " ": " ",
    " ": " ", " ": " ", " ": " ", "　": " ",
    # zero-width / soft hyphen -> remove
    "​": "", "‌": "", "‍": "", "­": "", "﻿": "",
}
_CHAR_TABLE = {ord(k): v for k, v in CHAR_MAP.items()}

# --- line classifiers ---------------------------------------------------------
PAGE_NUM_RE = re.compile(r"^\s*[-–—]?\s*(?:page\s+)?\d{1,4}\s*[-–—]?\s*$", re.I)
ROMAN_PAGE_RE = re.compile(r"^\s*[ivxlcdm]{1,7}\s*$", re.I)
BOILERPLATE_RES = [
    re.compile(p, re.I) for p in (
        r"this content downloaded",
        r"all use subject to",
        r"jstor\.org",
        r"https?://(www\.)?jstor",
        r"electronic copy available at",
        r"ssrn\.com",
        r"papers\.ssrn",
        r"^\s*downloaded from\b",
        r"^\s*doi:\s*10\.",
        r"^\s*©\s*\d{4}",
        r"\bAll Rights Reserved\b",
    )
]
# A token that reads as a numeric/statistic cell: 12, -0.050, (2.34), 1,234, 5%, .03***
NUM_TOKEN_RE = re.compile(r"^[\(\[]?[+-]?\$?\d[\d.,]*\)?%?\*{0,3}[\)\]]?$")
# A token of pure significance markers / separators
SYMBOL_TOKEN_RE = re.compile(r"^[\*†‡§%/=<>±~\-—–.,;:()\[\]]+$")
SENTENCE_END = (".", "?", "!", ":")
# Section header: "4. Empirical Results" / "IV. Results" — never drop these.
HEADER_RE = re.compile(r"^\s*(\d{1,2}|[IVXLC]{1,5})\.?\s+[A-Z][A-Za-z].{1,78}$")


def alpha_word_count(tokens: list[str]) -> int:
    return sum(1 for t in tokens if len(re.sub(r"[^A-Za-z]", "", t)) >= 2)


def numeric_token_count(tokens: list[str]) -> int:
    return sum(1 for t in tokens if NUM_TOKEN_RE.match(t))


def is_table_row(line: str) -> bool:
    """Numeric-dominant, non-sentence line — a table/regression row, not prose."""
    s = line.strip()
    if not s:
        return False
    if HEADER_RE.match(s):
        return False
    tokens = s.split()
    if len(tokens) < 2:
        return False
    nums = numeric_token_count(tokens)
    alphas = alpha_word_count(tokens)
    if nums >= 3 and nums >= alphas and not s.endswith(SENTENCE_END):
        return True
    # line made almost entirely of symbols/stars/numbers
    symbolic = sum(1 for t in tokens if SYMBOL_TOKEN_RE.match(t) or NUM_TOKEN_RE.match(t))
    if symbolic == len(tokens) and alphas == 0:
        return True
    return False


def repeated_lines(lines: list[str], threshold: int) -> set[str]:
    """Normalized short non-sentence lines occurring >= threshold times (running heads)."""
    counts: Counter[str] = Counter()
    for ln in lines:
        s = ln.strip()
        if not s or len(s) > 80 or s.endswith(SENTENCE_END) or HEADER_RE.match(s):
            continue
        counts[re.sub(r"\s+", " ", s).lower()] += 1
    return {k for k, v in counts.items() if v >= threshold}


def clean_text(text: str, args) -> tuple[str, Counter]:
    text = text.translate(_CHAR_TABLE)
    lines = text.split("\n")
    repeats = repeated_lines(lines, args.repeat_threshold) if not args.no_drop_repeated else set()
    out: list[str] = []
    dropped: Counter = Counter()
    samples: dict[str, list[str]] = {}

    def record(cat: str, line: str) -> None:
        dropped[cat] += 1
        samples.setdefault(cat, [])
        if len(samples[cat]) < 4:
            samples[cat].append(line.strip()[:90])

    for ln in lines:
        s = ln.strip()
        norm = re.sub(r"\s+", " ", s).lower()
        if PAGE_NUM_RE.match(s) or ROMAN_PAGE_RE.match(s):
            record("page_number", ln)
            continue
        if not args.no_drop_boilerplate and any(r.search(s) for r in BOILERPLATE_RES):
            record("boilerplate", ln)
            continue
        if repeats and norm in repeats:
            record("repeated_head", ln)
            continue
        if not args.no_drop_tables and is_table_row(ln):
            record("table_row", ln)
            continue
        out.append(ln.rstrip())

    cleaned = "\n".join(out)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip() + "\n"
    dropped.samples = samples  # type: ignore[attr-defined]
    return cleaned, dropped


def raw_source(pdf_path: Path) -> tuple[str, str] | None:
    """Read the RAW companion txt (never the .clean.txt), else PyMuPDF."""
    same = pdf_path.with_suffix(".txt")
    if same.exists():
        return same.read_text(encoding="utf-8", errors="replace"), f"txt:{same.name}"
    if pdf_path.parent.name == "audit_writing_corpus":
        cand = pdf_path.parent / "txt" / (pdf_path.stem + ".txt")
        if cand.exists():
            return cand.read_text(encoding="utf-8", errors="replace"), f"txt:{cand.name}"
    try:
        import fitz  # type: ignore
        doc = fitz.open(str(pdf_path))
        return "\n".join(p.get_text() for p in doc), "pymupdf"
    except Exception:
        return None


def non_ascii_summary(text: str, top: int = 8) -> str:
    c = Counter(ch for ch in text if ord(ch) > 127)
    if not c:
        return "pure ASCII"
    parts = [f"{repr(ch)}x{n}" for ch, n in c.most_common(top)]
    return f"{sum(c.values())} non-ASCII ({len(c)} distinct): " + ", ".join(parts)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", help="Comma-separated paper codes.")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--overwrite", action="store_true", help="Regenerate existing .clean.txt files.")
    ap.add_argument("--dry-run", action="store_true", help="Report only; write nothing.")
    ap.add_argument("--repeat-threshold", type=int, default=4,
                    help="Drop short non-sentence lines occurring >= N times (running heads).")
    ap.add_argument("--no-drop-tables", action="store_true")
    ap.add_argument("--no-drop-repeated", action="store_true")
    ap.add_argument("--no-drop-boilerplate", action="store_true")
    ap.add_argument("--verify-extract", action="store_true",
                    help="After cleaning, confirm the results section still extracts.")
    args = ap.parse_args(argv)

    papers = B.parse_gold_set(B.GOLD_SET)
    B.resolve_sources(papers)
    try:
        selected = B.filter_papers(papers, args.only, args.limit)
    except SystemExit as exc:
        print(str(exc), file=sys.stderr)
        return 2

    rows = []
    for paper in selected:
        if paper.pdf_path is None:
            rows.append(dict(code=paper.code, status="MISSING_PDF"))
            print(f"{paper.code:<8} MISSING_PDF")
            continue
        out_path = paper.pdf_path.with_name(paper.pdf_path.stem + ".clean.txt")
        if out_path.exists() and not args.overwrite and not args.dry_run:
            rows.append(dict(code=paper.code, status="SKIP_EXISTING", out=out_path.name))
            print(f"{paper.code:<8} SKIP_EXISTING ({out_path.name})")
            continue
        src = raw_source(paper.pdf_path)
        if src is None:
            rows.append(dict(code=paper.code, status="NO_SOURCE"))
            print(f"{paper.code:<8} NO_SOURCE")
            continue
        raw, src_label = src
        cleaned, dropped = clean_text(raw, args)
        raw_lines, clean_lines = raw.count("\n") + 1, cleaned.count("\n") + 1
        verify = ""
        if not args.dry_run:
            out_path.write_text(cleaned, encoding="utf-8")
            if args.verify_extract:
                proc = B.run_subprocess(
                    [sys.executable, str(B.SECTION_SPLITTER), str(paper.pdf_path), "results"],
                    timeout=120,
                )
                # primary OR fallback success counts as OK
                ok, _, _ = B.extract_results(paper.pdf_path, 120)
                verify = "extract:OK" if ok else f"extract:FAIL(rc={proc.returncode})"
        row = dict(
            code=paper.code, status="DRY_RUN" if args.dry_run else "WROTE",
            src=src_label, out=out_path.name,
            raw_lines=raw_lines, clean_lines=clean_lines,
            raw_chars=len(raw), clean_chars=len(cleaned),
            dropped=dict(dropped), samples=getattr(dropped, "samples", {}),
            residue=non_ascii_summary(cleaned), verify=verify,
        )
        rows.append(row)
        drop = ", ".join(f"{k}={v}" for k, v in sorted(dropped.items())) or "none"
        print(f"{paper.code:<8} {row['status']:<8} lines {raw_lines}->{clean_lines}  "
              f"chars {len(raw)}->{len(cleaned)}  dropped[{drop}]  {verify}")

    # report
    lines = [
        "# Pre-clean report",
        "",
        f"Generated: {dt.datetime.now().isoformat(timespec='seconds')}",
        f"Mode: {'DRY_RUN' if args.dry_run else 'WRITE'}  |  drop tables={not args.no_drop_tables} "
        f"repeated={not args.no_drop_repeated}(>= {args.repeat_threshold}) "
        f"boilerplate={not args.no_drop_boilerplate}",
        "",
        "| Code | Status | Lines (raw->clean) | Chars (raw->clean) | Dropped | Residual non-ASCII | Verify |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        if r.get("status") in (None, "MISSING_PDF", "NO_SOURCE", "SKIP_EXISTING"):
            lines.append(f"| {r['code']} | {r.get('status','')} | - | - | - | - | {r.get('out','')} |")
            continue
        drop = "<br>".join(f"{k}: {v}" for k, v in sorted(r["dropped"].items())) or "none"
        lines.append(
            f"| {r['code']} | {r['status']} | {r['raw_lines']}->{r['clean_lines']} | "
            f"{r['raw_chars']}->{r['clean_chars']} | {drop} | {r['residue'][:80]} | {r['verify']} |"
        )
    lines.append("")
    lines.append("## Sample dropped lines (audit the conservative heuristics)")
    for r in rows:
        if not r.get("samples"):
            continue
        lines.append(f"### {r['code']}")
        for cat, ex in r["samples"].items():
            for e in ex:
                lines.append(f"- `{cat}`: {e}")
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nWrote {REPORT_PATH.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

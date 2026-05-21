#!/usr/bin/env python3
"""drop_failing_quotes.py — remove annotated-table rows whose Quote cell does not
verify verbatim against the paper's source TXT.

Deterministic companion to repair_draft_quotes.py: repair fixes what it can by
fuzzy-matching a verbatim span; this drops the residual rows that still fail, so
a staging draft becomes fully quote-clean. Non-table content (Commentary,
Self-check, Reviewer notes) is left untouched. Refuses to drop below --min-keep
verified rows (reports instead, so a thin draft is flagged not silently gutted).

Usage:
  drop_failing_quotes.py <section> [codes...] [--min-keep 12] [--apply]
Without --apply it is a dry run. Sections: any <code>_<section>.md suffix.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import batch_generate_results_drafts as B  # noqa: E402

DRAFTS = ROOT / "corpus_inventory" / "track_b_drafts"
VERIFY = ROOT / "audit-write-skills" / "plugins" / "audit-write" / "scripts" / "verify_quote.py"


def is_table_row(line: str) -> bool:
    s = line.strip()
    return s.startswith("|") and s.endswith("|") and s.count("|") >= 6


def quote_cell(line: str) -> str:
    # | Para | Quote | Block | Move | Annotation | Conf |  -> cell index 2
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    return cells[1] if len(cells) >= 2 else ""


def is_separator(line: str) -> bool:
    return set(line.strip()) <= set("|-: ")


def verifies(txt_path: Path, quote: str) -> bool:
    q = quote.strip().strip('"').strip()
    if not q:
        return False
    proc = subprocess.run([sys.executable, str(VERIFY), str(txt_path), q],
                          capture_output=True, text=True, encoding="utf-8", errors="replace")
    return proc.returncode == 0


def process(code: str, section: str, min_keep: int, apply: bool,
            txt_by_code: dict[str, Path]) -> None:
    draft = DRAFTS / f"{code}_{section}.md"
    if not draft.exists():
        print(f"{code:<9} MISSING ({draft.name})")
        return
    txt = txt_by_code.get(code)
    if txt is None or not Path(txt).exists():
        print(f"{code:<9} NO_TXT — skip")
        return
    lines = draft.read_text(encoding="utf-8").splitlines()
    kept, dropped, header_seen = [], [], False
    pending_drops: list[str] = []
    for ln in lines:
        if is_table_row(ln) and not is_separator(ln):
            q = quote_cell(ln)
            # header row (the "Quote (verbatim..." labels) — keep
            if not header_seen and "quote" in q.lower():
                header_seen = True
                kept.append(ln)
                continue
            if verifies(Path(txt), q):
                kept.append(ln)
            else:
                pending_drops.append(ln)
                dropped.append(q[:70])
            continue
        kept.append(ln)
    n_quote_rows = sum(1 for k in kept if is_table_row(k) and not is_separator(k)
                       and "quote" not in quote_cell(k).lower())
    if dropped and n_quote_rows < min_keep:
        print(f"{code:<9} REFUSE — would leave {n_quote_rows} < {min_keep} verified; "
              f"{len(dropped)} residual flagged, not dropped")
        return
    print(f"{code:<9} keep={n_quote_rows} drop={len(dropped)}"
          + (f"  e.g. {dropped[0]!r}" if dropped else ""))
    if apply and dropped:
        draft.write_text("\n".join(kept).rstrip() + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    args = [a for a in (argv or sys.argv[1:]) if not a.startswith("--")]
    flags = [a for a in (argv or sys.argv[1:]) if a.startswith("--")]
    if not args:
        print("usage: drop_failing_quotes.py <section> [codes...] [--min-keep N] [--apply]")
        return 2
    section = args[0]
    codes = args[1:]
    apply = "--apply" in flags
    min_keep = 12
    for f in flags:
        if f.startswith("--min-keep="):
            try:
                min_keep = int(f.split("=", 1)[1])
            except ValueError:
                pass
    papers = B.parse_gold_set(B.GOLD_SET)
    B.resolve_sources(papers)
    txt_by_code = {p.code: p.txt_path for p in papers if p.txt_path}
    if not codes:
        codes = [p.code for p in papers]
    print(f"section={section} apply={apply} min_keep={min_keep}\n")
    for c in codes:
        process(c, section, min_keep, apply, txt_by_code)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

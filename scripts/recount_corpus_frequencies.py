#!/usr/bin/env python3
"""recount_corpus_frequencies.py — inventory every k/N frequency claim in the
audit-write bank + pattern files, with line + context, so Phase D can re-derive
them over the expanded corpus (n=22 = 6 template + 16 Stage-1 pilot).

This does NOT auto-rewrite — frequency re-derivation needs the move-presence
matrix (corpus_inventory/move_presence_matrix.md) and human judgment. It emits a
review table; the orchestrator applies edits after approval.

Usage: recount_corpus_frequencies.py            # scan default bank files
       recount_corpus_frequencies.py --md        # markdown table output
Exit: 0 always (advisory)
"""
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent
SK = ROOT / "audit-write-skills" / "plugins" / "audit-write" / "skills"
FILES = [
    SK / "audit-write" / "move_bank.md",
    SK / "audit-write-intro" / "intro_patterns.md",
    SK / "audit-write-hypothesis" / "hypothesis_patterns.md",
    SK / "audit-write-results" / "results_patterns.md",
]

# frequency-claim patterns (the "k/6" family + verbal forms)
CLAIM = re.compile(
    r"\b\d+/6\b"               # 4/6, 6/6
    r"|\b\d+ of 6\b"           # 5 of 6
    r"|\ball 6\b"
    r"|\bcorpus-unanimous\b"
    r"|\bunanimous\b"
    r"|\bappears in \d+\b"
    r"|\b\d+/\d+ papers\b",
    re.I,
)
# claims already re-derived to n=22 (skip — Phase C/D digests, matrix-backed)
SKIP_CONTEXT = ("n=22", "/22", "Phase-C", "Phase C", "pilot digest", "move_presence")


def scan():
    rows = []
    for f in FILES:
        if not f.exists():
            continue
        for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if any(s in line for s in SKIP_CONTEXT):
                continue
            for m in CLAIM.finditer(line):
                rows.append((f.name, i, m.group(0), line.strip()[:110]))
    return rows


def main():
    md = "--md" in sys.argv
    rows = scan()
    if md:
        print("| File | Line | Claim | Context |")
        print("|---|---|---|---|")
        for fn, ln, claim, ctx in rows:
            print(f"| {fn} | {ln} | `{claim}` | {ctx.replace('|','¦')} |")
    else:
        cur = None
        for fn, ln, claim, ctx in rows:
            if fn != cur:
                print(f"\n### {fn}")
                cur = fn
            print(f"  L{ln:>4}  {claim:<18}  {ctx}")
    print(f"\n[{len(rows)} un-re-derived frequency claims across {len(FILES)} files]")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""lint_style.py — deterministic style/integrity linter for a DRAFT.

Stdlib only. Point this at a *generated draft* (not the skill docs — those
quote banned verbs as negative examples and would false-positive). It enforces
the parts of style_dna.md / the rubric integrity gate that are mechanical:

  ERROR   personalization tokens (gareth / integexp / integrity exposure …)
  ERROR   integrity-gate smell: a hard "(Name, 19xx/20xx)" citation that is
          NOT a sanctioned methodological anchor and NOT an [AUTHOR:] slot
          → likely a fabricated reference (rubric.md gate). Heuristic; review.
  WARN    blacklist verbs in a claim ("show that", "prove", "demonstrate
          definitively", "delve", "leverage", "shed light", "pave the way",
          "pivotal", "groundbreaking", "paradigm-shifting")

Usage:  lint_style.py FILE [FILE ...]
Exit:   0 = no ERRORs · 1 = ERROR(s)   (WARNs never fail the run)
"""
import re
import sys

PERSONAL = re.compile(r"gareth|integexp|integrity[ -]?(exposure|propaganda)", re.I)
BANNED = [
    "show that", "prove that", "proves that", "demonstrate definitively",
    "delve", "leverage", "shed light", "pave the way", "paradigm-shifting",
    "groundbreaking", "pivotal",
]
# real, suite-sanctioned methodological anchors (kept as hard cites by design)
ANCHORS = [
    "aobdia", "defond and zhang", "defond & zhang", "cunningham", "cohen 19",
    "cohen, 19", "hainmueller",
]
CITE = re.compile(r"\(([A-Z][A-Za-z.\-]+(?:[^()]{0,60}?))?\b(19|20)\d{2}[a-z]?\)")


def lint(path):
    errs, warns = [], []
    try:
        lines = open(path, encoding="utf-8").read().splitlines()
    except (OSError, UnicodeDecodeError) as e:
        return [f"{path}: cannot read ({e})"], []
    for i, ln in enumerate(lines, 1):
        low = ln.lower()
        if PERSONAL.search(ln):
            errs.append(f"{path}:{i}: ERROR personalization token: {ln.strip()[:90]}")
        for m in CITE.finditer(ln):
            span = m.group(0)
            ctx = ln[max(0, m.start() - 40):m.end() + 5].lower()
            if any(a in ctx for a in ANCHORS):
                continue
            if "[author" in ctx or "[illustrative" in ctx:
                continue
            errs.append(
                f"{path}:{i}: ERROR possible fabricated cite {span} "
                f"(not a sanctioned anchor / not an [AUTHOR:] slot) — verify"
            )
        for b in BANNED:
            if b in low:
                warns.append(f"{path}:{i}: WARN blacklist verb '{b}': {ln.strip()[:80]}")
    return errs, warns


def main():
    if len(sys.argv) < 2:
        print("usage: lint_style.py FILE [FILE ...]")
        return 2
    all_err, all_warn = [], []
    for p in sys.argv[1:]:
        e, w = lint(p)
        all_err += e
        all_warn += w
    for w in all_warn:
        print(w)
    for e in all_err:
        print(e)
    if all_err:
        print(f"lint_style: {len(all_err)} ERROR(s), {len(all_warn)} WARN(s) — FAIL")
        return 1
    print(f"lint_style: 0 ERRORs, {len(all_warn)} WARN(s) — OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

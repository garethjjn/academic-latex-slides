#!/usr/bin/env python3
"""check_structure.py — advisory binary self-check for a DRAFT section.

Stdlib only. The mechanism mirror of rubric.md's "Objective pre-checklist":
it answers the *mechanically decidable* subset of the binary checklist as
literal Y / N / NA so the score is reproducible and sycophancy-resistant
(see docs/external-validation-ng.md). It does NOT score and NEVER fails the
run — the rubric + the critic agent own the judgement. Heuristic by design;
treat N/Y on C5/C6 as a prompt to look, not a verdict.

  C1  cite-integrity   no manufactured hard (Name, Year) cite
  C3  register         no blacklist verbs in the draft
  C4  AI-slop tells    no em-dash overuse / "not X ... it's Y"
  C5  structure        section's mandatory element (needs --section)
  C6  magnitude        an effect magnitude is present where required

Usage:  check_structure.py FILE [--section abstract|intro|hypothesis|design|
                                          results|robustness]
Exit:   always 0 (advisory). Prints one Y/N/NA line per check + a summary.
"""
import re
import sys

EM_DASH = "—"
BANNED = [
    "show that", "prove that", "proves that", "demonstrate definitively",
    "delve", "leverage", "shed light", "pave the way", "paradigm-shifting",
    "groundbreaking", "pivotal",
]
ANCHORS = [
    "aobdia", "defond and zhang", "defond & zhang", "cunningham", "cohen 19",
    "cohen, 19", "hainmueller",
]
CITE = re.compile(r"\(([A-Z][A-Za-z.\-]+(?:[^()]{0,60}?))?\b(19|20)\d{2}[a-z]?\)")
NOTXBUTY = [
    re.compile(r"\bit['’]s not\b[^.\n]{1,60}?\bit['’]s\b", re.I),
    re.compile(
        r"\bnot (?:just |merely |simply |only )?about\b[^.\n]{1,60}?\bit['’]s\b",
        re.I,
    ),
]
# a numeric effect magnitude: "2.1 percentage points", "19%", "0.041 (s.e.",
# "1.3 standard deviations", decile/quartile shift
MAGNITUDE = re.compile(
    r"\b\d+(?:\.\d+)?\s?(?:percentage points?|percent|%|pp|standard deviations?|"
    r"s\.?d\.?|decile|quartile)\b|\b\d+(?:\.\d+)?%|\(\s?0?\.\d{2,3}\b",
    re.I,
)
TENSION = re.compile(
    r"\btension\b|\bhowever\b|\bon the other hand\b|\bcountervailing\b|"
    r"\bcompeting (?:argument|prediction|force)|\bin contrast\b|\bnot clear\b",
    re.I,
)
# identification machinery that design (§3) must DEFER to results (§4)
ID_MACHINERY = re.compile(
    r"\bdifference-in-differences\b|\bdiff-in-diff\b|\bregression discontinuity\b|"
    r"\binstrument(?:al variable)?\b|\bfalsification\b|\bplacebo\b|"
    r"\bexogenous shock\b|\bstaggered\b|\bparallel trends?\b",
    re.I,
)


def yn(ok):
    return "Y" if ok else "N"


def check(path, section):
    try:
        text = open(path, encoding="utf-8").read()
    except (OSError, UnicodeDecodeError) as e:
        print(f"{path}: cannot read ({e})")
        return
    low = text.lower()
    rows = []

    # C1 — cite integrity (same heuristic as lint_style.py)
    fab = False
    for ln in text.splitlines():
        for m in CITE.finditer(ln):
            ctx = ln[max(0, m.start() - 40):m.end() + 5].lower()
            if any(a in ctx for a in ANCHORS):
                continue
            if "[author" in ctx or "[illustrative" in ctx:
                continue
            fab = True
    rows.append(("C1 cite-integrity", yn(not fab), "integrity gate + Dim 3"))

    # C3 — blacklist verbs
    has_banned = any(b in low for b in BANNED)
    rows.append(("C3 register (blacklist verbs)", yn(not has_banned), "Dim 2"))

    # C4 — AI-slop tells
    n_words = max(1, len(text.split()))
    n_em = text.count(EM_DASH)
    em_bad = n_em > max(2, n_words // 150)
    flat = " ".join(text.splitlines())
    notxy = any(rx.search(flat) for rx in NOTXBUTY)
    rows.append(("C4 AI-slop tells", yn(not (em_bad or notxy)), "Dim 2"))

    # C5 — section mandatory element  /  C6 — magnitude where required
    has_mag = bool(MAGNITUDE.search(text))
    if section == "abstract":
        rows.append(("C5 abstract has ZERO effect numbers",
                      yn(not has_mag), "Dim 1/3"))
    elif section == "intro":
        rows.append(("C5 intro states >=1 magnitude", yn(has_mag), "Dim 1"))
        rows.append(("C6 effect magnitude present", yn(has_mag), "Dim 3"))
    elif section == "hypothesis":
        rows.append(("C5 tension cue present", yn(bool(TENSION.search(text))),
                      "Dim 1/4"))
    elif section == "design":
        rows.append(("C5 §3 free of identification machinery",
                      yn(not ID_MACHINERY.search(text)), "Dim 1"))
    elif section in ("results", "robustness"):
        rows.append(("C6 effect magnitude present", yn(has_mag), "Dim 3"))
    else:
        rows.append(("C5/C6 section structural checks", "NA",
                      "pass --section to enable"))

    print(f"check_structure: {path}  (section={section or 'generic'})")
    for name, val, maps in rows:
        print(f"  [{val:>2}] {name:<42} -> {maps}")
    ncount = sum(1 for _, v, _ in rows if v == "N")
    print(f"  {ncount} N -> rubric.md: force each mapped dimension down one band"
          if ncount else "  0 N -> no rubric downgrade triggered by this check")


def main():
    args = [a for a in sys.argv[1:]]
    section = None
    if "--section" in args:
        i = args.index("--section")
        if i + 1 < len(args):
            section = args[i + 1].lower()
        args = args[:i] + args[i + 2:]
    if not args:
        print("usage: check_structure.py FILE [--section NAME]")
        return 0
    for p in args:
        check(p, section)
    return 0  # advisory: never fails the run


if __name__ == "__main__":
    sys.exit(main())

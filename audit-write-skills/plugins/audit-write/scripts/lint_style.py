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
  WARN    AI-slop tells (style_dna.md §9): em-dash overuse (>=3 em-dashes AND
          above density threshold) and the rhetorical "not X ... it's Y"
          construction. Conservative by design — see
          docs/external-validation-ng.md for the precision rationale.

Usage:  lint_style.py FILE [FILE ...]
Exit:   0 = no ERRORs · 1 = ERROR(s)   (WARNs never fail the run)
"""
import re
import sys

# Force UTF-8 stdout so Windows GBK codec doesn't choke on em-dashes / pilcrows.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

PERSONAL = re.compile(r"gareth|integexp|integrity[ -]?(exposure|propaganda)", re.I)
BANNED = [
    "prove that", "proves that", "demonstrate definitively",
    "delve", "leverage", "shed light", "pave the way", "paradigm-shifting",
    "groundbreaking", "pivotal",
]
# real, suite-sanctioned methodological anchors (kept as hard cites by design)
ANCHORS = [
    "aobdia", "defond and zhang", "defond & zhang", "cunningham", "cohen 19",
    "cohen, 19", "hainmueller",
]
CITE = re.compile(r"\(([A-Z][A-Za-z.\-]+(?:[^()]{0,60}?))?\b(19|20)\d{2}[a-z]?\)")

# AI-slop tells (style_dna.md §9). Deliberately conservative to avoid flagging
# legitimate audit prose ("not significant but economically large").
EM_DASH = "—"
# matches the *mirrored* "it's not X, it's Y" / "not (just) about X ... it's Y"
# form — not the bare "not A but B" used in legitimate argumentation.
NOTXBUTY = [
    re.compile(r"\bit['’]s not\b[^.\n]{1,60}?\bit['’]s\b", re.I),
    re.compile(
        r"\bnot (?:just |merely |simply |only )?about\b[^.\n]{1,60}?\bit['’]s\b",
        re.I,
    ),
]

# Contribution-block checks (C4 triadic / C7 unpinned-literature; rubric.md).
# Only run when the draft is contribution-bearing ("contribut" present), to
# avoid flagging "First,/Second," used in ordinary methods/argument lists.
# own-work "show that" (banned) vs prior-lit "the literature shows that" (fine):
# fire only when an own-work marker precedes show/shows/showing that.
OWN_SHOW = re.compile(
    r"\b(?:we|by|our|this study|this paper|results?|table|column)\b"
    r"[^.\n]{0,40}?\bshow(?:s|ing)? that\b", re.I)
ORDINAL = re.compile(r"\b(First|Second|Third|Fourth|Fifth|Finally),\s", re.I)
# a contribution legitimately names a literature / prior work / cite-or-author slot
LIT_SIGNAL = re.compile(
    r"\bliterature\b|\bresearch\b|\bstudies\b|\bstream\b|\bwork on\b|"
    r"\bprior work\b|\bline of\b|\[author|\([A-Z][A-Za-z.\-]+[^()]{0,40}\b(?:19|20)\d{2}",
    re.I,
)


def contribution_segments(text):
    """Return [(ordinal, segment_text), ...] for a contribution block, or []."""
    if "contribut" not in text.lower():
        return []
    marks = [(m.group(1).capitalize(), m.start()) for m in ORDINAL.finditer(text)]
    if len(marks) < 2:                       # not a numbered list
        return []
    segs = []
    for k, (ordn, start) in enumerate(marks):
        end = marks[k + 1][1] if k + 1 < len(marks) else min(len(text), start + 600)
        segs.append((ordn, text[start:end]))
    return segs


def lint(path):
    errs, warns = [], []
    try:
        text = open(path, encoding="utf-8").read()
    except (OSError, UnicodeDecodeError) as e:
        return [f"{path}: cannot read ({e})"], []
    lines = text.splitlines()
    for i, ln in enumerate(lines, 1):
        low = ln.lower()
        if PERSONAL.search(ln):
            errs.append(f"{path}:{i}: ERROR personalization token: {ln.strip()[:90]}")
        # Build a set of character ranges that fall INSIDE a "..." verbatim
        # quote on this line. Cites inside verbatim quotes from a source paper
        # are not fabrications — they belong to the cited paper, not the
        # annotator. We skip them.
        quoted_ranges = []
        in_q = False
        q_start = None
        for j, ch in enumerate(ln):
            if ch == '"':
                if not in_q:
                    in_q = True
                    q_start = j + 1
                else:
                    in_q = False
                    quoted_ranges.append((q_start, j))
        def _inside_quote(a, b):
            return any(qs <= a and b <= qe for qs, qe in quoted_ranges)
        for m in CITE.finditer(ln):
            span = m.group(0)
            if _inside_quote(m.start(), m.end()):
                continue
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
    # file-level AI-slop tells (style_dna.md §9)
    n_words = max(1, len(text.split()))
    n_em = text.count(EM_DASH)
    em_threshold = max(2, n_words // 150)  # floor 2 → never warns on <3 em-dashes
    if n_em > em_threshold:
        warns.append(
            f"{path}: WARN em-dash overuse: {n_em} em-dashes "
            f"(threshold {em_threshold} for {n_words} words) — style_dna.md §9"
        )
    flat = " ".join(lines)
    for rx in NOTXBUTY:
        m = rx.search(flat)
        if m:
            warns.append(
                f"{path}: WARN rhetorical \"not X ... it's Y\" construction: "
                f"\"{m.group(0)[:60]}\" — style_dna.md §9"
            )
            break
    m = OWN_SHOW.search(flat)
    if m:
        warns.append(
            f"{path}: WARN blacklist verb 'show that' (own-work claim): "
            f"\"{m.group(0)[:60]}\" — use find / document (style_dna §2)"
        )
    # contribution-block checks (rubric.md C7 + C4-triadic)
    segs = contribution_segments(text)
    for ordn, seg in segs:
        if not LIT_SIGNAL.search(seg):
            warns.append(
                f"{path}: WARN contribution-literature: '{ordn}' contribution names "
                f"no identifiable literature/research/[AUTHOR:] (rubric C7, Dim 4)"
            )
    if len(segs) == 3 and all(o in ("First", "Second", "Third") for o, _ in segs):
        lens = [len(s.split()) for _, s in segs]
        if min(lens) and (max(lens) - min(lens)) / max(lens) <= 0.20:
            warns.append(
                f"{path}: WARN triadic-contributions: three contributions of near-equal "
                f"length ({'/'.join(map(str, lens))} words) — AI tell, vary length "
                f"(rubric C4, Dim 2; style_dna.md §9)"
            )
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

#!/usr/bin/env python3
"""consistency_check.py — advisory whole-paper internal-consistency extractor.

Stdlib only, offline, READ-ONLY. The mechanism layer for `audit-write-review`
CONSISTENCY mode: it does the *deterministic* extraction so the model can spend
its judgement on the things a regex cannot decide (notation drift, claim parity).
It NEVER edits the manuscript and NEVER fails the run (advisory, exit 0).

Modeled on the structure of jusi-aalto/crossref (a SKILL doc + a bundled .py),
but with NO network: instead of validating references against the Crossref API,
it checks the paper against *itself*.

What it extracts / flags:
  1. Citation coverage   \\cite/\\citep/\\citet/\\citeauthor/\\citealp keys vs the
                          .bib entry keys  ->  cited-but-missing · defined-but-unused
  2. Acronyms            "Full Name (ABC)" definitions vs ABC uses
                          ->  used-before-defined · defined-more-than-once
  3. Notation            symbol/variable definitions ("let X denote", "X is
                          measured as", "we define X")  ->  defined-twice (drift)
  4. Magnitude inventory numeric effect sizes per section (abstract / intro /
                          results)  ->  raw inventory for the model's claim-parity check

Usage:
  consistency_check.py PAPER.tex [--bib refs.bib] [--json]
Exit: always 0 (advisory). Prints a human report, or JSON with --json.
"""
import json
import re
import sys

# ---- citation commands (LaTeX) -------------------------------------------------
# \citet[see][p.4]{key1,key2}  ->  capture the {...} key group, split on commas
CITE_CMD = re.compile(
    r"\\(?:cite|citep|citet|citeauthor|citealp|citealt|citeyear|parencite|"
    r"textcite|footcite|autocite)\*?\s*(?:\[[^\]]*\]\s*){0,2}\{([^}]*)\}")
# a .bib entry head:  @article{Smith2020,
BIB_ENTRY = re.compile(r"@\s*\w+\s*\{\s*([^,\s}]+)\s*,")

# ---- acronyms ------------------------------------------------------------------
# "Public Company Accounting Oversight Board (PCAOB)"  ->  capture PCAOB
ACRONYM_DEF = re.compile(r"\(([A-Z][A-Za-z]*[A-Z][A-Za-z]*s?)\)")
# a standalone acronym token in running text (2+ caps, optional trailing s)
ACRONYM_USE = re.compile(r"(?<![A-Za-z])([A-Z]{2,}[A-Z0-9]*s?)(?![A-Za-z])")
# acronym-like tokens that are not jargon worth tracking
ACRONYM_STOP = {
    "OLS", "GMM", "IV", "FE", "DV", "IV", "SE", "SES", "USA", "US", "UK", "EU",
    "GAAP", "IFRS", "CEO", "CFO", "AND", "THE", "FOR", "NBER", "SSRN", "DOI",
    "PDF", "II", "III", "IV", "VI", "VII", "ROA", "ROE",
}

# ---- notation / variable definitions ------------------------------------------
# "let X denote", "X is defined as", "we define X as", "X is measured as",
# "X equals", "where X is" — capture the defined token (a short symbol/word).
NOTATION_DEF = re.compile(
    r"\b(?:let|where|define|we define|denote(?:s|d)? by)\s+([A-Za-z][A-Za-z0-9_]{0,24})\b"
    r"|\b([A-Za-z][A-Za-z0-9_]{0,24})\s+(?:is|are)\s+(?:defined|measured|"
    r"computed|calculated|given by|equal to|the)\b",
    re.I)

# ---- magnitudes (mirror of check_structure.py MAGNITUDE) ----------------------
MAGNITUDE = re.compile(
    r"\b\d+(?:\.\d+)?\s?(?:percentage points?|percent|pp|standard deviations?|"
    r"s\.?d\.?|basis points?|bps)\b|\b\d+(?:\.\d+)?\s?%",
    re.I)

# ---- section splitting ---------------------------------------------------------
TEX_SECTION = re.compile(r"\\(?:sub)*section\*?\s*\{([^}]*)\}")
MD_SECTION = re.compile(r"(?m)^#{1,3}\s+(.*)$")
TEX_ABSTRACT = re.compile(
    r"\\begin\{abstract\}(.*?)\\end\{abstract\}", re.S | re.I)


def read(path):
    return open(path, encoding="utf-8", errors="replace").read()


def strip_comments(tex):
    # drop LaTeX line comments (unescaped %) so commented-out cites don't count
    out = []
    for ln in tex.splitlines():
        m = re.search(r"(?<!\\)%", ln)
        out.append(ln[:m.start()] if m else ln)
    return "\n".join(out)


def split_sections(text):
    """Return {section_label_lower: section_text}. Best-effort for .tex and .md."""
    sections = {}
    abs_m = TEX_ABSTRACT.search(text)
    if abs_m:
        sections["abstract"] = abs_m.group(1)
    heads = [(m.start(), m.group(1).strip()) for m in TEX_SECTION.finditer(text)]
    if not heads:
        heads = [(m.start(), m.group(1).strip()) for m in MD_SECTION.finditer(text)]
    for i, (pos, label) in enumerate(heads):
        end = heads[i + 1][0] if i + 1 < len(heads) else len(text)
        body_start = text.find("\n", pos)
        sections[label.lower()] = text[body_start if body_start > 0 else pos:end]
    return sections


def cited_keys(text):
    keys = []
    for m in CITE_CMD.finditer(text):
        for k in m.group(1).split(","):
            k = k.strip()
            if k:
                keys.append(k)
    return keys


def find_citation_coverage(text, bib_text):
    cited = cited_keys(text)
    cited_set = set(cited)
    result = {"cited_count": len(cited_set), "bib_keys": 0,
              "cited_but_missing": [], "defined_but_unused": []}
    if bib_text is not None:
        defined = {m.group(1).strip() for m in BIB_ENTRY.finditer(bib_text)}
        result["bib_keys"] = len(defined)
        result["cited_but_missing"] = sorted(cited_set - defined)
        result["defined_but_unused"] = sorted(defined - cited_set)
    return result


def find_acronyms(text):
    defs = {}        # acronym -> first definition char offset
    for m in ACRONYM_DEF.finditer(text):
        a = m.group(1)
        defs.setdefault(a, []).append(m.start())
    first_use = {}
    for m in ACRONYM_USE.finditer(text):
        a = m.group(1)
        if a in ACRONYM_STOP:
            continue
        first_use.setdefault(a, m.start())
    used_before_def = []
    defined_twice = []
    for a, positions in defs.items():
        if len(positions) > 1:
            defined_twice.append(a)
    for a, use_pos in first_use.items():
        if a in defs and use_pos < min(defs[a]):
            used_before_def.append(a)
        # an acronym used 2+ words but NEVER spelled out at all
    never_defined = sorted(
        a for a, _ in first_use.items()
        if a not in defs and sum(1 for _ in re.finditer(rf"\b{re.escape(a)}\b", text)) >= 3)
    return {"defined": sorted(defs), "used_before_defined": sorted(used_before_def),
            "defined_more_than_once": sorted(defined_twice),
            "used_often_never_defined": never_defined}


def find_notation(text):
    defined = {}
    for m in NOTATION_DEF.finditer(text):
        term = (m.group(1) or m.group(2) or "").strip()
        if len(term) < 1:
            continue
        if term.lower() in ("the", "this", "that", "it", "we", "is", "are", "a", "an"):
            continue
        defined.setdefault(term, 0)
        defined[term] += 1
    defined_twice = sorted(t for t, n in defined.items() if n > 1)
    return {"defined_terms": sorted(defined), "defined_multiple_times": defined_twice}


def find_magnitudes(sections):
    inv = {}
    for sec in ("abstract", "introduction", "intro", "results", "the results",
                "empirical results", "main results"):
        for label, body in sections.items():
            if sec in label:
                mags = sorted({m.group(0).strip() for m in MAGNITUDE.finditer(body)})
                if mags:
                    inv.setdefault(label, mags)
    return inv


def run(path, bib_path):
    text = strip_comments(read(path))
    bib_text = read(bib_path) if bib_path else None
    sections = split_sections(text)
    return {
        "manuscript": path,
        "bib": bib_path,
        "sections_detected": sorted(sections),
        "citation_coverage": find_citation_coverage(text, bib_text),
        "acronyms": find_acronyms(text),
        "notation": find_notation(text),
        "magnitude_inventory": find_magnitudes(sections),
    }


def print_report(r):
    p = print
    p(f"consistency_check: {r['manuscript']}"
      + (f"  (bib: {r['bib']})" if r["bib"] else "  (no .bib supplied)"))
    p(f"  sections detected: {', '.join(r['sections_detected']) or '(none)'}")

    cc = r["citation_coverage"]
    p("\n[1] CITATION COVERAGE")
    p(f"  in-text cite keys: {cc['cited_count']}   bib entries: {cc['bib_keys']}")
    if r["bib"] is None:
        p("  (supply --bib refs.bib to check cited-but-missing / defined-but-unused)")
    else:
        miss, unused = cc["cited_but_missing"], cc["defined_but_unused"]
        p(f"  [{'N' if miss else 'Y'}] cited-but-missing from .bib ({len(miss)}): "
          + (", ".join(miss) if miss else "none"))
        p(f"  [{'?' if unused else 'Y'}] defined-but-unused in .bib ({len(unused)}): "
          + (", ".join(unused[:20]) + (" …" if len(unused) > 20 else "")
             if unused else "none"))

    ac = r["acronyms"]
    p("\n[2] ACRONYMS / ABBREVIATIONS")
    p(f"  [{'N' if ac['used_before_defined'] else 'Y'}] used-before-defined: "
      + (", ".join(ac["used_before_defined"]) if ac["used_before_defined"] else "none"))
    p(f"  [{'N' if ac['defined_more_than_once'] else 'Y'}] defined-more-than-once: "
      + (", ".join(ac["defined_more_than_once"]) if ac["defined_more_than_once"] else "none"))
    p(f"  [?] used 3+ times, never spelled out: "
      + (", ".join(ac["used_often_never_defined"]) if ac["used_often_never_defined"] else "none"))

    nt = r["notation"]
    p("\n[3] NOTATION / VARIABLE DEFINITIONS")
    p(f"  [{'N' if nt['defined_multiple_times'] else 'Y'}] terms defined multiple times "
      "(possible drift): "
      + (", ".join(nt["defined_multiple_times"]) if nt["defined_multiple_times"] else "none"))
    p(f"  defined terms inventoried: {len(nt['defined_terms'])}")

    mi = r["magnitude_inventory"]
    p("\n[4] MAGNITUDE INVENTORY (for claim-parity -- model compares across sections)")
    if mi:
        for label, mags in mi.items():
            p(f"  {label}: {', '.join(mags)}")
    else:
        p("  (no abstract/intro/results magnitudes detected)")

    p("\nNote: heuristic + advisory. [N]=worth fixing, [?]=worth a look, [Y]=clean. "
      "The model layers judgement (notation drift, claim parity) on this inventory.")


def main():
    args = sys.argv[1:]
    as_json = False
    bib = None
    if "--json" in args:
        as_json = True
        args.remove("--json")
    if "--bib" in args:
        i = args.index("--bib")
        if i + 1 < len(args):
            bib = args[i + 1]
            args = args[:i] + args[i + 2:]
        else:
            args = args[:i]
    if not args:
        print("usage: consistency_check.py PAPER.tex [--bib refs.bib] [--json]")
        return 0
    result = run(args[0], bib)
    if as_json:
        print(json.dumps(result, indent=2))
    else:
        print_report(result)
    return 0  # advisory: never fails the run


if __name__ == "__main__":
    sys.exit(main())

"""
B1 — extract a target section (intro / hypothesis / results) from an accounting
paper PDF.

Source priority:
  1. Companion `.txt` next to the PDF (same basename) — `paper/*.txt` style
  2. `audit_writing_corpus/txt/<basename>.txt` if PDF lives in audit_writing_corpus/
  3. PyMuPDF text extraction (fitz) as last resort

Section detection (the hard part):
  - Find all numbered top-level headers `N. Title` in the body
  - Match target by case-insensitive substring against a curated title bank
  - For `results`, exclude robustness/sensitivity/additional/conclusion variants
  - Return text between target header and the next numbered header

Usage:
  python scripts/pdf_section_split.py <pdf_path> <intro|hypothesis|results>
  python scripts/pdf_section_split.py <pdf_path> --list-sections
  python scripts/pdf_section_split.py <pdf_path> <section> --with-paragraphs

Exit codes:
  0  section found, text printed to stdout
  1  PDF/text not found
  2  section header not detected (text printed via --list-sections for debug)
  3  PyMuPDF unavailable AND no companion .txt
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Windows default cp936/GBK chokes on Unicode (¶, em-dash, etc.) — force UTF-8
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------------------
# Section title bank (case-insensitive substring match on detected header title)
# ---------------------------------------------------------------------------
SECTION_TITLES: dict[str, list[str]] = {
    "intro": [
        "introduction",
        "motivation",
    ],
    "hypothesis": [
        "hypothes",                       # catches "hypothesis", "hypotheses"
        "theory and hypothes",
        "theoretical framework",
        "theoretical background",
        "theory development",
        "background and hypothes",
        "prior literature",
        "related literature",
        "literature and hypothes",
        "literature review and hypothes",
        "predictions",
        "conceptual framework",
        "research issues",                # TAR-era equivalent (DeFond/Lim/Zang 2016 etc.)
        "research questions",
        "motivation and hypothes",
        "background and research issues",
    ],
    "results": [
        "results",                        # primary
        "main results",
        "empirical results",
        "findings",
        "main findings",
        "main empirical results",
    ],
    "abstract": [
        "abstract",
    ],
    "design": [                           # §3 sample / measures / model
        "research design",
        "empirical design",
        "research method",                # method / methodology / methods
        "data and sample",
        "sample and data",
        "sample selection",
        "sample and variable",
        "sample, data",                   # "Sample, data, and measures" (22-FHKF)
        "sample data",                    # "PCAOB sample data construction ..." (19-Aob)
        "data and variable",              # "Data and Variables" (22-CHLP)
        "setting, data",                  # "Setting, data, and summary statistics" (20-CKMS)
        "data and method",
        "variable measurement",
        "measurement of variable",
        "variable definition",
        "empirical model",
        "model and variable",
        "research model",
    ],
    "robustness": [                       # the inverse of the results-exclude set
        "robustness",
        "sensitivity",
        "additional analys",              # analysis / analyses
        "additional test",
        "supplementary analys",
        "further analys",
        "further test",
        "other analys",
    ],
}

# Headers we EXCLUDE when matching `results` (we want main results, not robustness)
RESULTS_EXCLUDE = [
    "robustness", "sensitivity", "additional", "supplementary",
    "conclusion", "discussion", "implications", "summary",
    "limitations", "extensions",
]
# Per-section exclude lists (first header matching a title and no exclude wins).
SECTION_EXCLUDE: dict[str, list[str]] = {
    "results": RESULTS_EXCLUDE,
    # design: avoid grabbing a later results/robustness header that mentions the model
    "design": ["results", "findings", "robustness", "sensitivity",
               "conclusion", "discussion"],
}


# ---------------------------------------------------------------------------
# Source acquisition
# ---------------------------------------------------------------------------
def find_companion_txt(pdf_path: Path) -> Path | None:
    """Locate the .txt that pairs with the given PDF, trying several locations.

    A pre-cleaned `<stem>.clean.txt` (see scripts/preclean_corpus.py) is preferred
    over the raw `<stem>.txt` so section extraction operates on normalized ASCII.
    """
    # 1. Same dir, cleaned then raw
    clean = pdf_path.with_name(pdf_path.stem + ".clean.txt")
    if clean.exists():
        return clean
    candidate = pdf_path.with_suffix(".txt")
    if candidate.exists():
        return candidate
    # 2. audit_writing_corpus/txt/ if PDF is in audit_writing_corpus/
    if pdf_path.parent.name == "audit_writing_corpus":
        clean_corpus = pdf_path.parent / "txt" / (pdf_path.stem + ".clean.txt")
        if clean_corpus.exists():
            return clean_corpus
        candidate = pdf_path.parent / "txt" / (pdf_path.stem + ".txt")
        if candidate.exists():
            return candidate
    return None


def extract_text_pymupdf(pdf_path: Path) -> str | None:
    try:
        import fitz  # PyMuPDF
    except ImportError:
        return None
    try:
        doc = fitz.open(str(pdf_path))
        return "\n".join(page.get_text() for page in doc)
    except Exception as e:
        print(f"PyMuPDF extraction error: {e}", file=sys.stderr)
        return None


def get_text(pdf_path: Path) -> tuple[str, str]:
    """Return (text, source_label) — companion txt first, else PyMuPDF."""
    txt = find_companion_txt(pdf_path)
    if txt:
        return txt.read_text(encoding="utf-8", errors="replace"), f"txt:{txt.name}"
    extracted = extract_text_pymupdf(pdf_path)
    if extracted is not None:
        return extracted, "pymupdf"
    raise SystemExit(3)


# ---------------------------------------------------------------------------
# Section header detection
# ---------------------------------------------------------------------------
# A "header" line: starts with N. or N (no period, common in some journals);
# followed by a Title-Case phrase 3–80 chars, no period inside.
HEADER_RE = re.compile(
    r"""^\s*
        (?P<num>\d{1,2}|[IVX]{1,5})   # Arabic 1–99 OR Roman I–XX (TAR-style)
        \.?                            # optional period
        \s+
        (?P<title>[A-Z][A-Za-z][A-Za-z0-9 ,\-:;'’!?&/()]{1,78})
        \s*$
    """,
    re.VERBOSE,
)

# Roman numeral → int (covers I–XX, enough for any paper structure)
ROMAN_TO_INT: dict[str, int] = {
    "I": 1,    "II": 2,   "III": 3,  "IV": 4,   "V": 5,
    "VI": 6,   "VII": 7,  "VIII": 8, "IX": 9,   "X": 10,
    "XI": 11,  "XII": 12, "XIII": 13,"XIV": 14, "XV": 15,
    "XVI": 16, "XVII": 17,"XVIII": 18,"XIX": 19,"XX": 20,
}


def num_to_int(s: str) -> int:
    """Convert Arabic or Roman numeral string to int. Returns 0 if unrecognized."""
    if s.isdigit():
        return int(s)
    return ROMAN_TO_INT.get(s.upper(), 0)


def find_headers(text: str) -> list[tuple[int, int, str]]:
    """Return list of (line_index, section_number, title) sorted by line_index.

    Filters out obvious false positives:
      - References / Bibliography / Tables / Figures / Appendix (these are
        usually unnumbered or use letters, but stray matches happen)
      - "Table N. ..." which can look like a section header
      - "Figure N. ..." likewise
    """
    headers: list[tuple[int, int, str]] = []
    for i, line in enumerate(text.split("\n")):
        m = HEADER_RE.match(line)
        if not m:
            continue
        title = m.group("title").strip()
        title_lower = title.lower()
        # Reject false positives
        if title_lower.startswith(("table", "figure", "panel", "appendix")):
            continue
        num = num_to_int(m.group("num"))
        if num == 0 or num > 30:
            continue  # implausible
        headers.append((i, num, title))
    # Keep strictly increasing prefix of section numbers (a paper goes
    # 1→2→3, not 5→1→2 — backward jumps are usually table/figure captions)
    cleaned: list[tuple[int, int, str]] = []
    last_num = 0
    for h in headers:
        if h[1] >= last_num:
            cleaned.append(h)
            last_num = h[1]
    return cleaned


def match_target(headers: list[tuple[int, int, str]], section: str) -> int | None:
    """Return the index into `headers` for the requested section, or None."""
    titles = SECTION_TITLES[section]
    for j, (_, _, title) in enumerate(headers):
        tl = title.lower()
        if not any(s in tl for s in titles):
            continue
        if any(w in tl for w in SECTION_EXCLUDE.get(section, [])):
            continue
        return j
    return None


def extract_section(text: str, section: str) -> tuple[str, str] | None:
    headers = find_headers(text)
    if not headers:
        return None
    j = match_target(headers, section)
    if j is None:
        return None
    lines = text.split("\n")
    start = headers[j][0]
    end = headers[j + 1][0] if j + 1 < len(headers) else len(lines)
    body = "\n".join(lines[start:end])
    label = f"section {headers[j][1]}: {headers[j][2]}"
    return body, label


def split_paragraphs(text: str) -> list[str]:
    """Split section text into paragraphs.

    Heuristic: a paragraph break is a blank line OR a line break followed by
    a capital letter where the previous line ends without sentence terminator.
    For PDF-extracted text, blank-line separation is most reliable; for
    line-wrapped .txt, we fall back to indent-based detection.
    """
    # Normalise excessive whitespace
    blocks = re.split(r"\n\s*\n", text.strip())
    # Drop the header line(s) at top
    if blocks and HEADER_RE.match(blocks[0].split("\n", 1)[0]):
        first = blocks[0].split("\n", 1)
        if len(first) > 1:
            blocks[0] = first[1]
        else:
            blocks = blocks[1:]
    # Re-join hyphenated line wraps within each block
    cleaned = []
    for b in blocks:
        b = re.sub(r"-\n", "", b)
        b = re.sub(r"\n", " ", b)
        b = re.sub(r"\s+", " ", b).strip()
        if len(b) > 30:  # drop tiny fragments (page numbers, etc.)
            cleaned.append(b)
    return cleaned


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf_path", type=Path)
    ap.add_argument("section", nargs="?",
                    choices=["intro", "hypothesis", "results",
                             "abstract", "design", "robustness"])
    ap.add_argument("--list-sections", action="store_true",
                    help="Print all detected section headers and exit")
    ap.add_argument("--with-paragraphs", action="store_true",
                    help="Output as numbered ¶ blocks instead of raw text")
    args = ap.parse_args(argv)

    if not args.pdf_path.exists():
        print(f"ERROR: PDF not found: {args.pdf_path}", file=sys.stderr)
        return 1

    text, source = get_text(args.pdf_path)
    print(f"# source: {source}", file=sys.stderr)

    if args.list_sections:
        for line_i, num, title in find_headers(text):
            print(f"  L{line_i:>5}  §{num:>2}  {title}")
        return 0

    if not args.section:
        ap.error("section required unless --list-sections")

    result = extract_section(text, args.section)
    if result is None:
        print(f"ERROR: '{args.section}' section header not found.", file=sys.stderr)
        print("Detected headers:", file=sys.stderr)
        for line_i, num, title in find_headers(text):
            print(f"  L{line_i}  §{num}  {title}", file=sys.stderr)
        return 2

    body, label = result
    print(f"# {label}", file=sys.stderr)

    if args.with_paragraphs:
        paragraphs = split_paragraphs(body)
        for i, p in enumerate(paragraphs, 1):
            print(f"## ¶{i}")
            print(p)
            print()
    else:
        print(body)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

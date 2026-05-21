#!/usr/bin/env python3
"""Generate Phase-C results-section staging drafts for the audit-write corpus.

This script reads the 16-paper pilot inventory, extracts each paper's results
section, sends the extracted section to an OpenAI-compatible chat-completions
API, writes ``<CODE>_results.md`` staging drafts, and runs the local quote and
style gates. It does not edit accepted pattern files or accept logs.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib import request
from urllib.error import HTTPError, URLError

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


ROOT = Path(__file__).resolve().parents[1]
GOLD_SET = ROOT / "corpus_inventory" / "gold_set_pilot.md"
PAPER_DIR = ROOT / "paper"
TRACK_B_DRAFTS = ROOT / "corpus_inventory" / "track_b_drafts"
STATUS_PATH = TRACK_B_DRAFTS / "_results_batch_status.md"
SECTION_SPLITTER = ROOT / "scripts" / "pdf_section_split.py"
OPENAI_DEFAULT_BASE_URL = "https://api.openai.com/v1"
DEEPSEEK_DEFAULT_BASE_URL = "https://api.deepseek.com/v1"
QWEN_DEFAULT_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"

# Provider abstraction. Each provider maps to its key/base-url/model env vars,
# a default base URL, and a default model. Provider precedence (when neither
# --provider nor AUDIT_RESULTS_PROVIDER is set) follows PROVIDER_ORDER: QWEN is
# preferred when its key is present, then DeepSeek, then OpenAI.
PROVIDER_ORDER = ("qwen", "deepseek", "openai")
PROVIDER_KEY_ENV = {
    "qwen": "QWEN_API_KEY",
    "deepseek": "DEEPSEEK_API_KEY",
    "openai": "OPENAI_API_KEY",
}
PROVIDER_BASE_ENV = {
    "qwen": "QWEN_BASE_URL",
    "deepseek": "DEEPSEEK_BASE_URL",
    "openai": "OPENAI_BASE_URL",
}
PROVIDER_MODEL_ENV = {
    "qwen": "QWEN_MODEL",
    "deepseek": "DEEPSEEK_MODEL",
    "openai": "OPENAI_MODEL",
}
PROVIDER_DEFAULT_BASE = {
    "qwen": QWEN_DEFAULT_BASE_URL,
    "deepseek": DEEPSEEK_DEFAULT_BASE_URL,
    "openai": OPENAI_DEFAULT_BASE_URL,
}
PROVIDER_DEFAULT_MODEL = {
    "qwen": "qwen3.7-max",
    "deepseek": "deepseek-v4-pro",
    "openai": None,
}
RESULTS_PATTERNS = (
    ROOT
    / "audit-write-skills"
    / "plugins"
    / "audit-write"
    / "skills"
    / "audit-write-results"
    / "results_patterns.md"
)
LINT_STYLE = (
    ROOT / "audit-write-skills" / "plugins" / "audit-write" / "scripts" / "lint_style.py"
)
VERIFY_QUOTE = (
    ROOT / "audit-write-skills" / "plugins" / "audit-write" / "scripts" / "verify_quote.py"
)

# Section-parametrized generation. `results` keeps the original behaviour; the
# other sections reuse the same extraction + quote + lint pipeline.
_SKILLS = ROOT / "audit-write-skills" / "plugins" / "audit-write" / "skills"
SECTION_CONFIG: dict[str, dict[str, str]] = {
    "results": {
        "patterns": str(_SKILLS / "audit-write-results" / "results_patterns.md"),
        "moves": ("descriptive statistics, primary/baseline result, economic magnitude "
                  "translation, identification/falsification/placebo, fixed effects or "
                  "alternative measures, cross-section/heterogeneity, mechanism/channel, "
                  "null or mixed-result handling, and section closer"),
    },
    "design": {
        "patterns": str(_SKILLS / "audit-write-design" / "design_patterns.md"),
        "moves": ("the dependent-variable definition + its defense paragraph, the "
                  "independent variable built bottom-up, the numbered baseline equation, "
                  "the control groups (2-4 categorical), and the fixed-effects + clustering "
                  "choices; note when identification machinery (rotation/shock/falsification) "
                  "is deferred OUT of this section to results"),
    },
    "abstract": {
        "patterns": str(_SKILLS / "audit-write-abstract" / "abstract_patterns.md"),
        "moves": ("setup, prediction-with-tension, finding, heterogeneity, "
                  "cost/dark-side, and the Collectively/Overall closer; record that the "
                  "abstract carries ZERO effect-size numbers (sample sizes/years only)"),
    },
    "robustness": {
        "patterns": str(_SKILLS / "audit-write-robustness" / "robustness_patterns.md"),
        "moves": ("the numbered identification battery (e.g. rotation, regulatory shock, "
                  "decomposition, channel test, cross-sectional partition, client FE), "
                  "alternative-specification tests, and falsification/placebo tests"),
    },
}

PDF_READER_CANDIDATES = [
    ROOT
    / "audit-write-skills"
    / "plugins"
    / "audit-write"
    / "skills"
    / "audit-pdf-reader"
    / "audit-pdf-reader.md",
    ROOT
    / "audit-write-skills"
    / "plugins"
    / "audit-write"
    / "skills"
    / "audit-pdf-reader"
    / "SKILL.md",
]

PDF_READER_FALLBACK = """\
Audit-pdf-reader staging contract, distilled from v1.2:
- Write a draft annotated exemplar at corpus_inventory/track_b_drafts/<CODE>_results.md.
- Use short verbatim quotes from the source text; each quote must be directly verifiable.
- Select at least 12 rows.
- For results sections, cover descriptive statistics, primary/baseline result,
  economic magnitude, identification/falsification, cross-section/heterogeneity,
  and mechanism/channel moves when present.
- Each row should include paragraph/block id, quote, move/function, local
  annotation, and confidence.
- Keep annotations as corpus-learning notes, not claims about the user's paper.
- Do not invent hard citations or unsupported numeric magnitudes.
"""

SYSTEM_PROMPT = """\
You are preparing corpus staging notes for the audit-write-results skill.
Your output must be faithful to the supplied paper text. Do not invent quotes,
citations, results, statistics, tables, or section labels. If a move is absent,
say it is absent in reviewer notes rather than fabricating an example.
"""

ROMAN_TO_INT = {
    "I": 1,
    "II": 2,
    "III": 3,
    "IV": 4,
    "V": 5,
    "VI": 6,
    "VII": 7,
    "VIII": 8,
    "IX": 9,
    "X": 10,
    "XI": 11,
    "XII": 12,
    "XIII": 13,
    "XIV": 14,
    "XV": 15,
}

EXT_HEADER_RE = re.compile(
    r"^\s*(?P<num>\d{1,2}|[IVX]{1,5})[\.\)]?\s+(?P<title>[^\n]{3,140})\s*$",
    re.I,
)

SECTIONISH_KEYWORDS = [
    "introduction",
    "background",
    "hypothes",
    "research design",
    "sample",
    "data",
    "measure",
    "descriptive",
    "empirical",
    "results",
    "findings",
    "test",
    "analysis",
    "analyses",
    "audit quality",
    "auditor choice",
    "audit process",
    "competition",
    "social connections",
    "mutual fund",
    "conclusion",
    "additional",
    "further",
    "robustness",
    "sensitivity",
]

RESULTS_START_PHRASES = [
    "results",
    "findings",
    "main results",
    "empirical results",
    "main empirical tests",
    "empirical tests",
    "empirical analysis",
    "empirical analyses",
    "hypotheses tests",
    "hypothesis tests",
    "tests of hypotheses",
    "ai and audit quality",
    "credit market development and auditor choice",
    "social connections and mutual fund stockholdings",
    "audit process efficiency",
]

RESULTS_EXCLUDE_KEYWORDS = [
    "robustness",
    "sensitivity",
    "additional",
    "supplementary",
    "conclusion",
    "discussion",
    "references",
    "appendix",
]


@dataclass
class Paper:
    code: str
    filename: str
    pdf_path: Path | None = None
    txt_path: Path | None = None


@dataclass
class PaperStatus:
    code: str
    pdf: str = ""
    extract: str = "NOT_RUN"
    api: str = "NOT_RUN"
    quote: str = "NOT_RUN"
    lint: str = "NOT_RUN"
    final: str = "NOT_RUN"
    output: str = ""
    notes: list[str] = field(default_factory=list)

    def note(self, text: str) -> None:
        clean = " ".join(str(text).split())
        if clean:
            self.notes.append(clean)


def rel(path: Path | None) -> str:
    if path is None:
        return ""
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def read_text(path: Path, max_chars: int | None = None) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    if max_chars and max_chars > 0 and len(text) > max_chars:
        return (
            text[:max_chars]
            + "\n\n[TRUNCATED BY batch_generate_results_drafts.py at "
            + f"{max_chars} chars]\n"
        )
    return text


def parse_gold_set(path: Path) -> list[Paper]:
    text = read_text(path)
    papers: list[Paper] = []
    seen: set[str] = set()
    row_re = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*`([^`]+\.pdf)`\s*\|\s*$")
    for line in text.splitlines():
        match = row_re.match(line)
        if not match:
            continue
        code, filename = match.groups()
        if code in seen:
            continue
        seen.add(code)
        papers.append(Paper(code=code, filename=filename))
    return papers


def normalized_name(name: str) -> str:
    dash_chars = "\u2010\u2011\u2012\u2013\u2014\u2212"
    out = unicodedata.normalize("NFKC", name).casefold()
    for char in dash_chars:
        out = out.replace(char, "-")
    out = re.sub(r"\s+", " ", out)
    return out.strip()


def filename_tokens(name: str) -> set[str]:
    normalized = normalized_name(Path(name).stem)
    tokens = re.findall(r"[a-z0-9]+", normalized)
    stop = {"the", "and", "of", "in", "from", "with", "to", "a", "an"}
    return {token for token in tokens if len(token) > 1 and token not in stop}


def find_pdf(filename: str) -> Path | None:
    exact = PAPER_DIR / filename
    if exact.exists():
        return exact
    target = normalized_name(filename)
    for candidate in PAPER_DIR.glob("*.pdf"):
        if normalized_name(candidate.name) == target:
            return candidate
    target_tokens = filename_tokens(filename)
    target_years = {token for token in target_tokens if re.fullmatch(r"\d{4}", token)}
    best: tuple[float, Path] | None = None
    for candidate in PAPER_DIR.glob("*.pdf"):
        candidate_tokens = filename_tokens(candidate.name)
        if target_years and not (target_years & candidate_tokens):
            continue
        overlap = len(target_tokens & candidate_tokens)
        denom = max(1, min(len(target_tokens), len(candidate_tokens)))
        score = overlap / denom
        if score >= 0.62 and (best is None or score > best[0]):
            best = (score, candidate)
    if best is not None:
        return best[1]
    return None


def find_txt(pdf_path: Path | None) -> Path | None:
    if pdf_path is None:
        return None
    # Prefer the pre-cleaned ASCII companion when present (see preclean_corpus.py):
    # it feeds both the generation input and the quote-verification corpus, so the
    # model quotes clean ASCII and the gate matches it.
    clean = pdf_path.with_name(f"{pdf_path.stem}.clean.txt")
    if clean.exists():
        return clean
    same_stem = pdf_path.with_suffix(".txt")
    if same_stem.exists():
        return same_stem
    if pdf_path.parent.name == "audit_writing_corpus":
        clean_corpus = pdf_path.parent / "txt" / f"{pdf_path.stem}.clean.txt"
        if clean_corpus.exists():
            return clean_corpus
        candidate = pdf_path.parent / "txt" / f"{pdf_path.stem}.txt"
        if candidate.exists():
            return candidate
    return None


def resolve_sources(papers: list[Paper]) -> None:
    for paper in papers:
        paper.pdf_path = find_pdf(paper.filename)
        paper.txt_path = find_txt(paper.pdf_path)


def filter_papers(papers: list[Paper], only: str | None, limit: int | None) -> list[Paper]:
    selected = papers
    if only:
        wanted = [item.strip() for item in only.split(",") if item.strip()]
        wanted_set = set(wanted)
        selected = [paper for paper in selected if paper.code in wanted_set]
        missing = [code for code in wanted if code not in {paper.code for paper in selected}]
        if missing:
            raise SystemExit(f"--only contains unknown code(s): {', '.join(missing)}")
    if limit is not None:
        selected = selected[:limit]
    return selected


def run_subprocess(args: list[str], timeout: int = 180) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=str(ROOT),
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
    )


def extract_results(pdf_path: Path, timeout: int, section: str = "results") -> tuple[bool, str, str]:
    proc = run_subprocess(
        [
            sys.executable,
            str(SECTION_SPLITTER),
            str(pdf_path),
            section,
            "--with-paragraphs",
        ],
        timeout=timeout,
    )
    details = "\n".join(part for part in [proc.stderr.strip(), proc.stdout[:500].strip()] if part)
    if proc.returncode == 0:
        return True, proc.stdout, details
    # the decimal-multivariate fallback is results-specific; other sections rely on the splitter
    if section != "results":
        return False, proc.stdout, details
    fallback_ok, fallback_text, fallback_detail = fallback_extract_results(pdf_path)
    if fallback_ok:
        combined = "\n".join(
            part
            for part in [
                "primary splitter failed; fallback extractor used",
                fallback_detail,
                details[:700],
            ]
            if part
        )
        return True, fallback_text, combined
    return False, proc.stdout, details


def num_to_int(value: str) -> int:
    if value.isdigit():
        return int(value)
    return ROMAN_TO_INT.get(value.upper(), 0)


def read_source_text(pdf_path: Path) -> tuple[str, str] | None:
    txt_path = find_txt(pdf_path)
    if txt_path is not None:
        return read_text(txt_path), f"txt:{rel(txt_path)}"
    try:
        import fitz  # type: ignore
    except ImportError:
        return None
    try:
        doc = fitz.open(str(pdf_path))
        return "\n".join(page.get_text() for page in doc), "pymupdf"
    except Exception:
        return None


def clean_header_title(title: str) -> str:
    title = re.sub(r"\s+", " ", title).strip()
    return title.rstrip(".")


def looks_like_section_title(title: str) -> bool:
    lower = title.casefold()
    if lower.startswith(("table", "figure", "panel", "appendix")):
        return False
    if len(title.split()) > 16:
        return False
    return any(keyword in lower for keyword in SECTIONISH_KEYWORDS)


def find_extended_headers(text: str) -> list[tuple[int, int, str]]:
    headers: list[tuple[int, int, str]] = []
    for line_index, line in enumerate(text.splitlines()):
        match = EXT_HEADER_RE.match(line)
        if not match:
            continue
        num = num_to_int(match.group("num"))
        if num <= 0 or num > 15:
            continue
        title = clean_header_title(match.group("title"))
        if not looks_like_section_title(title):
            continue
        headers.append((line_index, num, title))
    return headers


def is_results_start(title: str) -> bool:
    lower = re.sub(r"\s+", " ", title.casefold()).strip(" .:-")
    if any(keyword in lower for keyword in RESULTS_EXCLUDE_KEYWORDS):
        return False
    for phrase in RESULTS_START_PHRASES:
        if lower == phrase:
            return True
        if lower.startswith(f"{phrase}:"):
            return True
        if phrase in {"results", "findings"} and lower.startswith(f"{phrase} "):
            return True
        if phrase not in {"results", "findings"} and lower.startswith(f"{phrase} "):
            trailing = lower[len(phrase) + 1 :]
            if len(trailing.split()) <= 6:
                return True
    return False


def is_unnumbered_results_start(title: str) -> bool:
    lower = re.sub(r"\s+", " ", title.casefold()).strip(" .:-")
    if any(keyword in lower for keyword in RESULTS_EXCLUDE_KEYWORDS):
        return False
    strict = {
        "results",
        "findings",
        "main results",
        "empirical results",
        "main empirical tests",
        "empirical tests",
        "empirical analysis",
        "empirical analyses",
        "hypotheses tests",
        "hypothesis tests",
        "tests of hypotheses",
        "ai and audit quality",
        "credit market development and auditor choice",
        "audit process efficiency",
    }
    return lower in strict or any(lower.startswith(f"{phrase}:") for phrase in strict)


def paragraphize(text: str) -> str:
    blocks = re.split(r"\n\s*\n", text.strip())
    paragraphs: list[str] = []
    for block in blocks:
        block = re.sub(r"-\n", "", block)
        block = re.sub(r"\n", " ", block)
        block = re.sub(r"\s+", " ", block).strip()
        if len(block) >= 30:
            paragraphs.append(block)
    return "\n\n".join(f"## P{i}\n{paragraph}" for i, paragraph in enumerate(paragraphs, 1))


def fallback_extract_results(pdf_path: Path) -> tuple[bool, str, str]:
    source = read_source_text(pdf_path)
    if source is None:
        return False, "", "fallback failed: no txt and PyMuPDF unavailable"
    text, source_label = source
    lines = text.splitlines()
    headers = find_extended_headers(text)
    for index, (line_index, _, title) in enumerate(headers):
        if not is_results_start(title):
            continue
        end_line = len(lines)
        for next_line, _, next_title in headers[index + 1 :]:
            if next_line <= line_index:
                continue
            end_line = next_line
            break
        body = "\n".join(lines[line_index:end_line])
        detail = f"fallback source: {source_label}; section: {title}; lines {line_index}-{end_line}"
        return True, paragraphize(body), detail

    decimal_ok, decimal_text, decimal_detail = fallback_decimal_multivariate(text, source_label)
    if decimal_ok:
        return True, decimal_text, decimal_detail

    for line_index, line in enumerate(lines):
        title = clean_header_title(line)
        if not is_unnumbered_results_start(title):
            continue
        end_line = len(lines)
        for later_index in range(line_index + 1, len(lines)):
            later = clean_header_title(lines[later_index])
            if any(keyword in later.casefold() for keyword in RESULTS_EXCLUDE_KEYWORDS):
                end_line = later_index
                break
        body = "\n".join(lines[line_index:end_line])
        detail = f"fallback source: {source_label}; unnumbered start: {title}; lines {line_index}-{end_line}"
        return True, paragraphize(body), detail

    header_summary = "; ".join(f"{num} {title}" for _, num, title in headers[:12])
    return False, "", f"fallback failed: no extended results header found ({header_summary})"


def fallback_decimal_multivariate(text: str, source_label: str) -> tuple[bool, str, str]:
    lines = text.splitlines()
    decimal_re = re.compile(r"^\s*\d{1,2}\.\d{1,2}\.?\s+(?P<title>[^\n]{3,140})\s*$", re.I)
    top_re = re.compile(r"^\s*\d{1,2}\.?\s+(?P<title>[^\n]{3,140})\s*$", re.I)
    for line_index, line in enumerate(lines):
        match = decimal_re.match(line)
        if not match:
            continue
        title = clean_header_title(match.group("title"))
        if not title.casefold().startswith("multivariate analysis"):
            continue
        end_line = len(lines)
        for later_index in range(line_index + 1, len(lines)):
            later_match = top_re.match(lines[later_index])
            if not later_match:
                continue
            later_title = clean_header_title(later_match.group("title")).casefold()
            if later_title.startswith(("conclusion", "references")):
                end_line = later_index
                break
        body = "\n".join(lines[line_index:end_line])
        detail = (
            f"fallback source: {source_label}; decimal multivariate start: "
            f"{title}; lines {line_index}-{end_line}"
        )
        return True, paragraphize(body), detail
    return False, "", "fallback decimal multivariate start not found"


def load_pdf_reader_contract(max_chars: int) -> tuple[str, str]:
    for candidate in PDF_READER_CANDIDATES:
        if candidate.exists():
            return read_text(candidate, max_chars), rel(candidate)
    return PDF_READER_FALLBACK, "fallback:v1.2-distilled-contract"


def build_prompt(
    paper: Paper,
    results_text: str,
    results_patterns: str,
    pdf_reader_contract: str,
    pdf_reader_source: str,
    section: str = "results",
    moves: str | None = None,
) -> str:
    source_txt = rel(paper.txt_path) if paper.txt_path else f"none; quote gate will use extracted {section} text"
    moves = moves or SECTION_CONFIG.get(section, SECTION_CONFIG["results"])["moves"]
    return f"""\
Task: Generate a draft annotated exemplar for audit-write-{section} (Stage-1 distillation).

Paper:
- Code: {paper.code}
- Source PDF: {rel(paper.pdf_path)}
- Source TXT: {source_txt}
- Output file name: corpus_inventory/track_b_drafts/{paper.code}_{section}.md

Required markdown output:
- Title: "# Draft annotated exemplar - {paper.code} / {section} (API draft)"
- Opening italic metadata paragraph with STATUS: DRAFT, Source PDF, Source TXT.
- Section heading: "## Annotated example (draft): <authors/year if inferable> (`{paper.code}`)"
- A markdown table with this exact header:
  | Para | Quote (verbatim, <=25 words) | Block | Move | Annotation | Conf |
- Include at least 12 candidate rows.
- Use ASCII punctuation in your own markup and annotations.
- Each Quote cell must contain one short ASCII straight-double-quoted verbatim
  phrase copied from the supplied extracted {section} section.
- Do not use curly quote delimiters. Use "like this", not curly quotes.
- Cover these move families when present: {moves}.
- After the table, add "## Commentary", "## Self-check log", and
  "## Reviewer notes (for human)".
- The Conf column must use high, medium, or low.
- Each table row must fit on one physical line. Do not put line breaks inside
  quotes or table cells.
- Finish all required sections; do not stop before "## Reviewer notes (for human)".
- Do not use hard citations in annotations, commentary, self-checks, or reviewer
  notes unless copied inside a verbatim quote; use [AUTHOR:] placeholders for any
  annotator-side literature references.
- Do not mention this API prompt.

Audit-pdf-reader contract source: {pdf_reader_source}
{pdf_reader_contract}

Current audit-write-{section} pattern reference:
{results_patterns}

Extracted {section} section for {paper.code}:
<<<SECTION_START
{results_text}
SECTION_END>>>
"""


def chat_completion(
    *,
    base_url: str,
    api_key: str,
    model: str,
    prompt: str,
    temperature: float,
    max_tokens: int,
    timeout: int,
) -> str:
    url = base_url.rstrip("/") + "/chat/completions"
    payload: dict[str, Any] = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    body = json.dumps(payload).encode("utf-8")
    req = request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    try:
        with request.urlopen(req, timeout=timeout) as response:
            raw = response.read().decode("utf-8", errors="replace")
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {detail[:1000]}") from exc
    except URLError as exc:
        raise RuntimeError(f"URL error: {exc}") from exc

    data = json.loads(raw)
    try:
        return data["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(f"Unexpected API response shape: {raw[:1000]}") from exc


def split_md_row(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return []
    cells: list[str] = []
    buf: list[str] = []
    escaped = False
    for char in stripped.strip("|"):
        if escaped:
            buf.append(char)
            escaped = False
            continue
        if char == "\\":
            buf.append(char)
            escaped = True
            continue
        if char == "|":
            cells.append("".join(buf).strip())
            buf = []
            continue
        buf.append(char)
    cells.append("".join(buf).strip())
    return cells


def is_separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def normalize_api_markdown(text: str) -> str:
    """Normalize common model punctuation drift before writing or parsing drafts."""
    replacements = {
        "\u201c": '"',
        "\u201d": '"',
        "\u201e": '"',
        "\u201f": '"',
        "\u2018": "'",
        "\u2019": "'",
        "\u201a": "'",
        "\u201b": "'",
        "\u2013": "-",
        "\u2014": "-",
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2212": "-",  # unicode MINUS SIGN (table coefficients: -0.050)
        "\u00a0": " ",
        "\ufb00": "ff",
        "\ufb01": "fi",
        "\ufb02": "fl",
        "\ufb03": "ffi",
        "\ufb04": "ffl",
        "\ufb05": "ft",
        "\ufb06": "st",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    return text


def repair_mojibake(text: str) -> str:
    """Best-effort recovery for UTF-8 text that was decoded as GBK/CP936."""
    mojibake_markers = ("\u9225", "\u6ded", "\u6a9a")
    if not any(marker in text for marker in mojibake_markers):
        return text
    try:
        repaired = text.encode("gbk", errors="strict").decode("utf-8", errors="strict")
    except UnicodeError:
        return text
    if sum(repaired.count(marker) for marker in mojibake_markers) < sum(
        text.count(marker) for marker in mojibake_markers
    ):
        return repaired
    return text


def extract_quote_cells(markdown: str) -> list[str]:
    markdown = normalize_api_markdown(repair_mojibake(markdown))
    lines = markdown.splitlines()
    quote_idx: int | None = None
    quotes: list[str] = []
    for line in lines:
        cells = split_md_row(line)
        if not cells:
            quote_idx = None
            continue
        lowered = [cell.lower() for cell in cells]
        if any("quote" in cell for cell in lowered):
            quote_idx = next(i for i, cell in enumerate(lowered) if "quote" in cell)
            continue
        if is_separator_row(cells):
            continue
        if quote_idx is None or quote_idx >= len(cells):
            continue
        cell = cells[quote_idx]
        for match in re.finditer(r'"([^"\n]{5,500})"', cell):
            quotes.append(match.group(1).strip())
        if '"' not in cell:
            cleaned = re.sub(r"[*_`]", "", cell).strip()
            if len(cleaned) >= 5:
                quotes.append(cleaned)
    if quotes:
        return dedupe_preserve_order(quotes)

    fallback = [m.group(1).strip() for m in re.finditer(r'"([^"\n]{5,500})"', markdown)]
    return dedupe_preserve_order(fallback)


def draft_contract_errors(markdown: str, min_quotes: int) -> list[str]:
    text = normalize_api_markdown(repair_mojibake(markdown))
    if not text.strip():
        return ["API returned an empty message"]
    errors: list[str] = []
    if "| Para | Quote (verbatim, <=25 words) | Block | Move | Annotation | Conf |" not in text:
        errors.append("missing required table header")
    if "## Commentary" not in text:
        errors.append("missing Commentary section")
    if "## Self-check log" not in text:
        errors.append("missing Self-check log section")
    if "## Reviewer notes (for human)" not in text:
        errors.append("missing Reviewer notes section")
    quotes = extract_quote_cells(text)
    if len(quotes) < min_quotes:
        errors.append(f"only {len(quotes)} quote(s), expected >= {min_quotes}")
    if text.count('"') % 2:
        errors.append("odd number of straight double quotes; likely truncated quote")
    return errors


def dedupe_preserve_order(items: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for item in items:
        key = re.sub(r"\s+", " ", item).strip()
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(key)
    return out


def word_count(text: str) -> int:
    return len(re.findall(r"\S+", text))


def verify_quotes(
    draft_path: Path,
    txt_path: Path | None,
    extracted_results: str,
    min_quotes: int,
    max_quote_words: int,
    timeout: int,
) -> tuple[str, str]:
    markdown = read_text(draft_path)
    quotes = extract_quote_cells(markdown)
    if not quotes:
        return "FAIL", "no quote cells found"

    too_long = [quote for quote in quotes if word_count(quote) > max_quote_words]
    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix="audit_results_quote_gate_") as tmp:
        tmp_dir = Path(tmp)
        corpus_path = txt_path
        if corpus_path is None:
            corpus_path = tmp_dir / "extracted_results.txt"
            corpus_path.write_text(extracted_results, encoding="utf-8")
        for index, quote in enumerate(quotes, 1):
            quote_file = tmp_dir / f"quote_{index:03d}.txt"
            quote_file.write_text(quote, encoding="utf-8")
            proc = run_subprocess(
                [
                    sys.executable,
                    str(VERIFY_QUOTE),
                    str(corpus_path),
                    "--file",
                    str(quote_file),
                ],
                timeout=timeout,
            )
            if proc.returncode != 0:
                failures.append(f"q{index}: {quote[:80]}")

    problems: list[str] = []
    if len(quotes) < min_quotes:
        problems.append(f"only {len(quotes)} quote(s), expected >= {min_quotes}")
    if too_long:
        problems.append(f"{len(too_long)} quote(s) exceed {max_quote_words} words")
    if failures:
        problems.append(f"{len(failures)} quote(s) not found")
    if problems:
        detail = "; ".join(problems)
        if failures:
            detail += f"; first failures: {' | '.join(failures[:3])}"
        return "FAIL", detail
    corpus_label = rel(txt_path) if txt_path else "extracted results text"
    return "OK", f"{len(quotes)}/{len(quotes)} quotes verified against {corpus_label}"


def run_lint(draft_path: Path, timeout: int) -> tuple[str, str]:
    proc = run_subprocess([sys.executable, str(LINT_STYLE), str(draft_path)], timeout=timeout)
    output = "\n".join(part for part in [proc.stdout.strip(), proc.stderr.strip()] if part)
    if proc.returncode == 0:
        return "OK", output.splitlines()[-1] if output else "lint_style OK"
    return "FAIL", output.splitlines()[-1] if output else "lint_style failed"


def render_status(statuses: list[PaperStatus], args: argparse.Namespace) -> str:
    timestamp = dt.datetime.now().isoformat(timespec="seconds")
    lines = [
        "# Results batch status",
        "",
        f"Generated: {timestamp}",
        "",
        f"- Inventory: `{rel(GOLD_SET)}`",
        f"- Provider: `{getattr(args, 'provider', '') or ''}`",
        f"- Model: `{args.model or ''}`",
        f"- Base URL: `{args.base_url or ''}`",
        f"- Dry run: `{bool(args.dry_run)}`",
        f"- Overwrite: `{bool(args.overwrite)}`",
        "",
        "| Code | PDF | Extract | API | Quote | Lint | Final | Output | Notes |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for item in statuses:
        notes = "<br>".join(escape_md(note) for note in item.notes)
        lines.append(
            "| "
            + " | ".join(
                [
                    escape_md(item.code),
                    escape_md(item.pdf),
                    escape_md(item.extract),
                    escape_md(item.api),
                    escape_md(item.quote),
                    escape_md(item.lint),
                    escape_md(item.final),
                    escape_md(item.output),
                    notes,
                ]
            )
            + " |"
        )
    lines.append("")
    return "\n".join(lines)


def escape_md(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def dry_run_report(statuses: list[PaperStatus]) -> str:
    lines = [
        "Code     PDF        TXT        Extract    Notes",
        "-------  ---------  ---------  ---------  -----",
    ]
    for item in statuses:
        notes = "; ".join(item.notes)
        lines.append(
            f"{item.code:<7}  {item.pdf or 'MISSING':<9}  "
            f"{item.quote or '':<9}  {item.extract:<9}  {notes}"
        )
    return "\n".join(lines)


def process_paper(
    paper: Paper,
    args: argparse.Namespace,
    results_patterns: str,
    pdf_reader_contract: str,
    pdf_reader_source: str,
    api_key: str | None,
    base_url: str,
) -> PaperStatus:
    status = PaperStatus(code=paper.code)
    status.pdf = rel(paper.pdf_path) if paper.pdf_path else "MISSING"
    output_path = TRACK_B_DRAFTS / f"{paper.code}_{args.section}.md"
    status.output = rel(output_path)

    if paper.pdf_path is None:
        status.extract = "MISSING_PDF"
        status.final = "FAILED"
        status.note(f"PDF not found for filename: {paper.filename}")
        return status

    if paper.txt_path:
        status.quote = rel(paper.txt_path)
    else:
        status.quote = "NO_TXT"
        status.note("No companion txt; quote gate will use extracted results text.")

    ok, results_text, details = extract_results(paper.pdf_path, args.extract_timeout, args.section)
    if not ok:
        status.extract = "FAIL"
        status.final = "FAILED"
        status.note(details[:500])
        return status
    status.extract = "OK"
    detail_lines = [line for line in details.splitlines() if line.strip()]
    if detail_lines:
        for line in detail_lines[:3 if "fallback extractor used" in details else 1]:
            status.note(line[:500])
    else:
        status.note("results section extracted")

    if args.max_section_chars and args.max_section_chars > 0 and len(results_text) > args.max_section_chars:
        results_text_for_api = (
            results_text[: args.max_section_chars]
            + "\n\n[TRUNCATED BY --max-section-chars]\n"
        )
        status.note(f"results text truncated for API at {args.max_section_chars} chars")
    else:
        results_text_for_api = results_text

    if args.dry_run:
        status.api = "DRY_RUN"
        status.final = "DRY_RUN"
        return status

    if output_path.exists() and not args.overwrite:
        status.api = "SKIP_EXISTING"
        status.note("Output exists; use --overwrite to regenerate.")
    else:
        if not api_key:
            status.api = "FAIL"
            status.final = "FAILED"
            status.note("OPENAI_API_KEY is required when generation is needed.")
            return status
        if not args.model:
            status.api = "FAIL"
            status.final = "FAILED"
            status.note("Model is required via --model or AUDIT_RESULTS_MODEL.")
            return status
        prompt = build_prompt(
            paper=paper,
            results_text=results_text_for_api,
            results_patterns=results_patterns,
            pdf_reader_contract=pdf_reader_contract,
            pdf_reader_source=pdf_reader_source,
            section=args.section,
        )
        content = ""
        last_error = ""
        for attempt in range(1, max(1, args.api_retries + 1) + 1):
            try:
                candidate = chat_completion(
                    base_url=base_url,
                    api_key=api_key,
                    model=args.model,
                    prompt=prompt,
                    temperature=args.temperature,
                    max_tokens=args.max_tokens,
                    timeout=args.api_timeout,
                )
            except Exception as exc:
                last_error = str(exc)[:700]
            else:
                candidate = normalize_api_markdown(candidate)
                contract_errors = draft_contract_errors(candidate, args.min_quotes)
                if not contract_errors:
                    content = candidate
                    break
                last_error = "; ".join(contract_errors)
            if attempt <= args.api_retries and args.sleep_seconds > 0:
                time.sleep(args.sleep_seconds)
        if not content:
            status.api = "FAIL"
            status.final = "FAILED"
            status.note(last_error or "API did not return a usable draft.")
            return status
        TRACK_B_DRAFTS.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content.rstrip() + "\n", encoding="utf-8")
        status.api = "OK"
        status.note(f"API draft written ({len(content)} chars).")
        if args.sleep_seconds > 0:
            time.sleep(args.sleep_seconds)

    if not output_path.exists():
        status.final = "FAILED"
        status.note("No draft file available for gates.")
        return status

    quote_status, quote_detail = verify_quotes(
        draft_path=output_path,
        txt_path=paper.txt_path,
        extracted_results=results_text,
        min_quotes=args.min_quotes,
        max_quote_words=args.max_quote_words,
        timeout=args.gate_timeout,
    )
    status.quote = quote_status
    status.note(quote_detail)

    lint_status, lint_detail = run_lint(output_path, timeout=args.gate_timeout)
    status.lint = lint_status
    status.note(lint_detail)

    status.final = "PASS" if quote_status == "OK" and lint_status == "OK" else "NEEDS_REVIEW"
    return status


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate audit-write results staging drafts from gold_set_pilot.md."
    )
    parser.add_argument(
        "--section",
        choices=sorted(SECTION_CONFIG),
        default="results",
        help="Paper section to distill (default results). Selects the pattern file, the "
             "splitter target, the move-family prompt, and the <CODE>_<section>.md output.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Parse, locate, and extract only.")
    parser.add_argument("--limit", type=int, help="Process only the first N selected papers.")
    parser.add_argument("--only", help="Comma-separated paper codes, e.g. 19-JWW,22-FW.")
    parser.add_argument("--overwrite", action="store_true", help="Regenerate existing drafts.")
    parser.add_argument(
        "--provider",
        choices=sorted(PROVIDER_ORDER),
        default=None,
        help=(
            "API provider. Defaults to AUDIT_RESULTS_PROVIDER, then the first of "
            "qwen/deepseek/openai whose key env var is set (QWEN preferred)."
        ),
    )
    parser.add_argument(
        "--model",
        default=None,
        help=(
            "Model name. Defaults to AUDIT_RESULTS_MODEL, then <PROVIDER>_MODEL, "
            "then the provider default (qwen3.6-plus for QWEN, deepseek-v4-pro for DeepSeek)."
        ),
    )
    parser.add_argument(
        "--base-url",
        default=None,
        help=(
            "OpenAI-compatible API base URL. Defaults to <PROVIDER>_BASE_URL, then "
            "the provider default (DashScope for QWEN, DeepSeek for DeepSeek)."
        ),
    )
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=16384,
        help=(
            "Completion token cap. Default 16384 gives headroom so verbose models "
            "finish the table + required sections instead of truncating mid-output. "
            "qwen3.6-plus typically completes in ~6.5k."
        ),
    )
    parser.add_argument("--pattern-chars", type=int, default=6000)
    parser.add_argument("--reader-chars", type=int, default=2500)
    parser.add_argument(
        "--max-section-chars",
        type=int,
        default=0,
        help="Optional API prompt cap for extracted results text; 0 sends full text.",
    )
    parser.add_argument("--min-quotes", type=int, default=12)
    parser.add_argument("--max-quote-words", type=int, default=25)
    parser.add_argument("--api-timeout", type=int, default=240)
    parser.add_argument("--api-retries", type=int, default=2)
    parser.add_argument("--extract-timeout", type=int, default=180)
    parser.add_argument("--gate-timeout", type=int, default=120)
    parser.add_argument("--sleep-seconds", type=float, default=0)
    return parser


def get_env_var(name: str) -> str | None:
    value = os.environ.get(name)
    if value:
        return value
    if os.name != "nt":
        return None
    try:
        import winreg
    except ImportError:
        return None
    locations = [
        (winreg.HKEY_CURRENT_USER, r"Environment"),
        (
            winreg.HKEY_LOCAL_MACHINE,
            r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment",
        ),
    ]
    for hive, subkey in locations:
        try:
            with winreg.OpenKey(hive, subkey) as key:
                registry_value, _ = winreg.QueryValueEx(key, name)
        except OSError:
            continue
        if registry_value:
            return str(registry_value)
    return None


def resolve_provider(explicit: str | None) -> str | None:
    """Pick the active provider from --provider, AUDIT_RESULTS_PROVIDER, or key presence."""
    choice = explicit or get_env_var("AUDIT_RESULTS_PROVIDER")
    if choice:
        choice = choice.strip().lower()
        if choice not in PROVIDER_KEY_ENV:
            raise SystemExit(
                f"Unknown provider '{choice}'; choose from {', '.join(PROVIDER_ORDER)}"
            )
        return choice
    for provider in PROVIDER_ORDER:
        if get_env_var(PROVIDER_KEY_ENV[provider]):
            return provider
    return None


def resolve_api_key(provider: str | None) -> tuple[str | None, str | None]:
    if provider is None:
        return None, None
    key_name = PROVIDER_KEY_ENV[provider]
    return get_env_var(key_name), key_name


def resolve_base_url(provider: str | None) -> str:
    if provider is None:
        return get_env_var("OPENAI_BASE_URL") or OPENAI_DEFAULT_BASE_URL
    return get_env_var(PROVIDER_BASE_ENV[provider]) or PROVIDER_DEFAULT_BASE[provider]


def resolve_model(provider: str | None) -> str | None:
    audit_results_model = get_env_var("AUDIT_RESULTS_MODEL")
    if audit_results_model:
        return audit_results_model
    if provider is None:
        return None
    provider_model = get_env_var(PROVIDER_MODEL_ENV[provider])
    if provider_model:
        return provider_model
    return PROVIDER_DEFAULT_MODEL[provider]


def main(argv: list[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)

    papers = parse_gold_set(GOLD_SET)
    if len(papers) != 16:
        print(f"ERROR: expected 16 pilot papers, parsed {len(papers)} from {rel(GOLD_SET)}", file=sys.stderr)
        return 2
    if any(paper.code == "22-HS" for paper in papers):
        print("ERROR: parsed deprecated 22-HS from filename table; expected 16-DLLN replacement.", file=sys.stderr)
        return 2
    if not any(paper.code == "16-DLLN" for paper in papers):
        print("ERROR: 16-DLLN replacement is missing from parsed filename table.", file=sys.stderr)
        return 2

    resolve_sources(papers)
    try:
        selected = filter_papers(papers, args.only, args.limit)
    except SystemExit as exc:
        print(str(exc), file=sys.stderr)
        return 2

    results_patterns = read_text(Path(SECTION_CONFIG[args.section]["patterns"]), args.pattern_chars)
    pdf_reader_contract, pdf_reader_source = load_pdf_reader_contract(args.reader_chars)
    status_path = TRACK_B_DRAFTS / f"_{args.section}_batch_status.md"

    try:
        provider = resolve_provider(args.provider)
    except SystemExit as exc:
        print(str(exc), file=sys.stderr)
        return 2
    args.provider = provider
    api_key, api_key_name = resolve_api_key(provider)
    if args.base_url is None:
        args.base_url = resolve_base_url(provider)
    if args.model is None:
        args.model = resolve_model(provider)
    if api_key_name:
        print(
            f"Using provider {provider}; key from {api_key_name}; "
            f"base URL: {args.base_url}; model: {args.model}"
        )

    statuses = [
        process_paper(
            paper=paper,
            args=args,
            results_patterns=results_patterns,
            pdf_reader_contract=pdf_reader_contract,
            pdf_reader_source=pdf_reader_source,
            api_key=api_key,
            base_url=args.base_url,
        )
        for paper in selected
    ]

    if args.dry_run:
        print(dry_run_report(statuses))
    else:
        TRACK_B_DRAFTS.mkdir(parents=True, exist_ok=True)
        status_path.write_text(render_status(statuses, args), encoding="utf-8")
        print(f"Wrote {rel(status_path)}")

    if any(status.final in {"FAILED", "NEEDS_REVIEW"} for status in statuses):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

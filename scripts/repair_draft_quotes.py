#!/usr/bin/env python3
"""repair_draft_quotes.py — option (a) fuzzy-match verbatim repair for staging drafts.

For each Quote-column cell that (i) fails verify_quote (paraphrased/fabricated) or
(ii) exceeds 25 words, find the closest VERBATIM span in the source TXT and
replace the cell with it — but ONLY when the match is confident AND the
replacement itself verifies. Everything else is left untouched and reported as a
residual for a targeted LLM pass (option c). No LLM here — pure deterministic.

Conservative by design: it is better to leave a quote for human/LLM repair than
to substitute a plausible-but-wrong sentence. Auto-replace requires
SequenceMatcher ratio >= --threshold (default 0.72) and a passing re-verify.

Usage:
  repair_draft_quotes.py <section> [codes...] [--threshold 0.72] [--apply]
Without --apply it is a dry run (reports what it would do, writes nothing).
Sections: intro | hypothesis | results
"""
import difflib
import re
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
except Exception:
    pass

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_draft_quotes import find_txt, ALL_CODES, DRAFTS, VERIFY  # reuse mapping

WORD_CAP = 25


def norm(s):
    s = s.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    s = s.replace("—", "-").replace("–", "-")
    s = re.sub(r"-\s*\n\s*", "", s)
    return re.sub(r"\s+", " ", s).strip()


def verify(txt_path, quote):
    r = subprocess.run([sys.executable, str(VERIFY), str(txt_path), quote],
                       capture_output=True, text=True)
    return r.returncode == 0


def sentences(text):
    text = norm(text)
    # split on sentence terminators while keeping reasonable chunks
    parts = re.split(r"(?<=[.;:])\s+", text)
    return [p for p in parts if len(p.split()) >= 4]


def is_clean_span(span):
    """Reject spans unsuitable for a pattern file: control-char corruption,
    leading footnote-number / fragment junk, or starting mid-word (lowercase
    start that is not a legit continuation word)."""
    if any(ord(ch) < 32 and ch not in "\t\n " for ch in span):
        return False  # control-char corruption (e.g. mangled × → \x01)
    if re.match(r"^\(?\d", span):       # leading "(1).24 ..." footnote intrusion
        return False
    if re.match(r"^[a-z]", span) and span.split()[0] not in (
        "we", "our", "the", "this", "that", "these", "those", "a", "an",
        "in", "for", "as", "to", "and", "but", "however", "moreover",
    ):
        return False  # starts mid-sentence on a non-connective lowercase word
    return True


def best_verbatim_span(quote, source_text, source_sents):
    """Return (span, ratio) for the best ≤25-word CLEAN verbatim span matching quote."""
    nq = norm(quote)
    # 1. find the most similar source sentence
    best_sent, best_ratio = None, 0.0
    for s in source_sents:
        r = difflib.SequenceMatcher(None, nq.lower(), s.lower()).ratio()
        if r > best_ratio:
            best_sent, best_ratio = s, r
    if not best_sent:
        return None, 0.0
    words = best_sent.split()
    # 2. if sentence is short enough, use it whole (strip trailing punctuation)
    if len(words) <= WORD_CAP:
        span = best_sent.rstrip(".;:")
        return (span, best_ratio) if is_clean_span(span) else (None, best_ratio)
    # 3. otherwise slide a ≤25-word window, pick the most-similar CLEAN window
    best_win, win_ratio = None, 0.0
    for i in range(0, len(words) - WORD_CAP + 1):
        win = " ".join(words[i:i + WORD_CAP]).rstrip(".;:")
        if not is_clean_span(win):
            continue
        r = difflib.SequenceMatcher(None, nq.lower(), win.lower()).ratio()
        if r > win_ratio:
            best_win, win_ratio = win, r
    return best_win, max(best_ratio if best_win else 0.0, win_ratio)


QUOTE_CELL = re.compile(r"^\|([^|]*)\|([^|]*)\|")


def repair(code, section, threshold, apply):
    draft = DRAFTS / f"{code}_{section}.md"
    if not draft.exists():
        return code, None
    txt = find_txt(code)
    if not txt:
        return code, ("NO_TXT", [], [], [])
    src = txt.read_text(encoding="utf-8", errors="ignore")
    sents = sentences(src)
    lines = draft.read_text(encoding="utf-8").splitlines()
    fixed, residual, ok = [], [], 0
    for li, line in enumerate(lines):
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c for c in s.split("|")]
        # data row has leading '' then ¶, Quote, Block, Move, ...
        if len(cells) < 6:
            continue
        qcell = cells[2].strip()
        q = qcell.strip().strip('"').strip("“”").strip()
        if not q or q.lower().startswith("quote") or set(q) <= {"-", ":", " "}:
            continue
        over = len(q.split()) > WORD_CAP
        good = verify(txt, q)
        if good and not over:
            ok += 1
            continue
        span, ratio = best_verbatim_span(q, src, sents)
        if span and ratio >= threshold and len(span.split()) <= WORD_CAP and verify(txt, span):
            fixed.append((q[:60], span[:60], round(ratio, 2)))
            if apply:
                # replace the quote text inside the cell, preserving surrounding quotes
                new_cell = cells[2].replace(q, span)
                cells[2] = new_cell
                lines[li] = "|".join(cells)
        else:
            residual.append((q[:70], round(ratio, 2), "over25" if over else "notfound"))
    if apply and fixed:
        draft.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return code, ("DONE", fixed, residual, ok)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = [a for a in sys.argv[1:] if a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    section = args[0]
    codes = args[1:] or ALL_CODES
    threshold = 0.72
    for f in flags:
        if f.startswith("--threshold"):
            threshold = float(f.split("=")[1]) if "=" in f else 0.72
    apply = "--apply" in flags
    print(f"section={section} threshold={threshold} apply={apply}\n")
    tot_fixed = tot_resid = 0
    for code in codes:
        c, res = repair(code, section, threshold, apply)
        if res is None:
            print(f"{c}: MISSING")
            continue
        status, fixed, residual, ok = res
        if status == "NO_TXT":
            print(f"{c}: NO_TXT")
            continue
        tot_fixed += len(fixed)
        tot_resid += len(residual)
        print(f"{c}: ok={ok} fixed={len(fixed)} residual={len(residual)}")
        for q, span, r in fixed:
            print(f"   FIX r={r}: {q!r}\n        -> {span!r}")
        for q, r, why in residual:
            print(f"   RESID ({why}) r={r}: {q!r}")
    print(f"\nTOTAL: fixed={tot_fixed} residual={tot_resid}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

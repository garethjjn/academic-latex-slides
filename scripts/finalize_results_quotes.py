#!/usr/bin/env python3
"""finalize_results_quotes.py — option (c) closeout for the results batch.

Applies a small set of human-verified verbatim replacements (recovered by
targeted source grep), then DROPS any annotated-table row whose Quote cell still
fails verify_quote or exceeds 25 words. Dropping an unverifiable row preserves
the no-fabricated-quotes integrity gate — better than substituting a plausible
but wrong sentence. Every drop is logged to stdout.

Usage: finalize_results_quotes.py [--apply]
"""
import re
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
except Exception:
    pass

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_draft_quotes import find_txt, DRAFTS, VERIFY

WORD_CAP = 25

# Human-verified verbatim replacements: code -> [(old_substring, new_verbatim)].
# old_substring is matched within the Quote cell; new_verbatim is confirmed
# present in the source TXT via verify_quote.
REPLACEMENTS = {
    "20-WY": [
        ("level of strictness in audit opinions",
         "strictness level of MAOs issued to the treatment ﬁrms increases by about 6.3%"),
        ("Rich[T, T + 2] in column 3 implies audit fees",
         "column 3 implies audit fees increase by about 8% (=e.077 - 1) during the post-listing period between T and T + 2"),
    ],
    "19-Aob": [
        ("an interquartile range increase",
         "Part I Finding by 0.6%, and that a restatement and small profit increases this probability by 10.1% and 5.0%"),
    ],
    "19-BGH": [
        ("This implies an odds ratio (untabulated) of 0.824",
         "This implies an odds ratio (untabulated) of 0.824, suggesting that a one"),
    ],
    "23-PSZ": [
        ("probability that a company receives a modified audit opinion reduces by 1.7",
         "a 1.7 pp decrease in the probability that a company headquartered in that city receives a MAO"),
    ],
    "20-CKMS": [
        ("misconduct is 43% as important as size in explaining matches",
         "misconduct is 43% as important as size in"),
    ],
    "22-FHKF": [
        ("one-standard-deviation increase in an audit firm",
         "a one-standard-deviation increase in the share of a firm’s AI workers over"),
    ],
}

CODES = ["20-WY", "22-CHLP", "22-Dug", "24-Chen", "19-Aob", "19-BGH",
         "20-CKMS", "23-PSZ", "22-FHKF"]


def verify(txt, q):
    r = subprocess.run([sys.executable, str(VERIFY), str(txt), q],
                       capture_output=True, text=True)
    return r.returncode == 0


def quote_of(cells):
    return cells[2].strip().strip('"').strip("“”").strip()


def main():
    apply = "--apply" in sys.argv
    total_repl = total_drop = 0
    for code in CODES:
        draft = DRAFTS / f"{code}_results.md"
        if not draft.exists():
            print(f"{code}: MISSING")
            continue
        txt = find_txt(code)
        lines = draft.read_text(encoding="utf-8").splitlines()
        repl_map = REPLACEMENTS.get(code, [])
        out, dropped, replaced = [], [], []
        for line in lines:
            s = line.strip()
            if not s.startswith("|") or len(line.split("|")) < 6:
                out.append(line)
                continue
            cells = line.split("|")
            q = quote_of(cells)
            if not q or q.lower().startswith("quote") or set(q) <= {"-", ":", " "}:
                out.append(line)
                continue
            # apply replacement if a mapping matches
            for old_sub, new in repl_map:
                if old_sub in q:
                    cells[2] = cells[2].replace(q, new)
                    line = "|".join(cells)
                    q = new
                    replaced.append(new[:55])
                    break
            # drop if still failing
            if len(q.split()) > WORD_CAP or not verify(txt, q):
                dropped.append(q[:70])
                continue
            out.append(line)
        total_repl += len(replaced)
        total_drop += len(dropped)
        print(f"{code}: replaced={len(replaced)} dropped={len(dropped)}")
        for d in dropped:
            print(f"   DROP: {d}")
        if apply:
            draft.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"\nTOTAL replaced={total_repl} dropped={total_drop} (apply={apply})")
    return 0


if __name__ == "__main__":
    sys.exit(main())

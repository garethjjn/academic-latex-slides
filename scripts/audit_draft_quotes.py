#!/usr/bin/env python3
"""audit_draft_quotes.py — deterministic verbatim-quote audit for staging drafts.

Extracts the Quote column from a draft's annotated table and runs each quote
through verify_quote.py against the paper's source TXT. Reports per-draft
pass/fail counts and flags quotes over the 25-word cap. No LLM — pure check.

Usage:
  audit_draft_quotes.py <section>            # audit all <code>_<section>.md drafts
  audit_draft_quotes.py <section> <code>...  # audit specific codes
Sections: intro | hypothesis | results
Exit: 0 = every audited draft fully clean · 1 = at least one issue
"""
import re
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent
DRAFTS = ROOT / "corpus_inventory" / "track_b_drafts"
PAPER = ROOT / "paper"
VERIFY = ROOT / "audit-write-skills" / "plugins" / "audit-write" / "scripts" / "verify_quote.py"

# Map shorthand -> source TXT filename stem (mirrors gold_set_pilot.md).
FILENAMES = {
    "19-JWW": "2019 - Jiang, Wang, Wang - The Accounting Review - Big N Auditors and Audit Quality New Evidence from Quasi-Experiments",
    "22-LNS": "2022 - Lee, Naiker, Stewart - The Accounting Review - Audit Office Labor Market Proximity and Audit Quality",
    "23-ACN": "2023 - Aobdia, Choudhary, Newberger - The Accounting Review - The Economics of Audit Production What Matters for Audit Quality An Empirical Analysis of the Role",
    "20-WY": "2020 - Wu, Ye - Journal of Accounting Research - Public Attention and Auditor Behavior The Case of Hurun Rich List in China",
    "22-CHLP": "2022 - Chen, Huang, Li, Pittman - Journal of Accounting Research - It's a Small World The Importance of Social Connections with Auditors to Mutual Fund Managers' Port",
    "22-Dug": "2022 - Duguay - Journal of Accounting Research - The Economic Consequences of Financial Audit Regulation in the Charitable Sector",
    "23-ZBLM": "2023 - Zimmerman, Barr‐Pulliam, Lee, Minutti‐Meza - Journal of Accounting Research - Auditors' Use of In‐House Specialists",
    "24-Chen": "2024 - Chen - Journal of Accounting Research - When Employees Go to Court Employee Lawsuits and Talent Acquisition in Audit Offices 3",
    "24-DGZZ": "2024 - De Franco, Guan, Zhou, Zhu - Journal of Accounting Research - The Impact of Credit Market Development on Auditor Choice Evidence from Banking Deregulation",
    "19-Aob": "2019 - Aobdia - Journal of Accounting and Economics - Do Practitioner Assessments Agree with Academic Proxies for Audit Quality Evidence from PCAOB and I",
    "19-BGH": "2019 - Beck, Gunn, Hallman - Journal of Accounting and Economics - The Geographic Decentralization of Audit Firms and Audit Quality",
    "20-CKMS": "2020 - Cook, Kowaleski, Minnis, Sutherland, Zehms - Journal of Accounting and Economics - Auditors Are Known by the Companies They Keep",
    "16-DLLN": "2016 - Dhaliwal, Lamoreaux, Litov, Neyland - Journal of Accounting and Economics - Shared Auditors in Mergers and Acquisitions",
    "23-PSZ": "2023 - Pan, Shroff, Zhang - Journal of Accounting and Economics - The Dark Side of Audit Market Competition",
    "22-FHKF": "2022 - Fedyk, Hodson, Khimich, Fedyk - Review of Accounting Studies - Is Artificial Intelligence Improving the Audit Process",
    "22-FW": "2022 - Fox, Wilson - Review of Accounting Studies - Double Trouble Irs's Attention to Financial Accounting Restatements",
}

ALL_CODES = list(FILENAMES)


# Distinctive glob per code: "YYYY - <FirstSurname>" — handles curly apostrophes
# and Unicode hyphens in the full filename that break exact-string matching.
GLOBS = {
    "19-JWW": "2019 - Jiang*", "22-LNS": "2022 - Lee, Naiker*",
    "23-ACN": "2023 - Aobdia, Choudhary*", "20-WY": "2020 - Wu, Ye*",
    "22-CHLP": "2022 - Chen, Huang*", "22-Dug": "2022 - Duguay*",
    "23-ZBLM": "2023 - Zimmerman*", "24-Chen": "2024 - Chen -*",
    "24-DGZZ": "2024 - De Franco*", "19-Aob": "2019 - Aobdia*",
    "19-BGH": "2019 - Beck*", "20-CKMS": "2020 - Cook*",
    "16-DLLN": "2016 - Dhaliwal*", "23-PSZ": "2023 - Pan, Shroff*",
    "22-FHKF": "2022 - Fedyk*", "22-FW": "2022 - Fox, Wilson*",
}


def find_txt(code):
    """Locate the source TXT for a shorthand, tolerant of hyphen/apostrophe variants."""
    stem = FILENAMES.get(code)
    if stem:
        cand = PAPER / f"{stem}.txt"
        if cand.exists():
            return cand
    pattern = GLOBS.get(code)
    if pattern:
        for p in sorted(PAPER.glob(f"{pattern}.txt")):
            return p
    return None


def extract_quotes(md):
    """Pull the Quote column (2nd cell) from each data row of the annotated table."""
    quotes = []
    for line in md.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 4:
            continue
        q = cells[1]
        if q.lower().startswith("quote") or set(q) <= {"-", ":", " "}:
            continue  # header / separator
        # strip surrounding quotation marks
        q = q.strip().strip('"').strip("“”").strip()
        if q:
            quotes.append(q)
    return quotes


def verify(txt_path, quote):
    r = subprocess.run(
        [sys.executable, str(VERIFY), str(txt_path), quote],
        capture_output=True, text=True,
    )
    return r.returncode == 0


def audit(code, section):
    draft = DRAFTS / f"{code}_{section}.md"
    if not draft.exists():
        return code, None
    txt = find_txt(code)
    if not txt:
        return code, ("NO_TXT", 0, 0, 0, [])
    md = draft.read_text(encoding="utf-8", errors="ignore")
    quotes = extract_quotes(md)
    over = [q for q in quotes if len(q.split()) > 25]
    notfound = [q for q in quotes if not verify(txt, q)]
    status = "CLEAN" if not over and not notfound else "ISSUES"
    return code, (status, len(quotes), len(over), len(notfound), notfound[:3])


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    section = sys.argv[1]
    codes = sys.argv[2:] or ALL_CODES
    any_issue = False
    print(f"{'code':10} {'status':7} {'rows':>4} {'>25w':>4} {'notfnd':>6}")
    for code in codes:
        c, res = audit(code, section)
        if res is None:
            print(f"{c:10} MISSING")
            continue
        status, n, over, nf, samples = res
        if status != "CLEAN":
            any_issue = True
        print(f"{c:10} {status:7} {n:>4} {over:>4} {nf:>6}")
        for s in samples:
            print(f"           ! notfound: {s[:80]}")
    return 1 if any_issue else 0


if __name__ == "__main__":
    sys.exit(main())

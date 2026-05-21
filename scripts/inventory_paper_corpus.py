"""
Phase 0a — read-only inventory of the paper corpus.

Input:  d:/OneDrive/tools/paper/  (flat dir, ~1.4k files, .pdf/.txt, naming
        convention 'YYYY - Authors - Journal - Title.ext' with fallbacks)
Output: d:/OneDrive/tools/corpus_inventory/
          manifest.csv         one row per file
          duplicates.md        within-corpus duplicates (true dupes + companion pairs)
          distribution.md      journal / subfield / year crosstabs + typology gap
          run_log.txt          summary log
"""

from __future__ import annotations

import csv
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
PAPER_DIR = Path("d:/OneDrive/tools/paper")
OUT_DIR = Path("d:/OneDrive/tools/corpus_inventory")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Journal classification (substring match, ordered)
# ---------------------------------------------------------------------------
# (canonical_name, tier, [substring keys to match within filename, case-insensitive])
JOURNALS: list[tuple[str, str, list[str]]] = [
    # Top-3 accounting
    ("The Accounting Review",            "top_acct", ["The Accounting Review", "Accounting Review"]),
    ("Journal of Accounting Research",   "top_acct", ["Journal of Accounting Research"]),
    ("Journal of Accounting and Economics","top_acct", ["Journal of Accounting and Economics"]),
    # Other top accounting / auditing
    ("Review of Accounting Studies",     "top_acct", ["Review of Accounting Studies"]),
    ("Contemporary Accounting Research", "top_acct", ["Contemporary Accounting Research", "Contemporary Accting Res"]),
    ("Accounting Organizations and Society", "top_acct", ["Accounting, Organizations and Society", "Accounting Organizations and Society"]),
    ("Auditing: A Journal of Practice & Theory", "top_acct", ["Auditing A Journal of Practice", "Auditing: A Journal of Practice"]),
    # Top finance
    ("The Journal of Finance",           "top_fin",  ["The Journal of Finance", "Journal of Finance"]),
    ("Journal of Financial Economics",   "top_fin",  ["Journal of Financial Economics"]),
    ("Review of Financial Studies",      "top_fin",  ["Review of Financial Studies"]),
    ("Journal of Financial and Quantitative Analysis", "top_fin", ["Journal of Financial and Quantitative Analysis"]),
    # Top general / methodological
    ("Management Science",               "top_gen",  ["Management Science"]),
    ("American Economic Review",         "top_gen",  ["American Economic Review"]),
    ("Quarterly Journal of Economics",   "top_gen",  ["Quarterly Journal of Economics"]),
    ("Journal of Political Economy",     "top_gen",  ["Journal of Political Economy"]),
    ("Econometrica",                     "top_gen",  ["Econometrica"]),
    # Other accounting / finance
    ("Journal of Accounting Auditing & Finance", "other_acct", ["Journal of Accounting Auditing", "Journal of Accounting, Auditing"]),
    ("Accounting Horizons",              "other_acct", ["Accounting Horizons"]),
    ("Journal of Business Ethics",       "other",      ["Journal of Business Ethics"]),
    ("Journal of Banking and Finance",   "other_fin",  ["Journal of Banking and Finance", "Journal of Banking & Finance"]),
    ("Journal of Corporate Finance",     "other_fin",  ["Journal of Corporate Finance"]),
    ("Annual Review of Financial Economics", "other_fin", ["Annual Review of Financial Economics"]),
    ("Journal of Management Information Systems", "other", ["Journal of Management Information Systems"]),
    ("SSRN Electronic Journal",          "wp",         ["SSRN Electronic Journal"]),
    ("Working Paper",                    "wp",         ["Working Paper", "NBER"]),
]

# ---------------------------------------------------------------------------
# Subfield classification (first-hit-wins by priority order)
# ---------------------------------------------------------------------------
# (subfield, [keywords; matched against title, case-insensitive, word-boundary loose])
SUBFIELDS: list[tuple[str, list[str]]] = [
    ("audit", [
        "auditor", "audit quality", "audit fees", "audit fee", "audit committee",
        "audit partner", "audit firm", "audit office", "audit market", "audit effort",
        "audit report", "auditing", "going concern", "PCAOB", "restatement",
        "internal control", "ICFR", "Big 4", "Big N", "Big Four", "Big-N",
        "engagement risk", "auditors'", "auditors ", "audit ",
    ]),
    ("earnings_mgmt_accruals", [
        "earnings management", "discretionary accrual", "abnormal accrual",
        "accrual quality", "real activities", "real earnings", "earnings quality",
        "income smoothing", "earnings smoothing", "meet or beat",
        "earnings persistence", "earnings predictability",
    ]),
    ("disclosure", [
        "disclosure", "10-K", "10K ", "MD&A", "MD and A", "management discussion",
        "press release", "conference call", "risk factor", "risk disclosure",
        "XBRL", "transparency", "voluntary disclosure", "mandatory disclosure",
        "non-GAAP", "non‐GAAP", "Regulation S-K", "Regulation S‐K", "Reg S-K",
        "narrative", "readability", "tone", "language",
    ]),
    ("analysts", [
        "analyst", "forecast", "recommendation", "sell-side", "buy-side",
    ]),
    ("tax", [
        "tax", " ETR ", "BEPS", "income shifting", "tax avoidance", "tax haven",
        "Country-by-Country", "Country‐by‐Country",
    ]),
    ("fraud_enforcement", [
        "fraud", "AAER", "SEC enforcement", "enforcement action", "misconduct",
        "whistleblow", "SEC ", "regulatory enforcement",
    ]),
    ("credit_ratings", [
        "credit rating", "rating agency", "rating agencies", "S&P", "Moody",
        "issuer-pay", "issuer pay",
    ]),
    ("governance_comp", [
        "CEO ", " CEO", "executive compensation", "executive pay", "compensation",
        "board ", "director", "governance", "ownership", "insider", "shareholder",
        "proxy", "say-on-pay", "incentive", "managerial",
    ]),
    ("mergers_acquisitions", [
        "merger", "acquisition", "takeover", "M&A", "deal ",
    ]),
    ("ipo_seo", [
        "IPO ", " IPO", "going public", "seasoned equity", "SEO ", "underwriter",
    ]),
    ("debt_capital_structure", [
        "leverage", "debt", "bond", "loan", "covenant", "creditor", "lending",
        "capital structure", "zero-leverage",
    ]),
    ("investors_capmkt", [
        "institutional investor", "mutual fund", "hedge fund", "trading",
        "liquidity", "market impact", "asset pricing", "anomaly", "return predictab",
        "investor attention", "stock return",
    ]),
    ("banking", [
        "bank ", "banks ", "banking", "deposit",
    ]),
    ("esg_csr", [
        "CSR", "ESG", "sustainability", "corporate social responsibility",
        "climate", "environmental", "carbon",
    ]),
    ("innovation_rd", [
        "innovation", "R&D", "patent",
    ]),
    ("regulation_law", [
        "regulation", "regulatory", "law and economics", "legal", "litigation",
        "lobby",
    ]),
    ("intl_china", [
        "China", "Chinese", "country-level", "cross-country", "cross country",
        "single-country",
    ]),
]

# ---------------------------------------------------------------------------
# Filename parsing
# ---------------------------------------------------------------------------
# Pattern A:  YYYY - Authors - Journal - Title.ext   (most common)
# Pattern B:  YYYY - Authors - Title.ext             (working paper, no journal)
# Pattern C:  anything else                          (unparseable)
FNAME_A = re.compile(r"^(?P<year>\d{4})\s-\s(?P<authors>.+?)\s-\s(?P<journal>.+?)\s-\s(?P<title>.+)\.(?P<ext>pdf|txt)$",
                     re.IGNORECASE)
FNAME_B = re.compile(r"^(?P<year>\d{4})\s-\s(?P<authors>.+?)\s-\s(?P<title>.+)\.(?P<ext>pdf|txt)$",
                     re.IGNORECASE)


def normalize_title(s: str) -> str:
    """Lower, strip diacritics, collapse non-alnum -> space, single-space."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    # treat unicode dashes, apostrophes uniformly
    s = re.sub(r"[‐‑‒–—―\-]", " ", s)
    s = re.sub(r"[׳''`´’]", "'", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    # strip trailing " 2"/" 3" etc. (filename de-duplication suffixes)
    s = re.sub(r"\s+\d+\s*$", "", s)
    return s.strip()


def classify_journal(journal_str: str, full_filename: str) -> tuple[str, str]:
    """Return (canonical_name, tier). Falls back to ('unknown','unknown')."""
    hay = (journal_str or "") + " || " + full_filename
    hay_l = hay.lower()
    for canon, tier, keys in JOURNALS:
        for k in keys:
            if k.lower() in hay_l:
                return canon, tier
    return ("unknown", "unknown")


def classify_subfield(title: str) -> str:
    """First-hit-wins subfield from title keywords; 'unknown' if none."""
    t = " " + title.lower() + " "
    for sub, keys in SUBFIELDS:
        for k in keys:
            if k.lower() in t:
                return sub
    return "unknown"


def year_bucket(y: int) -> str:
    if y < 2010:    return "pre2010"
    if y < 2015:    return "2010_2014"
    if y < 2020:    return "2015_2019"
    if y < 2025:    return "2020_2024"
    return "2025_2026"


def parse_filename(name: str) -> dict:
    rec = {"filename": name, "year": None, "authors": None, "journal_raw": None,
           "title": None, "ext": None, "parse_ok": False, "pattern": "C"}
    m = FNAME_A.match(name)
    if m:
        rec.update(year=int(m["year"]), authors=m["authors"].strip(),
                   journal_raw=m["journal"].strip(), title=m["title"].strip(),
                   ext=m["ext"].lower(), parse_ok=True, pattern="A")
        return rec
    m = FNAME_B.match(name)
    if m:
        rec.update(year=int(m["year"]), authors=m["authors"].strip(),
                   journal_raw=None, title=m["title"].strip(),
                   ext=m["ext"].lower(), parse_ok=True, pattern="B")
        return rec
    # fallback: try to grab extension at least
    em = re.search(r"\.(pdf|txt)$", name, re.IGNORECASE)
    if em:
        rec["ext"] = em.group(1).lower()
    return rec


# ---------------------------------------------------------------------------
# Walk + build manifest
# ---------------------------------------------------------------------------
def main() -> int:
    files = sorted(p for p in PAPER_DIR.iterdir() if p.is_file())
    records: list[dict] = []
    skipped = []

    for p in files:
        if p.suffix.lower() not in (".pdf", ".txt"):
            skipped.append((p.name, p.suffix))
            continue
        rec = parse_filename(p.name)
        rec["path"] = str(p)
        rec["size_bytes"] = p.stat().st_size
        if rec["parse_ok"]:
            rec["journal_canonical"], rec["journal_tier"] = classify_journal(
                rec["journal_raw"] or "", p.name)
            rec["subfield"] = classify_subfield(rec["title"])
            rec["year_bucket"] = year_bucket(rec["year"])
            rec["norm_key"] = f"{rec['year']}::{normalize_title(rec['title'])}"
        else:
            rec["journal_canonical"] = "unparseable"
            rec["journal_tier"] = "unparseable"
            rec["subfield"] = "unparseable"
            rec["year_bucket"] = "unparseable"
            rec["norm_key"] = f"UNPARSED::{p.stem.lower()}"
        records.append(rec)

    # ----- Manifest CSV -----
    csv_path = OUT_DIR / "manifest.csv"
    cols = ["filename", "ext", "size_bytes", "year", "year_bucket", "authors",
            "journal_raw", "journal_canonical", "journal_tier",
            "title", "subfield", "pattern", "parse_ok", "norm_key", "path"]
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in records:
            w.writerow(r)

    # ----- Duplicate analysis -----
    # 1. companion pairs: same norm_key, different ext (pdf+txt) -> NOT a dup
    # 2. true dups: same (norm_key, ext) -> real duplicate
    # 3. cross-key near-dups (e.g. ' 3' suffix): caught by trailing-digit strip in normalize_title
    by_key_ext: dict[tuple[str, str], list[dict]] = defaultdict(list)
    by_key: dict[str, list[dict]] = defaultdict(list)
    for r in records:
        by_key_ext[(r["norm_key"], r["ext"] or "")].append(r)
        by_key[r["norm_key"]].append(r)

    true_dups = {k: v for k, v in by_key_ext.items() if len(v) > 1}
    companion_pairs = 0
    pdf_only = 0
    txt_only = 0
    both = 0
    for k, group in by_key.items():
        exts = {r["ext"] for r in group}
        if "pdf" in exts and "txt" in exts:
            both += 1
            companion_pairs += 1
        elif "pdf" in exts and "txt" not in exts:
            pdf_only += 1
        elif "txt" in exts and "pdf" not in exts:
            txt_only += 1

    # ----- Distributions -----
    n_total = len(records)
    n_pdf = sum(1 for r in records if r["ext"] == "pdf")
    n_txt = sum(1 for r in records if r["ext"] == "txt")
    n_parse_ok = sum(1 for r in records if r["parse_ok"])
    unique_papers = len(by_key)

    journal_counts = Counter(r["journal_canonical"] for r in records if r["ext"] == "pdf")
    tier_counts = Counter(r["journal_tier"] for r in records if r["ext"] == "pdf")
    subfield_counts = Counter(r["subfield"] for r in records if r["ext"] == "pdf")
    year_counts = Counter(r["year_bucket"] for r in records if r["ext"] == "pdf")

    # journal x period crosstab (top accounting only)
    top_acct_journals = [
        "The Accounting Review", "Journal of Accounting Research",
        "Journal of Accounting and Economics", "Review of Accounting Studies",
        "Contemporary Accounting Research",
        "Auditing: A Journal of Practice & Theory",
    ]
    crosstab_jp: dict[tuple[str, str], int] = defaultdict(int)
    for r in records:
        if r["ext"] != "pdf":
            continue
        if r["journal_canonical"] in top_acct_journals:
            crosstab_jp[(r["journal_canonical"], r["year_bucket"])] += 1

    # subfield x tier crosstab
    crosstab_st: dict[tuple[str, str], int] = defaultdict(int)
    for r in records:
        if r["ext"] != "pdf":
            continue
        crosstab_st[(r["subfield"], r["journal_tier"])] += 1

    # ----- duplicates.md -----
    dup_path = OUT_DIR / "duplicates.md"
    with dup_path.open("w", encoding="utf-8") as f:
        f.write(f"# Duplicates report\n\n")
        f.write(f"- True same-extension duplicates: **{len(true_dups)} groups**, "
                f"{sum(len(v) for v in true_dups.values()) - len(true_dups)} redundant files\n")
        f.write(f"- PDF+TXT companion pairs (one logical paper, two files): **{companion_pairs}**\n")
        f.write(f"- PDF without TXT companion: {pdf_only}\n")
        f.write(f"- TXT without PDF companion: {txt_only}\n")
        f.write(f"- Logical papers (unique norm_key): **{unique_papers}**\n\n")
        if true_dups:
            f.write("## True duplicate groups (same paper, same extension, multiple files)\n\n")
            for (k, ext), group in sorted(true_dups.items(), key=lambda kv: -len(kv[1])):
                f.write(f"### {k} [{ext}]  ({len(group)} files)\n")
                for r in group:
                    f.write(f"- {r['filename']}  ({r['size_bytes']:,} B)\n")
                f.write("\n")
        else:
            f.write("\n_No same-extension true duplicates detected._\n")

    # ----- distribution.md -----
    dist_path = OUT_DIR / "distribution.md"
    with dist_path.open("w", encoding="utf-8") as f:
        f.write("# Paper-corpus distribution report (Phase 0a inventory)\n\n")
        f.write(f"_Source:_ `{PAPER_DIR}`  ·  _Generated by_ `scripts/inventory_paper_corpus.py`\n\n")
        f.write("## 1. Headline counts\n\n")
        f.write(f"- Total files: **{n_total}**  (pdf: {n_pdf}, txt: {n_txt})\n")
        f.write(f"- Filename parse success: **{n_parse_ok}/{n_total}** "
                f"({100*n_parse_ok/n_total:.1f}%)\n")
        f.write(f"- Logical papers (unique year+normalized-title): **{unique_papers}**\n")
        f.write(f"- PDF+TXT companion pairs: {companion_pairs}\n")
        f.write(f"- PDF-only (no extracted txt): {pdf_only}\n")
        f.write(f"- TXT-only (no source pdf): {txt_only}\n\n")

        f.write("## 2. Journal tier (PDFs only)\n\n")
        f.write("| Tier | Count | % of PDFs |\n|---|---|---|\n")
        for tier, c in tier_counts.most_common():
            f.write(f"| {tier} | {c} | {100*c/n_pdf:.1f}% |\n")

        f.write("\n## 3. Journal (PDFs only, sorted by count)\n\n")
        f.write("| Journal | Count |\n|---|---|\n")
        for j, c in journal_counts.most_common():
            f.write(f"| {j} | {c} |\n")

        f.write("\n## 4. Subfield distribution (PDFs only)\n\n")
        f.write("| Subfield | Count | % of PDFs |\n|---|---|---|\n")
        for s, c in subfield_counts.most_common():
            f.write(f"| {s} | {c} | {100*c/n_pdf:.1f}% |\n")

        f.write("\n## 5. Year bucket (PDFs only)\n\n")
        f.write("| Bucket | Count |\n|---|---|\n")
        for y in ["pre2010", "2010_2014", "2015_2019", "2020_2024", "2025_2026", "unparseable"]:
            if year_counts.get(y):
                f.write(f"| {y} | {year_counts[y]} |\n")

        f.write("\n## 6. Top-accounting journal × period (PDFs only)\n\n")
        periods = ["2010_2014", "2015_2019", "2020_2024", "2025_2026"]
        f.write("| Journal | " + " | ".join(periods) + " | Total |\n")
        f.write("|---|" + "|".join(["---"] * (len(periods) + 1)) + "|\n")
        for j in top_acct_journals:
            row = [crosstab_jp[(j, p)] for p in periods]
            f.write(f"| {j} | " + " | ".join(str(x) for x in row) + f" | **{sum(row)}** |\n")

        f.write("\n## 7. Subfield × tier (PDFs only) — typology view\n\n")
        tiers = ["top_acct", "top_fin", "top_gen", "other_acct", "other_fin", "other", "wp", "unknown"]
        f.write("| Subfield | " + " | ".join(tiers) + " | Total |\n")
        f.write("|---|" + "|".join(["---"] * (len(tiers) + 1)) + "|\n")
        for s, _ in subfield_counts.most_common():
            row = [crosstab_st[(s, t)] for t in tiers]
            f.write(f"| {s} | " + " | ".join(str(x) for x in row) + f" | **{sum(row)}** |\n")

        f.write("\n## 8. Typology gap vs existing 6-paper corpus (`corpus_manifest.md`)\n\n")
        f.write("The existing distilled corpus covers 6 audit-only exemplars "
                "(07-DHT, 16-DLZ, 24-DHXZ, 24-DLWW, 25-DQSZ, 26-KLYY). "
                "Cells the new corpus can fill:\n\n")
        gap_cells = [
            ("audit",                  "top_acct"),
            ("audit",                  "other_acct"),  # AJPT
            ("earnings_mgmt_accruals", "top_acct"),
            ("disclosure",             "top_acct"),
            ("analysts",               "top_acct"),
            ("tax",                    "top_acct"),
            ("fraud_enforcement",      "top_acct"),
            ("esg_csr",                "top_acct"),
        ]
        f.write("| Cell | Count in new corpus | Existing 6-paper coverage |\n|---|---|---|\n")
        existing = {
            ("audit", "top_acct"): "6/6 (all current exemplars)",
            ("audit", "other_acct"): "0/6 — AJPT/fee gap",
            ("earnings_mgmt_accruals", "top_acct"): "0/6",
            ("disclosure", "top_acct"): "0/6",
            ("analysts", "top_acct"): "0/6",
            ("tax", "top_acct"): "0/6",
            ("fraud_enforcement", "top_acct"): "0/6",
            ("esg_csr", "top_acct"): "0/6",
        }
        for cell in gap_cells:
            f.write(f"| {cell[0]} × {cell[1]} | {crosstab_st[cell]} | {existing.get(cell,'-')} |\n")

        f.write("\n## 9. Skipped (non pdf/txt)\n\n")
        if skipped:
            for n, ext in skipped:
                f.write(f"- {n}  (`{ext}`)\n")
        else:
            f.write("_None._\n")

    # ----- run_log -----
    log_path = OUT_DIR / "run_log.txt"
    with log_path.open("w", encoding="utf-8") as f:
        f.write(f"files_seen={n_total}\npdf={n_pdf}\ntxt={n_txt}\n"
                f"parse_ok={n_parse_ok}\nunique_papers={unique_papers}\n"
                f"true_dup_groups={len(true_dups)}\n"
                f"companion_pairs={companion_pairs}\npdf_only={pdf_only}\ntxt_only={txt_only}\n")

    print(f"OK  files={n_total}  pdf={n_pdf}  txt={n_txt}  unique={unique_papers}  "
          f"true_dups={len(true_dups)}  companions={companion_pairs}")
    print(f"out: {OUT_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

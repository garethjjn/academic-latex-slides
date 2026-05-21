"""
Parse Zotero raw markdown dumps → structured records → cross-reference with
paper/manifest.csv.

Inputs:
  corpus_inventory/zotero_raw/integrity_propaganda_audit.md   (full summary, 98 items)
  corpus_inventory/zotero_raw/english_first100.md             (keys+title, partial, 100/454)
  corpus_inventory/manifest.csv                                (paper/ corpus, 1389 files)

Outputs:
  corpus_inventory/zotero_inventory.csv         every Zotero record + classification + match
  corpus_inventory/zotero_x_paper.md            gap analysis: in-both / Zotero-only / paper-only
  corpus_inventory/extraction_recommendation.md prioritized action list for Stage 1
"""

from __future__ import annotations

import csv
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path("d:/OneDrive/tools")
RAW_DIR = ROOT / "corpus_inventory" / "zotero_raw"
OUT_DIR = ROOT / "corpus_inventory"
PAPER_MANIFEST = OUT_DIR / "manifest.csv"

# ---------------------------------------------------------------------------
# Title / subfield helpers — kept locally to avoid cross-script imports
# ---------------------------------------------------------------------------
def normalize_title(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r"[‐‑‒–—―\-]", " ", s)
    s = re.sub(r"[׳''`´’]", "'", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = re.sub(r"\s+\d+\s*$", "", s)
    return s.strip()


SUBFIELDS: list[tuple[str, list[str]]] = [
    ("audit", ["auditor", "audit quality", "audit fees", "audit fee",
               "audit committee", "audit partner", "audit firm", "audit office",
               "audit market", "audit effort", "audit report", "auditing",
               "going concern", "pcaob", "restatement", "internal control",
               "icfr", "big 4", "big n", "big four", "engagement risk",
               "auditors", "audit ", " audit"]),
    ("earnings_mgmt_accruals", ["earnings management", "discretionary accrual",
        "abnormal accrual", "accrual quality", "real activities", "real earnings",
        "earnings quality", "income smoothing", "earnings smoothing"]),
    ("disclosure", ["disclosure", "10-k", "md&a", "press release",
        "conference call", "risk factor", "risk disclosure", "xbrl",
        "transparency", "voluntary disclosure", "mandatory disclosure",
        "non-gaap", "regulation s-k", "narrative", "readability", "tone"]),
    ("analysts", ["analyst", "forecast", "recommendation"]),
    ("tax", ["tax", " etr ", "beps", "income shifting", "tax avoidance",
             "tax haven", "country by country"]),
    ("fraud_enforcement", ["fraud", "aaer", "sec enforcement",
        "enforcement action", "misconduct", "whistleblow", "regulatory enforcement"]),
    ("credit_ratings", ["credit rating", "rating agency", "rating agencies",
        "moody", "s&p", "issuer-pay", "issuer pay"]),
    ("governance_comp", ["ceo ", " ceo", "executive compensation", "executive pay",
        "compensation", "board ", "director", "governance", "ownership",
        "insider", "shareholder", "proxy", "say-on-pay"]),
    ("mergers_acquisitions", ["merger", "acquisition", "takeover", "m&a"]),
    ("ipo_seo", ["ipo ", " ipo", "going public", "seasoned equity"]),
    ("debt_capital_structure", ["leverage", "debt", "bond", "loan", "covenant",
        "creditor", "lending", "capital structure", "zero-leverage"]),
    ("investors_capmkt", ["institutional investor", "mutual fund", "hedge fund",
        "trading", "liquidity", "market impact", "asset pricing", "anomaly",
        "return predictab", "investor attention", "stock return"]),
    ("banking", ["bank ", "banks ", "banking", "deposit"]),
    ("esg_csr", ["csr", "esg", "sustainability", "corporate social responsibility",
        "climate", "environmental", "carbon"]),
    ("innovation_rd", ["innovation", "r&d", "patent"]),
    ("regulation_law", ["regulation", "regulatory", "law and economics", "legal",
        "litigation", "lobby"]),
    ("methodology",         # NEW: methodological / econometrics papers
     ["fixed effects models", "difference-in-differences", "diff-in-diff",
      "staggered", "propensity score", "entropy balanc", "coarsened exact",
      "bartik", "instrumental variable", "regression discontinuity",
      "causal inference", "matching estimator"]),
    ("culture_propaganda",  # NEW: integrity/propaganda/culture cluster (user's other project)
     ["propaganda", "communist", "trust", "cultural", "culture", "ideology",
      "media bias", "soulstealers", "guerrilla", "nazis", "rwandan"]),
    ("institutions_econ",   # NEW: foundational/institutional econ refs
     ["coase", "nature of the firm", "institutions", "social capital",
      "nature loving", "agency problems", "watts and zimmerman", "gifts and exchanges",
      "economic institutions of capitalism", "federalism"]),
    ("healthcare",          # NEW: healthcare operations (user's other project)
     ["hospital", "medicare", "physician", "aco", "balloon", "readmission",
      "affordable care", "clinical", "patient"]),
]


def classify_subfield(title: str) -> str:
    t = " " + title.lower() + " "
    for sub, keys in SUBFIELDS:
        for k in keys:
            if k.lower() in t:
                return sub
    return "unknown"


def year_from_date(d: str | None) -> int | None:
    if not d:
        return None
    m = re.search(r"(19|20)\d{2}", d)
    return int(m.group(0)) if m else None


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------
def parse_summary_md(path: Path) -> list[dict]:
    """Parse `## N. Title` blocks from a summary-detail collection dump."""
    text = path.read_text(encoding="utf-8")
    blocks = re.split(r"\n##\s+\d+\.\s+", text)
    records: list[dict] = []
    for block in blocks[1:]:  # first is header
        first_nl = block.find("\n")
        title = block[:first_nl].strip() if first_nl >= 0 else block.strip()
        def field(name: str) -> str | None:
            m = re.search(rf"\*\*{name}:\*\*\s*(.+)", block)
            return m.group(1).strip() if m else None
        key = field("Item Key")
        date = field("Date")
        authors = field("Authors")
        type_ = field("Type")
        attach = field("Attachments")
        tags_raw = field("Tags")
        has_pdf = bool(attach and "PDF" in attach)
        tags = [t.strip() for t in tags_raw.split(";")] if tags_raw else []
        records.append({
            "item_key": key, "title": title, "date": date,
            "year": year_from_date(date), "authors": authors, "type": type_,
            "has_pdf": has_pdf, "tags": tags,
            "norm_title": normalize_title(title),
            "subfield": classify_subfield(title),
            "source_collection": "integrity_propaganda_audit",
        })
    return records


def parse_keys_md(path: Path) -> list[dict]:
    """Parse the `- KEY | Title (Date) [PDF]` lines from a keys_only dump."""
    text = path.read_text(encoding="utf-8")
    pat = re.compile(r"^\-\s+`(?P<key>[A-Z0-9]+)`\s*\|\s*(?P<title>.+?)\s*\((?P<date>[^)]*)\)\s*(?P<extras>\[.*\])?\s*$", re.MULTILINE)
    records: list[dict] = []
    for m in pat.finditer(text):
        title = m.group("title").strip()
        date = m.group("date").strip()
        extras = m.group("extras") or ""
        records.append({
            "item_key": m.group("key"), "title": title, "date": date,
            "year": year_from_date(date), "authors": None, "type": None,
            "has_pdf": "PDF" in extras, "tags": [],
            "norm_title": normalize_title(title),
            "subfield": classify_subfield(title),
            "source_collection": "english",
        })
    return records


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------
def main() -> int:
    audit_recs = parse_summary_md(RAW_DIR / "integrity_propaganda_audit.md")
    english_recs = parse_keys_md(RAW_DIR / "english_first100.md")

    # Merge by item_key (audit-collection rows are richer, prefer them)
    by_key: dict[str, dict] = {}
    for r in audit_recs:
        by_key[r["item_key"]] = r
    overlap = 0
    for r in english_recs:
        if r["item_key"] in by_key:
            by_key[r["item_key"]]["source_collection"] = "both"
            overlap += 1
        else:
            by_key[r["item_key"]] = r

    zotero_recs = list(by_key.values())

    # ----- Cross-ref with paper/ manifest -----
    paper_rows = list(csv.DictReader(open(PAPER_MANIFEST, encoding="utf-8")))
    # one row per logical paper (drop txt companions; keep pdf)
    paper_by_normkey: dict[str, dict] = {}
    for r in paper_rows:
        if r["ext"] != "pdf":
            continue
        # build a (year, norm_title) key parallel to Zotero
        norm = r["norm_key"].split("::", 1)[1] if "::" in r["norm_key"] else r["norm_key"]
        year = r["year"]
        key = f"{year}::{norm}"
        paper_by_normkey.setdefault(key, r)

    # Pre-index paper titles per year for fast prefix-match fallback
    paper_titles_by_year: dict[str, list[tuple[str, dict]]] = defaultdict(list)
    for k, pr in paper_by_normkey.items():
        y, t = k.split("::", 1)
        paper_titles_by_year[y].append((t, pr))

    def prefix_match(zot_title: str, paper_title: str, min_ratio: float = 0.5) -> bool:
        """Either title is a prefix of the other, with shorter ≥ ratio of longer."""
        if not zot_title or not paper_title:
            return False
        a, b = sorted([zot_title, paper_title], key=len)
        if not b.startswith(a):
            return False
        return len(a) / len(b) >= min_ratio

    # match Zotero -> paper
    for r in zotero_recs:
        candidates = []
        if r["year"]:
            k = f"{r['year']}::{r['norm_title']}"
            if k in paper_by_normkey:
                candidates.append((k, paper_by_normkey[k], "exact_year_title"))
        # prefix-match fallback within same year (handles Windows-truncated filenames)
        if not candidates and r["year"]:
            for ptitle, pr in paper_titles_by_year.get(str(r["year"]), []):
                if prefix_match(r["norm_title"], ptitle):
                    candidates.append((f"{r['year']}::{ptitle}", pr,
                                       "prefix_year_title"))
                    break
        # year ± 1 fallback + prefix
        if not candidates and r["year"]:
            for dy in (-1, 1):
                y = str(r["year"] + dy)
                k = f"{y}::{r['norm_title']}"
                if k in paper_by_normkey:
                    candidates.append((k, paper_by_normkey[k], f"year{dy:+d}_title"))
                    break
                for ptitle, pr in paper_titles_by_year.get(y, []):
                    if prefix_match(r["norm_title"], ptitle):
                        candidates.append((f"{y}::{ptitle}", pr,
                                           f"year{dy:+d}_prefix"))
                        break
                if candidates:
                    break
        # title-only loose match (any year)
        if not candidates:
            for pk, pr in paper_by_normkey.items():
                _, ptitle = pk.split("::", 1)
                if r["norm_title"] and prefix_match(r["norm_title"], ptitle, 0.7):
                    candidates.append((pk, pr, "title_only_prefix"))
                    break
        if candidates:
            r["paper_match"] = candidates[0][2]
            r["paper_filename"] = candidates[0][1]["filename"]
            r["paper_journal"] = candidates[0][1]["journal_canonical"]
            r["paper_tier"] = candidates[0][1]["journal_tier"]
        else:
            r["paper_match"] = "none"
            r["paper_filename"] = ""
            r["paper_journal"] = ""
            r["paper_tier"] = ""

    # reverse: paper records not in Zotero
    zotero_normkeys = {f"{r['year']}::{r['norm_title']}" for r in zotero_recs if r["year"]}
    paper_only: list[dict] = []
    for k, pr in paper_by_normkey.items():
        if k not in zotero_normkeys:
            paper_only.append(pr)

    # ----- Save zotero_inventory.csv -----
    out_csv = OUT_DIR / "zotero_inventory.csv"
    cols = ["item_key", "year", "authors", "title", "type", "has_pdf",
            "subfield", "source_collection",
            "paper_match", "paper_filename", "paper_journal", "paper_tier",
            "date", "tags_count"]
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in sorted(zotero_recs, key=lambda x: (-(x["year"] or 0), x["title"])):
            row = {**r, "tags_count": len(r["tags"])}
            w.writerow(row)

    # ----- Compose cross-ref markdown -----
    n_zot = len(zotero_recs)
    n_audit_collection = len(audit_recs)
    n_english_only = sum(1 for r in zotero_recs if r["source_collection"] == "english")
    n_both = sum(1 for r in zotero_recs if r["source_collection"] == "both")
    n_audit_only = sum(1 for r in zotero_recs if r["source_collection"] == "integrity_propaganda_audit")
    n_matched = sum(1 for r in zotero_recs if r["paper_match"] != "none")
    n_zot_audit = sum(1 for r in zotero_recs if r["subfield"] == "audit")
    n_zot_audit_with_pdf = sum(1 for r in zotero_recs if r["subfield"] == "audit" and r["has_pdf"])
    n_zot_audit_matched = sum(1 for r in zotero_recs if r["subfield"] == "audit" and r["paper_match"] != "none")

    # subfield distribution in Zotero
    sub_dist = defaultdict(int)
    for r in zotero_recs:
        sub_dist[r["subfield"]] += 1

    xref_path = OUT_DIR / "zotero_x_paper.md"
    with xref_path.open("w", encoding="utf-8") as f:
        f.write("# Zotero × paper/ cross-reference\n\n")
        f.write("## 1. Headline\n\n")
        f.write(f"- Zotero items parsed (English-relevant subset): **{n_zot}** unique items\n")
        f.write(f"  - From `integrity_propaganda_audit` collection (98 items): {n_audit_only + n_both} surfaced\n")
        f.write(f"  - From `english` collection (only first 100 of 454 retrievable): {n_english_only + n_both} surfaced\n")
        f.write(f"  - In both collections: {n_both}\n")
        f.write(f"  - **Not yet scanned**: 354 items in `english` beyond the 100-cap\n")
        f.write(f"  - `chinese_articles` (101 items): skipped per English-only scope\n\n")
        f.write(f"- Matched to `paper/` corpus: **{n_matched}/{n_zot}** ({100*n_matched/n_zot:.0f}%)\n\n")

        f.write("## 2. Zotero subfield distribution\n\n")
        f.write("| Subfield | Count |\n|---|---|\n")
        for s, c in sorted(sub_dist.items(), key=lambda kv: -kv[1]):
            f.write(f"| {s} | {c} |\n")

        f.write("\n## 3. Audit slice — the priority slice for Stage 1\n\n")
        f.write(f"- Audit-classified Zotero items: **{n_zot_audit}**\n")
        f.write(f"  - With PDF attached in Zotero: **{n_zot_audit_with_pdf}**\n")
        f.write(f"  - Already in `paper/`: **{n_zot_audit_matched}**\n")
        f.write(f"  - In Zotero only (need to verify PDF / consider importing PDF to paper/): "
                f"**{n_zot_audit - n_zot_audit_matched}**\n\n")

        # Zotero audit items not in paper/
        f.write("### 3a. Audit items in Zotero NOT in paper/\n\n")
        f.write("These are candidates to (i) confirm have PDF attached, (ii) potentially import the PDF into paper/.\n\n")
        for r in sorted(zotero_recs, key=lambda x: -(x["year"] or 0)):
            if r["subfield"] != "audit" or r["paper_match"] != "none":
                continue
            pdf_flag = "✓PDF" if r["has_pdf"] else "✗no-PDF"
            f.write(f"- **{r['year'] or '?'}** — _{r['title']}_  ·  {pdf_flag}  ·  `{r['item_key']}`\n")
            if r["authors"]:
                f.write(f"   {r['authors']}\n")

        # Methodological refs (always useful for Stage 1)
        method_recs = [r for r in zotero_recs if r["subfield"] == "methodology"]
        f.write("\n### 3b. Methodological references in Zotero (always useful for Stage 1 design/identification)\n\n")
        for r in sorted(method_recs, key=lambda x: -(x["year"] or 0)):
            pdf_flag = "✓PDF" if r["has_pdf"] else "✗no-PDF"
            match = "✓in-paper/" if r["paper_match"] != "none" else "✗paper-only"
            f.write(f"- **{r['year'] or '?'}** — _{r['title']}_  ·  {pdf_flag}  ·  {match}  ·  `{r['item_key']}`\n")

        # Foundational survey refs (DeFond/Zhang 2014, Aobdia 2019, Lennox/Li/Wang 2025)
        f.write("\n### 3c. Foundational/methodological audit-quality survey papers\n\n")
        survey_titles = [
            "review of archival auditing research",        # DeFond Zhang 2014
            "survey of the archival audit literature",      # Lennox Li Wang 2025
            "do practitioner assessments agree",            # Aobdia 2019
            "measuring audit quality",                       # Rajgopal Srinivasan Zheng 2021
            "audit failures",                                # DeFond Zhang 2025
            "behavioral economics of accounting",            # Hanlon Yeung Zuo 2022
            "economics of auditing in china",                # Lin Shi Yuan Zuo 2024
            "review of china related accounting research",  # Lennox Wu 2022
            "auditing research using chinese data",          # DeFond Zhang Zhang 2021
        ]
        for r in zotero_recs:
            nt = r["norm_title"]
            for s in survey_titles:
                if s in nt:
                    pdf_flag = "✓PDF" if r["has_pdf"] else "✗no-PDF"
                    match = "✓in-paper/" if r["paper_match"] != "none" else "✗"
                    f.write(f"- **{r['year']}** — _{r['title']}_  ·  {pdf_flag}  ·  {match}  ·  `{r['item_key']}`\n")
                    break

        # paper-only items (not in Zotero) — biggest ROI to fix
        f.write("\n## 4. `paper/` audit×top_acct items NOT in Zotero "
                "(should be imported to Zotero)\n\n")
        paper_only_audit_topacct = [
            p for p in paper_only
            if p["subfield"] == "audit" and p["journal_tier"] == "top_acct"
        ]
        f.write(f"_{len(paper_only_audit_topacct)} items_\n\n")
        for p in sorted(paper_only_audit_topacct,
                        key=lambda x: (int(x["year"]) if x["year"] else 0)):
            f.write(f"- **{p['year']}** — {p['authors']} — _{p['title']}_  \n")
            f.write(f"  Journal: {p['journal_canonical']}  ·  `{p['filename']}`\n")

    # ----- Compose extraction recommendation -----
    rec_path = OUT_DIR / "extraction_recommendation.md"
    with rec_path.open("w", encoding="utf-8") as f:
        f.write("# Extraction recommendation — what to pull from Zotero into Stage 1\n\n")
        f.write("Stage 1 = deepen `audit-write` from 6 → ~20–30 curated audit exemplars + "
                "the methodological/survey reference layer.\n\n")
        f.write("## A. KEEP from Zotero (already in paper/ — verified PDF exists)\n\n")
        f.write("Audit-classified, Zotero ↔ paper/ matched, PDF present:\n\n")
        f.write("| Year | Title | Zotero key | paper/ filename |\n|---|---|---|---|\n")
        for r in sorted([x for x in zotero_recs
                         if x["subfield"] == "audit" and x["paper_match"] != "none"],
                        key=lambda x: -(x["year"] or 0)):
            f.write(f"| {r['year']} | {r['title'][:70]} | `{r['item_key']}` | `{r['paper_filename'][:60]}` |\n")

        f.write("\n## B. PRIORITY ADD — Zotero-only audit items (verify PDF, consider importing)\n\n")
        f.write("Audit-classified items in Zotero but not in paper/. If `has_pdf=✓`, Zotero has the PDF "
                "— we should either copy it to paper/ or work from Zotero's storage.\n\n")
        f.write("| Year | Title | PDF? | Zotero key |\n|---|---|---|---|\n")
        for r in sorted([x for x in zotero_recs
                         if x["subfield"] == "audit" and x["paper_match"] == "none"],
                        key=lambda x: -(x["year"] or 0)):
            pdf = "✓" if r["has_pdf"] else "✗"
            f.write(f"| {r['year']} | {r['title'][:80]} | {pdf} | `{r['item_key']}` |\n")

        f.write("\n## C. PRIORITY ADD — paper/ audit×top_acct items NOT in Zotero "
                "(import to Zotero for metadata)\n\n")
        f.write("| Year | Authors | Title | Journal |\n|---|---|---|---|\n")
        paper_only_audit_topacct = [
            p for p in paper_only
            if p["subfield"] == "audit" and p["journal_tier"] == "top_acct"
        ]
        for p in sorted(paper_only_audit_topacct,
                        key=lambda x: int(x["year"]) if x["year"] else 0, reverse=True):
            f.write(f"| {p['year']} | {p['authors'][:35]} | {p['title'][:70]} | {p['journal_canonical']} |\n")

        f.write("\n## D. RESERVE — foundational/survey refs (cite-only, not gold-set exemplars)\n\n")
        f.write("These are the methodological / framework references — they ARE in the suite's "
                "vocabulary (DeFond-Zhang 2014, Aobdia 2019, etc.) but should be marked `[-]` "
                "in the gold-set curation list. Keep them accessible in Zotero for citation:\n\n")
        survey_titles = ["review of archival auditing research", "survey of the archival audit literature",
            "do practitioner assessments agree", "measuring audit quality", "audit failures",
            "behavioral economics of accounting", "economics of auditing in china",
            "review of china related accounting research", "auditing research using chinese data"]
        for r in zotero_recs:
            nt = r["norm_title"]
            for s in survey_titles:
                if s in nt:
                    pdf = "✓" if r["has_pdf"] else "✗"
                    f.write(f"- **{r['year']}** — _{r['title']}_  ·  PDF:{pdf}  ·  `{r['item_key']}`\n")
                    break

        f.write("\n## E. OUT OF SCOPE — other Zotero clusters (skip for Stage 1)\n\n")
        skip = ["culture_propaganda", "institutions_econ", "healthcare"]
        cnts = defaultdict(int)
        for r in zotero_recs:
            if r["subfield"] in skip:
                cnts[r["subfield"]] += 1
        for s in skip:
            f.write(f"- `{s}`: {cnts[s]} items — user's other research projects, defer\n")

        f.write("\n## F. KNOWN GAP — 354 items in `english` collection not scanned\n\n")
        f.write("`get_collection_items` MCP capped at 100/call with no pagination. "
                "If we need exhaustive coverage, options:\n"
                "1. Use `zotero_get_item_metadata` per-key (slow, requires known keys)\n"
                "2. Query Zotero local SQLite directly\n"
                "3. Filter the remaining 354 by tag (tag scheme is sparse — limited recall)\n"
                "4. User exports a CSV from Zotero desktop UI and we ingest that\n\n"
                "**Decision deferred**: the 98-item curated `integrity_propaganda_audit` + 100 most-recent "
                "`english` items already cover the audit-quality cluster the user actively curates. "
                "Address the 354 gap only if Stage 1 distillation surfaces specific missing exemplars.\n")

    # ----- summary -----
    print(f"zotero_recs       = {n_zot}")
    print(f"  audit-classified= {n_zot_audit} (with PDF: {n_zot_audit_with_pdf})")
    print(f"  matched paper/  = {n_zot_audit_matched}")
    print(f"paper-only audit×top_acct (need add to Zotero) = "
          f"{sum(1 for p in paper_only if p['subfield']=='audit' and p['journal_tier']=='top_acct')}")
    print(f"out:")
    print(f"  {out_csv}")
    print(f"  {xref_path}")
    print(f"  {rec_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

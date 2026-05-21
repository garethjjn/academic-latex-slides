"""
Build the unified corpus master view across paper/ and Zotero.

Reads:
  corpus_inventory/manifest.csv                                 paper/ inventory
  corpus_inventory/zotero_raw/integrity_propaganda_audit.md     Zotero (curated)
  corpus_inventory/zotero_raw/english_first100.md               Zotero (partial)
  corpus_inventory/zotero_raw/audit_write_stage1_candidates.md  Zotero (just imported)

Writes:
  corpus_inventory/corpus_master.csv      one row per LOGICAL paper, with status flags
  corpus_inventory/corpus_master.md       human-readable summary of the unified state
"""

from __future__ import annotations

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from zotero_inventory_crossref import (
    parse_summary_md, parse_keys_md, normalize_title, classify_subfield,
)
from inventory_paper_corpus import parse_filename as parse_paper_filename


def fix_filename_shaped_zotero(records: list[dict]) -> None:
    """When a Zotero record's title is a full PDF filename (case for items
    just imported before DOI extraction completes), re-parse it with the
    same logic used for paper/ filenames so year and true title come out."""
    import re as _re
    for r in records:
        title = r.get("title") or ""
        # Heuristic: starts with 'YYYY - ' AND ends with .pdf/.txt
        if not _re.match(r"^\d{4}\s-\s", title):
            continue
        # Normalize: if missing extension, add .pdf to satisfy parse_paper_filename
        if not title.lower().endswith((".pdf", ".txt")):
            title = title + ".pdf"
        parsed = parse_paper_filename(title)
        if not parsed.get("parse_ok"):
            continue
        r["year"] = parsed["year"]
        r["title"] = parsed["title"]
        r["authors"] = parsed["authors"]
        r["norm_title"] = normalize_title(parsed["title"])
        r["subfield"] = classify_subfield(parsed["title"])

ROOT = Path("d:/OneDrive/tools")
RAW = ROOT / "corpus_inventory" / "zotero_raw"
OUT = ROOT / "corpus_inventory"
PAPER_CSV = OUT / "manifest.csv"


def main() -> int:
    # 1) Pull all Zotero records (3 sources merged on item_key)
    audit_col = parse_summary_md(RAW / "integrity_propaganda_audit.md")
    english_col = parse_keys_md(RAW / "english_first100.md")
    stage1_col = parse_keys_md(RAW / "audit_write_stage1_candidates.md")
    # Just-imported items have filename-shaped titles + empty dates — re-parse them
    fix_filename_shaped_zotero(stage1_col)
    fix_filename_shaped_zotero(english_col)
    # Mark each by source
    for r in audit_col:   r["source_collection"] = "integrity_propaganda_audit"
    for r in english_col: r["source_collection"] = "english"
    for r in stage1_col:  r["source_collection"] = "audit_write_stage1_candidates"

    zotero_by_key: dict[str, dict] = {}
    for r in audit_col + english_col + stage1_col:
        if r["item_key"] in zotero_by_key:
            # merge: keep richest record; record multi-collection membership
            existing = zotero_by_key[r["item_key"]]
            existing["source_collection"] = (
                existing["source_collection"] + "+" + r["source_collection"]
            )
        else:
            zotero_by_key[r["item_key"]] = r
    zotero_recs = list(zotero_by_key.values())

    # Index Zotero by normalized (year, title) for paper/ matching
    zot_index: dict[tuple[str, str], dict] = {}
    for r in zotero_recs:
        if not r["year"]:
            continue
        zot_index[(str(r["year"]), r["norm_title"])] = r

    def prefix_match(a: str, b: str, min_ratio: float = 0.5) -> bool:
        if not a or not b: return False
        s, l = sorted([a, b], key=len)
        if not l.startswith(s): return False
        return len(s) / len(l) >= min_ratio

    # 2) Walk paper/ manifest, mark zotero status on each
    paper_rows = list(csv.DictReader(open(PAPER_CSV, encoding="utf-8")))
    # one row per logical paper (drop txt companions, dedup by norm_key)
    paper_by_normkey: dict[str, dict] = {}
    for r in paper_rows:
        if r["ext"] != "pdf":
            continue
        paper_by_normkey.setdefault(r["norm_key"], r)

    # Group paper titles by year for prefix-match
    paper_titles_by_year: dict[str, list[tuple[str, dict]]] = defaultdict(list)
    for k, pr in paper_by_normkey.items():
        y, t = k.split("::", 1)
        paper_titles_by_year[y].append((t, pr))

    # 3) Build the unified rows
    unified: list[dict] = []
    matched_zotero_keys: set[str] = set()

    for pkey, pr in paper_by_normkey.items():
        y, ptitle = pkey.split("::", 1)
        # try exact then prefix match against Zotero
        zr = zot_index.get((y, ptitle))
        if not zr:
            for (zy, zt), z in zot_index.items():
                if zy != y: continue
                if prefix_match(zt, ptitle):
                    zr = z
                    break
        in_zotero = zr is not None
        if in_zotero:
            matched_zotero_keys.add(zr["item_key"])
        unified.append({
            "norm_key": pkey,
            "year": y, "title": pr["title"], "authors": pr["authors"],
            "journal_canonical": pr["journal_canonical"],
            "journal_tier": pr["journal_tier"],
            "subfield": pr["subfield"],
            "paper_filename": pr["filename"],
            "in_paper": True,
            "in_zotero": in_zotero,
            "zotero_key": zr["item_key"] if zr else "",
            "zotero_collection": zr["source_collection"] if zr else "",
            "status": "in_both" if in_zotero else "paper_only",
        })

    # Zotero records NOT matched to paper/
    for r in zotero_recs:
        if r["item_key"] in matched_zotero_keys: continue
        unified.append({
            "norm_key": f"{r['year']}::{r['norm_title']}",
            "year": str(r["year"] or ""),
            "title": r["title"],
            "authors": r["authors"] or "",
            "journal_canonical": "",
            "journal_tier": "",
            "subfield": r["subfield"],
            "paper_filename": "",
            "in_paper": False,
            "in_zotero": True,
            "zotero_key": r["item_key"],
            "zotero_collection": r["source_collection"],
            "status": "zotero_only",
        })

    # 4) Write CSV
    cols = ["status", "year", "authors", "title", "subfield",
            "journal_canonical", "journal_tier",
            "in_paper", "paper_filename",
            "in_zotero", "zotero_key", "zotero_collection",
            "norm_key"]
    out_csv = OUT / "corpus_master.csv"
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in sorted(unified, key=lambda x: (x["status"], -int(x["year"]) if x["year"] else 0)):
            w.writerow(r)

    # 5) Write human-readable summary
    n_total = len(unified)
    n_both = sum(1 for r in unified if r["status"] == "in_both")
    n_paper_only = sum(1 for r in unified if r["status"] == "paper_only")
    n_zot_only = sum(1 for r in unified if r["status"] == "zotero_only")

    audit_both = sum(1 for r in unified if r["status"] == "in_both" and r["subfield"] == "audit")
    audit_paper_only = sum(1 for r in unified if r["status"] == "paper_only" and r["subfield"] == "audit")
    audit_zot_only = sum(1 for r in unified if r["status"] == "zotero_only" and r["subfield"] == "audit")

    audit_topacct_both = sum(1 for r in unified
                              if r["status"] == "in_both" and r["subfield"] == "audit"
                              and r["journal_tier"] == "top_acct")
    audit_topacct_paper_only = sum(1 for r in unified
                                    if r["status"] == "paper_only" and r["subfield"] == "audit"
                                    and r["journal_tier"] == "top_acct")

    md_path = OUT / "corpus_master.md"
    with md_path.open("w", encoding="utf-8") as f:
        f.write("# Unified corpus master view\n\n")
        f.write("_Generated by_ `scripts/build_unified_corpus.py`. "
                "Single source of truth combining `paper/manifest.csv` + "
                "all Zotero collections currently parsed.\n\n")

        f.write("## 1. Headline\n\n")
        f.write(f"- Logical papers tracked: **{n_total}**\n")
        f.write(f"  - In both paper/ AND Zotero: **{n_both}** ✅\n")
        f.write(f"  - In paper/ only (no Zotero entry yet): **{n_paper_only}**\n")
        f.write(f"  - In Zotero only (no PDF in paper/): **{n_zot_only}**\n\n")

        f.write("## 2. Audit slice (the priority slice for Stage 1)\n\n")
        f.write(f"- Total audit-classified papers across both sides: "
                f"**{audit_both + audit_paper_only + audit_zot_only}**\n")
        f.write(f"  - In both: **{audit_both}** (Stage 1 ready)\n")
        f.write(f"  - paper/ only: **{audit_paper_only}** (still missing Zotero entry)\n")
        f.write(f"  - Zotero only: **{audit_zot_only}** (foundational refs, working papers, China research)\n\n")

        f.write("### 2a. Audit × top_acct (the actual gold-set pool)\n\n")
        f.write(f"- In both paper/ AND Zotero: **{audit_topacct_both}** ✅\n")
        f.write(f"- In paper/ only: **{audit_topacct_paper_only}** "
                f"(should be 0 after the import; if not, why?)\n\n")

        f.write("## 3. Subfield × status\n\n")
        by_sub = defaultdict(lambda: Counter())
        for r in unified:
            by_sub[r["subfield"]][r["status"]] += 1
        f.write("| Subfield | in_both | paper_only | zotero_only | Total |\n")
        f.write("|---|---:|---:|---:|---:|\n")
        for s in sorted(by_sub, key=lambda k: -sum(by_sub[k].values())):
            cnts = by_sub[s]
            tot = sum(cnts.values())
            f.write(f"| {s} | {cnts['in_both']} | {cnts['paper_only']} | "
                    f"{cnts['zotero_only']} | **{tot}** |\n")

        f.write("\n## 4. Zotero coverage of paper/ corpus\n\n")
        n_paper_total = sum(1 for r in unified if r["in_paper"])
        n_paper_in_zot = sum(1 for r in unified if r["in_paper"] and r["in_zotero"])
        f.write(f"- paper/ logical papers: **{n_paper_total}**\n")
        f.write(f"- Of which now in Zotero: **{n_paper_in_zot}** ({100*n_paper_in_zot/n_paper_total:.0f}%)\n")
        f.write(f"- Gap (still paper-only): **{n_paper_total - n_paper_in_zot}** "
                f"— mostly non-audit (finance, governance, methodology)\n\n")

        f.write("## 5. Files this view replaces\n\n")
        f.write("- `zotero_inventory.csv` (pre-import; superseded)\n")
        f.write("- `zotero_x_paper.md` (pre-import; superseded)\n"
                "- `extraction_recommendation.md` (Section A/B/C status now consolidated here)\n\n")
        f.write("Keep `zotero_import_log.md` and `audit_papers_to_curate.md` (those track actions).\n")

    print(f"unified rows: {n_total} (in_both={n_both}, paper_only={n_paper_only}, "
          f"zotero_only={n_zot_only})")
    print(f"  audit × top_acct in_both: {audit_topacct_both}")
    print(f"  audit × top_acct paper_only: {audit_topacct_paper_only}")
    print(f"out:")
    print(f"  {out_csv}")
    print(f"  {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

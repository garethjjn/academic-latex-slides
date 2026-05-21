"""
Move TRUE duplicates (same logical paper, same extension) into a quarantine
subfolder for user review. NON-DESTRUCTIVE: nothing is deleted; files only
move into paper/_duplicates_to_review/. The largest file in each group stays
in place (most likely the most complete copy).

Re-run-safe: skips files already moved.
"""

from __future__ import annotations

import csv
import shutil
import sys
from collections import defaultdict
from pathlib import Path

PAPER_DIR = Path("d:/OneDrive/tools/paper")
QUARANTINE = PAPER_DIR / "_duplicates_to_review"
OUT_DIR = Path("d:/OneDrive/tools/corpus_inventory")
MANIFEST = OUT_DIR / "manifest.csv"
LOG = OUT_DIR / "quarantine_log.csv"

QUARANTINE.mkdir(parents=True, exist_ok=True)


def main() -> int:
    if not MANIFEST.exists():
        print(f"ERROR: manifest not found at {MANIFEST}. Run inventory first.")
        return 2

    rows: list[dict] = []
    with MANIFEST.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append(r)

    # group by (norm_key, ext)
    groups: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for r in rows:
        groups[(r["norm_key"], r["ext"])].append(r)
    dup_groups = {k: v for k, v in groups.items() if len(v) > 1}

    moves: list[tuple[str, str, str, str]] = []  # (group_key, action, file, reason)
    for (key, ext), group in dup_groups.items():
        # Keep the file with the largest byte size; move the rest.
        group_sorted = sorted(group, key=lambda r: -int(r["size_bytes"]))
        keeper = group_sorted[0]
        moves.append((f"{key}::{ext}", "KEEP", keeper["filename"],
                      f"largest at {keeper['size_bytes']} B"))
        for r in group_sorted[1:]:
            moves.append((f"{key}::{ext}", "MOVE", r["filename"],
                          f"redundant copy ({r['size_bytes']} B)"))

    # Execute moves
    moved = 0
    skipped = 0
    errors: list[tuple[str, str]] = []
    for group_key, action, fname, reason in moves:
        if action != "MOVE":
            continue
        src = PAPER_DIR / fname
        dst = QUARANTINE / fname
        if not src.exists():
            skipped += 1
            errors.append((fname, "src missing (already moved?)"))
            continue
        if dst.exists():
            skipped += 1
            errors.append((fname, "already in quarantine"))
            continue
        try:
            shutil.move(str(src), str(dst))
            moved += 1
        except Exception as e:
            errors.append((fname, str(e)))

    # Log
    with LOG.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["group_key", "action", "file", "reason"])
        for row in moves:
            w.writerow(row)

    print(f"moved={moved}  skipped={skipped}  errors={len(errors)}")
    if errors:
        for fname, err in errors[:10]:
            print(f"  - {fname}: {err}")
    print(f"quarantine: {QUARANTINE}")
    print(f"log: {LOG}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

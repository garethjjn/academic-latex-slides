#!/usr/bin/env python3
"""Sync the canonical skill into the Claude Code plugin distribution."""

from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_SKILL = ROOT / "skills" / "academic-latex-slides"
PLUGIN_SKILL = (
    ROOT
    / "plugins"
    / "academic-latex-slides"
    / "skills"
    / "academic-latex-slides"
)


def main() -> None:
    if not CANONICAL_SKILL.exists():
        raise SystemExit(f"Canonical skill not found: {CANONICAL_SKILL}")

    if PLUGIN_SKILL.exists():
        shutil.rmtree(PLUGIN_SKILL)

    PLUGIN_SKILL.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(CANONICAL_SKILL, PLUGIN_SKILL)
    print(f"Synced {CANONICAL_SKILL} -> {PLUGIN_SKILL}")


if __name__ == "__main__":
    main()

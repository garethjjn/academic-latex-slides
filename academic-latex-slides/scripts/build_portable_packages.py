#!/usr/bin/env python3
"""Build transfer-ready ZIP packages for Codex and Claude Code installs."""

from __future__ import annotations

import shutil
from pathlib import Path

from sync_distributions import CANONICAL_SKILL, ROOT, main as sync_main


DIST_DIR = ROOT / "dist"
CODEX_ARCHIVE = DIST_DIR / "academic-latex-slides-codex-skill"
CLAUDE_ARCHIVE = DIST_DIR / "academic-latex-slides-claude-plugin"


def build_codex_zip() -> Path:
    return Path(
        shutil.make_archive(
            str(CODEX_ARCHIVE),
            "zip",
            root_dir=CANONICAL_SKILL.parent,
            base_dir=CANONICAL_SKILL.name,
        )
    )


def build_claude_zip() -> Path:
    include_paths = [
        ROOT / ".claude-plugin",
        ROOT / "plugins",
        ROOT / "README.md",
        ROOT / "LICENSE",
    ]
    staging_dir = DIST_DIR / "_claude_plugin_staging"
    if staging_dir.exists():
        shutil.rmtree(staging_dir)
    staging_dir.mkdir(parents=True)

    for path in include_paths:
        destination = staging_dir / path.name
        if path.is_dir():
            shutil.copytree(path, destination)
        else:
            shutil.copy2(path, destination)

    archive = Path(
        shutil.make_archive(
            str(CLAUDE_ARCHIVE),
            "zip",
            root_dir=staging_dir,
        )
    )
    shutil.rmtree(staging_dir)
    return archive


def main() -> None:
    sync_main()
    DIST_DIR.mkdir(exist_ok=True)
    codex_zip = build_codex_zip()
    claude_zip = build_claude_zip()
    print(f"Built {codex_zip}")
    print(f"Built {claude_zip}")


if __name__ == "__main__":
    main()

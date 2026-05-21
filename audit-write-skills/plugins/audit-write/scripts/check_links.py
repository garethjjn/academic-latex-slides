#!/usr/bin/env python3
"""check_links.py — resolve every intra-suite Markdown reference; report rot.

Stdlib only. Catches the pointer-discipline risk flagged in the v2 review:
move_bank / exemplar_gallery point into pattern files, and shared banks are
referenced by relative path from sibling skills — if a file is moved/renamed,
those references rot silently. This makes that mechanical.

Scans, for every *.md under the given root:
  - Markdown links            ](target)
  - Backtick code spans that contain a *.md path token
Resolves each relative to the containing file's directory. Ignores http(s),
anchors-only, ${VARS}, and [PLACEHOLDER] tokens.

Usage:  check_links.py [ROOT]   (default: the plugin root inferred from this file)
Exit:   0 = all resolve · 1 = broken refs found  (advisory callers may ignore)
"""
import os
import re
import sys

try:  # portable on non-UTF-8 default stdouts (e.g. GBK Windows)
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
except Exception:
    pass

MD_LINK = re.compile(r"\]\(([^)]+)\)")
# a path-like *.md token inside backticks: MUST contain a slash (a real
# reference), so bare prose mentions like `style_dna.md` are not flagged.
CODE_MD = re.compile(r"`([^`]*?/[^`]*?\.md)(?:[^`]*)?`")
SKIP = ("http://", "https://", "mailto:", "${", "[", "#")
# runtime artifacts the user creates in their working dir — never shipped files
RUNTIME = {"paper-spec.md", "outline.md"}


def candidates(text):
    for m in MD_LINK.finditer(text):
        yield m.group(1).strip()
    for m in CODE_MD.finditer(text):
        yield m.group(1).strip()


def norm(target):
    # strip section/anchor suffixes: "foo.md §2", "foo.md#x"
    t = target.split("#", 1)[0]
    t = re.split(r"\s+§|\s+§|\s", t, 1)[0]
    return t.strip()


def find_workspace_root(start):
    """Walk up from `start` looking for a workspace marker. Returns the
    workspace root or None. Markers (in priority order): .git directory,
    pyproject.toml, or presence of both corpus_inventory/ and paper/ siblings
    (this last is the repo-specific heuristic for the audit-write workspace)."""
    cur = os.path.abspath(start)
    while True:
        if os.path.isdir(os.path.join(cur, ".git")):
            return cur
        if os.path.isfile(os.path.join(cur, "pyproject.toml")):
            return cur
        if (os.path.isdir(os.path.join(cur, "corpus_inventory"))
                and os.path.isdir(os.path.join(cur, "paper"))):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            return None
        cur = parent


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
    workspace = find_workspace_root(root)
    broken = []
    scanned = 0
    for dirpath, _, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            path = os.path.join(dirpath, fn)
            scanned += 1
            try:
                text = open(path, encoding="utf-8").read()
            except (OSError, UnicodeDecodeError):
                continue
            for raw in candidates(text):
                if not raw or raw.startswith(SKIP):
                    continue
                if "<" in raw or ">" in raw:  # placeholder token, not a link
                    continue
                tgt = norm(raw)
                if not tgt.endswith(".md"):
                    continue
                if os.path.basename(tgt) in RUNTIME:
                    continue
                # Try resolution in order: (1) relative to containing file,
                # (2) relative to workspace root (for workspace-anchored refs
                # like `corpus_inventory/track_b_drafts/_accept_log.md` written
                # from agent files inside the plugin).
                resolved = os.path.normpath(os.path.join(dirpath, tgt))
                if os.path.exists(resolved):
                    continue
                if workspace:
                    resolved_ws = os.path.normpath(os.path.join(workspace, tgt))
                    if os.path.exists(resolved_ws):
                        continue
                broken.append((os.path.relpath(path, root), raw))
    if broken:
        print(f"check_links: {len(broken)} BROKEN reference(s) in {scanned} files:")
        for src, ref in broken:
            print(f"  {src}  ->  {ref}")
        return 1
    print(f"check_links: OK — {scanned} markdown files, all references resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Validate template manifests against the academic-latex-slides contract.

P1 scope: schema-shaped checks, placeholder consistency, and asset declaration.
Standard library only (no jsonschema dependency). The full smoke-compile matrix
is intentionally deferred to P2.

Usage:
    python validate_template.py <id> [<id> ...]
    python validate_template.py --all
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
TEMPLATES_DIR = SKILL_ROOT / "assets" / "templates"
SCHEMA_ID = "academic-latex-slides/template@1"

REQUIRED_KEYS = {
    "schema", "id", "name", "summary", "status", "engine",
    "documentclass", "entry", "placeholders", "capabilities",
    "escape_profile", "assets",
}
STATUS_VALUES = {"stable", "community", "experimental"}
PLACEHOLDER_VALUES = {
    "TITLE", "SHORT_TITLE", "SUBTITLE", "AUTHOR",
    "INSTITUTE", "SHORT_INSTITUTE", "DATE", "SECTION_INPUTS",
}
MANDATORY_PLACEHOLDERS = {"TITLE", "SECTION_INPUTS"}
CAP_KEYS = {"subtitle", "empty_subtitle", "section_divider",
            "title_graphic", "cjk"}
CAP_ENUMS = {
    "subtitle": {"optional", "required", "unsupported"},
    "empty_subtitle": {"omit-line", "keep"},
}
ESCAPE_PROFILES = {"latex-standard"}
PLACEHOLDER_RE = re.compile(r"\{\{([A-Z_]+)\}\}")


def validate(tid: str) -> list[str]:
    """Return a list of error strings (empty == valid)."""
    errs: list[str] = []
    tdir = TEMPLATES_DIR / tid
    mpath = tdir / "template.json"
    if not tdir.is_dir():
        return [f"template directory not found: {tdir}"]
    if not mpath.is_file():
        return [f"missing template.json in {tdir}"]
    try:
        m = json.loads(mpath.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"template.json is not valid JSON: {e}"]

    missing = REQUIRED_KEYS - m.keys()
    if missing:
        errs.append(f"missing required keys: {sorted(missing)}")
    extra = m.keys() - (REQUIRED_KEYS | {"good_fit", "min_scaffold", "maintainer"})
    if extra:
        errs.append(f"unknown keys: {sorted(extra)}")

    if m.get("schema") != SCHEMA_ID:
        errs.append(f"schema must be '{SCHEMA_ID}', got {m.get('schema')!r}")
    if m.get("id") != tid:
        errs.append(f"id {m.get('id')!r} must equal directory name {tid!r}")
    if m.get("status") not in STATUS_VALUES:
        errs.append(f"status must be one of {sorted(STATUS_VALUES)}")
    if m.get("engine") != "xelatex":
        errs.append("engine must be 'xelatex'")
    if m.get("entry") != "main.tex.template":
        errs.append("entry must be 'main.tex.template'")
    if m.get("escape_profile") not in ESCAPE_PROFILES:
        errs.append(f"escape_profile must be one of {sorted(ESCAPE_PROFILES)}")

    # placeholders: declared set must exactly match the entry file's tokens,
    # and must include the mandatory ones.
    declared = m.get("placeholders", [])
    if not isinstance(declared, list) or not declared:
        errs.append("placeholders must be a non-empty array")
        declared_set: set[str] = set()
    else:
        declared_set = set(declared)
        bad = declared_set - PLACEHOLDER_VALUES
        if bad:
            errs.append(f"unknown placeholders declared: {sorted(bad)}")
        if not MANDATORY_PLACEHOLDERS <= declared_set:
            errs.append(
                f"placeholders must include {sorted(MANDATORY_PLACEHOLDERS)}"
            )
    entry_path = tdir / "main.tex.template"
    if not entry_path.is_file():
        errs.append("entry file main.tex.template not found")
    else:
        used = set(PLACEHOLDER_RE.findall(entry_path.read_text(encoding="utf-8")))
        if used - declared_set:
            errs.append(f"entry uses undeclared placeholders: {sorted(used - declared_set)}")
        if declared_set - used:
            errs.append(f"declared placeholders absent from entry: {sorted(declared_set - used)}")

    caps = m.get("capabilities", {})
    if not isinstance(caps, dict):
        errs.append("capabilities must be an object")
    else:
        cmiss = CAP_KEYS - caps.keys()
        if cmiss:
            errs.append(f"capabilities missing keys: {sorted(cmiss)}")
        cextra = caps.keys() - CAP_KEYS
        if cextra:
            errs.append(f"capabilities has unknown keys: {sorted(cextra)}")
        for k, allowed in CAP_ENUMS.items():
            if k in caps and caps[k] not in allowed:
                errs.append(f"capabilities.{k} must be one of {sorted(allowed)}")
        for k in ("section_divider", "title_graphic", "cjk"):
            if k in caps and not isinstance(caps[k], bool):
                errs.append(f"capabilities.{k} must be boolean")

    assets = m.get("assets", [])
    if not isinstance(assets, list):
        errs.append("assets must be an array")
    else:
        for a in assets:
            if not isinstance(a, dict):
                errs.append(f"asset entry not an object: {a!r}")
                continue
            amiss = {"file", "purpose", "source", "license"} - a.keys()
            if amiss:
                errs.append(f"asset {a.get('file', '?')!r} missing {sorted(amiss)}")
            f = a.get("file")
            if f and not (tdir / f).exists():
                errs.append(f"declared asset not found on disk: {f}")
            if not str(a.get("source", "")).strip():
                errs.append(f"asset {f!r} has empty source")
            if not str(a.get("license", "")).strip():
                errs.append(f"asset {f!r} has empty license")
        declared_files = {a.get("file") for a in assets if isinstance(a, dict)}
        ignore = {"main.tex.template", "template.json"}
        for item in tdir.iterdir():
            if item.name in ignore:
                continue
            if item.name not in declared_files:
                errs.append(f"asset present on disk but not declared: {item.name}")
    return errs


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("ids", nargs="*", help="template ids to validate")
    ap.add_argument("--all", action="store_true", help="validate every template")
    args = ap.parse_args()

    if args.all or not args.ids:
        ids = sorted(
            p.parent.name
            for p in TEMPLATES_DIR.glob("*/template.json")
        )
    else:
        ids = args.ids

    if not ids:
        print("no templates found to validate", file=sys.stderr)
        raise SystemExit(2)

    failed = False
    for tid in ids:
        errs = validate(tid)
        if errs:
            failed = True
            print(f"FAIL  {tid}")
            for e in errs:
                print(f"      - {e}")
        else:
            print(f"OK    {tid}")
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()

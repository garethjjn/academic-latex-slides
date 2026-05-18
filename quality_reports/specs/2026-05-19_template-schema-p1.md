# Requirements Spec — Template Manifest & Registry (P1: Foundation)

**Status:** DRAFT (awaiting user approval)
**Date:** 2026-05-19
**Scope:** Phase 1 of the "template contribution guide + schema" optimization.
P1 is deliberately **zero behavior change** — it adds a declarative layer and
makes the engine *discover* templates instead of hardcoding them, without
altering any generated output.

## Goal

Lower the template-contribution barrier from "edit Python + 3 docs + rediscover
known LaTeX pitfalls" to "add one validated JSON file", by introducing a
per-template manifest and a discoverable registry — starting with the safest
slice.

## Non-goals (explicitly deferred)

- Removing the SJTU empty-subtitle special-case in `render_main` → **P2**.
- Smoke-compile matrix validator + CI gate → **P2**.
- Auto-generating `templates.md` / README table / Acknowledgements → **P3**.
- Rewording the `SKILL.md` "four variants only" rule → **P3** (governance).
- `status: community` ecosystem / gallery → **P4**.

## Requirements

### MUST

- **M1.** A JSON Schema file `template.schema.json` defining
  `academic-latex-slides/template@1` (fields: `schema, id, name, summary,
  good_fit, status, engine, documentclass, entry, placeholders, capabilities,
  escape_profile, assets[ {file,purpose,source,license} ], min_scaffold,
  maintainer`).
- **M2.** A valid `template.json` in each of the 4 existing template dirs
  (`msu, sjtu, cityu, generic`), authored to **describe current behavior
  exactly** (descriptive only — not yet wired to change engine logic).
- **M3.** `scaffold.py` derives `--template` choices by **scanning
  `assets/templates/*/template.json`** instead of the hardcoded
  `TEMPLATE_CHOICES` tuple. The set of accepted/rejected `--template` values
  MUST be identical to today (msu/sjtu/cityu/generic accepted; anything else
  rejected with a clear message).
- **M4.** **Zero behavior change**: for every (template × deck-type × language)
  combination, scaffold output MUST be byte-identical to pre-P1 output.
  `render_main` and asset-copy logic are untouched in P1.
- **M5.** Every shipped `template.json` validates against
  `template.schema.json`.
- **M6.** Canonical → plugin mirror parity preserved: manifests land in
  `plugins/academic-latex-slides/...` via `sync_distributions.py`; trees stay
  byte-identical after sync.

### SHOULD

- **S1.** A lightweight `scripts/validate_template.py <id>` that checks
  (a) manifest validates against schema, (b) every `{{PLACEHOLDER}}` in `entry`
  is declared and every declared placeholder is present, (c) declared assets
  exist and each has non-empty `source` + `license`. (Full compile matrix is
  P2.)
- **S2.** Backward-compat shim: if a template dir has **no** `template.json`,
  `scaffold.py` synthesizes a minimal in-memory manifest from current behavior
  so nothing breaks during partial migration.

### MAY

- **A1.** `scaffold.py --list-templates` prints id + summary + status from the
  registry.
- **A2.** A generated `assets/templates/registry.json` index (fast listing;
  not authoritative — manifests are the source of truth).

## Clarity status

- **CLEAR:** schema fields, P1 scope boundary, zero-behavior-change constraint,
  publish path (revise-commit workflow, no Claude co-author — per memory).
- **ASSUMED:** manifest is **per-template-dir `template.json`** (self-contained,
  best for PR-based contribution) rather than one central file. User may
  override.
- **ASSUMED:** `template.schema.json` lives at
  `assets/templates/template.schema.json` (next to the templates it governs).
- **BLOCKED:** none.

## Acceptance criteria

1. `python scripts/validate_template.py msu|sjtu|cityu|generic` → all pass.
2. `scaffold.py --template <x>` accepts exactly the same 4 ids as before;
   unknown id error message still clear.
3. Diff of scaffold output (4 templates × {lecture,research-talk} × {en,zh})
   before vs after P1 = empty.
4. After `sync_distributions.py`, canonical and plugin mirror byte-identical.
5. Published via a single `revise:` commit, plain push, no `Co-Authored-By`.

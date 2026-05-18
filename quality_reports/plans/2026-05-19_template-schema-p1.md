# Implementation Plan — Template Manifest & Registry (P1)

**Status:** DRAFT (awaiting approval)
**Spec:** quality_reports/specs/2026-05-19_template-schema-p1.md
**Date:** 2026-05-19
**Principle:** smallest safe increment; zero behavior change; dogfood the
revise-commit publish workflow + no Claude co-author (per memory).

## Approach

Add a descriptive declarative layer (schema + 4 manifests) and switch
`scaffold.py` from a hardcoded tuple to filesystem discovery, with a
synthesized-manifest fallback so partial states never break. No engine logic
(`render_main`, asset copy, escaping, SJTU special-case) is modified in P1.

## Files

Canonical root: `academic-latex-slides/skills/academic-latex-slides/`

| Action | Path |
| --- | --- |
| ADD | `assets/templates/template.schema.json` (JSON Schema, `@1`) |
| ADD | `assets/templates/msu/template.json` |
| ADD | `assets/templates/sjtu/template.json` (declares `empty_subtitle: omit-line` — descriptive; engine still does the regex in P1) |
| ADD | `assets/templates/cityu/template.json` |
| ADD | `assets/templates/generic/template.json` |
| ADD | `scripts/validate_template.py` (schema + placeholder + asset-declaration checks; stdlib only) |
| EDIT | `scripts/scaffold.py` — replace `TEMPLATE_CHOICES` constant use with `discover_templates()` (scan `*/template.json`; fallback to synthesized manifest if absent); add `--list-templates` (MAY) |
| RUN | `scripts/sync_distributions.py` (mirror manifests + schema + validator into `plugins/`) |
| ADD (local only) | this plan + spec under `quality_reports/` (root; not in published `academic-latex-slides/` tree) |

`scaffold.py` constraint: keep `escape_latex`, `render_main`, `write_sections`,
`copy_template_assets` **unchanged**. Only the `--template` choice source and
an optional `--list-templates` are touched.

## Order of work

1. Author `template.schema.json` (the contract).
2. Author 4 `template.json` files; run them through a JSON-Schema check as
   they're written.
3. Write `validate_template.py`; confirm all 4 pass (S1).
4. Refactor `scaffold.py` discovery; keep hardcoded list as a cross-check
   assertion (must equal discovered set) to enforce M3/M4.
5. **Regression gate:** scaffold all 4 templates × {lecture,research-talk} ×
   {en,zh} into a temp dir BEFORE and AFTER the refactor; `diff -r` must be
   empty (M4 acceptance #3). Also one `latexmk -xelatex` smoke per template.
6. `sync_distributions.py`; verify canonical vs `plugins/` byte-identical (M6).
7. Commit on master (`revise:` message, bash here-doc, **no Co-Authored-By**).
8. Publish: `tree=$(git rev-parse master:academic-latex-slides)`;
   `commit-tree -p plugin-export`; `git branch -f plugin-export`;
   **plain** `git push plugin-origin plugin-export:main` (no force/squash).
9. Verify remote: commit count incremented, `template.json` ×4 + schema present
   in published tree.

## Verification / acceptance

- `validate_template.py` green for all 4 (spec #1).
- Pre/post scaffold `diff -r` empty (spec #3) — the hard zero-behavior-change gate.
- Unknown `--template zzz` still errors clearly (spec #2).
- 4 smoke compiles exit 0.
- Canonical ≡ plugin mirror after sync (spec #4).
- Published via one `revise:` commit, plain push, no co-author (spec #5).

## Rollback

All P1 changes are additive except the `scaffold.py` discovery refactor.
Rollback = revert the `scaffold.py` edit (manifests/schema/validator are inert
without it). Local `plugin-export` branch + master history allow a clean
revert; no history rewrite needed (revise workflow only ever fast-forwards).

## Risk register

- **R1 discovery breaks an edge case** (e.g. ordering, hidden dirs) → mitigated
  by the hardcoded-set cross-check assertion + pre/post diff gate.
- **R2 manifest drifts from real behavior** → P1 manifests are authored by
  reading each `main.tex.template`; validator enforces placeholder consistency.
- **R3 scope creep into P2** (tempting to also kill the SJTU regex) → explicitly
  out; P1 manifest only *describes* `empty_subtitle`.

## Out of scope (next phases)

P2 wire `empty_subtitle`/`escape_profile` into engine + compile-matrix CI ·
P3 docs-as-code + SKILL rule reword · P4 community status + gallery.

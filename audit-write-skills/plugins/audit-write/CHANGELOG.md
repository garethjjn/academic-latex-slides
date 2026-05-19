# Changelog — audit-write

All notable changes to the audit-write skill suite. The pre-1.0 phases (P1–P3) were
the development arc that produced the first packaged plugin release.

## [P5] — in progress — mechanism layer + external-validation hardening

### Added
- `docs/external-validation-ng.md` — design-rationale note: an independent
  practitioner account of AI-assisted writing (progressive outlining +
  rubric-against-sycophancy) corroborates the suite's two pillars; records
  provenance caveats and the gap analysis behind the refinements below.
- `rubric.md`: an **Objective pre-checklist** (binary C1–C7, run before banding);
  any `N` forces its mapped dimension down one band — reproducible, sycophancy-
  resistant scoring. The `## Score` output block now carries the checklist line.
- `scripts/check_structure.py` — advisory (always exit 0) binary self-check; the
  mechanism mirror of the rubric pre-checklist (`--section`-aware).
- `style_dna.md` §9: generic AI-slop tells (em-dash overuse, reflexive triads,
  "not X but Y", a noun-poverty / vague-adjective principle, empty-grand-claim).
- `progressive_outline.md`: a **"Why the ratchet is high-leverage"** rationale
  (outline edits cascade; surface the AGAINST before Stage 1; review speed).
- Golden tests for the new detectors (bad/good fixtures + `run_tests.py` cases).

### Changed
- `scripts/lint_style.py`: two conservative stdlib WARN detectors — em-dash
  overuse (≥3 + density) and the mirrored "not X … it's Y" construction. WARNs
  never fail the run. Rule-of-three / empty-grand-claim kept instruction-only
  (no reliable mechanical signature).
- `agents/audit-write-critic.md`: procedure now runs the binary pre-checklist
  before banding and emits the checklist in the Score block.

## [1.0.0] — 2026-05-20 — first plugin release (P4)

### Added
- Claude Code **plugin packaging**: `.claude-plugin/plugin.json`, a single-plugin
  marketplace (`.claude-plugin/marketplace.json` at repo root), nested documented
  layout (`plugins/audit-write/skills/…`). Installable via `/plugin marketplace add`
  + `/plugin install`.
- Placeholder `agents/`, `hooks/`, `scripts/` directories (populated in P5).

### Changed
- Skills relocated under `plugins/audit-write/skills/`. They remain mutual siblings,
  so every `../audit-write/<bank>.md` reference resolves unchanged — **zero link
  migration**.

### Decided (schema-verified, docs 2026-05-19)
- **Cancelled** the long-deferred `assets/` foldering: sibling skills resolve relative
  links identically and the docs recommend relative paths for skill-markdown links;
  moving banks to `assets/` would be churn against the documented pattern. Banks stay
  in `skills/audit-write/`.
- No `commands/` layer — the 9 skills are directly invocable; wrappers were redundant.

## [P3] — 2026-05-20 — interview + progressive-outline ratchet

- New `audit-write-interview` skill: guided AskUserQuestion intake → canonical
  `paper-spec.md`.
- New hub assets: `paper_spec_template.md` (the context object every sub-skill
  consumes), `progressive_outline.md` (Stage 0–4 ratchet with approval gates).
- DRY: standard "Context source" pointer in all 6 section sub-skills — prefer an
  existing `paper-spec.md`, else `/audit-write-interview`; removed the duplicated
  per-skill "establish context" step.

## [P2] — 2026-05-20 — asset-library refactor

- Absorbed `audit-referee-response` as a bundled sub-skill.
- New shared banks: `rubric.md` (anchored 0–100 instrument + integrity gate),
  `null_and_identification_protocols.md`, `journal_profile_bank.md`, `move_bank.md`,
  `referee_objection_bank.md`, `exemplar_gallery.md`.
- Single-sourced the null-result protocol + numbered identification battery
  (was duplicated in 4 files).
- Two-tier hard-rule re-grade across all 8 SKILLs: integrity rules absolute;
  conventions = corpus priors (anchored to the verifiability note).
- Lazy-load policy in every sub-skill (~50% lower default context).
- All Mode-C scoring wired to the shared rubric. Tier-B banks passed proofreader +
  domain-reviewer; integrity gate confirmed.

## [P1] — 2026-05-20 — de-personalization + verifiability

- Removed a private running example; standardized on one generic `[ILLUSTRATIVE]`
  preparer-experience example across all section demos.
- Added `corpus_manifest.md`: shorthand-code decode, tiered evidentiary set, and the
  verifiability note ("k/6" = corpus prior, not law).
- Portability: dropped a hardcoded `~/.claude` path; registered shared resources.
- De-hallucination: fabricated benchmark citations → `[AUTHOR:]` slots.

## Forker note

This is a public template. Set `author`, `homepage`, `repository` in
`plugin.json`/`marketplace.json`, and follow the maintenance discipline in the
top-level `README.md` (pointer discipline, frequency re-derivation, single-source,
integrity-first, swap-corpus-keep-architecture).

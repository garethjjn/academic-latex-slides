# Changelog — audit-write

All notable changes to the audit-write skill suite. The pre-1.0 phases (P1–P3) were
the development arc that produced the first packaged plugin release.

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

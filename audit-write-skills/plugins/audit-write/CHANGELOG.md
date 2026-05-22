# Changelog — audit-write

All notable changes to the audit-write skill suite. The pre-1.0 phases (P1–P3) were
the development arc that produced the first packaged plugin release.

## [1.4.0] — 2026-05-22 — audit-write-review: four modular review modes + offline consistency check

### Added
- **Comprehensive review mode (new default).** One human-friendly report scored across
  **7 audit review dimensions** (research question & contribution · hypothesis & theory ·
  identification · measurement & construct validity · specification & inference · magnitude &
  economic significance · writing/structure/presentation), with Strengths / Major Concerns /
  Referee Objections / 1–5 dimension ratings — adapted from the generic comprehensive
  manuscript-review format and re-grounded in the suite's O1–O8 objection bank.
  Journal-agnostic. New `comprehensive_review_protocol.md`.
- **Consistency review mode (new).** A whole-paper *internal*-consistency audit — notation/
  terminology drift, claim parity across abstract↔intro↔results, and in-text-cite ↔
  bibliography coverage — backed by a bundled **stdlib Python** extractor
  (`scripts/consistency_check.py`, offline, read-only, advisory exit 0). Inspired by the
  *shape* of `jusi-aalto/crossref` (a SKILL doc + a `.py`) but uses **no network**: it checks
  the paper against itself rather than the Crossref API. New `consistency_review_protocol.md`.

### Changed
- **`audit-write-review` is now a slim 4-mode orchestrator** that interviews for the mode
  (unless the user names one) and routes to a per-mode protocol file:
  **comprehensive** (default) · **writing** · **peer** · **consistency**. The four are
  independent and not substitutes. `allowed-tools` gains `Bash` (to run the consistency script).
- **Writing review extracted** from the old inline SKILL.md block into its own
  `writing_review_protocol.md` (rubric instrument unchanged), with a plain-language verdict
  line added atop the report for readability.
- **Peer review: target journal is now optional.** If unstated and not inferable, the
  pipeline runs a journal-neutral disposition draw instead of blocking. Per-journal
  referee-pool weights + `journal_profile_bank.md` calibration are retained (peer is the only
  journal-calibrated mode; comprehensive/writing/consistency are journal-agnostic).
- **Human-friendlier reports across modes** — each report now leads with a plain-language
  headline/verdict before the structured tables (desk review, referee reports, editorial
  decision, writing review).

### Notes
- All four modes remain **read-only** and integrity-gated: no invented citations, results, or
  magnitudes; unknowns stay `[AUTHOR: …]`. The two peer-pipeline agents (`audit-editor`,
  `audit-referee-simulator`) are unchanged.

## [1.3.1] — 2026-05-22 — retarget to the accounting top-5 (AJPT → CAR + RAST)

### Changed
- **Journal calibration now spans the accounting top-5: JAE / JAR / TAR / CAR / RAST.**
  AJPT (*Auditing: A Journal of Practice and Theory*) is no longer a target desk; it is
  replaced by **CAR** (Contemporary Accounting Research) and **RAST** (Review of Accounting
  Studies). `journal_profile_bank.md` (single source) gains full CAR + RAST rows — profile
  table, reviewer culture, and inference cues:
  - **CAR** — rigorous clean archival design + clear *incremental* contribution;
    methodologically pluralistic; identification bar near JAR; broad/international generalizability.
  - **RAST** — financial-reporting-quality / capital-markets linkage + analytical-empirical;
    high identification bar; values economic significance and a clear economic/theory frame;
    shorter papers.
- Propagated the swap to every consumer: the `audit-editor` + `audit-referee-simulator`
  agent personas, the `audit-write-review` peer pipeline (calibration line, INSTITUTIONAL
  disposition lens, and the per-journal referee-pool weights table — AJPT column → CAR + RAST),
  `audit-referee-response` reviewer-culture section (AJPT subsection → CAR + RAST), the
  `paper-spec` target-journal field, and the hub inference-cue quick reference.
- **Roadmap convention is now TAR-only.** AJPT used to keep the end-of-intro roadmap; CAR and
  RAST follow the modern (no-roadmap) convention, so the rule is: keep for TAR, drop for
  JAE/JAR/CAR/RAST (intro_patterns.md, the intro SKILL.md, style_dna.md).
- **Robustness/identification battery default** now lists JAE/JAR/CAR/RAST (TAR alone tolerates
  a looser structure), in the robustness SKILL.md + null_and_identification_protocols.md.

### Notes
- AJPT remains where it is a **factual citation** (e.g. Nelson & Tan 2005, *AJPT* in the
  corpus manifest's review-structure benchmark) and in the source-PDF filename decode legend
  — it is dropped only as a *target* desk, not erased as a real journal.

## [1.3.0] — 2026-05-22 — whole-paper review: writing review + simulated peer-review pipeline (Opt. R4)

### Added
- **`audit-write-review` sub-skill** (1 hub + 8 → **9** bundled sub-skills). Interviews the
  user for the review *type*, then runs one of two distinct reviews:
  - **Writing review** — the suite's holistic AUDIT, run section by section against the
    shared `rubric.md` (integrity gate → binary pre-checklist → 5 weighted dimensions),
    optionally via the `audit-write-critic` agent for independent per-section scores.
    Writes a `writing_review.md` report into the same `audit_review_<paper>/` folder as
    the peer-mode reports (symmetric, persistable artifact — not just chat output).
  - **Peer review** — a simulated editorial pipeline calibrated to JAE/JAR/TAR/AJPT:
    editor desk review → two referees with deliberately different dispositions → editorial
    decision letter (Accept / Minor / Major / Reject), classifying every major concern
    FATAL / ADDRESSABLE / TASTE and tagging it with an O1–O8 code for the rebuttal.
- **`peer_review_protocol.md`** pattern file: the 6-way audit referee-disposition taxonomy
  (IDENTIFICATION · MEASUREMENT · CONTRIBUTION · INSTITUTIONAL · THEORY · GENERAL-SKEPTIC,
  each mapped to O-codes), per-journal referee-pool weights, audit-flavored critical/
  constructive peeve pools, the pipeline phases, the decision rule, and the four report
  templates (desk_review / referee_A / referee_B / editorial_decision).
- **`audit-editor` agent** (model: opus) — desk review + referee selection + editorial
  synthesis. Read-only; never rewrites; no WebSearch novelty probe (novelty is the
  CONTRIBUTION referee's job, argued from the manuscript, never asserted from invented work).

### Changed
- **`audit-referee-simulator` agent** is now **disposition-aware**: accepts an optional
  disposition + critical/constructive peeves (assigned by `audit-editor`) so two referees
  read the same paper from different priors; emits a 0–100 score with audit dimension
  weights + mandatory sanity-check blockers; every major comment now carries a
  "What would change my mind" line. Standalone single-referee use is unchanged.
- Hub `audit-write` `SKILL.md`: routing row + clarifying question + architecture diagram
  updated; the inline "review my whole paper" holistic audit now defers to
  `audit-write-review` for the full (esp. peer) experience.
- README: status, features, architecture, quick-start, repository-layout, and roadmap
  (Opt. R4) updated for the 9th sub-skill and the third agent.

### Notes
- **Distillation provenance:** the peer-review pipeline shape (editor + dispositioned
  referees, FATAL/ADDRESSABLE/TASTE, "what would change my mind", peeve injection) is
  adapted from the generic `review-paper --peer` workflow (itself from Hugo Sant'Anna's
  clo-author) and re-grounded in the audit desk — disposition taxonomy mapped to O1–O8,
  calibration via `journal_profile_bank.md`.
- **Scope:** core pipeline only — one fresh round, two referees, one decision. R&R
  continuation is handled by handing the decision letter to `audit-referee-response`;
  no hostile-editor stress mode and no N-referee variance distribution (deliberately
  out of scope to keep the distillation focused).

## [1.2.0] — 2026-05-22 — section gates + design/abstract/robustness deepening (Opt. R3)

### Added
- **Section-specific `check_structure.py` gates** that mechanize the rubric pre-checklist per
  section (the high-leverage enforcement layer; each held-out blind-eval confirmed gates move the
  score where digest content alone did not):
  - **intro:** a signed/directional prediction must be a displayed formal `H1.` (RQ-first intros exempt).
  - **design:** identification-machinery-deferred (existing) + numbered baseline equation + SE
    clustering + a descriptive-statistics block + controls tiered into ≥2 named groups.
  - **robustness:** a numbered / enumerated battery of ≥3 tests.
  - **abstract:** zero effect-size numbers (existing).
  Golden fixtures + tests for each (run_tests 15/15).
- **Stage-1 pilot digests** distilled into the pattern files: design (§13b, 13 papers),
  abstract (16 papers), robustness (§14b, 4 papers — see finding below). Each mirrors the lean
  digest form (per-paper table + reusable variants + retrieval guide).
- **Step-3 deterministic-gate sections** added to the design / robustness / abstract SKILL.md
  (intro / results / hypothesis already had them).

### Changed
- intro_patterns.md slimmed/harmonized (Opt. R2, also in 1.1.0 line) and design/abstract deepened
  over the Stage-1 pilot corpus. Held-out blind eval: design 82→85, abstract 90→92, robustness 82.

### Notes
- **Corpus finding:** only 4 of 16 pilot papers carry a *standalone* robustness section (the rest
  fold robustness into §4 results), so robustness received a *light* deepening (gate + 4-paper
  digest), not an n=22 deepening.
- `audit-referee-response` deepening is deferred to a later round (no paper-section to distill;
  it would deepen from the O1–O8 objection bank).

## [1.1.0] — 2026-05-22 — mechanism layer, corpus deepening, context slim

### Added
- **Corpus deepening (Stage 1).** Distilled 16 additional pilot papers × 3 sections
  (intro / hypothesis / results) into the pattern files; re-derived headline move
  frequencies over **n=22**; extended the exemplar gallery + move bank accordingly.
- **Intro formal-H gate (Round 2).** `check_structure.py --section intro` now flags a
  signed/directional prediction that is not crystallized as a displayed `H1.`; pure
  RQ-first intros stay exempt (`NA`). Golden fixtures + tests added.
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
- **Context economy (Round 2).** `intro_patterns.md` slimmed ~74% (120K→31K chars):
  kept the 5-block guidance, n=22 frequency tables, two anchor exemplars (`26-KLYY` +
  `19-JWW`), and the self-audit checklist; the other pilot intros moved to a compact
  digest + retrieval pointers, harmonizing intro with the hypothesis/results form.
  Held-out regression held composite at 90 (no regression vs the pre-slim 85).
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

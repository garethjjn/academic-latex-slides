# audit-write — Audit-Research Writing Skill Suite

> A Claude Code skill suite that drafts, rewrites, and audits empirical
> **audit-research** papers in a calibrated register reverse-engineered from a
> named corpus of published audit papers at top-tier accounting journals.
> Corpus-grounded, integrity-gated, and de-personalized for public reuse.

**Status:** v1.3.0 — packaged Claude Code **plugin** · 1 hub + 9 bundled sub-skills
(incl. `audit-write-interview` and `audit-write-review`) · 11 shared asset banks · staged drafting ratchet ·
0–100 rubric with an integrity gate · **section-specific mechanical self-check gates**
(`check_structure.py`) for intro / abstract / design / results / robustness · source
corpus disclosed in a manifest. See
[plugins/audit-write/CHANGELOG.md](plugins/audit-write/CHANGELOG.md) for the full release history.

---

## Table of contents

- [What this is](#what-this-is)
- [Why it is different](#why-it-is-different)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Quick start](#quick-start)
- [Using the suite: the recommended workflow](#using-the-suite-the-recommended-workflow)
- [Working on a single section: the three modes](#working-on-a-single-section-the-three-modes)
- [The scoring rubric & binary pre-checklist](#the-scoring-rubric--binary-pre-checklist)
- [The mechanism layer (P5): running the checks](#the-mechanism-layer-p5-running-the-checks)
- [The corpus & scientific discipline](#the-corpus--scientific-discipline)
- [Repository layout](#repository-layout)
- [Roadmap](#roadmap)
- [Maintenance discipline (for forkers)](#maintenance-discipline-for-forkers)
- [Scope, limitations & licensing](#scope-limitations--licensing)

---

## What this is

`audit-write` is a set of Claude Code **skills** for writing empirical accounting/audit
papers aimed at top-tier accounting journals. It does three things for any
section of a paper:

- **DRAFT** a section from your notes (research question, DV, IV, setting, finding),
- **REWRITE** an existing draft into the target register, with a paragraph-level change log,
- **AUDIT** a draft against a fixed, anchored rubric (no rewriting — diagnosis only).

It is **not** a generic academic-writing assistant. The structural conventions, verb
register, hedging vocabulary, magnitude-reporting rules, identification rhetoric, and
contribution formulas are reverse-engineered from a **named corpus** of published audit
papers and encoded as section-specific templates.

## Why it is different

| Generic writing assistant | `audit-write` |
|---|---|
| "Write good academic prose" | Section-specific anatomies (5-block intro, 5-move abstract, 4/6-move hypothesis, 5-part design, 6-sub-section results, numbered robustness battery, 4-move rebuttal) |
| Invents plausible-sounding citations | **Integrity gate**: any fabricated citation/result/number caps the score at 55/100; unknowns must be `[AUTHOR: …]` placeholders |
| Generic confidence | Calibrated, corpus-derived register: verb whitelist/blacklist, banned marketing adjectives, anti-AI tells |
| Rules asserted as universal | Rules **graded**: integrity rules are absolute; conventions are *corpus priors you may override with a stated reason* |
| Opaque basis | Every "k/6" frequency claim is traceable to a disclosed corpus (`corpus_manifest.md`) |

## Features

- **Hub-and-spoke.** One dispatcher (`audit-write`) + 9 bundled sub-skills: the
  interview/progressive-outline intake, abstract, intro, hypothesis, design, results,
  robustness, review, and referee-response.
- **3 operating modes** per section sub-skill: DRAFT / REWRITE / AUDIT.
- **Whole-paper review in two senses** (`audit-write-review`, interviews you for which):
  a rubric-scored **writing** review, or a simulated **peer**-review pipeline (editor desk
  review → two referees with deliberately different dispositions → editorial decision letter,
  calibrated to JAE/JAR/TAR/AJPT, every concern tied to an O1–O8 objection code).
- **9 shared asset banks** (single-sourced, no duplication): style DNA, audit-quality
  framework, corpus manifest, scoring rubric, null/identification protocols, journal
  profile bank, move bank, referee-objection bank, exemplar gallery.
- **Anchored 0–100 rubric with an integrity gate** — reproducible scores across sections
  and sessions; the same instrument the (planned) critic agent will use.
- **Corpus-grounded & verifiable** — a manifest decodes every shorthand code
  (`07-DHT` … `26-KLYY`) to a real citation and states the verifiability boundary.
- **Calibrated, non-dogmatic rules** — a two-tier "how to read these" preamble in every
  skill separates absolute integrity rules from overridable corpus priors.
- **Context-economical** — a lazy-load policy tells each skill to read only its own
  pattern file + style DNA + rubric up front, and the heavier banks on demand.
- **De-personalized** — ships one generic `[ILLUSTRATIVE]` worked example
  (audit-partner preparer experience → audit quality); no private project content.

## Architecture

```
audit-write  (hub: dispatcher + 9 shared asset banks)
├── audit-write-abstract        5-move / 6-sentence abstract
├── audit-write-intro       ★   5-block introduction ("75% of acceptance")
├── audit-write-hypothesis      4-/6-move arc + pair-prediction device
├── audit-write-design          5-part §3 (identification deferred to §4)
├── audit-write-results         6-sub-section §4 + magnitude translation
├── audit-write-robustness      numbered identification battery
├── audit-write-review          whole-paper review: writing (rubric) OR peer (editor + 2 referees)
└── audit-referee-response      4-move point-by-point rebuttal

agents:  audit-write-critic (writing scorer) · audit-referee-simulator (referee persona,
         disposition-aware) · audit-editor (desk review + referee selection + synthesis)
```

Sub-skills consult the hub's banks via `../audit-write/<bank>.md`. Two banks
(`move_bank`, `exemplar_gallery`) are **indexes that point into** the section pattern
files rather than copies — this keeps verbatim corpus exemplars in one place so the
quote→source verifiability chain is never broken.

## Installation

This repo is a single-plugin **Claude Code marketplace**. No build step, no
dependencies, no API keys.

**A — Install as a plugin (recommended)**

```
/plugin marketplace add <this-repo-url-or-local-path>
/plugin install audit-write@audit-write-marketplace
```

(`/plugin marketplace add .` works if you cloned the repo and Claude Code is launched
from its root.) The plugin's skills, agents, and hooks are auto-discovered from
`plugins/audit-write/`.

**B — Manual skills install (no plugin system)**

Copy the skill directories under your Claude Code skills folder
(`~/.claude/skills/` · Windows `%USERPROFILE%\.claude\skills\`). Keep the layout — the
sub-skills resolve shared banks via the relative path `../audit-write/`.

```bash
cp -r plugins/audit-write/skills/* ~/.claude/skills/        # macOS/Linux
```
```powershell
Copy-Item -Recurse -Force plugins\audit-write\skills\* $env:USERPROFILE\.claude\skills\   # Windows
```

Then verify in Claude Code:

```
/audit-write what's the audit-quality framework?
```

If registered you'll get the framework reference and a routing offer.

## Quick start

```
/audit-write help me start a paper          # → interview, then progressive outline
/audit-write-review review my whole paper    # → interviews: writing review, peer review, or both
/audit-write which sub-skill for my Section 2?
```

Or go straight to one section in one of the three modes:

```
/audit-write-intro draft an intro from these notes: <RQ, DV, IV, setting, finding>
/audit-write-results rewrite my §4 for JAE style: <paste draft>
/audit-write-abstract audit my abstract: <paste abstract>
```

## Using the suite: the recommended workflow

The suite is built around **progressive outlining**: never have the model
produce a final draft in one shot. You ratchet through resolution levels with an
approval gate at each step, because **editing an outline is high-leverage and
editing prose is not** — changing a few words of a skeleton line reorganises a
whole section, while changing the same words in finished prose changes only
those words. The rationale and its provenance are in
[progressive_outline.md](plugins/audit-write/skills/audit-write/progressive_outline.md)
and [docs/external-validation-ng.md](plugins/audit-write/docs/external-validation-ng.md).

Run the whole thing with one command and let the gates pace you:

```
/audit-write draft my whole paper        # runs Stage 0 → 4
```

What each stage produces and where it stops for you:

| Stage | Trigger | Produces | Gate (it stops here) |
|---|---|---|---|
| **0 Interview** | `/audit-write-interview` or "help me start a paper" | `paper-spec.md` — RQ, DV, IV, setting, the FOR (mechanism) **and the AGAINST** (tension), pejorative-reading risk, contributions | You confirm the spec; any BLOCKED field halts the ratchet here |
| **1 Skeleton** | "outline first" / auto after Stage 0 | `outline.md` — one line per block/move, no prose | You edit/approve the structure before any argument is written |
| **2 Bullets** | auto after Stage 1 approval | `outline.md` — bullet claims + `[AUTHOR:]` slots | You approve the argument/logic before any prose cost |
| **3 Prose** | auto after Stage 2 approval | draft, **one block at a time** (routed to the section sub-skill) | Per-block accept / revise |
| **4 Self-audit** | auto after prose | rubric score + fixes (integrity gate first) | Score reported: ≥90 ship · 75–89 revise · <75 do not ship |

Two enforced behaviours that shape the workflow:

- **Surface the AGAINST before Stage 1.** Stage 0 captures the counter-argument
  and pejorative-reading risk as required spec fields, and the hypothesis
  section's tension paragraph is mandatory — the structure answers the likely
  reviewer objection (catalogued O1–O8) instead of retrofitting it into finished
  prose.
- **You may collapse, not skip.** "Just draft it" lets the model fold Stages 1–2
  together, but it must still show you the skeleton before writing prose. Gates
  are not optional by default.

State persists to `paper-spec.md` and `outline.md` in your working directory, so
the workflow survives a context reset and every section reuses the same spec
(no re-interviewing).

## Working on a single section: the three modes

Every section sub-skill runs in one of three modes — name the mode in your prompt:

- **DRAFT** — build the section from your notes; unknowns become `[AUTHOR: …]` slots.
- **REWRITE** — recast an existing draft into the register, with a paragraph-level change log.
- **AUDIT** — read-only diagnosis + a rubric Score block; no rewriting.

```
# DRAFT
/audit-write-intro draft intro. RQ: do audit partners with prior preparer
experience provide higher audit quality? Setting: partner-firm-years,
engagement-partner-disclosure regime. Finding: −1.8 pp restatements
(15% of base). Target: JAE.
→ 5-block intro, [AUTHOR:] slots, a magnitude in Block 4, numbered
  contributions, a self-audit.

# REWRITE
/audit-write-results rewrite my §4 for JAE style: <paste draft>
→ recast §4 + a paragraph-level change log.

# AUDIT
/audit-write-results audit my §4: <paste>
→ sub-section-by-sub-section diagnosis + the rubric Score block.

# Whole-paper review (interviews you for which review you want)
/audit-write-review review my paper for JAR: <path or pasted sections>
→ asks: (1) WRITING review (rubric-scored register/structure, section-by-section),
  (2) PEER review (editor desk → 2 dispositioned referees → decision letter), or (3) both.
  Both modes write a markdown report into one audit_review_<paper>/ folder: writing_review.md
  (writing mode) and desk_review / referee_A / referee_B / editorial_decision (peer mode,
  every concern tagged with its O-code for the rebuttal).

# Referee response (R&R)
/audit-referee-response draft a response to Reviewer 2's
"identification is weak" comment: <paste comment>
→ 4-move response (acknowledge → reframe → action → location),
  drawing on the O1–O8 objection bank, with [AUTHOR: run …] slots.
```

Sub-skills: `audit-write-abstract` · `-intro` · `-hypothesis` · `-design` ·
`-results` · `-robustness` · `-review` · `audit-referee-response`. Invoke the hub
`/audit-write` if you are unsure which one you need.

## The scoring rubric & binary pre-checklist

Every AUDIT, the holistic review, and the `audit-write-critic` agent score with
one shared instrument
([rubric.md](plugins/audit-write/skills/audit-write/rubric.md)). It runs in three
layers, in order:

1. **Integrity gate (first, pass/fail).** Any fabricated citation, invented
   result, or invented magnitude presented as real → total **capped at 55/100
   (FAIL)**, offending spans named. Unknowns must be `[AUTHOR: …]` slots.
2. **Binary pre-checklist (objective, before banding).** Seven yes/no items —
   answered literally Y/N/NA, nothing in between — remove the wiggle room that
   lets a free-form critique drift upward (sycophancy). Any **N forces its mapped
   dimension down one band**; C1/C2 = N trips the integrity gate.

   | # | Binary check | Maps to |
   |---|---|---|
   | C1 | every hard `(Name, Year)` cite is a sanctioned anchor or an `[AUTHOR:]` slot | gate + Dim 3 |
   | C2 | no invented numeric result/magnitude presented as real | gate + Dim 3 |
   | C3 | zero blacklist verbs in claim sentences | Dim 2 |
   | C4 | zero AI-slop tells (em-dash overuse, "not X but Y", reflexive triads, mood-adjective+abstract-noun) | Dim 2 |
   | C5 | the section's mandatory element is present (intro: a magnitude; abstract: **zero** effect numbers; hypothesis: a tension paragraph; design: identification machinery **out** of §3) | Dim 1 |
   | C6 | every reported effect is magnitude-anchored where required (or honest `[AUTHOR:]`) | Dim 3 |
   | C7 | each contribution names an identifiable literature | Dim 4 |

3. **5 weighted dimensions, anchored bands.** structure (20) · DeFond register
   (20) · magnitude & evidentiary discipline (25) · argument & contribution
   clarity (20) · audit vocabulary (15). Bands: 90–100 / 75–89 / 60–74 / <60.

**Ship thresholds:** ≥90 ship-ready · 75–89 revise-then-ship · <75 do not ship.
The Score block prints the C1–C7 line, the per-dimension bands, the composite,
the integrity-gate line, and one headline fix.

## The mechanism layer (P5): running the checks

The integrity gate, the AI-slop tells, and link health are also enforced
*mechanically* by stdlib-only Python scripts (no dependencies, no API keys).
They are advisory aids to the rubric, not a replacement for it.

```
# golden tests — proves the mechanism layer works (run from anywhere)
python plugins/audit-write/tests/run_tests.py

# style/integrity linter — point at a GENERATED DRAFT, not the skill docs
python plugins/audit-write/scripts/lint_style.py mydraft.md
#   ERROR personalization token / suspected fabricated cite   → exit 1
#   WARN  blacklist verb · em-dash overuse · "not X … it's Y"  → never fails

# binary self-check — the mechanism mirror of the rubric pre-checklist
python plugins/audit-write/scripts/check_structure.py mydraft.md --section intro
#   prints C1/C3/C4/C5/C6 as literal Y/N/NA; always exit 0 (advisory)

# link health — every intra-suite Markdown reference resolves
python plugins/audit-write/scripts/check_links.py
```

`lint_style.py` is **draft-only by design** — the skill docs quote banned verbs
as negative examples and would false-positive. The em-dash and "not X … it's Y"
detectors are deliberately conservative (≥3 em-dashes + density; the mirrored
form only) so they never fire on legitimate audit prose such as "not significant
but economically large". `check_links.py` also runs automatically as a
`PostToolUse` hook on every Write/Edit. Rule-of-three and empty-grand-claim are
caught at the instruction layer (`style_dna.md` §9), not mechanically — see
[docs/external-validation-ng.md](plugins/audit-write/docs/external-validation-ng.md)
for why.

## The corpus & scientific discipline

The pattern files distill a fixed, named corpus of audit papers. `audit-write/corpus_manifest.md` decodes every shorthand code to a real
citation, tiers the full evidentiary set, and states the rules of engagement:

- **Frequency claims are corpus priors, not laws.** "6/6 papers do X" means *the named
  corpus is unanimous* — a strong default you may override with a stated reason, not a
  rule of the field.
- **Quotes are traceable.** Verbatim exemplars and `¶`-anchors resolve to plain-text
  extractions of the source papers.
- **No evidence is manufactured.** Substantive citations are always `[AUTHOR: …]`
  slots; only a small set of sanctioned methodological anchors appear as hard cites.

This suite ships the **distilled patterns only** — not the source PDFs (third-party
copyright). It is a writing *register and structure* tool, not a guarantee of
acceptance.

## Repository layout

```
audit-write-skills/                     ← repo = single-plugin marketplace
├── README.md                           ← this file
├── .claude-plugin/
│   └── marketplace.json                ← lists the plugin (source ./plugins/audit-write)
└── plugins/
    └── audit-write/                    ← THE plugin
        ├── .claude-plugin/plugin.json
        ├── CHANGELOG.md
        ├── agents/                     ← critic + referee-simulator + editor (peer review)
        ├── hooks/                      ← hooks.json (P5)
        ├── scripts/                    ← stdlib checks (P5)
        └── skills/
            ├── audit-write/            ← hub skill + 11 shared banks
            │   ├── SKILL.md
            │   ├── style_dna.md  audit_quality_framework.md  corpus_manifest.md
            │   ├── rubric.md  null_and_identification_protocols.md
            │   ├── journal_profile_bank.md  move_bank.md
            │   ├── referee_objection_bank.md  exemplar_gallery.md
            │   ├── progressive_outline.md      ← Stage 0–4 ratchet
            │   └── paper_spec_template.md      ← canonical context object
            ├── audit-write-interview/  (SKILL.md — Stage 0 intake)
            ├── audit-write-abstract/   (SKILL.md + abstract_patterns.md)
            ├── audit-write-intro/      (SKILL.md + intro_patterns.md + contribution_formulas.md)
            ├── audit-write-hypothesis/ (SKILL.md + hypothesis_patterns.md)
            ├── audit-write-design/     (SKILL.md + design_patterns.md)
            ├── audit-write-results/    (SKILL.md + results_patterns.md)
            ├── audit-write-robustness/ (SKILL.md + robustness_patterns.md)
            ├── audit-write-review/     (SKILL.md + peer_review_protocol.md)
            └── audit-referee-response/ (SKILL.md)
```

All skill dirs are mutual siblings under `skills/`, so every `../audit-write/<bank>.md`
reference resolves unchanged whether installed as a plugin or copied manually.

## Roadmap

| Phase | Scope | Status |
|---|---|---|
| P1 | De-personalize · corpus manifest · portability | ✅ done |
| P2 | Asset-library refactor · rubric · hard-rule re-grade · lazy-load · absorb referee | ✅ done |
| P3 | Interview intake + progressive-outline ratchet + DRY context object | ✅ done |
| P4 | Claude Code **plugin** packaging (`plugin.json` + single-plugin marketplace; `assets/` foldering cancelled — schema-verified unnecessary) | ✅ done |
| P5 | Mechanism layer: hook-enforced integrity/link checks, critic + referee-simulator agents, golden tests | ✅ done |
| Opt. R1–R3 | Mechanize the rubric pre-checklist as `check_structure.py` section gates (intro formal-H · design equation/clustering/descriptive-stats/control-tiering · robustness numbered-battery · abstract zero-magnitude); slim/harmonize intro; deepen design/abstract over the Stage-1 pilot corpus; held-out blind eval per change | ✅ done |
| Opt. R4 | **Whole-paper review** sub-skill (`audit-write-review`): interview-driven choice of a rubric-scored *writing* review vs a simulated *peer*-review pipeline (new `audit-editor` agent; disposition-aware `audit-referee-simulator`); audit disposition taxonomy mapped onto the O1–O8 bank | ✅ done |

**Honest status:** the integrity gate and lazy-load policy are currently *instructions
the agent is told to follow*, not mechanically enforced — enforcement is P5. Quality is
verified structurally and by review, not yet measured against generated output. P5 also
adds a binary pre-checklist to the rubric and stdlib AI-slop detectors; the rationale
(an independent account corroborating the suite's two pillars) is recorded in
[plugins/audit-write/docs/external-validation-ng.md](plugins/audit-write/docs/external-validation-ng.md).

## Maintenance discipline (for forkers)

This suite is a public template. If you fork it for your field:

1. **Pointer discipline.** `move_bank.md` and `exemplar_gallery.md` point into pattern
   files; if you restructure a pattern file, update the pointers (they fail silently).
2. **Frequency re-derivation.** Any "k/6" is over the named corpus. If you change the
   corpus, re-derive the counts — do not leave a stale `k/6` (`corpus_manifest.md` §5.3).
3. **Single source.** The null/identification protocol, journal conventions, and rubric
   live once in the hub banks. Don't re-state them in skills; link.
4. **Integrity first.** Never replace `[AUTHOR: …]` slots with invented citations to
   "make it look finished." The rubric integrity gate exists to catch exactly this.
5. **Swap the corpus, keep the architecture.** The hub-spoke + banks + rubric structure
   is field-agnostic; the *content* is audit-specific. Replace `corpus_manifest.md` and
   the pattern files; keep the scaffolding.

## Scope, limitations & licensing

- **Evidence base is small and correlated.** The corpus is DeFond-coauthored /
  China / partner-trait-heavy. The manifest discloses this; the rules are framed as
  priors accordingly. Best fit: archival audit-quality papers for JAE/JAR/TAR. Weaker
  fit: experimental audit, pure-US settings, non-accounting — the suite will say so and
  defer.
- **Not a guarantee.** It encodes a register and structure, not a path to acceptance.
- **Licensing.** Distilled patterns are the project's own work and reusable. Source
  papers are **not** redistributed; obtain them from their publishers via the manifest
  citations. The suite is fully usable without them.

## Acknowledgments

- **Maintainer:** Gareth Jiang.
- **Built with [Claude](https://www.anthropic.com/claude) (Anthropic) in Claude Code.**
  Claude was a substantial co-developer of this suite — corpus distillation into the
  pattern files and digests, the section-specific `check_structure.py` gates and golden
  tests, the progressive-outline ratchet, and the held-out blind-eval methodology were
  developed in collaboration with Claude. Final design decisions, the corpus selection,
  and review are the maintainer's.

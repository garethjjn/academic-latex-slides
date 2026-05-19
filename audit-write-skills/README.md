# audit-write — Audit-Research Writing Skill Suite

> A Claude Code skill suite that drafts, rewrites, and audits empirical
> **audit-research** papers in the DeFond / Zuo / Khurana register, targeting
> **JAE · JAR · TAR**. Corpus-grounded, integrity-gated, and de-personalized for
> public reuse.

**Status:** v2 (post asset-library refactor) · 1 hub + 7 bundled sub-skills · 9 shared
asset banks · scoring rubric with an integrity gate · evidence base disclosed in a
corpus manifest.

---

## Table of contents

- [What this is](#what-this-is)
- [Why it is different](#why-it-is-different)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Quick start](#quick-start)
- [Usage examples](#usage-examples)
- [The scoring rubric](#the-scoring-rubric)
- [The corpus & scientific discipline](#the-corpus--scientific-discipline)
- [Repository layout](#repository-layout)
- [Roadmap](#roadmap)
- [Maintenance discipline (for forkers)](#maintenance-discipline-for-forkers)
- [Scope, limitations & licensing](#scope-limitations--licensing)

---

## What this is

`audit-write` is a set of Claude Code **skills** for writing empirical accounting/audit
papers aimed at the top-3 accounting journals (Journal of Accounting and Economics,
Journal of Accounting Research, The Accounting Review). It does three things for any
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
| Generic confidence | Calibrated DeFond register: verb whitelist/blacklist, banned marketing adjectives, anti-AI tells |
| Rules asserted as universal | Rules **graded**: integrity rules are absolute; conventions are *corpus priors you may override with a stated reason* |
| Opaque basis | Every "k/6" frequency claim is traceable to a disclosed corpus (`corpus_manifest.md`) |

## Features

- **8 skills, hub-and-spoke.** One dispatcher (`audit-write`) + 7 bundled sub-skills:
  abstract, intro, hypothesis, design, results, robustness, referee-response.
- **3 operating modes** per sub-skill: DRAFT / REWRITE / AUDIT.
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
└── audit-referee-response      4-move point-by-point rebuttal
```

Sub-skills consult the hub's banks via `../audit-write/<bank>.md`. Two banks
(`move_bank`, `exemplar_gallery`) are **indexes that point into** the section pattern
files rather than copies — this keeps verbatim corpus exemplars in one place so the
quote→source verifiability chain is never broken.

## Installation

These are **Claude Code skills**. Install by placing each skill directory under your
Claude Code skills folder (`~/.claude/skills/` on macOS/Linux,
`C:\Users\<you>\.claude\skills\` on Windows). Keep the directory layout intact — the
sub-skills resolve shared banks via the relative path `../audit-write/`.

**macOS / Linux**

```bash
cp -r audit-write-skills/* ~/.claude/skills/
```

**Windows (PowerShell)**

```powershell
Copy-Item -Recurse -Force audit-write-skills\* $env:USERPROFILE\.claude\skills\
```

Then verify in Claude Code:

```
/audit-write what's the DeFond audit-quality framework?
```

If the skills are registered you will get the framework reference and a routing offer.
No build step, no dependencies, no API keys. (Plugin packaging — a single
`/plugin install` — is roadmap item P4.)

## Quick start

Invoke the hub when you are unsure which section you need; it routes you:

```
/audit-write review my whole audit paper
/audit-write which sub-skill should I use for my Section 2?
```

Or invoke a sub-skill directly with one of the three modes:

```
/audit-write-intro draft an intro from these notes: <RQ, DV, IV, setting, finding>
/audit-write-results rewrite my §4 for JAE style: <paste draft>
/audit-write-abstract audit my abstract for DeFond style: <paste abstract>
```

## Usage examples

**1 — Draft an introduction (Mode A).**

```
/audit-write-intro draft intro. RQ: do audit partners with prior preparer
experience provide higher audit quality? Setting: partner-firm-years, engagement-
partner-disclosure regime. Finding: −1.8 pp restatements (15% of base). Target: JAE.
```

Returns a 5-block intro with `[AUTHOR: …]` placeholders for anything you did not
supply, a magnitude in Block 4, numbered contributions, and a self-audit.

**2 — Audit an existing results section (Mode C).**

```
/audit-write-results audit my §4: <paste>
```

Returns a sub-section-by-sub-section diagnosis and the rubric Score block
(per-dimension band → composite → **integrity-gate line** → one headline fix).

**3 — Holistic review across the whole paper.**

```
/audit-write review the whole paper: <paths or pasted sections>
```

Routes each section through its sub-skill and returns a combined report with a
top-issues list.

**4 — Respond to referees (R&R).**

```
/audit-referee-response draft a response to Reviewer 2's comment that our
identification is weak: <paste comment>
```

Returns a 4-move response (acknowledge → reframe → action → location) drawing on the
O1–O8 objection bank, with `[AUTHOR: run …]` slots for any new analysis.

## The scoring rubric

Every AUDIT and the holistic review score with one shared instrument
([`audit-write/rubric.md`](audit-write/rubric.md)):

- **Integrity gate (applied first).** Any fabricated citation, invented result, or
  invented magnitude presented as real → total **capped at 55/100 (FAIL)**, offending
  spans named.
- **5 weighted dimensions:** structure (20) · DeFond register (20) · magnitude &
  evidentiary discipline (25) · argument & contribution clarity (20) · audit vocabulary
  (15). Anchored bands: 90–100 / 75–89 / 60–74 / <60.
- **Ship thresholds:** ≥90 ship-ready · 75–89 revise-then-ship · <75 do not ship.

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
audit-write-skills/
├── README.md                       ← this file
├── audit-write/                    ← hub skill
│   ├── SKILL.md
│   ├── style_dna.md                verb register, hedging, anti-AI tells
│   ├── audit_quality_framework.md  DeFond-Zhang taxonomy + glossary
│   ├── corpus_manifest.md          provenance + verifiability note
│   ├── rubric.md                   0–100 instrument + integrity gate
│   ├── null_and_identification_protocols.md
│   ├── journal_profile_bank.md     JAE/JAR/TAR/AJPT conventions
│   ├── move_bank.md                cross-section move index
│   ├── referee_objection_bank.md   O1–O8 objection→response catalog
│   └── exemplar_gallery.md         navigational index of annotated exemplars
├── audit-write-abstract/  (SKILL.md + abstract_patterns.md)
├── audit-write-intro/     (SKILL.md + intro_patterns.md + contribution_formulas.md)
├── audit-write-hypothesis/(SKILL.md + hypothesis_patterns.md)
├── audit-write-design/    (SKILL.md + design_patterns.md)
├── audit-write-results/   (SKILL.md + results_patterns.md)
├── audit-write-robustness/(SKILL.md + robustness_patterns.md)
└── audit-referee-response/(SKILL.md)
```

## Roadmap

| Phase | Scope | Status |
|---|---|---|
| P1 | De-personalize · corpus manifest · portability | ✅ done |
| P2 | Asset-library refactor · rubric · hard-rule re-grade · lazy-load · absorb referee | ✅ done |
| P3 | Interview-driven requirements + progressive-outlining commands | planned |
| P4 | Claude Code **plugin** packaging (`plugin.json`, marketplace, `${CLAUDE_PLUGIN_ROOT}`, `assets/` foldering) | planned |
| P5 | Mechanism layer: hook-enforced integrity/link checks, critic + referee-simulator agents, golden tests | planned |

**Honest status:** the integrity gate and lazy-load policy are currently *instructions
the agent is told to follow*, not mechanically enforced — enforcement is P5. Quality is
verified structurally and by review, not yet measured against generated output.

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

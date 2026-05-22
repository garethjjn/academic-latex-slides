# audit-write — an AI writing suite for audit-research papers

![version](https://img.shields.io/badge/version-1.3.1-blue)
![license](https://img.shields.io/badge/license-MIT-green)
![Claude Code](https://img.shields.io/badge/Claude%20Code-plugin-8A2BE2)
![journals](https://img.shields.io/badge/calibrated%20to-JAE%20·%20JAR%20·%20TAR%20·%20CAR%20·%20RAST-lightgrey)
![tests](https://img.shields.io/badge/golden%20tests-15%2F15-brightgreen)

> A **Claude Code** plugin that helps you **draft, rewrite, audit, and peer-review**
> empirical **audit-research** papers in the calibrated register of the accounting
> top-5 (JAE, JAR, TAR, CAR, RAST). The structure, tone, and rules are
> reverse-engineered from a named corpus of published audit papers — not invented by a
> chatbot. It never fabricates citations or numbers, and it tells you exactly where its
> rules come from.

It is a **writing register-and-structure tool**, not a content generator: you supply the
research idea and the results; the suite makes the paper *read and stand up* like an
accepted top-5 audit paper.

---

## Table of contents

- [Who this is for](#who-this-is-for)
- [What it does — a 30-second example](#what-it-does--a-30-second-example)
- [New to Claude Code? Start here](#new-to-claude-code-start-here)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Your first 10 minutes (tutorial)](#your-first-10-minutes-tutorial)
- [The features, in plain language](#the-features-in-plain-language)
  - [The 9 sub-skills](#the-9-sub-skills)
  - [The three working modes](#the-three-working-modes)
  - [Whole-paper review (writing review + peer review)](#whole-paper-review-writing-review--peer-review)
  - [The 0–100 quality rubric](#the-0100-quality-rubric)
  - [The optional mechanism layer (Python checks)](#the-optional-mechanism-layer-python-checks)
- [The recommended workflow: progressive outlining](#the-recommended-workflow-progressive-outlining)
- [Why it is different from "ask ChatGPT to write my paper"](#why-it-is-different-from-ask-chatgpt-to-write-my-paper)
- [The corpus & scientific discipline](#the-corpus--scientific-discipline)
- [Glossary](#glossary)
- [FAQ & troubleshooting](#faq--troubleshooting)
- [Architecture & repository layout](#architecture--repository-layout)
- [Customizing / forking for your field](#customizing--forking-for-your-field)
- [Roadmap](#roadmap)
- [Scope, limitations & licensing](#scope-limitations--licensing)
- [Acknowledgments](#acknowledgments)

---

## Who this is for

- **Accounting / auditing PhD students and faculty** writing archival audit-quality
  papers for JAE, JAR, TAR, CAR, or RAST.
- Researchers who can describe their **research question, variables, setting, and
  findings**, and want the paper *written, tightened, and stress-tested* in the
  conventions reviewers at those journals expect.
- **People who have never used an AI "agent" before.** You do not need to know how
  Claude Code works — the [Start here](#new-to-claude-code-start-here) section walks you
  through it from zero.

You do **not** need to be a programmer. The only tool you install is Claude Code; the
suite itself has no code dependencies, no build step, and no API keys.

---

## What it does — a 30-second example

You give it your raw research notes:

```
/audit-write-intro draft an introduction.
RQ: do audit partners with prior financial-statement-preparer experience deliver
higher audit quality? Setting: engagement-partner-disclosure regime, partner-firm-years.
Finding: restatements fall 1.8 percentage points (≈15% of the base rate). Target: JAE.
```

It returns a journal-ready **5-block introduction** in the conventional audit-research
voice — motivation → gap → theory-with-tension → setting → findings-with-magnitude —
with numbered contributions, the required economic magnitude in the findings block, and
**`[AUTHOR: …]` placeholders** anywhere a citation or number would be needed (it never
makes those up). Then it **scores its own draft** against a fixed rubric and tells you
the single highest-leverage fix.

Other things you can ask it to do:

| You want to… | Command |
|---|---|
| Turn rough notes into a structured paper spec, then outline it | `/audit-write-interview` |
| Rewrite a clunky results section into JAE style | `/audit-write-results rewrite my §4: <paste>` |
| Get a brutally honest quality score on your abstract | `/audit-write-abstract audit my abstract: <paste>` |
| Run a mock editor + 2 referees and get a decision letter | `/audit-write-review peer review my paper for JAR: paper.pdf` |
| Draft a point-by-point response to a reviewer | `/audit-referee-response respond to R2's "identification is weak": <paste>` |

---

## New to Claude Code? Start here

If you have never used Claude Code or an AI "agent", read this once. Five terms is all
you need:

- **Claude Code** — Anthropic's AI assistant that runs in your terminal (or VS Code /
  JetBrains). You type requests in plain English; it reads your files and helps you work.
  Get it at **<https://claude.com/code>**.
- **A "skill"** — a packaged set of expert instructions Claude loads on demand. You
  trigger one by typing a slash command, e.g. `/audit-write-intro`. Think of it as
  hiring a specialist for one job.
- **A "plugin"** — a bundle of related skills (plus agents and helper scripts) you
  install in one step. **`audit-write` is one plugin** containing 9 skills.
- **An "agent"** — a focused helper a skill can spin up for a sub-task (here: a
  referee, an editor, a scorer). You normally don't call agents directly; the skills do.
- **A "marketplace"** — the place Claude Code installs plugins from. This GitHub repo
  *is* a marketplace.

**How you actually use it:** open Claude Code, type a slash command like
`/audit-write help me start a paper`, press Enter, and answer its questions in plain
English. That's the whole interaction model.

---

## Prerequisites

1. **Claude Code installed and working.** Follow the official guide at
   <https://docs.claude.com/en/docs/claude-code> (it works on macOS, Windows, and Linux,
   in the terminal or as a VS Code / JetBrains extension). Using Claude Code requires a
   Claude account (a Pro/Max subscription or API billing) — see Anthropic's site for
   current options.
2. **(Optional) Python 3.8+** — only if you want to run the optional mechanical
   self-check scripts. The skills themselves do not need Python. The scripts use the
   standard library only — nothing to `pip install`.

That's it. No Git knowledge required to *use* the suite (though you'll use Git if you
fork it).

---

## Installation

### Option A — Install as a plugin (recommended)

Inside Claude Code, run these two commands:

```text
/plugin marketplace add garethjjn/auditing-research-writing-skills
/plugin install audit-write@audit-write-marketplace
```

The first line registers this repo as a marketplace; the second installs the plugin.
Claude Code auto-discovers the skills, agents, and hooks. (You can also point
`/plugin marketplace add` at a local folder path if you cloned the repo.)

### Option B — Manual install (no plugin system)

Copy the skill folders into your Claude Code skills directory, keeping the layout intact
(the sub-skills find their shared files via the relative path `../audit-write/`):

```bash
# macOS / Linux
cp -r plugins/audit-write/skills/* ~/.claude/skills/
```
```powershell
# Windows (PowerShell)
Copy-Item -Recurse -Force plugins\audit-write\skills\* $env:USERPROFILE\.claude\skills\
```

### Verify it works

In Claude Code, type:

```text
/audit-write what is the audit-quality framework?
```

If the plugin is live, you'll get the DeFond–Zhang audit-quality definition and an offer
to route you to the right sub-skill. You're ready.

> **Updating later:** plugins installed from this repo auto-update on the next Claude
> Code restart (or run the update option in the `/plugin` menu). See the
> [FAQ](#faq--troubleshooting).

---

## Your first 10 minutes (tutorial)

This walks a new user from zero to a drafted, self-scored section.

**1. Open Claude Code in your paper's folder.** In a terminal:

```bash
cd path/to/my-paper
claude
```

Working inside your paper's folder lets the suite save a `paper-spec.md` and `outline.md`
there and reuse them across sessions.

**2. Let it interview you.** Type:

```text
/audit-write-interview
```

It asks a short, structured set of questions — your research question, dependent and
independent variables, the institutional setting, the *mechanism* you expect (the "for"),
the **counter-argument** (the "against"), and your intended contributions. It writes your
answers to `paper-spec.md`. Every later step reuses this file, so you only answer once.

**3. Outline before prose.** Type:

```text
/audit-write draft my whole paper
```

The suite runs a **progressive outline** (skeleton → bullet claims → prose, one block at
a time), pausing for your approval at each step. Editing a one-line skeleton is far
cheaper than rewriting finished paragraphs — that's the whole point. (See
[the workflow section](#the-recommended-workflow-progressive-outlining).)

**4. Or jump straight to one section.** If you already have a draft, skip the interview:

```text
/audit-write-results rewrite my results section for JAR style: <paste your draft>
```

**5. Get an honest score.** Any section can be audited (read-only, no rewriting):

```text
/audit-write-abstract audit my abstract: <paste>
```

You'll get a **0–100 score** with a per-dimension breakdown and one headline fix.
Thresholds: **≥90 ship-ready · 75–89 revise-then-ship · <75 don't ship yet.**

**6. Stress-test before submitting.** When the paper is close:

```text
/audit-write-review peer review my paper for JAR: paper.pdf
```

It runs a **mock editorial pipeline** — a desk review, two referees with deliberately
different temperaments, and an editorial decision letter — and writes the reports to an
`audit_review_<paper>/` folder.

That's the full arc: **interview → outline → draft → audit → peer review.** You can enter
at any step.

---

## The features, in plain language

### The 9 sub-skills

One **hub** dispatcher (`audit-write`) routes you to the right specialist. You can also
call any sub-skill directly.

| Skill | What it writes / does | Plain-language note |
|---|---|---|
| `audit-write` | **Hub / dispatcher** + concept reference | Ask it anything; it routes you. Also answers "what's the DeFond style / audit-quality framework?" |
| `audit-write-interview` | Structured intake → `paper-spec.md` | Start here when beginning a paper or with messy notes |
| `audit-write-abstract` | The abstract (5-move, ~150 words) | Abstracts use **no** effect-size numbers — direction only |
| `audit-write-intro` ★ | The introduction (5 blocks) | The most important section ("75% of acceptance"); needs a magnitude in the findings block |
| `audit-write-hypothesis` | Hypothesis development (§2) | Includes the mandatory **tension paragraph** (the honest counter-argument) |
| `audit-write-design` | Research design / methods (§3) | Sample, variables, baseline model; identification machinery is deferred to §4 |
| `audit-write-results` | Results (§4) | Leads with the headline; translates coefficients into economic magnitudes |
| `audit-write-robustness` | Robustness / additional analyses (§5) | A numbered identification battery (the modern gold standard) |
| `audit-write-review` | **Whole-paper review** | Writing review (rubric) *or* mock peer review (editor + referees) — it asks which |
| `audit-referee-response` | Point-by-point reviewer rebuttals (R&R) | The 4-move response: acknowledge → reframe → action → location |

★ = most-used.

### The three working modes

Every *section* sub-skill runs in one of three modes — just name the mode in your prompt:

- **DRAFT** — build the section from your notes; unknowns become `[AUTHOR: …]` slots.
- **REWRITE** — recast an existing draft into the target register, with a
  paragraph-level change log so you can see exactly what changed.
- **AUDIT** — read-only diagnosis + a 0–100 score block. No rewriting.

```text
# DRAFT
/audit-write-intro draft an intro. RQ: …  Setting: …  Finding: …  Target: JAE.

# REWRITE
/audit-write-results rewrite my §4 for JAE style: <paste draft>

# AUDIT
/audit-write-results audit my §4: <paste>
```

### Whole-paper review (writing review + peer review)

`audit-write-review` answers two *different* questions, and asks which you want:

1. **Writing review** — *Is it written like an accepted audit paper?* A rubric-scored,
   section-by-section diagnosis of register, structure, and contribution clarity. Cheap;
   read-only. Best for a draft you're still polishing.
2. **Peer review** — *Will it survive review?* A simulated editorial pipeline:
   **editor desk review → two referees with deliberately different dispositions →
   editorial decision letter** (Accept / Minor / Major / Reject), calibrated to your
   target journal, with every concern tagged to an objection code (O1–O8) so you can hand
   it straight to `audit-referee-response`. Best as a pre-submission dress rehearsal.

Both modes save a Markdown report into one `audit_review_<paper>/` folder.

### The 0–100 quality rubric

Every AUDIT and the writing review score against **one shared instrument**, so an "82"
means the same thing every time. It runs in three layers:

1. **Integrity gate (pass/fail, first).** Any fabricated citation, invented result, or
   made-up number presented as real → score **capped at 55/100**, with the offending text
   named. Unknowns must be `[AUTHOR: …]` placeholders. *This is the suite's core promise:
   it will not manufacture evidence.*
2. **Binary pre-checklist (7 yes/no items).** Objective checks answered Y/N before any
   subjective scoring — this stops the score from drifting upward into flattery.
3. **5 weighted dimensions.** Structure (20) · register/voice (20) · magnitude &
   evidentiary discipline (25) · argument & contribution clarity (20) · audit vocabulary
   (15).

<details>
<summary><b>Show the 7 binary checks and band thresholds</b></summary>

| # | Binary check | Maps to |
|---|---|---|
| C1 | every hard `(Name, Year)` cite is a sanctioned anchor or an `[AUTHOR:]` slot | gate + magnitude |
| C2 | no invented numeric result/magnitude presented as real | gate + magnitude |
| C3 | zero blacklist verbs in claim sentences ("show that", "prove", …) | register |
| C4 | zero AI-slop tells (em-dash overuse, "not X but Y", reflexive triads) | register |
| C5 | the section's mandatory element is present (intro: a magnitude; abstract: **zero** effect numbers; hypothesis: a tension paragraph; design: identification machinery **out** of §3) | structure |
| C6 | every reported effect is magnitude-anchored where required (or honest `[AUTHOR:]`) | magnitude |
| C7 | each contribution names an identifiable literature | argument |

Bands per dimension: 90–100 / 75–89 / 60–74 / <60. **Ship thresholds: ≥90 ship-ready ·
75–89 revise-then-ship · <75 don't ship.** Full instrument:
[`rubric.md`](plugins/audit-write/skills/audit-write/rubric.md).
</details>

### The optional mechanism layer (Python checks)

For users who want a second, mechanical opinion, the plugin ships tiny **standard-library
Python scripts** (no dependencies, no API keys). They are advisory aids to the rubric.

```bash
# Style/integrity linter — point at a GENERATED DRAFT (not the skill docs)
python plugins/audit-write/scripts/lint_style.py mydraft.md

# Binary self-check — mirrors the rubric pre-checklist
python plugins/audit-write/scripts/check_structure.py mydraft.md --section intro

# Link health across the suite's docs
python plugins/audit-write/scripts/check_links.py

# Golden tests — prove the mechanism layer itself works
python plugins/audit-write/tests/run_tests.py
```

`check_links.py` also runs automatically as a hook on every file write. The linters are
deliberately conservative so they don't fire on legitimate audit prose (e.g. "not
significant but economically large").

---

## The recommended workflow: progressive outlining

The single most important habit: **never have the model produce a finished draft in one
shot.** Ratchet up through resolution levels, approving each:

| Stage | You get | It stops for you to… |
|---|---|---|
| **0 Interview** | `paper-spec.md` — RQ, variables, setting, the *for* (mechanism) and the *against* (tension), contributions | confirm the spec |
| **1 Skeleton** | `outline.md` — one line per block, no prose | edit/approve the structure |
| **2 Bullets** | bullet claims + `[AUTHOR:]` slots | approve the logic before any prose cost |
| **3 Prose** | the draft, one block at a time | accept / revise each block |
| **4 Self-audit** | a rubric score + fixes | decide: ship / revise / rework |

**Why:** editing a one-line skeleton reorganizes a whole section; editing the same words
in finished prose changes only those words. Outlining is high-leverage; polishing is not.
Run it all with `/audit-write draft my whole paper` and let the approval gates pace you.
State persists to `paper-spec.md` + `outline.md`, so it survives closing your laptop and
every section reuses the same spec (no re-interviewing). Rationale and provenance:
[`progressive_outline.md`](plugins/audit-write/skills/audit-write/progressive_outline.md).

---

## Why it is different from "ask ChatGPT to write my paper"

| A generic AI assistant | `audit-write` |
|---|---|
| "Write good academic prose" | Section-specific anatomies (5-block intro, 5-move abstract, 4/6-move hypothesis, 5-part design, 6-sub-section results, numbered robustness battery, 4-move rebuttal) |
| Invents plausible-sounding citations and numbers | **Integrity gate**: any fabricated citation/result/number caps the score at 55/100; unknowns must be `[AUTHOR: …]` placeholders |
| Generic, often over-confident tone | Calibrated, corpus-derived voice: a verb whitelist/blacklist, banned marketing adjectives, anti-AI-slop tells |
| States its rules as universal truths | Rules are **graded**: integrity rules are absolute; conventions are *corpus priors you may override with a stated reason* |
| Opaque — you can't tell where advice comes from | Every "6/6 papers do X" claim traces to a disclosed corpus ([`corpus_manifest.md`](plugins/audit-write/skills/audit-write/corpus_manifest.md)) |

---

## The corpus & scientific discipline

The suite's rules are **distilled from a fixed, named corpus** of published audit papers,
not invented. The manifest decodes every shorthand code (`07-DHT` … `26-KLYY`) to a real
citation and states the rules of engagement:

- **Frequency claims are corpus priors, not laws.** "6/6 papers do X" means *the named
  corpus is unanimous* — a strong default you may override with a stated reason.
- **Quotes are traceable.** Verbatim exemplars resolve to plain-text extractions of the
  source papers.
- **No evidence is manufactured.** Substantive citations are always `[AUTHOR: …]` slots;
  only a small set of sanctioned methodological anchors appear as hard cites.

This repo ships the **distilled patterns only** — not the source PDFs (third-party
copyright). Obtain them from their publishers via the manifest citations; the suite is
fully usable without them.

---

## Glossary

Terms you'll see in the suite's output:

- **DeFond / Zuo / Khurana register** — the writing voice of leading modern audit-research
  authors; calibrated, evidence-forward, never over-claiming.
- **`[AUTHOR: …]` slot** — a placeholder the suite inserts wherever a real citation or
  number is needed but not supplied. *You* fill these in; the suite never invents them.
- **Magnitude** — an economic effect size (e.g. "1.8 pp, ≈15% of the base rate"). Required
  in the introduction and results; **banned** in the abstract (direction only).
- **Tension paragraph** — the mandatory passage in the hypothesis section that honestly
  states the counter-argument to your prediction.
- **O1–O8** — the catalog of recurring referee objections (e.g. O1 "your identification is
  weak", O3 "your DV doesn't capture audit quality"). Used to pre-empt objections and to
  route reviewer comments to rebuttal templates.
- **Identification battery** — the numbered set of tests (shocks, rotation, falsification,
  fixed-effects saturation) that defends a causal claim.
- **Disposition** — a referee's prior/temperament in the peer-review pipeline
  (IDENTIFICATION, MEASUREMENT, CONTRIBUTION, INSTITUTIONAL, THEORY, GENERAL-SKEPTIC).
- **Hub-and-spoke** — the architecture: one dispatcher skill + specialist sub-skills that
  share a single set of reference files.

---

## FAQ & troubleshooting

<details>
<summary><b>I typed <code>/audit-write</code> and nothing happened.</b></summary>

The plugin isn't registered in this session. Confirm installation
([above](#installation)), then **restart Claude Code** (plugins load at startup). Verify
with `/audit-write what is the audit-quality framework?`.
</details>

<details>
<summary><b>Will it write my whole paper for me?</b></summary>

No — by design. It structures, tightens, and stress-tests your writing, but **you** supply
the research question, data, and results. It refuses to invent citations or numbers; those
become `[AUTHOR: …]` slots you fill in. It is a register-and-structure tool, not a
content generator, and **not a guarantee of acceptance**.
</details>

<details>
<summary><b>I updated the repo on GitHub but my installed plugin is the old version.</b></summary>

Plugins installed from this marketplace auto-update on the **next Claude Code restart**
(the running session keeps the version it loaded). You can also trigger an update from the
`/plugin` menu. Local edits to a cloned copy require re-syncing the marketplace.
</details>

<details>
<summary><b>It keeps inserting <code>[AUTHOR: …]</code> instead of a real citation.</b></summary>

That's intentional and non-negotiable — the integrity gate forbids fabricated references.
Replace each slot with the citation you choose. (This is exactly the behavior that
separates it from a generic chatbot.)
</details>

<details>
<summary><b>My paper isn't audit research / isn't for a top-5 accounting journal.</b></summary>

The suite is tuned for archival audit-quality papers at JAE/JAR/TAR/CAR/RAST and will say
so and defer outside that scope. For other fields, see
[Customizing / forking](#customizing--forking-for-your-field) — the architecture is
field-agnostic; you swap the corpus and pattern files.
</details>

<details>
<summary><b>Do I need Python? Do I need an API key?</b></summary>

No to both for normal use. The skills run entirely inside Claude Code. Python is only for
the *optional* mechanical self-check scripts, and they use the standard library only.
</details>

---

## Architecture & repository layout

```text
audit-write  (hub: dispatcher + 11 shared reference banks)
├── audit-write-interview      structured intake → paper-spec.md
├── audit-write-abstract       5-move / 6-sentence abstract
├── audit-write-intro       ★  5-block introduction ("75% of acceptance")
├── audit-write-hypothesis     4-/6-move arc + pair-prediction device
├── audit-write-design         5-part §3 (identification deferred to §4)
├── audit-write-results        6-sub-section §4 + magnitude translation
├── audit-write-robustness     numbered identification battery
├── audit-write-review         whole-paper review: writing (rubric) OR peer (editor + 2 referees)
└── audit-referee-response     4-move point-by-point rebuttal

agents:  audit-write-critic (writing scorer) · audit-referee-simulator (referee persona,
         disposition-aware) · audit-editor (desk review + referee selection + synthesis)
```

Sub-skills consult the hub's reference banks via the relative path `../audit-write/<bank>.md`,
so the layout must stay intact. Two banks (`move_bank`, `exemplar_gallery`) are **indexes
that point into** the section pattern files rather than copies — this keeps every verbatim
corpus exemplar in one place so the quote→source chain is never broken.

<details>
<summary><b>Show the full file tree</b></summary>

```text
audit-write-skills/                     ← repo = single-plugin marketplace
├── README.md                           ← this file
├── LICENSE                             ← MIT
├── .claude-plugin/
│   └── marketplace.json                ← lists the plugin
└── plugins/
    └── audit-write/                    ← THE plugin
        ├── .claude-plugin/plugin.json
        ├── CHANGELOG.md
        ├── agents/                     ← critic + referee-simulator + editor
        ├── hooks/                      ← hooks.json (auto link-check on write)
        ├── scripts/                    ← stdlib self-check scripts
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
</details>

---

## Customizing / forking for your field

The hub-and-spoke + reference-bank + rubric **architecture is field-agnostic**; only the
*content* is audit-specific. To adapt it (e.g. for a different accounting subfield or
another discipline):

1. **Set your target journal** in `paper-spec.md` — it drives the roadmap rule, abstract
   norms, and identification bar (see
   [`journal_profile_bank.md`](plugins/audit-write/skills/audit-write/journal_profile_bank.md)).
2. **Swap the corpus, keep the scaffolding.** Replace `corpus_manifest.md` and the
   `*_patterns.md` files with your field's; keep the rubric, ratchet, and bank structure.
3. **Re-derive frequency claims.** Any "k/6" is over the *named* corpus — don't leave a
   stale count if you change the corpus.
4. **Keep the single source.** Conventions, the rubric, and protocols live once in the hub
   banks; link to them, don't copy.
5. **Integrity first.** Never replace `[AUTHOR: …]` slots with invented citations to "make
   it look finished" — the integrity gate exists to catch exactly that.

---

## Roadmap

| Phase | Scope | Status |
|---|---|---|
| P1 | De-personalize · corpus manifest · portability | ✅ done |
| P2 | Asset-library refactor · rubric · hard-rule re-grade · lazy-load · absorb referee | ✅ done |
| P3 | Interview intake + progressive-outline ratchet + DRY context object | ✅ done |
| P4 | Claude Code **plugin** packaging (`plugin.json` + single-plugin marketplace) | ✅ done |
| P5 | Mechanism layer: hook-enforced integrity/link checks, critic + referee-simulator agents, golden tests | ✅ done |
| Opt. R1–R3 | Section-specific `check_structure.py` gates; slim/harmonize intro; deepen design/abstract over the pilot corpus; held-out blind eval per change | ✅ done |
| Opt. R4 | **Whole-paper review** sub-skill (writing + simulated peer review; new `audit-editor` agent; disposition-aware referee) | ✅ done |
| Opt. R5 | Retarget to the accounting top-5 (AJPT → CAR + RAST) | ✅ done |

**Honest status:** the integrity gate and lazy-load policy are *instructions the agent is
told to follow*, reinforced by the stdlib mechanism layer (hook-enforced link checks,
advisory linters, golden tests). Quality is verified structurally and by review; it is not
yet measured against a large sample of generated output. Full history:
[CHANGELOG.md](plugins/audit-write/CHANGELOG.md).

---

## Scope, limitations & licensing

- **Evidence base is small and correlated.** The corpus is DeFond-coauthored / China /
  partner-trait-heavy. The manifest discloses this; rules are framed as priors
  accordingly. **Best fit:** archival audit-quality papers for the accounting top-5
  (JAE/JAR/TAR/CAR/RAST). **Weaker fit:** experimental audit, pure-US settings,
  non-accounting — the suite will say so and defer.
- **Not a guarantee.** It encodes a register and structure, not a path to acceptance.
- **License:** **MIT** — see [LICENSE](LICENSE). The distilled patterns are the project's
  own work and reusable. Source papers are **not** redistributed; obtain them from their
  publishers via the manifest citations.

---

## Acknowledgments

- **Maintainer:** Gareth Jiang.
- Co-developed with **Claude** (Anthropic) in Claude Code — see the commit history /
  Contributors for the collaboration record. Final design decisions, the corpus selection,
  and review are the maintainer's.

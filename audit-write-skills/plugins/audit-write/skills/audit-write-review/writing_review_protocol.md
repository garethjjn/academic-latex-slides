# Writing Review Protocol (pattern file for `audit-write-review`, WRITING mode)

**What this is.** The suite's holistic **writing audit**, run section by section against
the one shared rubric. It answers *"is this written like an accepted audit paper?"* —
register, structure, magnitude discipline, framework anchoring, and contribution clarity.
Cheap, section-granular, read-only. The right tool for a draft you are still polishing for
voice and structure (use COMPREHENSIVE for an all-round substance+writing read, or PEER for
the survival question).

> **Do not invent a new rubric.** The only scoring instrument is `../audit-write/rubric.md`
> (integrity gate → 7 binary pre-checklist items → 5 weighted dimensions). This mode applies
> it; it does not redefine it. Journal-agnostic — register standards do not vary by journal.

---

## Procedure

1. Read `../audit-write/rubric.md` (the scoring instrument) and `../audit-write/style_dna.md`
   (verb whitelist/blacklist, AI-slop tells, register mechanics).
2. For each section present, plug that section's pattern file into **Dimension 1**'s anatomy:
   - intro → `../audit-write-intro/intro_patterns.md`
   - abstract → `../audit-write-abstract/abstract_patterns.md`
   - hypothesis → `../audit-write-hypothesis/hypothesis_patterns.md`
   - design → `../audit-write-design/design_patterns.md`
   - results → `../audit-write-results/results_patterns.md`
   - robustness → `../audit-write-robustness/robustness_patterns.md`
3. Score each section with the rubric: **integrity gate → binary pre-checklist (C1–C7) →
   5 weighted dimensions → composite**. You MAY spawn the `audit-write-critic` agent (via
   `Task`) per section for an independent, uncontaminated score — recommended for a long
   paper so one section's issues don't bleed into another's score. Or apply the rubric inline
   for a short paper.
4. **Read-only.** Name flaws and the rule each violates; never rewrite. (Route rewrites to
   the section sub-skill.)
5. Write the combined report to `writing_review.md` in the per-paper folder (template below).
   For a short pasted snippet where a file is overkill, render it inline instead — ask if unsure.

---

## Report template (`writing_review.md`)

Lead with a plain-language verdict line, then the per-section detail and cross-cutting
issues — so the author sees the headline before the rubric machinery.

```markdown
# Writing Review: [Paper Title]
**Date:** YYYY-MM-DD   **Reviewer:** audit-write-review (writing mode)   **File:** [path]

## Verdict
[One plain-language sentence: e.g. "Reads close to JAE register; the binding issue is
unanchored magnitudes in §4 and a missing tension paragraph in §2."]  **Overall: [X]/100.**

## Section scores
| Section | Composite | Integrity gate | Headline fix |
|---|:---:|:---:|---|
| Abstract | …/100 | PASS/FAIL | … |
| Introduction | … | … | … |
| Hypothesis | … | … | … |
| Design | … | … | … |
| Results | … | … | … |
| Robustness | … | … | … |

## Per-section detail
[For each section, the rubric's canonical Score block:
 - the C1–C7 pre-checklist line
 - per-dimension bands (Structure / Register / Evidentiary / Argument / Vocabulary)
 - composite
 - integrity-gate line
 - headline fix]

## Top 5 cross-cutting issues
[Issues a section-by-section pass alone would miss — notation drift §3↔§5; a contribution
claimed in the intro but unsupported in the results; magnitude conventions inconsistent
between intro and §4.]

## Overall
**[X]/100** (weighted: intro 25 · hypothesis 15 · design 20 · results 25 · robustness 15)
Ship guidance: **≥90 ship-ready · 75–89 revise-then-ship · <75 do not ship.**
```

Each section's Score block is the rubric's canonical block verbatim
(`../audit-write/rubric.md` "Output format"). Do not improvise alternative dimensions or weights.

---

## Hard rules (this mode)

1. **Read-only** — diagnose; never rewrite.
2. **One instrument** — `rubric.md` only; the integrity gate applies verbatim.
3. **Never invent** a citation or magnitude in your own report; flag the manuscript's if it does.
4. **Journal-agnostic** — register and structure standards do not change by target journal.

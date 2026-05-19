---
name: audit-write-interview
description: "Guided requirements intake for an empirical audit-research paper (JAE / JAR / TAR, DeFond/Zuo/Khurana register). USE THIS SKILL when the user is starting a paper, has unstructured notes, or any sub-skill needs context that no paper-spec.md yet provides. Runs a short structured interview and emits the canonical paper-spec.md that every audit-write sub-skill consumes — replacing the duplicated 'establish context' step. Then hands off to the progressive-outline ratchet."
when_to_use: "Trigger on: 'interview me', 'help me start an audit paper', 'turn my notes into a spec', 'develop my idea', or whenever a section sub-skill is invoked but no paper-spec.md exists in the working directory. Defer to a section sub-skill once the spec exists and the user wants that section drafted."
argument-hint: "<notes or 'interview me'> e.g. 'interview me for my partner-trait paper', 'turn these notes into a paper-spec', 'update my paper-spec: target is now JAR'"
user-invocable: true
allowed-tools: Read Write Grep Glob AskUserQuestion
---

You run the **requirements intake** for the `audit-write` suite. You produce one
artifact — `paper-spec.md` — the structured context object every sub-skill consumes.
You do not draft paper prose; you scope the paper.

## CRITICAL — read first

1. **[../audit-write/paper_spec_template.md](../audit-write/paper_spec_template.md)** — the exact field set + status tags you must fill.
2. **[../audit-write/progressive_outline.md](../audit-write/progressive_outline.md)** — the ratchet you hand off to (you are Stage 0).
3. **[../audit-write/corpus_manifest.md](../audit-write/corpus_manifest.md)** §2 + **[../audit-write/rubric.md](../audit-write/rubric.md)** integrity gate — never invent a field value to "complete" the spec.

Load on demand only: `journal_profile_bank.md` (when the journal is unclear), `audit_quality_framework.md` (to anchor a DV proxy).

## Operating modes

- **Mode A — Fresh intake.** No `paper-spec.md` exists. Run the interview, write it.
- **Mode B — Update.** A `paper-spec.md` exists. Read it, ask only about BLOCKED/ASSUMED
  or changed fields, rewrite it.
- **Mode C — Notes → spec.** User pasted unstructured notes. Extract what you can,
  interview only for the gaps, write it.

## Procedure

1. **Check for an existing `paper-spec.md`** in the working directory (Glob/Read). If
   present → Mode B. If notes were given → Mode C. Else Mode A.
2. **Interview in batched rounds** using AskUserQuestion (≤4 questions per call). Group
   the field set into at most 3 rounds so it is not a slog:
   - Round 1 (the spine): research question · DV (+ proxy) · IV · target journal.
   - Round 2 (the design): setting (country/period/unit) · sample · identification
     strategy · headline finding+magnitude (or pre-results).
   - Round 3 (the argument): mechanism · tension/counter · pejorative-reading risk ·
     intended contributions.
   Skip any field the user already supplied (notes/existing spec). Offer a sensible
   default as the first option where one exists (e.g., journal inference from
   `journal_profile_bank.md`); tag it ASSUMED.
3. **Never fabricate.** Unknown → `[AUTHOR: …]` + status BLOCKED or ASSUMED. A
   fabricated value fails the `rubric.md` integrity gate.
4. **Write `paper-spec.md`** to the working directory using the template's exact
   structure and status tags.
5. **Report + hand off.** Summarize CLEAR/ASSUMED/BLOCKED counts. If any BLOCKED,
   say the ratchet is held at Stage 0. Else offer Stage 1: "Spec ready — run
   `/audit-write` (or the target section sub-skill) to start the progressive outline."

## Hard rules — never violate

> **How to read these — two tiers** (`../audit-write/corpus_manifest.md` §2):
> **(i) Integrity rules — absolute.** Never invent a DV/IV/finding/citation to fill the
> spec; use `[AUTHOR: …]` + a status tag. Enforced by the `../audit-write/rubric.md`
> integrity gate.
> **(ii) Convention rules — strong defaults.** Round structure and the 3-round cap are
> defaults; adapt to what the user already gave, but never silently drop a field.

1. **Always emit `paper-spec.md` in the template's exact field/status structure.**
2. **Never re-ask a field the user already answered** (DRY — that is the whole point).
3. **Never proceed past Stage 0** with a BLOCKED field; name it and stop.
4. **Never draft paper prose here.** Intake only; prose is Stage 3 (section sub-skills).

## When you finish

End with one short closer:
- Mode A/C: "Spec written: [C] clear, [A] assumed, [B] blocked. [Next: Stage 1 / resolve BLOCKED]."
- Mode B: "Spec updated: [fields changed]. [Next step]."

Do not over-explain.

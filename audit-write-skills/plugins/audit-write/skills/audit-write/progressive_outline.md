# Progressive Outline — the staged drafting ratchet

**What this is.** The end-to-end workflow for writing a paper (or a section) by
*ratcheting through resolution levels with approval gates*, instead of jumping from
notes to 2,500 words of prose. The expensive failure in academic drafting is committing
prose to a wrong structure or argument; this catches that at Stage 1–2 when it is cheap
to fix.

The hub (`audit-write`) orchestrates this; section sub-skills do the Stage-3 prose.
State persists to two files in the user's working directory so the workflow survives
context compaction: **`paper-spec.md`** (the context object — see
`paper_spec_template.md`) and **`outline.md`** (the evolving skeleton/bullets).

---

## The 5 stages (each ends with an explicit approval gate)

```
Stage 0 — INTERVIEW            → paper-spec.md
   Invoke /audit-write-interview. Produces the structured spec.
   GATE: user confirms the spec. Any BLOCKED field stops here.

Stage 1 — SKELETON             → outline.md (one line per block/move)
   For the target section(s), emit the canonical anatomy as a skeleton:
   one line per block/move, placeholders only, no prose.
   GATE: user edits/approves the structure before any argument is written.

Stage 2 — BULLETS              → outline.md (bullet claims + [AUTHOR:] slots)
   Expand each block to bullet-level claims with [AUTHOR: cite] slots.
   The argument now exists in skeleton form — still no prose.
   GATE: user approves the argument/logic before prose cost is incurred.

Stage 3 — PROSE                → draft (block-by-block, not whole-paper)
   Expand one block at a time in the DeFond register, routing to the
   relevant section sub-skill. Stop after each block for a quick check.
   GATE: per-block accept / revise.

Stage 4 — SELF-AUDIT           → rubric score + fixes
   Run the section sub-skill's Mode-C audit; score with rubric.md
   (integrity gate first); apply fixes; re-score.
   GATE: report score; ≥90 ship-ready, 75–89 revise, <75 do not ship.
```

## Why the ratchet is high-leverage

(Corroborated by an independent practitioner account —
`../../docs/external-validation-ng.md`.)

1. **Outline edits cascade; prose edits do not.** Changing a few words of a
   *skeleton* line reorganises an entire block of the eventual draft. Changing the
   same words in finished *prose* changes only those words and leaves a wrong
   structure intact. Iterate where the leverage is — Stages 1–2 — not Stage 3.
   This is the whole reason the gates come *before* prose, not after.
2. **Surface the AGAINST before Stage 1.** Before the skeleton, state the evidence
   *for and against* the prediction. In audit writing this is not optional: the
   hypothesis section's tension paragraph is mandatory (`style_dna.md`) and likely
   reviewer objections are catalogued (`referee_objection_bank.md`, O1–O8). Pull
   the counter-argument in at Stage 1 so the structure already answers it, rather
   than retrofitting a tension paragraph into finished prose.
3. **Outline-first speeds review.** A skeleton/bullet diff is read in seconds; a
   re-prosed section is not. Cheap review at every gate is the point.

## Operating rules

1. **Never skip a gate without the user saying so.** "just draft it" → you may
   collapse Stages 1–2 but must still show the skeleton before prose.
2. **One block at a time in Stage 3.** Do not emit a full section then ask; emit a
   block, checkpoint, continue. Keeps revisions cheap.
3. **The spec is law for content, not the rules.** Pull every DV/IV/setting/finding
   from `paper-spec.md`; pull *structure* from the section's pattern file; pull
   *scoring* from `rubric.md`. Do not re-ask what the spec already answers (DRY).
4. **Integrity gate runs at Stages 2 and 4.** A bullet or prose block that introduces a
   fabricated citation/result fails immediately (`rubric.md`).
5. **Pre-results papers are fine.** Magnitudes stay `[AUTHOR: …]`; the ratchet still
   runs; Stage 4 notes "DRAFT-PRE-RESULTS".

## Invocation cues (hub routes these here)

- "interview me / help me start a paper / develop my idea" → Stage 0
- "outline first / skeleton / progressive outline / don't write prose yet" → Stages 1–2
- "draft the whole paper" → full ratchet 0→4
- "just the [section]" → spec (or quick intake) → Stages 1–4 for that section only

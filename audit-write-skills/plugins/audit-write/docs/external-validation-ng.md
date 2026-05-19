# External validation — Andrew Ng on AI-assisted writing

**What this is.** A design-rationale note. Two short instructional videos on
AI-assisted writing independently describe the two techniques this suite is built
on. This document records (1) a faithful summary of the source material, (2) the
provenance caveats, and (3) the gap analysis that produced the P5-era refinements.
It is the "why" behind [style_dna.md](../skills/audit-write/style_dna.md) §9,
[rubric.md](../skills/audit-write/rubric.md)'s binary pre-checklist, and
[progressive_outline.md](../skills/audit-write/progressive_outline.md)'s
high-leverage rationale.

---

## 1. Provenance & caveats (read first)

Same discipline as [corpus_manifest.md](../skills/audit-write/corpus_manifest.md)
§2: state the evidentiary boundary before using the material.

- **Source.** Two ASR (speech-to-text) transcripts of an Andrew Ng course on
  AI-assisted writing, sitting in the user's working tree as "6. AI辅助写作.mp4.md"
  (Video 6, *AI-assisted writing*) and "7. AI评析点评.mp4.md" (Video 7, *AI
  critique*). They are **not** an academic source and are **not** redistributed
  with the plugin.
- **Reliability.** Auto-generated. Visible ASR errors were corrected for this
  summary (e.g. *chatGPD*→ChatGPT, *Artificial Gender Intelligence*→AGI,
  *secrecy*→AI slop, *hopeful*→helpful, *per calorie*→per criterion, *config
  between*→conflict between). Each file also carries an embedded vendor ad line,
  and Video 7's tail degenerates into a repeated "you can do" loop; its content is
  reconstructed only up to the rubric-summing instruction. **Treat as practitioner
  instruction corroborating an existing design — not as a citable authority.**
- **Status of the claim.** This is *external corroboration*, not new evidence. It
  raises confidence in the suite's two pillars and motivates bounded refinements;
  it does not change the corpus or any section anatomy.

---

## 2. Faithful summary

### Video 6 — AI-assisted writing

- Writing is the single largest category of ChatGPT use (~24%, attributed to an
  OpenAI study). Writing *is* thinking; AI reasoning can assist, but naive "write
  this for me" produces **AI slop**.
- **AI slop** = text that reads acceptably sentence-by-sentence but collectively
  lacks substance — written without careful thought. Reported tells:
  - **Em-dash (—) overuse** relative to human writing.
  - **Overused tokens**: *delve*, *nuanced*; fewer unique words overall.
  - **Rule-of-three / triadic lists** used more than humans do.
  - **Noun-poverty**: leans on vague adjective+noun ("robust instruction",
    "highly insightful paper") instead of concrete nouns.
  - The **"not X but Y" / "not just about X, it's about Y"** construction where X
    and Y are both vague abstractions ("not about infrastructure, it's about
    architecture").
  - **Big, empty-but-self-important sentences** ("but it does change everything").
  - Feedback loop: heavy AI use is making *humans* imitate AI (*delve* rising in
    spontaneous and prepared human speech) — a reason for sustained vigilance.
- **Progressive outlining** (the recommended workflow): ask AI to research
  evidence *for and against* the thesis → brainstorm 2–3 outline options
  (including a counter-argument section) → give feedback → expand to bullets →
  feedback → *only then* generate prose.
- **Why outline-first is high-leverage**: editing a few words of an *outline*
  cascades into reorganising a whole section; editing the same words of finished
  *prose* changes only those words. Iterating at the cheap (outline) resolution is
  where the leverage is, and it speeds review. ~⅔ of writing-focused chats start
  from existing text, not a blank page — which motivates Video 7.

### Video 7 — AI critique

- **Edit piece by piece**: one sentence/paragraph at a time; brainstorm a few
  phrasings (e.g. punchy / visionary / conversational), settle one, move on. A
  whole-article rewrite is hard to review (you cannot see what changed or why).
- Holistic critique is undermined by **sycophancy**: asked to critique without
  constraints, AI tends to praise.
- The fix is a **rubric** (explicit grading criteria + point system). The sharpest
  stated principle: **criteria must be binary and unambiguous — true/false,
  yes/no, nothing in between** ("does every named character have a goal? Y/N").
  Objectivity comes from the *binary checklist*, not from qualitative bands. You
  can co-develop the rubric with AI; after scoring, ask for rubric-targeted
  improvement suggestions.

---

## 3. Gap analysis → refinements adopted (P5 era)

| Ng technique | Suite already had | Refinement adopted | Where |
|---|---|---|---|
| Anti-slop tells | `style_dna.md` §9 (partial: *delve*, "robust audit framework", "vital role") | Added em-dash overuse, rule-of-three, "not X but Y", a stated **noun-poverty / vague-adjective principle**, the empty-grand-claim tell | [style_dna.md](../skills/audit-write/style_dna.md) §9 |
| Rubric defeats sycophancy | 5 weighted bands + adversarial critic agent | Added a **binary yes/no pre-checklist** run before banding; any **N** forces the mapped dimension down one band (Ng's "nothing in between") | [rubric.md](../skills/audit-write/rubric.md) |
| Progressive outlining | Stage 0–4 ratchet with approval gates | Added the explicit **high-leverage rationale** + the "research evidence for *and against* before Stage 1" framing, tied to the suite's mandatory tension paragraph + objection bank | [progressive_outline.md](../skills/audit-write/progressive_outline.md) |
| Mechanical enforcement | P5 `lint_style.py`, golden tests | Two stdlib WARN detectors (em-dash density; "not X … it's Y"); a new advisory `check_structure.py` mirroring the binary pre-checklist | `../scripts/lint_style.py`, `../scripts/check_structure.py` |

**Deliberately *not* adopted (out of scope this pass):**

- A generic sentence-workshop REWRITE sub-mode and automatic outline-variant
  generation — useful but a larger change than warranted here.
- **Rule-of-three as a hard linter rule** — kept instruction-only (`style_dna.md`
  §9). A stdlib regex for triadic lists is too false-positive-prone; audit prose
  legitimately uses "A, B, and C" enumerations.
- The empty-grand-claim tell — kept instruction-only for the same reason (no
  reliable mechanical signature).

The two mechanised detectors are intentionally conservative: the em-dash check
needs ≥3 em-dashes *and* above-threshold density before it WARNs, and the
"not X … it's Y" check requires the mirrored *it's … it's* / *not about … it's*
form so it does not fire on legitimate "not significant but economically large".

---

## 4. Why this belongs in the suite (not just a note)

The convergence is the point: an independent practitioner account arrives at
*progressive outlining* and *rubric-against-sycophancy* — exactly the suite's
two pillars. That is evidence the architecture is sound and worth hardening, not
redesigning. The refinements are bounded, single-sourced, and pushed down into
the P5 mechanism layer so they are enforced, not merely asserted — consistent
with the suite's integrity-first, corpus-grounded ethos
([corpus_manifest.md](../skills/audit-write/corpus_manifest.md) §2).

See [../CHANGELOG.md](../CHANGELOG.md) (P5) for the change record.

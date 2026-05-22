# Comprehensive Review Protocol (pattern file for `audit-write-review`, COMPREHENSIVE mode)

**What this is.** The default review mode: **one human-friendly report** that diagnoses an
audit-research paper across the ~7 dimensions a top-journal referee actually weighs —
substance *and* writing — and ends with a prioritized fix list. It is the audit-research
adaptation of a generic comprehensive manuscript review, re-grounded in this suite's
audit-quality framework and O1–O8 objection bank.

> **Journal-agnostic by design.** Unlike PEER mode, COMPREHENSIVE does **not** calibrate
> its standards to a target journal. It asks "is this good audit research, written well?",
> not "will it survive at JAR specifically?". If the user wants the journal-specific
> survival question, route them to PEER mode.

> **Prior-not-law caveat** (`../audit-write/corpus_manifest.md` §2). The dimensions and
> their emphasis describe the conventions distilled from the named corpus. The **integrity
> gate is absolute**; everything else is a strong default a user may override with reason.

---

## How this differs from the other modes

| | COMPREHENSIVE | WRITING | PEER |
|---|---|---|---|
| Instrument | 7 review dimensions (substance + writing) | 5-dim writing **rubric** (register/structure) | 2 referee personas + editor |
| Output | one readable report + 1–5 ratings | per-section rubric Score blocks | desk review + 2 referee reports + decision |
| Best for | a near-final draft you want one honest read on | a draft you're still polishing for voice | a pre-submission survival rehearsal |

COMPREHENSIVE is the right default: it reads the whole paper once and tells the author what
a smart referee would flag, in plain language, without the cost of the full peer pipeline.

---

## The 7 review dimensions

Read the paper end-to-end first. Then evaluate each dimension, citing **specific sections,
equations, and tables**. Where a concern matches the objection bank, tag its **O-code**
(`../audit-write/referee_objection_bank.md`) so it routes cleanly to `audit-referee-response`.

### D1 — Research question & contribution clarity  *(O6)*
- Is the research question stated sharply and early?
- Can you state the contribution in one paragraph? Does the paper name the **closest prior
  paper** and the delta, or does it settle for "adds to the literature"?
- Do the stated contributions actually follow from the results?

### D2 — Hypothesis development & theory
- Is there a clean theory → prediction chain?
- Is there an **honest tension paragraph** (the credible counter-argument), not a strawman?
- Does the specification map to the stated mechanism?

### D3 — Identification & causal credibility  *(O1, O5)*
- Is the causal claim credible, or is "plausibly exogenous" merely asserted?
- Are the identifying assumptions stated explicitly? Threats addressed (omitted variables,
  reverse causality, selection)?
- Is there a quasi-experiment / shock / rotation / falsification, or only OLS-on-a-cross-section?

### D4 — Measurement & construct validity  *(O3, O8)*
- Does the DV actually capture **audit quality** as defined by the DeFond–Zhang framework
  (`../audit-write/audit_quality_framework.md`), or is a proxy used naively as "good/bad audits"?
- If DAC / abnormal accruals: is the Aobdia (2019) caveat acknowledged and a second proxy used?
- For a novel measure: is there a construct-validity / convergent check?

### D5 — Econometric specification & inference  *(O4)*
- Standard errors clustered at the **treatment level** (firm / client / partner / city×year)?
- Fixed-effects structure appropriate to the unit of the claim (e.g. partner claims → partner/firm FE)?
- Functional form, sample selection, multiple-testing concerns addressed?

### D6 — Magnitude & economic significance
- Are headline effects translated from coefficients into **economic magnitude** (pp + % of
  base rate + a literature benchmark), not left as bare coefficients?
- Are the magnitudes economically meaningful, or trivial-and-unframed? Is a null handled
  honestly (CI bounds + power), per `../audit-write/null_and_identification_protocols.md`?

### D7 — Writing, structure & presentation  *(O2 for setting)*
- Section anatomy sound (5-block intro, 5-move abstract, tension in §2, identification in §4 not §3)?
- DeFond register: no over-claiming verbs ("show that/prove/demonstrate"), no marketing
  adjectives on own work, no AI tells (`../audit-write/style_dna.md`)?
- **Notation consistent** across sections; tables/figures self-contained (labels, notes,
  units); single-country generalizability argued, not asserted (O2); right length for the claim?

> For a sharper read on D7 specifically, you MAY spawn the `audit-write-critic` agent (via
> `Task`) on the intro or abstract for an independent rubric score, then fold its headline
> into D7. The 7 dimensions remain the primary instrument here — do not replace them with
> the writing rubric.

---

## Procedure

1. **Pre-flight** already done by the orchestrator (manuscript located, sections inventoried).
2. **Read the whole paper.** Long PDFs in ≤5-page chunks.
3. **Score each dimension 1–5** using the band anchors below. Note evidence as you go.
4. **Write 3–5 Referee Objections** — the toughest questions a top referee would ask, each
   with why it matters and how to address it. Anchor to O-codes where they fit.
5. **Apply the integrity gate** (`../audit-write/rubric.md`): if the paper presents a
   fabricated cite / invented result / made-up magnitude as real, say so prominently — but
   note this audits the *manuscript's* honesty, and your own report must never invent
   citations either (`[AUTHOR: reviewer would cite …]`).
6. **Write the report** (template below) to `comprehensive_review.md` in the per-paper folder.

### Per-dimension 1–5 band anchors

| Rating | Meaning |
|:---:|---|
| **5** | Exemplary — a strength to preserve; nothing a referee would flag here. |
| **4** | Solid — minor polish only. |
| **3** | Adequate but exposed — a referee would raise this; addressable. |
| **2** | Weak — a likely major-revision trigger as written. |
| **1** | Failing / absent — would draw a reject-leaning comment. |

Overall rating is a holistic judgment (not a mechanical mean) — a single **1** on D3
identification can cap the overall regardless of strong writing.

---

## Report template (`comprehensive_review.md`)

Human-readable first: lead with a plain-language verdict and the strengths, *then* the
structured concerns. No code-jargon in the summary.

```markdown
# Comprehensive Review: [Paper Title]

**Date:** YYYY-MM-DD   **Reviewer:** audit-write-review (comprehensive mode)
**File:** [path]   **Sections present:** [abstract · intro · …]

## Summary assessment

**Overall recommendation:** [Strong Accept / Accept / Revise & Resubmit / Reject]

[2–3 short plain-language paragraphs: the paper's main contribution in one or two
sentences; its principal strength; the single binding constraint a referee would fixate
on. Written so a co-author who hasn't read your rubric can follow it.]

## Strengths
1. [Concrete strength, with where it shows.]
2. …
3. …

## Major concerns

### MC1 — [short title]
- **Dimension:** [D1–D7]   **O-code:** [O# if applicable]
- **Issue:** [specific, with §/table/equation reference]
- **Suggestion:** [the concrete fix or test that resolves it]
- **Location:** [section / page / table]

[Repeat MC2, MC3, … — ordered most to least binding.]

## Minor concerns
- **mc1** — [issue] → [fix]   (§/table)
- …

## Referee objections (the tough questions)

### RO1 — [the question, in a referee's voice]
**Why it matters:** [why this could sink the paper]
**How to address it:** [specific response / added analysis]   [O# if applicable]

[Repeat for 3–5 objections.]

## Specific comments
[Optional section-by-section line notes: notation slips, table-note gaps, wording.]

## Dimension ratings

| # | Dimension | Rating (1–5) |
|---|---|:---:|
| D1 | Research question & contribution | [N] |
| D2 | Hypothesis development & theory | [N] |
| D3 | Identification & causal credibility | [N] |
| D4 | Measurement & construct validity | [N] |
| D5 | Specification & inference | [N] |
| D6 | Magnitude & economic significance | [N] |
| D7 | Writing, structure & presentation | [N] |
| | **Overall** | **[N]** |

**Integrity gate:** [PASS / FAIL — if FAIL, name the offending span(s)]
**Top fix:** [the single highest-leverage change, one sentence]
```

---

## Principles

- **Be constructive.** Every criticism carries a concrete suggestion or a "what would fix this".
- **Be specific.** Reference exact sections, equations, tables — never "the methods feel weak".
- **Distinguish fatal from minor.** Not everything is equally important; order MCs by bindingness.
- **Acknowledge what's done well.** Strengths are not filler — they tell the author what to protect.
- **Never fabricate.** No invented citations, results, or magnitudes — `[AUTHOR: …]` placeholders only.
- **Read-only.** Diagnose; never rewrite the manuscript (route rewrites to section sub-skills).
- **Plain language up top.** The summary and objections should read like a thoughtful
  colleague, not a scoring machine — that is the whole point of this mode.

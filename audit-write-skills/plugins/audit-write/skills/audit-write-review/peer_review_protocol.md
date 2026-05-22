# Peer-Review Protocol (pattern file for `audit-write-review`)

**What this is.** The audit-specific distillation of a simulated editorial pipeline —
**editor desk review → two referees with deliberately different dispositions → editorial
decision** — calibrated to JAE / JAR / TAR / AJPT. It is the "peer review" half of
`audit-write-review`; the "writing review" half reuses `../audit-write/rubric.md` and the
`audit-write-critic` agent unchanged.

> **Provenance.** The pipeline shape (editor + dispositioned referees, FATAL/ADDRESSABLE/
> TASTE classification, "what would change my mind", pet-peeve injection) is adapted from
> the generic `review-paper --peer` workflow, itself adapted from Hugo Sant'Anna's
> clo-author. This file re-grounds those mechanics in the audit-research desk: the
> disposition taxonomy maps onto the suite's own O1–O8 objection bank, and calibration
> uses `../audit-write/journal_profile_bank.md` instead of a generic econ-journal table.

> **Prior-not-law caveat** (`../audit-write/corpus_manifest.md` §2). The journal cultures,
> referee-pool weights, and peeve pools below describe the named corpus and the reviewer
> culture distilled from it. Treat them as strong defaults a user may override with a
> stated reason, not as journal policy.

---

## The audit referee-disposition taxonomy (6-way)

Each disposition is a referee *prior* — the lens through which that referee reads the
paper first. Each maps onto the objection codes in
`../audit-write/referee_objection_bank.md`, so a concern a referee raises routes cleanly
back to `audit-referee-response` for the rebuttal.

| Disposition | Reads the paper looking for… | Primary O-codes | Kills the paper on… |
|---|---|---|---|
| **IDENTIFICATION** | Whether the causal claim survives. Probes shocks, partner rotation, FE saturation, falsification, reverse causality. | O1, O5 | "Plausibly exogenous" asserted, not argued; no quasi-experiment or falsification. |
| **MEASUREMENT** | Whether the DV/IV actually captures audit quality. DAC ↔ Aobdia 2019; novel-measure construct validity. | O3, O8 | Proxy used naively as "audit quality"; novel measure with no validation. |
| **CONTRIBUTION** | What is *new* vs the single closest prior paper. The JAR hawk. | O6 | Contribution stated as "adds to the literature"; cannot differentiate from a recent paper. |
| **INSTITUTIONAL** | Setting richness and generalizability; sample representativeness (esp. single-country). The TAR/AJPT lens. | O2 | Institutional setting under-described; sample narrowness unaddressed. |
| **THEORY** | Theory→specification mapping; whether the tension paragraph is honest; framework anchoring. | (framework) | Hypothesis has no tension; spec does not map to the stated mechanism. |
| **GENERAL-SKEPTIC** | Reasons to reject. Magnitudes too small, too-clean results, robustness theater, estimator choices. | O4, O5 | Effect economically trivial and unframed; robustness is coverage, not threat-targeted. |

**Why exactly two referees, deliberately different.** A single reviewer is a point
estimate of how the paper fares; cognitive diversity is the entire value of peer review.
The editor draws two *different* dispositions so the author sees the paper from two priors
at once — not the same complaint twice.

---

## Per-journal referee-pool weights (calibration)

The editor draws dispositions according to the target journal's culture
(`../audit-write/journal_profile_bank.md` "Reviewer culture" rows). Weights are relative
sampling priors, not probabilities to compute precisely — pick the two highest-weight
dispositions that differ, unless the paper's own weaknesses argue otherwise.

| Disposition | **JAE** | **JAR** | **TAR** | **AJPT** |
|---|:---:|:---:|:---:|:---:|
| IDENTIFICATION | ●●● | ●●● | ●● | ● |
| MEASUREMENT | ●●● | ●●● | ●● | ●●● |
| CONTRIBUTION | ●● | ●●●● | ●● | ● |
| INSTITUTIONAL | ●● | ● | ●●●● | ●●● |
| THEORY | ●● | ● | ●●● | ● |
| GENERAL-SKEPTIC | ●●● | ●● | ●● | ● |

**Selection rule.** Draw disposition D1 = highest-weight for the journal; draw D2 =
next-highest that **differs** from D1. **Override:** if the paper has an obvious
soft spot the default draw would miss (e.g. a DAC-based DV at JAE where the default
draw is IDENTIFICATION + GENERAL-SKEPTIC), swap one referee to the disposition that owns
that weakness (MEASUREMENT). State the override and its reason in the desk review.

---

## Peeve pools (audit-flavored)

Each referee is assigned **one critical peeve + one constructive peeve**, injected into
their prompt so the two referees feel like distinct people. Keep the pools flat; sample
uniformly. Peeves are *texture*, not the core objection — the disposition + O-codes drive
the substance.

### Critical peeves (sample 1 per referee)

- Standard errors must be clustered at the level of treatment (firm / client / partner / city×year) — not just "robust".
- Partner-level claims need partner or firm fixed effects, not only industry×year.
- DAC / abnormal-accruals DV used without the Aobdia (2019) caveat or a second proxy.
- Magnitude reported as a coefficient only — wants pp + % of base rate + a literature benchmark.
- Rotation / shock identification without a falsification or placebo test.
- PSM / entropy balancing reported without a covariate-balance table (std. diffs < 10%).
- Novel partner-trait measure with no convergent / face-validity check.
- Sample construction not traced end-to-end (raw → analysis sample), attrition footnoted not analyzed.
- Too-clean results (round-number point estimates; p exactly at 0.01) without explanation.
- Robustness theater — many specs, none targeting a *named* threat.
- Notation / proxy drift — a variable defined one way in §3, used differently in §5.
- A contribution claim ("first to…") with no named literature it advances over.
- Tension paragraph absent — the hypothesis has no honest counter-argument.
- Single-country generalizability asserted, not argued (no comparable-setting cites).

### Constructive peeves (sample 1 per referee)

- Rewards an honest "what this paper does not show" paragraph that bounds the claims.
- Values a clean quasi-experiment over heavier econometric machinery.
- Credits triangulation across audit-quality proxies over a single DV.
- Appreciates magnitude framing to a base rate and a prior-literature benchmark.
- Rewards a tension paragraph that genuinely entertains the opposite prediction.
- Values setting-as-feature framing for non-US data (done honestly, not as spin).
- Credits a construct-validity appendix for a novel measure.
- Appreciates a paper that pre-empts the obvious referee objection (O1–O8) in-text.
- Rewards disciplined scope — narrow and identified over broad and correlational.
- Values a clear contribution statement that names the closest prior paper and the delta.

---

## The pipeline

```
Phase 0  Pre-flight        locate manuscript · infer/confirm journal · section inventory
Phase 1  Editor desk review  audit-editor → DESK REJECT (stop) or SEND OUT
Phase 1b Referee selection   audit-editor draws 2 differing dispositions + peeves
Phase 2  Two referees         audit-referee-simulator ×2 (different dispositions), blind
Phase 3  Editorial synthesis  audit-editor classifies FATAL/ADDRESSABLE/TASTE → decision
Phase 4  Summary + handoff    report paths · decision · route to audit-referee-response
```

The orchestrating skill spawns each agent via `Task` so the two referees run in
**independent contexts** (genuinely blind to each other) — inline role-play would collapse
the cognitive diversity that is the whole point.

### Phase 0 — Pre-flight (required)

Output a short Pre-Flight Report before spawning any agent, so the user can confirm inputs:

```markdown
## Pre-Flight — audit-write-review (peer)

**Manuscript:** [path] — [pages / sections detected]
**Target journal:** [SHORT] → [full name]  (source: stated / inferred via cue table)
**Sections present:** abstract · intro · hypothesis · design · results · robustness  [✓/✗ each]
**Round:** fresh   (R&R continuation → hand off to audit-referee-response, not this skill)
```

If the manuscript path doesn't resolve or the journal can't be inferred, stop and ask.

### Phase 1 — Editor desk review (`audit-editor`)

The editor reads title + abstract + intro + design overview + the first results table —
**not** the whole paper — looking for desk-reject signals. Audit-specific desk-reject
criteria:

- **Wrong fit / below the bar** — out of scope, or a field-journal paper at JAE/JAR/TAR.
- **No statable contribution** — can't write the one-paragraph contribution from intro+abstract.
- **Fatal design flaw visible in the abstract** — DV that obviously can't bear an
  audit-quality interpretation; identification that is obviously OLS-on-a-cross-section;
  unit of analysis mismatched to the claim (partner claim, firm-level data).
- **Integrity flag** — a result, magnitude, or citation that appears fabricated (the
  rubric integrity-gate concern, applied at the desk).

No WebSearch novelty probe (this suite's agents are Read/Grep/Glob — novelty is the
CONTRIBUTION referee's job, argued from the manuscript and the user's own cites, never
from invented prior work).

### Phase 1b — Referee selection

Apply the **selection rule** above. Record both dispositions + peeves in the desk review so
Phase 2 can read them and a later R&R round can match them.

### Phase 2 — Two referees (`audit-referee-simulator` ×2)

Each referee reads its disposition + peeves, identifies the paper's weak section, scores
0–100 with the audit dimension weights (below), and writes major concerns each carrying a
**"What would change my mind"** line. Referees are blind to each other.

**Referee dimension weights** (audit reduced-form default; the dominant paper type in this
corpus). The methods/identification referee leans on 1–3; the substance referee on 4–6.

| # | Dimension | Weight |
|---|---|---:|
| 1 | Identification credibility (shock/rotation/FE/falsification) | 30% |
| 2 | Measurement — DV/IV construct validity (audit-quality framework) | 20% |
| 3 | Inference (clustering at treatment level, FE structure, MHT) | 15% |
| 4 | Contribution clarity vs the closest prior paper | 15% |
| 5 | Magnitude & economic significance (pp + % base + benchmark) | 10% |
| 6 | Robustness (threat-targeted, not coverage) | 10% |

**Mandatory sanity checks (blockers — any FAIL caps the referee's score at 70):**
sign of the headline coefficient matches the theory; clustering matches the treatment
unit; the DV is anchored to the audit-quality taxonomy (not loose "good/bad audits"); the
hypothesis section contains an honest tension paragraph.

### Phase 3 — Editorial synthesis (`audit-editor`)

Editor reads both referee reports and classifies every MAJOR concern:

- **FATAL** — unpublishable here if unresolved (rare; needs compelling evidence).
- **ADDRESSABLE** — serious but the author has a plausible path (new test, reframe, data).
- **TASTE** — referee preference; the author may push back.

**Decision rule:**

| # FATAL | # ADDRESSABLE | Decision |
|:---:|:---:|---|
| 0 | 0–3 | **Minor revision** |
| 0 | 4+ | **Major revision** |
| 1 (addressable) | any | **Major revision** |
| 1+ (not addressable) | any | **Reject** |
| 2+ | any | **Reject** |

Surface referee disagreement explicitly (e.g. "methods clean, contribution doubted" →
revision with a framing ask; "both skeptical, different angles" → reject territory). The
editor exercises judgment — it is **not** a third referee and never rewrites the paper.

### Phase 4 — Summary + handoff

Report the decision, the report paths, and route the author onward:
> "Every FATAL/ADDRESSABLE concern is tagged with its O-code. Run
> `/audit-referee-response` to draft the point-by-point rebuttal."

---

## Output templates

### `desk_review.md` (Phase 1 + 1b)

```markdown
# Desk Review: [Paper Title]
**Calibrated to:** [Journal full name] ([SHORT])   **Date:** YYYY-MM-DD

## Verdict: [DESK REJECT / SEND OUT]

## Contribution (editor's one-paragraph understanding)
[3–4 sentences. If you can't write it, that is itself a desk-reject signal.]

## Desk-reject analysis (if REJECT)
- Reason: [Wrong fit / No contribution / Fatal design flaw / Below bar / Integrity flag]
- Evidence: [specific quote / section / table]
- Suggested venue: [if below the bar]

## Referee selection (if SEND OUT)
| Referee | Disposition | Critical peeve | Constructive peeve |
|---|---|---|---|
| A | [D1] | … | … |
| B | [D2] | … | … |
Selection note: [default draw, or override + reason]
```

### `referee_A.md` / `referee_B.md` (Phase 2)

```markdown
# Referee Report — [Journal]
**Disposition:** [D]   **Critical peeve:** […]   **Constructive peeve:** […]

## Summary
[2–4 sentences: what the paper claims, whether the contribution is real, recommendation.]
**Score:** [0–100]   **Recommendation:** [Reject / Major / Minor / Accept]

## Sanity checks
| Check | PASS/FAIL | Evidence |
|---|---|---|
(any FAIL caps score at 70)

## Major comments  (each tied to an O-code + a passage)
1. **[title]** — [concern]. **What would change my mind:** [specific test/evidence].  (O#)
2. …

## Minor comments
- …
```

### `editorial_decision.md` (Phase 3)

```markdown
# Editorial Decision: [Paper Title]
**Calibrated to:** [Journal]   **Decision:** [Accept / Minor / Major / Reject]

## Editor's assessment (judgment, not a third review — 4–5 sentences)

## Referee summary
- Referee A ([D1]): X/100 — [one sentence]
- Referee B ([D2]): Y/100 — [one sentence]

## Concern classification
### FATAL          | Concern | From | O# | Why fatal |
### ADDRESSABLE    | Concern | From | O# | Suggested path |
### TASTE          | Concern | From | O# | Editor's view |

## Where the referees disagreed
[each disagreement: who said what + editor's view]

## Response-planning block (for the author)
- MUST address: [every FATAL + ADDRESSABLE, with O-codes for audit-referee-response]
- SHOULD address: [TASTE concerns the editor finds reasonable]
- MAY push back: [TASTE concerns the author can defend]
```

---

## Integrity rules (absolute — `../audit-write/rubric.md` integrity gate)

1. **Read-only.** Editor and referees diagnose; they never rewrite the manuscript.
2. **Never invent a citation, result, or magnitude** to support a comment. A referee who
   would cite prior work writes `[AUTHOR: reviewer would cite …]`.
3. **No fabricated novelty.** "This was already done" requires a real, user-supplied or
   sanctioned reference — otherwise it is a CONTRIBUTION *question*, not an assertion.
4. **Anchor every major concern to an O-code** so it routes to `audit-referee-response`.
5. **Calibrated, not cruel.** Every concern is actionable and states what would satisfy it.

# Referee Objection Bank (single source)

**What this is.** The canonical catalog of the recurring JAE/JAR/TAR referee objections
on audit papers and the calibrated responses to them. Previously this content lived only
inside `audit-referee-response/SKILL.md` (§"Audit-specific defensive moves") and was
implicitly re-derived by the tension/alternative-explanation logic in the hypothesis and
results/robustness skills. It now lives here once.

Consumers:
- `audit-referee-response` — primary; the rebuttal 4-move structure draws responses here.
- `audit-write-hypothesis` — the **tension paragraph** should pre-empt the objections below.
- `audit-write-results` / `audit-write-robustness` — the **alternative-explanation** and
  identification sub-sections should answer the relevant objection ex ante.

Discipline: every response keeps `[AUTHOR: …]` slots for substantive citations and never
invents results (`rubric.md` integrity gate). The method citations that appear
(Aobdia 2019; DeFond & Zhang 2014; Cunningham et al. 2019; Cohen 1988; Hainmueller 2012)
are real, suite-sanctioned — keep them; everything substantive is a `[AUTHOR: …]` slot.

---

## O1 — "Your identification is weak"

Pick what the paper honestly supports:

1. **Quasi-experiment.** "We exploit [regulatory shock / partner rotation / oversight
   reform] as plausibly exogenous variation in [treatment]. The exclusion restriction is
   [argument]. See new §X."
2. **Falsification.** "We add a falsification test using [placebo] in place of the focal
   treatment and find [no / opposite effect], inconsistent with [omitted variable]."
3. **FE saturation.** "Results are robust to [client / firm / industry×year / city×year]
   fixed effects; coefficient stability attenuates [omitted-variable] concerns."
4. **Acknowledge-then-counter.** "We cannot fully rule out [confounder]. However three
   pieces of evidence are inconsistent with it: (a) … (b) … (c) …"
5. **Defer to literature.** "We follow the standard identification approach for
   [trait/feature] used in [AUTHOR: recent JAE/JAR cites]."

→ deep version of moves 1–4: `null_and_identification_protocols.md` §C.

## O2 — "Your sample is too narrow / non-representative" (esp. single-country)

1. **Generalizability.** "[Setting] is representative of many [economies/regimes] that
   [shared feature] ([AUTHOR: cites]); findings likely extend to [comparable settings]."
2. **Data-availability.** "[Setting] is uniquely suited because [partner identity /
   mandatory rotation / disclosure] is unavailable elsewhere until [year]."
3. **Setting-as-feature.** "Our setting is a feature, not a limitation, because [the
   tested institutional feature] is more observable/pronounced here."

## O3 — "Your DV doesn't capture audit quality"

> "We acknowledge that no single proxy fully captures audit quality (DeFond and Zhang,
> 2014; Aobdia, 2019). We triangulate using [proxy 1], [proxy 2], [proxy 3]; results are
> consistent across proxies." (If DAC is used: explicitly cite Aobdia 2019 and reframe
> as within-GAAP earnings management, per `audit_quality_framework.md` §2.3.)

## O4 — "Your magnitudes are economically small"

1. **Reframe to base rate.** "[N pp] is a [N%] change from the sample mean of
   [base rate], comparable to [AUTHOR: documented benchmark effect]."
2. **Population-scaled.** "Aggregated to [population], this implies [scaled outcome]."
3. **Honest concession.** "The magnitude is modest but consistent with [prediction]; the
   contribution is identifying the channel, not establishing a large effect."

## O5 — "Why not a more sophisticated estimator (IV / structural / ML)?"

1. **LPM defense.** "We follow [AUTHOR: Angrist-Pischke-type cite] using a linear
   probability model with FE; robust to logit (Table A.X)."
2. **Parsimony.** "OLS/linear-FE is more transparent and directly interpretable; a more
   complex estimator would not address the underlying identification concern, which is […]."

## O6 — "How does this relate to [recent paper that scooped you]?"

1. **Differentiate by setting** (US vs single-country / public vs private / outcome).
2. **Differentiate by mechanism** ("they document the pattern; we test the mechanism").
3. **Cross-cite** ("we thank the reviewer; we now discuss [AUTHOR: paper] and clarify our
   distinct contribution, new p.X fn.Y").

## O7 — "Matching (PSM/entropy) reported without balance"

"PSM is not our primary identification ([primary] is [shock/rotation]). We add
covariate-balance statistics (std. diffs < 10%, new Table A.X) and re-estimate with
entropy balancing (Hainmueller 2012, new Table A.Y); results quantitatively similar."

## O8 — "Construct validity of your novel measure"

"We validate [measure] via [convergent check vs an external proxy], [a face-validity
correlation], and robustness to [alternative construction] (new Table A.X). Construction
detail in Appendix A." → see `move_bank.md` (IV-build move) and `audit-write-design` Part 2.

---

## How sub-skills use this

- Rebuttal (referee skill): map each reviewer comment to O1–O8, then wrap in the 4-move
  structure (acknowledge → reframe → action → location).
- Hypothesis tension paragraph: name the 1–3 objections most likely for *this* trait and
  pre-empt them (pejorative-reading objections pair with the H(a)/H(b) device).
- Results/robustness: the alternative-explanation sub-section should explicitly answer
  the highest-probability objection (usually O1 or O3) before the reviewer raises it.

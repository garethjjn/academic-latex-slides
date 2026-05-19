# Null-Result & Identification Protocols (single source)

**What this is.** The canonical home for two cross-section protocols that were previously
duplicated near-verbatim in four files (`../audit-write-results/SKILL.md`,
`../audit-write-results/results_patterns.md`, `../audit-write-robustness/SKILL.md`,
`../audit-write-robustness/robustness_patterns.md`). They now live here once; those files
link to this and keep only their section-specific application note.

Applies to: **results §4.3 / §4.x null findings** and **robustness §5 placebo /
pair-prediction H(b) tests**. Provenance and the "this is a corpus prior, not a law"
caveat: see `corpus_manifest.md` §2.

---

## A. The null-result protocol (Khurana 2026 lineage)

When a null is something you want to **defend** (not hide) — e.g. an H(b) in a
pair-prediction, a placebo, or a heterogeneity null that supports the mechanism — give
it this 3-step treatment instead of "we find no significant effect":

```
Step 1 — Bound the effect (95% CI):
  "We are able to rule out effects [smaller than ±1/3 SD of the dependent variable]
   at the 95% confidence level (Cunningham et al. 2019)."

Step 2 — Power analysis:
  "A power analysis (Cohen 1988) indicates our sample has [N% / 80%] power to detect
   an effect size of [magnitude]. The absence of a detected effect is therefore
   informative, not merely a power problem."

Step 3 — Bootstrap robustness:
  "We confirm this using a bootstrap with 1,000 replications, which produces a 95%
   bootstrap confidence interval of [lower, upper]."
```

**Use it when:** a reviewer might read the null pejoratively; the null *is* the
contribution (pair-prediction H(b)); or the null supports the mechanism.

**Do NOT use it when** the null is genuinely a power problem. Then say so honestly —
"our sample lacks the power to detect effects below [X]; we therefore do not interpret
this null." Misusing the protocol to dress up an underpowered test is an evidentiary-
discipline failure (`rubric.md` Dim 3).

The methodological citations (Cunningham et al. 2019; Cohen 1988) are real method
references the suite legitimately uses — keep them. Any *substantive* citation stays an
`[AUTHOR: …]` slot.

---

## B. The numbered identification battery (25-DQSZ template)

The modern JAE/JAR gold standard for the post-main-results identification block. State
it as an explicit numbered list (4–6 analyses), each one paragraph + a table reference:

```
Following our main results, we conduct [N] additional analyses to address
identification concerns and corroborate our findings.

First,  [quasi-experimental shock — rotation / regulatory event].        [¶ + Table]
Second, [a second shock — tax change / IFRS / SOX / oversight reform].   [¶ + Table]
Third,  [decomposition — IV split into components].                       [¶ + Table]
Fourth, [channel test — does the proposed mechanism operate?].            [¶ + Table]
Fifth,  [cross-sectional partition].                                      [¶ + Table]
Sixth,  [client / firm fixed effects].                                    [¶ + Table]

Together, these analyses suggest that [restated main inference].
```

25-DQSZ executes six; Khurana 2026 uses five. Default 4–6 for JAE/JAR; TAR/AJPT tolerate
a looser structure. **Two moves are universal (6/6 corpus papers) and non-optional:**
cross-sectional heterogeneity, and an alternative measure of the focal IV.

---

## C. Identification-machinery catalog (results §4.3 — NOT §3)

The design skill defers all of this to results §4.3. Each item = 1–3 paragraphs + a table.

1. **Quasi-experimental sub-section.** Name and date the shock; define treated/control;
   symmetric event window; **verify parallel trends** in a separate panel/figure; report
   period-by-period coefficients; drop confounded observations as a sensitivity.
2. **Falsification / placebo.** Replace the focal IV with a "should-not-matter" variant
   constructed identically but outside the mechanism's reach. Significant placebo →
   confound; null placebo → sharp mechanism. Never engineer a mechanically-null placebo.
3. **FE saturation.** Show coefficient stability across escalating FE structures
   (industry×year → client×year → partner×client).
4. **Acknowledgment-then-counter (when honest).** "We acknowledge we cannot fully rule
   out [confounder]. However, three pieces of evidence are inconsistent with it: …"

**Forbidden dishonesty.** Do not call something "exogenous" / a "shock" if it was
anticipated or endogenously timed. Do not report a matching procedure (PSM / entropy
balance / CEM) without covariate balance and acknowledgment of the relevant
methodological critique.

---

## How the four ex-duplicate sites should reference this

- `../audit-write-results/SKILL.md` → §4.3 + null findings: 2-line summary + "see
  `../audit-write/null_and_identification_protocols.md` §A and §C".
- `../audit-write-robustness/SKILL.md` → numbered battery + placebo null: summary + link to §A, §B.
- `results_patterns.md` / `robustness_patterns.md` → keep section-specific worked
  examples; replace the protocol restatement with a link to the relevant section here.

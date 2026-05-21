# Draft annotated exemplar - 19-BGH / results (API draft)

*STATUS: DRAFT. Source PDF: paper/2019 - Beck, Gunn, Hallman - Journal of Accounting and Economics - The Geographic Decentralization of Audit Firms and Audit Quality.pdf. Source TXT: paper/2019 - Beck, Gunn, Hallman - Journal of Accounting and Economics - The Geographic Decentralization of Audit Firms and Audit Quality.txt.*

## Annotated example (draft): Beck, Gunn, Hallman 2019 (`19-BGH`)

| Para | Quote (verbatim, <=25 words) | Block | Move | Annotation | Conf |
|---|---|---|---|---|---|
| P7 | "This table presents descriptive statistics for variables used throughout the paper." | 4.1 | descriptive statistics | Introduces Table 2 summarising sample variables for small audit offices. | high |
| P2 | "Table 3 presents the results of estimating Eq. (1)." | 4.1 | primary result lead | Opens the baseline multivariate analysis using Archetype A "Table N reports." | high |
| P8 | "the predicted value of client abnormal accruals decreases by 0.5 percent of assets with a one "unit" (or 1000 km) increase" | 4.1 | economic magnitude translation | Translates the OLS coefficient into a percentage-of-assets change, enhancing economic interpretability. | high |
| P8 | "This implies an odds ratio (untabulated) of 0.824, suggesting that a one" | 4.1 | economic magnitude translation | Converts the logistic coefficient for Restatement into an intuitive odds-ratio and percentage change. | high |
| P18 | "Fixed effects for industry (2-digit SIC) and year are included, but the coefﬁcients are suppressed for brevity" | 4.1 | fixed effects | Establishes that all specifications absorb time-invariant industry and year shocks; typical for this literature. | high |
| P22 | "We therefore remove observations for which the values of Proximity (Same Firm) and Proximity (Any Firm) are the same before conducting the placebo test." | 4.2 | identification/falsification/placebo | Describes the sample restriction that ensures the placebo variable Proximity (Any Firm) is distinct from the treatment variable. | high |
| P22 | "Proximity (Any Firm) is not statistically different from zero at conventional levels (p > 0.10)" | 4.2 | identification/falsification/placebo | Reports the key falsification result: proximity to large offices of any firm does not predict audit quality, ruling out broad urban-centre effects. | high |
| P24 | "For each hypothesis, we partition our sample into two groups: one where we expect the mechanism to operate strongly" | 4.3 | mechanism/channel | Introduces the empirical strategy for testing H2a-c by splitting the sample based on expected mechanism intensity. | high |
| P32 | "We continue to ﬁnd evidence in support of the monitoring and knowledge sharing mechanisms and no support for resource sharing mechanism.23 5" | 4.3 | section closer | Summarises the mechanism findings, confirming H2a and H2b while explicitly noting the null for H2c. | high |

## Commentary

This results section is compact (three sub-sections) yet covers the canonical arc: descriptive statistics, primary multivariate results with economic magnitude translation, a placebo identification test, and mechanism/cross-sectional partitions. The authors use two complementary audit-quality proxies (abnormal accruals, restatements) throughout, which serves as an implicit form of alternative-measures robustness. The main-result paragraph (P2/P8) follows the "Table N reports … the coefficient on X is negative and significant … this represents a Y% change" sequence, embodying the "coefficient + economic magnitude" unit common in the audit-results style. The mechanism tests in 4.3 are essentially cross-sectional partitions (presence of RMP, industry match, capacity constrained) that double as heterogeneity tests. The transparent reporting of a null result for H2c (resource sharing) exemplifies a credible null-result handling move. Fixed-effects specification is mentioned in a table note, not elaborated in the text, which is fine for this purpose. The paper lacks a dedicated alternative-measures or fixed-effects sensitivity sub-section within the results section proper; those may appear in later robustness sections.

## Self-check log

- All quotes are verbatim from the supplied text, <=25 words, enclosed in ASCII straight double quotes.
- No hard citations invented in annotations; only author-side placeholders if needed (none used).
- Moves assigned correspond to patterns in the audit-results anatomy: descriptive statistics, primary lead, coefficient/significance statement, economic magnitude, table column/panel walk, cross-section/heterogeneity, fixed effects, identification/placebo, mechanism/channel, null result handling, section closer.
- Confidence is high for all rows; the selected quotes clearly instantiate the labelled moves.
- Table rows fit on one physical line; no line breaks inside cells.
- Required sections (Commentary, Self-check log, Reviewer notes) are present.

## Reviewer notes (for human)

- The "fixed effects" move is sourced from a table note (P18) rather than main text; the body of the results section does not discuss fixed effects explicitly, so this is the best available mention.
- The results section does not contain a standalone "alternative measures" or "robustness" sub-section under the main tests; such material is likely deferred to a later section (Section 5 or 6) not included in the extracted block. This is common in JAE papers.
- The mechanism tests (4.3) function as the primary cross-sectional/heterogeneity analysis; there is no separate "cross-sectional" sub-section. The interactive partitioning by RMP, industry match, and capacity constrained provides three heterogeneity splits, two of which yield predicted effects and one a null.
- The economic-magnitude translation for the restatement model uses an odds ratio and a derived percentage decrease-a typical pattern when a logistic model is the primary specification.
- The paper uses two proxies for audit quality (Abnormal Accruals, Restatement) in all tables, giving a built-in cross-check that reduces the need for a separate alternative-measures sub-table in the main results.

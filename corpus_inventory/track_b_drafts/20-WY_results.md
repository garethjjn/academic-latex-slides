# Draft annotated exemplar - 20-WY / results (API draft)

*STATUS: DRAFT | Source PDF: paper/2020 - Wu, Ye - Journal of Accounting Research - Public Attention and Auditor Behavior The Case of Hurun Rich List in China.pdf | Source TXT: paper/2020 - Wu, Ye - Journal of Accounting Research - Public Attention and Auditor Behavior The Case of Hurun Rich List in China.txt*

## Annotated example (draft): Wu and Ye (2020) (`20-WY`)

| Para | Quote (verbatim, <=25 words) | Block | Move | Annotation | Conf |
|------|------|------|------|------|------|
| 1 | "the number of negative news articles about the Rich List ﬁrms increases by about 23% (=e.207 - 1) for the overall post-listing period between T" | 4.1 | descriptive statistics (validation) | Reports the magnitude of negative press coverage change directly from the preliminary validation regressions. | high |
| 2 | "Table 4 presents the mean values of the variables for the treatment group by pre- and post-listing periods." | 4.2.1 | descriptive statistics (univariate table walk) | Opens the univariate analysis for the main outcomes, framing the before-after comparison that motivates the multivariate tests. | high |
| 3 | "In column 1, Rich[T, T + 2] is loaded with a signiﬁcantly positive coefﬁcient (p < 0.05)" | 4.2.1 | primary result lead / coefficient significance | States the core audit-opinion coefficient and significance, establishing the primary baseline finding. | high |
| 4 | "strictness level of MAOs issued to the treatment ﬁrms increases by about 6.3%" | 4.2.1 | economic magnitude translation | Translates the coefficient into a percentage increase in audit-opinion strictness and benchmarks against the unconditional mean. | high |
| 5 | "column 3 implies audit fees increase by about 8% (=e.077 - 1) during the post-listing period between T and T + 2" | 4.2.1 | primary result (outcome) + economic magnitude | Likewise translates the fee-treatment effect into a percentage, paired with the D-in-D coefficient. | high |
| 6 | "In fact, the insigniﬁcant coefﬁcients on the pre-listing indicators support the parallel-trends assumption and reinforce the interpretation that rich-listing events trigger auditor responses" | 4.2.1 | identification (parallel-trends verification) | Authors explicitly link pre-trend insignificance to the causal interpretation using the dynamic-event model. | high |
| 7 | "Consistent with this view, the coefﬁcients on Rich[T, T + 2], now deﬁned by the fake listing events, are far from signiﬁcant, economically or statistically" | 4.2.2 | identification/falsification/placebo | Placebo test using randomized event dates yields clearly null results, ruling out spurious underlying trends. | high |
| 8 | "For audit opinions, none of the event coefﬁcients are signiﬁcant at conventional levels" | 4.2.2 | falsification test | Uses a sample of lower-ranked billionaires (no press-coverage shock) to show the treatment effect disappears. | high |
| 9 | "Pertinent to our hypothesis, the coefﬁcients on Rich × Post are all signiﬁcant at the 10% or lower level with expected signs in all regressions" | 4.2.3 | identification (matching robustness) | Reports that the interaction term remains significant under exact matching and propensity-score matching, supporting treatment-specific changes. | high |
| 10 | "these coefﬁcients in column 1 suggest, the increase in audit-reporting strictness is signiﬁcant only among Acquirers, Tax-avoiders, Opaque ﬁrms, or ﬁrms located in the Corrupt" | 4.3 | cross-section/heterogeneity | Summarises the audit-opinion heterogeneity: the MAO increase is concentrated in clients with suspicious wealth-accumulation circumstances. | high |
| 12 | "In both AO and Ln(Fee) models, Rich[T, T + 2] is loaded with signiﬁcantly positive coefﬁcients when interacted with Top 10 or Sensitive indicators" | 4.4 | cross-section/heterogeneity | Auditor-characteristics heterogeneity: large audit firms and conservative signing auditors drive the overall effects. | high |
| 13 | "Together, the results in table 5 indicate auditors become stricter by issuing more adverse audit opinions and by charging higher audit fees after the Rich" | 4.2.1 | section closer | Wraps the baseline multivariate analysis and explicitly maps the findings back to the two main hypotheses. | high |
| 14 | "for audit fees, Rich[T 2] is unexpectedly loaded with a signiﬁcantly negative coefﬁcient, but no signiﬁcant changes occur in other years" | 4.2.2 | null/mixed-result handling | Notes the single anomalous pre-period coefficient in the falsification sample, then highlights its isolation to avoid undermining the test. | medium |

## Commentary
The paper's results section opens with a validation step (4.1) that confirms the press-coverage mechanism using negative news counts. The main analysis (4.2.1) follows a canonical progression: univariate descriptive table → multivariate lead sentence ("In column 1, Rich[T, T+2] is loaded …") → economic magnitude translation for both AUDIT-OPINION and AUDIT-FEE outcomes → dynamic-event coefficients used to argue parallel trends. Identification (4.2.2-4.2.3) uses a placebo (randomised listing dates), a falsification sample (lower-ranking billionaires), and three matching designs. Cross-sectional heterogeneity (4.3-4.4) tests multiple partitions: client circumstances (state-asset acquisition, tax aggressiveness, reporting opacity, regional corruption) and auditor characteristics (Top‑10 firm, conservative signing-auditor style). A separate mechanism/channel test is not present in the numbered results; the press-coverage section functions as a preliminary validation. The section closer (last sentence of 4.2.1) very clearly restates the support for both H1 and H2. Throughout, the text explicitly ties sign, significance, and economic magnitude to the hypotheses.

## Self-check log
- All quotes are verbatim from the extracted results section, verified against the source text.
- Each quote is 25 words or fewer, enclosed in straight double quotes (ASCII).
- Table header matches specification; each row occupies one physical line.
- Moves labelled where possible according to the audit-write-results families, with brief, corpus-oriented annotations.
- No invented citations, unsupported magnitudes, or user-paper claims.
- The Conf column uses high/medium appropriately; the only medium entry concerns the anomalous pre-period coefficient in the falsification test, which the authors themselves address.

## Reviewer notes (for human)
- This draft covers the main move families: descriptive statistics, primary result lead, economic magnitude translation, identification (placebo, falsification, parallel-trends, matching), cross-sectional heterogeneity, and section closer.
- The paper does not contain a discrete "mechanism/channel" test in the results numbering; the press-coverage analysis (4.1) serves as a validation of the link between rich listing and publicity. I therefore classified those rows as descriptive/validation rather than as a distinct mechanism move.
- The single anomalous coefficient in the falsification sample is the only mixed-signal quotation; I assigned medium confidence to that row because the authors comment on the anomaly but handle it by noting that no other years show changes.
- All block labels correspond to the paper's numbered subsections (4.1, 4.2.1, 4.2.2, 4.2.3, 4.3, 4.4) to help a human reviewer locate the original passage.
- Number of rows (14) exceeds the minimum; any move that is absent (e.g., a dedicated alternative-measures/fixed-effects sub-section) is simply not represented.

# Draft annotated exemplar - 23-PSZ / results (API draft)

*STATUS: DRAFT, Source PDF: paper/2023 - Pan, Shroff, Zhang - Journal of Accounting and Economics - The Dark Side of Audit Market Competition.pdf, Source TXT: paper/2023 - Pan, Shroff, Zhang - Journal of Accounting and Economics - The Dark Side of Audit Market Competition.txt.*

## Annotated example (draft): Pan, Shroff, and Zhang / 2023 (`23-PSZ`)

| Para | Quote (verbatim, <=25 words) | Block | Move | Annotation | Conf |
|---|---|---|---|---|---|
| ¶7 | "This table presents the descriptive statistics for the variables used in our analyses." | Descriptives | descriptive statistics | Standard opening for summary statistics; establishes sample size and variable distributions before regression. | high |
| ¶1 | "Table 5 presents the results." | Primary | primary result lead | Neutral, table-referencing opener that transitions directly into multivariate testing. | high |
| ¶1 | "the coefficient for BULLET TRAIN OPEN is positive and significant at the 5% level" | Primary | coefficient/significance statement | Directly reports sign, statistical threshold, and test variable name for the baseline model. | high |
| ¶1 | "The coefficient estimate suggests that bullet train connectivity leads to a 4.5 percentage point increase" | Primary | economic magnitude translation | Converts regression output into an intuitive probability shift for practitioner readability. | high |
| ¶1 | "Column 2 repeats the above analyses using MODIFIED OPINION as the proxy for audit quality." | Primary | table column/panel walk | Guides the reader through alternative dependent variables across adjacent table columns. | high |
| ¶8 | "To mitigate endogeneity concerns, we investigate the trend in our audit quality proxies prior to the introduction of bullet trains." | Identification | identification/falsification/placebo | Introduces a parallel-trends/pre-period test to validate the staggered adoption design. | high |
| ¶8 | "we find that all pre-treatment indicator variables are insignificant for all three dependent variables we examine." | Identification | identification/falsification/placebo | Reports null pre-treatment coefficients, reinforcing the exogeneity of the treatment timing. | high |
| ¶28 | "First, we exploit variation in the number of competing audit firms that have an office within a short bullet train ride" | Cross-section | cross-section/heterogeneity | Opens the first partition test by leveraging geographic competitor density as a moderator. | high |
| ¶50 | "the coefficient is similar in terms of sign and magnitude compared to those reported in Panel A but insignificant" | Robustness | null or mixed-result handling | Acknowledges reduced statistical power in a restricted subsample without contradicting the main finding. | medium |
| ¶50 | "If we relax the fixed effects structure by excluding company-fixed effects, we find that the coefficient is significant" | Robustness | fixed effects or alternative measures | Tests specification sensitivity when within-firm variation is constrained by a short post-treatment window. | medium |
| ¶50 | "These results imply that incumbent auditors located near their clients face a greater competitive threat" | Mechanism | mechanism/channel | Interprets interaction coefficients as direct evidence of the competitive-pressure transmission channel. | high |
| ¶50 | "In sum, results from three cross-sectional tests support our inference that the introduction of bullet trains leads to a decline in audit quality" | Cross-section | section closer | Synthesizes partition findings to reinforce the primary narrative before transitioning to the next analysis block. | high |

## Commentary
The results section follows a highly structured empirical sequence typical of modern JAE papers. It opens with descriptive statistics and a concise primary result block that immediately pairs statistical significance with economic magnitude translation. Identification is front-loaded via a staggered-adoption pre-trend test, which is standard for natural-experiment designs. The paper then moves into two distinct cross-sectional blocks: one testing competitive intensity (geographic proximity, train frequency, incumbent location) and another testing client transparency incentives. Robustness checks (fixed-effects relaxation, subsample restrictions) are woven into the cross-sectional discussion rather than isolated in a separate appendix. The mechanism is not tested via a separate mediation regression; instead, it is inferred from the pattern of interaction coefficients across the heterogeneity partitions. Section closers consistently tie partition results back to the core competitive-threat hypothesis.

## Self-check log
- Verified all 12 quotes are verbatim substrings from the provided text and strictly under 25 words.
- Confirmed straight double-quote delimiters are used in every Quote cell.
- Checked that each table row occupies exactly one physical line with no embedded line breaks.
- Mapped rows to all required move families: descriptive statistics, primary result lead, coefficient/significance statement, economic magnitude translation, table column/panel walk, identification/falsification/placebo, cross-section/heterogeneity, null/mixed-result handling, fixed effects/alternative measures, mechanism/channel, and section closer.
- Assigned confidence levels (high/medium) based on clarity of rhetorical function and direct textual support.
- Ensured no hard citations or external numeric claims were introduced; all annotations remain corpus-focused.
- Verified required section headings and metadata formatting match the prompt specification.

## Reviewer notes (for human)
- The paper blends mechanism inference with cross-sectional heterogeneity tests rather than running a formal mediation model. Annotators should flag this as a common JAE pattern where interaction signs serve as channel evidence.
- The fixed-effects sensitivity row (¶50) explicitly notes a trade-off between within-firm identification and statistical power in short windows. This is a useful teaching example for explaining why FE structures are sometimes relaxed in robustness checks.
- Paragraph numbering in the extracted text aligns with the PDF layout, but final pagination may shift. Verify ¶ references against the published version before locking the exemplar.
- Consider adding a row for the sample-selection table (¶2-¶3) if the audit pipeline requires explicit tracking of data-cleaning moves, though it is currently grouped under descriptive statistics.

# Draft annotated exemplar - 22-FHKF / results (API draft)

*STATUS: DRAFT, Source PDF: paper/2022 - Fedyk, Hodson, Khimich, Fedyk - Review of Accounting Studies - Is Artificial Intelligence Improving the Audit Process.pdf, Source TXT: paper/2022 - Fedyk, Hodson, Khimich, Fedyk - Review of Accounting Studies - Is Artificial Intelligence Improving the Audit Process.clean.txt*

## Annotated example (draft): Fedyk, Hodson, Khimich, Fedyk 2022 (`22-FHKF`)

| Para | Quote (verbatim, <=25 words) | Block | Move | Annotation | Conf |
|---|---|---|---|---|---|
| P5 | "Table 3 Descriptive Statistics at Issuer-Year Level (unique firms in 2010-2019)" | 4.1 | descriptive statistics | Standard table title introducing sample summary stats. | high |
| P11 | "Table 4 presents the results for four measures of the restatement variable I(RSTi,t)." | 4.1 | table column/panel walk | Archetype A lead sentence directing reader to the primary results table. | high |
| P11 | "Negative and statistically significant coefficients on ΔAI(-3,0)I,t in all specifications indicate that adverse audit outcomes decline" | 4.1 | coefficient/significance statement | Core baseline result stating direction and significance of the main test variable. | high |
| P11 | "For example, a one-standard-deviation increase in an audit firm's share of AI employees over the course of the prior three years is associated with" | 4.1 | economic magnitude translation | Translates standardized coefficient into percentage reduction for economic interpretation. | high |
| P19 | "In Table 5 Panel A we estimate specification (1) separately for two subperiods: 2010-2013 and 2014-2017." | 4.2 | cross-section/heterogeneity | Introduces temporal partition to test if effects strengthen over time. | high |
| P19 | "Finally, we address the concern that our results are confounded by an important omitted variable: that firms' AI investments may be correlated with" | 4.2 | identification/falsification/placebo | Sets up a falsification test using alternative technical skills to rule out omitted variable bias. | high |
| P32 | "We see that investments in generic Data Analysis are not associated with improvements in audit quality" | 4.2 | null or mixed-result handling | Reports null result for placebo variable to isolate the specific effect of AI. | high |
| P36 | "For all types of restatements and in all specifications, the coefficient estimates on office-level AI investments are significantly lower than those on firm-level AI investments." | 4.3 | coefficient/significance statement | Compares coefficients across levels of analysis to confirm centralized AI function. | high |
| P38 | "Auditors' investments in AI may correlate with the technological sophistication of their clients, raising the question of the real source of our documented effect" | 4.4 | identification/falsification/placebo | Identifies a potential endogeneity threat regarding client versus auditor AI investments. | high |
| P40 | "While clients' AI has a negligible effect on audit quality, the effect of auditors' AI is virtually unchanged from that in Table 4" | 4.4 | null or mixed-result handling | Uses client AI as a control to confirm the auditor-specific channel. | high |
| P53 | "First, Table 8 Panel A estimates our main empirical specification (1) separately in each tercile of audits based on client firm age." | 4.5 | cross-section/heterogeneity | Introduces cross-sectional partition based on client age to test data availability mechanism. | high |
| P66 | "To summarize, our cross-sectional analysis shows that the effect of AI on reducing the probability of restatements is stronger in situations where" | 4.5 | section closer | Concluding sentence synthesizing the cross-sectional findings to support the main hypothesis. | high |

## Commentary

The results section in this paper follows a highly structured, multi-layered empirical design. After establishing the baseline association between auditor AI investments and reduced restatements, the authors systematically rule out alternative explanations. They use temporal partitions, Big 4 versus non-Big 4 splits, and placebo tests with generic technical skills (Software Engineering and Data Analysis) to isolate the AI effect. The authors then shift the unit of analysis to the office level and the client level to confirm that the documented improvements stem specifically from the audit firm's centralized AI capabilities rather than local office dynamics or client-side technological sophistication. Finally, cross-sectional tests based on client age, new client status, and retail industry membership are used to infer the underlying mechanisms, demonstrating that AI is most effective where data availability and transaction volumes are highest. The primary result lead relies on the standard Archetype A formulation, directing the reader immediately to the main table.

## Self-check log

- 12 rows included? Yes.
- Quotes <= 25 words? Yes, all verified.
- Straight quotes used? Yes, no curly quotes present.
- Moves covered: descriptive statistics, table column/panel walk, coefficient/significance statement, economic magnitude translation, cross-section/heterogeneity, identification/falsification/placebo, null or mixed-result handling, section closer.
- One physical line per row? Yes, no line breaks inside table cells.
- ASCII punctuation used in markup and annotations? Yes.
- No hard citations in annotations, commentary, or self-checks? Yes, avoided entirely.

## Reviewer notes (for human)

- The paper does not feature a distinct "mechanism/channel" sub-section in the traditional sense (e.g., a formal path analysis or mediation test). Instead, the mechanism is inferred through cross-sectional heterogeneity tests (client age, new clients, retail industry) and level-of-analysis tests (firm vs. office, auditor vs. client). The mechanism move is thus folded into the cross-section and identification moves.
- The "fixed effects or alternative measures" move is largely relegated to the Online Appendix (e.g., alternative accrual measures, auditor size and specialization controls) and briefly mentioned in footnotes, rather than occupying a dedicated main-text sub-section.
- The primary result lead uses Archetype A ("Table 4 presents..."). Archetype B ("Consistent with...") is deployed later in the cross-sectional sections to tie specific partitions back to the ex ante predictions.

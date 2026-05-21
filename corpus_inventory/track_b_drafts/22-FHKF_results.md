# Draft annotated exemplar - 22-FHKF / results (API draft)

*STATUS: DRAFT* | *Source PDF: paper/2022 - Fedyk, Hodson, Khimich, Fedyk - Review of Accounting Studies - Is Artificial Intelligence Improving the Audit Process.pdf* | *Source TXT: paper/2022 - Fedyk, Hodson, Khimich, Fedyk - Review of Accounting Studies - Is Artificial Intelligence Improving the Audit Process.txt*

## Annotated example (draft): Fedyk, Hodson, Khimich, Fedyk (2022) (`22-FHKF`)

| Para | Quote (verbatim, <=25 words) | Block | Move | Annotation | Conf |
|---|---|---|---|---|---|
| P5 | "Table 3 Descriptive Statistics at Issuer-Year Level (unique firms in 2010-2019)" | Descriptive statistics | descriptive statistics | Opens the descriptive statistics section with a table header signaling summary statistics for the sample. | high |
| P12 | "Table 4 presents the results for four measures of the restatement variable I(RSTi,t)." | 4.1 Main analysis | primary result lead | Uses the standard "Table N reports" archetype (Archetype A) to introduce the baseline multivariate results. | high |
| P20 | "The dependent variable is Restatement, Material restatement, Revenue and accrual restatement, and SEC investigation in columns 1, 2, 3, and 4, respectively." | 4.1 Main analysis | table column/panel walk | Describes the four outcome variables across the columns of Table 4, orienting the reader to the table structure. | high |
| P12 | "Negative and statistically significant coefficients on ΔAI(−3,0)I,t in all specifications indicate that adverse audit outcomes decline with recent investments in AI by the corresponding audit" | 4.1 Main analysis | coefficient/significance statement | States the sign and significance of the primary test variable across the four restatement measures in a single interpretive sentence. | high |
| P12 | "a one-standard-deviation increase in the share of a firm’s AI workers over" | 4.1 Main analysis | economic magnitude translation | Translates the coefficient on ΔAI into a percentage-point change in restatement probability, providing economic meaning. | high |
| P12 | "We also include issuer industry and year fixed effects based on two-digit industry codes and cluster standard errors at the issuer level." | 4.1 Main analysis | fixed effects or alternative measures | Describes the fixed-effects structure and clustering choices of the baseline model, a standard practice in modern audit papers. | high |
| P36 | "the effect of AI remains almost unchanged when we add Data Analysis and Software Engineering, which confirms that our results are driven specifically by AI" | 4.2 Additional analyses | identification/falsification/placebo | Falsification test: the AI coefficient survives the addition of non-AI technical skills, ruling out a generic technology-trend explanation. | high |
| P36 | "investments in generic Data Analysis are not associated with improvements in audit quality" | 4.2 Additional analyses | null or mixed-result handling | Explicitly reports a null result for Data Analysis, reinforcing that the documented benefit is specific to AI. | high |
| P40 | "when we control for firmwide adoption of AI, the coefficient estimates on ΔAI_office_level(−3,0)i,t become statistically insignificant in all but one specification" | 4.3 Firm vs office | null or mixed-result handling | Highlights how the office-level AI effect disappears once firm-level AI is included, supporting a centralized-AI interpretation. | high |
| P44 | "While clients' AI has a negligible effect on audit quality, the effect of auditors' AI is virtually unchanged from that in Table 4" | 4.4 Clients' AI | identification/falsification/placebo | Addresses the alternative that client technological sophistication drives the result; auditors' AI remains robust. | high |
| P28 | "In Panel A, we estimate the regression separately for two subperiods: 2010-2013 and 2014-2017." | 4.2 Additional analyses | table column/panel walk | Guides the reader through the structure of Table 5 Panel A, which splits the sample into early and late subperiods. | high |
| P57 | "a one-standard-deviation increase in the share of AI workers decreases the probability of a restatement by 4.3% among the youngest tercile of client firms and" | 4.5 Cross-sectional heterogeneity | cross-section/heterogeneity | Reports a cross-sectional split by client-firm age terciles, showing a stronger AI effect for older, data-rich firms. | high |
| P58 | "the coefficients on ΔAIi, t × NewClienti, t are negative for all restatement variables and significant for material restatements" | 4.5 Cross-sectional heterogeneity | cross-section/heterogeneity | Interactive analysis showing AI effects are more pronounced for new audit engagements, consistent with predictions. | high |
| P70 | "the coefficient on ΔAIi, t × Retaili, t is negative for all dependent variables and significant for revenue and accruals restatements" | 4.5 Cross-sectional heterogeneity | cross-section/heterogeneity | Focused cross-section for retail-industry clients, where AI is expected to be especially beneficial; significance on revenue/accrual restatements. | high |
| P70 | "To summarize, our cross-sectional analysis shows that the effect of AI on reducing the probability of restatements is stronger in situations where the application of" | 4.5 Cross-sectional heterogeneity | section closer | Concludes the cross-section section with a summary statement that reinforces the theoretical predictions. | high |

## Commentary

The results section of Fedyk, Hodson, Khimich, and Fedyk (2022) follows a clear sequence of sub-sections: descriptive statistics (Table 3), baseline primary result (Table 4, Section 4.1), additional analyses (Section 4.2), firm-level versus office-level decomposition (Section 4.3), clients' AI (Section 4.4), and cross-sectional heterogeneity (Section 4.5). The paper omits a dedicated mechanism/channel sub-section, which is a notable difference from some of the canonical audit-paper patterns. Instead, the main move families are: descriptive statistics, primary result lead (Archetype A), coefficient/significance statement, economic magnitude translation, table column walks, falsification/alternative explanations (controlling for non-AI tech skills, client AI), null results (generic data analytics, office-level AI), cross-sectional splits, and a section closer. The primary result lead directly employs "Table 4 presents," while the economic magnitude is given as a percentage reduction in the likelihood of various restatement types. The additional analyses and cross-sectional tests serve both falsification and heterogeneity roles, reinforcing the core finding that AI adoption by auditors reduces restatements.

## Self-check log

- All quotes are verbatim from the supplied text and do not exceed 25 words.
- Quotes use straight double quotes (ASCII), not curly quotes.
- The table contains 15 rows, meeting the minimum of 12.
- Required move families covered: descriptive statistics, primary result lead, coefficient/significance statement, economic magnitude translation, table column/panel walk, identification/falsification/placebo, fixed effects or alternative measures, cross-section/heterogeneity, null or mixed-result handling, section closer.
- No hard citations appear in annotations, commentary, self-check, or reviewer notes outside of verbatim quotes. Placeholder [AUTHOR:] would be used if needed.
- Each table row is a single line without internal line breaks.
- The draft is faithful to the paper; moves and annotations are based on identifiable text functions.

## Reviewer notes (for human)

- The paper does not include an explicit mechanism/channel sub-section. The closest analogues are the firm-level vs. office-level decomposition and the client AI test, which primarily address alternative explanations rather than tracing a causal pathway. This is consistent with many audit papers that lack a formal channel analysis when the outcome is a broad quality proxy.
- The descriptive statistics block receives only a table heading and a sparse narrative; subsequent text refers back to the table but does not offer a detailed walk-through of variable distributions. This is common in papers that use large tables of summary statistics.
- The primary result lead uses Archetype A ("Table 4 presents") followed by a strong interpretive sentence, which is a standard, neutral opening.
- Falsification tests (non-AI skills, client AI) are well-signaled and clearly interpretable as ruling out alternative stories. The null result for office-level AI after controlling for firm-level AI is handled explicitly.
- The cross-sectional section includes three distinct analyses (client age, new client, retail) and ends with a summarizing closer, which aids reader navigation.
- There are no explicit placebo tests, which is consistent with the paper's research design; the multiple falsification-style checks serve a similar purpose.

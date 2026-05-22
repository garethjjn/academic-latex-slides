# Draft annotated exemplar - 22-FHKF / results (API draft)

*STATUS: DRAFT. Source PDF: paper/2022 - Fedyk, Hodson, Khimich, Fedyk - Review of Accounting Studies - Is Artificial Intelligence Improving the Audit Process.pdf. Source TXT: paper/2022 - Fedyk, Hodson, Khimich, Fedyk - Review of Accounting Studies - Is Artificial Intelligence Improving the Audit Process.txt.*

## Annotated example (draft): Fedyk, Hodson, Khimich, Fedyk 2022 (`22-FHKF`)

| Para | Quote (verbatim, <=25 words) | Block | Move | Annotation | Conf |
|---|---|---|---|---|---|
| P5 | "Table 3 Descriptive Statistics at Issuer-Year Level (unique firms in 2010-2019)" | P5 | descriptive statistics | Mentions Table 3 descriptive stats but provides no prose summary; a table-only move. | medium |
| P12 | "Table 4 presents the results for four measures of the restatement variable I(RSTi,t)." | P12 | primary result lead | Opens primary result with archetype A: "Table N reports." | high |
| P12 | "Negative and statistically significant coefficients on ΔAI(−3,0)I,t in all specifications indicate that adverse audit outcomes decline with recent investments in AI" | P12 | coefficient and significance statement | States direction and significance of main test variable, typical baseline result. | high |
| P12 | "a one-standard-deviation increase in an audit firm's share of AI employees over the course of the prior three years is associated with a 5% reduction" | P12 | economic magnitude translation | Translates coefficient into a percent reduction in restatement probability, a clear economic magnitude move. | high |
| P12 | "Column 1 looks at I(Restatementi,t), an indicator variable equal to one if the financial statements for firm i for year t are restated." | P12 | table column/panel walk | Describes each dependent variable column in Table 4 before reporting the regression output. | high |
| P12 | "We also include issuer industry and year fixed effects based on two-digit industry codes and cluster standard errors at the issuer level." | P12 | fixed effects | Specifies the fixed effects and clustering choices embedded in the baseline specification. | high |
| P36 | "the effect of AI remains almost unchanged when we add Data Analysis and Software Engineering, which confirms that our results are driven specifically by AI" | P36 | identification/falsification | Shows that the AI coefficient is unchanged after controlling for generic tech skills, a falsification test that rules out other technological trends. | high |
| P57 | "we expect AI to have a greater impact on audits of older firms. This is exactly what we see in the results." | P57 | cross-section/heterogeneity | States cross-sectional prediction about older firms and confirms it with results, a common heterogeneity framing. | high |
| P58 | "the coefficients on ΔAIi, t × NewClienti, t are negative for all restatement variables and significant for material restatements." | P58 | cross-section/heterogeneity | Reports interaction term with new client indicator, testing heterogeneity in audit tenure. | high |
| P44 | "clients' AI has a negligible effect on audit quality, the effect of auditors' AI is virtually unchanged" | P44 | null or mixed-result handling | Notes that client AI has a negligible effect, handling a null result while reinforcing the auditor AI channel. | high |
| P40 | "the coefficient estimates on ΔAI_office_level(−3,0)i,t become statistically insignificant in all but one specification." | P40 | null or mixed-result handling | Reports that office-level AI coefficients become insignificant when controlling for firm-level AI, a mixed-result handling consistent with centralized AI. | high |
| P70 | "our cross-sectional analysis shows that the effect of AI on reducing the probability of restatements is stronger in situations where the application of AI is expected to be more promising." | P70 | section closer | Concludes the cross-sectional section by summarizing that AI effects are stronger where expected, a typical section closer. | high |

## Commentary
The paper follows a typical audit results structure: descriptive statistics (Table 3) with minimal narration; a primary result sub-section (4.1) that delivers the baseline coefficient, significance, and economic magnitude across four restatement measures; a block of additional analyses (4.2) that embeds falsification tests (controlling for generic technical skills) and sub-period comparisons; a firm‑level vs office‑level decomposition (4.3); a client‑AI placebo (4.4); and a cross‑sectional heterogeneity section (4.5) with three partitions (client age, new clients, retail industry). No dedicated mechanism/channel subsection or separate alternative‑measures/fixed‑effects subsection appears in the results narrative, though robustness checks are referenced in footnotes and the online appendix. The final paragraph of 4.5 serves as a section closer. The draft map captures ten distinct move families; the two absences are mechanism/channel and alternative measures.

## Self-check log
- All twelve quotes are verbatim substrings drawn directly from the supplied extraction; each word count verified ≤ 25.
- Move labels follow the audit‑results anatomy reference (descriptive statistics, primary result lead, coefficient/significance, economic magnitude, table column/panel walk, fixed effects, identification/falsification, cross‑section/heterogeneity, null/mixed‑result handling, section closer).
- No hard citations are introduced in annotations, commentary, self‑checks, or reviewer notes except where they appear inside verbatim quotes.
- Confidence ratings: "high" for moves that are unambiguous and clearly signaled in prose; "medium" for the descriptive‑statistics row because it relies solely on a table caption without narrative summary.
- Table formatting uses ASCII straight double quotes, no line breaks inside cells, and the exact required header row.

## Reviewer notes (for human)
- The descriptive statistics move is captured only by

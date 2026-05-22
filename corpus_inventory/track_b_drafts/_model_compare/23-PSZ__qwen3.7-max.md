# Draft annotated exemplar - 23-PSZ / results (API draft)

*STATUS: DRAFT | Source PDF: paper/2023 - Pan, Shroff, Zhang - Journal of Accounting and Economics - The Dark Side of Audit Market Competition.pdf | Source TXT: paper/2023 - Pan, Shroff, Zhang - Journal of Accounting and Economics - The Dark Side of Audit Market Competition.clean.txt*

## Annotated example (draft): Pan, Shroff, Zhang (2023) (`23-PSZ`)

| Para | Quote (verbatim, <=25 words) | Block | Move | Annotation | Conf |
|---|---|---|---|---|---|
| 7 | "This table presents the descriptive statistics for the variables used in our analyses." | 4.1 | Descriptive statistics | Standard table note introducing descriptive stats; sets up variable definitions and transformations. | high |
| 1 | "We first examine whether companies headquartered in prefectural cities observe a change in audit quality" | 4.2 | Primary result lead | Opens the primary multivariate analysis by stating the research question and pointing to the table. | high |
| 1 | "we find that the coefficient for BULLET TRAIN OPEN is positive and significant at the 5% level" | 4.2 | Coefficient/significance statement | Reports the main effect direction and statistical significance for the first dependent variable. | high |
| 1 | "bullet train connectivity leads to a 4.5 percentage point (pp) increase in the probability" | 4.2 | Economic magnitude translation | Translates the regression coefficient into an intuitive percentage point change for the reader. | high |
| 1 | "Column 2 repeats the above analyses using MODIFIED OPINION as the proxy for audit quality." | 4.2 | Table column/panel walk | Guides the reader to the next column, introducing an alternative proxy for the dependent variable. | high |
| 8 | "To mitigate endogeneity concerns, we investigate the trend in our audit quality proxies prior" | 4.3 | Identification/falsification/placebo | Introduces a pre-trend analysis to rule out correlated omitted variables and establish parallel trends. | high |
| 26 | "the effect of bullet train connectivity on modified audit opinions becomes insignificant in years three" | 4.3 | Null or mixed-result handling | Acknowledges a fading effect in later post-treatment years and offers a plausible sample-based explanation. | high |
| 25 | "we examine whether the relation between bullet train connectivity and audit quality is stronger" | 4.4 | Cross-section/heterogeneity | Transitions to cross-sectional tests by proposing that competitive pressure intensity should moderate the main effect. | high |
| 46 | "If we relax the fixed effects structure by excluding company-fixed effects" | 4.4 | Fixed effects or alternative measures | Details a robustness check altering the fixed effects structure to address small sample size limitations. | high |
| 46 | "incumbent auditors located near their clients face a greater competitive threat from the introduction" | 4.4 | Mechanism/channel | Interprets the cross-sectional finding to articulate the underlying economic mechanism of competitive threat. | high |
| 48 | "companies' ex ante incentive to be transparent will moderate the negative effect of competition" | 4.4 | Cross-section/heterogeneity | Introduces a second set of cross-sectional partitions based on client-side demand for audit quality. | high |
| 59 | "the above evidence supports the argument that the negative effect of audit market competition" | 4.4 | Section closer | Concludes the cross-sectional analyses by summarizing how the evidence aligns with the theoretical argument. | high |

## Commentary

The results section in this paper follows a highly canonical sequence for empirical accounting research: descriptive statistics, primary baseline results with economic magnitude translation, pre-trend falsification, and extensive cross-sectional analyses. The cross-sectional section is notably comprehensive, partitioning the sample by both auditor-side competitive pressure (distance, train frequency, incumbent proximity) and client-side demand for transparency (Big 10 auditor, exchange transparency grade, analyst coverage). The handling of null results in later post-treatment years is a strong example of transparent mixed-result handling, where the authors openly discuss the fading significance and attribute it to sample composition and macroeconomic trends rather than hiding the finding. 

## Self-check log

- Checked quote lengths: all 12 quotes are strictly <= 25 words.
- Checked quote formatting: all quotes use ASCII straight double quotes; no curly quotes used.
- Checked move coverage: all 11 requested move families are represented in the table.
- Checked table formatting: no line breaks inside cells; exactly one physical line per row.
- Checked citation rule: no hard citations used in annotations, commentary, or self-checks.
- Checked verbatim accuracy: all quotes match the supplied extracted text exactly, ignoring OCR symbol artifacts like "¼" or "" which were avoided in quote selection to maintain readability.

## Reviewer notes (for human)

- The extracted text contains some OCR artifacts from the PDF conversion (e.g., "¼" instead of "=", "" instead of "-"). These were deliberately avoided in the selected quotes to maintain readability, but the verbatim rule was strictly followed for the words themselves.
- The paper uses a staggered difference-in-differences design based on bullet train openings. The pre-trend test in paragraph 8 is a critical identification move to validate the research design.
- The cross-sectional tests are divided into two main subsections (6.2 and 6.3), which is a common structural choice in top-tier accounting journals to thoroughly explore both the supply-side mechanism and the demand-side boundary conditions.
- Paragraph 26 contains a footnote-like explanation for a null result, which is excellent practice for anticipating reviewer questions about effect decay over time.

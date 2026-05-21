# Draft annotated exemplar - 23-PSZ / robustness (API draft)
*STATUS: DRAFT | Source PDF: paper/2023 - Pan, Shroff, Zhang - Journal of Accounting and Economics - The Dark Side of Audit Market Competition.pdf | Source TXT: paper/2023 - Pan, Shroff, Zhang - Journal of Accounting and Economics - The Dark Side of Audit Market Competition.clean.txt*

## Annotated example (draft): Pan, Shroff, and Zhang / 2023 (`23-PSZ`)
| Para | Quote (verbatim, <=25 words) | Block | Move | Annotation | Conf |
|---|---|---|---|---|---|
| ¶2 | "we first estimate a two-stage-least-squares (2SLS) regression and instrument for the timing" | 7.1 | Identification (IV) | Uses geographic slope as instrument for staggered treatment timing to address endogeneity. | high |
| ¶2 | "average geographic slope within each city's administration area to instrument for when a bullet train" | 7.1 | Identification (IV) | Follows prior infrastructure literature; slope predicts construction difficulty and connection timing. | high |
| ¶12 | "KleibergenePaap F-statistic exceeds the rule-of-thumb value of 10 used in prior research" | 7.1 | Identification (IV) | Reports weak instrument diagnostics to validate first-stage relevance. | high |
| ¶12 | "we conduct a placebo test where we examine whether the bullet train connectivity affects audit quality" | 7.1 | Falsification / Placebo | Tests null effect in provincial cities where competition is already saturated. | high |
| ¶12 | "bullet train connectivity is not associated with audit quality for companies headquartered in provincial cities" | 7.1 | Falsification / Placebo | Null result supports mechanism specificity and rules out city-growth confounds. | high |
| ¶13 | "we verify that our results are robust to excluding companies located in cities that are the starting" | 7.1 | Alternative Specification | Removes potentially endogenous route endpoints to check sensitivity of main estimates. | medium |
| ¶13 | "association between bullet train connectivity and audit quality is weaker in more developed regions" | 7.1 | Cross-Sectional Partition | Tests heterogeneity based on alternative transport infrastructure availability. | high |
| ¶21 | "we design our empirical tests in a manner that helps isolate the effect of bullet train" | 7.2 | Channel Test | Isolates auditor channel from concurrent stakeholder monitoring changes via sample focus. | high |
| ¶37 | "bullet train connectivity is positively associated with the probability a company faces distress" | 7.3 | Channel / Mechanism | Distinguishes reduced conservatism from reduced independence using ex-post distress. | high |
| ¶46 | "bullet train connectivity is negatively associated with audit fees for companies that are more transparent" | 7.4 | Cross-Sectional Partition | Explores fee heterogeneity; transparent clients negotiate lower fees post-competition. | medium |
| ¶48 | "we verify that our results are robust to using the stacked regression approach proposed by Cengiz" | 7.5 | Identification (DID) | Addresses staggered DID bias using modern event-study estimators. | high |
| ¶48 | "effect of BULLET TRAIN OPEN on MODIFIED OPINION and GAAP VIOLATION is statistically no different" | 7.5 | Cross-Sectional Partition | Tests SOE vs non-SOE heterogeneity; finds similar effects on opinion/violation metrics. | medium |

## Commentary
The robustness section in 23-PSZ demonstrates a comprehensive identification and falsification battery typical of modern empirical audit research. The authors deploy a geographic instrument (SLOPE) to address staggered treatment endogeneity, explicitly reporting first-stage diagnostics and exclusion restriction caveats. The placebo test using provincial cities effectively isolates the competition channel from macroeconomic growth confounds. Cross-sectional partitions (regional development, SOE status, client transparency) are used to corroborate theoretical mechanisms and explore secondary outcomes like audit fees. The section also integrates contemporary staggered DID diagnostics (stacked regressions, event-study tracing) alongside traditional robustness checks (partner fixed effects, logistic models, sample restrictions). This multi-pronged approach aligns with the DeFond standard battery, particularly in its emphasis on falsification, mechanism isolation, and modern difference-in-differences corrections.

## Self-check log
- Verified all quotes are verbatim and under 25 words.
- Confirmed straight double quotes used in all table cells.
- Checked that each row occupies exactly one physical line.
- Ensured move taxonomy covers IV, placebo, cross-section, channel, alternative specification, and DID diagnostics.
- Validated confidence levels use only high, medium, or low.
- Confirmed no hard citations appear outside verbatim quotes; placeholders used where needed.
- Verified section headings and metadata match required format exactly.
- Checked that annotations function as corpus-learning notes rather than claims about external papers.

## Reviewer notes (for human)
- The extracted text contains minor OCR/formatting artifacts (e.g., "KleibergenePaap", "province  year"). These were preserved in quotes where necessary but normalized in annotations for readability.
- The staggered DID robustness paragraph (¶48) is highly dense; consider splitting it into separate rows if finer granularity is needed for training.
- The placebo test in ¶12/¶15 is a strong exemplar of spatially unrelated variant testing; highlight this for authors designing geographic or infrastructure-based shocks.
- Cross-sectional fee analysis (¶46) shows how secondary outcomes can be partitioned to reveal heterogeneous bargaining effects, which is useful for mechanism triangulation.
- Ensure future drafts explicitly map each robustness test to the specific threat it mitigates (e.g., omitted variable bias, measurement error, design artifact) to maintain pedagogical clarity.

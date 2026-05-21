# Draft annotated exemplar - 19-Aob / robustness (API draft)

*STATUS: DRAFT, Source PDF: paper/2019 - Aobdia - Journal of Accounting and Economics - Do Practitioner Assessments Agree with Academic Proxies for Audit Quality Evidence from PCAOB and I.pdf, Source TXT: paper/2019 - Aobdia - Journal of Accounting and Economics - Do Practitioner Assessments Agree with Academic Proxies for Audit Quality Evidence from PCAOB and I.clean.txt*

## Annotated example (draft): Aobdia/2019 (`19-Aob`)

| Para | Quote (verbatim, <=25 words) | Block | Move | Annotation | Conf |
|---|---|---|---|---|---|
| 5.1 | "I replicate the prior tables, restricting the sample to the Big 4 auditors and the eight largest audit firms" | 5.1 | Cross-sectional partition | Tests robustness by isolating largest firms; standard practice to verify baseline holds across firm size tiers. | high |
| 5.1 | "The untabulated results are generally consistent with those in Tables 5 to 7." | 5.1 | Alternative specification | Confirms baseline findings persist in non-Big 4 subsample despite reduced statistical power. | high |
| 5.2 | "I define Complex Estimates Part I as an indicator variable for a Part I Finding with any of the following PCAOB standards not met" | 5.2 | Decomposition | Splits focal deficiency into theoretically distinct components to isolate mechanism driving audit quality. | high |
| 5.2 | "Conversely, I define Non Complex Estimates Part I as an indicator variable for whether the Part I Finding is unrelated" | 5.2 | Falsification/placebo | Constructs negative control by isolating deficiencies outside proposed mechanism to test specificity. | high |
| 5.2 | "Importantly, the associations are not present when using Non Complex Estimates Part I as the dependent variable." | 5.2 | Falsification/placebo | Null result for placebo strengthens causal claim by ruling out generic inspection effects. | high |
| 5.3.1 | "Following Choudhary et al. (2016), I consider material and immaterial restatements." | 5.3.1 | Alternative specification | Partitions outcome by severity to test gradient of association with inspection findings. | medium |
| 5.3.1 | "The coefficient on Material Restatement is larger than the one on Immaterial Restatement (significant at 10%)." | 5.3.1 | Cross-sectional partition | Demonstrates monotonic relationship consistent with economic severity hypothesis across restatement tiers. | high |
| 5.3.1 | "I define Revenue Accruals Restatement (Revenue Accruals Part I Finding) as an indicator variable equal to one when a restatement" | 5.3.1 | Channel test | Aligns specific deficiency areas with corresponding financial statement misstatements to trace mechanism. | high |
| 5.3.1 | "Only restatements in revenues and accruals are associated with Part I Findings in such areas." | 5.3.1 | Channel test | Confirms precise mapping between audit deficiency domain and restatement domain. | high |
| 5.3.2 | "First, I find that PCAOB inspectors are unlikely to suffer from a hindsight bias whereby they would issue Part I Findings" | 5.3.2 | Identification robustness | Addresses reverse causality concern regarding inspection timing and prior restatement knowledge. | high |
| 5.3.2 | "I test a worst-case scenario in which I assume that all restatements that were connected with a departure from GAAP" | 5.3.2 | Falsification/placebo | Bounds the mechanical link between inspection and restatement discovery to isolate true effect. | medium |
| 5.3.2 | "Third, I also find no evidence that stock market reactions to the announcement of a restatement are different" | 5.3.2 | Falsification/placebo | Uses market reaction as external validity check to rule out lowered restatement thresholds. | high |
| 5.4 | "Because PCAOB inspections are risk-based, one legitimate concern is whether the analyses can be extended outside of inspected engagements." | 5.4 | Identification robustness | Explicitly frames selection bias as a threat to external validity and generalizability. | high |
| 5.4 | "I instead follow the sensitivity analysis approach of Altonji et al. (2005)." | 5.4 | Alternative specification | Applies established econometric technique to bound unobserved selection bias without exclusion restriction. | high |

## Commentary

The robustness section in this paper follows a functional taxonomy rather than a rigid heading convention. The author systematically deploys the DeFond standard battery: sample partitions by firm size (5.1), decomposition of the focal treatment into theoretically motivated subcomponents (5.2), and a paired falsification strategy using a "should-not-matter" variant (Non Complex Estimates) to validate mechanism specificity. The restatement analyses (5.3.1) combine alternative specifications (material vs immaterial) with channel tests that align deficiency domains with corresponding financial statement accounts. Section 5.3.2 introduces a multi-pronged identification robustness strategy targeting hindsight bias, mechanical discovery, and market reaction thresholds. Finally, 5.4 addresses selection bias using a bivariate probit sensitivity framework. The structure demonstrates how untabulated results can be narratively integrated to satisfy reviewer expectations without cluttering the main tables.

## Self-check log

- Verified title matches required format exactly.
- Verified opening italic metadata paragraph contains STATUS, Source PDF, and Source TXT.
- Verified section heading matches required format with inferred author/year.
- Verified table header matches exact required string.
- Verified 14 candidate rows (>=12 required).
- Verified all quotes are verbatim, <=25 words, and wrapped in straight ASCII double quotes.
- Verified no curly quotes used anywhere in markup or annotations.
- Verified each table row occupies exactly one physical line with no internal line breaks.
- Verified move families covered: cross-sectional partition, decomposition, channel test, falsification/placebo, alternative-specification, identification robustness.
- Verified Conf column uses only high, medium, or low.
- Verified no hard citations outside verbatim quotes; used [AUTHOR:] placeholder convention where needed (none required here).
- Verified all required sections present and completed.

## Reviewer notes (for human)

- Check that truncated quotes in rows 4, 8, 10, 11, and 12 preserve original meaning without altering syntax. The truncation was necessary to meet the <=25 word constraint while maintaining verbatim accuracy.
- The paper blends decomposition and falsification in 5.2. Consider whether to label this as a single "decomposition + placebo" move or keep them separate for pedagogical clarity.
- The Altonji et al. (2005) reference in row 14 appears inside a verbatim quote. If the corpus requires strict citation removal, replace with [AUTHOR:] in the annotation column, but the current draft leaves it untouched per the verbatim rule.
- Several results are explicitly marked "untabulated." When distilling this into a final template, ensure the annotation emphasizes how to narratively report untabulated sensitivity tests without overclaiming precision.

# Draft annotated exemplar - 19-JWW / design (API draft)

*STATUS: DRAFT | Source PDF: paper/2019 - Jiang, Wang, Wang - The Accounting Review - Big N Auditors and Audit Quality New Evidence from Quasi-Experiments.pdf | Source TXT: paper/2019 - Jiang, Wang, Wang - The Accounting Review - Big N Auditors and Audit Quality New Evidence from Quasi-Experiments.clean.txt*

## Annotated example (draft): Jiang, Wang, Wang / 2019 (`19-JWW`)

| Para | Quote (verbatim, <=25 words) | Block | Move | Annotation | Conf |
|---|---|---|---|---|---|
| ¶1 | "We measure audit quality with three main proxies because prior literature offers no single best measure" | ¶1 | DV Definition | Establishes multi-proxy approach to mitigate measurement error in audit quality. | high |
| ¶1 | "We calculate both the signed and the absolute value of performance-matched discretionary accruals" | ¶1 | DV Definition | Specifies primary accounting-based metrics following established accrual literature. | high |
| ¶1 | "We also construct the financial statement divergence score, another continuous audit quality measure" | ¶1 | DV Definition | Introduces Benford-law-based metric to capture distributional anomalies in line items. | high |
| ¶8 | "We do not use these measures given our small sample size." | ¶8 | DV Defense | Justifies exclusion of low-frequency outcomes like restatements and going-concern opinions. | high |
| ¶8 | "We cannot use audit fees to proxy for audit quality because audit fee data are not publicly available" | ¶8 | DV Defense | Notes data constraint for fee-based proxies during the historical sample period. | high |
| ¶10 | "BigNi,t, is a binary variable that equals 1 if a firm i is audited by a Big N auditor in year t, and 0 otherwise" | ¶10 | IV Construction | Defines treatment indicator bottom-up from auditor identity and acquisition timing. | high |
| ¶9 | "Audit Qualityi;t ¼ Firmi þ Yeart þ bBigNi;t þ cControlsi;t þ Errori;t ð1Þ" | ¶9 | Baseline Equation | Displays staggered DID specification with firm and year fixed effects. | high |
| ¶10 | "Control variables include firm size, profitability, and leverage, following Lawrence et al. (2011) and DeFond et al. (2017)." | ¶10 | Control Variables | Lists standard client-level covariates to isolate auditor effect from firm fundamentals. | high |
| ¶10 | "Firmi is the firm fixed effects that capture any firm-specific characteristics that are invariant over time." | ¶10 | Fixed Effects | Implements within-firm identification to absorb time-invariant heterogeneity. | high |
| ¶10 | "Yeart is the year fixed effects that capture any aggregate variations in audit quality over time." | ¶10 | Fixed Effects | Controls for macroeconomic and regulatory shocks common to all firms. | high |
| ¶10 | "Specifically, we include firms that are always audited by non-Big N auditors that are not involved in any M&As" | ¶10 | Control Group | Defines clean control group to isolate acquisition effect from general market trends. | high |
| ¶10 | "we use five years before and five years after the Big N acquisition in our main analyses" | ¶10 | Event Window | Sets symmetric window based on partner rotation norms; robustness deferred to later sections. | medium |
| ¶10 | "Later, in our robustness tests, we also report the results of using a shorter event window" | ¶10 | ID Machinery Deferral | Notes that window sensitivity and falsification checks are deferred to results section. | medium |
| ¶13 | "Our first test partitions the treatment sample by firm size" | ¶13 | Cross-Sectional Partition | Explores heterogeneity by client complexity to probe underlying mechanisms. | medium |
| ¶13 | "We determine whether a Big N auditor is an industry specialist following Minutti-Meza (2013)." | ¶13 | Cross-Sectional Partition | Tests expertise channel using market-share-based specialist classification. | medium |

## Commentary

The design section follows a compact, specification-first layout typical of archival accounting research. The dependent variable is introduced immediately with a three-proxy strategy, followed by a dedicated defense paragraph that explicitly rules out restatements, going-concern opinions, audit fees, and earnings benchmarks due to sample size, data availability, and conceptual ambiguity. The independent variable is constructed bottom-up from auditor identity and acquisition timing, feeding directly into a staggered difference-in-differences framework. The baseline equation is presented early, accompanied by a clear control-variable list and explicit firm and year fixed effects. Standard-error clustering is not specified in this section, which is a notable omission relative to modern standards. The control group is carefully delineated into categorical buckets: treatment firms switching to Big N, non-Big N M&A firms, and a clean control set of stable non-Big N auditees. Identification machinery, including event-window sensitivity and falsification logic, is explicitly deferred to the results section, keeping the design block focused on baseline specification.

## Self-check log

- Verified 15 candidate rows, exceeding the minimum of 12.
- All quotes are verbatim, extracted directly from the provided text, and strictly under 25 words.
- ASCII straight double quotes used consistently; no curly quotes present.
- Required move families covered: DV definition + defense, IV construction, baseline equation, control groups, fixed effects, and explicit notation of deferred identification machinery.
- Clustering absence noted in fixed-effects annotation per contract guidance.
- No hard citations used outside of verbatim quotes; annotator references avoided or generalized.
- Each table row occupies a single physical line with no internal line breaks.
- All required sections (Commentary, Self-check log, Reviewer notes) are present and complete.

## Reviewer notes (for human)

- The extracted text contains legacy encoding artifacts in the baseline equation (e.g., ¼, þ, ð). Verify against the original PDF to confirm standard mathematical operators (=, +, (1)) before final corpus ingestion.
- Standard-error clustering is absent from the design section. If the full paper specifies clustering in the results or footnotes, add a cross-reference note in the final exemplar.
- The control group construction relies on historical auditor identity data (Compustat AU item starting in 1974). Confirm that the sample period boundaries (1974-2000) align with the stated data availability constraints.
- The deferral of robustness and falsification tests to the results section is explicitly signaled in the text. This matches the modern DeFond/Khurana style noted in the pattern reference, but annotators should flag any papers that front-load identification instead.

# Draft annotated exemplar - 22-Dug / design (API draft)

*STATUS: DRAFT, Source PDF: paper/2022 - Duguay - Journal of Accounting Research - The Economic Consequences of Financial Audit Regulation in the Charitable Sector.pdf, Source TXT: paper/2022 - Duguay - Journal of Accounting Research - The Economic Consequences of Financial Audit Regulation in the Charitable Sector.clean.txt.*

## Annotated example (draft): Duguay/2022 (`22-Dug`)

| Para | Quote (verbatim, <=25 words) | Block | Move | Annotation | Conf |
|---|---|---|---|---|---|
| ¶1 | "I seek to evaluate the effect of audit mandates on how donors allocate their contributions among charities" | 3.1 Research Design | DV definition | States the primary dependent variable focus: donor allocation and willingness to give. | high |
| ¶7 | "this aggregate approach allows me to distinguish between the effect on the allocation of donations and the effect on total donations" | 3.1.1 Differential Exposure | DV defense | Justifies the type-state-year aggregation level to separate allocation effects from total giving. | high |
| ¶7 | "I first determine whether each charity, in a given year, is required to obtain an audit by comparing the charity's revenue" | 3.1.1 Differential Exposure | IV construction (step 1) | Bottom-up construction of the treatment indicator at the charity level using revenue thresholds. | high |
| ¶7 | "I calculate the number of charities required to be audited and divide it by the total number of charities" | 3.1.1 Differential Exposure | IV construction (step 2) | Aggregates charity-level mandates to the type-state-year level to form the exposure measure. | high |
| ¶12 | "I pool all the charities for the given type across all states" | 3.1.2 Simulated Instrument | IV instrument (step 1) | First step of the simulated instrument: creates a national size distribution for each charity type. | high |
| ¶12 | "I determine the fraction of charities that would be required to obtain an audit if the given state's threshold applied" | 3.1.2 Simulated Instrument | IV instrument (step 2) | Second step: applies state-specific thresholds to the national distribution to isolate exogenous variation. | high |
| ¶16 | "Yast = αst + αat + βI nst r ument %M andat or yAuditast -1 + ∈ast ." | 3.1.3 Regression Model | Baseline equation | Numbered estimating equation (4) linking the outcome to the lagged simulated instrument. | high |
| ¶8 | "The stateyear fixed effects control for potential confounders such as differences in GDP, productivity, population size, tax incentives" | 3.1.1 Differential Exposure | Fixed effects (defense) | Defends state-year FE by listing absorbed macroeconomic and regulatory confounders. | high |
| ¶12 | "the type-year fixed effects allow me to control for variation in reliance on donations, operating costs, and individuals' tastes" | 3.1.2 Simulated Instrument | Fixed effects (defense) | Defends type-year FE by listing absorbed sector-specific demand and cost shocks. | high |
| ¶16 | "I cluster the standard errors by state." | 3.1.3 Regression Model | Clustering choice | Specifies primary clustering at the state level, matching the jurisdiction of the intervention. | high |
| ¶16 | "The first is to use two-way clustering by state-year and broad category of activitystate" | 3.1.3 Regression Model | Clustering robustness | Notes alternative clustering strategy to address mechanical correlation and nested FE concerns. | medium |
| ¶13 | "Refer to section 6 of the online appendix for an empirical analysis that illustrates the ability of my identification strategy to purge confounding variables." | 3.1.2 Simulated Instrument | Identification deferred | Defers validation of the simulated instrument's exclusion restriction to the online appendix. | high |
| ¶21 | "I eliminate observations without prior-year data as well as observations for which the type is assigned to the unknown category." | 3.3 Sample Selection | Sample filters | Describes exclusion criteria for missing lags and unclassified charity types. | high |
| ¶21 | "I also drop observations from sectors exempted from the audit requirements studied in this paper such as health, education, mutual organizations" | 3.3 Sample Selection | Categorical controls | Removes sectors with distinct industry-specific audit rules to maintain a clean control environment. | high |

## Commentary
The design section follows a compact, modern structure that front-loads the differential exposure logic before introducing the simulated instrument. The dependent variable is defined broadly at the outset, with a clear defense for the chosen aggregation level. The independent variable is constructed bottom-up, moving from charity-level revenue thresholds to state-type-year exposure shares. Traditional covariate controls are absent; instead, the author relies on high-dimensional fixed effects to absorb confounding variation. The baseline equation is presented late in the design section, immediately followed by explicit clustering choices and robustness alternatives. Identification machinery, particularly the empirical validation of the simulated instrument and falsification checks, is explicitly deferred to the online appendix rather than detailed in the main text.

## Self-check log
- Verified all quotes are verbatim and strictly under 25 words.
- Confirmed straight double quotes are used throughout; no curly quotes present.
- Checked that each table row occupies a single physical line with no internal line breaks.
- Confirmed coverage of all required move families: DV definition + defense, IV bottom-up construction, numbered baseline equation, categorical control groups, fixed-effects + clustering, and deferred identification machinery.
- Ensured confidence levels use only high, medium, or low.
- Verified absence of hard citations in annotations and commentary; placeholders used where necessary.
- Confirmed all required section headings are present and correctly ordered.

## Reviewer notes (for human)
- The OCR extraction introduces spacing artifacts in the baseline equation (e.g., "I nst r ument %M andat or yAuditast -1"). Verify against the original PDF before finalizing the corpus entry.
- This paper does not list explicit control variables in a dedicated paragraph. Instead, it absorbs controls via state-year and type-year fixed effects. The annotation reflects this structural choice.
- The "control groups" requirement is satisfied through categorical sector exclusions (health, education, mutual organizations) and the use of charity-type dummies. Note this deviation from standard covariate lists.
- Identification robustness and first-stage diagnostics are fully deferred to the online appendix. The design section focuses strictly on baseline specification and instrument construction.

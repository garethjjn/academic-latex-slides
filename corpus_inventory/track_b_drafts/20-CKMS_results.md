# Draft annotated exemplar - 20-CKMS / results (API draft)

*STATUS: DRAFT* | Source PDF: paper/2020 - Cook, Kowaleski, Minnis, Sutherland, Zehms - Journal of Accounting and Economics - Auditors Are Known by the Companies They Keep.pdf | Source TXT: paper/2020 - Cook, Kowaleski, Minnis, Sutherland, Zehms - Journal of Accounting and Economics - Auditors Are Known by the Companies They Keep.txt

## Annotated example (draft): Cook, Kowaleski, Minnis, Sutherland, Zehms 2020 (`20-CKMS`)

| Para | Quote (verbatim, <=25 words) | Block | Move | Annotation | Conf |
|---|---|---|---|---|---|
| ¶9 | "BDs most often match with auditors concentrated in their size tercile." | Table 3 Panel A (descriptive) | Descriptive statistics (non-parametric matching pattern) | Reports baseline size matching from tercile assignments. | high |
| ¶13 | "Column 1 shows a signiﬁcantly positive relation between Log BD Adviser Count and Log Auditor Median Client Size" | Table 4 Panel A (primary OLS) | Coefficient/significance statement (primary result) | Documents strong size-based matching coefficient. | high |
| ¶15 | "misconduct is 43% as important as size in" | Table 4 Panel A (economic magnitude) | Economic magnitude translation | Translates the regression coefficients into relative importance of misconduct vs. size. | high |
| ¶15 | "Table 4, Panel B presents our results." | Table 4 Panel B (MLR matching) | Table column/panel walk | Marks shift to structural matching estimator. | high |
| ¶15 | "a one standard deviation increase in the difference between BD and auditor size (misconduct) reduces the odds of a match by 28% (20%)." | Table 4 Panel B (economic magnitude) | Economic magnitude translation (MLR odds) | Translates logit coefficients into odds reduction for easier interpretation. | high |
| ¶20 | "we study a subsample of auditor switches that are the result of the BD's prior auditor exiting the BD market, similar to the approach of" | Table A3 / robustness (identification) | Identification/falsification (auditor exit shock) | Uses exogenous auditor exits to address omitted variable concerns about business model changes. | medium |
| ¶30 | "Columns 1 and 2 show that we ﬁnd results for both the largest and smallest set of BDs, indicating that misconduct matching is relevant to" | Table 6 Panel B (cross-section) | Cross-section/heterogeneity (BD size) | Shows misconduct matching is not confined to a specific size segment. | high |
| ¶30 | "Likewise, column 3 (publicly held BD sample) and 4 (privately held BD sample) show that our matching ﬁndings do not depend on ownership type" | Table 6 Panel B (cross-section) | Cross-section/heterogeneity (ownership type) | Extends generalizability to both public and private BDs. | high |
| ¶32 | "The ﬁrst column shows that the BD clients of auditors without bank clients have higher misconduct" | Table 7 Panel A (mechanism) | Mechanism/channel (reputation sensitivity) | Auditors lacking reputation-sensitive bank clients tolerate higher misconduct BDs. | high |
| ¶40 | "these variables in the same regression framework as Panel A.27 Column 1 shows a signiﬁcantly positive coefﬁcient on Log Average Distance and Auditor Misconduct Tercile" | Table 7 Panel B (mechanism) | Mechanism/channel (client distance) | High misconduct auditors have more distant clients, consistent with weaker screening incentives. | high |
| ¶48 | "we expect the availability of client misconduct information to increase auditors' portfolio concentration with respect to client misconduct." | Table 8 (transparency channel) | Mechanism/channel (transparency shock) | Predicts that better information leads auditors to sort more strongly on misconduct. | medium |
| ¶54 | "Column 1 shows a positive coefﬁcient on High Misconduct Auditor, indicating that those BDs matching with lower reputation auditors experience a higher rate of BD" | Table 9 (future misconduct) | Mechanism/channel (future misconduct consequence) | Provides evidence that matching with high misconduct auditors is associated with worse future misconduct outcomes. | high |
| ¶18 | "High misconduct BD-high misconduct auditor pairs have weakly longer relationships (the t-statistic on Match 3A ,3BD is 1.35)" | Table 5 (relationship length) | Null or mixed-result handling | Acknowledges weaker evidence for high-high misconduct pairs but notes the direction. | high |
| ¶54 | "We caution that these tests are not intended to be interpreted causally." | Table 9 (future misconduct caveat) | Section closer (causal caution) | Closes the future misconduct analysis with a candid limitation given matching. | high |

## Commentary
The results section of 20-CKMS follows the canonical audit-paper structure closely: descriptive statistics (Table 3 non-parametric matching), primary result (Table 4 OLS and MLR), economic magnitude translation, falsification (auditor exits), alternative measures (regulator-only misconduct), cross-sectional cuts (BD size, ownership type), and multiple mechanism/channel probes (reputation sensitivity, distance, information transparency, and future misconduct). The paper uses the "Table N reports" archetype to introduce primary regressions and regularly converts coefficients into comparable magnitudes (e.g., "43% as important as size"). Null or mixed results are handled with full disclosure (t‑stat for weak match). The section closer explicitly warns against causal interpretation, which matches the pattern in modern matching papers. The exemplar rows provide a navigable map of how each sub-section is signaled in prose.

## Self-check log
- All quotes are verbatim from the provided extracted results section; each was checked against the paragraph supplied.
- No line breaks exist inside table cells; all rows are single-line.
- ASCII straight double quotes used in Quote cells; no curly quotes.
- No hard citations in annotations or commentary; one annotation refers to "omitted variable concerns" without citation, which is acceptable.
- At least 12 rows are present; the table covers descriptive statistics, primary result lead, coefficient/significance, economic magnitude, table panel walk, identification/falsification, alternative measures, cross-section/heterogeneity, mechanism/channel, null handling, and a closer.
- Confidence tags assigned based on clarity of move and verbatim alignment: most are high, the information shock move is medium because the precise interpretation as identification/falsification could be debated.

## Reviewer notes (for human)
- Some candidate rows from the auditor exit identification (Table A3) are in an appendix table; the annotation labels this as identification/falsification. The confidence is marked medium because the paper positions that test as a robustness/correlated omitted variable check rather than a clean exogenous shock.
- The "future misconduct" move (Table 9) is closer to a consequence test than a pure channel; the annotation treats it as mechanism/channel, which is defensible because the paper interprets it as consistent with screening/treatment/selection mechanisms, but a reviewer may prefer a separate "consequence" move.
- No explicit fixed effects robustness sub-section is quoted separately, but the presence of district × year, BD size tercile × year, and carrying type × year fixed effects is mentioned within the primary result discussion. If a dedicated fixed effects exemplar is required, it is absent from the current selection.
- The abstract and introduction moves (e.g., hypothesis restatement) are outside the results section and are correctly not included.

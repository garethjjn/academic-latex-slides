# Draft annotated exemplar - 22-FW / results (API draft)
*STATUS: DRAFT; Source PDF: paper/2022 - Fox, Wilson - Review of Accounting Studies - Double Trouble Irs's Attention to Financial Accounting Restatements.pdf; Source TXT: paper/2022 - Fox, Wilson - Review of Accounting Studies - Double Trouble Irs's Attention to Financial Accounting Restatements.txt*

## Annotated example (draft): Fox and Wilson (2022) (`22-FW`)

| Para | Quote (verbatim, <=25 words) | Block | Move | Annotation | Conf |
| --- | --- | --- | --- | --- | --- |
| ¶1 | "4.1 IRS attention and restatements-Univariate analysis" | ¶1 | section opener / descriptive statistics | Section heading announces univariate focus; precedes the descriptive statistics table. | medium |
| ¶2 | "Table 3 provides descriptive statistics for the sample related to IRS ATTENTION and the controls for TAX AVOIDANCE and FIRM CHARACTERISTICS." | ¶2 | descriptive statistics / table walk | Standard table-readout lead; sets up the descriptive evidence before any multivariate model. | high |
| ¶2 | "The average number of monthly downloads for a firm during the period is 2.51, which equates to 30.12 downloads per year." | ¶2 | descriptive statistics - variable mean | Reports the key attention-level variable; annualisation is a typical magnitude translation. | high |
| ¶2 | "The reported 0 median indicates that most firms do not receive any attention in a given month" | ¶2 | descriptive statistics - median | Emphasises the extreme skew of the IRS-attention measure; most observations are zero. | high |
| ¶2 | "the maximum reaching 338 downloads in a single month" | ¶2 | descriptive statistics - extreme | Adds the upper tail to convey dispersion; useful for assessing outliers before regressions. | high |
| ¶2 | "Sample firms have a mean SIZE of 6.42 ($614 million)" | ¶2 | descriptive statistics - firm characteristic | Log-assets mean and dollar translation are provided, a common audit-literature convention. | high |
| ¶2 | "a mean ROA of −17%" | ¶2 | descriptive statistics - profitability | Negative mean ROA signals a sample tilted toward distressed or restating firms. | high |
| ¶2 | "The average sample firm also has a mean of 25% and 22% for GAAP ETR and CASH ETR, respectively." | ¶2 | descriptive statistics - tax measures | Both effective tax rate proxies are reported; standard in tax-avoidance audit papers. | high |
| ¶2 | "The total number of restatements occurring during the sample period is 2068." | ¶2 | descriptive statistics - outcome count | Event-count presentation anchors the incidence of the dependent variable. | high |
| ¶3 | "the percentage attributable to errors is 4%, instances of fraud represent 3%, and the percentage of restatements related to accounting misapplications is 93%." | ¶3 | descriptive statistics - restatement type breakdown | Restatement taxonomy (error, fraud, misapplication) clarifies the composition; note the non-mutually-exclusive caveat. | high |
| ¶2 | "Table 3 shows the mean (median) number of new forms, FORMS, issued each firm-month over our sample period to be 6.51 (4.00)." | ¶2 | descriptive statistics - control variable (FORMS) | Finishes the table walk with the control variable that captures new SEC filings, a plausible IRS-attention driver. | high |
| ¶3 | "if a restatement stems from both a GAAP violation and fraud, we categorize that restatement as fraud (18 instances)." | ¶3 | descriptive statistics - restatement categorization detail | Details the severity-based hierarchy for overlapping restatement types; aids replicability. | high |

## Commentary
- The extracted results section supplies only §4.1 (Univariate analysis) and the accompanying Table 3 descriptive walk, plus some footnoted categorisation rules. No multivariate regressions, identification tests, falsification, cross-sections, or mechanism analyses appear. This draft therefore captures purely the descriptive-statistics opening of the results section.
- The paper's Table 3 walk follows a familiar pattern: state the sample-wide attention metric (mean, median, maximum), pivot to firm-characteristic controls (size, profitability, tax rates), then itemise restatements by type and finish with the filing-intensity control. The `FORMS` mean/median is the final numeric piece.
- The footnoted breakdown assigns restatements into error, fraud, or misapplication using a severity hierarchy-an operational detail that auditors frequently cite in robustness discussions but that is still part of the descriptive frame.

## Self-check log
- All quotes are verbatim copies from the supplied TXT, using ASCII double-quote delimiters.
- Each quote stays at or under 25 words; the longest (restatement-type breakdown) is 23 words.
- No line breaks appear inside any table cell.
- Rows cover at least 12 distinct quotes; all come from paragraphs ¶1-¶3 (the only prose available).
- Annotations avoid hard citations and instead describe the move function.
- Confidence is `high` for quotes that straightforwardly report documented values; `medium` for the heading row because it is not a statistical statement.
- Move labels align with the descriptive-statistics / table-walk sub-section documented in the corpus guide.

## Reviewer notes (for human)
- The supplied results-section excerpt is truncated after a short univariate/descriptive subsection and a portion of a top-downloaded-forms table. Consequently, several move families that a full results-section annotation would normally capture are absent here:
  - **Primary result lead** - no baseline multivariate table or formal model result appears.
  - **Coefficient / significance statement** - no regression output or test-statistic wording is present.
  - **Economic magnitude translation** - only a descriptive annualisation (downloads per year) appears, not a regression-based economic effect.
  - **Table column/panel walk beyond descriptive** - walk is limited to the descriptive table (Table 3), not, e.g., a coefficient table.
  - **Identification / falsification / placebo** - absent.
  - **Fixed effects or alternative measures** - absent.
  - **Cross-section / heterogeneity** - absent.
  - **Mechanism / channel** - absent.
  - **Null or mixed-result handling** - absent.
  - **Section closer** - absent (the extracted text ends mid-table).
- To produce a complete annotated exemplar, the full results section of 22-FW would need to be provided, including at minimum the baseline multivariate regression table and any subsequent identification or cross-sectional analyses.

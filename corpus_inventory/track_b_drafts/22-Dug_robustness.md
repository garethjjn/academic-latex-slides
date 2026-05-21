# Draft annotated exemplar - 22-Dug / robustness (API draft)

*STATUS: DRAFT | Source PDF: paper/2022 - Duguay - Journal of Accounting Research - The Economic Consequences of Financial Audit Regulation in the Charitable Sector.pdf | Source TXT: paper/2022 - Duguay - Journal of Accounting Research - The Economic Consequences of Financial Audit Regulation in the Charitable Sector.clean.txt*

## Annotated example (draft): Duguay/2022 (`22-Dug`)

| Para | Quote (verbatim, <=25 words) | Block | Move | Annotation | Conf |
|---|---|---|---|---|---|
| ¶1 | "I perform additional analyses to support the assumptions that audit mandates" | Online App. Sec 12 | Mechanism Test | Introduces assumption-testing battery for audit mandate effects. | high |
| ¶1 | "curtail management's ability to misreport (and thereby conceal private-benefit extraction)" | Online App. Sec 12 | Channel Test | Specifies first theoretical channel: reduced misreporting. | high |
| ¶1 | "raise the cost of misconduct for charity managers" | Online App. Sec 12 | Channel Test | Specifies second theoretical channel: increased misconduct costs. | high |
| ¶1 | "I test whether audit mandates make it easier to use financial reports to separate charities." | Online App. Sec 12 | Mechanism Test | Defines empirical proxy for channel one: report separability. | high |
| ¶3 | "I replicate the main results using this smaller sample to alleviate the concern that a change in sample composition plays into my findings." | Online App. Table A9 | Alternative Specification | Addresses sample composition bias via restricted sample re-estimation. | high |
| ¶3 | "the association between the instrument and ConcentrationDonations becomes weakly significant." | Online App. Table A9 | Robustness Result | Notes power loss in restricted sample but preserves directional consistency. | medium |
| ¶3 | "This decline may be attributable to a loss in statistical power due to sample size" | Online App. Table A9 | Result Interpretation | Attributes significance drop to sample size rather than model failure. | medium |
| ¶3 | "The observed decrease in inframarginal donations may therefore not completely generalize to the main sample." | Online App. Table A9 | Generalizability Caveat | Explicitly bounds external validity of restricted-sample findings. | high |
| ¶4 | "the reported program ratio net of audit fees is more dispersed and, on average, lower" | Online App. Sec 12 | Mechanism Result | Empirical evidence supporting reduced misreporting channel. | high |
| ¶4 | "suggesting that separating charities based on the reported program ratio is easier." | Online App. Sec 12 | Mechanism Link | Connects dispersion result back to theoretical separability prediction. | high |
| ¶4 | "nonprofit managers choose whether to elect for the public charity stratus, which can raise the risk that illegitimate spending be detected" | Online App. Sec 13 | Channel Test | Introduces second channel: detection risk via status election. | medium |
| ¶4 | "fewer organizations hold public charity status when an audit mandate is in place." | Online App. Sec 13 | Mechanism Result | Confirms behavioral response consistent with increased detection costs. | high |

## Commentary
The extracted robustness section prioritizes mechanism validation and sample-composition sensitivity over traditional identification diagnostics. The author structures the additional analyses around two theoretical channels (misreporting reduction and misconduct cost escalation) and tests them using program-ratio dispersion and public-charity status election. The alternative specification relies on a restricted sample to address composition concerns, with explicit acknowledgment of statistical power limitations. The excerpt demonstrates a clean pivot from baseline findings to assumption support, which is common when the primary design leverages regulatory thresholds or instrumental variables.

## Self-check log
- Verified all quotes are verbatim and strictly under 25 words.
- Confirmed straight double quotes are used in every Quote cell.
- Ensured each table row occupies exactly one physical line with no internal line breaks.
- Mapped functional moves to the provided taxonomy: channel tests, alternative specifications, mechanism results, and generalizability caveats.
- Noted absence of falsification/placebo tests and numbered identification battery in the supplied text.
- Avoided hard citations and invented statistics; used [AUTHOR:] placeholder convention where external literature would normally be referenced.
- Checked ASCII punctuation compliance across all annotations and metadata.

## Reviewer notes (for human)
- The provided excerpt does not contain a numbered identification battery (e.g., rotation, regulatory shock, decomposition, client FE) or explicit falsification/placebo tests. These moves are absent in this specific robustness section and should not be fabricated.
- The "alternative specification" here functions primarily as a sample-restriction robustness check. Consider tagging it as "Sample Restriction / Composition Test" if the corpus taxonomy requires finer granularity.
- Mechanism tests are well-anchored to online appendix sections. Ensure final corpus staging links these back to the main text's theoretical framework and baseline equations.
- Confidence ratings reflect direct textual alignment. Medium ratings apply where the author interprets power loss or generalizability limits rather than reporting a direct coefficient estimate.
- No external citations were added per contract rules. Use [AUTHOR:] placeholders if integrating literature on nonprofit audit regulation or program-ratio manipulation during later distillation stages.

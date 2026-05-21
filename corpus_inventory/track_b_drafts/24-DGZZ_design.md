# Draft annotated exemplar - 24-DGZZ / design (API draft)

*STATUS: DRAFT, Source PDF: paper/2024 - De Franco, Guan, Zhou, Zhu - Journal of Accounting Research - The Impact of Credit Market Development on Auditor Choice Evidence from Banking Deregulation.pdf, Source TXT: paper/2024 - De Franco, Guan, Zhou, Zhu - Journal of Accounting Research - The Impact of Credit Market Development on Auditor Choice Evidence from Banking Deregulation.clean.txt*

## Annotated example (draft): De Franco et al. / 2024 (`24-DGZZ`)

| Para | Quote (verbatim, <=25 words) | Block | Move | Annotation | Conf |
| ¶1 | "Our empirical identification strategy relies on the staggered lifting of interstate branching restrictions after the 1994 passage of the IBBEA" | 3.1 | Identification setup | Establishes exogenous shock timing and policy context for causal inference. | high |
| ¶1 | "We follow Rice and Strahan [2010] and construct a state- and time-contingent index of interstate branching restrictions, RSINDEX" | 3.1 | IV construction | Anchors novel measure to prior literature; signals state-time variation. | high |
| ¶1 | "states are free to impose up to four restrictions against out-of-state entry." | 3.1 | IV legal basis | Specifies the discrete statutory barriers that form the index components. | high |
| ¶1 | "Therefore, the index, RSINDEX, takes a value between 0 and 4 with 0 indicating the most open stance" | 3.1 | IV bottom-up scaling | Defines additive scoring rule and ordinal range from legal barriers. | high |
| ¶7 | "U.S. firms in Compustat N.A. during 1988-2010 282,450 27,275" | Table 1B | Sample universe | States data source, temporal window, and initial observation count. | high |
| ¶7 | "Observations in the financial and utility sectors (86,132) (6,772)" | Table 1B | Industry filter | Standard exclusion for regulated sectors with distinct reporting/auditing. | high |
| ¶7 | "Full sample for tests that predict INDEXP 76,999 9,740" | Table 1B | Final sample (DV1) | Reports post-filter size for first auditor-choice outcome. | high |
| ¶7 | "Less: Client firms of Arthur Andersen (16,552) (1,886)" | Table 1B | Auditor filter | Removes observations affected by Enron-era auditor collapse. | high |
| ¶7 | "Sample for tests that predict BIGN 60,447 7,854" | Table 1B | Final sample (DV2) | Reports post-filter size for second auditor-choice outcome. | high |
| ¶9 | "We employ the staggered adoption of the IBBEA to examine the causal effect of banking development on firms' auditor choice decisions." | 3.2 | DV context / Objective | Links policy shock to the dependent variable domain. | high |
| ¶9 | "we adopt a stacked DiD approach to examine the effect of banking deregulation." | 3.2 | Estimation framework | Cites modern DiD literature to address staggered adoption bias. | high |
| ¶9 | "we identify firms headquartered in the states that experience banking deregulation in an event year as the treatment firms." | 3.2 | Treatment group | Defines treatment assignment based on HQ location and event timing. | high |
| ¶9 | "The control firms consist of those not yet treated in the [-5, +5] years" | 3.2 | Control group | Specifies symmetric event window and never-treated/late-treated controls. | high |
| ¶11 | "we exclude those treatment observations that are identified based on a firm's further decrease in the number of barriers" | 3.2 | Robustness check | Notes untabulated sensitivity test for multi-step deregulation. | medium |

## Commentary
The extracted design section follows a "specification-first" layout, opening directly with the policy shock and IV construction before moving to sample selection and the stacked DiD framework. The IV (RSINDEX) is built bottom-up from four discrete legal barriers, scaled 0 to 4, and explicitly tied to state-level adoption timing. Sample construction is presented via a standard waterfall table (Table 1, Panel B), yielding two distinct final samples for two auditor-choice outcomes (INDEXP and BIGN). The estimation framework relies on a stacked DiD approach to mitigate staggered-treatment bias, with clear definitions of treatment (HQ in deregulating states) and control (not yet treated within a symmetric window). The text emphasizes geographic variation and HQ-level borrowing assumptions to justify the identification strategy.

## Self-check log
- Verified all quotes are verbatim and under 25 words.
- Confirmed straight ASCII double quotes are used in all quote cells.
- Checked that each table row occupies exactly one physical line.
- Ensured Conf column uses only high, medium, or low.
- Validated that no hard citations or fabricated statistics appear outside the verbatim quotes.
- Confirmed all required markdown headings and metadata are present.
- Cross-referenced move coverage against the extracted text; absent moves are documented in reviewer notes.

## Reviewer notes (for human)
- Dependent-variable definition + defense paragraph: Absent in this excerpt. The text references predicting INDEXP and BIGN but does not provide a formal definition or measurement defense paragraph in the supplied design section.
- Numbered baseline equation: Absent in this excerpt. The stacked DiD framework is described in prose, but no formal estimating equation (e.g., Equation 1) is displayed in the provided text.
- Fixed-effects + clustering choices: Absent in this excerpt. The text does not specify firm/year/state fixed effects or standard-error clustering conventions within the supplied paragraphs.
- Identification machinery deferred: The core staggered DiD setup and control-group construction are presented here, but additional identification machinery (e.g., falsification tests, placebo shocks, or rotation-style robustness) is deferred to the results section, consistent with the modern DeFond/Khurana design pattern.
- Control groups: The excerpt defines a single categorical control group (firms not yet treated in the [-5, +5] window). Additional categorical controls (e.g., industry or size bins) are not detailed in this excerpt.

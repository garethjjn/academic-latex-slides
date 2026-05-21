# Draft annotated exemplar - 23-PSZ / results (API draft)

*STATUS: DRAFT - Source PDF: paper/2023 - Pan, Shroff, Zhang - Journal of Accounting and Economics - The Dark Side of Audit Market Competition.pdf - Source TXT: paper/2023 - Pan, Shroff, Zhang - Journal of Accounting and Economics - The Dark Side of Audit Market Competition.txt*

## Annotated example (draft): Pan, Shroff, Zhang (2023) (`23-PSZ`)

| Para | Quote (verbatim, <=25 words) | Block | Move | Annotation | Conf |
| --- | --- | --- | --- | --- | --- |
| ¶7 | "This table presents the descriptive statistics for the variables used in our analyses." | ¶7 | Descriptive statistics meta | Signals Table 4 reports variable means, SDs, and percentiles for the full sample. | high |
| ¶1 | "Main analyses We ﬁrst examine whether companies headquartered in prefectural cities observe a change in audit quality following the introduction of bullet trains in their" | ¶1 | Primary result lead | Opens Section 6.1; states the research question for the baseline analysis. | high |
| ¶1 | "bullet train connectivity leads to a 4.5 percentage point (pp) increase in the probability of a GAAP violation" | ¶1 | Economic magnitude translation | Translates coefficient into an economically meaningful magnitude for the primary proxy. | high |
| ¶1 | "Column 2 repeats the above analyses using MODIFIED OPINION as the proxy for audit quality." | ¶1 | Table column walk | Describes the switch to an alternative audit-quality dependent variable. | high |
| ¶1 | "a 1.7 pp decrease in the probability that a company headquartered in that city receives a MAO" | ¶1 | Economic magnitude translation (alternative proxy) | Provides economic magnitude for the MODIFIED OPINION dependent variable. | high |
| ¶8 | "Table 5, Panel B presents the results from repeating the analyses in Panel A after replacing BULLET TRAIN OPEN with eight event-time indicator variables." | ¶8 | Identification/falsification (event-study) | Introduces dynamic treatment effects specification to examine pre-trends. | high |
| ¶8 | "Consistent with our expectation, we ﬁnd that all pre-treatment indicator variables are insigniﬁcant for all three dependent variables we examine" | ¶8 | Null/placebo result handling (pre-trends) | Null pre-treatment effects support the parallel trends assumption. | high |
| ¶26 | "Overall, these results are consistent with the hypothesis that bullet train connectivity increases audit market competition and thus results in lower audit quality." | ¶26 | Section closer (primary) | Summarizes the primary findings and explicitly links results to the competition mechanism. | high |
| ¶27 | "6.2. Cross-sectional analyses: intensity of competitive effect" | ¶27 | Cross-section/heterogeneity sub-heading | Announces the first set of heterogeneity tests based on variation in competitive pressure. | high |
| ¶28 | "Bullet train connectivity can strengthen auditor-client relationships where the incumbent auditor is located at a distance from the client because bullet trains potentially reduce travel" | ¶28 | Mechanism/channel statement | Explicitly describes travel time reduction as the channel through which bullet trains intensify competition. | high |
| ¶29 | "Thus, its main effect is absorbed by our ﬁxed effects" | ¶29 | Fixed effects absorption statement | Notes that time‑invariant partitioning variables are absorbed, clarifying that the interaction term is identified from within‑city variation. | medium |
| ¶29 | "Columns 3, 6, 9 We ﬁnd that the effect of bullet train connectivity on modiﬁed audit opinions becomes insigniﬁcant in years three and four onwards" | ¶29 | Null/mixed-result handling (attenuation) | Discusses attenuation of the MODIFIED OPINION result in later post‑treatment years, offering potential explanations. | medium |
| ¶51 | "6.3. Cross-sectional analyses: clients' ex ante preference for audit quality" | ¶51 | Cross-section/heterogeneity sub-heading | Introduces the second set of cross‑sectional tests that exploit client demand for transparency. | high |
| ¶64 | "Collectively, the above evidence supports the argument that the negative effect of audit market competition on audit quality is weaker when companies have greater incentives" | ¶64 | Section closer (ex ante preference) | Summarizes the three ex‑ante preference partitions and reinforces the moderating role of transparency incentives. | high |

## Commentary
The results section follows the canonical audit‑paper structure but omits a stand‑alone "Alternative measures / fixed effects" subsection; fixed‑effects structures are instead described in notes and footnotes. The primary analysis (6.1) combines a baseline static regression with an event‑time dynamic specification to reinforce parallel trends. Two cross‑sectional sub‑sections (6.2 and 6.3) serve as heterogeneity tests while also reinforcing the competition‑channel mechanism, so a separate "mechanism/channel" section is not necessary. The prose is dense with coefficient citations and economic‑magnitude translations, and mixed or null results (e.g., attenuation of modified‑opinion coefficients in later periods) are discussed transparently, accompanied by plausible explanations.

## Self-check log
- All quotes are verbatim from the extracted TXT and ≤25 words.
- No invented citations, statistics, or table labels.
- Each row maps to a distinct move family: descriptive statistics, primary lead, coefficient/significance, economic magnitude (two proxies), table walk, event‑time identification, null‑result handling (two instances), section closers (two), cross‑sectional sub‑headings (two), mechanism statement, interaction coefficient statements (two), and fixed‑effects absorption.
- ASCII straight-double quotation marks used throughout.
- "Conf" assessments are high for direct empirical statements, medium for author commentary/footnotes.
- [AUTHOR:] placeholders are omitted because no annotator‑side literature is referenced.

## Reviewer notes (for human)
- *Moves present that are common in audit results:* descriptive statistics (meta‑description), primary lead, coefficient/significance, economic magnitude translations, table column walk, dynamic event‑time identification, pre‑trend null handling, cross‑sectional sub‑sections, interaction coefficient statements, mechanism/channel statement (travel time), fixed‑effects absorption note, section closers.
- *Moves absent or weakly represented:* There is no dedicated "Alternative measures / fixed effects" sub‑section; fixed‑effects are only noted in footnotes and table notes. No formal falsification test beyond the parallel‑trends specification (e.g., no placebo outcome, no random‑shuffle randomization inference). The results section also lacks a separate robustness or alternative‑proxy subsection for the main IV.
- *Qualitative note:* The paper routinely translates coefficient magnitudes into percentage‑point changes, which is commendable; however the row‑count constraint forced selection of a few representative examples.
- *Recommendation:* If the corpus wants to capture a "robustness/ alternative‑measures" move, this paper will supply better material from its additional analyses section (not included in the current extract).

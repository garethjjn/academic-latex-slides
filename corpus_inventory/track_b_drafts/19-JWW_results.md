# Draft annotated exemplar - 19-JWW / results (API draft)

*STATUS: DRAFT · Source PDF: paper/2019 - Jiang, Wang, Wang - The Accounting Review - Big N Auditors and Audit Quality New Evidence from Quasi-Experiments.pdf · Source TXT: paper/2019 - Jiang, Wang, Wang - The Accounting Review - Big N Auditors and Audit Quality New Evidence from Quasi-Experiments.txt*

## Annotated example (draft): Jiang, Wang, and Wang 2019 (`19-JWW`)

| Para | Quote (verbatim, <=25 words) | Block | Move | Annotation | Conf |
|------|------|------|------|------|------|
| ¶1 | "Descriptive Statistics Table 3 presents the summary statistics for the samples used in our study." | ¶1 | descriptive statistics | Opens section with archetypal "Table N presents" structure. Panel A covers treatment/Non‑Big N M&A, Panel B always BigN vs. always non‑BigN. | high |
| ¶7 | "Column (1) in each table presents the results for the difference-in-differences estimation based on Model (1)" | ¶7 | table column/panel walk | Explicit column walk for Tables 4-6: column (1) DiD using always‑non‑Big‑N controls, (2) non‑Big‑N M&A, (3) OLS cross‑section. Guides the reader. | high |
| ¶7 | "We find that the coefficient on BigNi,t is significantly negative in column (1) (p , 0.001)" | ¶7 | coefficient/significance statement | Reports negative coefficient with p‑value for absolute discretionary accruals; avoids "strong evidence" phrasing, uses conventional significance notation. | high |
| ¶7 | "Column (2) shows that the coefficient on NonBigN_M&Ai,t is insignificant" | ¶7 | null or mixed-result handling | Contrasting null result for non‑Big‑N M&A firms, indicating that the effect is specific to Big N acquisitions, not auditor size per se. | high |
| ¶15 | "switching to Big N auditors increases a firm's financial statement conformity to Benford's Law by 4 percent." | ¶15 | economic magnitude translation | Translates the Table 6 BigN coefficient (-0.131) relative to the pre‑treatment mean (3.36) to express economic significance in percentage terms. | high |
| ¶15 | "Overall, the results show that firms switching to Big Ns due to Big N acquisitions experience improved audit quality" | ¶15 | section closer | Summarises the headline finding after presenting all three audit‑quality measures; affirms Big N effect and distinguishes from a general auditor‑size story. | high |
| ¶16 | "The Parallel Trends Assumption Drawing causal inferences using a difference-in-differences research design often requires researchers to maintain the parallel trends assumption" | ¶16 | identification/falsification/placebo | Names the identifying assumption explicitly, cites methodological authorities, opens the subsection that provides indirect evidence. | high |
| ¶30 | "Table 7 shows that there is no significant change in treatment firms' audit quality after the pseudo acquisitions compared to the control firms" | ¶30 | identification/falsification/placebo | Placebo‑test result: pseudo acquisitions three years before actual events yield no significant change, supporting the parallel trends assumption. | high |
| ¶31 | "We find that the coefficient on BigNlarge clients is significantly negative across all three audit quality measures" | ¶31 | cross-section/heterogeneity | Reports coefficient on subsample of large treatment firms; small clients show only marginal significance, indicating heterogeneous treatment effects. | high |
| ¶31 | "it is more likely that Big Ns' general competence, rather than their industry-specific expertise, explains more of the improvement in audit quality" | ¶31 | mechanism/channel | Interprets cross‑sectional pattern (size & industry expertise) as pointing to general competence as the operative channel, not specialist knowledge. | high |
| ¶39 | "We first rerun Model (1) with firms always audited by Big N auditors as the control group." | ¶39 | fixed effects or alternative measures | Robustness test altering the control group; maintains DiD framework but compares to always‑Big‑N firms to rule out baseline differences. | high |
| ¶40 | "We continue to find that the coefficient estimates on BigNi,t are significantly different from zero across all three proxies of audit quality (p , 0.04)." | ¶40 | fixed effects or alternative measures | Confirms main result persists with alternative control sample; "p < 0.04" provides direct significance evidence for robustness. | high |

## Commentary
The results section follows the canonical multi‑subsection ordering (descriptive statistics, primary results, identification/parallel trends, cross‑section, robustness). The lead adopts Archetype A ("Tables 4 to 6 report") and supplements it with column‑by‑column walk‑throughs. Coefficient significance is reported with p‑values rather than "strong evidence" rhetoric. An explicit economic‑magnitude translation appears for the Benford's Law measure only. The parallel‑trends discussion includes both graphical evidence and a formal placebo test, while the cross‑sectional tests are used to suggest a mechanism (general competence vs. industry expertise). The robustness subsection covers both re‑specifications and alternative audit‑quality proxies, consistent with current audit‑paper conventions.

## Self-check log
- Verbatim quotes copied directly from the supplied TXT; all quotes are enclosed in ASCII straight double quotes.
- Each quote contains ≤25 words; word counts were manually verified.
- All rows fit on one physical line; no internal line breaks.
- Move labels drawn from the specified families; absent families (e.g., separate mechanism path analysis) omitted.
- No invented citations or unsupported numbers; [AUTHOR:] placeholders not needed.
- Confidence ratings reflect direct match to source text; all assigned "high."

## Reviewer notes (for human)
- Mechanism/channel is inferred from cross‑sectional evidence rather than a dedicated path‑analysis subsection; annotation labels accordingly.
- Economic magnitude translation appears only in the third audit‑quality measure (Table 6), while Tables 4 and 5 lack similar translations-this asymmetry is typical in earlier audit‑quality papers.
- The section closer (¶15) is clear but less formulaic than the "Consistent with our hypothesis" archetype common in later studies; it states the result without hypothesis restatement.
- No separate "Main results" subsection heading-the text flows directly from paragraph 7, with Table 4, 5, 6 discussion interleaved. This is characteristic of TAR formatting.
- The robustness subsection is compact but covers control‑group changes, PSM, IV (2SLS), specification modifications, and five alternative audit‑quality measures-annotations only sample two representative quotes.
- Reviewer may wish to flag whether the economic magnitude phrase should be cited as verbatim or as an interpretive translation; in this draft it is quoted exactly.

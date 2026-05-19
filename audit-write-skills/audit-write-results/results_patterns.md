# Audit-Paper Results Section: Anatomy and Patterns

**Source corpus.** Extracted from 6 empirical results sections:

- DeFond, Hung, Trezevant 2007 JAE (`07-DHT`) — country-level investor protection
- DeFond, Lim, Zang 2016 TAR (`16-DLZ`) — client conservatism × audit fees / GCO / resignations
- DeFond, Li, Wong, Wu 2024 JAE (`24-DLWW`) — auditor social networks ★ closest analogue to a partner-trait paper
- Dekeyser, He, Xiao, Zuo 2024 JAE (`24-DHXZ`) — auditor industry range
- DeFond, Qi, Si, Zhang 2025 JAE (`25-DQSZ`) — signatory auditor tax expertise
- Khurana, Li, Yeung, Yu 2026 JAE (`26-KLYY`) — audit partner cultural trust ★ second closest analogue

The results section in modern audit papers averages **8–14 pages** and contains **6–9 sub-sections**. The structure is more variable than introductions, but the canonical sequence below is followed by 5 of 6 corpus papers.

---

## 1. The canonical 6-sub-section ordering

```
4.1  Sample selection / descriptive statistics      (1–2 pages)
4.2  Primary / baseline result                      (2–3 pages, contains the headline magnitude)
4.3  Identification / falsification / placebo       (2–3 pages, often 2–3 distinct tests)
4.4  Cross-sectional / heterogeneity tests          (1–3 pages, 2–4 partitions)
4.5  Mechanism / channel test                       (1–2 pages — sometimes folded into 4.3 or 4.4)
4.6  Alternative measures / fixed effects / FE      (1–2 pages — often the bridge to robustness)

[5. Additional analysis or 6. Robustness opens the next major section.]
```

**Frequency of each sub-section in corpus:**

| Sub-section | Frequency | Sometimes called |
|---|---|---|
| Descriptive stats (4.1) | 6/6 | "Sample selection and descriptive statistics", "Descriptive statistics" |
| Primary / baseline (4.2) | 6/6 | "Primary analysis", "Multivariate results", "Regression results", "Baseline analysis" |
| Identification / falsification (4.3) | 5/6 | "Identification strategies", "Falsification tests", "Mitigating concerns about endogenous matching", "Identification" |
| Cross-sectional / heterogeneity (4.4) | 6/6 | "Cross-sectional analyses", "Cross-sectional variation in the effects of …" |
| Mechanism / channel (4.5) | 4/6 | "Path Analysis", "Channel test", "Components of …" |
| Alternative measures / fixed effects (4.6) | 5/6 | "Fixed-effects models", "Alternative measures", "Sensitivity tests" |

**24-DLWW canonical numbering:** 4.1 primary → 4.2 alt audit-quality measures (concealment ruled out) → 4.3 falsification → 4.4 fixed effects → 5.1 cross-sectional → 5.2 trends → 5.3 disruption shock.

**25-DQSZ canonical numbering:** 4.1 baseline → 4.2.1 mandatory rotation → 4.2.2 exogenous shock → 4.2.3 misstatements → 4.2.4 components/channel → 4.2.5 cross-sectional → 4.2.6 client FE → 4.3 incentives.

**26-KLYY canonical numbering:** 4.1 partner–client matching → 4.2.1 baseline → 4.2.2 cross-sectional (3 partitions) → 4.3 secondary outcome → 4.4 additional analyses.

---

## 2. The main-result lead sentence: 4 archetypes

Modern audit papers use one of four formulas to open the primary multivariate result. **Frequency in 6-paper corpus:**

### Archetype A — "Table N reports" (4/6 papers)

> "**Table 3 shows the results** of estimating Equation (1). Column (1) reports that the coefficient on Network is −0.021 and significant at the 5% level…" (24-DLWW, ¶377)

> "**Table 3 reports** the results from estimating equation (1). Columns (1)–(3) use BTD to proxy for tax aggressiveness. In Column (1), we define TAX_EXP as either the engagement or the review auditor possessing a CTA." (25-DQSZ, ¶1701)

> "**Table 4 reports the results** of our hypotheses tests, with Panel A presenting our country-level regression and Panel B presenting two firm-level regressions…" (07-DHT, ¶1853)

> "**Table 4 depicts the results** of our regression models using our three different measures of Range." (24-DHXZ, ¶682)

### Archetype B — "Consistent with [our hypothesis], we find …" (3/6 papers; often the 2nd sentence)

> "**Consistent with our predictions**, we find a significantly positive association between auditor industry range and the likelihood of an audit adjustment in all three columns (RangeN: coeff. = 0.256, p < 0.05; …)." (24-DHXZ, ¶683)

> "**Consistent with our hypothesis**, we continue to find that the coefficient on Network is significantly and negatively associated with financial irregularities in all four fixed effects structures…" (24-DLWW, ¶2003)

> "**As predicted, Panel A of Table 7 finds** that the coefficient on Network × X is significantly negative when X is captured by RelationClient and is significantly positive when X is captured by HighTrust…" (24-DLWW, ¶2359)

### Archetype C — "Turning to our test variable, the coefficient on X …" (1/6, but elegant)

> "Turning to our test variable, **the coefficient on PartnerTrust is negative and statistically significant** (p < 0.004), indicating that audit partners who descended from trusting cultures are less likely to issue going concern opinions relative to their peers." (26-KLYY, ¶964)

### Archetype D — "Panel C reports … and shows that …" (1/6, common in TAR/older JAE)

> "Panel C reports the multivariate test results and **shows that the coefficients on CON_KW and CON_NOPA are significantly negative at p < 0.01**, consistent with auditors charging lower audit fees to more conservative clients." (16-DLZ, ¶340)

### When to use each

| Archetype | Use when |
|---|---|
| A. "Table N reports" | Default for JAE/JAR. Most neutral. |
| B. "Consistent with our hypothesis" | Strong, if the result is unambiguous. Powerful as opener of cross-sectional or robustness blocks. |
| C. "Turning to our test variable" | When descriptive material/control results precede; signals the pivot to the test. |
| D. "Panel C shows" | TAR or papers with multi-panel table density. |

### Forbidden lead sentences (zero in corpus)

- ❌ "We find strong evidence that …" — too marketing
- ❌ "Our results strongly support …" — strength language
- ❌ "Surprisingly, we find …" — never frame results as surprising
- ❌ "As one would expect, …" — too casual
- ❌ "The results are consistent with the prior literature." — opens with prior literature, not the test

---

## 3. Magnitude framing — every audit paper does this, in 6 forms

Block 4 of the intro has at least one magnitude. The **results section repeats the magnitude with more precision** and adds 1–3 more forms. Catalog of magnitude forms across the corpus, with verbatim examples:

### Form 1: Percentage point change (5/6 papers; most common)

> "This represents **a 2.1 percentage point reduction** in the probability of a financial reporting irregularity, from 11.1% for an engagement auditor with weak connections, to 9.0% for an engagement auditor with strong connections (i.e., above-median)…" (24-DLWW, ¶379)

> "This indicates that clients of tax-expert auditors have **0.6 percentage points lower BTD** than clients of non-tax-experts…" (25-DQSZ, ¶1703)

> "the coefficients on BigN and FirmIndSpec are significantly negative, resulting in **a 3.9 percentage point reduction** (37% decline) and **a 2.8 percentage point reduction** (27% decline) in reported financial irregularities, respectively…" (24-DLWW, ¶601)

### Form 2: Percentage of base rate (5/6 papers; almost always paired with Form 1)

> "…which equals **a 19% decline** in financial irregularities. Thus, the effect is both statistically and economically significant." (24-DLWW, ¶381)

> "…**equal to 11% of the sample mean ETR** of 18.9 percentage points." (25-DQSZ, ¶1710)

> "…**equals 40% of the sample mean BTD** of 1.5 percentage points." (25-DQSZ, ¶1704)

> "…which represents a reduction of approximately **17% relative to the unconditional mean** of 4.8% (Panel A of Table 2)." (26-KLYY, ¶967–968)

> "…which translates to a reduction of approximately **15% relative to the unconditional mean** of 4.6%." (26-KLYY, ¶972)

### Form 3: Decile / quartile shift (1/6 papers but distinctive)

> "The estimated coefficient 0.293 (0.097) on CON_KW (CON_NOPA) indicates that **a one-decile increase in conservatism is associated with about a 3.3 (1.1) percent decline in audit fees**." (16-DLZ, ¶342–343)

> "**A one-decile increase in CON_KW and CON_NOPA reduces the propensity of auditors to resign by 2.3 percent and 1.2 percent**, respectively." (16-DLZ, ¶388)

### Form 4: Standard-deviation framing (3/6 papers; standard for partner-trait papers)

> "**A one standard deviation increase in PartnerTrust is associated with a 0.8% decrease** in the probability of a going concern opinion, which represents a reduction of approximately 17% relative to the unconditional mean of 4.8%." (26-KLYY, ¶966–968)

> "**a one-standard-deviation increase in CON_KW results in a 0.049-standard-deviation decrease in audit fees** through CON_KW's impact on auditor litigation risk." (16-DLZ, ¶2021)

### Form 5: Interquartile change (1/6 — Dekeyser's signature framing)

> "When we hold all other variables at their means, **an interquartile change in RangeN, RangeHerf, and RangeEntropy leads to a 6.64%, 7.16%, and 7.26% increase in the likelihood of an audit adjustment**, respectively." (24-DHXZ, ¶946)

### Form 6: Comparison to a literature benchmark (3/6 — strongest pattern for credibility)

> "**These effects are similar in magnitude to the effect of mandatory partner rotation (6.5–9.3%) documented in Lennox et al. (2014) and that of early career experiences (4.7%) documented in He et al. (2018)**." (24-DHXZ, ¶947–948)

> "**Notably, our ETR coefficients are comparable to those in Bradshaw et al. (2019) for the SOEs (0.014)**." (25-DQSZ, ¶1711)

> "In evaluating the magnitude of the effects of Network on audit quality, while economically significant, are also somewhat lower, **compared with these two factors that have long been associated with audit quality** [BigN and FirmIndSpec]…" (24-DLWW, ¶604)

### Best-practice combination

The strongest magnitude paragraphs combine **Form 1 + Form 2 + Form 6** in 2–3 sentences:

> "Column (1) reports that the coefficient on Network is −0.021 and significant at the 5% level, indicating that the clients of engagement auditors with stronger social networks report fewer financial reporting irregularities. **This represents a 2.1 percentage point reduction** in the probability of a financial reporting irregularity, from 11.1% … to 9.0% …, **which equals a 19% decline** in financial irregularities. **Thus, the effect is both statistically and economically significant**." (24-DLWW, ¶377–381)

This three-step move — coefficient → percentage points → percent of mean — is the **gold standard**. Use it for every major magnitude in the paper.

### Hard rule

Block 4 (primary result) MUST contain at least **two** of: percentage points, percent of mean, std-dev change, interquartile shift, or literature benchmark comparison. Coefficient + significance level alone is insufficient for the headline result.

---

## 4. Coefficient → economic-magnitude translation

Standard 3-sentence move:

```
Sentence 1: Statistical statement.
   "The coefficient on X is [value] and significant at the [N]% level."

Sentence 2: Economic translation.
   "This represents a [N percentage point / std-dev / decile] [reduction/increase] in
   [outcome], from [base] to [post]."

Sentence 3: Relative magnitude.
   "This equals [N]% of [the sample mean / base rate / a comparable effect from Lennox
   et al. (2014)]."
```

**Verbatim example (24-DLWW, the cleanest in the corpus):**

> "Column (1) reports that the coefficient on Network is −0.021 and significant at the 5% level, indicating that the clients of engagement auditors with stronger social networks report fewer financial reporting irregularities. This represents a 2.1 percentage point reduction in the probability of a financial reporting irregularity, from 11.1% for an engagement auditor with weak connections, to 9.0% for an engagement auditor with strong connections (i.e., above-median), which equals a 19% decline in financial irregularities. Thus, the effect is both statistically and economically significant."

**Verbatim example (25-DQSZ):**

> "As predicted, the coefficient on TAX_EXP is negative (p<1%). This indicates that clients of tax-expert auditors have 0.6 percentage points lower BTD than clients of non-tax-experts, which equals 40% of the sample mean BTD of 1.5 percentage points."

**Verbatim example (26-KLYY):**

> "Turning to our test variable, the coefficient on PartnerTrust is negative and statistically significant (p < 0.004), indicating that audit partners who descended from trusting cultures are less likely to issue going concern opinions relative to their peers. The effect of PartnerTrust on GoingConcern is sizable: a one standard deviation increase in PartnerTrust is associated with a 0.8% decrease in the probability of a going concern opinion, which represents a reduction of approximately 17% relative to the unconditional mean of 4.8%."

**Forbidden alternatives:**

- ❌ "Significant at p < 0.05." (no economic interpretation)
- ❌ "Highly significant." (no quantification)
- ❌ "Has a sizable effect on …" (sizable is a marketing word; see verb whitelist)
- ❌ Reporting only t-statistic without coefficient

---

## 5. Reading-the-table prose: column-walk templates

When walking the reader through a multi-column or multi-panel table, the corpus uses these sentence patterns. Verbatim from corpus:

### Column-by-column walk (most common)

> "**Column (1) reports** that the coefficient on Network is −0.021 and significant at the 5% level, indicating that …" (24-DLWW)

> "**Column (2) of Table 3** repeats our hypothesis test after disaggregating Network it into three components: …" (24-DLWW, ¶382)

> "**Columns (1) and (2) find that the coefficients on UE×Network are significantly positive** both with and without control variables." (24-DLWW, ¶1657)

> "**Columns (4)–(6) report that** when ETR is the dependent variable, the coefficients on TAX_EXP range from 0.015 in Column (5) to 0.021 in Column (4) (all p<1%)." (25-DQSZ, ¶1708)

> "**Starting with column (1), we find** that the coefficient on PartnerTrust is positive and statistically significant when |TotalAccrual| is the dependent variable. **In contrast, the coefficients on PartnerTrust are not statistically significant** in columns (2) and (3), where BeatBenchmark and BigRRestatement are the dependent variables." (26-KLYY, ¶2589–2592)

### Panel-by-panel walk

> "**Panel A of Table 7 finds** that the coefficient on Network × X is significantly negative when X is captured by RelationClient and is significantly positive when X is captured by HighTrust (at the 10% level)." (24-DLWW, ¶2359)

> "**Panel B of Table 7, Column (1) finds** that the coefficient on Network × HiSpdRail is insignificant." (24-DLWW, ¶2367)

> "**Table 5, Panel A reports** that the coefficients on CONSV are negative and statistically significant at p < 0.01, consistent with client conservatism reducing auditor litigation risk. **Panel B reports** the results for the restatement tests." (16-DLZ, ¶2247–2248)

### "We add … to the original analysis" (when extending an existing table)

> "**Column (2) disaggregates Network** into auditors with strong business connections and weak political connections (Network(BusOnly)) …" (24-DLWW, ¶1267 note)

> "**In column (1)**, we find that audit partners who descended from trusting cultures are more likely to be matched to clients with lower bankruptcy risk …" (26-KLYY, ¶553)

### "Together, …" / "Overall, …" (closing sentence of the column walk)

This is **non-negotiable** — every primary-result block ends with a 1-sentence closer.

> "**Together, Table 3 finds** that signatory auditors' tax expertise is associated with lower tax aggressiveness." (25-DQSZ, ¶1712)

> "**Overall, Table 3 finds** that clients with auditors who have stronger networks report fewer financial reporting irregularities, consistent with these auditors providing higher quality audits." (24-DLWW, ¶1231)

> "**In summary, our analysis in Table 4 finds evidence** that three financial reporting factors … are associated with cross-country differences in the information content of annual earnings announcements." (07-DHT, ¶2254)

> "**Taken together, the different-in-difference analysis in Table 4 further attenuates concerns** that the client-partner selection or other unobservable client or auditor characteristics explain the effects of tax-expert signatory auditors on tax aggressiveness." (25-DQSZ, ¶1766)

---

## 6. Cross-sectional / heterogeneity presentation

### The standard 4-step structure

```
Step 1: STATE THE PARTITION + WHY.
   "We expect the effect to be stronger when [condition], because [theoretical reason]."
   "We conjecture that the association is stronger for clients that [satisfy condition]."

Step 2: DEFINE THE PARTITIONING VARIABLE.
   "We define X = 1 when [condition] and zero otherwise."
   "We measure X using [data source / construction rule]."

Step 3: STATE THE PREDICTION ON THE INTERACTION.
   "We expect the coefficient on X × [main variable] to be [sign]."

Step 4: REPORT + INTERPRET.
   "As predicted, Panel A finds the coefficient on X × Y is [sign and significance]."
```

### Verbatim leads (frequency in corpus: cross-sectional appears 6/6)

> "**While China is primarily a relationship-based economy, there is variation in the use of relational contracts. We conjecture that** the association between Network and FinIrreg is stronger for clients that are more likely to use relational contracts, because the benefits of social connections should be greater. **We explore this using two tests.**" (24-DLWW, ¶2043–2044)

> "**This section examines two cross-sectional variables that could moderate** the effect of auditor tax expertise on tax aggressiveness: client ownership structure and auditor industry specialization." (25-DQSZ, ¶2632)

> "**Our results in Table 5 suggest** that trusting audit partners are less likely to issue going concern opinions, with this effect leading to a reduction in Type I errors and no significant change in Type II errors. **However, these results represent the average effect of audit partner trust and we do not expect them to hold uniformly across all engagements. Therefore, we perform a number of cross-sectional tests to shed light on the specific conditions in which these relations hold.** Section 4.2.2.1 examines the role of auditors' legal liability; Section 4.2.2.2 examines the role of clients' negative media coverage; and Section 4.2.2.3 examines the role of client trustworthiness." (26-KLYY, ¶1851–1855)

### Closing sentence patterns ("the result varies predictably …")

> "**Taken together, the results in Table 7 show that the effects of tax-expert auditors on tax aggressiveness vary predictably with client and auditor characteristics, which helps alleviate concerns that unobservable company and auditor characteristics explain our results.**" (25-DQSZ, ¶2662)

> "**Thus, consistent with our predictions, the effect of the auditor's network is stronger among clients that rely more heavily on relationship-based contracting.**" (24-DLWW, ¶2360–2361)

> "**These results confirm our prediction that the reduction in Type I errors is primarily found in settings where audit partners perceive heightened litigation risk and tend to be more conservative.**" (26-KLYY, ¶2326–2328)

### Templates for sub-sub-section headings

Modern JAE papers number cross-sectional partitions as `4.2.2.1`, `4.2.2.2`, `4.2.2.3`. **26-KLYY uses this nesting to perfection** — one sub-section per partition with a 1-sentence "We begin by examining" / "Next, we examine" / "Our third cross-sectional partition" verbal scaffolding:

> "**4.2.2.1. Role of auditor legal liability. We begin by examining whether** …" (26-KLYY, ¶1856)

> "**4.2.2.2. Role of negative media coverage. Next, we examine whether** …" (26-KLYY, ¶2329)

> "**4.2.2.3. Role of client trustworthiness. Our third cross-sectional partition examines whether** …" (26-KLYY, ¶2341)

---

## 7. Mechanism / channel test prose

### The 3-flavor framework

Audit papers test mechanisms via:

1. **Decomposition** (split DV / split IV into components — "is the effect driven by piece A or piece B?")
2. **Mediation / path analysis** (formal Baron & Kenny / Sobel — "what % of the effect goes through M?")
3. **Suggestive evidence** (look at one specific channel — "consistent with channel C, we find …")

### Flavor 1: Decomposition (3/6 papers; the most rigorous + most common)

> "**However, lower BTD may be caused by a reduction in tax aggressiveness (an increase in taxable income) and/or a reduction in opportunistic earnings management (a decrease in book income). If tax-expert auditors reduce BTD by reducing tax aggressiveness, we should find that their effects are associated with increases in taxable income rather than decreases in book income**, which would further strengthen our identification. **We follow Armstrong et al. (2012) and partition BTD into PBI** (pre-tax book income) **and TI** (taxable income). **We then repeat our analysis using PBI and TI as dependent variables and use seemingly unrelated regressions to estimate the difference in the coefficients on TAX_EXP across the models.**" (25-DQSZ, ¶2492–2497)

> "**To further investigate the channel through which auditors monitor aggressive tax strategies, we examine tax-related audit adjustments.**" (25-DQSZ, ¶2620)

> "**Column (2) of Table 3 repeats our hypothesis test after disaggregating Network it into three components: Network(BusOnly), Network(GovOnly) and Network(Both).** … Importantly, **finding a significantly negative coefficient on Network(BusOnly) is inconsistent with our results in Column (1) being explained by connected auditors using their strong political connections to conceal poor client performance.**" (24-DLWW, ¶382–387)

### Flavor 2: Path analysis / formal mediation (1/6 — 16-DLZ canonical)

> "**We next perform a path analysis to test our maintained assumption that inherent risk and auditor business risk are the paths through which conservatism affects fees, GCOs, and resignations.** Path analysis uses a structural equation model to answer how a source variable (in our case, conservatism) affects an outcome variable (in our case, fees, GCOs, or resignations) **by decomposing the correlation between the source variable and an outcome variable into their direct path, and their indirect paths through mediating variables (Baron and Kenny 1986).**" (16-DLZ, ¶1656–1657)

> "**The total mediated path for litigation risk … is significantly negative at p < 0.01, with a coefficient of 0.049. The coefficient implies that a one-standard-deviation increase in CON_KW results in a 0.049-standard-deviation decrease in audit fees through CON_KW's impact on auditor litigation risk. This suggests that the proportion of the total effect … that is attributable to litigation risk is about 35 percent [=0.049/(0.089 − 0.049 − 0.003)].**" (16-DLZ, ¶2021–2024)

### Flavor 3: Suggestive evidence (4/6 papers)

> "**The results in Columns (5)–(7) suggest that one channel through which tax-expert auditors curb tax aggressiveness is by making audit adjustments that increase taxable income, which further improves our identification.**" (25-DQSZ, ¶2628–2630)

> "**This is consistent with Watts (2003), who argues that an important reason for auditors' preference for conservative accounting is to mitigate litigation concern.**" (16-DLZ, ¶2214)

### Mechanism-test lead sentences

- "**To shed light on the mechanism**, we …"
- "**To investigate the channel through which** [main effect] operates, we …"
- "**To further investigate the channel** through which …" (25-DQSZ)
- "**Consistent with [theory] being the channel**, we find that …"
- "**This result is consistent with the [X] channel**: …"

---

## 8. Alternative explanation handling — the "we address this by …" move

### The 3-step move

```
Step 1: NAME THE ALTERNATIVE.
   "An alternative interpretation of our findings is that [X]."
   "A potential concern is that [X]."

Step 2: PROPOSE THE ADDITIONAL TEST.
   "To address this, we …"
   "We mitigate this concern by …"

Step 3: REPORT THE TEST AND CONCLUDE.
   "The results in Table N are inconsistent with [the alternative]."
   "Instead, our results are consistent with [our hypothesis]."
```

### Verbatim examples

> "**An alternative interpretation of our findings is that strong connections help auditors conceal their clients' poor performance by shielding them from regulatory scrutiny. To address this, we repeat our hypothesis test using three alternative measures of audit quality**: going concern modified audit opinions (GCs), stock price crash risk, and earnings response coefficients (ERCs)." (24-DLWW, ¶1234–1235)

> "**Thus, the results in Panel A are inconsistent with strong social connections helping auditors to conceal poor performance among their clients. Instead, they find** that auditors with stronger social networks are more likely to issue GC opinions, **consistent with the delivery of higher audit quality**." (24-DLWW, ¶1263–1264)

> "**Because more audit adjustments are required when pre-audit reporting quality is lower, our results could be driven by lower pre-audit reporting quality instead of auditor performance. To mitigate this concern, we calculate two measures of pre-audit financial reporting quality.**" (24-DHXZ, ¶1299–1301)

> "**A potential limitation of analyzing the change in tax laws is that some companies did not benefit from the decreased statutory tax rate. Specifically, companies with low effective tax rates before 2008 did not experience a tax decline … Thus, we repeat our analysis after retaining only companies whose actual tax rate declined after 2008. As reported in columns (5) and (6), we continue to find similar results for this subsample.**" (25-DQSZ, ¶1758–1765)

> "**We also acknowledge that** it is possible that larger ERCs could be the result of unsophisticated investors who are fooled by connected auditors who conceal their clients' bad news. **However, this seems inconsistent with prior studies, which find** that ERCs in China are reliably associated with several indicators of high earnings quality across a variety of settings…" (24-DLWW, ¶1661–1664)

### "We acknowledge, however …" pattern

This "concede + counter" move appears 5/6. It signals epistemic humility while neutralizing a referee objection:

> "**We acknowledge, however, that there are limitations in using GCs to measure audit quality** (DeFond and Zhang, 2014). Specifically, the auditor's decision to issue a GCs is only applicable to clients that are in reasonably poor financial health, **and the evaluation of GC problems is not the auditor's primary area of expertise**." (24-DLWW, footnote 22)

---

## 9. Null result handling — confidence intervals, power analysis, bootstrap

26-KLYY (and only 26-KLYY) gives the canonical playbook for null results. **This is the single best modern template for handling insignificant coefficients.** When the result on a key DV is not statistically significant, do not fall silent — perform 3 supporting analyses:

### The 3-step null-result protocol (26-KLYY)

> "In column (3), where TypeIIError is the dependent variable, the coefficient on PartnerTrust is not statistically significant (p > 0.10). **To assess how much confidence can be placed in the absence of an association, we perform three complementary analyses.**
>
> **First**, we consider the magnitude of the 95% confidence interval for the insignificant PartnerTrust coefficient (e.g., Cready et al., 2022). **The confidence interval of [–0.00244, 0.00094] indicates that the potential effect size does not exceed one-third of one standard deviation in TypeIIError, consistent with the threshold Cunningham et al. (2019) propose for interpreting a null result as evidence of a small or negligible effect.**
>
> **Second**, we follow prior research and **perform a power analysis to determine whether our sample size is large enough to detect meaningful effects, if present** (e.g., Christensen et al., 2021; Blann et al., 2023). We find that our sample size of 16,414 is sufficient to detect a 0.02180 standard deviation change in TypeIIError (i.e., 0.00102/0.04678) **when alpha equals 0.05 and power is set at the conventional 0.80 level** (Cohen, 1988, p. 530).
>
> **Third**, to address concerns about small sample sizes, **we calculate standard errors using the bootstrap method with 1000 replications** (e.g., Gutierrez et al., 2018; Sherwood, 2025), and find consistent results.
>
> **While these analyses suggest that the lack of significant association between PartnerTrust and TypeIIError is unlikely to stem from insufficient test power, we caution that our null results cannot completely rule out the possibility of such a relation existing.**" (26-KLYY, ¶973–984)

### Verbatim cite for "we find no evidence …" (alternative-explanation null)

> "**Consistent with Table 3, the coefficients on IND_EXP are insignificant. In addition, the coefficients on IND_EXP × POST2008 are also insignificant. … This placebo test also provides comfort that our results in Columns (1) and (2) are not spuriously driven by other concurrent changes in 2008.**" (25-DQSZ, ¶1753–1757)

> "**Panel B of Table 7, Column (1) finds that the coefficient on Network × HiSpdRail is insignificant. Thus, while high-speed rails may improve efficiencies, including those related to auditing, they do not necessarily reduce the prevalence or importance of relationship-based contracting.**" (24-DLWW, ¶2367–2369)

### Forbidden null-result framing

- ❌ "We do not find evidence that …" (without follow-up power discussion)
- ❌ "There is no relationship between …" (overstates absence)
- ❌ "The effect is zero." (cannot conclude from p > 0.10)
- ❌ "Our hypothesis is rejected." (mixes confirmatory/Popperian language)

### Acceptable null-result phrasings

- ✅ "The coefficient on X is not statistically significant (p > 0.10)."
- ✅ "We find no significant association between X and Y."
- ✅ "The 95% confidence interval [a, b] is consistent with a small or negligible effect."
- ✅ "We caution that our null results cannot completely rule out the possibility of such a relation existing." (26-KLYY's verbatim epistemic hedge)

---

## 10. Verb whitelist — the conservatively-confident voice

Counts of the dominant reporting verbs in the 6 results sections:

| Verb | Frequency | Example |
|---|---|---|
| **find** (most common) | hundreds | "We find that the coefficient on Network …" |
| **report** | very high | "Table 4 reports that …" / "Column (1) reports …" |
| **show** (in narrow sense) | high | "Panel C shows that the coefficients are negative." |
| **indicate** | high | "This indicates that clients of tax-expert auditors have 0.6 percentage points lower BTD." |
| **suggest** | medium | "These results suggest that …" |
| **consistent with** | very high | "Consistent with our hypothesis, we find …" |
| **observe** | medium | "We observe that 70% of the auditors have a bachelor's degree or higher." |
| **document** | low–medium | "We document a significant negative association." |
| **provide evidence** | medium | "These analyses provide additional evidence supporting the interpretation that …" |
| **continue to hold / continue to find** | high in robustness | "Our main results continue to hold." |

### Use in narrow technical sense only:

- **"show"** = the table/column literally shows it; not "we have shown" in the sense of "we have proven"
- **"indicate"** = the data point indicates this; not "this indicates a fundamental truth"
- **"suggest"** = used when results lean toward an interpretation but are not airtight
- **"consistent with"** = used when results match a prediction; **never** "prove" or "demonstrate"

### Strong claims allowed:

- ✅ "robust negative association" (26-KLYY uses)
- ✅ "economically significant" (paired with magnitude)
- ✅ "statistically and economically significant" (24-DLWW)
- ✅ "sizable" (rare; only 26-KLYY uses with magnitude immediately following)

### Forbidden verbs (zero in corpus)

- ❌ **prove** / **proves** / **proven**
- ❌ **demonstrate** in unhedged sense ("our results demonstrate definitively …")
- ❌ **establish** ("we establish that …") — too strong
- ❌ **conclusively show** / **definitively show**
- ❌ **reveal** (too dramatic; not in any results section)
- ❌ **uncover** (Khurana intro uses "uncover a robust negative association" once; never in results)
- ❌ **clearly** as a hedge ("clearly show", "clearly indicate") — rhetorical filler

---

## 11. Forbidden patterns — what's NOT done

Patterns absent from all 6 corpus papers:

1. **No marketing adjectives describing magnitude.**
   - ❌ "huge effect", "enormous decrease", "massive", "substantial" (used sparingly only with concrete number), "tiny", "vanishing"
   - ✅ "economically significant", "sizable" (only paired with magnitude)

2. **No bare "highly significant" / "very significant" / "extremely significant".**
   - ❌ "The coefficient is highly significant."
   - ✅ "The coefficient is significantly negative at the 1% level (p < 0.01)."

3. **No p-values in parentheses without coefficients.**
   - ❌ "Network is significant (p < 0.05)."
   - ✅ "The coefficient on Network is −0.021 and significant at the 5% level (t = −2.45)."

4. **No bare t-statistics without the coefficient and significance level.**
   - ❌ "The t-statistic is 2.45."
   - ✅ "The coefficient is 0.293 with a t-statistic of 7.42 (p < 0.01)."

5. **No "we believe", "we think", "we feel" — first-person belief verbs.**
   - ❌ "We believe these results suggest …"
   - ✅ "These results are consistent with …"

6. **No "obviously" / "clearly" / "of course" — these condescend to the reader.**

7. **No "interesting", "surprising", "unexpected" framings (except in narrowly defined places).**
   - ❌ "Surprisingly, we find that …"
   - ✅ "Inconsistent with [the alternative interpretation], we find that …"

8. **No vague "strongly" or "weakly" without numbers.**
   - ❌ "The effect is strongly negative."
   - ✅ "The coefficient is −0.021 (significant at the 5% level), representing a 19% decline relative to the base rate."

9. **No "first to" / "first study to" claims in the results.** (These belong in contributions.)

10. **No discussing the table / panel layout in advance ("As we discuss below in Table N…"). Always: report Table N's content, then move on.**

11. **No "as shown in Table 2 (which is too long to reproduce here)…".** Tables are loaded; just reference and report.

---

## 12. Annotated example: 24-DLWW Section 4.1 (the cleanest results lead in the corpus)

This is the **single best results-section opening** in the corpus. Annotated paragraph by paragraph:

### ¶1 (the headline-result paragraph)

> "**[A. Table-N opener]** Table 3 shows the results of estimating Equation (1). **[B. Column-1 statistical statement]** Column (1) reports that the coefficient on Network is −0.021 and significant at the 5% level, **[C. plain-English interpretation]** indicating that the clients of engagement auditors with stronger social networks report fewer financial reporting irregularities. **[D. Magnitude form 1: percentage points]** This represents a 2.1 percentage point reduction in the probability of a financial reporting irregularity, from 11.1% for an engagement auditor with weak connections, to 9.0% for an engagement auditor with strong connections (i.e., above-median), **[E. Magnitude form 2: percent of base rate]** which equals a 19% decline in financial irregularities. **[F. Closer]** Thus, the effect is both statistically and economically significant."

**Moves: A → B → C → D → E → F.** Six moves in one paragraph, ~70 words. This is the gold standard.

### ¶2 (the disaggregation / mechanism paragraph)

> "**[A. Pivot to additional column]** Column (2) of Table 3 repeats our hypothesis test after disaggregating Network it into three components: Network(BusOnly), Network(GovOnly) and Network(Both). **[B. Result statement]** We find that the coefficient on each component is significantly negative at the 5% level. **[C. Coefficient range + magnitude]** The values of the coefficients range from −0.018 to −0.016, indicating a 1.8 to 1.6 percentage point reduction in the probability of a financial reporting irregularity, which equals a 15%–17% decline over the average incidence of financial irregularities. **[D. Importance / alternative-explanation rule-out]** Importantly, finding a significantly negative coefficient on Network(BusOnly) is inconsistent with our results in Column (1) being explained by connected auditors using their strong political connections to conceal poor client performance."

**Moves: A → B → C → D.** Note the [D] move — disaggregation is also a falsification of an alternative.

### ¶3 (the benchmark-comparison paragraph)

> "**[A. Other-coefficient report + magnitude]** Table 3 also finds that the coefficients on BigN and FirmIndSpec are significantly negative, resulting in a 3.9 percentage point reduction (37% decline) and a 2.8 percentage point reduction (27% decline) in reported financial irregularities, respectively, **[B. Benchmark comparison]** consistent with prior literature (e.g., He et al., 2022; Liu et al., 2010). In evaluating the magnitude of the effects of Network on audit quality, while economically significant, are also somewhat lower, compared with these two factors that have long been associated with audit quality. **[C. Honest hedge / scope]** We note, however, that these other audit quality measures are audit-firm characteristics, while our measure captures an individual auditor-level characteristic, and as such may be difficult to compare."

**Moves: A → B → C.** This paragraph signals the author has thought about external benchmarking and pre-empts the referee's "your effect is small" objection.

### ¶4 (controls + closer)

> "**[A. Other-control-coefficient sweep]** Among the auditor-level controls, Table 3 finds that the coefficient on ClientTies is positive but insignificant. We also find that the coefficient on Tenure is negative and significant; and that the coefficient on the auditor office's geographic proximity to the client (Proximity) is insignificant. Among the client company controls we find significantly negative coefficients on CFO, SOE, INV and ROA; and significantly positive coefficients on Growth, Leverage, Loss and Age. **[B. Section closer]** Overall, Table 3 finds that clients with auditors who have stronger networks report fewer financial reporting irregularities, consistent with these auditors providing higher quality audits."

**Moves: A → B.** The closing sentence restates the headline finding in plain English. Required closer.

---

## 13. How to lead with the headline finding — never bury the lead

In audit papers, the FIRST regression you report is your headline result. The first sentence of your first results paragraph is the most-read sentence of your entire paper after the abstract. **Do not bury it.**

### Examples of strong leads (corpus):

- 24-DLWW: "Table 3 shows the results of estimating Equation (1). Column (1) reports that the coefficient on Network is −0.021 and significant at the 5% level…" (¶377)
- 25-DQSZ: "Table 3 reports the results from estimating equation (1). Columns (1)–(3) use BTD to proxy for tax aggressiveness." (¶1701)
- 24-DHXZ: "Table 4 depicts the results of our regression models using our three different measures of Range. Consistent with our predictions, we find a significantly positive association…" (¶682–683)
- 26-KLYY: "Table 5 presents the regression results testing H1 and H2." (¶561)

### Anti-patterns (NOT in corpus, but common in submissions):

- ❌ "Before reporting our results, we briefly discuss the descriptive statistics in Table 2."
- ❌ "Table 2 reports descriptive statistics. We discuss these before turning to our main results."
- ❌ "We first present descriptive statistics, then sample distribution, then control variables, before turning to the main result."

The corpus's solution: **fold descriptive stats into a 1-paragraph 4.1 sub-section that is purely descriptive, then open 4.2 with "Table N reports the results of estimating Equation (X)."** No transitional throat-clearing.

---

## 14. Self-audit checklist

Before finalizing the results section, verify:

- [ ] Sub-section 4.1 (descriptive stats) is at most 1.5 pages, ends with a 1-sentence summary, and does NOT discuss the test variable's significance
- [ ] Sub-section 4.2 (primary result) opens with one of the 4 archetypes (Table N reports / Consistent with / Turning to / Panel C shows)
- [ ] Primary result reports at least 2 of: percentage-point change, percent of base rate, std-dev change, decile/quartile shift, interquartile shift, literature benchmark
- [ ] Coefficient → magnitude translation follows the 3-sentence move (statistical → economic → relative)
- [ ] Each table walked column-by-column with explicit "Column (N) reports/finds/shows" prose
- [ ] Each table block ends with a 1-sentence "Overall, Table N finds…" / "Together, Table N indicates…" closer
- [ ] At least one alternative explanation is named and addressed in the "An alternative interpretation is X. We address this by Y. The results in Z are inconsistent with X." move
- [ ] Cross-sectional / heterogeneity sub-section follows the 4-step structure (state partition + why → define variable → state interaction prediction → report + interpret)
- [ ] All cross-sectional results conclude with "consistent with our predictions, the effect is stronger when…" or "vary predictably with…" prose
- [ ] If a test for a key DV is null, the 26-KLYY 3-step null protocol (95% CI + power analysis + bootstrap) is applied, OR the null is the main message and is properly hedged with "we caution that…"
- [ ] No marketing adjectives ("huge", "enormous", "massive", "tiny") describing magnitudes
- [ ] No bare "highly significant" / "extremely significant"; instead p-values + coefficients
- [ ] No p-values without coefficients
- [ ] No banned verbs ("prove", "establish", "demonstrate definitively", "reveal", "uncover")
- [ ] No "we believe / we think / we feel" — first-person belief verbs
- [ ] No "surprisingly", "interestingly", "remarkably" framings of results
- [ ] At least one mechanism / channel test (decomposition, mediation, OR suggestive evidence)
- [ ] At least one identification test (rotation, exogenous shock, placebo, falsification, OR PSM)
- [ ] Fixed-effects robustness paragraph reports absorption rate + VIF if absorption > 50% (24-DLWW best practice)
- [ ] Magnitudes are also cited against literature benchmarks where possible (24-DHXZ, 25-DQSZ best practice)
- [ ] Results section length is 8–14 pages (excluding tables); if longer, fold material into Robustness section

---

## Quick reference: the 3 most actionable patterns

1. **The 3-sentence magnitude translation** (24-DLWW gold standard):
   > "The coefficient on X is [value], significant at the [N]% level. This represents a [N percentage point] [reduction/increase] in [outcome], from [base] to [post]. This equals [N]% of [the sample mean / a comparable effect from prior literature]."

2. **The "Table N reports … Overall, Table N finds…" sandwich** — always open and close a regression block with an explicit reference to the table.

3. **The 26-KLYY null-result protocol** — when a key coefficient is insignificant, do 95% CI + power analysis + bootstrap, then close with "we caution that our null results cannot completely rule out the possibility of such a relation existing."

These three patterns alone reproduce 60–70% of the rhetorical scaffolding of a top-3 audit results section.

# Audit-Paper Research Design: Section Anatomy and Identification Rhetoric

**Source corpus.** Extracted from the research-design sections (typically Section 3, occasionally Section 4) of 6 empirical papers:
- DeFond, Hung, Trezevant 2007 JAE (`07-DHT`) — cross-country panel; design = §3 "Research design"
- DeFond, Lim, Zang 2016 TAR (`16-DLZ`) — US audit fees / GCO / resignation; design = §III "Variables Measurement and Model Specification"; sample = §IV
- DeFond, Li, Wong, Wu 2024 JAE (`24-DLWW`) — China engagement-auditor social networks; design = §3 "Data and research design"
- DeFond, Qi, Si, Zhang 2025 JAE (`25-DQSZ`) — China signatory auditor tax expertise; design = §3 "Sample, measures and descriptive statistics" + §4.1 model presentation
- Khurana, Li, Yeung, Yu 2026 JAE (`26-KLYY`) — US partner cultural trust; design = §3 "Data and methodology"
- Dekeyser, He, Xiao, Zuo 2024 JAE (`24-DHXZ`) — China audit-partner industry range; design = §4 "Research methods"

**Note on 25-DQSZ structure.** This paper splits design into a §3 "Sample, measures, descriptive statistics" block (no equation) and a §4.1 "Empirical results" block that *opens* by stating equation (2) and the controls. The model is therefore presented in the results section, not the design section. This is a non-standard layout and the only such case in the corpus.

---

## 1. Standard structure: stable 4-7 sub-section ordering

The corpus follows a near-canonical sub-section order, with two structural variants:

### Variant A — "Setup-first" (4 of 6 papers: 24-DLWW, 24-DHXZ, 26-KLYY, 25-DQSZ)

```
3.1  Sample selection / Data         [paragraph + Table 1 sample-selection schedule]
3.2  Variable measurement(s)         [DV first, IV second, sometimes a separate sub-section per construct]
3.3  Empirical model(s)              [numbered equation, control list, FE, SE clustering]
3.4  Descriptive statistics          [Table 2: means/SD/quartiles; sometimes a sample-distribution table]
```

### Variant B — "Specification-first" (2 of 6 papers: 07-DHT, 16-DLZ)

```
3.   Research design / Variables Measurement and Model Specification
       — DV definition + measurement
       — equation displayed inline with full variable definitions
       — controls justified individually
4.1  Sample selection / Sample and Data
4.2  Descriptive statistics
```

**Cross-cutting moves (universal in 6/6):**
- A numbered estimating equation (always Equation (1) in the design section)
- A control-variable paragraph organized by category ("audit-firm characteristics", "audit-office characteristics", "client characteristics")
- An explicit fixed-effects sentence
- An explicit standard-error clustering sentence
- A line declaring the prediction sign on the focal coefficient

**Functional sub-sections (corpus frequency):**

| Sub-section function | Frequency | Typical heading |
|---|---|---|
| Sample selection table + prose | 6/6 | "3.1 Sample selection" / "Sample and Data" |
| Construct (IV) measurement | 6/6 | "Measuring [Construct]" / "3.2 Measures of [X]" |
| DV measurement | 6/6 | embedded in §3.1 or §3.3 first sentence |
| Empirical model with numbered equation | 6/6 | "3.3 Empirical models" / "Research design" |
| Descriptive statistics + correlation | 6/6 | "3.4 Descriptive statistics" |
| Validation of novel measure | 4/6 (24-DHXZ, 26-KLYY, 24-DLWW, 25-DQSZ) | embedded sub-paragraph |
| Identification strategies | 1/6 in design section (07-DHT 4 paragraphs); 4/6 deferred to results (24-DLWW §4.3, 25-DQSZ §4.2, 24-DHXZ §6, 24-DLWW §5.3) | "Identification strategy" / "Falsification tests" |

**Structural note.** The design section in the modern DeFond/Khurana style is strikingly compact — typically 3-4 pages. Identification machinery (rotation, shocks, falsification, FE robustness) is **deferred to the results section**, not previewed in §3. The design section's job is to specify the baseline model cleanly. This contrasts with macro-finance papers that front-load identification.

---

## 2. Sample-construction prose

### The canonical sample-selection table

Every paper presents a vertical waterfall of filters in Table 1 (or its equivalent). The filter table is organized as:

```
Starting universe                          N1
Less:  filter 1 (with reason)             −x1
Less:  filter 2                           −x2
...
Final sample for [analysis A]              N_A
```

### Verbatim filtering language — building blocks

**Opening sentence (3 corpus templates):**
- "Our sample period covers [year] through [year], with [data] obtained from the [database]." (07-DHT, p. 297)
- "Our sample covers [year] to [year]. We begin in [year] because [reason], and we end in [year] to avoid [reason]." (24-DLWW)
- "Our sample period is from [year] to [year], which begins shortly after a major [policy change]... We end the sample period in [year] because [reason]." (25-DQSZ)

**Filter sentence (corpus-validated formulae):**
- "We exclude [N] observations [reason]." — the dominant pattern (used 4/6 times)
- "We remove [N] observations [reason]." (25-DQSZ uses both "remove" and "exclude" in the same paragraph)
- "We restrict our sample to only the observations that have the data needed to construct our key variables." (26-KLYY) — generic catch-all
- "Consistent with prior research, we remove firms in the financial sector (SIC codes 60–69) and winsorize all continuous variables at the top and bottom 1 percent." (16-DLZ) — combines two filters in one sentence
- "we drop singleton observations (Breuer and deHaan, 2024)." (26-KLYY) — modern econometric hygiene

**Final-sample sentence (the load-bearing line):**
- "Our final sample comprises [N] observations for the [first] analysis and [M] observations for the [second] analysis." (25-DQSZ)
- "This leaves a sample of [N] firm-year observations, comprising [k] unique client companies and [m] unique engagement auditors." (24-DLWW) — provides cluster counts
- "After imposing these filters, our final sample has [N] client-year observations, corresponding to [k] unique audit partners." (26-KLYY) — same template
- "The final sample includes [N] client-year observations across [k] unique engagement partners and [m] unique clients over the ten-year period from [year] to [year]." (24-DHXZ)

**Canonical sample-construction sentence template (synthesized from corpus):**

> "Our sample period is [year]–[year]. We begin with [N0] [unit-of-observation]. We exclude [n1] observations [reason 1]; [n2] observations [reason 2]; and [n3] observations with missing data on [variable list]. Our final sample comprises [N] observations, corresponding to [k] unique [clients/partners/firms]."

### Sample-justification rationales — what reasons the corpus uses

The corpus restricts to one of these 7 rationales:
1. **Data availability / start of disclosure regime** — "Our sample starts in [year] because [the relevant disclosure was first available]" (24-DHXZ: 2006 = MOF audit-adjustment data)
2. **End-period to avoid confound** — "We end in [year] to avoid the effects of COVID-19" (24-DLWW), "to avoid [a regulatory change that compromises measurement]" (25-DQSZ end-2016 for IFRIC 23)
3. **Restriction to financially distressed firms** — "we estimate the model using a sample of distressed firms, defined as firms that report either negative net income or negative operating cash flows" (16-DLZ); "a smaller sample of 4,946 financially distressed client-year observations, where a client is classified as financially distressed if the client reports negative earnings or negative operating cash flow" (26-KLYY)
4. **Removal of financial sector** — "Consistent with prior research, we remove firms in the financial sector (SIC codes 60–69)" (16-DLZ); "Observations in the Financial Industry: −628" (25-DQSZ)
5. **Removal of structurally non-applicable observations** — "observations with zero or negative taxable income (Chen et al., 2010; Manzon and Plesko, 2001)" (25-DQSZ); restrict ETR to [0,1]
6. **Modern econometric hygiene** — "we drop singleton observations (Breuer and deHaan, 2024)" (26-KLYY)
7. **Removal of incomplete identification** — "observations without information to identify auditor's signature" (25-DQSZ); "missing data on auditors" (24-DLWW)

**Forbidden sample-justification rhetoric (none in corpus):**
- ❌ "Our sample is large enough to..."
- ❌ "We use the most recent data available"
- ❌ Vague timeframe ("recent years"): every paper specifies start year + end year + reason

---

## 3. Variable measurement section

### Dependent variable (DV) introduction — verbatim templates

The DV is always introduced with a "Following [Author Year]" credibility move:

- "Following Gul et al. (2013) and He et al. (2017), we proxy for audit quality using financial reporting irregularities (FinIrreg), which equal one if [definition]." (24-DLWW)
- "Following Lennox et al. (2014), we use audit adjustments as our proxy for audit quality. We construct a variable Adjustment that equals one if [definition], and zero otherwise." (24-DHXZ)
- "Following prior studies (Bradshaw et al., 2019; Chan et al., 2013; Tang et al., 2017), we use the book-tax difference (BTD) and current effective tax rate (ETR) to measure tax avoidance." (25-DQSZ)
- "We measure the information content of earnings announcements as the 2-day abnormal return variance around the earnings announcement date, where higher variance is consistent with greater information content (Beaver, 1968; Warner et al., 1988; Landsman and Maydew, 2002)." (07-DHT)

**Defense-of-DV move (5/6 papers).** After defining DV, papers add a 1-3 sentence justification:

- "Financial irregularities are an appealing proxy for audit quality because the auditor's primary responsibility is to assure that the client's financial statements are free from material misstatement. Financial statements that are subsequently found to contain material misstatements or financial misrepresentations are incontrovertible evidence that the auditor failed to fulfill their primary responsibility. Thus, unlike most other commonly used audit quality proxies, financial irregularities are clear indicators of poor audit quality that are directly attributable to the engagement auditor." (24-DLWW)

This DV-defense paragraph is **mandatory** when using a non-standard DV. Pattern: (1) name the proxy, (2) tie it to the auditor's primary responsibility, (3) explain why it's preferable to alternatives.

### Independent variable (IV) introduction

The novel-measure IV gets its own labeled sub-section in 4/6 papers:
- §3.2 "Measuring audit partners' cultural trust" (26-KLYY)
- §4.2 "Measures of auditor industry range" (24-DHXZ)
- §3.2 "Tax avoidance measures" (25-DQSZ — DV is novel; IV is a label, TAX_EXP, defined inline)
- 24-DLWW: 4 paragraphs of measurement prose embedded in §3.1 (no separate sub-heading)

### Controls — the standard ordering

The corpus presents control variables in **categorical groups, not as a flat list**. The ordering is:

**For audit-quality papers with auditor + client controls:**
```
1. Audit-firm-level controls       (Big4, FirmTenure, FirmIndustryExpert)
2. Audit-office-level controls      (OfficeSize, OfficeClientImportance)
3. Audit-partner/auditor-level      (PartnerExperience, PartnerBig4Exp, PartnerFemale, ...)
4. Client-level controls            (ClientSize, ClientLeverage, ClientLoss, ClientROA, ...)
```

**Example (26-KLYY):** "At the audit firm level, we control for the number of years that the audit firm has audited the client (FirmTenure) and whether the audit firm is a leader in the client's industry (FirmIndustryExpert). At the audit office level, we control for the size of the audit office (OfficeSize) and the client's relative importance to the audit office (OfficeClientImportance). At the audit partner level, we control for whether the partner has ever worked for a Big 4 audit firm (PartnerBig4Exp), the number of clients the partner audited during the year (PartnerBusyness)..."

**Example (24-DHXZ) uses a different category structure:** "We include this first set of control variables to control for possible intrinsic differences between auditors with wide and narrow industry ranges. ... Our second set of control variables pertains to company attributes that contribute to the occurrence of misstatements (condition #1). ... Our third set of control variables encompasses audit features that impact the probability of the auditor identifying a misstatement and requiring the client to correct the misstatement (condition #2)."

This 24-DHXZ "two-condition" rationale (misstatement-occurrence vs. misstatement-detection) is borrowed directly from Lennox, Wu, and Zhang (2014). It is **the most explicit theoretical justification of controls in the corpus** and a model worth imitating.

**Forbidden controls patterns (none in corpus):**
- ❌ Listing controls as a comma-separated string with no rationale
- ❌ Saying "we control for the standard set of variables used in [literature]"
- ❌ Hiding controls in a footnote without naming them in body

### Lagging and timing of independent variables

A subtle but consistent move:
- "all independent variables are measured in the year concurrent with audit fees except CONSV, which is lagged by one year. We use lagged conservatism in our tests to help mitigate concerns with endogeneity and reverse causality." (16-DLZ)

This is the explicit endogeneity-mitigation justification for lagging the focal IV. It is the **first identification move** in the design section and should be defaulted to whenever the IV is plausibly contaminated by the DV.

---

## 4. Empirical model presentation

### The numbered-equation convention (6/6)

Every paper presents a numbered estimating equation (always (1)) and, where applicable, sub-equations (2), (3), (4) for additional outcomes.

**The opening verb.** 4 of 6 papers use "We estimate the following [model class]":
- "We estimate the following ordinary least squares (OLS) model based on prior research" (16-DLZ)
- "we estimate the following linear probability model (LPM)" (26-KLYY)
- "we estimate the following logistic regression adapted from Landsman, Nelson, and Rountree (2009)" (16-DLZ — for resignation model)

The other two use:
- "We test our hypothesis by estimating the following regression:" (24-DLWW)
- "We test our hypothesis by estimating the following OLS regression:" (25-DQSZ)
- "We then specify the following logistic model in which we regress Adjustment on Range" (24-DHXZ)

### Equation display style

Two conventions exist:

**Style A — Greek-letter, compact form (3/6).** Use when the focal coefficient is explicitly named:
```
FinIrreg_it = α + β1·Network_it + γ·Controls + Fixed effects + ε_it    (1)
```
(24-DLWW, 24-DHXZ, 26-KLYY)

**Style B — Full coefficient enumeration (3/6).** Use when controls are theoretically heterogeneous and require sign predictions:
```
LAUDIT_t = c0 + c1·CONSV_{t-1} + c2·MV_t + c3·Quick_t + c4·Loss_t + ... + ε_t    (1)
```
(16-DLZ, 25-DQSZ, 07-DHT)

**Modern preference (2024-2026 JAE):** Style A. The full enumeration in 16-DLZ is older convention.

### Variable definitions: footnote vs. inline vs. appendix

**Corpus convention (6/6):** Variables are defined in **Appendix A** (or B), and the design-section text says "Detailed variable definitions for all models are presented in Appendix A" (16-DLZ) or "All variables are defined in Appendix 1" (24-DLWW) or "we summarize these control variables in the following paragraph and define them in detail in Appendix A" (26-KLYY).

The design section names each control variable with its short label and a brief gloss (1 sentence at most), but reserves full definitions for the appendix. **Do not paste an Appendix A into the body.**

**Exception (07-DHT):** The 2007 paper defines all variables inline within the design section. This is older JAE convention and is no longer preferred.

### The "control set" sentence — a load-bearing template

```
"When estimating equation (1), we include a comprehensive set of control variables based on prior research."
                                       (26-KLYY)

"We control for the following audit firm-level characteristics, where all variables are
defined in Appendix 1: [list]. We control for the following individual auditor characteristics:
[list]. We control for the following client characteristics: [list]."
                                       (24-DLWW)
```

---

## 5. Identification rhetoric — the central catalog

This is the densest component of the design (and post-design) sections. The corpus uses **8 distinct identification moves**, often combined.

### Move 1: Lagged-IV / reverse-causality preemption

> "all independent variables are measured in the year concurrent with audit fees except CONSV, which is lagged by one year. We use lagged conservatism in our tests to help mitigate concerns with endogeneity and reverse causality. While the auditors' choice of fees, GCO, and resignation potentially affect client conservatism in the contemporaneous year, it is unlikely that they affect the prior year's client conservatism." (16-DLZ)

**Use when:** the IV is plausibly endogenous to the DV in the current period. **Stock template:** "We use lagged [IV] to mitigate concerns with [reverse causality / endogeneity]. While [contemporaneous IV] could be affected by [DV], it is unlikely that [DV in year t] affects [IV in year t–1]."

### Move 2: Mandatory audit-partner rotation as quasi-experiment

> "China requires mandatory auditor (but not audit firm) rotation every five years (Lennox et al., 2014). We use this to examine whether tax aggressiveness decreases (increases) when a non-tax-expert (tax-expert) auditor is replaced by a tax expert (non-tax expert). Unless a client coincidentally changes its tax strategy during the year in which the mandatory five-year rotation occurs, it is unlikely that the change in the auditor's tax expertise is explained by selection." (25-DQSZ §4.2.1)

**Logic:** the rotation is mandatory (i.e., not chosen by the client), so partner-trait variation generated at the rotation moment is plausibly exogenous to client-side determinants of the outcome.

### Move 3: Regulatory shock as DiD treatment

> "Effective January 1, 2008, China replaced two separate income tax laws for domestic and foreign-investment companies with a single tax law. This reduced the top marginal tax rate from 33% to 25% for all companies, reducing the benefits of tax aggressiveness and companies' incentives to engage in aggressive tax avoidance. Thus, we expect the effect of tax-expert signatory auditors on tax aggressiveness to decline following the exogenous tax rate decrease." (25-DQSZ §4.2.2)

> "On October 19, 2013, the Organization Department of the Communist Party of China's Regulation 18 ('Reg. 18') banned government and university officials (including university presidents and deans) from serving as independent directors, triggering a wave of director resignations in the two years following its passage... To identify the effect of Reg. 18 we employ a difference-in-differences (DiD) design that restricts our analysis to companies during the five-year period surrounding the new regulation, 2012–2016 (T-2 to T+2)." (24-DLWW §5.3)

**Pattern:** (1) name the regulation with date and citation; (2) describe what it changed; (3) explain why the change generates plausibly exogenous variation in the IV (or in the demand for the DV); (4) specify the DiD window; (5) discuss parallel trends.

### Move 4: Falsification / placebo tests

**Geographic placebo (24-DLWW):**
> "While we expect the auditor's social network within the client's province (Network) to improve the auditor's competency in deterring irregularities, we do not expect the auditor's connections with networks outside of the client's province to deter them. Thus, we perform falsification tests that repeat our analysis in Table 3 after including placebo measures of the auditors' social networks. Our first measure, Network(NeighborProv), captures each auditor's connections in their clients' neighboring provinces... Our second measure, Network(OutProv), captures the engagement auditor's social ties in all provinces except the province in which the client is located."

**Construct placebo (25-DQSZ):**
> "Columns (3) and (4) of Panel B report placebo tests that replace auditor tax expertise with industry expertise. We regress our tax aggressiveness measures on IND_EXP, POST2008, and IND_EXP × POST2008. Consistent with Table 3, the coefficients on IND_EXP are insignificant... This placebo test also provides comfort that our results in Columns (1) and (2) are not spuriously driven by other concurrent changes in 2008."

**Outcome placebo (25-DQSZ §4.2.3):**
> "We argue that one reason that tax-expert auditors have incentives to reduce tax aggressiveness is that it increases misstatement risk. Thus, finding that tax-expert auditors mitigate the types of tax aggressiveness that lead to misstatements would further strengthen our identification."

**Pattern:** Identify a related-but-irrelevant variable (or sample). Predict null effect. Run identical specification. Report null. Use the words "placebo" or "falsification."

### Move 5: Fixed-effects defense / robustness

The standard FE escalation pattern:

> "Our primary results are robust to including audit firm, client, signatory auditor, and province-year fixed effects." (24-DLWW Block 5)

**In the design section, FE choice is justified explicitly:**

- "Equation (1) also includes year, audit office, and client fixed effects to further control for unobserved sources of heterogeneity (Gormley and Matsa, 2014)." (26-KLYY)
- "We include three sets of fixed effects in our analysis. To alleviate the concern that the effect of auditor industry range may be driven by the number of clients an auditor has, we control for auditor portfolio size fixed effects based on the number of clients... In addition, we incorporate industry and year fixed effects to control for unobserved heterogeneity across industries and over time." (24-DHXZ)
- "We also include province, industry, and year fixed effects." (24-DLWW)

**Standard rationale citations:** Gormley and Matsa (2014) for unobserved-heterogeneity defense; Petersen (2009) for clustered SE.

### Move 6: Cross-sectional corroboration

> "We also investigate whether our findings are stronger in [setting where the mechanism should be amplified]. To examine these predictions, we partition our sample into [groups]." (24-DLWW §5.1)

In the design section, cross-sectional corroboration is **not previewed as identification**. It appears in the results section. But it is *invoked* in the design section's setting-justification:

> "China also has variation in market development across its provinces, which should affect the clients' reliance on relational contracting." (24-DLWW intro)

### Move 7: Matching (PSM, entropy balance) — corpus stance

**Striking observation:** Of the 6 corpus papers, **only one explicitly uses propensity score matching** (25-DQSZ §4.2.3 for tax-restatement matched sample), and even there, it is a 1-to-1 industry-and-size match, not formal PSM. **DeFond-style papers post-2017 systematically prefer fixed-effects designs over PSM.** This is consistent with DeFond, Erkens, and Zhang (2017) JAE, which documented that PSM produces unstable inference in audit settings.

Reproducible template — "matched-sample" prose (25-DQSZ):
> "Following Agrawal and Chadha (2005), we match each restatement company to a non-restatement company (1) in the same industry as the restating company (the same two-digit code for manufacturing companies and the same one-digit code for other companies); and (2) with the closest market capitalization to the restating company at the end of the year before the earliest restatement."

**Rule:** Avoid PSM unless you have a strong reason. Prefer fixed-effects + control-variable specification.

### Move 8: Acknowledge-then-counter

This is the modern DeFond move that pre-empts referee objections:

> "A potential limitation of analyzing the change in tax laws is that some companies did not benefit from the decreased statutory tax rate. Specifically, companies with low effective tax rates before 2008 did not experience a tax decline following the top marginal rate decline. Thus, we repeat our analysis after retaining only companies whose actual tax rate declined after 2008. As reported in columns (5) and (6), we continue to find similar results for this subsample." (25-DQSZ §4.2.2)

> "However, we note that while the decline in audit quality is gradual in the full sample, it begins immediately following the disruption, which may be sooner than one might expect... We address this issue in Columns (3) and (4) of Table 8, which report the results after excluding turnovers due to the political scandals that potentially confound the results in Columns (1) and (2)." (24-DLWW §5.3)

**Pattern:** "[Concession of limitation]. [However/Thus] we [counter-test]. [The counter-test confirms / mitigates the limitation]."

### Quick-reference catalog

| Move | Frequency in corpus | Verbatim trigger |
|---|---|---|
| Lag IV | 1/6 (16-DLZ) | "we use lagged X to help mitigate concerns with endogeneity and reverse causality" |
| Partner rotation | 1/6 (25-DQSZ) | "Unless a client coincidentally changes its [behavior] during the year of mandatory rotation, it is unlikely that..." |
| Regulatory shock (DiD) | 2/6 (24-DLWW, 25-DQSZ) | "Effective [date], [Authority] [policy change]. We employ a DiD design..." |
| Geographic placebo | 1/6 (24-DLWW) | "While we expect [in-province], we do not expect [out-of-province]..." |
| Construct placebo | 1/6 (25-DQSZ) | "[Replace focal IV] with [related IV]. Consistent with [null]..." |
| FE escalation | 6/6 | "Our primary results are robust to including [progressively more granular] fixed effects" |
| Acknowledge-then-counter | 4/6 | "A potential limitation of [X] is that [Y]. Thus, we repeat..." |
| Matched sample | 1/6 (25-DQSZ) | "Following [Author Year], we match each [treatment] to [control]..." |
| Cross-sectional corroboration | 6/6 | "We also examine whether [effect] is stronger when [moderator] is high" |

---

## 6. Endogeneity acknowledgment patterns

Modern DeFond-style papers explicitly acknowledge they cannot fully identify causal effects in three places:

### Acknowledgment 1: The matching limitation (audit-partner papers)

> "Audit partners are not randomly assigned to audit engagements. The matching of audit partners to clients can be influenced by partner assignment by the audit firm (Dodgson et al., 2020), partner shopping by the client (Chen et al., 2016), and negotiations between the partner and the client (Gibbins et al., 2001). This type of matching is not unique to our research question and applies to virtually all studies that examine the effects of individual audit partners (Lennox and Wu, 2018). Nevertheless, to assess the extent of such matching in our setting and to inform the empirical design of our main tests, we begin by running a determinants model to understand whether audit partners who descended from trusting cultures are matched to clients with different underlying characteristics." (26-KLYY §4.1)

**Template:** Acknowledge non-randomness → cite the canonical critique paper (Lennox and Wu 2018) → describe a determinants model → explain how the FE structure mitigates the residual concern.

### Acknowledgment 2: The measurement limitation (24-DHXZ)

> "A limitation of our approach is the lack of data on an auditor's private clients, which is a common challenge faced by studies on audit partners (Lennox and Wu, 2018). The industry range measures are based on an auditor's publicly listed clients and each client's primary industry. Thus, some auditors with a large set of private clients in different industries may be wrongly classified as having a narrow industry range. A similar downward bias can occur for the auditors of a small set of publicly listed clients that operate in multiple industries. To the extent that these measurement errors cause some misclassifications of a wide range as a narrow range because of unobservability, our estimates of the effects of industry range on audit adjustments are likely to be attenuated."

**Template:** Acknowledge measurement gap → cite the canonical critique → state the direction of the bias → argue the bias is conservative (i.e., works against finding the result).

### Acknowledgment 3: The country-level confounder limitation (07-DHT)

> "While we measure the firm-level control variables in each of the 8 years during our investigation period, we do not remeasure the country-level independent variables each year due to data limitations. We note that this is a common limitation in cross-country studies (Hung, 2000; Leuz et al., 2003), and that changes in country-level institutions are a slow process (North, 1990). To the extent that our independent variables change over the investigation period, we introduce noise into our measures. However, we do not expect this noise to bias towards supporting our hypotheses."

**Template:** Acknowledge time-invariance limitation → cite prior work that did the same → argue noise → argue noise is unbiased / conservative.

### Acknowledgment of judgment in hand-collection (24-DLWW)

> "However, as previously discussed, there is some question regarding the speed with which this disruption is expected to affect earnings quality. Thus, it is important to caveat that our sample selection process for identifying the corruption-related disruptions, which involves extensive hand collection, necessarily involves judgement. While we followed a collection process used in prior research (Pan and Tian, 2020), we cannot be certain that we were able to identify all of these cases."

**Template:** Acknowledge judgment → cite prior work using same process → acknowledge uncertainty.

---

## 7. China-setting design moves (4/6 corpus papers use Chinese data)

In the **design** section (different from intro), the China justification is operational:

### Move 7a: Identify the unique data feature

> "We hand-collect the engagement auditor's identity from annual reports and obtain education, personal data, and office location from resumes at the Chinese Institute of Certified Public Accountants (CICPA). We identify the auditor's office using registration records from provincial CICPA chapters, audit firm websites and business registration records." (24-DLWW)

> "Audit reports in China are signed by two auditors, with one signature above the other, where the top signature is from the auditor who performs the review work, and the bottom signature is from the auditor who is responsible for the fieldwork (He et al. 2017, 2018; Lennox et al., 2014). We measure the engagement auditor's local networks because they are geographically closer to the client and have stronger influence on the detection of financial irregularities." (24-DLWW)

> "Data on audit adjustments come from China's Ministry of Finance (MOF). We manually collect the names of engagement partners from annual reports. Information on audit partners' characteristics is from the China Securities Regulatory Commission (CSRC) and the Chinese Institute of Certified Public Accountants (CICPA). Company-level information comes from the China Stock Market and Accounting Research (CSMAR) database." (24-DHXZ)

**The signer-role explanation is a recurring rhetorical move in China papers** because it (a) signals institutional knowledge, (b) justifies why the focal partner is the right unit. The corpus typically cites institutional-context references when describing the dual-signer convention; the specific anchor papers are the user's call.

### Move 7b: Acknowledge the China-specific feature might generalize

> "Several recent studies use the audit adjustment data to examine broad economic questions that are not specific to the China setting (Lennox et al., 2014, 2016, 2018, 2020, 2023; He et al., 2018; Lennox and Wu, 2022b). Our approach is similar in that our theory does not hinge on the specific institutional setting." (24-DHXZ footnote 13)

This is the "our setting is uniquely good for measurement, but the mechanism is general" move — used to deflect the "what does China have to do with this?" referee objection.

### Move 7c: Industry classification choice

> "Industry classifications are from the CSRC industry classification scheme with two-digit industry codes for manufacturers and one-digit industry codes for other sectors (Guan et al., 2016; Gul et al., 2013)." (24-DLWW)

> "We follow the CSRC industry classification commonly used in China research (Chen et al., 2016; Giannetti et al., 2015)." (24-DHXZ)

This sentence is **always** included in China audit papers and **always** cites two China-finance-or-accounting papers for the convention.

### Move 7d: The data-source disclaimer chain

The corpus uses a fixed phrase chain: "We obtain financial and stock market data from Wind Infor and the China Stock Market & Accounting Research (CSMAR) databases." (25-DQSZ) — append "We manually collect [hand-collected items] from [primary source]" — append "Information on [auditor characteristics] is from [CICPA / CSRC / CCTAA]". This three-source enumeration appears in 3 of 4 China corpus papers.

---

## 8. Standard error and clustering language

**Universal pattern (6/6):** A single sentence states the clustering choice, followed by a footnote or sentence claiming robustness to alternative clusterings.

**Verbatim corpus templates:**

- "We cluster standard errors by client since we have multiple yearly observations for each client (Petersen, 2009)." (26-KLYY)
- "Standard errors are clustered by audit firm." (24-DLWW); footnote: "Our results are robust to clustering by client, province, or engagement auditor."
- "To address potential serial correlation in the data, we cluster standard errors by client (Petersen, 2009)." (24-DHXZ)
- "with standard errors clustered at the client-company level." (25-DQSZ)
- "In all models, we use standard errors clustered by firm." (16-DLZ)

**Pattern:**
1. State cluster level in body.
2. Cite Petersen (2009) for justification.
3. Footnote robustness to alternative clustering.

**Cluster-level choice is dictated by the unit of treatment variation:**
- Treatment varies at audit firm → cluster at audit firm (24-DLWW)
- Treatment varies at client → cluster at client (26-KLYY, 24-DHXZ, 25-DQSZ)
- Treatment varies at firm-year and panel is unbalanced → two-way cluster occasionally (not in corpus design sections, but appears in robustness)

---

## 9. Fixed effects choice and justification

### The corpus FE structure (modal choice)

| Paper | Year FE | Industry FE | Client FE | Audit Office FE | Audit Firm FE | Province FE | Auditor FE |
|---|---|---|---|---|---|---|---|
| 07-DHT | – | ✓ | – | – | – | – (country FE = unit of obs) | – |
| 16-DLZ | ✓ | ✓ | – | – | – | – | – |
| 24-DLWW | ✓ | ✓ | – | – | – | ✓ | – |
| 24-DHXZ | ✓ | ✓ | – (used in robustness) | – | – | – | "Portfolio-size FE" (novel) |
| 25-DQSZ | ✓ | ✓ | – (used in robustness §4.2.6) | – | – | – | – |
| 26-KLYY | ✓ | – | ✓ | ✓ | – | – | – |

### The defense of FE choice

Three rhetorical templates:

**Template 1 — "Gormley and Matsa" defense:**
> "Equation (1) also includes year, audit office, and client fixed effects to further control for unobserved sources of heterogeneity (Gormley and Matsa, 2014)." (26-KLYY)

**Template 2 — "structural justification" defense:**
> "To alleviate the concern that the effect of auditor industry range may be driven by the number of clients an auditor has, we control for auditor portfolio size fixed effects based on the number of clients. We use indicator variables for auditors with one client (4945 observations), two clients (4034 observations), three clients (2590 observations), four clients (1486 observations), and five or more clients (2482 observations). This approach allows us to compare auditors with the same number of clients but different industry experiences." (24-DHXZ)

**Template 3 — "robustness escalation" defense:**
> "Our primary results are robust to including audit firm, client, signatory auditor, and province-year fixed effects." (24-DLWW)

### Power-vs-precision trade-off

> "Including client fixed effects can significantly reduce the power of the test due to limited time-series data of audit adjustments. Thus, prior research often omits client fixed effects from the analysis (e.g., He et al., 2018; Lennox et al., 2014). Our sample contains ten years of data, and our results continue to hold after we include client fixed effects, though the statistical significance is somewhat reduced (see Section 5.3.2)." (24-DHXZ)

This is the **canonical client-FE trade-off paragraph.** Use when the focal IV varies modestly within client.

### Modern econometric hygiene moves

- **Singleton dropping** (26-KLYY): "we drop singleton observations (Breuer and deHaan, 2024)" — increasingly mandatory with high-dimensional FE
- **LPM over logit/probit** (24-DLWW, 26-KLYY): "We use a linear probability model to estimate Equation (1) because it includes several fixed effects (Angrist and Pischke, 2008), although our results are robust to using a logit model."
- **Incidental-parameters defense** (26-KLYY footnote 13): "We estimate equation (1) using ordinary least squares (OLS) rather than a non-linear approach (probit or logit) to avoid the incidental parameter problem (e.g., Hanlon and Hoopes, 2014; Dou et al., 2018)."

---

## 10. Construct validation for novel measures

The papers introducing novel constructs follow a 4-step validation anatomy.

### Anatomy

```
Step 1: Source the data / algorithm
Step 2: Describe the construction procedure
Step 3: Defend with prior-validation evidence
Step 4: Address measurement-error concerns + describe robustness checks
```

### Example A — PartnerTrust (26-KLYY §3.2)

> [Step 1] "We measure the cultural component of audit partners' trust beliefs (PartnerTrust) using a two-step procedure. First, we identify each audit partner's country of origin using the NamePrism algorithm, which uses a person's name to predict the person's nationality/ethnicity. This approach has become a widely accepted procedure in academic research and, to the best of our knowledge, NamePrism is the most effective name-based nationality/ethnicity classifier currently available (e.g., Diamond et al., 2019; Perez-Saiz and Xiao, 2022)."

> [Step 2] "Second, we measure the level of trust in each country using data from the World Values Survey... Our measure of trust is the average response across all survey participants in each country, where responses are coded as 1 when 'most people can be trusted' is selected and responses are coded as 0 when 'you can never be too careful when dealing with others' is selected. For each name that we input into NamePrism, the algorithm returns probabilities for 39 geographic regions... Combining the previous steps, we compute PartnerTrust as the probability-weighted average trust for the top three regions that each partner is from."

> [Step 3] "This approach to measuring cultural trust has been validated by a number of studies using data from the General Social Survey... Using these data, Bhagwat and Liu (2020) document a strong positive correlation between the tendency to trust of immigrants in the United States and the tendency to trust in their genealogical countries of origin (p < 0.0001)... Tests by independent researchers have yielded similar results, providing compelling evidence for the validity of our PartnerTrust measure (e.g., Guiso et al., 2006; Fernández, 2011)."

> [Step 4] "In additional sensitivity analyses, we show that our inferences are robust to using U.S. Census records to infer audit partners' countries of origin (Bhagwat and Liu, 2020) and using other algorithms, including the OnoMAP software developed by the Department of Geography at University College London (Ellahie et al., 2017) as well as the matching technique developed by Kerr (2008) which is utilized by Brochet et al. (2019)."

### Example B — Industry range (24-DHXZ §4.2)

> [Step 1] "We construct three proxies to capture the extent to which an auditor has diverse experiences in different industries. All three proxies are based on the idea that diverse experiences in different industry environments make auditors more likely to encounter inconsistencies and counterexamples..."

> [Step 2] "More specifically, our first proxy RangeN is measured by the natural logarithm of the number of industries that the auditor's portfolio covers in the past three years (t–2 to t). The other two proxies, RangeHerf and RangeEntropy, are based on the Herfindahl index and the entropy index, respectively..."

> [Step 4] "A limitation of our approach is the lack of data on an auditor's private clients, which is a common challenge faced by studies on audit partners (Lennox and Wu, 2018). The industry range measures are based on an auditor's publicly listed clients and each client's primary industry. Thus, some auditors with a large set of private clients in different industries may be wrongly classified as having a narrow industry range... To the extent that these measurement errors cause some misclassifications of a wide range as a narrow range because of unobservability, our estimates of the effects of industry range on audit adjustments are likely to be attenuated."

### Example C — Local Network (24-DLWW)

The Network construct is built bottom-up: define a **single tie** (school + work) → count ties → benchmark vs. provincial median → combine business + government networks → define construct alternatives (BusOnly, GovOnly, Both). Crucially, 24-DLWW shows the additional move of **decomposing the construct into orthogonal sub-components** to provide internal validation.

> "Network(BusOnly) equals 1 if the number of business ties is above the median and the number of political ties is below the median (i.e., Network(Bus) = 1 and Network(Gov) = 0), and zero otherwise. Thus, Network(BusOnly) captures auditors with strong business connections, but weak political connections."

### Example D — CTA tax expertise (25-DQSZ)

> "Given the high level of effort associated with attaining CTA designation it is not surprising that a relatively small percentage of auditors are both willing and able to purse CTA status. Interestingly, however, the pass rate of the CTA exam is also 21%. Thus, if all auditors strive for CTA designation, we would expect only around 20% to be successful." (footnote 17)

This is a "construct face-validity sanity check" — compare the empirical share of constructed indicator vs. an institutional benchmark.

### Construct validation checklist

A novel measure passes the corpus bar only if you write:
1. ☐ Data source named with citation
2. ☐ Algorithm/formula given (or referenced if standard)
3. ☐ External validation cited (prior paper that validated similar measure)
4. ☐ Limitation acknowledged (Lennox-Wu 2018 cite for partner-data limitations)
5. ☐ Robustness to alternative measurement strategies promised
6. ☐ Decomposition into sub-components (where applicable, as in 24-DLWW)
7. ☐ Sanity-check against institutional benchmark (where possible, as in 25-DQSZ CTA pass rate)

---

## 11. Verb whitelist (design section specific)

These verbs appear with high frequency in the corpus design sections. Use them. They form the active vocabulary of method:

**Estimation:**
- estimate (the most common method verb: "We estimate the following...")
- specify ("We specify the following logistic model")
- regress ("We regress Adjustment on Range")

**Measurement:**
- measure ("We measure X as...")
- proxy for ("We proxy for audit quality using...")
- construct ("We construct three proxies")
- compute ("we compute PartnerTrust as the probability-weighted average...")
- collect / hand-collect / manually collect ("We manually collect restatement announcements")
- identify ("We identify the auditor's office using...")
- obtain ("we obtain education...from resumes at CICPA")

**Sample construction:**
- exclude ("We exclude observations with...")
- remove ("We remove observations in the financial sector")
- restrict ("We restrict our sample to only the observations that have...")
- drop ("we drop singleton observations")
- retain ("we only retain GCO firms in the first year they receive a GCO")
- winsorize ("we winsorize all continuous variables at the top and bottom 1 percent")

**Specification:**
- include ("We also include province, industry, and year fixed effects.")
- control for ("We control for [list]")
- cluster ("Standard errors are clustered by audit firm")
- lag ("CONSV, which is lagged by one year")

**Identification:**
- exploit ("We exploit a regulatory shock that...")
- examine ("We examine whether tax aggressiveness decreases when...")
- mitigate ("We use lagged X to mitigate concerns with endogeneity")
- attenuate ("our estimates...are likely to be attenuated")
- alleviate ("To alleviate the concern that...")

**Validation:**
- validate ("This approach has been validated by...")
- corroborate ("Corroborating our primary findings...")

**Acknowledgment:**
- acknowledge ("We acknowledge that...")
- caveat ("it is important to caveat that...")
- recognize / note ("We note, however, that...")

---

## 12. Forbidden patterns (none in corpus design sections)

These constructions appear **zero** times in the 6 corpus design sections:

- ❌ "We run regressions of X on Y" — corpus says "estimate" or "regress X on Y"
- ❌ "We test using a large sample" — sample size is given as a number, not a vague claim
- ❌ "We perform robustness checks" without naming them
- ❌ Listing every robustness check up front in the design section — robustness is deferred
- ❌ "We use a fancy / sophisticated / advanced method" — no self-praise of method
- ❌ "Our results are statistically and economically significant" in the design section — significance claims belong in results
- ❌ "We hand-collected a unique dataset" — corpus says "We hand-collect [specific items] from [specific source]"
- ❌ "Our identification strategy is..." as a topic sentence — corpus describes the strategy via the regulatory event or rotation, never in the abstract
- ❌ "Show that" / "demonstrate that" / "prove" — banned across all sections (see intro_patterns.md)
- ❌ Defining a control variable in the body without an Appendix definition
- ❌ Mixing model presentation and results (i.e., reporting coefficients in §3) — coefficients always go in §4 results
- ❌ Saying "Following prior literature, we control for [list]" without naming a specific paper

---

## 13. Annotated example: DeFond et al. 2024 (24-DLWW) §3 Data and Research Design

This is the **single most useful template** for a China audit paper studying an auditor trait or auditor connection that affects audit quality.

### Move-by-move annotation

| Block | Lines | Move |
|---|---|---|
| §3 heading | 253 | "3. Data and research design" — explicitly names both |
| §3.1 sub-heading | 254 | "3.1. Research design" — note: design comes BEFORE data here, an inversion of the modal Variant A. This choice signals that the dependent variable (FinIrreg) and the model spec are the load-bearing pieces. |
| ¶1 (DV introduction) | 255-262 | "Following [Author Year], we proxy for audit quality using [construct], which equal [definition]." → Defense paragraph that begins "Financial irregularities are an appealing proxy for audit quality because..." |
| ¶2 (DV data sources) | 263-267 | "We manually collect restatement data from..." + "We manually obtain data on enforcement actions by the CSRC." + "Consistent with [Author Year], we only retain enforcement actions related to [scope]." (with footnote on robustness to disaggregation) |
| ¶3 (IV introduction) | 268-272 | "Our primary independent variable of interest is..." → "Based on prior research [citation chain] and the strong government involvement in China [citation], we measure local networks using a combination of (1) business networks, and (2) government networks, based on school and work ties within each network." |
| ¶4 (IV step 1: business network) | 273-283 | "We begin by measuring business networks (Network(Bus)), which equal one if [precise threshold rule]" → "We measure social ties using school and work ties." → defines school tie + work tie + exclusion rule (focal-client ties excluded but used as control) |
| ¶5 (IV step 2: political network) | 284-289 | "We then measure local political networks (Network(Gov))..." — symmetric structure to ¶4 |
| ¶6 (IV step 3: combined) | 290-291 | "We then compute our network measure (Network), which equals the sum of [components], divided by two." — single sentence aggregating |
| ¶7 (model presentation) | 292-313 | "We test our hypothesis by estimating the following regression: [Eq. 1]. If auditors with more extensive social networks... we should find a negative coefficient on Network. We use a linear probability model to estimate Equation (1) because it includes several fixed effects (Angrist and Pischke, 2008), although our results are robust to using a logit model." |
| ¶8 (controls — audit firm) | 313-315 | "We control for the following audit firm-level characteristics, where all variables are defined in Appendix 1: Big 4 auditor (BigN), audit firm industry specialization (FirmIndSpec) and the audit firm's connection with the IPO committee (IPOCommittee)." |
| ¶8 (controls — auditor) | 315-320 | "We control for the following individual auditor characteristics: [11 controls each with single-word gloss]" |
| ¶8 (controls — client) | 320-323 | "We control for the following client characteristics: [13 controls each with single-word gloss]" |
| ¶9 (FE + clustering) | 324-326 | "We also include province, industry, and year fixed effects. Industry classifications are from the CSRC industry classification scheme... Standard errors are clustered by audit firm." (footnote 17 promises robustness to alternative clustering) |
| §3.2 (data) | 327-... | "Our sample covers 2005 to 2018. We begin in 2005 because [reason], and we end in 2018 to avoid [reason]." → CSMAR data → sample selection waterfall in prose: "From the 31,879 company-year observations of non-financial A-share companies in CSMAR, we exclude 9249 observations with missing data on auditors; and 1852 observations with missing data for variables used in Equation (1). This leaves a sample of 20,778 firm-year observations, comprising 3048 unique client companies and 4089 unique engagement auditors." |
| ¶ (institutional explanation) | 333-336 | "Audit reports in China are signed by two auditors, with one signature above the other, where the top signature is from the auditor who performs the review work, and the bottom signature is from the auditor who is responsible for the fieldwork (He et al. 2017, 2018; Lennox et al., 2014)." |
| ¶ (data assembly) | 337-341 | "We hand-collect the engagement auditor's identity from annual reports and obtain education, personal data, and office location from resumes at the Chinese Institute of Certified Public Accountants (CICPA)..." |
| ¶ (Tables 1 + 2 description) | 342-374 | Sample distribution table (Table 1) → descriptive statistics (Table 2) → discussion of construct decomposition (BusOnly, GovOnly, Both) |

**Total length of §3 in 24-DLWW:** approximately 4 single-spaced pages of journal text — a useful length budget.

### Why this is the canonical template

1. DV-defense paragraph structurally separated and unmistakable
2. IV measurement built bottom-up (atom → group → aggregate construct)
3. Model presented with explicit prediction sentence ("we should find a negative coefficient on Network")
4. LPM-vs-logit choice defended with citation
5. Three-tier control structure (audit firm / auditor / client) matches the reader's mental model
6. FE structure stated and clustering choice stated in single sentence each
7. Sample-selection waterfall integrated into prose (not just a table)
8. China-institutional explanation deployed at the precise moment a non-China reader needs it
9. Hand-collection footprint disclosed transparently
10. Construct decomposition (BusOnly, GovOnly, Both) sets up the cross-sectional analyses without spoiling them

---

## 13b. Stage-1 Phase-C pilot digest (13 archival papers; 2026-05-22)

The full annotated row tables for these 13 pilot design sections live as staging files named `<code>_design.md` in the Track B drafts directory (`corpus_inventory/track_b_drafts/`). §13 above keeps the full canonical anchor (24-DLWW); this digest distills the rest — which §3 layout and construction variants are reusable. (3 pilot papers — 23-ACN, 20-WY, 16-DLLN — are omitted: their section headers were not cleanly detectable for extraction.)

| Code | §3 layout | DV / IV construction | Distinctive design feature |
|---|---|---|---|
| `22-LNS` | Setup-first (canonical) | DV + baseline equation first | Controls in 4 categorical blocks (client / office / economic-bonding / city-labor) — the reference control-tiering |
| `23-ZBLM` | Setup-first | Functional baseline equation first; DV triad (process + output) | IV continuous then partitioned into indicators for skewness + entropy balancing; grouped controls |
| `22-FW` | DV-first | Attention proxy built bottom-up from raw server logs | Controls in 4 categorical blocks (tax-avoidance / firm / ...); heavy measurement-validity documentation |
| `19-JWW` | Specification-first | Three-proxy DV; bottom-up IV | DV-defense paragraph that RULES OUT alternatives (restatements / GC / fees / earnings-benchmarks) on sample-size + data + conceptual grounds |
| `19-BGH` | Specification-first | Big 4-restricted; IV via geographic APIs + ellipsoidal distance | Baseline equation early; dual DV (abnormal accruals + restatements) |
| `23-PSZ` | Specification-first | Single numbered equation; treatment at city-year level | Cleanly separates baseline from identification; states city-level clustering in §3; three AQ proxies |
| `24-DGZZ` | Specification-first | Policy shock + IV first; RSINDEX from 4 legal barriers (0-4) | Sample waterfall table; stacked-DiD framework introduced as the IV (the identification battery still belongs in §4) |
| `19-Aob` | Setup-first | Multi-proxy DV (modified Jones, Dechow-Dichev, scaled accruals) + binary (restatement, GC) | Per-DV defense; subsample restrictions (e.g. distressed firms for going concern) |
| `20-CKMS` | Setup-first | IV bottom-up (misconduct disclosures -> binary -> BD-year average) | Institutional-context + data-provenance heavy; granular IV construction defended by prior literature |
| `22-CHLP` | Setup-first | Manual alumni-record extraction IV | Front-loads data provenance; explicit 2004 start-date justification (market development) |
| `22-Dug` | Exposure / instrument-first | Bottom-up IV (charity revenue thresholds -> state-type-year exposure share); simulated instrument | Traditional covariate controls deliberately ABSENT — the instrument / institutional design carries identification |
| `22-FHKF` | Setup-first | Bottom-up focal AI measure; DVs (restatements, fees) appear in the descriptive block | Data-provenance + construct-validation heavy; compressed DV defense |
| `24-Chen` | Setup-first | IV bottom-up (employee lawsuits, DB-filtered, court-docket-validated); web-scraped DV | Dedicated defense for the web-scraped incoming-auditor-quality DV |

### New reusable variants surfaced by the pilot (n=13)

1. **The two layout families hold and re-balance.** Setup-first (sample / data / measures before the model) is the modal pilot layout (~7/13: 19-Aob, 20-CKMS, 22-CHLP, 22-FHKF, 22-LNS, 23-ZBLM, 24-Chen); specification-first (numbered equation early) is the strong minority (4/13: 19-BGH, 19-JWW, 23-PSZ, 24-DGZZ); DV-first (22-FW) and exposure/instrument-first (22-Dug) are edge variants. Default to setup-first; use specification-first when a clean shock or equation should lead.
2. **The DV-defense can RULE OUT, not just defend.** 19-JWW's defense paragraph explicitly rejects restatements / going-concern / fees / earnings-benchmarks (sample-size + data + conceptual reasons) before adopting its three accrual proxies. A multi-proxy DV triad with per-proxy defense is the corpus norm (19-Aob, 23-ZBLM).
3. **Controls are tiered into categorical blocks, not a flat list.** 22-LNS (client / office / economic-bonding / city-labor), 22-FW (tax / firm / ...), 23-ZBLM (grouped) name 3-4 control groups. A flat control list is the single most common Dimension-1 miss in a thin draft.
4. **IV is built bottom-up almost universally** (raw source -> coded indicator -> aggregated): server logs (22-FW), regulatory disclosures (20-CKMS), alumni records (22-CHLP), court-validated lawsuits (24-Chen), a legal-barrier index (24-DGZZ).
5. **The IV construction MAY introduce a shock/instrument; the identification battery still defers to §4.** 24-DGZZ (stacked DiD), 22-Dug (simulated instrument), and 23-PSZ (city-year treatment) introduce the source of variation in §3 as part of building the IV, but the falsification / placebo / FE-escalation rhetoric stays in §4 (the skill's deferral rule).
6. **Controls may be deliberately absent** when an instrument or institutional design carries identification (22-Dug) — but say so explicitly; do not silently omit them.

### Drafting retrieval guide

| If your §3 has... | Retrieve |
|---|---|
| the canonical setup-first layout + categorical control blocks | `22-LNS` or `24-DLWW` (anchor, §13) |
| a clean shock / equation that should lead | `23-PSZ` or `24-DGZZ` (specification-first) |
| a multi-proxy DV needing per-proxy defense | `19-JWW`, `19-Aob`, or `23-ZBLM` |
| a novel hand-built / scraped IV (bottom-up construction) | `22-FW`, `20-CKMS`, `22-CHLP`, or `24-Chen` |
| an instrument / exposure design with few covariates | `22-Dug` |
| entropy balancing / continuous-IV partition | `23-ZBLM` |

---

## 14. Self-audit checklist (15 items)

Before submitting the design section, verify each item:

- [ ] Section opens with DV definition, citing the prior paper that established the DV
- [ ] DV-defense paragraph (1-3 sentences) explains why DV is preferable to alternatives
- [ ] Novel IV (if any) is built bottom-up, with each construction step a separate sentence
- [ ] At least one prior validation citation appears for each novel measure
- [ ] At least one acknowledged limitation of the IV measurement appears, with direction-of-bias argument
- [ ] Equation is numbered (always (1) for the focal model)
- [ ] Equation is followed by a sign-prediction sentence ("we expect/predict β1 to be...")
- [ ] LPM-vs-logit choice is defended (Angrist-Pischke 2008 cite if LPM, incidental-parameter cite if OLS over logit)
- [ ] Controls are organized into 2-4 categorical groups (audit firm / office / partner / client), not a flat list
- [ ] Each control has a brief gloss in body; full definitions in Appendix
- [ ] Fixed effects choice is named in single sentence with citation justification (Gormley-Matsa 2014 standard)
- [ ] Standard error clustering choice is named with Petersen 2009 cite; alternative clustering robustness in footnote
- [ ] Sample period: explicit start year + end year + reason for each
- [ ] Sample selection: vertical waterfall in Table, prose narration in body, final-sample sentence with cluster counts
- [ ] No identification machinery (rotation, shocks, falsification) is fully described in §3 — preview only; full development in results section
- [ ] No coefficient values reported in design section (those go in §4 results)
- [ ] Hand-collection footprint disclosed transparently with primary source named
- [ ] If China data: signer-role explanation appears with He et al. 2017/2018 + Lennox et al. 2014 cites
- [ ] If China data: industry classification scheme named (CSRC) with prior-paper cite
- [ ] Lagged-IV justification appears if IV is plausibly endogenous (16-DLZ template)
- [ ] No banned verbs ("show that", "prove", "demonstrate") and no banned patterns (sophisticated method self-praise, every-robustness-check listing)
- [ ] Design section length: 3-5 pages of journal text (not 8+)

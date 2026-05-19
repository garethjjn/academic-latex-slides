# Audit-Paper Robustness / Additional Analyses: The DeFond Standard Battery

**Source corpus.** Extracted from the robustness, additional-analyses, sensitivity, cross-sectional, and identification sections of 6 empirical audit papers:

- DeFond, Hung, Trezevant 2007 JAE — `07-DHT` (cross-country investor protection × earnings announcement informativeness)
- DeFond, Lim, Zang 2016 TAR — `16-DLZ` (client conservatism → audit fees / GCO / resignation)
- DeFond, Li, Wong, Wu 2024 JAE — `24-DLWW` (auditor social network → financial irregularities) ★ template paper
- Dekeyser, He, Xiao, Zuo 2024 JAE — `24-DHXZ` (auditor industry range → audit adjustments)
- DeFond, Qi, Si, Zhang 2025 JAE — `25-DQSZ` (signatory auditor tax expertise → tax aggressiveness) ★ has explicit "First...Sixth" structure
- Khurana, Li, Yeung, Yu 2026 JAE — `26-KLYY` (audit partner cultural trust → going concern)

**Section structure across corpus (heading conventions).** The 6 papers split out the post-main-results material in 4 different ways. Pattern names you will use:

| Paper | Section names used | Total post-results sections |
|---|---|---|
| 07-DHT | "5. Additional analysis" + "6. Robustness tests" | 2 separate |
| 16-DLZ | "V. SENSITIVITY TESTS" + "VI. TESTS WITH UNCONDITIONAL CONSERVATISM" | 1 omnibus + 1 extension |
| 24-DLWW | "5. Additional analysis" + "6. Robustness tests" | 2 separate (+ Section 4.3 falsification embedded in main) |
| 24-DHXZ | "6. Cross-sectional analyses" + "7. Supplementary analyses" | 2 separate (+ Section 5.3 endogenous matching embedded in main) |
| 25-DQSZ | "4.2 Identification strategies" (in main) + "5. Additional analyses (untabulated)" | 1 in-main identification block + 1 untabulated tail |
| 26-KLYY | "4.2 Cross-sectional tests" + "4.3 Financial reporting cost" + "4.4 Additional analyses" | 1 numbered subsection inside Section 4 |

**Key takeaway.** The label is fungible — "Robustness", "Sensitivity", "Additional", "Supplementary", "Identification" all overlap. What matters is the **functional taxonomy** below, not the heading you choose.

---

## 1. The DeFond Standard Battery — Canonical Catalog

Each test below appears in **3 or more** of the 6 corpus papers. This catalog is the highest-value content of this skill: when reviewers say "we want to see standard robustness," this is what they mean.

### 1.1 Falsification / Placebo with Spatially or Functionally Unrelated Variant ★★★★

**Frequency: 5 of 6** (07-DHT, 24-DLWW, 25-DQSZ, 24-DHXZ, 26-KLYY-style alternatives)

**What it tests.** Replace the focal independent variable with a "should-not-matter" version that is constructed identically but lies outside the proposed mechanism's reach. If the placebo coefficient is significant, the design has a confound; if insignificant, the mechanism is sharp.

**Verbatim openings:**
- "We also perform falsification tests that repeat our analysis in Table 3 after including placebo measures of the auditors' social networks. We perform this test using two measures." (24-DLWW, §4.3)
- "Columns (3) and (4) of Panel B report placebo tests that replace auditor tax expertise with industry expertise." (25-DQSZ, §4.2.2)
- "We also perform a placebo test by replacing auditor tax expertise with industry expertise and find that industry expertise has no effect on tax aggressiveness." (25-DQSZ, intro)
- "As a placebo test, we replace tax-related audit adjustments (TAXADJ) with non-tax-related audit adjustments (NONTAXADJ) in [the specification]." (25-DQSZ, §4.2.4)

**When to use.** Whenever your treatment has a natural geographic, temporal, or functional analogue that *should not* operate through the proposed channel. (E.g., for a within-province auditor network → use neighboring-province network as placebo.)

**When to skip.** If no honest "should-not-matter" version exists. Do NOT invent a placebo that is mechanically guaranteed to be null.

---

### 1.2 Cross-Sectional / Heterogeneity Partition ★★★★

**Frequency: 6 of 6** (universal; this is non-negotiable in modern JAE/TAR audit papers)

**What it tests.** Predict ex ante that the effect is stronger in subsample S1 than in S2. If S1>S2, this corroborates the proposed mechanism by showing the effect varies in a theory-consistent direction. (Distinct from simple subsample re-estimation: here the prediction is about the *interaction* sign, not just sample size.)

**Verbatim openings:**
- "We conjecture that the association between Network and FinIrreg is stronger for clients that are more likely to use relational contracts, because the benefits of social connections should be greater. We explore this using two tests." (24-DLWW, §5.1)
- "This section examines two cross-sectional variables that could moderate the effect of auditor tax expertise on tax aggressiveness: client ownership structure and auditor industry specialization." (25-DQSZ, §4.2.5)
- "The importance of a partner's industry range depends on the complexity of the environment as complexity tends to reduce the 'validity' of the environment (Epstein, 2019; Kahneman and Klein, 2009). The complexity of auditing increases for larger clients..." (24-DHXZ, §6.2)
- "Conditional on our first prediction, we examine whether the [trust] effect is concentrated in settings where audit partners face greater litigation risk..." (26-KLYY, §4.2.2)

**Standard internal structure of a cross-sectional test (4 sentences):**
1. Theory sentence: "We expect [interaction] because [mechanism]."
2. Measurement sentence: "We capture [partition variable] using [definition / source]."
3. Specification sentence: "We test this by estimating [equation] where X equals [partition variable]."
4. Result + theory link: "Consistent with our prediction, the coefficient on [Treatment × Partition] is [sign and significance]." Add a "consistent with" theory restatement.

**When to use.** Always. If you can think of zero ex-ante predictions about heterogeneity, your theory is too thin to be a JAE paper.

**When to skip.** Never skip. (You may run only 1-2 cross-sectional tests instead of 4-5 if your sample is small, but at least one is mandatory.)

---

### 1.3 Quasi-Experimental Identification — Regulatory Shock or Mandatory Rotation ★★★★

**Frequency: 4 of 6** (24-DLWW, 25-DQSZ, 16-DLZ partially, 26-KLYY via partner switch)

**What it tests.** A pre-specified, plausibly exogenous event that changes the treatment exposure for some firms but not others. Standard DiD or event-study form.

**Verbatim openings:**
- "Our first test exploits regulations in China that require signatory auditors to rotate every five years." (25-DQSZ, intro to §4.2)
- "We exploit a regulatory shock that disrupts the auditor's business connections..." (24-DLWW, intro)
- "Lastly, we explore the effects of a regulation that resulted in the resignation of many independent directors, thereby disrupting auditors' networks. On October 19, 2013, the Organization Department of the Communist Party of China's Regulation 18 ('Reg. 18') banned government and university officials..." (24-DLWW, §5.3)
- "Our second test examines the effects of a regulatory shock that reduces corporate tax rates, thereby weakening the incentives to engage in aggressive tax planning. ... Effective January 1, 2008, China replaced two separate income tax laws..." (25-DQSZ, §4.2.2)
- "To investigate this empirically, we identify audit partner switches that occurred in 2018, which permit a two-year pre- and post-period in our difference-in-differences (DID) framework." (26-KLYY, §4.4.3)

**Standard ingredients (all required):**
1. Name and date the policy (e.g., "Reg. 18, October 19, 2013").
2. Identify the treated/control split clearly.
3. Restrict the event window symmetrically (e.g., T-2 to T+2).
4. **Verify parallel trends** in a separate panel/figure ("In Panel A of Appendix B we verify the validity of parallel trends assumption for the auditor rotation analysis." — 25-DQSZ).
5. Show coefficients on T-1, T, T+1, T+2 separately if window is wide enough.
6. Report a sensitivity test that drops confounded observations (e.g., 24-DLWW drops provinces with concurrent corruption-related dismissals).

**Forbidden dishonesty:** Do not call something a "regulatory shock" if firms anticipated it (e.g., long-pre-announced reforms). Do not use the word "exogenous" unless your shock is genuinely orthogonal to firm/auditor selection.

**When to use.** Whenever your setting offers a plausibly exogenous event. Mandatory partner rotation in China is the most common; SOX subevents, IFRS adoption, AS5/AS18, China's 2017 audit centralization pilot, anti-corruption purges, and PCAOB inspection regime changes all qualify.

---

### 1.4 Alternative Measure of the Independent Variable ★★★★

**Frequency: 6 of 6** (universal)

**What it tests.** Re-estimate using a different proxy for the focal variable. If results hold across measures, construct validity rises.

**Verbatim openings:**
- "Goldman et al. (2022) measures tax expertise at the audit office level using TAXSCORE... we also perform an analysis that includes TAXSCORE along with TAX_EXP." (25-DQSZ, §5.3.1)
- "Table 9, Panel A, repeats our hypothesis test using two alternative proxies for auditors' geographic proximity to their clients. The first captures whether the auditor's office is in the same city as the client's headquarters (DeFond et al., 2018); the second captures whether the auditor's office is within 100 km of the client's headquarters." (24-DLWW, §6.1)
- "To test whether our measure of audit partners' cultural trust, PartnerTrust, is robust to using alternative name classification techniques, we use four complementary approaches and report the regression results in Panels A – D of Table A2 of the Online Appendix." (26-KLYY, §4.4.5)
- "Because the results with the two proxies for conservatism are similar, we present the results based on the CON_KW for parsimony." (16-DLZ, §V opening)

**Pattern.** Modern papers often run 2-4 alternative measures. The common framing: "Our results are not sensitive to using [list of alternative measures]."

**When to use.** Always. At least one alternative measure of the focal variable is mandatory.

---

### 1.5 Alternative Measure of the Dependent Variable ★★★

**Frequency: 5 of 6** (07-DHT swaps abnormal return variance for trading volume; 16-DLZ uses CON_NOPA alongside CON_KW; 25-DQSZ uses ETR alongside Cash ETR; 26-KLYY uses |TotalAccrual|, BeatBenchmark, BigRRestatement; 24-DHXZ supplements audit adjustments with restatements)

**What it tests.** Replace the main outcome with a related construct. Distinguishes whether the result is about the latent construct or about a quirk of the specific proxy.

**Verbatim openings:**
- "Another commonly used measure to assess the information content of earnings announcements is abnormal trading volume (Beaver, 1968). Thus, we repeat our analysis in Table 4, Panel B after replacing abnormal return variance with abnormal trading volume..." (07-DHT, §5.3)
- "While we use current ETR in our main analysis, we also use ETR as an alternative measure and find that our results in Table 3 remain unchanged." (25-DQSZ, §5.3.2)
- "To further understand the effects of auditor industry range, we use financial misstatements (Misstatement) as the dependent variable." (24-DHXZ, §7.2)

**When to use.** Whenever a credible alternative DV exists. For audit-quality papers: if main DV is restatements, a robustness DV could be discretionary accruals or audit fees; if main DV is GCO, alternative is dismissal.

---

### 1.6 Fixed-Effects Saturation ★★★★

**Frequency: 5 of 6** (24-DLWW, 25-DQSZ, 26-KLYY, 24-DHXZ, 16-DLZ; 07-DHT uses a different country-level FE structure)

**What it tests.** Add increasingly stringent fixed effects (industry → year → industry-year → firm → auditor → firm-year) to absorb potential unobserved heterogeneity. If the coefficient survives client/firm fixed effects, the result is identified off within-firm variation.

**Verbatim openings:**
- "Our primary results are robust to including audit firm, client, signatory auditor, and province-year fixed effects." (24-DLWW, intro)
- "We repeat our primary analysis after controlling for client company-fixed effects, which effectively examines the association between tax-expert signatory auditors and tax aggressiveness within each client, thus controlling for differences across clients that may explain their tax aggressiveness." (25-DQSZ, §4.2.6)
- "In Panel B, we include client fixed effects in the logistic model. In Panel C, we include client fixed effects and pre-audit accruals in the logistic model. In Panel D, we include client fixed effects and pre-audit discretionary accruals in the logistic model." (24-DHXZ, Table 6)

**Standard FE ladder for an audit paper using Chinese signatory data:**
1. Industry × Year FE (always start here)
2. + Province FE
3. + Audit-firm FE
4. + Auditor FE (engagement partner)
5. + Province × Year FE (replace industry+year+province above)
6. + Client-firm FE (the most demanding; only within-client variation in the IV is used)

**Critical reporting move (24-DLWW Table 6):** Report "Variation absorbed by fixed effects" and "VIF for [main IV]" at the bottom of the FE-saturation table. This anticipates the reviewer's "are you sure there's any variation left?" question.

**When to use.** Always include at least one column of the main table with strong FE (industry × year + province minimum). A separate FE-saturation panel/table is standard.

---

### 1.7 Subsample Restrictions ★★★★

**Frequency: 6 of 6** (universal — different cuts in different papers)

**What it tests.** Re-estimate on subsamples that exclude observations potentially driving the result, or restrict to specific institutional subsets where the prediction should be sharpest.

**Standard cuts (with verbatim opening):**

| Cut | Frequency | Verbatim opening |
|---|---|---|
| Big N vs. non-Big N | 4/6 | "We repeat our analysis separately for Big N and non-Big N auditor clients." (16-DLZ, Panel F) |
| SOE vs. private | 3/6 | "Because SOEs and non-SOEs have different stakeholders and governance practices, they have different incentives with regard to tax planning..." (25-DQSZ) |
| Drop dominant country/region | 3/6 | "Because the large weight on the US or Japan might drive the results in our firm-level hypothesis tests, we repeat our full-model regression... after excluding US and Japanese firms sequentially from our sample." (07-DHT, §6.1) |
| Drop ambiguous-treatment observations | 4/6 | "First, we drop all years in which the engagement auditor in year T differs from the engagement auditor in year T-1. Second, we drop all observations in which ClientTies = 1." (24-DLWW, §6.2) |
| Drop influential / outlier obs | 3/6 | "To examine the potential effects of influential observations, we rerun our full-model regression... after dropping observations with absolute values of R-student statistics exceeding three." (07-DHT, §6.4) |
| Pre/Post structural break | 3/6 | "Because SOX requires audit committees to be fully independent and to have at least one financial expert, we can partially control for the effect of audit committee attributes by conducting our analysis during the post-SOX period, when the attributes are more homogenous." (16-DLZ) |
| Restrict to first-time event | 2/6 | "First, we restrict our analysis to observations where the client received a clean opinion in the prior year. This filter limits our analysis to first-time going concern opinions..." (26-KLYY, §4.4.6) |
| Drop measurement-error subgroup | 2/6 | "PartnerTrust may contain measurement error for female audit partners due to the convention of wives taking on their husbands' surnames... To address this concern, we exclude female audit partners from our sample and re-run our regressions." (26-KLYY, §4.4.6) |

**When to use.** Always include 2-3 subsample cuts. Big4/non-Big4 and SOE/private are the modal "free shots."

---

### 1.8 Controlling for Plausible Omitted Correlated Variable ★★★★

**Frequency: 5 of 6**

**What it tests.** Add a control variable that would be a "smoking gun" omitted variable if your result actually reflected its effect.

**Verbatim openings:**
- "To ensure that governance is not an omitted correlated variable, we repeat our tests after including several governance variables (following Lara et al. 2009): the G-index (Gindex)... whether the CEO is chairman (Duality), proportion of executives on the board (Executive), and the number of board meetings during the year (Meeting)." (16-DLZ)
- "Prior studies document that discretionary accruals (DA) are associated with auditor litigation, audit fees, and GCOs. Because DA potentially reflect conservatism, we repeat our tests after controlling for signed, absolute value, and income-increasing DA." (16-DLZ)
- "Prior literature finds that various individual auditor characteristics affect audit quality, including graduate degrees, accounting major and education cohort (Gul et al., 2013). After adding these variables to our main analysis in Table 3, we find that the coefficient on TAX_EXP remains significantly negative (positive)..." (25-DQSZ, §5.3.4)
- "A factor that may influence our findings is capital market development. ... We therefore repeat our full-model regression... after adding a variable that captures capital market development." (07-DHT, §6.2)

**When to use.** Always. Identify the 1-2 most likely "but isn't this just X?" alternatives and pre-empt them with a controls-added test.

---

### 1.9 Channel / Mechanism Test ★★★

**Frequency: 4 of 6**

**What it tests.** Decompose the dependent variable or insert a mediator to show the result operates through the proposed channel rather than through a substitute.

**Verbatim openings:**
- "Our fourth test finds that clients of tax-expert auditors report higher taxable income but not lower pre-tax book income, consistent with tax-expert auditors lowering BTDs by reducing tax aggressiveness rather than by reducing earnings management. We also find that tax-expert auditors are associated with a higher likelihood of year-end audit adjustments that increase taxable income, but not with audit adjustments that affect non-taxable income, consistent with year-end adjustments being a channel..." (25-DQSZ, §4.2.4)
- "Our third test finds that tax-expert auditors attenuate the positive association between tax-aggressiveness and tax-related misstatements." (25-DQSZ, intro)

**When to use.** Whenever you can split your DV into a treated component and a placebo component (here: tax-related vs non-tax-related restatements; here: within-province vs out-of-province network connections).

---

### 1.10 Joint / System Estimation ★★

**Frequency: 2 of 6**

**What it tests.** Re-estimate the main equation jointly with a second equation to address the concern that the dependent variables are determined together.

**Verbatim opening:**
- "Because it is possible that auditors use a combined strategy in response to client conservatism, we jointly estimate all three models (Models (1) through (3), above) using a system of equations. We perform this test with all common observations (n = 17,010) without restrictions for distress or auditor switches." (16-DLZ)

**When to use.** When you have multiple correlated DVs (e.g., audit fee + GCO + resignation) and a reviewer might worry about endogenous selection across them.

---

### 1.11 PSM (Propensity Score Matching) — Use With Defensive Framing ★★

**Frequency: 1 of 6 explicitly executed (24-DHXZ); flagged in 14-DZ review as problematic**

**Critical context.** Post-Shipman et al. (2017) and Defond et al. (2014) and King-Nielsen (2019), JAE/TAR reviewers expect either (a) a brief, hedged defense, or (b) a substitute method (entropy balancing, CEM). The 24-DHXZ paper is the corpus's only explicit user, and even they footnote the controversy:

> "The propensity score matching method used by Minutti-Meza (2013) is not without controversy (King and Nielsen, 2019; Shipman et al., 2017)." (24-DHXZ, fn 7)

**Verbatim opening (24-DHXZ §5.3.1):**
> "To address concerns about potential endogenous matching between auditors and clients, we employ a propensity score matching approach as suggested by Minutti-Meza (2013). Specifically, for each continuous industry range proxy, we construct a variable D_Range, equal to one for auditors with a wide industry range, i.e., the value of Range for that auditor is above the yearly median. We then estimate the propensity score by regressing D_Range on all control variables from our baseline model using a probit regression. We match clients based on their propensity score, within common support and without replacement, using a caliper distance of 0.03."

**Defensive framing rules:**
1. **Never lead the robustness section with PSM.** Place it after FE saturation and DiD.
2. **Footnote the controversy.** Cite Shipman et al. 2017 and King-Nielsen 2019.
3. **Specify caliper, replacement, common support** explicitly. (24-DHXZ uses 0.03 caliper, no replacement, common support.)
4. **Pair with a balance table.** Show pre-match vs post-match standardized differences.
5. **Better alternative:** Entropy balancing (Hainmueller 2012, McMullin & Schonberger 2020) — re-weights rather than discards observations and avoids King-Nielsen's "model-dependence" critique. None of the 6 corpus papers use it, but post-2024 referees increasingly request it.

**When to use.** Only when (a) reviewer explicitly asks, OR (b) your treatment is a discrete auditor/client choice that is plausibly endogenous to observable client characteristics. Never as the primary identification.

**When to skip.** If you have a regulatory shock + FE saturation, you do not need PSM. Save the table space.

---

### 1.12 Influential-Observations / Outlier Checks ★★

**Frequency: 3 of 6**

**Verbatim opening:**
- "To examine the potential effects of influential observations, we rerun our full-model regression (Model 2) in Table 4, Panel B after dropping observations with absolute values of R-student statistics exceeding three." (07-DHT, §6.4)
- "All continuous variables are winsorized at the 1% and 99% levels and standardized." (26-KLYY, table notes — winsorization done up-front in main spec)

**When to use.** Brief paragraph at the end of robustness section stating winsorization at 1%/99% is the modern standard; outlier-deletion sensitivity is optional.

---

### 1.13 Standard-Error / Inference Robustness ★★

**Frequency: 4 of 6**

**Verbatim opening:**
- "Third, we re-estimate standard errors using the bootstrap method with 1000 replications (e.g., Gutierrez et al., 2018; Sherwood, 2025), and obtain results consistent with those based on conventional standard errors." (26-KLYY, §4.3)
- "To control for potential time-series correlation among our regression error terms, we repeat our full-model regression (Model 2) in Table 4, Panel B after including only one randomly selected annual observation for each firm in our analysis." (07-DHT, §6.3)
- "Standard errors are clustered at the client level." (26-KLYY, table notes)

**When to use.** If your default clustering choice is debatable (e.g., client vs. auditor vs. firm-year), include one column or panel with the alternative.

---

### 1.14 Power Analysis / Confidence-Interval Sharpening for Null Results ★

**Frequency: 1 of 6, but rising rapidly post-2024 (e.g., Cunningham et al. 2019)**

**Verbatim opening (26-KLYY §4.3):**
> "Because insignificant coefficient estimates can reflect either a genuine absence of an association or a lack of statistical power, we take three additional steps in interpreting the results in columns (2) and (3). First, we compute the 95% confidence intervals for the insignificant PartnerTrust coefficients and verify that the potential effect sizes do not exceed one-third of one standard deviation in the respective dependent variables (e.g., Cunningham et al., 2019). Second, we perform a power analysis (Cohen, 1988) and confirm that our sample size is large enough to detect meaningful effects, if present."

**When to use.** Whenever your story REQUIRES a null result on a secondary outcome. (E.g., "trust reduces Type I errors but should NOT change Type II errors" — the null on Type II must be defended with CI + power, not just dismissed.)

---

## 2. "Robustness" vs "Additional Analyses" — The Distinction

Empirically the distinction in the corpus is **fuzzy** but the modal usage is:

| Section name | What goes here | Example |
|---|---|---|
| **Robustness / Sensitivity** | Tests of the SAME hypothesis under alternative specifications. Goal: show the main result is not artifact of a specification choice. | Alternative DV measure, alternative IV measure, alternative FE, drop subsamples, cluster differently. |
| **Additional Analyses** | NEW questions that extend, validate, or complicate the main hypothesis. Goal: show the result has structure consistent with the proposed mechanism. | Cross-sectional partitions, channel/mechanism tests, novel DV (e.g., auditor dismissals), validation tests of the IV measure. |
| **Identification** (in main results) | Causal inference moves embedded in the main results section. Goal: rule out reverse causality and selection. | DiD around a regulatory shock, mandatory rotation event study, instrument. |

**Verbatim distinction in 25-DQSZ:**
- §4.2 "Identification strategies" (in main results section): mandatory rotation, tax rate shock, tax-related misstatement decomposition, channel test, cross-sectional, client FE — these are the SIX numbered tests.
- §5 "Additional analyses (untabulated)": reconciliation with prior literature, robustness tests with alternative measures.

**Verbatim distinction in 24-DLWW:**
- §5 "Additional analysis": cross-sectional (relationship-based contracting), trends (high-speed rail, online sales), and Reg. 18 disruption — these EXTEND the hypothesis to specific settings.
- §6 "Robustness tests": alternative proxies, alternative samples, high-incentive periods — these are SAME-hypothesis sensitivity.

**Verbatim distinction in 24-DHXZ:**
- §6 "Cross-sectional analyses": economic co-movement, complexity, M&A activity, experience — extending the hypothesis.
- §7 "Supplementary analyses": portfolio specialization, financial misstatements — different angle on same construct.
- §5.3 (embedded in main results): "Mitigating concerns about endogenous matching" — PSM. (Note: identification embedded in main, not in robustness.)

**Practical rule for skill users.**
- If the test answers "is my main result real?" → **Robustness**.
- If the test answers "does the effect look the way the theory predicts?" → **Additional Analyses**.
- If the test addresses reverse causality / selection → **Identification** (often inside main results, sometimes in additional).

When in doubt, default to two sections: "5. Additional Analyses" (cross-sectional + mechanism + new DV) and "6. Robustness Tests" (alt measures + alt samples + alt FE + alt SE). This is the modal JAE structure (24-DLWW, 07-DHT).

---

## 3. Cross-Sectional / Heterogeneity Test Presentation Format

Standard format observed across 24-DLWW, 24-DHXZ, 25-DQSZ, 26-KLYY:

### 3.1 The 4-Sentence Setup

```
[1. Theory.] Because [mechanism], we expect that the effect of [Treatment] on
[Outcome] is stronger when [Partition variable] is [high/low].

[2. Measurement.] We capture this by [defining Partition variable]. Specifically,
[Partition] equals one if [criterion], and zero otherwise. We obtain [data source].

[3. Specification.] We test this by estimating:
   Y_it = α + β1 × Treatment_it × Partition_it + β2 × Treatment_it
        + β3 × Partition_it + γ × Controls + Fixed Effects + ε_it
We expect the coefficient on Treatment × Partition to be [sign].

[4. Result + theory link.] As predicted, [Table N, Panel A] finds that the
coefficient on Treatment × Partition is [sign] and significant at the [X%] level.
This is consistent with [restate mechanism in plain English].
```

### 3.2 Real Examples

**24-DLWW §5.1 (relationship-based contracting):**
> "We conjecture that the association between Network and FinIrreg is stronger for clients that are more likely to use relational contracts, because the benefits of social connections should be greater. We explore this using two tests.
>
> Our first test follows Li et al. (2020) and creates a variable that captures clients who are more likely to engage in relationship-based contracting (RelationClient). Specifically, RelationClient = 1 if the client satisfies one of the following criteria: (1) related-party transactions with parties in the same province are more than 35 percent of sales; (2)... and zero otherwise. We expect the effects of Network to be stronger when RelationClient = 1.
>
> ...
>
> As predicted, Panel A of Table 7 finds that the coefficient on Network × X is significantly negative when X is captured by RelationClient and is significantly positive when X is captured by HighTrust (at the 10% level). Thus, consistent with our predictions, the effect of the auditor's network is stronger among clients that rely more heavily on relationship-based contracting."

**26-KLYY §4.2.2.1 (litigation risk):**
> "In our first test, we argue that litigation risk will be more salient for an audit partner if there has been a recent lawsuit against an auditor within the client's industry. To test this empirically, we manually review the defendant section of lawsuit complaint files and construct an indicator variable (HighLitigationRisk) that equals one if there was at least one auditor litigation case in the client's industry in the past 3 years, and zero otherwise. We then interact this variable with PartnerTrust and include both the main effect and the interaction term in equations (1)–(3)."

### 3.3 Magnitudes Reporting

If interaction coefficient is significant, **always** translate it into an economic magnitude:
- "An auditor's network effect on financial irregularities is roughly twice as large in relationship-heavy provinces as in low-trust provinces."
- "Moving from the bottom to the top decile of Partition switches the marginal effect of the treatment from X to Y."

Avoid stating "the interaction is significant" without an economic interpretation.

---

## 4. Falsification / Placebo Test Rhetoric

### 4.1 Falsification Setup Formula

```
[1. Theoretical reason placebo should not work.] While we expect [Treatment] to
[affect Y via mechanism M], we do not expect [Placebo] to [affect Y] because
[Placebo lies outside M's reach].

[2. Construction.] We construct [Placebo] using [identical procedure as
Treatment, applied to a different domain].

[3. Test.] We perform falsification tests that repeat our analysis after
[replacing Treatment with Placebo / adding Placebo alongside Treatment].

[4. Result.] As expected, the coefficient on [Placebo] is insignificant. [If
included alongside, also note that Treatment retains significance.] These
results are consistent with [restate mechanism].
```

### 4.2 Verbatim Examples

**24-DLWW §4.3 (out-of-province placebo):**
> "While we expect the auditor's social network within the client's province (Network) to improve the auditor's competency in deterring irregularities, we do not expect the auditor's connections with networks outside of the client's province to deter them. Thus, we perform falsification tests that repeat our analysis in Table 3 after including placebo measures of the auditors' social networks. We perform this test using two measures."

> "The results are shown in Table 5. Columns (1) and (3) replace Network with each placebo. As expected, we find that the coefficients on the placebo measures are insignificant in both regressions. Columns (2) and (4) add the placebo measures to our original regression and find the coefficient on Network continues to be significantly negative at the 5% level and that the coefficients on the placebo measures are again insignificant. These falsification tests are consistent with network connections within the client's province, but not with connections outside of the client's province, improving the auditor's ability to deliver high audit quality."

> "Finding that the coefficient on Network remains significant in Columns (2) and (4) also indicates that the placebo measures are not omitted correlated variables that explain our results."

**25-DQSZ §4.2.2 (industry-expertise placebo):**
> "Columns (3) and (4) of Panel B report placebo tests that replace auditor tax expertise with industry expertise. We regress our tax aggressiveness measures on IND_EXP, POST2008, and IND_EXP × POST2008. Consistent with Table 3, the coefficients on IND_EXP are insignificant. In addition, the coefficients on IND_EXP × POST2008 are also insignificant. However, the coefficients on TAX_EXP are significantly negative in Column (3) and significantly positive in Column (4) (both p<1%), suggesting that our findings in Panel A are due to tax expertise and not industry expertise. This placebo test also provides comfort that our results in Columns (1) and (2) are not spuriously driven by other concurrent changes in 2008."

### 4.3 Two Common Falsification Designs

**Design 1: Spatial placebo.** Take your treatment defined for region/community X, and re-define it for region X' (a different region) where the mechanism does not operate. (Used by 24-DLWW: same-province network vs. neighboring/out-of-province network.)

**Design 2: Functional placebo.** Take your treatment of type T, and replace with treatment of type T' (a related-but-different type) where the mechanism does not operate. (Used by 25-DQSZ: tax expertise vs industry expertise; also used by 25-DQSZ: tax-related vs non-tax-related restatements.)

### 4.4 Forbidden Placebo Moves

- ❌ Don't claim a result as a "placebo" if you know ex ante it should be marginally significant.
- ❌ Don't run 10 placebos and report only the 2 that are insignificant.
- ❌ Don't use "lagged independent variable" as a placebo — it's just a different specification.

---

## 5. Quasi-Experimental Robustness Moves — How to Frame

When a paper exploits a natural experiment, the framing in the robustness section follows a recurring 5-part structure:

```
1. NAME the policy + DATE + ISSUING BODY.
   "On October 19, 2013, the Organization Department of the Communist Party of
    China's Regulation 18 ('Reg. 18') banned government and university officials
    from serving as independent directors..." (24-DLWW)

2. EXPLAIN why it is plausibly exogenous.
   "Unless a client coincidentally changes its tax strategy during the year in
    which the mandatory five-year rotation occurs, it is unlikely that the change
    in the auditor's tax expertise is explained by selection." (25-DQSZ)

3. DEFINE treatment and control groups.
   "Our treatment group is restricted to the auditors in our sample who have
    connections with independent directors who are forced to resign because of
    Reg. 18..." (24-DLWW)

4. RESTRICT the event window symmetrically.
   "We examine a three-year window around the rotation and compare tax
    aggressiveness during the year before the rotation with tax aggressiveness
    during the year of and the year following the rotation." (25-DQSZ)
   "the five-year period surrounding the new regulation, 2012–2016 (T-2 to T+2)" (24-DLWW)

5. VERIFY parallel trends.
   "In Panel A of Appendix B we verify the validity of parallel trends assumption
    for the auditor rotation analysis." (25-DQSZ)
```

### 5.1 Common Quasi-Experiments in Audit Research

| Shock | Used in corpus | Useful for |
|---|---|---|
| Mandatory partner rotation (China, 5-yr cycle) | 25-DQSZ | Almost any partner-trait paper in China |
| Reg. 18 (China, 2013) | 24-DLWW | Auditor-network / political-connection papers |
| 2008 tax-rate cut (China) | 25-DQSZ | Tax-aggressiveness papers |
| SOX § 404 (US) | 16-DLZ partial | Internal control / audit fee papers |
| IFRS adoption | none in corpus | Cross-country accounting quality |
| Auditor exit shocks (Big 5 → 4) | none in corpus | Audit market structure |
| China 2017 audit centralization | none in corpus | Audit-firm management studies |
| Audit partner switches (within firm) | 26-KLYY | Partner-trait papers without an external shock |

### 5.2 Confound-Removal Subtest

After the headline DiD, papers often run a "drop confounded observations" sensitivity:

> "We also perform an analysis after excluding Reg. 18 observations that overlap with political scandals which resulted in the removal of several high-level provincial officials during our sample period. We remove these observations because prior studies find that these high-level political turnovers triggered significant political uncertainty that had the effect of disrupting business contracting." (24-DLWW)

This is the modern referee-savvy way to handle "but couldn't your shock be confounded by [contemporaneous shock Y]?" — explicitly drop Y and re-run.

---

## 6. PSM and Matching Language — Post-Shipman/King-Nielsen Convention

### 6.1 Default Position in Modern JAE

Post-2017 (Shipman, Swanquist, Whited TAR; DeFond et al. 2014 critique; King-Nielsen 2019), the corpus shows the following pattern:

- Only **1 of 6** corpus papers (24-DHXZ) uses PSM as a primary robustness method.
- That paper **footnotes the controversy** rather than ignoring it.
- PSM is placed **after** other identification methods (FE saturation, mechanism tests).
- The implementation is detailed: caliper, replacement rule, common support.

### 6.2 Verbatim Defensive Language

**24-DHXZ §5.3.1 (full verbatim):**
> "5.3. Mitigating concerns about endogenous matching
>
> 5.3.1. Propensity score matching
>
> To address concerns about potential endogenous matching between auditors and clients, we employ a propensity score matching approach as suggested by Minutti-Meza (2013). Specifically, for each continuous industry range proxy, we construct a variable D_Range, equal to one for auditors with a wide industry range, i.e., the value of Range for that auditor is above the yearly median. We then estimate the propensity score by regressing D_Range on all control variables from our baseline model using a probit regression. We match clients based on their propensity score, within common support and without replacement, using a caliper distance of 0.03. This procedure generates three matched samples, one for each industry range variable."

**Footnote 7 of 24-DHXZ:** "The propensity score matching method used by Minutti-Meza (2013) is not without controversy (King and Nielsen, 2019; Shipman et al., 2017)."

### 6.3 14-DZ (DeFond-Zhang Review) Discussion of PSM

While not in the empirical corpus, the DeFond-Zhang 2014 JAE review paper (`14-DZ`) discusses PSM in audit research at length:

> "These techniques [Heckman, DiD, PSM] may partially attenuate [endogeneity], but they cannot eliminate it. Researchers should not overstate the conclusions by claiming to have 'controlled for selection bias'. Further, DeFond et al. (2014) find that Propensity Score Matching is sensitive to research design choices inherent in propensity score matching."

> "DeFond et al. (2014) propose a new technique, Coarsened Exact Matching, which does not suffer from these problems and thus results in higher [matching quality]." (14-DZ p. 1756)

**Implication for skill users:** When PSM is unavoidable, prefer Coarsened Exact Matching (CEM) or Entropy Balancing, and explicitly cite Shipman et al. (2017) + DeFond et al. (2014) in the framing.

### 6.4 What to Write Instead of PSM (Recommended Substitutes)

| Move | When to use | Verbatim model |
|---|---|---|
| **Entropy balancing** | Continuous treatment, want to keep all observations | "Following Hainmueller (2012), we use entropy balancing to re-weight the control sample to match the treated sample on the means and variances of all controls." |
| **Coarsened Exact Matching (CEM)** | Discrete treatment with rich categorical controls | "Following DeFond et al. (2014), we use coarsened exact matching, which does not suffer from the model-dependence problems of PSM (King and Nielsen, 2019)." |
| **Within-firm fixed effects** | Panel data with treatment variation within firm | "We control for client company fixed effects, which effectively examines the association within each client, thus controlling for time-invariant differences across clients." (25-DQSZ) |

---

## 7. Fixed-Effects Saturation Defense — Standard Pattern

### 7.1 The Saturation Table

The modal saturation table runs 4 columns with progressively stronger FE:

```
                                  (1)        (2)        (3)        (4)
Main IV                         Coef***    Coef**     Coef*      Coef*

Province FE                       YES        NO         NO         NO
Industry FE                       YES        YES        NO         NO
Year FE                           YES        NO         YES        NO
Audit Firm FE                     YES        NO         NO         YES
Province-Year FE                  NO         YES        NO         YES
Client Company FE                 NO         NO         YES        YES
Engagement Auditor FE             NO         NO         YES        YES

Variation absorbed by FE         44.0%      7.7%      79.4%      81.2%
VIF for Main IV                  2.03       1.42       6.99       7.94
N                              20,721     20,778    19,519     19,517
Adj R²                          0.068      0.050      0.281      0.289
```

**Critical reporting move:** ALWAYS report the row "Variation absorbed by FE" and "VIF for Main IV" at the bottom. This anticipates the reviewer's question "is there enough within-X variation left to identify your effect?"

### 7.2 Verbatim Lead

**24-DLWW Table 6 caption + body:**
> "We also find that our primary results are robust to including audit firm, client, signatory auditor, and province-year fixed effects."

> "This table presents company-level linear probability regression model results for our primary analysis with different fixed effect structures... Variation absorbed by fixed effects is the adjusted R² from a regression of the independent variable (Network) on the respective fixed effects, and VIF is the variance inflation factor for the independent variable of interest (Network)."

### 7.3 The "Fixed-Effect Survival" Sentence

After reporting the saturated FE column, include a sentence:

> "Our coefficient of interest on [IV] retains its sign and statistical significance after including [strongest FE], indicating that our results are not driven by time-invariant heterogeneity at the [client/auditor/firm] level."

---

## 8. Alternative-Measure Tests — Justification Pattern

### 8.1 Standard Sentence Structure

```
[1. Acknowledge measurement choice in main spec.]
"We use [measure A] in our main analysis because [reason: prior literature /
salience / data availability]."

[2. Identify alternative.]
"However, prior research also uses [measure B] (cite). [Measure B] differs from
[measure A] in that [conceptual difference], and may capture [different aspect
of construct]."

[3. Re-estimate.]
"We repeat our primary analysis using [measure B] and find that our results
remain unchanged. The coefficient on [IV] is [sign and significance]."

[4. (Optional) Defense of original choice.]
"We retain [measure A] in our main analysis because [reason], but the
robustness of our results to [measure B] alleviates concerns about
measurement-error sensitivity."
```

### 8.2 Real Examples

**25-DQSZ §5.3.2:**
> "While we use current ETR in our main analysis, we also use ETR as an alternative measure and find that our results in Table 3 remain unchanged. In addition, Chinese-listed companies are subject to varying applicable tax rates (ATRs) due to various preferential tax policies (Shevlin et al., 2012). Following Tang et al. (2017), we modify our ETR measure and construct METR, which is ETR divided by ATR... We find that our results in Table 3 remain unchanged using the METR measure."

**07-DHT §6.5 (alternative regression specification):**
> "Our descriptive statistics in Table 2 indicate that the means of the abnormal return variance tend to be higher than the medians, suggesting that our measure of abnormal return variance is skewed. Thus, we rerun our full-model regression (Model 2) in Table 4, Panel B after replacing all variables other than the dummies with the ranked values of the corresponding variables. The analysis (not tabulated) yields results consistent with the results in Model 2 of Table 4, Panel B... Thus, our overall conclusions are not sensitive to this alternative regression specification."

**26-KLYY §4.4.5 (4 alternative IV constructions in parallel):**
> "To test whether our measure of audit partners' cultural trust, PartnerTrust, is robust to using alternative name classification techniques, we use four complementary approaches and report the regression results in Panels A – D of Table A2 of the Online Appendix. As these four approaches were developed by independent research teams, they have unique strengths and weaknesses which help to cross-validate our findings. In Panel A, we use U.S. Census records from 1850 to 1940... In Panel B, we use the OnoMAP software... In Panel C, we use the ethnicity-name matching technique developed by Kerr (2008)... In Panel D, we use OpenAI's GPT-4o..."

The 26-KLYY 4-method triangulation is the **gold standard** for measure robustness in 2026-era audit papers: when the IV is a constructed proxy, show convergence across **independent** measurement teams.

---

## 9. Subsample Tests — Standard Pattern

### 9.1 Subsample Sentence Structure (3 sentences)

```
[1. Identify subsample.] We re-estimate equation [N] separately for [Subsample
A] and [Subsample B], where [definition of split].

[2. Theoretical motivation OR mechanical motivation.] We do this because
[Subsample A and B differ in [characteristic that may matter]] / [a large
weight on [Subsample A] might drive our results].

[3. Result.] [Table N, Panel X] reports that [the coefficient on IV remains
significant in both subsamples] / [the coefficient is [sign and significance]
in Subsample A and [sign and significance] in Subsample B].
```

### 9.2 Real Examples

**16-DLZ Table 7, Panel F (Big-N split):**
> "Panel F reports our primary regression results when the sample firms audited by Big N and non-Big N auditors are separately estimated."

> Body: "We repeat our analysis separately for Big N and non-Big N auditor clients. The results reported in Table 7, Panel F indicate that the coefficients on CONSV are all significant and negative for both Big N and non-Big N auditor clients, similar to the results for the full sample."

**24-DLWW §6.2 (alternative samples):**
> "Panel B of Table 9 presents our hypothesis test using alternative samples. First, we drop all years in which the engagement auditor in year T differs from the engagement auditor in year T-1. Second, we drop all observations in which ClientTies = 1. This leaves a sample in which none of the auditors have connections with client management. Third, we drop all auditors who are located in Beijing, Shanghai and Shenzhen, because these are the three regions in which the central government's CSRC offices and stock exchanges are located. The results of Columns (1) to (3) continue to find a significantly negative coefficient on Network using these sub-samples."

---

## 10. Tables vs. Inline (Untabulated) — What Goes Where

### 10.1 ALWAYS in a table

- Cross-sectional / heterogeneity test (1 panel per partition variable)
- Falsification / placebo test (especially when columns include both placebo-only and joint specifications)
- Quasi-experimental DiD (treatment effect + parallel trends in separate columns)
- FE saturation (4-column ladder)
- Alternative measure of main IV
- Alternative measure of main DV (if it's a different construct, not just a transformation)

### 10.2 USUALLY untabulated (inline prose with "untabulated" tag)

- Subsample sensitivity ("Our results hold after dropping [subsample]; not tabulated.")
- Trivial alternative specifications (winsorization at 5/95 vs 1/99; rank vs level)
- Adding 1-2 obvious controls
- Standard error clustering robustness
- Outlier-deletion sensitivity

### 10.3 Verbatim "Untabulated" Phrases

- "The analysis (not tabulated) yields results consistent with the results in Model 2 of Table 4, Panel B." (07-DHT, repeated)
- "We also perform several untabulated robustness checks." (16-DLZ, opening line of §V "Other Robustness Checks")
- "In untabulated analysis, we find that..." (25-DQSZ, multiple)
- "5. Additional analyses (untabulated)" — entire section labeled this way (25-DQSZ §5)

### 10.4 The Ratio

Modal corpus paper has roughly:
- **3-5 tables of robustness** (cross-sectional + falsification + DiD + FE saturation + alt measure)
- **5-10 untabulated robustness items** described in 1-3 sentences each, often grouped at the end of a §V "Other Robustness" subsection (16-DLZ pattern) or in a dedicated §5/§6 (07-DHT pattern).

---

## 11. Closing Sentence of Robustness Section — Patterns

The robustness/additional section closes with a recurring sentence type that **summarizes without enumerating**.

### 11.1 Verbatim Closings

**07-DHT §5 closing:**
> "Overall, our analysis and discussion in this section suggest that our results are unlikely to be driven by lack of informational efficiency among the firms in countries with weak investor protection institutions."

**07-DHT §6 closing implicitly:**
> "Thus, our overall conclusions are not sensitive to controlling for capital market development." (each subsection has its own micro-closing)

**24-DLWW §5.3 closing:**
> "In summary, the results in Table 8 find that the exogenous director dismissals due to Reg. 18 reduced audit quality, consistent with our primary findings. However, as previously discussed, there is some question regarding the speed with which this disruption is expected to affect earnings quality. Thus, it is important to caveat that our sample selection process for identifying the corruption-related disruptions, which involves extensive hand collection, necessarily involves judgement."

**24-DLWW §7 (Conclusion intro, summarizing robustness):**
> "We also perform tests that find that our results are not explained by strong social connections facilitating the auditor's ability to conceal financial reporting irregularities. In addition, we perform falsification tests that indicate our results do not generally hold for auditors who have stronger connections with social networks outside of their clients' provinces. We further find that our results are stronger in provinces where clients are more likely to engage in relationship-based contracting and weaker in settings where clients are less likely to engage in relationship-based contracting and when auditors' social networks are disrupted by regulatory change. Taken together, our findings are consistent with..."

**25-DQSZ §4.2.5 closing (cross-sectional):**
> "Taken together, the results in Table 7 show that the effects of tax-expert auditors on tax aggressiveness vary predictably with client and auditor characteristics, which helps alleviate concerns that unobservable company and auditor characteristics explain our results."

### 11.2 Closing Templates

**Template A — "Together, these analyses suggest that..."**
> "Taken together, the results in [Tables N–M] show that [the effect varies in theory-consistent ways / the effect survives standard sensitivity tests], which helps alleviate concerns that [main alternative explanation] explains our results."

**Template B — "Robust to..."**
> "Overall, our results are robust to [list of sensitivity tests], suggesting that [mechanism] is not driven by [specific concern]."

**Template C — "Cumulatively..."**
> "Cumulatively, the cross-sectional, falsification, and quasi-experimental tests above corroborate our primary inference that [mechanism]."

### 11.3 Forbidden Closings

- ❌ "All robustness checks pass" (no specifics; reviewers hate this)
- ❌ "Our results are bulletproof"
- ❌ "We have addressed all alternative explanations"
- ❌ Long laundry-list closings — keep it to 1-2 sentences if you've already enumerated.

---

## 12. Verb Whitelist for Robustness Sections

These verbs appear repeatedly across the corpus and signal the conservatively-confident DeFond voice.

| Verb | Function | Example |
|---|---|---|
| **exploit** | for natural experiment | "Our first test exploits regulations in China that require signatory auditors to rotate every five years." (25-DQSZ) |
| **address** | for an explicit concern | "To address concerns about potential endogenous matching..." (24-DHXZ) |
| **attenuate** | for endogeneity / measurement-error worry | "We perform six analyses to attenuate endogeneity concerns." (25-DQSZ) |
| **alleviate** | for a specific reviewer concern | "...helps alleviate concerns that unobservable company and auditor characteristics explain our results." (25-DQSZ) |
| **rule out** | for an alternative explanation | "To rule out the possibility that our findings are driven entirely by this information-based channel..." (24-DHXZ) |
| **mitigate** | for partial address (weaker than rule out) | "...helping to mitigate the concern that our insignificant results for Type II errors may be due to low test power." (26-KLYY) |
| **corroborate** | for results aligning across tests | "Thus, our hypothesis tests that use trading volume corroborate the results of our primary analysis." (07-DHT) |
| **triangulate** | for measure robustness | "These results triangulate with those in Table 5, giving us comfort that the association between audit partners' cultural trust and going concern decisions is unlikely to be spurious." (26-KLYY) |
| **repeat** | for re-estimation under alt spec | "We repeat our primary analysis after controlling for client company-fixed effects..." (25-DQSZ) |
| **decompose** | for splitting variable | "we decompose the variable Range into two variables..." (24-DHXZ) |
| **disrupt** | for shock to mechanism | "...the resignation of many independent directors, thereby disrupting auditors' networks." (24-DLWW) |
| **provide comfort that** | for soft confirmation | "This placebo test also provides comfort that our results... are not spuriously driven by other concurrent changes in 2008." (25-DQSZ) |
| **suggesting that** | for inference | "...suggesting that auditors have career incentives to obtain CTA designation." (25-DQSZ) |
| **consistent with** | for theory link | "...consistent with our primary findings." (24-DLWW, repeated) |

### 12.1 Forbidden Verbs in Robustness Sections

- ❌ "prove" / "demonstrate definitively" / "establish causally" — overclaim
- ❌ "show that" without qualification — too strong; use "find" or "provide evidence that"
- ❌ "kitchen-sink" any framing — never say you "kitchen-sinked" the regression
- ❌ "robust across all specifications" without enumeration — reviewers will demand the list

---

## 13. Forbidden Patterns in Robustness Sections

Cataloged from the (absence of) violations across the 6-paper corpus and from referee-feedback norms.

### 13.1 Rhetorical forbiddens

- ❌ "We kitchen-sink the regression to address all concerns at once."
- ❌ "All robustness checks pass without exception" — without enumeration.
- ❌ "Our results are bulletproof / unassailable / incontrovertible."
- ❌ "We control for everything that could possibly matter."
- ❌ Marketing adjectives: "comprehensive battery", "exhaustive sensitivity analysis", "extensive robustness".

### 13.2 Structural forbiddens

- ❌ Re-introducing the main hypothesis fresh (waste of words; you already stated it).
- ❌ Long restatement of the main result coefficient at the start of each robustness subsection.
- ❌ Re-estimating with the same modification 3 different ways without consolidating.
- ❌ Cherry-picking placebo: only reporting placebos that are insignificant.
- ❌ "Untabulated" used as a shield for negative results (if the result kills your story, tabulate it and explain).

### 13.3 Identification forbiddens

- ❌ Calling something "exogenous" without defending exogeneity.
- ❌ Skipping the parallel trends test for a DiD design.
- ❌ Using PSM as the primary identification when you have a regulatory shock available.
- ❌ Running falsification tests in a setting where they are mechanically null.
- ❌ Treating "results survive in subsample S" as causal evidence.

### 13.4 Reporting forbiddens

- ❌ Reporting only one specification per robustness panel (always include the original main column for comparison).
- ❌ Hiding sample size changes in untabulated text — always report N when restricting.
- ❌ Hiding which observations were dropped — always say "We exclude X observations because Y."

---

## 14. Annotated Example: 25-DQSZ "First...Sixth" Six-Test Identification Battery

The 2025 DeFond-Qi-Si-Zhang JAE paper on signatory tax expertise contains the **single best template** for an identification/robustness battery in modern audit research. The structure is explicit, numbered, and exhaustive — exactly what reviewers want.

### 14.1 Verbatim Frame (from intro, ¶'s introducing the battery)

> "A threat to our analysis is that tax-expert auditors may be endogenously chosen. In particular, tax-aggressive clients may intentionally select non-tax-expert auditors in order to avoid scrutiny. However, doing so would subject tax-aggressive clients to the costs that arise from tax aggressiveness... If both clients and auditors have incentives to match tax-aggressive clients with tax-expert auditors, the effect of tax-expertise on tax aggressiveness we document may be understated. Nevertheless, **we perform six analyses to attenuate endogeneity concerns**."

### 14.2 The Six Tests

| # | Test | Type (in our taxonomy) | Verbatim opening |
|---|---|---|---|
| 1 | **Mandatory rotation** | Quasi-experimental (§1.3) | "Our first test exploits regulations in China that require signatory auditors to rotate every five years." |
| 2 | **2008 tax-rate cut** + **placebo with industry expertise** | Quasi-experimental (§1.3) + Placebo (§1.1) | "Our second test examines the effects of a regulatory shock that reduces corporate tax rates, thereby weakening the incentives to engage in aggressive tax planning. ... We also perform a placebo test by replacing auditor tax expertise with industry expertise..." |
| 3 | **Tax-related vs non-tax-related misstatement decomposition** | Falsification + Channel (§1.1, §1.9) | "Our third test finds that tax-expert auditors attenuate the positive association between tax-aggressiveness and tax-related misstatements... We also perform placebo tests that find that tax-expert auditors are not associated with a reduction in non-tax-related misstatements..." |
| 4 | **Decomposition of BTD into pre-tax-book-income and taxable-income components** + **tax vs non-tax audit adjustments** | Channel (§1.9) | "Our fourth test finds that clients of tax-expert auditors report higher taxable income but not lower pre-tax book income..." |
| 5 | **Cross-sectional: SOE vs private + auditor with vs without industry expertise** | Cross-sectional (§1.2) | "Our fifth test comprises two cross-sectional analyses. We find that tax-expert auditors have a weaker effect on reducing tax aggressiveness for state-owned enterprises (SOEs)..." |
| 6 | **Client company fixed effects** | FE saturation (§1.6) | "In our sixth test we find that our main results continue to hold after including client company-fixed effects, indicating that our results are not explained by time-invariant differences across client companies." |

### 14.3 Why This Structure Works

1. **Explicit count.** "We perform six analyses" — sets reviewer expectation; no ambiguity.
2. **Six distinct functions.** No two tests are the same identification move. Each one closes a specific door.
3. **Two natural experiments + two falsifications + cross-section + FE.** Hits five of the canonical-battery items in Section 1 above.
4. **Each test is justified ex ante**, not just executed. Each "First, ... Second, ..." sentence states what the test does AND what worry it addresses.
5. **Closing sentence (§4.2.5):** "Taken together, the results in Table 7 show that the effects of tax-expert auditors on tax aggressiveness vary predictably with client and auditor characteristics, which helps alleviate concerns that unobservable company and auditor characteristics explain our results."

### 14.4 Adaptable Skeleton for Skill Users

If you have a setting where you can run multiple identification tests, use this skeleton:

```
A threat to our analysis is that [Treatment] may be endogenously chosen.
[Briefly state the two main directions of bias.] Nevertheless, we perform
[N] analyses to attenuate endogeneity concerns.

Our first test exploits [regulatory shock or rotation event]. Consistent with
a causal relation, we find [direction of effect].

Our second test examines [a different shock or quasi-experiment]. Consistent
with a causal relation, we find [direction of effect]. We also perform a
placebo test by [substituting placebo treatment] and find [null result].

Our third test [channel decomposition or alternate DV that should/shouldn't move].
This is consistent with [restating mechanism]. We also perform placebo tests
that find [null result on the placebo].

Our fourth test [further channel evidence or auxiliary outcome].

Our fifth test comprises [cross-sectional analyses].

In our [Nth] test we find that our main results continue to hold after
including [most demanding fixed effects], indicating that our results are
not explained by [time-invariant heterogeneity at unit X].

[Optional: Our [N+1th] test does [robustness-only sensitivity, e.g., alt
measures].]

Taken together, [closing template from §11.2].
```

---

## 15. Self-Audit Checklist

Before finalizing a robustness / additional-analyses section, verify:

- [ ] **Section split correct.** Did you separate "Additional Analyses" (extending hypothesis) from "Robustness Tests" (sensitivity to specification), OR explicitly justify combining them?
- [ ] **At least one cross-sectional / heterogeneity test** with ex-ante prediction that the effect varies in a theory-consistent way.
- [ ] **At least one falsification / placebo test** using a spatially or functionally unrelated variant of the IV.
- [ ] **At least one alternative measure of the focal IV** (and ideally also of the DV).
- [ ] **Fixed-effects ladder reported** — at minimum 4 columns from "industry+year" through "client-firm + engagement-auditor FE".
- [ ] **"Variation absorbed by FE" and "VIF for IV" reported** at the bottom of the FE table (24-DLWW Table 6 standard).
- [ ] **At least one quasi-experimental test** if your setting offers a plausibly exogenous shock; parallel trends verified.
- [ ] **At least 2-3 subsample restrictions** (Big4/non-Big4, SOE/private, drop a dominant region/period).
- [ ] **PSM defensively framed** if used at all — Shipman 2017 + King-Nielsen 2019 footnoted; entropy balancing or CEM considered as alternative.
- [ ] **Untabulated tail (5-10 mini-tests)** of inline-only robustness items — at the end of §6 or in a final "Other robustness checks" subsection.
- [ ] **Closing sentence template C/B/A** used — no marketing adjectives, no "all checks pass", no "kitchen sink".
- [ ] **Verb whitelist enforced** — exploit, address, attenuate, rule out, mitigate, corroborate, triangulate, alleviate, repeat, provide comfort that.
- [ ] **No forbidden verbs** — no "prove", no "definitively", no "show that" un-hedged.
- [ ] **No null-placebo cherry-picking** — all run placebos reported, not just the insignificant ones.
- [ ] **Sample size N reported** when restricting to subsample.
- [ ] **If your story requires a null on a secondary outcome** — power analysis + 95% CI + effect-size benchmark explicitly defended (26-KLYY §4.3 standard).

---

## 16. Length Budget per Robustness Section

| Subsection | Median word count | Range |
|---|---|---|
| Cross-sectional / heterogeneity (per partition) | 250 | 150–500 |
| Falsification / placebo | 400 | 250–800 |
| Quasi-experimental DiD | 600 | 400–1200 |
| FE saturation | 250 | 150–400 |
| Alternative measure (per measure) | 150 | 100–300 |
| Subsample test (per subsample) | 100 | 50–200 |
| Untabulated tail (each item) | 50 | 30–100 |
| **TOTAL (Robustness + Additional combined)** | **3,500–6,000** | **2,500–8,000** |

For a JAE/JAR audit paper, robustness + additional analyses occupy **30–40% of total body word count** (excluding intro/conclusion). For TAR, slightly less due to TAR's more compact format.

---

## 17. Quick Reference: Mapping Tests to Reviewer Concerns

| Reviewer concern | Best test(s) to run |
|---|---|
| "But couldn't [auditor self-selection] explain this?" | Quasi-experimental (mandatory rotation, regulatory shock) + client FE |
| "But this is just measuring [related construct X], not [your construct]" | Falsification placebo using X; alternative IV measures |
| "But the result might just reflect industry/year trends" | FE saturation up to industry × year × province |
| "But isn't this just driven by Big4 / SOEs / Beijing-Shanghai?" | Subsample restrictions excluding each |
| "But the DV is noisy" | Alternative DV measures; channel decomposition |
| "But your N is too small to generalize" | Power analysis + 95% CI + alternative samples |
| "But your standard errors are misclustered" | Multi-way clustering / bootstrap inference |
| "But you didn't use PSM" | Hedged PSM in appendix; better, entropy balancing with Shipman footnote |
| "But the parallel trends might not hold" | Pre-treatment year placebo (T-1, T-2 indicators) in DiD |
| "But couldn't [contemporaneous shock Y] explain this?" | Drop confounded observations and re-run |
| "But your IV is endogenous" | Cross-sectional moderator showing effect varies with theory-consistent partition |
| "Why don't you find an effect on [secondary outcome]?" | Power analysis + CI bounds; mechanism story for asymmetric effect |

---

## 18. Closing Note on the DeFond Style of Robustness

Robustness sections in the DeFond / Zuo / Khurana JAE-TAR tradition share a distinctive voice:

1. **Pre-emptive, not reactive.** The robustness section should anticipate referee concerns BEFORE the referee raises them. Structure as: "A threat to our analysis is X. We address this by running Y." (25-DQSZ §4.2 opening is the canonical example.)

2. **Hedged but not weak.** Use "alleviate concerns" not "eliminate concerns"; "consistent with a causal relation" not "establishes causality"; "provides comfort" not "proves". The conservatively-confident voice (see audit-write/style_dna.md) is essential.

3. **Honest about limits.** When a test is partial, say so. When data is hand-collected and judgment-laden, caveat. (24-DLWW §5.3 closing is an exemplar of honest scope-setting.)

4. **No invented robustness.** Do not run a test that has no chance of overturning the main result and report it as evidence. Reviewers will see this as filler.

5. **Numbered when battery is large.** If you have 4+ identification tests, number them ("First, ... Second, ..."). 25-DQSZ's "we perform six analyses" structure is the modern gold standard.

6. **Closing without enumeration.** End with one summary sentence using "Taken together," "Cumulatively," or "Overall," — do not re-list every test.

The goal is not to convince the reviewer that no possible objection remains (impossible). The goal is to demonstrate (a) that you have **anticipated** the central objections, (b) that each anticipated objection has been **addressed by a transparent, falsifiable test**, and (c) that the **pattern of robustness results corroborates the proposed mechanism rather than a mechanical artifact**.

When in doubt, do what 25-DQSZ does: run six tests, label each one explicitly with its function, close with one summary sentence.

# Audit-Paper Introduction: 5-Paragraph Anatomy

**Source corpus.** Extracted from 6 empirical introductions:
- DeFond, Hung, Trezevant 2007 JAE (`07-DHT`)
- DeFond, Lim, Zang 2016 TAR (`16-DLZ`)
- DeFond, Li, Wong, Wu 2024 JAE (`24-DLWW`) ★ closest analogue to typical China-audit paper
- DeFond, Qi, Si, Zhang 2025 JAE (`25-DQSZ`) ★ signatory-auditor design
- Khurana, Li, Yeung, Yu 2026 JAE (`26-KLYY`) ★ closest analogue: partner cultural trait → AQ
- Dekeyser, He, Xiao, Zuo 2024 JAE (`24-DHXZ`) — Zuo lineage

The 7th paper (DeFond-Zhang 2014 JAE *Archival Auditing Review*) is a review-paper intro and uses a different structure — see `../audit-write/audit_quality_framework.md` for its framework content, but do not use its intro structure as a template for empirical papers.

---

> **Frequency provenance (Stage-1 update 2026-05-21).** A bare `k/6 (template)` count is over the 6 original template papers (`corpus_manifest.md` §1). Headline move frequencies re-derived over **n=22** (6 template + 16 Stage-1 pilot) are written `k/22` with a pointer to `corpus_inventory/move_presence_matrix.md`. Do not read a `k/6 (template)` as if it were n=22.


## The canonical 5-block structure

Modern top-3 audit papers organize the introduction in **5 functional blocks**, totaling **5–8 actual paragraphs** (some blocks span 2 paragraphs). The block ordering is **stable across all 6 papers**.

```
Block 1: MOTIVATION + GAP                     [1–2 paragraphs]
Block 2: THEORY / HYPOTHESIS DEVELOPMENT      [1–3 paragraphs, MUST include tension]
Block 3: SETTING + DATA + DESIGN              [1–2 paragraphs]
Block 4: MAIN FINDINGS WITH MAGNITUDES        [1–2 paragraphs]
Block 5: ROBUSTNESS / IDENTIFICATION          [1–2 paragraphs, often merged with Block 4 in shorter intros]
[Final block]: CONTRIBUTIONS                  [3–5 paragraphs, numbered]
[Optional] LIMITATIONS / SCOPE                [1 paragraph at very end]
[Optional] ROADMAP                            [1 short paragraph — MODERN JAE PAPERS HAVE DROPPED THIS]
```

Total length: **3-5 pages typical, ~2,000-3,000 words**.

---

## Block 1 — Motivation + Gap (1–2 paragraphs)

### Function

Establish what the literature has done, identify a specific gap or tension, and state the research question. **No throat-clearing.** Open inside the literature, not outside it.

### The valid opening moves (frequency re-derived over n=22: 6 template + 16 Stage-1 pilot; see `corpus_inventory/move_presence_matrix.md`)

| Move | Freq (n=22) | Example | Use when |
|---|---|---|---|
| **A. Lit-baseline opening** | 11/22 | "A large body of research finds that social connections between economic agents affect a variety of financial outcomes" (24-DLWW ¶1) | Default; safest; signals you know the field |
| **B. Lit-contradiction opening** | 1/22 (+1 hybrid 23-PSZ) | "Prior research finds that some potential monitors of tax aggressiveness, including tax-expert auditors, facilitate aggressive tax avoidance. These studies, however, examine auditors who also provide non-audit tax services to their clients, creating conflicting incentives." (25-DQSZ ¶1) | When your contribution is to **overturn** a prior finding |
| **C. Theory-grounded opening** | 1/22 (+2 hybrid 24-Chen, 22-FHKF) | "Economic theories of cultural transmission emphasize that culture plays a critical role in shaping individual beliefs and preferences (e.g., Bisin and Verdier, 2000, 2023)." (26-KLYY ¶1) | When the contribution rests on importing theory from outside accounting |
| **D. Construct-introduction opening** | 2/22 | "Conditional conservatism is a qualitative accounting characteristic that potentially enhances financial reporting quality (Watts 2003). However, while research documents that conservatism improves debt contracting..." (16-DLZ ¶1) | When you're studying a well-known construct from a new angle |
| **E. RQ-first opening** (NEW; Stage-1) | 5/22 | "we examine whether Big N auditors provide higher audit quality than non-Big N auditors" (19-JWW ¶1) — RQ stated before any lit anchor | Design-driven / methods / concordance papers (19-JWW, 19-Aob, 22-FHKF, 23-ZBLM, 16-DLLN) |

### Forbidden openings

The corpus contains **zero** instances of any of these:
- ❌ Real-world anecdote / news event ("In 2024, Big-Four auditor X failed to detect...")
- ❌ Policy motivation ("Given the importance of audit quality for capital markets...")
- ❌ Quotations or epigraphs in the intro body (Dekeyser 2024 has an epigraph BEFORE Section 1, not in ¶1)
- ❌ "Auditing is one of the most important..." — broad-claim openings
- ❌ "The literature lacks..."  / "It is important to study..."

### Gap statement formula

The gap MUST appear by end of ¶1 (sometimes early ¶2). Three forms:

1. **Direct gap.** "However, the effects of [X] have not been explored." (24-DLWW)
2. **Conditional gap.** "These studies, however, examine [setting that confounds the inference]" (25-DQSZ)
3. **Construct-tension gap.** "However, while research documents [benefits of X], there is limited evidence on whether [X affects Y]." (16-DLZ)

### Research-question statement

Always present, usually the **last sentence of Block 1**. Standard formula:

> "The purpose of [our/this] study is to examine whether [precise prediction]."  
> — or —  
> "We attempt to fill this gap by investigating whether [precise prediction]."  
> — or —  
> "In this paper, we extend this literature by investigating whether [precise prediction]."

**Concrete examples from corpus:**

- "The purpose of this study is (1) to examine cross-country differences in investors' reactions to annual earnings announcements..., and (2) to identify country-level differences in the financial reporting environment that influence the announcements' informativeness." (07-DHT)
- "We attempt to fill this gap by investigating whether and how client conservatism affects audit fee pricing, audit opinion formation, and auditor resignation decisions." (16-DLZ)
- "The purpose of our study is to examine the effects of auditors' social connections within their clients' business community, a setting in which auditors' connections may lead to desirable financial outcomes in the form of higher quality audits." (24-DLWW)
- "The purpose of this study is to examine whether signatory auditors with tax expertise, who only perform audit services, curb tax aggressiveness." (25-DQSZ)
- "In this paper, we extend this literature by investigating whether cultural differences in trust influence audit partners' going concern opinions and clients' financial reporting quality." (26-KLYY)

---

## Block 2 — Theory / Hypothesis Development (1–3 paragraphs)

### Function

Walk the reader through the conceptual logic supporting the prediction, AND explicitly state countervailing forces ("tension"). The tension paragraph is a **strong default, not a law** — re-derived over n=22 it appears in canonical form in 7/22 intros, in some variant (active-phrasing / enumerated / head-placed / in-¶1 / three-sided / methodological) in another 7/22, and is absent-from-intro (often deferred to §2) in 8/22. Include it unless you have a deliberate reason to defer to Section 2. See `corpus_inventory/move_presence_matrix.md`.

### Standard internal structure

```
¶2a: Argument FOR the predicted direction.
     "We hypothesize that..." or "We posit that..."
     — Mechanism stated in plain English.
     — May cite 2-3 supporting papers.

¶2b: Tension / counter-arguments.
     "We note, however, that there is tension in our prediction."
     — or —
     "Several factors may work against our prediction."
     — or —
     "However, there are also reasons why [the opposite may hold]."
     — Counter-mechanism stated in plain English.

¶2c (optional): Net resolution.
     "Whether the net effect is [positive/negative] is ultimately an empirical question."
     — Or a conclusion about which force is likely to dominate.
```

### Hypothesis statement format

State the hypothesis **in alternative form** at end of Block 2:

> "**Hypothesis [N].** [Subject] is [associated with / negatively associated with / positively associated with] [outcome], ceteris paribus."

**Examples:**
- "**Hypothesis 1.** Countries with higher earnings quality have more informative annual earnings announcements." (07-DHT)
- "**H1.** Audit partners' cultural trust is negatively associated with the likelihood of issuing going concern opinions, ceteris paribus." (26-KLYY)

For papers with one main hypothesis, just say "Our hypothesis" without numbering. For papers with multiple hypotheses (07-DHT has 4; 26-KLYY has 5), number them.

---

## Block 3 — Setting + Data + Design (1–2 paragraphs)

### Function

Justify why this empirical setting is appropriate, describe the data, and (briefly) describe identification.

### China-setting justification template

5 of 6 (template) papers use Chinese data. The justification follows a **standard 3-part structure**:

```
(1) Data availability advantage:
    "China has a long time-series of publicly available data on engagement auditor identity,
     as well as information on social connections for individual auditors..." (24-DLWW)
    "China provides information on whether a signatory auditor is a Certified Tax Agent (CTA)..." (25-DQSZ)

(2) Institutional feature that enables the test:
    "China, like many countries, is primarily a relational economy, where companies
     rely heavily on social networks..." (24-DLWW)
    "The market for non-audit services (NAS) in China is relatively underdeveloped..." (25-DQSZ)

(3) Within-China variation that powers cross-sectional tests:
    "China also has variation in market development across its provinces, which should
     affect the clients' reliance on relational contracting..." (24-DLWW)
```

### Data-description sentence

Single sentence at end of block:

> "Our final sample consists of [N] [unit-of-observation] [observations] over the period [year]–[year]."

**Examples:**
- "Our sample consists of 53,197 annual earnings announcements from companies in 26 countries during the period 1995 through 2002..." (07-DHT)
- "We perform our tests over the period 2005–2018, with 20,778 client company-year observations, where 10.4% of our observations report financial irregularities..." (24-DLWW)
- "Our final sample consists of 18,924 company-year observations for the book-tax difference (BTD) analysis and 17,076 observations for the current effective tax rate (ETR) analysis." (25-DQSZ)

---

## Block 4 — Main Findings with Magnitudes (1–2 paragraphs)

### Function

State the headline result, give the economic magnitude, and pre-empt one or two alternative explanations.

### Lead-sentence formula

> "Consistent with our hypothesis, we find [direction of effect]." 
> — or —
> "As hypothesized, we find that [subject] [verb] [outcome]."

**Frequency in corpus:** "Consistent with..." appears as opening of Block 4 in 4/6 (template) papers. "As hypothesized" appears in 2/6 (template).

### Magnitude reporting — non-negotiable

Every paper reports the economic magnitude in Block 4 using **at least one** of these formats:

1. **Percentage point change:**
   > "auditors with strong connections lower the probability of their clients' reporting a financial irregularity by 2.1 percentage points" (24-DLWW)

2. **Percentage of base rate:**
   > "This represents an economically significant 19% decline in the average incidence of financial irregularities..." (24-DLWW)

3. **Decile shift:**
   > "moving from the bottom to the top decile of conservatism decreases audit fees by 29 (10) percent..." (16-DLZ)

4. **Standard-deviation framing:**
   > "a one standard deviation increase in PartnerTrust is associated with a 0.8% decrease in the probability of issuing a going concern opinion..." (26-KLYY)

5. **Interquartile change:**
   > "An interquartile change in our measures of industry range leads to about a 7% increase in the likelihood of an audit adjustment." (24-DHXZ)

**Strong default (re-derived n=22):** Block 4 should carry at least ONE numerical magnitude; coefficient + standard error alone is insufficient. Present in 19/22 intros. The 3 exceptions (19-JWW, 22-CHLP, 24-Chen) are pre-2024 or JAR papers that report direction-only — treat magnitude as mandatory for modern JAE/TAR submissions, where its absence now reads as a gap.

### Alternative explanations (in 5/6 (template) papers)

After the magnitude, immediately address the most likely alternative explanation:

> "We also investigate alternative explanations for our findings. One alternative explanation is that [X]. We investigate this..." (24-DLWW)

> "A threat to our analysis is that [X] may be endogenously chosen. However, [counter-argument]." (25-DQSZ)

---

## Block 5 — Robustness / Identification (1–2 paragraphs)

### Function

Demonstrate causal evidence (where possible) and falsification.

### Standard moves (frequency in corpus)

| Move | Frequency | Example |
|---|---|---|
| Auditor rotation as quasi-experiment | 2/6 (template) | "Our first test exploits regulations in China that require signatory auditors to rotate every five years..." (25-DQSZ) |
| Regulatory shock | 3/6 (template) | "We exploit a regulatory shock that disrupts the auditor's business connections..." (24-DLWW) |
| Placebo / falsification test | 4/6 (template) | "We also perform falsification tests that replace [X] with two placebos..." (24-DLWW) |
| Cross-sectional corroboration | 6/6 (template) | "Corroborating our primary findings, we also find that our results are stronger in [setting] and weaker in [setting]." (24-DLWW) |
| Fixed effects robustness | 5/6 (template) | "Our primary results are robust to including audit firm, client, signatory auditor, and province-year fixed effects." (24-DLWW) |

**Use whichever 2-3 of these are honest in the paper.** Do not invent.

---

## Final Block — Contributions (3–5 paragraphs, numbered)

### Function

State 3–4 numbered contributions to specific literatures. This is the **closing argument** of the introduction.

### Standard opening sentence

> "Our study contributes to [the audit literature / the literature on X / several streams of research] by..."

**Variants:**
- "Our study contributes to the auditing literature by examining the trade-off between..." (24-DLWW)
- "Our study makes several contributions to the literature." (25-DQSZ)
- "Our study makes two main contributions." (26-KLYY) — short version
- "We make four main contributions." (24-DHXZ)
- "Our paper contributes to the literature in several ways." (07-DHT)

### Numbered-contribution structure (3-4 typical)

```
First, we [contribute to literature L1] by [doing Z1].
   [Cite 2-4 prior papers in L1.] [Explain what's new.]

Second, we [contribute to literature L2] by [doing Z2].
   [Cite 2-4 prior papers in L2.] [Explain what's new.]

Third, we [contribute to literature L3] by [doing Z3].
   [Cite 2-4 prior papers in L3.] [Explain what's new.]

[Optional Fourth: implications for practice / regulators / policy.]
```

See `contribution_formulas.md` for 8 specific formulas.

### Closing limitation paragraph (in 4/6 (template) papers)

After contributions, optionally add 1 paragraph acknowledging scope limitations:

> "We acknowledge, however, that our use of Chinese data may limit the generalizability of our findings. In particular, because China's economy is traditionally relationship-based, the extent to which our findings extend to economies that rely more on arms-length contracting, such as the U.S., is unclear. Nonetheless, China is representative of many emerging and transitional economies..." (24-DLWW)

This is **NOT a weakness signal.** It is the modern DeFond style — preempting the reviewer's first objection and reframing it.

---

## Roadmap — drop it for JAE/JAR, keep it for TAR/AJPT

Modern JAE intros (3 of 4 corpus JAE papers) **do not** include an explicit roadmap. The 2007 DeFond JAE paper does ("The remainder of the study proceeds as follows..."). The 2016 TAR paper has roadmap. The 2024-2025 JAE papers don't.

**Default:** No roadmap unless target journal is TAR/AJPT, or unless the paper is unusually long (>50 pages with non-standard structure).

---

## Length budget per block (corpus median)

| Block | Median words | Range |
|---|---|---|
| 1. Motivation + Gap | 250 | 150–500 |
| 2. Theory + Tension | 400 | 250–800 |
| 3. Setting + Data | 250 | 150–400 |
| 4. Findings + Magnitudes | 350 | 200–600 |
| 5. Robustness | 200 | 100–400 |
| Final. Contributions | 600 | 400–1200 |
| Limitations (optional) | 150 | 0–300 |
| **TOTAL** | **~2,200** | **1,500–3,500** |

---

## Annotated example: Khurana et al. 2026 JAE (closest analogue to a partner-trait paper)

This paper is the **single most important structural template** for a paper studying auditor partner traits. Annotated mapping:

| Section | Block | Move |
|---|---|---|
| ¶1: "Economic theories of cultural transmission..." | 1 | Theory-grounded opening (Move C) |
| ¶2: "Prior research has theorized that culture..." | 1 | Gap statement (paucity of data) |
| ¶3: "In this paper, we extend this literature..." | 1 | Research question |
| ¶4: "Building on the theoretical arguments..." | 2a | Hypothesis intuition |
| ¶5: "Conditional on our first prediction..." | 2a | Mechanism (Type I/II framework) |
| ¶6: "We argue that the likelihood of Type I and Type II errors..." | 2b | Tension |
| ¶7: "While our previous hypotheses suggest..." | 2b | Cost of trust (counter) |
| ¶8: "To examine these predictions empirically..." | 3 | Setting + design (epidemiological approach) |
| ¶9: "The analyses in our study uncover a robust negative association..." | 4 | Main finding |
| ¶9 (continued): "a one standard deviation increase in PartnerTrust is associated with a 0.8% decrease..." | 4 | Magnitude |
| ¶10: "Next, we conduct cross-sectional tests..." | 5 | Robustness/cross-sectional |
| ¶11: "Turning to clients' financial reporting quality..." | 4 (extended) | Secondary finding |
| ¶12: "We conclude by conducting a number of additional tests..." | 5 | Robustness |
| ¶13: "Our study makes two main contributions. First, we add to a growing literature on the role of individual audit partners..." | Final | Contribution 1 |
| ¶14: "Second, we add to an emerging literature on the role of culture..." | Final | Contribution 2 |

**Notable omissions in 26-KLYY:** No roadmap; no limitations paragraph. Modern minimalist JAE style.

---

## Annotated example: Jiang, Wang, Wang 2019 TAR (RQ-first opener + design-driven Block 2; `19-JWW`)

This paper is a **counter-template** to the canonical 5-block intro: it inverts Block 1 by leading with the research question, substitutes a methodological-debate tension for the conventional theory derivation in Block 2, and reports direction-only findings in Block 4 without numeric magnitudes. Use it as the reference exemplar when the paper's contribution is a quasi-experimental design rather than a new theory.

| Section | Block | Move |
|---|---|---|
| ¶1: "we examine whether Big N auditors provide higher audit quality than non-Big N auditors" | 1 | M3 research question (RQ-first opener; inverts M1A lit-baseline default) |
| ¶1: "DeAngelo (1981) argues that audit quality should increase with auditor size." | 1 | M1A lit-baseline (placed after RQ, not before) |
| ¶1: "the Big N effect remains controversial" | 1 | M2 conditional gap (controversy framing) |
| ¶1: "such a setting does not exist in reality" | 1 | M2 direct gap (via counterfactual ideal-experiment frame) |
| ¶3: "selection models are fragile and can yield quite literally any possible outcome in response to fairly minor changes in model specification" | 2 | M4 tension (methodological, via quoted critique of PSM/Heckman) |
| ¶4: "The debate between Lawrence et al. (2011) and DeFond et al. (2017) highlights the need for more evidence on the Big N effect" | 2 | Net resolution (debate framing motivates new quasi-experiment) |
| ¶4: "Our study answers these calls by exploring the exogenous setting of Big N auditors' acquisitions of non-Big N auditors" | 3 | Setting + design (exogeneity source for client-firm switches) |
| ¶4: "Our final treatment sample includes 331 public firms with sufficient data that switched from a non-Big N to a Big N auditor" | 3 | Sample-size sentence (period 1976–1995 in surrounding prose) |
| ¶4: "We find that client firms of the acquired non-Big N auditors (treatment firms) report smaller discretionary accruals" | 4 | Main finding lead (direct; omits "Consistent with our hypothesis" opener) |
| ¶4: "we manually collect a sample of mergers and acquisitions (M&As) between two non-Big N auditors" | 5 | Falsification via non-Big-N M&A null-control sample |
| ¶4: "In a placebo test, we create pseudo acquisitions by assuming that the Big N acquisitions occur three years earlier than the actual date" | 5 | Pre-event placebo (standard form) |
| ¶4: "larger treatment firms, not the smaller ones, experience improved audit quality after the Big N acquisitions" | 5 | Cross-sectional partition by client firm size |
| ¶6: "we find no significant market reactions among the treatment firms" | 4 (secondary) | Secondary null on investor market reaction |
| ¶7: "Our study contributes to the literature on the Big N effect by utilizing the unique setting of Big Ns' acquisitions of non-Big N auditors" | Final | M6 form 7 Contribution 1 (design-asset framing) |
| ¶7: "Our setting has two main limitations. First, the uniqueness of our setting unfortunately leads us to identify a small treatment sample from 1976 to 1995" | Final | M7 closing scope/limitation (placed mid-Final, non-canonical) |
| ¶7: "Our study also contributes to the research on the impact of auditor mergers and acquisitions in general" | Final | M6 form 4 Contribution 2 (complement/extend auditor-M&A literature) |
| ¶7: "The rest of the study proceeds as follows. Section II discusses the background on Big N acquisitions and related literature" | Final | Roadmap (TAR convention; modern JAE drops this) |

**Notable deviations in 19-JWW** (file this paper as the "design-driven, not theory-driven" counter-template):

1. **RQ-first opening.** Sentence 1 of ¶1 states the research question; the lit-baseline anchor (DeAngelo 1981, Francis-Wilson 1988, Dopuch-Simunic 1982, Sirois-Simunic 2011) backs it up only after the RQ is in place. Inverts the M1A default.
2. **Design-driven Block 2.** No theory derivation; tension comes from quoted methodological critiques of PSM/Heckman selection-correction approaches. When the contribution is a quasi-experiment rather than a new theory, this is the available substitution.
3. **No numeric magnitude in Block 4.** Direction-only finding ("smaller discretionary accruals"). Predates the modern magnitude-non-negotiable norm; do not replicate this in 2024+ submissions.
4. **M7 limitation embedded mid-Final.** Limitations sit between Contribution 1 and Contribution 2 rather than after both contributions. Atypical placement; the 4/6 (template) corpus default is post-contribution.
5. **TAR roadmap preserved.** Final sentence is the explicit "Section II discusses..." roadmap; supports the convention that TAR/AJPT keep roadmaps even when modern JAE drops them.

---

## Annotated example: Lee, Naiker, Stewart 2022 TAR (practitioner-data opener + M4 tension omission; `22-LNS`)

This paper is the reference exemplar for the **M1A practitioner-data variant**: instead of opening on academic literature, it opens on AICPA's industry-data citation and PwC's recruiter map. It is also the first corpus paper to **omit the M4 tension paragraph** entirely, which has implications for the "M4 corpus-unanimous" claim in `move_bank.md`.

| Section | Block | Move |
|---|---|---|
| ¶1: "the American Institute of Certified Public Accountants' (AICPA) CPA Firm Top Issues Survey ranks the search for talent" | 1 | M1A practitioner-data variant (industry survey, not academic lit) |
| ¶1: "this paper investigates how audit quality is affected by an audit office's proximity to target universities" | 1 | M3 research question (end of ¶1, canonical placement) |
| ¶2: "PricewaterhouseCoopers (PwC) maintains a list of 256 schools where it has a dedicated recruiter responsible for recruitment activities" | 1 | M2 institutional anchor (single-firm evidence preview) |
| ¶2: "an important question is whether the proximity of audit offices to more feeder and accredited schools can positively affect audit quality" | 1 | M3 RQ formalization (canonical form) |
| ¶3: "future audit research should be on the auditing implications of graduate labor markets, which has not been considered in prior studies" | 1 | M2 direct gap (anchored on Causholli et al. 2010 call-for-research) |
| ¶4: "the proximity to more target schools should allow audit offices to interact with more high-quality students through networking and recruitment events" | 2 | Hypothesis intuition (mechanism only; M4 tension absent) |
| ¶5: "Based on a sample of 39,337 Big 4 auditor client observations from 2000 to 2016" | 3 | Sample-size sentence (2000–2016 period) |
| ¶5: "we find positive associations between audit quality and our proximity measures" | 4 | Main finding lead (direct; omits "Consistent with our hypothesis" opener) |
| ¶5: "reduces the likelihood of a client misstatement by around 9.07 (9.44) percent" | 4 | M5 F5+F2 magnitude (interquartile shift coupled with percent-of-base reduction) |
| ¶6: "Our main findings are robust to a battery of other tests to address endogeneity concerns, including an instrumental variable approach and an entropy balancing design" | 5 | Robustness battery (IV + entropy balancing) |
| ¶8: "auditor changes involving client firms switching to audit offices that are in proximity to more (fewer) universities are associated with a lower (higher) likelihood" | 5 | Switch-based falsification (Big R DV) |
| ¶9: "the positive effect of proximity on audit quality is driven by cities with a greater concentration of audit offices and by cities with larger offices" | 5 | Cross-sectional partition (demand-side mechanism corroboration) |
| ¶9: "our results do not hold for offices that have access to better schools" | 5 | Discriminant placebo (beyond-60-mile schools yield null) |
| ¶10: "Our study complements and extends recent work on how audit quality is affected by human capital factors (Beck et al. 2018; Hoopes et al. 2018)" | Final | M6 form 4 Contribution 1 (complement/extend human-capital literature) |
| ¶12: "Our findings also extend the broader research on how audit quality is affected by various audit office- and partner-level factors" | Final | M6 form 4 Contribution 3 (audit office/partner extension) |
| ¶13: "Our findings should be of interest to the AICPA, audit offices, and their clients" | Final | M6 form 5 implications closer (practitioner / regulator audience) |

**Notable deviations in 22-LNS**:

1. **M1A practitioner-data variant.** Opener cites industry data (AICPA survey, PwC recruiter map) rather than academic literature. The rhetorical function of M1A (establish baseline + signal field-knowledge) is preserved; the *evidence type* is practitioner not academic. File this as an M1A sub-form, not a new opener category.
2. **M4 tension omission.** Block 2 develops the proximity → recruiting → audit-quality mechanism but provides no explicit counter-mechanism or "however, there are reasons why..." paragraph. The endogeneity-concern phrasing in Block 5 is identification-against-confound, not a theoretical tension. Adding 22-LNS to the corpus would change the M4 frequency claim from "corpus-unanimous 6/6 (template)" to "k/N where M4 is the dominant default but not universal".
3. **No roadmap on a TAR paper.** Intro ends with the AICPA/offices/clients implications paragraph rather than "Section II discusses...". Mild deviation from the style_dna §8 TAR-keeps-roadmap convention; suggests the rule may soften to "TAR optional, JAR/JAE drop".
4. **F5+F2 magnitude coupling.** Block 4 reports the interquartile-shift form ("an interquartile shift... reduces the likelihood... by around 9.07 (9.44) percent") that doubles as a percent-of-base reduction; cleanest single-clause F5+F2 pairing in the corpus to date.
5. **Block 5 density.** Combines IV, entropy balancing, alternative DV proxies, expanded city/state controls, orthogonalization, subsample exclusions, switch-design Big-R falsification, cross-sectional partition by office concentration, and beyond-60-mile discriminant placebo. Use as a structural template when the contribution rests on overcoming geography-confound concerns.

---

## Annotated example: Aobdia, Choudhary, Newberger 2023 TAR (canonical 5-block exemplar with role-decomposition; `23-ACN`)

23-ACN is the most canonical intro in the augmented batch — it hits 8 of 10 self-audit items including M1A lit-baseline, M2 gap by end of Block 1, explicit M4 tension, sample-size sentence, magnitude in Block 4, "Consistent with..." lead, and TAR roadmap. Reach for this template when writing an "economics of audit production" or audit-team-composition paper with proprietary PCAOB-style data and cost-benefit framing.

| Section | Block | Move |
|---|---|---|
| ¶1: "academics, practitioners, and regulators have increasingly focused on identifying which audit production factors affect audit quality" | 1 | M1A lit-baseline; canonical M1A opener with tri-audience referent (academic + practitioner + regulator) |
| ¶1: "However, there is limited large-sample evidence of the cost-benefit tradeoffs of such audit production characteristics" | 1 | M2 conditional gap; data-scarcity framing on the cost-benefit dimension |
| ¶1: "An evaluation of who drives audit quality, not just what drives it, is critical to understanding how to improve audit quality" | 1 | M3 RQ implicit; "who not just what" framing sharpens gap into question |
| ¶2: "the lack of data available to researchers on both and the difficulty in measuring audit quality" | 1 | M2 direct gap (cause); names the binding cause — data scarcity plus measurement difficulty |
| ¶3: "Our research adds to the paucity of large-sample empirical evidence on the costs and benefits of audit production characteristics" | 1 | M3 RQ formalization; canonical "adds to the paucity" form |
| ¶4: "we exploit Public Company Accounting Oversight Board (PCAOB) proprietary data on audit production characteristics and team members" | 3 | Setting + data source; proprietary PCAOB data as setting justification |
| ¶7: "Predictions are mixed on the impact of middle management on quality and costs" | 2 | M4 tension marker; explicit M4 marker pivoting to counter-mechanism in next sentence |
| ¶7: "In contrast, PCAOB audit standards that assign the ultimate responsibility of the audit to the lead partner (AS 1201)" | 2 | Counter-mechanism; AS 1201 + organizational-hierarchy theory as counter to delegation argument |
| ¶8: "Our final sample is composed of 1,930 engagements inspected by the PCAOB between 2006 and 2015" | 3 | Sample-size sentence; canonical Block 3 form, 2006–2015 period |
| ¶9: "Consistent with Christensen et al. (2021) and Contessotto et al. (2019), we first confirm a positive association between average client experience and audit quality" | 4 | Main finding lead (canonical); uses the "Consistent with..." opener that 19-JWW and 22-LNS omit |
| ¶9: "average client expertise (pre-year-end auditing) is associated with a 2.5 (1.6)-percentage-point reduction in the incidence of restatements" | 4 | M5 F4+F1 magnitude; SD-shift coupled with percentage-point reduction in dual-DV phrasing |
| ¶10: "the positive associations between client expertise and pre-year-end auditing with audit quality are explained by middle managers and relatively more so than lead/EQR partners" | 4 | Role-decomposition finding; mid-manager partition novel relative to lead-partner literature |
| ¶11: "Turning next to the costs of these production characteristics, we find a positive association between middle management client expertise (pre-year-end auditing) and audit fees" | 4 | Cost-side secondary finding; cost-benefit tradeoff completed |
| ¶12: "We contribute to the literature by showing that, in the U.S., audit practitioners, regulators, and academics should focus on audit team composition" | Final | M6 form 4 Contribution 1; complements DeFond-Zhang 2014 lineage |
| ¶13: "Our evidence can aid practitioners by highlighting the importance of staffing, particularly in terms of the timing of audit procedures and turnover" | Final | M6 form 5 implications closer; practitioner/audit-committee audience |
| ¶14: "The remainder of this paper is structured as follows: Section II discusses the setting and prior literature; Section III" | Final | Roadmap; canonical TAR roadmap closer |

**Notable features in 23-ACN**:

1. **Cleanest M4 in the augmented batch.** "Predictions are mixed... In contrast, PCAOB audit standards..." anchors the counter-mechanism on a regulator standard (AS 1201) plus organizational-hierarchy theory rather than on prior empirical work. Reach for this M4 form when the counter-prediction has a regulatory or institutional grounding stronger than a competing empirical lit.
2. **Dual-DV parenthetical magnitude phrasing.** "2.5 (1.6)-percentage-point reduction in the incidence of restatements" pairs F4 SD-shift with F1 percentage-point and embeds a second DV (Part I Finding) in the parenthetical. Use as a corpus-novel magnitude form when reporting parallel coefficients on two audit-quality DVs without sacrificing readability.
3. **No formal H statement; RQ-framing.** Paper uses research questions (¶7 "Predictions are mixed"; ¶10 "we focus on the role of middle managers") instead of "**H1.** ... ceteris paribus". Defensible for exploratory empirical papers — pairs with 22-CHLP, 23-ZBLM, 20-CKMS, 24-Chen as the exploratory-paper variant of style_dna §8.
4. **Non-canonical block ordering 1→3→2→4→5→Final.** Block 2 (theory + tension) sits in ¶7 — after the Block 3 setting/design preview in ¶4. This is a contributions-preview architecture rather than the canonical sequence; tolerated when the design asset is part of what motivates the paper.
5. **Role-decomposition as Block 4 sub-finding.** Block 4 reports a within-team decomposition (middle-manager vs lead/EQR partner) that is itself a novel finding, not just a robustness sub-test. When the paper's contribution rests on disaggregating an aggregate effect, follow this template by placing the decomposition immediately after the headline finding.

---

## Annotated example: Aobdia 2019 JAE (RQ-first opener + three-sided tension + single-author "I"; `19-Aob`)

19-Aob is a single-author JAE paper that inverts the M1A default by leading with the research question in sentence 1, anchors Block 2 with an unusually rich three-sided tension, and frames the paper as a concordance/measurement study rather than a directional-hypothesis test. Reach for this template when the contribution is a methodological-concordance question, especially a single-authored "measurement" paper using proprietary regulatory data.

| Section | Block | Move |
|---|---|---|
| ¶1: "This study examines the degree of concordance between widely used academic measures of audit quality and the views of audit firms and regulators" | 1 | M3 research question (RQ-first opener); states the concordance question before any lit anchor |
| ¶1: "Prior accounting research introduces multiple input and output measures of audit quality based on externally observable data" | 1 | M1A lit-baseline; placed after RQ, mirrors 19-JWW inversion |
| ¶1: "However, each construct indirectly measures audit quality, and has weaknesses" | 1 | M2 conditional gap; construct-indirectness pivot to alternative approach |
| ¶1: "An alternative approach to measure audit quality is to consider practitioners' assessments of what constitutes a high-quality audit" | 1 | M2 construct-tension gap; introduces practitioner-assessment alternative |
| ¶1: "understanding the degree of concordance between practitioners' assessments of audit quality and academic measures can help determine which observable measures" | 1 | M3 RQ formalization; restates RQ in measurable form, closes Block 1 |
| ¶2: "On the one hand, auditors aim to obtain reasonable assurance about whether the financial statements are free of material misstatements" | 2 | M4 tension (pro side); AU 110 reasonable-assurance standard as pro-direction mechanism |
| ¶2: "On the other hand, based on direct evidence from the audit process, practitioners could judge an audit acceptable" | 2 | M4 tension (counter side); counter-mechanism for practitioner-academic divergence |
| ¶2: "despite their advantages, practitioner measures of audit quality could suffer from several issues" | 2 | M4 tension (third hand); adds a third tension layer on practitioner-measure limitations |
| ¶2: "I use in this study two proprietary measures of practitioners' views of audit quality, both obtained from the Public Company Accounting Oversight Board" | 3 | Setting + data source; dual-data design (regulator + audit-firm internal) |
| ¶2: "I use two reasonably large confidential datasets of 5,309 engagements inspected by the PCAOB and 2,286 internal inspections" | 3 | Sample-size sentence; dual-sample framing for triangulation |
| ¶3: "I find that unsigned discretionary accruals, unsigned total accruals, and unsigned accruals deflated by cash flow from operations are associated with Part I Findings" | 4 | Main finding lead; direct, omits canonical "Consistent with..." opener |
| ¶3: "they increase the probability of a Part I Finding by 10.1% and 5.0%, respectively" | 4 | M5 F2 percent-of-base magnitude; for restatement and small-profit DV pair |
| ¶3: "An interquartile range increase (75th percentile less 25th percentile value) in audit fees decreases the probability of a Part I Finding by 10.7%" | 4 | M5 F5 IQR magnitude; for the audit-fees input proxy |
| ¶3: "these measures explain a small portion, between 3% and 19%, of the practitioners' views" | 4 | Joint-power caveat; pre-empts referee objection on combined predictive power |
| ¶4: "I find that PCAOB inspectors are unlikely to suffer from a hindsight bias whereby they would issue Part I Findings to engagements" | 5 | Hindsight-bias placebo; falsification against mechanical restatement-to-finding inference |
| ¶4: "Overall, this study contributes to the literature in several ways" | Final | Contributions opener; signals numbered contributions follow |
| ¶4: "My study offers guidance about which publicly available measures of audit quality, for U.S. listed issuers, are predictive of the practitioners' views" | Final | M6 form 5 Contribution 1; implications-for-audience (academic users of AQ proxies) |
| ¶4: "My study also provides unique descriptive evidence about the PCAOB and internal inspection processes, based on direct access to these data" | Final | M6 form 8 Contribution 2; novel-measure / data-asset framing |
| ¶4: "One caveat is that, because PCAOB inspections are risk-based, the results perhaps cannot be generalized outside of inspected engagements" | Final | M7 closing scope/limitation; risk-based-inspection scope acknowledged before roadmap |
| ¶4: "The remainder of this paper is structured as follows. Section 2 provides background on academic and practitioners' views of audit quality" | Final | Roadmap; JAE 2019 retains roadmap (modern JAE 2024+ drops it) |

**Notable deviations in 19-Aob**:

1. **RQ-first opener inverts M1A.** Sentence 1 of ¶1 states the concordance research question; the M1A lit-baseline anchor follows. Pairs with 19-JWW, 22-FHKF, 23-ZBLM as the corpus's RQ-first family. The corpus claim "M1A 4/6 (template) default" is now better stated as "M1A dominant but RQ-first is a recognized variant for concordance / methods / first-archival-evidence papers".
2. **Three-sided M4 tension.** ¶2 layers three counter-considerations (AU 110 pro-direction · practitioner-judgment counter · practitioner-measure limitations third hand). The third hand is rare in the corpus and worth recording as an "M4 three-sided" sub-form; reach for it when the paper's measurement claim itself has known weaknesses that deserve acknowledgement in the intro.
3. **Dual-magnitude pair across adjacent sentences.** Block 4 reports F2 percent-of-base for output proxies and F5 IQR for the input (audit fees) proxy in two adjacent sentences keyed to proxy type. Use this template when output and input proxies of the same construct have different natural magnitude forms.
4. **Single-author "I" register.** All quotes use first-person singular. The DeFond/Khurana lineage uses "we" even on single-authored work; 19-Aob breaks this. JAE tolerates the singular form — pairs with 22-Dug, 24-Chen as a JAR/JAE solo-voice variant.
5. **No formal H statement.** Frames the question as measurement-concordance, not directional-hypothesis test. Defensible for methods/concordance papers; pattern matches 23-ACN — papers with "concordance"/"economics of"/"what matters for" titles default to RQ-only framing.

---

## Annotated example: Beck, Gunn, Hallman 2019 JAE (construct-tension opener + Block 2 omission + spatial-distance magnitude; `19-BGH`)

19-BGH opens with an M1D construct-introduction (decentralization) that supplies its own M2 tension, defers Block 2 (theory + formal H statements) entirely to Section 2 of the paper, and reports a corpus-novel F6 spatial-distance magnitude ("within 185 kilometers"). Reach for this template when the contribution is a puzzle-driven empirical question whose theory will be developed in the body rather than the intro.

| Section | Block | Move |
|---|---|---|
| ¶1: "Big 4 accounting firms are decentralized organizations, and individual practice offices have significant autonomy with respect to contracting and administering" | 1 | M1D construct-introduction; opens by introducing the decentralization construct rather than lit-baseline |
| ¶1: "A geographically decentralized structure is advantageous because it lowers transportation costs and reduces information asymmetry" | 1 | M1A lit-baseline; establishes prior benefit-side baseline before pivoting to cost side |
| ¶2: "While decentralization increases the proximity between auditors and clients, it also reduces the proximity between individual auditors within the audit firm" | 1 | M2 construct-tension gap; pivots benefit-side baseline into cost-side opening |
| ¶2: "we build on a number of recent studies that conclude Big 4 audit firms' large offices provide higher quality audits compared to small offices" | 1 | M3 research question setup; builds RQ on office-size-AQ lit anchor |
| ¶2: "why do Big 4 auditors not export the audit competency developed in large practice offices to other practice offices within the firm?" | 1 | M3 RQ sharpened; puzzle-form RQ anchored on Choi, Francis-Yu, Francis et al. |
| ¶3: "Our analysis reveals that the audit competency of large offices does, in fact, 'spillover' to small offices" | 4 | Main finding lead; direct, omits canonical "Consistent with our hypothesis" opener |
| ¶3: "audit quality is higher when the small office is in closer geographic proximity to a large office of the same firm" | 4 | Headline result restated; mirrors hypothesis-aligned language for H1 |
| ¶3: "within 185 kilometers [km] when we use restatements as the proxy for audit quality" | 4 | M5 F6 benchmark; corpus-novel spatial-distance threshold magnitude |
| ¶3: "A placebo variable defining proximity as the distance to any large audit office" | 5 | Placebo / falsification; placebo previewed inside Block 4 prose |
| ¶5: "We conduct interviews with representatives from each of the Big 4 audit firms to identify the location of partners tasked with oversight" | 3 | Setting + data source; proprietary partner-location interviews as novel data anchor |
| ¶5: "proximity to a large office has a greater effect on small office audit quality when an RMP is located in the large office" | 4 | Mechanism finding 1; monitoring-channel partition by RMP location |
| ¶6: "proximity to a large office has a stronger relationship with small office audit quality when that large office has relevant industry-specific experience" | 4 | Mechanism finding 2; knowledge-sharing channel partition by industry experience |
| ¶7: "we find no evidence to suggest that proximity to a large office has a differential effect on audit quality" | 4 | Null finding (resource channel); rare explicit null in Block 4 |
| ¶9: "we support our causal interpretation that RMP monitoring leads to higher audit quality by performing difference-in-differences analyses" | 5 | DiD identification; using regional leadership consolidations at two Big 4 firms |
| ¶10: "Our findings make several important contributions to the existing literature. First, we answer an important and interesting question in archival audit research" | Final | M6 form 1 Contribution 1; canonical "First, we answer..." add-to-literature form |
| ¶11: "we document the above results using a research design that addresses an important econometric concern with extant archival audit research" | Final | M6 form 4 Contribution 2; method-asset contribution addressing Minutti-Meza 2013 critique |
| ¶12: "our findings provide some of the first empirical evidence on the effectiveness of audit firms' internal monitoring" | Final | M6 form 3 Contribution 3; first-to-examine form, responds to DeFond-Zhang 2014 call |
| ¶13: "centralizing the RMP monitoring function can unintentionally exacerbate, rather than ameliorate, quality controls problems when audit offices themselves remain decentralized" | Final | M6 form 5 Contribution 4; counterintuitive policy-implications closer |

**Notable deviations in 19-BGH**:

1. **Block 2 omission (intro defers theory to §2).** No theory + M4 tension paragraph in the intro — H1/H2a/H2b/H2c and counter-mechanism discussions live entirely in Section 2.1–2.4. This is a structurally non-canonical intro layout closer to a "puzzle-driven empirics-first" form, and supports softening the corpus claim about M4 to "dominant default, deferrable when theory is foregrounded in the body".
2. **Construct-tension as opener.** M1D construct-introduction (decentralization) supplies the M2 tension *within the same construct* — decentralization is simultaneously the baseline and the puzzle. File as an M1D variant where the construct itself supplies the M2 tension; reach for it when the contribution rests on unpacking a single ambiguous organizational form.
3. **F6 spatial-distance magnitude (corpus-novel variant).** "within 185 kilometers" is a kilometer-threshold benchmark form not previously catalogued. Pairs naturally with the placebo previewed in the same paragraph; reach for it when the IV has a natural distance, time, or unit threshold.
4. **Explicit Block 4 null.** Resource-sharing channel returns a null ("we find no evidence..."). Reporting the null directly in intro Block 4, rather than burying it in §4, is rare and closer to Khurana 2026 null-protocol style.
5. **Four numbered contributions in prose.** First / Second / Third / Finally — canonical four-contribution structure with the fourth doubling as an M6 form 5 implications closer (centralization-can-exacerbate-problems paradox). The "Finally" pivot is the rhetorical centerpiece.

---

## Annotated example: Wu, Ye 2020 JAR (anecdote opener + 3-part China template + dual-DV F2 magnitudes; `20-WY`)

20-WY opens with a Deng Xiaoping anecdote (off-canon under the M1A/B/C/D taxonomy), deploys the canonical 3-part China-setting justification, and reports paired F2 percent-of-base magnitudes on dual DVs (MAO strictness and audit fees). Reach for this template when writing a China-setting DiD audit paper where the natural-experiment event has cultural / policy resonance worth exploiting.

| Section | Block | Move |
|---|---|---|
| ¶1: "Let some people get rich first!" | 1 | M1 anecdote opener (forbidden variant); Deng Xiaoping pronouncement, off the M1A/B/C/D taxonomy |
| ¶1: "Exploiting the inclusion of clients' controlling owners on the Rich List, we examine how client publicity shapes auditor decisions" | 1 | M3 RQ formalization; canonical "we examine how/whether" form despite anecdote opener |
| ¶2: "We rarely observe a large sample in which auditors strategically respond to heightened client publicity" | 1 | M2 direct gap; data-scarcity framing on auditor risk-management response |
| ¶2: "Several methodological issues plague the exploration of the" | 1 | M2 conditional gap (enumerated); three-part identification preview converts gap into design motivation |
| ¶2: "self-interested auditors are expected to take actions to minimize potential losses" | 2 | Hypothesis intuition; plain-English mechanism preview anchored on auditor self-interest |
| ¶3: "The publication of the Rich List provides us an opportunity to observe how increased publicity shapes auditor behavior" | 3 | Setting transition; frames Rich List as natural experiment |
| ¶3: "China's transition from a planned to a market economy has left various institutional voids" | 3 | China-justification (institutional feature); standard 3-part China template piece |
| ¶4: "The above reasoning suggests auditors will become stricter in auditing clients after their controlling owners are placed on the Rich List" | 2 | Hypothesis statement (narrative form); directional H stated narratively, not as formal "H1." block |
| ¶4: "we apply the difference-in-differences (DiD) design" | 3 | Identification design; DiD on first-time-listing event |
| ¶5: "Our treatment sample comprises 631 pre- and post-listing" | 3 | Sample-size sentence; treatment-control DiD framing |
| ¶5: "the strictness level of MAOs issued to the treatment firms increases by about 6.3% after the listing event" | 4 | M5 F2 percent-of-base magnitude; on ordered MAO DV |
| ¶5: "Auditors also charge higher audit fees, estimated at about 8%" | 4 | M5 F2 percent-of-base magnitude (second DV); paired dual-DV finding signature |
| ¶5: "These economically significant results survive a battery of analyses" | 5 | Robustness preview; one-sentence preview without ID-battery detail |
| ¶5: "the post-listing increase in the strictness of MAOs is concentrated among cases" | 5 | Cross-sectional partition; by wealth-generation questionability |
| ¶5: "via the privatization of state assets or tax aggressiveness" | 5 | Mechanism via cross-section; names questionability proxies (SOE privatization · tax aggressiveness · opacity · corrupt region) |
| ¶6: "the impact of rich listings is more evident among audit firms that are larger" | 5 | Auditor-attribute partition; Big-N reputation capital + conservative engagement auditors |
| ¶7: "First, we extend research on the impacts of client publicity on auditor behavior" | Final | M6 form 4 Contribution 1; complement/extend client-publicity literature |
| ¶8: "Second, our study sheds new light on how auditors respond to changes in clients' external environments" | Final | M6 form 4 Contribution 2; extends audit-environment literature |
| ¶9: "We also contribute to the literature on the 'political process' of financial reporting" | Final | M6 form 4 Contribution 3; links to Watts-Zimmerman political-cost literature |
| ¶10: "caution should be exercised when making inferences from our observations" | Final | M7 closing scope/limitation; China-specific anti-rich sentiment as generalizability constraint |
| ¶11: "The remainder of the article is organized as follows" | Final | Roadmap; JAR convention retains roadmap |

**Notable deviations in 20-WY**:

1. **Anecdote opener tolerated by JAR 2020.** ¶1 leads with Deng Xiaoping's "Let some people get rich first!" pronouncement and a scandal montage before reaching the RQ — currently listed as 0/6 (template) forbidden in intro_patterns.md. 20-WY is a JAR-tolerated counter-example, suggesting the "forbidden anecdote opener" rule should soften to "rare; tolerated in pre-2023 JAR when the anecdote carries policy resonance, not acceptable at JAR/JAE/TAR post-2023".
2. **M4 tension paragraph absent.** Block 2 develops only the pro-prediction mechanism (publicity → regulator scrutiny → auditor risk); no "however..." counter-paragraph. Aligns with 22-LNS, 22-FHKF, 22-FW, 24-Chen — corpus M4 frequency claim should be revised from "6/6 (template) unanimous" to "dominant default but not universal (k/N)".
3. **Hypothesis stated narratively.** ¶4 states the directional prediction as "The above reasoning suggests auditors will become stricter..." rather than the canonical "**H1.** ... ceteris paribus" form. Defensible for a DiD-event paper where directionality is unambiguous.
4. **Dual-DV paired-magnitude pattern.** Block 4 carries paired F2 percent-of-base magnitudes ("about 6.3%" for MAO; "about 8%" for audit fees) in adjacent sentences. Cleaner two-sentence dual-DV F2+F2 variant; use when both DVs are continuous and natural percentage scales differ.
5. **"sheds new light" usage.** style_dna §2 lists "shed light on" as a banned hedge; 20-WY uses it on Contribution 2. Pre-2023 papers tolerate it, post-2023 don't — record as a 2020-tolerable usage that would not pass a modern referee.

---

## Annotated example: Cook, Kowaleski, Minnis, Sutherland, Zehms 2020 JAE (private-firm BD setting + triple-prediction + internal-benchmark F6; `20-CKMS`)

20-CKMS departs from the conventional Big-N + public-client opener and instead opens inside reputation theory before pivoting to a private-firm broker-dealer setting where the authors observe every auditor-client match. It develops three predictions of two-sided matching rather than a single hypothesis and reports a corpus-novel internal-benchmark F6 magnitude. Reach for this template when the contribution rests on a complete-market setting that bypasses prior-lit selection critiques.

| Section | Block | Move |
|---|---|---|
| ¶1: "The role of reputation risk in the audit market has a long history in the accounting literature" | 1 | M1A lit-baseline; canonical opener anchored on DeAngelo 1981 reputation lineage |
| ¶1: "Auditing is a 'credence good' in which clients cannot fully understand the quality of the service they purchase" | 1 | M1A construct anchor; imports credence-good frame to motivate reputation mechanism |
| ¶2: "Clients relying on auditor reputation creates three implications for auditor behavior" | 2 | Mechanism preview; three-implication scaffold previews theory structure |
| ¶3: "Efforts to study how reputation concerns influence auditors' client acceptance and continuance decisions" | 1 | M2 conditional gap; names binding empirical constraint of prior reputation research |
| ¶3: "The literature studying auditor-client matches generally focuses on what are widely considered to be the most reputable auditors" | 1 | M2 direct gap; Big-4-and-public-client focus identified as corpus limitation |
| ¶4: "In this paper, we investigate three predictions of two-sided matching based on reputation in audit markets" | 1 | M3 research question; canonical form but triple-prediction architecture |
| ¶5: "We investigate these predictions in the US broker-dealer (BD) market" | 3 | Setting introduction; novel non-public-firm setting replaces conventional Big-N opener |
| ¶6: "all BDs must obtain an audit so we observe the complete BD client portfolio for all audit firms in this market" | 3 | Data-coverage advantage; universe-coverage feature addresses prior-lit selection critique |
| ¶7: "the null hypothesis is that new and existing client misconduct is unrelated" | 4 | Null framing; explicit null statement, rare in audit intros |
| ¶8: "we find an economically and statistically significant relation between new and existing client misconduct" | 4 | Main finding lead; direct, omits canonical "Consistent with our hypothesis" opener |
| ¶8: "client misconduct records are nearly half as important as client size in explaining auditor-client matching" | 4 | M5 F6 benchmark; internal-benchmark variant anchored on size comparator from same regression |
| ¶9: "one might wonder if the matching we find simply reflects a form of opinion shopping" | 4 | Alt-explanation rebuttal; pre-empts litigation-risk reframe of headline finding |
| ¶10: "We find more misconduct among BD clients of auditors without bank and IPO market exposure" | 4 | Cross-sectional corroboration; reputation-portfolio partition |
| ¶11: "post-modernization, auditors increasingly concentrate their client portfolios in a given misconduct segment" | 5 | Regulatory shock; 2007 BrokerCheck modernization as transparency shock |
| ¶12: "the identity of a BD's new auditor predicts the BD's future misconduct" | 4 | Secondary finding; forward-looking prediction extends matching result temporally |
| ¶13: "research on reputation in audit markets has been hampered by difficulties separating reputation from litigation risk" | Final | M6 form 4 Contribution 1; reframes gap as contribution, complements Weber-Skinner lineage |
| ¶14: "our setting allows us to study the entire set of auditors and clients in a market" | Final | M6 form 7 Contribution 2; universe-coverage methodological asset |
| ¶15: "our findings are relevant to recent models studying how the matching process depends on the information environment" | Final | M6 form 4 Contribution 3; bridges to theoretical matching literature outside accounting |
| ¶16: "our findings add to the growing work concerned with BD misconduct" | Final | M6 form 1 Contribution 4; add-to-literature framing for BD misconduct corpus |

**Notable deviations in 20-CKMS**:

1. **Setting-as-methodological-asset opener.** First corpus paper to open on a non-public-firm audit market (US broker-dealers) and explicitly frame this as the asset. The M2 conditional gap (litigation-vs-reputation confound) and M2 direct gap (Big-4-public-client sampling limit) appear as a doubled gap statement, both addressed by the BD setting. Canonical exemplar for **"setting-as-methodological-asset"** M6 form 7 contributions.
2. **Triple-prediction architecture instead of single-H.** Develops three predictions of two-sided matching; no formal "**H1.**" — Block 2 theory expansion sits entirely in §2. Pairs with 23-ACN, 22-CHLP, 23-ZBLM, 24-Chen as the RQ/multi-prediction variant. Reach for it when the contribution is a system of related predictions rather than a single directional test.
3. **No "Consistent with our hypothesis" opener in Block 4.** Block 4 leads with "we find an economically and statistically significant relation," skipping the canonical lead form. Consistent with 19-JWW, 22-LNS, 22-FHKF — papers without a formal H in Block 2 also drop the matching opener in Block 4.
4. **Internal-benchmark F6 magnitude variant.** "nearly half as important as client size" references the in-paper benchmark of client-size matching mechanics rather than an external literature comparator. Worth recording as an "internal-benchmark F6 variant" — the comparator is the same regression's other coefficient.
5. **Block 5 transparency-shock as identification.** 2007 BrokerCheck modernization sits in Block 4/5 hybrid space, paired with cross-sectional partition and forward-misconduct prediction rather than a discrete identification battery. Matches the corpus pattern of "regulatory shock" as a Block 5 move (~3/6 (template) frequency).

---

## Annotated example: Chen, Huang, Li, Pittman 2022 JAR (China-setting social-connections + "injecting tension" + spatio-temporal validation; `22-CHLP`)

22-CHLP follows the canonical 5-block structure for a China-setting social-connections paper, with a corpus-novel "injecting tension" M4 phrasing and a spatio-temporal coincidence validation test (fund-manager site visit timing aligned with the connected auditor's fieldwork). Reach for this template when writing a Chinese-setting paper that exploits signatory-auditor disclosure and needs to defend the directional ambiguity between information-leakage and reputation-protection channels.

| Section | Block | Move |
|---|---|---|
| ¶1: "Prior research analyzes economic outcomes stemming from social connections between corporate executives and related parties" | 1 | M1A lit-baseline; canonical opener anchored on social-connections literature |
| ¶1: "In this paper, we evaluate empirical associations consistent with mutual fund managers eliciting private information" | 1 | M3 research question; canonical "In this paper..." form closes Block 1 |
| ¶2: "The private information auditors possess is highly valuable to mutual funds in investing" | 2 | Hypothesis intuition; auditor-as-information-source argument |
| ¶2: "Auditors also secure proprietary information through informal discussions with top managers and board members of the client firms" | 2 | Mechanism elaboration; informal-channels variant of audit-as-conduit theory |
| ¶3: "However, injecting tension into our analysis, socially connected auditors eager to protect their valuable reputations" | 2 | M4 tension opener; corpus-novel "injecting tension" phrasing |
| ¶3: "whether mutual fund portfolio decisions are sensitive to fund manager" | 2 | Empirical-question resolution; routes tension to empirical question |
| ¶4: "We focus on the Chinese market in this study for several reasons" | 3 | China-setting lead; signals canonical 3-part structure |
| ¶4: "this market provides a high-power testing ground for our research questions" | 3 | Setting justification; institutional-feature anchored on guanxi-dominance |
| ¶4: "we focus on the Chinese market to capitalize on its unique data availability" | 3 | Data-availability justification; signatory-auditor disclosure enables fund-auditor matching |
| ¶6: "Education is one of the strongest forces that shape individuals' social worlds" | 2 | IV-construct intuition; school-ties IV via homophily / alumni-network mechanism |
| ¶7: "Analyzing a sample of open-end mutual funds in the Chinese market covering the period from 2004 to 2017" | 3 | Sample-size sentence; open-end mutual funds, 2004–2017 |
| ¶7: "we begin by documenting that mutual funds whose managers are socially connected with the signatory auditors" | 4 | Main finding lead; direct form, paper has no formal H |
| ¶7: "in a test that exploits mandatory auditor partner rotation as an exogenous shock" | 5 | Identification — rotation; mirrors 25-DQSZ rotation move |
| ¶8: "cross-sectional analyses reveal stronger associations between fund manager-auditor connections and stockholdings" | 5 | Cross-sectional corroboration; multi-dimensional heterogeneity preview |
| ¶9: "we document that the mutual fund manager is more likely to schedule their corporate site visit" | 5 | Validation test; corporate-site-visit timing as novel auditor-fieldwork-coincidence design |
| ¶10: "mutual fund trading on firms with connected auditors is more closely related to upcoming earnings news" | 4 | Secondary finding (trading); pre-news trading consistent with information flow |
| ¶11: "mutual funds and firms in which they invest are more likely to appoint connected auditors and pay them higher fees" | 4 | Reciprocal-side finding; closes two-way information-for-compensation loop |
| ¶12: "We make several contributions to extant research" | Final | Contribution lead; signals numbered structure |
| ¶12: "First, we extend prior work on the importance of social connections to the capital markets" | Final | M6 form 4 Contribution 1; extends social-connections-to-capital-markets literature |
| ¶13: "Second, we advance research on mutual funds that explores the channels" | Final | M6 form 4 Contribution 2; extends mutual-fund informational-advantage literature |
| ¶14: "Third, our analysis has policy implications given that information leakage from socially connected auditors" | Final | M6 form 5 Contribution 3; policy-implications closer to regulator/audit-committee audience |
| ¶15: "The rest of the paper is organized as follows" | Final | Roadmap; JAR roadmap closer |

**Notable features in 22-CHLP**:

1. **"Injecting tension" M4 variant.** Existing pattern file catalogues three canonical M4 openers; 22-CHLP adds "However, injecting tension into our analysis..." — same rhetorical function with a more active verbal construction. Reach for this when the canonical "We note, however, that there is tension..." reads too passive for the paper's voice. This is an active-phrasing M4 variant; not an M4 omission.
2. **No numeric magnitudes in Block 4.** Direction-only findings throughout ("more shares of these firms", "mutual fund performance improves"). Places 22-CHLP alongside 19-JWW, 24-Chen as a magnitude-omission case. Pre-2024 norm; modern JAR/JAE (24-DLWW, 26-KLYY) requires at least one F1/F2/F4 form.
3. **No formal "H1." statement; RQ-framing throughout.** Block 2 closes with "distils to an empirical question". Pattern matches 23-ACN, 23-ZBLM, 24-Chen — exploratory-paper RQ variant. Style_dna §8 rule should soften to "formal H expected in most cases; RQ accepted for exploratory associations papers".
4. **Block 2 / Block 3 boundary fuzziness.** Block 2 spans ¶2–¶3 and returns at ¶6 (school-ties IV intuition). The IV-construct intuition sits between Block 3 (setting) and Block 4 (findings) — non-canonical placement. Reach for this only when the IV-construct genuinely needs a theory anchor that doesn't fit in §3 design.
5. **Spatio-temporal coincidence validation test (design-novel).** ¶9 describes a validation in which the fund manager's site visit aligns with the connected auditor's fieldwork timing. Corpus-novel "spatio-temporal coincidence" identification move; reach for it when a behavioral mechanism predicts timing alignment that can be measured.

---

## Annotated example: Duguay 2022 JAR (policy-motivation opener + ¶1 M4 + single-author "I" + identification-dense Block 3; `22-Dug`)

22-Dug is a counter-template to the canonical 5-block intro in three respects: it opens with a policy-motivation form (currently flagged forbidden in the move bank), deploys M4 tension inside ¶1 rather than Block 2, and front-loads identification machinery into Block 3 that the audit-write-design skill ordinarily defers to §4. Reach for this template when writing a single-authored regulation-consequences paper with a quasi-experimental policy-variation design.

| Section | Block | Move |
|---|---|---|
| ¶1: "Financial audit regulations lie at the heart of major policy debates" | 1 | M1 policy-motivation variant (off-canon); forbidden by canonical M1A–D but tolerated here |
| ¶1: "Regulation mandating that charities have their financial statements audited is also contentious" | 1 | M2 construct-tension gap; narrows policy frame to charitable-audit specific gap |
| ¶1: "On one hand, such audit mandates could solve potential market failures or externality issues" | 1 | M4 tension (pro-side); pro-regulation half of policy-tension, unusual ¶1 placement |
| ¶1: "On the other hand, mandatory audits can represent a financial and administrative burden for charities" | 1 | M4 tension (counter-side); counter-mechanism on cost burden, closes tension in ¶1 |
| ¶2: "In this paper, I evaluate the economic consequences of financial audit regulation in the charitable sector" | 1 | M3 research question; canonical M3 form, single-author "I" voice |
| ¶4: "investigating the consequences of nonprofit audit regulation is particularly important, given its sheer economic significance" | 1 | M2 importance amplifier; setting-importance amplifier before economic-magnitude statistics |
| ¶6: "I propose that state-level audit mandates reduce donors' moral-hazard concerns for four reasons" | 2 | Mechanism preview; enumerated four-reason scaffold |
| ¶7: "I hypothesize that audit mandates lead donors to shift part of their donations toward smaller, lesser" | 2 | Hypothesis statement (narrative); no formal "**H1.**" bold |
| ¶10: "One advantage of this differential exposure design is that it mitigates concerns over the endogenous timing" | 3 | Identification design; differential-exposure design rationale |
| ¶11: "The state-year fixed effects control for differences in wealth, culture, social needs, and operating costs across states" | 3 | Fixed-effects justification; state-year FE rationale |
| ¶13: "I test my hypotheses by analyzing a comprehensive sample of public charities in the United States" | 3 | Sample-size sentence; period 1998 to 2015 follows |
| ¶13: "Consistent with my empirical predictions, I find that audit mandates are associated with a lower concentration of donations" | 4 | Main finding lead (canonical); matches DeFond default |
| ¶13: "an audit mandate of moderate scope (i.e., where about 25% of charities are required to obtain an audit)" | 4 | M5 F1 magnitude (with treatment-intensity gloss); treatment-intensity gloss precedes pp form |
| ¶14: "I also show this reallocation of donations allows the charitable sector to serve more diverse geographic areas" | 4 | Secondary finding (real effects); real-effects on diversity of charitable provision |
| ¶16: "To support the credibility of the proposed mechanism, I provide additional discussions and analyses" | 5 | Robustness lead-in; mechanism-credibility framing |
| ¶17: "My paper contributes to two streams of research. First, it complements the literature on the consequences of mandatory audits" | Final | M6 form 4 Contribution 1; two-stream framing, mandatory-audits literature |
| ¶18: "Second, I contribute to the nonprofit literature by demonstrating the real effect of audit mandates" | Final | M6 form 4 Contribution 2; real-effects framing |

**Notable deviations in 22-Dug**:

1. **Policy-motivation opener tolerated.** ¶1 sentence 1 is policy motivation — the move bank lists this as 0/6 (template) forbidden in the canonical corpus, but 22-Dug is a 2022 JAR counter-example with a quasi-experimental policy-variation design. Combined with 20-WY's anecdote opener, the "forbidden openings" claim should soften to "rare; JAR-tolerated when the policy resonance is genuine, not acceptable post-2023 at JAE/TAR".
2. **M4 tension in ¶1, not Block 2.** "On one hand … On the other hand" tension lives in ¶1 itself, immediately after the policy opener. Block 2 carries only the four-reason mechanism preview and narrative H. Combined with 22-LNS, 20-WY, 22-FHKF, 22-FW, 24-Chen — the M4-corpus-unanimous claim is no longer defensible; M4 in canonical Block 2 placement is the *dominant* form, not universal.
3. **Single-author "I" register.** Verb whitelist still holds but pronoun differs from corpus-universal "we". Pairs with 19-Aob, 24-Chen — JAR/JAE tolerance for solo voice. File as a register sub-variant, not a deviation requiring style-DNA update.
4. **Narrative H statement, no formal "**H1.**".** Section 2 may carry the formal H; the intro version is narrative. Suggests style_dna §8 intro-formal-H requirement should soften from rule to convention.
5. **Block 3 identification density.** The intro carries differential-exposure design rationale, state-year and type-year FE structure, and a simulated-instrumental-variable mention — front-loading what the audit-write-design skill says should sit in §4. Reach for this density only when the identification asset *is* the contribution (as in regulation-consequences papers).

---

## Annotated example: Fedyk, Hodson, Khimich, Fedyk 2022 RAST (RQ-first + labor-economics theory import + multi-DV magnitude + mixed-methods; `22-FHKF`)

22-FHKF is a design-driven AI-and-audit paper that opens with the broad research question in sentence 1 (RQ-first family with 19-JWW, 19-Aob, 23-ZBLM), imports its theory anchor from labor economics (Frey-Osborne automation-exposure, Babina AI labor-economics IV), and reports a corpus-novel multi-DV magnitude form (F4 SD-shift paired with four parallel F2 percent-of-base reductions). Reach for this template when the contribution is a technology-adoption question combining archival data with semi-structured interviews.

| Section | Block | Move |
|---|---|---|
| ¶1: "How does artificial intelligence (AI) affect firms' product quality and efficiency?" | 1 | M3 RQ-first opener; RQ-as-first-sentence, inverts M1A default |
| ¶1: "the evidence on whether AI can help make firms more productive remains mixed" | 1 | M1B lit-contradiction; Babina/Rock cites with explicit mixed-evidence framing |
| ¶1: "Providing compelling empirical evidence of AI's impact on firms' product quality and efficiency is challenging for two reasons" | 1 | M2 conditional gap; explicit two-cause gap framing |
| ¶1: "there is a dearth of firm-level data necessary to quantify AI adoption in individual firms" | 1 | M2 direct gap (data cause); names data scarcity at firm level |
| ¶1: "placing auditors among the occupations that are most exposed to new technologies such as AI" | 2 | M1C theory-grounded anchor; imports Frey-Osborne automation-exposure theory |
| ¶1: "our paper is the first to demonstrate the gains from AI investments for firms' product quality and efficiency" | 1 | M3 RQ formalization; restates in M6 form-3 "first-to-examine" framing |
| ¶2: "we adopt the novel measure of AI human capital proposed by Babina et al. (2020)" | 3 | M8 IV-build (borrowed measure); anchored on borrowed-and-validated novel measure from labor economics |
| ¶2: "Our sample spans 2010-2019, covers the 36 largest U.S. public accounting firms with at least 100 employees" | 3 | Sample-size sentence; firm-level sample with size threshold |
| ¶3: "we conduct in-depth semi-structured interviews with 17 audit partners representing the largest eight audit firms" | 3 | Mixed-methods anchor; interview supplement guides empirical predictions |
| ¶4: "We document that audit firms investing in AI are able to measurably lower the incidence of restatements" | 4 | Main finding lead; uses "We document" rather than canonical "Consistent with..." |
| ¶4: "a one-standard-deviation increase in the share of a firm's AI workers over the course of the prior three years" | 4 | M5 F4 magnitude (SD shift); paired with F2 percent reductions across four DVs |
| ¶5: "The reduction in restatements comes entirely from auditors' AI, consistent with the findings in Austin et al. (2021)" | 4 | Mechanism partition; auditor-AI versus client-AI decomposition |
| ¶6: "our results are stronger in subsamples where we expect AI to have greater effects" | 5 | Cross-sectional corroboration; partition by firm age, new-client status, retail industry |
| ¶7: "AI not only improves product quality but also enables audit firms to deliver the product more efficiently" | 4 | Secondary finding (efficiency); pivot from quality-side to efficiency-side findings |
| ¶9: "the reduction in accounting employees concentrates at the junior level" | 4 | Labor-decomposition finding; within-firm labor-tier partition novel to corpus |
| ¶10: "This offers novel insight to the recent literature on the adoption and economic impact of AI" | Final | M6 form 4 Contribution 1; AI-economics literature |
| ¶11: "Our results also speak to the literature on audit quality" | Final | M6 form 4 Contribution 2; audit-quality literature |
| ¶11: "we contribute a novel perspective to the literature on the effects of new technologies on audit" | Final | M6 form 3 Contribution 3; first-to-examine framing on technology-in-audit |
| ¶12: "The remainder of the paper proceeds as follows" | Final | Roadmap; explicit roadmap retained per RAST/TAR convention |

**Notable deviations in 22-FHKF**:

1. **RQ-first opener.** Sentence 1 is the broad RQ; M1B lit-contradiction and M2 gap follow in the same paragraph. Second corpus paper after 19-JWW to invert M1A — strengthens the RQ-first counter-template pattern alongside 19-Aob and 23-ZBLM.
2. **M1C theory import from labor economics.** Theoretical anchor (Frey-Osborne 2017 automation-exposure + Babina et al. 2020 AI-productivity) is imported from labor economics rather than accounting theory. Corpus-novel M1C source domain; closer analogue is 26-KLYY's cultural-transmission anchor. File as M1C-via-labor-economics sub-variant.
3. **M4 tension paragraph absent.** Like 22-LNS, 20-WY, 22-FW, 24-Chen, the paper omits the canonical M4 counter-paragraph. Cost-benefit framing in §2.2 hints at tension but is presented as a finding (quality AND efficiency improve), not as competing predictions. Further weakens the "M4 corpus-unanimous" claim.
4. **Multi-DV magnitude form (corpus-novel).** F4 SD-shift paired with four parallel F2 percent-of-base reductions (5.0% restatements, 1.4% material, 1.9% accruals/revenue, 0.3% SEC investigations) in one sentence. Cleaner even than 23-ACN's dual-DV parenthetical; reach for this when reporting a single IV effect on multiple parallel DVs.
5. **Mixed-methods anchor.** 17-partner interview supplement is non-decorative: six interview insights set the empirical predictions and motivate the auditor-AI vs client-AI partition. Mixed-methods integration is unusual in the corpus; reach for it when archival data alone cannot identify the mechanism.

---

## Annotated example: Fox, Wilson 2022 RAST (paucity-of-insight M1A + cockroach-theory anchor + time-decline magnitude; `22-FW`)

22-FW is a tax-and-restatement nexus paper whose intro is close to the canonical 5-block structure but uses a paucity-of-insight M1A framing, substitutes a three-reasons enumeration plus cockroach-theory anchor for canonical theory derivation, and reports a corpus-novel time-decline magnitude form (600 days → 2 days). Reach for this template when the dependent variable is a latency / timeliness measure and the paper extends a single anchor study (here, Bozanic et al. 2017).

| Section | Block | Move |
|---|---|---|
| ¶1: "Research provides limited insight into what draws the attention of tax authorities to public information" | 1 | M1A lit-baseline; opener with embedded gap, paucity-of-insight framing |
| ¶1: "We investigate whether the IRS uses public information to obtain qualitative signals about firms' information environment or management integrity" | 1 | M3 RQ; canonical M3 statement pivots from gap to investigated relation |
| ¶2: "The IRS and other tax authorities face increasing resource constraints" | 1 | Policy motivation anchor; resource-scarcity framing motivates signal-deployment RQ |
| ¶2: "In this environment, the need for informative signals to better deploy limited resources is greater than ever" | 1 | Motivation reinforcement; reinforces policy stakes |
| ¶3: "It remains unknown whether the IRS's interest in public information extends beyond tax disclosures to more qualitative signals of potential tax misreporting" | 1 | M2 direct gap; positions paper as extension of Bozanic et al. lineage |
| ¶3: "Building on the analysis of Bozanic et al. (2017), we examine instances of financial restatements as potentially useful signals to the IRS" | 1 | M3 RQ formalization; anchors RQ on single prior paper |
| ¶4: "Financial restatements are likely to draw the attention of the IRS for the following three reasons, which are not necessarily mutually exclusive" | 2 | Mechanism enumeration; three-reasons enumeration substitutes for formal theory walk |
| ¶4: "The latter two reasons fall under the cockroach theory, which predicts that, where one problem surfaces, more are likely to be revealed" | 2 | Theory anchor; cockroach-theory anchor for spillover-from-restatement-to-tax mechanism |
| ¶5: "We measure IRS scrutiny by implementing an approach similar to that used by Bozanic et al. (2017)" | 3 | Setting + measure source; borrows measurement strategy from anchor paper |
| ¶6: "We find that, relative to all other public filings and relative to the same nonrestating forms" | 4 | Main finding lead; direct, omits canonical "Consistent with..." opener |
| ¶6: "The average time to download a restatement related filing in 2006 was over 600 days and declined to just two days in 2016" | 4 | M5 time-decline magnitude; corpus-novel form substituting for pp/% effect-size |
| ¶7: "This design partially allays concerns over endogeneity because the timing of the event is specific to the signal of the restatement" | 5 | Identification preview; event-study timing embedded inside Block 4 narrative |
| ¶8: "attributable to fraud result in an incremental increase in attention, relative to restatements stemming from the misapplication of GAAP" | 4 | Cross-sectional partition; restatement-type partition, fraud vs GAAP-misapplication |
| ¶8: "We find that Big R restatements significantly increase IRS attention, suggesting that restatements perceived as more severe trigger a greater increase in information acquisition" | 4 | Severity partition; Big-R-vs-little-r intensive-margin corroboration |
| ¶9: "we investigate IRS attention following a firm's disclosure of material weaknesses" | 4 | Extension test; broadens signal-class beyond restatements |
| ¶10: "Using path analysis, we find evidence that, as firms receive more attention from tax authorities following a restatement, there is a subsequent increase" | 4 | Consequences via mediation; path-analysis linking IRS attention to downstream tax outcomes |
| ¶11: "Our results are consistent with the IRS paying attention to qualitative signals of tax misreporting that are not directly tied to tax accruals or tax disclosures" | Final | M6 form 1 Contribution 1; extends IRS-public-info use beyond Bozanic tax-disclosure setting |
| ¶12: "By showing that IRS attention increases following a restatement, we broaden the implications of financial misreporting to include another important stakeholder" | Final | M6 form 4 Contribution 2; adds tax authority as restatement-cost stakeholder |
| ¶13: "Our results also add to the ongoing debate about the connection between aggressive financial and tax reporting" | Final | M6 form 1 Contribution 3; book-tax-aggressiveness link debate |
| ¶14: "We recognize that our measure of IRS attention has limitations" | Final | M7 closing limitation; opaque-process and proxy-validity acknowledgements |

**Notable deviations in 22-FW**:

1. **Time-decline magnitude form (corpus-novel F7).** Block 4 reports magnitude in time-units ("600 days → 2 days") rather than canonical pp / % / SD / decile / IQR. Worth recording as a candidate F7 time-decline sub-form for results-section papers where the DV is latency / timeliness.
2. **M4 tension omission in intro.** No explicit "We note, however, that there is tension..." paragraph; counter-mechanism (restatements may not draw IRS interest because earnings restate downward) deferred to §2.3 hypothesis development. Joins 22-LNS, 20-WY, 22-FHKF, 24-Chen as M4-omission cases — corpus M4 claim needs revision.
3. **Gap statement deferred past ¶1.** Formal M2 direct gap ("It remains unknown whether...") appears in ¶3 rather than canonical end-of-¶1 placement. ¶1 carries implicit gap ("Research provides limited insight..."); ¶2 inserts a policy/resource-constraint motivation between the two gap statements. Reach for this when the policy stakes need a paragraph of their own.
4. **No formal H statement in intro.** Hypotheses H1, H2a, H2b, H3 appear in §2.3, not in the intro. Follows older RAST convention of stating Hs only in development section; consistent with paper's RAST venue and 2022 date.
5. **Dual-literature closer.** Contributions 1 (IRS-public-info-use) and 2 (restatement-cost-stakeholder) are followed by Contribution 3 (book-tax-aggressiveness debate) — canonical "tax-restatement-nexus" contribution pattern: anchor + restatement-cost extension + book-tax-debate closer.

---

## Annotated example: Pan, Shroff, Zhang 2023 JAE (bullet-train shock + M4-in-¶1 + minimalist Final block; `23-PSZ`)

23-PSZ is a "Dark Side" overturning thesis built on the staggered introduction of Chinese bullet trains as plausibly exogenous shocks to audit-market competition. It folds the M4 two-sided theoretical tension *inside* Block 1 rather than deferring it to a standalone Block 2 paragraph, pairs M1A lit-baseline with M1B lit-contradiction in a hybrid opener, and closes with a minimalist single-paragraph Final block. Reach for this template when the design asset (exogenous shock) is the contribution and the JAE minimalist closer is the venue norm.

| Section | Block | Move |
|---|---|---|
| ¶1: "Understanding how audit market competition affects audit quality is of significant interest to academics, practitioners, and regulators" | 1 | M1A lit-baseline; canonical opener with tri-audience referent |
| ¶1: "From a theoretical perspective, it is unclear what effect audit market competition has on equilibrium audit quality" | 1 | M4 tension preview; two-sided tension flagged early, inside Block 1 |
| ¶1: "Prior studies examine the relation between audit market concentration, the typical proxy for competition, and audit quality and/or fees, but find mixed evidence" | 1 | M1B lit-contradiction; mixed-evidence framing motivates "Dark Side" overturning thesis |
| ¶1: "there is a lack of consensus among academics and practitioners on whether competition increases or decreases audit quality" | 1 | M2 conditional gap; consensus-absence framing anchored on DeFond-Zhang 2014 review |
| ¶2: "A primary reason for the mixed evidence on the relation between audit market competition and audit quality is that existing proxies" | 1 | M2 direct gap (cause); names binding cause as measurement error |
| ¶3: "In this paper, we examine whether audit market competition improves or worsens equilibrium audit quality using plausibly exogenous changes" | 1 | M3 research question; canonical "In this paper, we examine whether..." form |
| ¶3: "We use the staggered introduction of bullet trains across prefectural cities in China between 2008 and 2017 as shocks to travel time" | 3 | Setting + design; quasi-experimental setting as competition shock |
| ¶4: "The Chinese setting not only provides plausibly exogenous variation in audit market competitiveness, but also allows us to measure audit quality" | 3 | China setting justification; identification asset plus measure availability |
| ¶5: "Using data from 2007 to 2017 and a generalized difference-in-differences design, we find that the introduction of bullet trains leads to" | 4 | Main finding lead; canonical "we find" lead paired with DiD design statement |
| ¶5: "a 4.5 percentage point (pp) increase in the probability that a company headquartered in that city violates GAAP" | 4 | M5 F1 magnitude; pp form on primary GAAP-violation DV |
| ¶5: "These results are consistent with the hypothesis that competition increases auditors' focus on client retention" | 4 | Mechanism interpretation; canonical "consistent with" interpretation, client-retention channel |
| ¶5: "We find no evidence of a pre-treatment trend in audit quality before the inception of bullet train operations in a city" | 5 | Parallel-trends check; supports parallel-trends assumption |
| ¶6: "We find that the negative relation between bullet train connectivity and audit quality is stronger when bullet trains impose greater competitive pressure" | 5 | Cross-sectional partition; competition-intensity gradient corroborates mechanism |
| ¶7: "We find that the negative effect of competition on audit quality is weaker when clients demand high-quality audits ex ante" | 5 | Cross-sectional partition; demand-side moderation corroborates bargaining channel |
| ¶8: "We conduct an instrumental-variable test and a placebo test to mitigate the concern that factors correlated with the introduction of bullet trains" | 5 | Identification battery; IV + placebo battery |
| ¶9: "new bullet train routes in provincial cities are not associated with audit quality changes for companies located in these cities" | 5 | Placebo test; placebo on provincial cities yields null |
| ¶10: "bullet train connectivity is not associated with changes in the quality of pre-audit earnings" | 5 | Discriminant null; pre-audit-earnings null isolates auditor-behaviour channel |
| ¶11: "This paper contributes to the literature by using a plausibly exogenous shock to audit market competition that helps us test the causal relation" | Final | M6 form 7 Contribution 1; design-asset framed, single-paragraph contribution form |
| ¶12: "we caveat that our inferences are based on analyses of companies and auditors in China, where the regulatory and institutional environment is weaker" | Final | M7 closing scope/limitation; canonical 4/6 (template) corpus placement |

**Notable features in 23-PSZ**:

1. **M4 tension folded into Block 1.** ¶1 sentence 2 ("From a theoretical perspective, it is unclear...") flags two-sided tension *inside* Block 1; the intro has no standalone Block 2 tension paragraph (Section 2 of the paper expands it). Active M4 phrasing inside the opener — not an M4 omission. Joins 22-CHLP variants but with earlier placement; reach for this when the tension is short enough to live in the gap statement itself.
2. **M1A + M1B hybrid opener.** Row 3 ("Prior studies... but find mixed evidence") plus the "Dark Side" title framing meets the M1B test (overturning a prior finding), but the paper opens with M1A baseline rhetoric. Corpus-novel hybrid; reach for it when the JAE convention requires softening contradiction inside a baseline opener.
3. **Single-paragraph Final block (JAE minimalist).** Only one contribution paragraph plus an M7 limitation — no numbered "First, Second, Third" contributions. Defensible because the contribution is framed entirely around the design asset (exogenous shock). Modern JAE minimalist variant.
4. **Parallel-trends check inside Block 4.** Pre-trend evidence immediately follows magnitude reporting in ¶5 rather than waiting for a dedicated identification block. DiD-paper convention; reach for it when parallel-trends is conceptually part of believing the headline number.
5. **F1-only intro magnitude.** 4.5 pp / 1.7 pp / 1.6 pp on three DVs reported without F2 percent-of-base translation, F4 SD-shift, or F6 literature benchmark. Less rich than F4+F1 (23-ACN) or F5+F2 (22-LNS) coupling; defensible when the F1 effect is large enough to stand alone.

---

## Annotated example: Zimmerman, Barr-Pulliam, Lee, Minutti-Meza 2023 JAR (RQ-first + enumerated 4-issue M4 + odds-ratio magnitude + process-positive/output-null pairing; `23-ZBLM`)

23-ZBLM inverts the canonical M1A opener with an M3 RQ-first sentence, deploys a corpus-novel enumerated four-issue M4 tension (knowledge gap, coopetition, vague standards, moral hazard), reports magnitude as an odds-ratio (corpus-novel for intros), and juxtaposes a process-side positive finding with an output-side null. Reach for this template when writing a first-archival-evidence paper on a multi-faceted auditor decision (specialist use, AI adoption, in-house resources) that requires multiple counter-mechanisms.

| Section | Block | Move |
|---|---|---|
| ¶1: "In this study, we examine the consequences of using auditor-employed specialists in audit engagements" | 1 | M3 RQ-first opener; pre-empts theory baseline with direct scope statement |
| ¶2: "Despite the growing importance of specialists, data on this aspect of audit engagements are not available from public sources" | 1 | M2 direct gap; canonical data-scarcity framing |
| ¶2: "We are among the first to provide archival evidence and answer multiple calls for additional research in this area" | 1 | M6 form 3 first-to-examine (preview); contribution preview embedded in Block 1 |
| ¶3: "we provide descriptive evidence that specialists' involvement is increasingly prevalent in our sample of inspected engagements" | 3 | Descriptive-evidence lead; uncommon Block 3 opener |
| ¶4: "Second, we turn to the most important aspect of our study, examining the association between auditors' use of specialists and audit quality" | 2 | Hypothesis-development bridge; flags central audit-quality test |
| ¶4: "On the one hand, involving specialists deepens the audit team's pool of expertise and may increase audit quality" | 2 | Hypothesis intuition (positive side); expertise-pooling mechanism |
| ¶4: "the effective use of specialists' work in audit procedures has at least four important challenges" | 2 | M4 tension (enumerated counter); four-issue tension structure |
| ¶4: "auditors face a moral hazard problem when deciding whether to use specialists and how much effort they should spend" | 2 | Counter-mechanism (moral hazard); agency-theory anchor |
| ¶4: "make the association between the use of specialists and audit quality an open empirical issue" | 2 | Net-resolution closer; canonical close of two-handed tension |
| ¶5: "We use a combination of proxies to examine audit quality from the process- and output-based perspectives" | 3 | Setting + DV taxonomy; DV plurality flagged early |
| ¶5: "use entropy balancing to mitigate concerns that engagements with different levels of specialist involvement systematically differ" | 3 | Identification preview; entropy balancing as observable-imbalance fix |
| ¶6: "We document that the use of specialists is positively associated with the incidence of audit process deficiencies" | 4 | Main finding lead; uses "document" rather than canonical "Consistent with" |
| ¶6: "moving from a relatively low to a high level of specialist involvement increases the odds of a Part I finding related to complex estimates by 50%" | 4 | M5 odds-ratio magnitude; corpus-novel form distinct from F1/F2/F4 |
| ¶6: "we do not find robust evidence that the use of specialists is associated with output-based proxies for audit quality" | 4 | Null secondary finding; output-side null adjacent to process-side positive |
| ¶6: "We acknowledge that the PCAOB selects engagements for inspection using a confidential risk-based approach" | 5 | Identification caveat; signals robustness section addresses selection concern |
| ¶6: "the baseline positive association between the use of specialists and process deficiencies is stronger when the client's board of directors has low accounting expertise" | 5 | Cross-sectional partition; board-expertise partition corroborates baseline |
| ¶8: "We only find that auditors' use of specialists is positively associated with the incidence of impairments" | 4 | Secondary finding (mechanism); impairment-incidence as estimate-level evidence |
| ¶8: "We find that specialist use is positively related to team hours and negatively related to realization rates" | 4 | Cost-side secondary finding; mirrors quality-side, completes cost-benefit framing |
| ¶9: "Overall, this study provides a contemporary institutional background and new evidence on auditors' use of their in-house" | Final | M6 closing summary; "Overall" close summarizing contribution |
| ¶9: "Our findings align with concerns noted by the PCAOB and prior experimental and survey studies about complex estimates and auditors' use of specialists" | Final | M6 form 4 Contribution 1; aligns archival evidence with PCAOB + experimental lineage |
| ¶9: "Our study also contributes to the literature on auditors' decisions in the allocation of effort during the audit process" | Final | M6 form 4 Contribution 2; audit-effort allocation literature |
| ¶9: "extends a stream of research that uses proprietary PCAOB data to examine the determinants and consequences of auditors' decisions during the audit process" | Final | M6 form 4 Contribution 3; proprietary-PCAOB-data stream (Aobdia; Gipper-Hail-Leuz lineage) |

**Notable features in 23-ZBLM**:

1. **RQ-first opener.** Sentence 1 of ¶1 states the RQ directly with no preceding lit-baseline. Joins 19-JWW, 19-Aob, 22-FHKF as the corpus's RQ-first family. Consider promoting this as a recognized M3 sub-pattern rather than flagging as deviation.
2. **Enumerated four-issue M4 tension (corpus-novel).** Block 2 lists four numbered tensions (knowledge gap, coopetition, vague standards, moral hazard) rather than the canonical single tension paragraph. Each issue is expanded in §2.2. Corpus-novel M4 variant; reach for it when the counter-mechanism has multiple independent components rather than one unified counter-theory.
3. **Odds-ratio magnitude form (F8, corpus-novel for intro).** Block 4 reports "increases the odds of a Part I finding by 50%" — neither F1 pp, F2 percent-of-base, F4 SD-shift, F6 benchmark, nor F7 time-decline. Add as F8 odds-ratio with 23-ZBLM as founding exemplar; standard in logit tables but rare as intro magnitude.
4. **Process-positive paired with output-null.** ¶6 sequences "positively associated with process deficiencies" → "we do not find robust evidence... output-based proxies". Deliberate dual-DV juxtaposition complicating the audit-quality construct (per DeFond-Zhang 2014). Reach for this when the construct itself has known process/output divergence that the paper exploits as a feature.
5. **No formal H + no roadmap.** Uses primary research question form ("Our primary research question is..."), parallel to 23-ACN, 22-CHLP, 20-CKMS, 24-Chen. Intro ends at ¶9 with the third contribution; no "The remainder of this paper..." sentence. Supports softening style_dna §8: JAR exploratory archival papers may state RQs not formal Hs, and JAR drops roadmaps.

---

## Annotated example: Chen 2024 JAR (single-author "I" + M1A+M1C hybrid + employee-lawsuit setting + direction-only Block 4; `24-Chen`)

24-Chen is a single-author JAR audit-labor-economics paper that follows a near-canonical 5-block arc but inverts voice register ("I" throughout) and imports the theory anchor (employer reputation / signaling) from outside the audit literature while sitting inside an M1A lit-baseline opener. Reach for this template when writing a solo-authored audit paper that exploits a labor-side outcome (talent acquisition, retention) and connects it to downstream audit quality.

| Section | Block | Move |
|---|---|---|
| ¶1: "The audit industry is knowledge-intensive, with quality employees being a key input into audit services" | 1 | M1A lit-baseline; canonical opener anchored on knowledge-intensive-industry framing |
| ¶1: "Despite the importance of cultivating a skilled workforce in the audit industry, we know very little about the factors influencing talent acquisition" | 1 | M2 direct gap; data-scarcity framing on talent-acquisition dimension |
| ¶1: "In this study, I examine whether employee lawsuits filed against an audit office hinder an office's ability to recruit quality employees" | 1 | M3 research question; canonical M3 closer of Block 1, pairs labor-market DV with AQ DV |
| ¶2: "First, employee lawsuits are prevalent in audit firms. From 2005 to 2018, 25% of Big 4 audit offices" | 1 | M2 institutional anchor; prevalence statistic motivating setting |
| ¶3: "An office's involvement in employee lawsuits provides a salient signal of its working conditions and corporate culture" | 2 | Hypothesis intuition (signaling); M1C-flavored theory import from firm-reputation literature |
| ¶4: "competent job applicants value an audit office's work culture and treatment of its employees and can differentiate themselves in the labor market" | 2 | Mechanism close; self-selection channel on observed culture signal |
| ¶4: "they may be less inclined to join an audit office after an employee lawsuit" | 2 | Prediction statement; informal directional prediction, formal H deferred to §2.3 |
| ¶5: "I overcome this challenge by collecting publicly available professional profiles of all individuals who report any instance of working in an audit position" | 3 | M8 novel-measure (IV-build); from public auditor profiles, addresses data-scarcity gap |
| ¶5: "all incoming auditors of Big 4 audit offices from 2005 to 2018, which contains 45,711 individual-year observations" | 3 | Sample-size sentence; individual-auditor panel rather than client-firm panel |
| ¶6: "Utilizing a generalized difference-in-differences (GDD) approach, I find that the quality of an audit office's incoming auditors declines following an employee lawsuit" | 4 | Main finding lead; GDD identification mentioned in same sentence, omits "Consistent with..." |
| ¶6: "Cross-sectionally, the adverse lawsuit effect on talent acquisition is more pronounced when an audit office is undergoing higher growth" | 5 | Cross-sectional partition; growth and media-coverage moderators previewed |
| ¶7: "I find the likelihood of financial restatements among clients served by an audit office increases after the office faces employee lawsuits" | 4 | Secondary AQ finding; closes talent-channel → audit-quality chain |
| ¶8: "To the best of my knowledge, this study is the first to examine employee lawsuits filed against audit offices" | Final | M6 form 3 Contribution 1; first-to-examine, distinguishes from accounting-lawsuit literature |
| ¶8: "this study also responds to the call from the labor economics literature for research identifying firm attributes that influence job seekers" | Final | M6 form 4 Contribution 2; complements labor-economics employer-attributes literature |
| ¶9: "My study extends their work by showing that employer reputation also affects the quality of talent attracted" | Final | M6 form 4 Contribution 2b; extends Turban-Cable employer-reputation lineage from quantity to quality |
| ¶10: "This study also contributes to an emerging literature that investigates the role of human capital in audit firms" | Final | M6 form 4 Contribution 3; human-capital-in-audit literature, individual-auditor-level measure as differentiator |

**Notable deviations in 24-Chen**:

1. **Single-author "I" register.** First-person singular throughout ("I examine", "I find", "My study extends"). Style_dna §6 says "we" is universal even on single-authored work; 24-Chen breaks this. Joins 19-Aob, 22-Dug — JAR/JAE solo-voice variant. Reach for "I" when the paper is dissertation-derived solo work in JAR.
2. **M1A + M1C theory-import hybrid.** Opener cites Aobdia-Srivastava-Wang 2018 and CAQ 2018 (audit-lit baseline) but the substantive theory anchor (employer reputation, signaling) is imported from labor economics / firm-reputation literature. Functionally M1A surface with M1C theoretical substance. Reach for this hybrid when the audit-lit baseline is thin and the conceptual heavy lifting needs an outside theory.
3. **No formal H in the intro.** Block 2 closes with informal "they may be less inclined to join" prediction; formal "**H1.**" deferred to §2.3. Pairs with 23-ACN, 23-ZBLM, 20-CKMS, 22-CHLP — JAR-tolerated exploratory variant.
4. **No M4 tension paragraph.** Block 2 lacks canonical "We note, however, that there is tension..."; counter-mechanism (remedial HR changes, reputation-repair, Chakravarthy-DeHaan-Rajgopal 2014) sits in §2.3 rather than the intro. Combined with 22-LNS, 20-WY, 22-FHKF, 22-FW — M4 should be downgraded from "corpus-unanimous" to "k/N dominant default".
5. **No magnitude in Block 4 of the intro.** Main finding ("quality of incoming auditors declines") is direction-only; no pp / SD / decile magnitude in the intro itself. Style_dna §7 says "Block 4 MUST have at least ONE numerical magnitude" — 24-Chen breaks this rule (similar to 19-JWW, 22-CHLP). The pre-2024 magnitude-omission tolerance is fading; do not replicate in 2024+ submissions.

---

## Annotated example: De Franco, Guan, Zhou, Zhu 2024 JAR (IBBEA banking-deregulation + 4-mechanism Block 2 + F1+F2 dual-DV pairing; `24-DGZZ`)

24-DGZZ is a US-setting JAR paper that exploits staggered IBBEA banking-deregulation as the identification asset, develops an unusually long four-mechanism Block 2 walk, and reports F1+F2 magnitudes paired on dual audit-quality DVs (Big-N share and industry expert). Reach for this template when writing a within-country quasi-experiment paper whose mechanism story has multiple independent supply-side and demand-side channels.

| Section | Block | Move |
|---|---|---|
| ¶1: "Understanding the forces that determine firms' auditor choice decisions, an important aspect of audit quality" | 1 | M1A lit-baseline; canonical opener anchored on audit-quality construct |
| ¶1: "places much less emphasis on how institutional factors such as the development of capital markets" | 1 | M2 conditional gap; names institutional-factors gap left by firm-characteristics literature |
| ¶1: "The issue of correlated, omitted variables, however, poses a challenge for these cross-country studies" | 1 | M2 direct gap (cause); identifies binding identification cause |
| ¶2: "We exploit the staggered adoption of the Riegle-Neal Interstate Banking and Branching Efficiency Act (IBBEA)" | 3 | Setting + design; staggered IBBEA adoption as identification asset |
| ¶2: "This setting allows us to study the impact of credit market development on auditor choice" | 1 | M3 RQ formalization; non-canonical placement after Block 3 setup |
| ¶2: "We extend existing international research by providing causal evidence on this relation in the United States" | 1 | M3 RQ extension; positions contribution against international cross-country studies |
| ¶3: "Firms trade off the benefits and costs when choosing an auditor" | 2 | Theory anchor (benefits/costs); agency-cost theory opens Block 2 |
| ¶4: "It is unclear ex ante whether firms' demand for higher quality audit services will increase or decrease" | 2 | M4 tension lead; canonical "unclear ex ante" opens directional ambiguity |
| ¶4: "If firms engage a higher quality auditor to facilitate external financing, as the literature suggests" | 2 | Mechanism (supply-side); expanded bank credit reduces demand for higher-quality audit |
| ¶5: "Firms must also consider the demand for higher quality financial statements (which higher quality auditors provide)" | 2 | Mechanism (demand-side); out-of-state entering banks raise information-asymmetry demand |
| ¶5: "entering banks have lending expertise, they may substitute their better lending skill and private and soft information" | 2 | Counter-mechanism; lending-skill substitution channel |
| ¶6: "improved bank lending practices that result from deregulation can further reduce the demand for monitoring by other capital providers" | 2 | Delegated-monitoring mechanism; Diamond/Fama anchor |
| ¶7: "Our stacked difference-in-differences (DiD) regressions offer empirical evidence that is consistent with banking deregulation" | 4 | Main finding lead (canonical); pairs stacked DiD design with directional finding |
| ¶7: "Using a large panel of firm-year observations for 7,854 unique U.S. firms during the 1988 to 2010 sample period" | 3 | Sample-size sentence; embedded inside main-finding paragraph |
| ¶7: "firms headquartered in IBBEA-adopting states are 1.8% less likely to engage a Big N auditor" | 4 | M5 F1+F2 magnitude; F1 pp on Big-N-share DV with companion F2 % of base |
| ¶8: "we document that banking deregulation has a more pronounced negative effect on the demand for a higher quality auditor" | 4 | Cross-sectional corroboration; partition on external-financing dependence |
| ¶8: "A caveat of these cross-sectional analyses is that we are unable to clearly identify our mechanisms" | 4 | M7 inline caveat (mechanism); pre-empts referee objection on coarse partitions |
| ¶9: "As a robustness test, we conduct a dynamic DiD analysis surrounding the staggered deregulatory events" | 5 | Dynamic-DiD robustness; addresses pre-trend concern |
| ¶9: "As a placebo test, we randomly assign the interstate branching deregulation years in our sample to each deregulating state" | 5 | Placebo (pseudo-event); random reassignment of deregulation years |
| ¶9: "banking deregulation has a negative impact on the financial reporting quality of firms headquartered in the affected states" | 4 | Secondary finding (FRQ corroboration); corroborates audit-demand channel |
| ¶10: "we establish a causal link between banking deregulation and firms' auditor choices" | Final | M6 form 7 Contribution 1; single-country quasi-experiment as method asset |
| ¶10: "extant research on the determinants of auditor choice focuses mainly on firm characteristics" | Final | M6 form 6 gap-fill; positions paper against firm-characteristics-only literature |
| ¶11: "our paper adds to the literature that examines the role of audits in debt financing and bank lending decisions" | Final | M6 form 4 Contribution 2; complements audit-and-debt-financing literature |

**Notable features in 24-DGZZ**:

1. **M3 RQ split across Block 1 and Block 3.** RQ formalization ("This setting allows us to study...") and extension ("We extend existing international research...") both sit in ¶2 *after* the IBBEA setting introduction. No canonical "The purpose of this study is to examine whether..." in Block 1. File as a setting-embedded M3 variant; reach for it when the setting itself is what makes the RQ tractable.
2. **Four-mechanism Block 2 walk (corpus-longest).** ¶3–¶6 develop four distinct mechanisms before the main finding: cost-of-credit (supply-side), information-asymmetry-from-entering-banks (demand-side), lending-skill substitution (counter), delegated-monitoring (counter). M4 tension marker is at the *head* of the walk in ¶4, not at the end. Reach for this when the directional prediction has multiple independent supply and demand channels.
3. **F1+F2 magnitude pairing on dual DVs.** Magnitudes on TWO audit-quality proxies (Big N and industry expert) using F1 pp + F2 percent-of-base pairing for both. Structurally similar to 23-ACN's dual-DV phrasing; corpus pattern emerging: when the paper uses two audit-quality DVs, magnitudes are reported on both in the same paragraph in F1+F2 form.
4. **Inline mechanism caveat.** ¶8 ends with "A caveat of these cross-sectional analyses is that we are unable to clearly identify our mechanisms... We consider these analyses to be more suggestive than conclusive." Inline M7-style caveat that pre-empts referee objection but is placed mid-intro rather than in a dedicated closing-scope paragraph. Reach for it when the cross-sectional partitions are obviously coarse.
5. **No closing limitation; no roadmap.** Unlike most corpus papers, 24-DGZZ closes directly on C2 with no scope/generalizability disclaimer (the within-US setting is treated as a feature) and no roadmap. Consistent with the JAR/JAE convention of dropping roadmaps; supports the rule "TAR keeps roadmaps, JAR/JAE drop".

---

## Annotated example: Dhaliwal, Lamoreaux, Litov, Neyland 2016 JAE (extreme M1A-bypass + no M2 gap + concurrent-paper differentiation + dual-DV CAR magnitude; `16-DLLN`)

16-DLLN is the most aggressive M1A-inversion in the augmented batch — Block 1 has zero lit-baseline anchor AND no M2 gap, with ¶1 leading on the RQ plus a hypothesis preview while all lit anchors are deferred to §2. Reach for this template when writing a 2016-era JAE M&A-audit paper where the contribution is a portfolio-level conflict-of-interest finding and the design rests on a long US M&A panel.

| Section | Block | Move |
|---|---|---|
| ¶1: "We examine acquisition outcomes when the same auditor audits the financial statements of both a bidder and a target firm" | 1 | M3 RQ-first opener; sentence-1 RQ, no M1A anchor precedes |
| ¶1: "We hypothesize that shared auditors facilitate the flow of information between bidders and targets" | 1 | Hypothesis preview; folded into ¶1, ahead of Block 2 derivation |
| ¶1: "the benefits of such mitigated information asymmetry accrue primarily to the acquiring firm" | 1 | Asymmetric-prediction signal; flags asymmetric direction inside opener |
| ¶2: "External auditors have unique access to senior executives, participate in audit committee meetings" | 2 | Mechanism intuition; information-intermediary mechanism anchored on auditor access |
| ¶3: "With lower bid competition, an acquirer with a shared auditor has the opportunity to negotiate a more favorable price for the target firm" | 2 | Mechanism — bargaining channel; bargaining-power channel from info advantage to deal price |
| ¶4: "Therefore, we expect the shared auditor effect on deal outcomes to be more pronounced if the bidder and acquirer contract with the same auditor practice office" | 2 | Office sub-mechanism prediction; office-level intensification |
| ¶6: "As sharing confidential information about target clients with acquirer clients appears to be a violation of conflict of interest rules" | 2 | M4 normative-tension pre-emption; acknowledges predicted behavior violates conflict-of-interest rules |
| ¶6: "we expect that higher (lower) quality auditors would be less (more) likely to act as information intermediaries" | 2 | Cross-sectional prediction (audit quality); tension resolved by attenuation in higher-quality auditors |
| ¶6: "we expect the shared-auditor effect on M&A deals to be stronger prior to SOX" | 2 | Cross-sectional prediction (SOX); regulatory-shock attenuator prediction |
| ¶7: "Using data on public transactions from 1985 to 2010, we examine the impact of shared auditors on the outcomes of all acquisitions" | 3 | Sample-period sentence; doubles as setting justification for the US M&A market over a 25-year panel |
| ¶7: "approximately 26% of all acquisitions among clients of Big-N audit firms have a shared auditor" | 3 | Descriptive prevalence; prevalence statistic justifying the setting |
| ¶8: "premiums paid by acquirers in shared-auditor deals are nearly 4.2% lower than deals in which the target and acquirer have different auditors" | 4 | M5 F1 percentage-point magnitude; headline finding on deal premium |
| ¶8: "average announcement day returns are 1.80% lower for targets and 0.70% higher for acquirers in deals with shared auditors" | 4 | M5 dual-DV magnitude (target + acquirer); paired CAR magnitudes documenting asymmetric incidence |
| ¶9: "These results are robust to controls for geographic distance between the target and acquirer" | 5 | Robustness battery; geographic-distance confound addressed up front |
| ¶11: "We find the shared-auditor effect on deal outcomes is concentrated in deals with smaller targets" | 5 | Cross-sectional partition (target size); smaller-target partition corroborates moderation |
| ¶11: "the shared-auditor effect is stronger in the pre-SOX period relative to the post-SOX period" | 5 | Pre-/post-SOX partition; closes the loop on Block 2 SOX prediction |
| ¶12: "Our study makes three contributions. First, we provide evidence that acquirers benefit from sharing an auditor's office with a target" | Final | M6 form 1 Contribution 1; numbered opener, adds to audit literature |
| ¶13: "our study documents a novel conflict of interest as it relates to the auditor's client portfolio" | Final | Contribution 1 reframe; portfolio-level conflict-of-interest framing |
| ¶14: "Second, our results also add to prior studies" | Final | M6 form 4 Contribution 2; complement/extend auditor-impact-beyond-audit literature |
| ¶15: "Third, by providing evidence that shared auditor offices impact the acquisition process and deal outcomes" | Final | M6 form 4 Contribution 3; information-asymmetry and shared-intermediary literatures |
| ¶16: "Our study complements a concurrent paper by Cai et al. (2014) who also examine the effect of shared auditors on acquisitions" | Final | Concurrent-paper differentiation; rare Final-block sub-form, candidate form 9 |
| ¶17: "The remainder of the paper is organized as follows. Section 2 discusses prior literature and hypothesis development" | Final | Roadmap; canonical JAE-2016 closer, supports "JAE drops roadmaps post-2020" rule |

**Notable deviations in 16-DLLN**:

1. **Extreme M1A bypass + no M2 gap.** Block 1 has neither lit-baseline nor gap statement. ¶1 states the RQ in sentence 1 and previews the hypothesis in sentence 2; lit anchor deferred entirely to §2. The most aggressive M1A-inversion in the augmented batch, joining 19-JWW, 19-Aob, 22-FHKF, 23-ZBLM in the RQ-first family with the additional twist that even the gap statement is omitted from the intro.
2. **No canonical M4 tension paragraph.** Block 2 spans five paragraphs of mechanism without a "however, there are reasons why the opposite may hold" pivot. The ¶6 normative-tension pre-emption serves a similar rhetorical function (acknowledges a problem with the prediction) but resolves via cross-sectional moderation rather than direction reversal. Adding 16-DLLN further weakens the M4-corpus-unanimous claim alongside 22-LNS, 20-WY, 22-FHKF, 22-FW, 24-Chen — Phase D will need to recount.
3. **Concurrent-paper differentiation move.** ¶16 explicitly differentiates from a concurrent Cai-and-co-authors paper on the same topic. Rare in the corpus; candidate for a new Final-block contribution sub-form ("form 9 — concurrent-paper differentiation"). Reach for it when the reviewer might ask whether the paper scoops or is scooped by parallel work.
4. **Dual-DV CAR magnitude (coordinated-clause variant).** ¶8 reports paired target/acquirer announcement returns in coordinated clauses ("1.80% lower for targets and 0.70% higher for acquirers"). Structurally analogous to 23-ACN's parenthetical dual-DV form but uses different syntax. Worth filing as an M&A-specific M5 sub-form for papers where the headline asymmetry is target-vs-acquirer.
5. **JAE-2016 roadmap retained.** ¶17 carries the canonical "The remainder of the paper is organized as follows" closer, supporting the style_dna §8 claim that the JAE-drops-roadmap convention is a post-2020 phenomenon.

---

## Checklist for self-audit

Before finalizing an introduction, verify:

- [ ] Block 1 opens INSIDE the literature (Move A/B/C/D), not with motivation rhetoric
- [ ] Gap statement appears by end of Block 1
- [ ] RQ stated explicitly with "The purpose of this study..." or "We examine whether..."
- [ ] Block 2 contains an explicit tension paragraph ("We note, however, that there is tension...")
- [ ] Hypothesis stated formally in alternative form
- [ ] Block 3 justifies the setting (especially for non-US data) in 3 parts: data availability + institutional feature + within-setting variation
- [ ] Block 4 reports at least ONE numerical magnitude (percentage, percentage points, or std-dev change)
- [ ] Block 4 leads with "Consistent with our hypothesis..." or "As hypothesized..."
- [ ] Block 5 contains at least one of: rotation/shock, placebo, cross-sectional corroboration
- [ ] Final block has 3-4 numbered contributions to identifiable literatures
- [ ] No forbidden openings (no anecdotes, no "important question in the literature")
- [ ] No banned verbs ("show that", "prove", "demonstrate definitively") — see `style_dna.md`
- [ ] If JAE/JAR, no roadmap. If TAR, optional roadmap.
- [ ] Length under 3,500 words (Block 1 + Block 2 + Block 3 + Block 4 + Block 5 + Contributions + optional limitations)

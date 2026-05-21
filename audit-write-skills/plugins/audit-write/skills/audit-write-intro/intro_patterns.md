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

## Stage-1 Phase-C pilot digest (16 archival papers; 2026-05-21)

The full annotated row tables for these 16 pilot intros live as staging files named `<code>_intro.md` in the Track B drafts directory (`corpus_inventory/track_b_drafts/`). This pattern file keeps two full anchor tables above — `26-KLYY` (canonical partner-trait template) and `19-JWW` (RQ-first / design-driven counter-template) — and distills the rest here: which opener and magnitude variants are reusable, and which example to retrieve when drafting. `22-HS` was rejected as survey-methodology and replaced by `16-DLLN` per the archival-only scope rule.

| Code | Opener | Distinctive feature(s) | Rule / variant implication |
|---|---|---|---|
| `19-JWW` | M3 RQ-first (inverts M1A lit-baseline) | Design-driven Block 2; falsification + placebo + size partition in Block 5; M7 limitation mid-Final | RQ-first is a recognized opener when identification, not theory, carries the paper (full table above) |
| `22-LNS` | M1A practitioner-data variant (AICPA survey) | M4 tension omitted in intro; F5+F2 interquartile magnitude | Practitioner-data opener is valid; intro M4 omission is risky and best repaired in Section 2 |
| `23-ACN` | M1A lit-baseline (tri-audience) | Cleanest canonical 5-block; role-decomposition ("who not just what"); F4+F1 magnitude | The reference canonical exemplar; "who not just what" sharpens the gap into the RQ |
| `20-WY` | Anecdote / illustrative opener | 3-part China-setting template; dual-DV F2 magnitudes | Anecdote opener works only if it pivots fast to the gap; reuse the China 3-part template |
| `22-CHLP` | M1A China social-connections | Explicit "injecting tension" device; spatio-temporal validation | A named tension-injection move is a clean way to satisfy the mandatory M4 |
| `22-Dug` | Policy-motivation opener | Head-placed M4 in para 1; single-author "I"; identification-dense Block 3 | Policy opener + early tension is valid; "I" is acceptable for single-author JAR |
| `23-ZBLM` | M3 RQ-first | Enumerated 4-issue M4; odds-ratio magnitude; process-positive / output-null pairing | Enumerated tension + positive/null pairing is a strong template for mixed findings |
| `24-Chen` | M1A+M1C hybrid | Single-author "I"; employee-lawsuit setting; direction-only Block 4 | Hybrid openers work; direction-only Block 4 is acceptable when magnitudes are deferred |
| `24-DGZZ` | Setting-led M1A (IBBEA banking deregulation) | 4-mechanism Block 2; F1+F2 dual-DV pairing | A deregulation shock can lead the opener; a multi-mechanism Block 2 is legitimate |
| `19-Aob` | M3 RQ-first | Three-sided tension; single-author "I"; F2+F5 magnitudes | Measurement-concordance papers can open RQ-first with multi-sided tension |
| `19-BGH` | Construct-tension (fast M1A to M2) | Block 2 omission; spatial-distance F6 ("within 185 kilometers"); F8 logit DV | Construct-tension opener + spatial-distance magnitude form are reusable |
| `20-CKMS` | M1A private-firm BD setting | Triple-prediction; internal-benchmark F6 ("half as important as client size") | Internal-benchmark magnitude (own-coefficient comparator) is a valid F6 sub-form |
| `16-DLLN` | Extreme M1A-bypass / RQ-led | No explicit M2 gap; concurrent-paper differentiation; dual-DV CAR magnitude | Older (2016) JAE permits no explicit gap; differentiate from concurrent work instead |
| `23-PSZ` | Setting-led (bullet-train shock) | M4 in para 1; minimalist Final block | A clean shock can open the paper; contributions may be compact |
| `22-FHKF` | M3 RQ-first | Labor-economics theory import; multi-DV magnitude; mixed-methods | RAST mixed-methods can import cross-discipline theory and open RQ-first |
| `22-FW` | M1A paucity-of-insight | Cross-discipline ("cockroach") theory anchor; time-decline magnitude | A cross-discipline theory anchor + temporal-decline magnitude form are reusable |

### New reusable variants surfaced by the pilot

1. **The opener is not just M1A.** Over n=22 the lit-baseline M1A remains dominant (11/22), but M3 RQ-first is a recognized variant (5/22: `19-JWW`, `19-Aob`, `22-FHKF`, `23-ZBLM`, `16-DLLN`), and setting-/shock-led openers (`23-PSZ`, `24-DGZZ`) and practitioner/anecdote variants (`22-LNS`, `20-WY`) also appear. Default to M1A; use a variant only when the design or setting is the contribution.
2. **Block 4 magnitude is near-universal but its FORM varies.** Beyond F1 (pp) + F2 (% of base): spatial-distance F6 (`19-BGH`), internal-benchmark F6 (`20-CKMS`), interquartile F5 (`22-LNS`, `19-Aob`), odds-ratio (`23-ZBLM`), temporal-decline (`22-FW`), and dual-DV CAR (`16-DLLN`). Always carry a magnitude; pick the form the design affords.
3. **Tension (M4) placement has several shapes.** Head-placed in para 1 (`22-Dug`, `23-PSZ`), enumerated multi-issue (`23-ZBLM` four issues; `19-Aob` three-sided), or omitted in the intro and repaired in Section 2 (`22-LNS`, `20-WY`). Treat omission as a risky exception, not a template.
4. **Single-author "I" is acceptable** in single-author JAR/JAE papers (`19-Aob`, `22-Dug`, `24-Chen`).
5. **The gap (M2) can be absent** in older JAE (`16-DLLN`, 2016), but this is an era-specific exception; modern JAE/JAR/TAR expect an explicit gap.
6. **Roadmap follows the journal.** Keep the "Section II..." roadmap for TAR/AJPT (`19-JWW`, `23-ACN`); modern JAE/JAR drop it.

### Drafting retrieval guide

| If your paper has... | Retrieve |
|---|---|
| partner-trait with a clean theory mechanism | `26-KLYY` (anchor, above) |
| design-/identification-led framing, RQ-first | `19-JWW` (anchor, above) or `22-FHKF` |
| a regulatory shock or setting-led opener | `23-PSZ` or `24-DGZZ` |
| a China institutional setting | `20-WY` or `22-CHLP` |
| a practitioner-data / human-capital opener | `22-LNS` or `23-ACN` |
| a single-author "I" voice | `19-Aob`, `22-Dug`, or `24-Chen` |
| a spatial / distance magnitude | `19-BGH` |
| an internal-benchmark magnitude | `20-CKMS` |
| measurement / proxy-validation framing | `19-Aob` |
| mixed-methods technology evidence | `22-FHKF` |
| no explicit gap (older JAE) | `16-DLLN` |

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

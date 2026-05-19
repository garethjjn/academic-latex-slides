---
name: audit-write-design
description: "Draft, rewrite, or audit the research design / methodology section (typically Section 3) of an empirical audit-research paper in DeFond / Zuo / Khurana style for JAE / JAR / TAR. USE THIS SKILL when the user is writing the section that defines the sample, measures, and baseline empirical model. Encodes a counter-intuitive structural rule: identification machinery (rotation, shocks, falsification, FE escalation) belongs in §4 (results), NOT §3 (design). §3 should do five compact things: define the DV with a defense paragraph, build the IV bottom-up, present a numbered baseline equation, list controls in 2-4 categorical groups, and state FE + clustering choices."
when_to_use: "Trigger when user asks to write, rewrite, or audit Section 3 / research design / methodology / sample-measures-model section of an audit paper. Indicator phrases: 'rewrite my Section 3', 'design my methodology', 'how do I justify my variable measurement', 'should I use PSM', 'what fixed effects', 'sample selection prose'. Defer to econ-write for non-audit empirical design sections."
argument-hint: "<task> e.g. 'rewrite my Section 3', 'design methodology from these notes', 'audit my research design', 'should my §3 include the rotation IV'"
user-invocable: true
allowed-tools: Read Grep Glob Edit Write
---

You are an expert audit-research design-section writer. Your task is to draft, rewrite, or audit the research design / methodology section (typically Section 3, sometimes "Data and Research Design", "Sample, Measures, and Model", "Research Methods") of an empirical audit-research paper for JAE / JAR / TAR.

The audit-paper design section has a **distinctive structural rule** that violates the instinct of writers (especially China-data writers):

> **Identification machinery — quasi-experiments, regulatory shocks, partner rotation, falsification, FE escalation — belongs in §4 (results), NOT §3 (design). §3 is for the baseline OLS specification only.**

This is true across all 6 corpus papers (DeFond 2007, 2016, 2024, 2025; Khurana 2026; Dekeyser 2024). Loading §3 with quasi-experimental rhetoric is a common AI-generated tell that signals the writer doesn't know the modern register.

---

## CRITICAL — Read these reference files when first invoked

1. **[design_patterns.md](design_patterns.md)** — the 5-part §3 anatomy, the deferral rule, China-setting design moves, FE + clustering conventions, construct validation patterns, identification rhetoric catalog
2. **[../audit-write/style_dna.md](../audit-write/style_dna.md)** — verb register, banned vocabulary
3. **[../audit-write/audit_quality_framework.md](../audit-write/audit_quality_framework.md)** — DV / IV vocabulary anchor

---

## The 5-part §3 anatomy

```
Part 1 — DEPENDENT VARIABLE + DEFENSE (1-2 paragraphs)
  Define DV. State why this proxy. Acknowledge alternatives. Cite the audit-quality framework references appropriate to your subfield.
  Pattern: "We measure audit quality using [proxy], following [Author Year]. [Proxy] is an appealing measure because [reason]. While [alternative proxy] is also used, we focus on [proxy] because [reason]."

Part 2 — INDEPENDENT VARIABLE BUILD (2-3 paragraphs)
  Construct the IV bottom-up. Start with raw data, build component measures, aggregate to final IV.
  Pattern: "We construct [IV] in three steps. First, [raw step]. Second, [aggregation]. Third, [final form]."
  For novel IVs (Network 24-DLWW, RangeN 24-DHXZ, PartnerTrust 26-KLYY, CTA 25-DQSZ): include validation paragraph.

Part 3 — BASELINE EMPIRICAL MODEL (1 paragraph + numbered equation)
  Numbered display equation (Eq. 1). Variable definitions in Appendix or footnote.
  Pattern: "We test our hypothesis using the following model:
            [Eq. 1]: Y_it = α + β·IV_it + γ·Controls_it + FE + ε_it
            We are interested in the coefficient β; a [direction] β is consistent with our hypothesis."

Part 4 — CONTROLS, FIXED EFFECTS, CLUSTERING (1-2 paragraphs)
  List controls in 2-4 categorical groups: client controls / auditor controls / institutional controls / partner controls.
  State FE structure. State SE clustering.
  Pattern: "We control for [3-5 client characteristics: size, leverage, ROA, ...]. We control for [3-5 auditor characteristics: Big-N, tenure, industry expertise, ...]. We include [client × year / industry × year / city × year] fixed effects. Standard errors are clustered by [audit firm / client / partner]."

Part 5 — SAMPLE CONSTRUCTION (1 paragraph)
  Filter language. Sample size sentence at end.
  Pattern: "Our sample begins with [N] observations from [database] over [year-year]. We exclude [N1] observations with [criterion 1], [N2] with [criterion 2], leaving a final sample of [N] observations."
```

**Total §3 length:** 1,500-2,500 words typical.

---

## Hard rules — never violate

1. **Defer all identification machinery to §4.** §3 is for the BASELINE spec only. Do NOT include in §3:
   - Auditor rotation as IV
   - Regulatory shock DiD
   - Falsification / placebo tests
   - PSM / entropy balance / matching
   - Cross-sectional partitions
   - FE saturation tests

   These all go in §4 (Results) under "Identification" or "Robustness" sub-sections. The rule applies whether your paper is JAE, JAR, or TAR.

2. **Standard error clustering must be specified explicitly.** Standard practice: cluster by audit firm (firm-level), audit office (office-level), or partner (partner-level), depending on the analysis level. Year × industry FE is NOT a substitute for clustering.

3. **Variable definitions belong in an Appendix table, not in the §3 prose.** Reference the appendix from §3 ("All variables are defined in Appendix A").

4. **Numbered equation at most ONCE in §3.** Save Eq. 2, 3, ... for §4 / robustness.

---

## Operating modes

### Mode A — DRAFT (from notes)

User provides: DV, IV, sample, controls, FE / clustering choices.

Output: full §3 with the 5-part anatomy. Insert `[AUTHOR: confirm sample N / period]` and `[APPENDIX A: variable definition table]` placeholders. ~1,500-2,500 words.

If user has provided identification machinery (rotation, shocks, falsification): note "These belong in §4, not §3. I will defer them. Confirm if you want them in §3 anyway."

### Mode B — REWRITE (transform existing draft)

Output: rewritten §3 + change log. Specifically check:
- Identification machinery in §3 → MOVE to §4
- Variable definitions in §3 prose → MOVE to Appendix
- Multiple numbered equations → COMPRESS to one
- Missing DV defense paragraph → ADD (cite the audit-quality framework references appropriate to the paper's subfield)
- Missing clustering specification → ADD
- China setting unjustified in §3 → ADD 1-paragraph defense

### Mode C — AUDIT (review without rewriting)

Structured audit report:

```markdown
# §3 Research Design Audit Report

**Word count:** [X] (target: 1,500-2,500)
**5-part anatomy compliance:** [PASS / PARTIAL / FAIL]

## Part-by-Part Diagnosis

### Part 1 — DV + Defense [PASS/WARN/FAIL]
- Audit-quality framework reference cited: [Y/N]
- Alternative proxies acknowledged: [Y/N]

### Part 2 — IV Build [PASS/WARN/FAIL]
- Bottom-up construction: [Y/N]
- Validation for novel measures: [Y/N]

### Part 3 — Baseline Model [PASS/WARN/FAIL]
- One numbered equation: [Y/N]
- Sign expectation stated: [Y/N]

### Part 4 — Controls, FE, Clustering [PASS/WARN/FAIL]
- Controls grouped: [Y/N]
- FE structure stated: [Y/N]
- SE clustering specified: [Y/N]

### Part 5 — Sample [PASS/WARN/FAIL]
- Filter table or prose: [Y/N]
- Final N stated: [Y/N]

## Identification-Deferral Audit

[Are any of the following in §3 (should be in §4 instead)?]
- [ ] Quasi-experimental shock (rotation, regulatory) — list location
- [ ] Falsification / placebo test — list location
- [ ] Matching procedure (PSM, entropy balance, CEM) — list location
- [ ] Cross-sectional partition — list location
- [ ] FE saturation comparison — list location

## Top 3 Fixes
1. [...]
2. [...]
3. [...]

## Score [X/100]
```

---

## Differences from related sub-skills

| Element | `audit-write-hypothesis` | `audit-write-design` (this) | `audit-write-results` |
|---|---|---|---|
| Identification machinery | Not present | **NOT PRESENT — deferred to §4** | **HERE** (sub-section under "Identification") |
| Numbered equations | None | **One** (baseline) | Multiple (model variants) |
| Tension | Full development | None | None |
| Variable definitions | None | Appendix reference | Brief inline + appendix |
| Length | 1,500-2,500 words | 1,500-2,500 words | 3,000-5,000 words |

---

## Demo / example interaction

**User input:**
> "Rewrite my §3. DV: restatement. IV: auditor early-life integrity-propaganda exposure (county-year). Sample: Chinese listed firms 2008-2022. I included rotation as IV in §3 — is that right?"

**Your response:**

Three structural issues to fix:
1. **Rotation as IV belongs in §4, not §3.** Move it to a §4.X "Identification" sub-section.
2. **§3 should describe the BASELINE OLS spec only.** Lead with the simple regression of restatement on integrity exposure with controls + FE.
3. **Add DeFond-Zhang 2014 + Aobdia 2019 citations** to the DV defense.

Drafted §3:

```markdown
## 3. Research Design

### 3.1 Measuring Audit Quality
Following DeFond and Zhang (2014), we measure audit quality using restatements (Restate), an output-based proxy widely used in the audit literature. Restate equals one if a client's annual financial statements are subsequently restated for a material accounting error, and zero otherwise. As Aobdia (2019) demonstrates, restatements correlate with PCAOB practitioner assessments of audit quality more strongly than do discretionary accruals, supporting their validity. While alternative proxies — discretionary accruals, going-concern opinions, audit fees — are also informative, restatements have the advantage of being attributable to the auditor's failure to detect a material misstatement (Lennox and Wu, 2022).

### 3.2 Measuring Auditor Integrity Exposure
We construct our auditor-level integrity-exposure measure (IntegExp) in three steps. First, [step 1: lexicon of integrity terms × People's Daily corpus → county-year integrity-content metric]. Second, [step 2: weight by radio-signal strength (county × birth-year) for childhood ages 5-15]. Third, [step 3: aggregate to auditor-level by birth-county and birth-year]. The resulting IntegExp ranges from [range], with higher values indicating greater early-life exposure. We validate IntegExp by [construct validation: e.g., correlation with county-level Confucian temple density; survey-based trust measures].

### 3.3 Empirical Model
We estimate the following baseline model:

> Eq. 1: Restate_{i,t} = α + β·IntegExp_{a,i,t} + γ·X_{i,t} + δ·Z_{a,t} + Industry × Year FE + ε_{i,t}

where _i_ indexes client firm, _a_ indexes auditor, and _t_ indexes year. β is the coefficient of interest; H1 predicts β < 0.

### 3.4 Controls, Fixed Effects, and Clustering
We control for client characteristics that affect restatement likelihood (X_{i,t}): firm size, leverage, ROA, market-to-book, sales growth, CFO, age, and SOE status. We control for auditor characteristics (Z_{a,t}): Big-4 status, audit fee, auditor tenure, industry specialization, and auditor age. We include client industry × year fixed effects to absorb industry-time-varying shocks. Standard errors are clustered by audit firm.

### 3.5 Sample Construction
Our sample begins with [N1] firm-year observations from CSMAR over 2008-2022. We exclude [N2] observations with missing auditor identity, [N3] with missing financial controls, and [N4] for which we cannot identify the auditor's birth-county. The final sample contains [N] firm-year observations across [N_firm] unique firms and [N_auditor] unique signatory auditors. Variable definitions are provided in Appendix A.
```

Identification machinery (rotation, falsification) deferred to §4.

---

## When you finish

End with one short closer line:

- Mode A: "§3 drafted in [N] words, 5-part structure complete."
- Mode B: "§3 rewritten in [N] words. Key change: [identification deferred to §4 / variable defs moved to appendix / clustering specified / etc.]."
- Mode C: "Audit complete: [N] FAILs, [M] WARNs. Top fix: [single sentence]."

Do not over-explain.

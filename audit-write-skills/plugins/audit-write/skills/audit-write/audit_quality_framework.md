# Audit Quality Framework — Distilled Reference

**Source.** DeFond & Zhang (2014, JAE 58: 275-326) "A review of archival auditing research" plus updates from DeFond & Zhang (2025) "Audit failures: why they occur and some suggestions for reducing them" and Lennox, Li & Wang (2025) "A survey of the archival audit literature."

This file is the **canonical conceptual reference** for any `audit-write-*` skill. When writing about audit quality, consult this for the framework, the proxy taxonomy, and the right vocabulary.

---

## 1. Definition of audit quality (canonical, DeFond-Zhang 2014)

> "**Higher audit quality is greater assurance that the financial statements faithfully reflect the firm's underlying economics, conditioned on the firm's financial reporting system and innate characteristics.**"

Key features of this definition:
- **Continuous, not binary.** Audit quality is a continuum, not a pass/fail.
- **Relative to constraints.** The achievable level depends on the firm's reporting system and innate characteristics — auditors can only do so much given a hostile pre-audit reporting environment.
- **Joint product.** Audit quality is a *component of* financial reporting quality, not a standalone construct. Cannot be cleanly separated from client-side factors.

### Implications for empirical work

- A finding that "auditors with characteristic X have lower discretionary accruals" is consistent with higher audit quality OR with X-auditors having different clients. Empirical work must disentangle these.
- A finding that "auditors with X issue fewer GC opinions" is **ambiguous** — could mean better client-screening (audit quality up) or weaker monitoring (audit quality down). The writer must specify which interpretation fits.

---

## 2. The audit-quality proxy taxonomy

### 2.1 Output-based proxies (what the audit produces)

These are observable consequences of the audit process. Direct reflection of audit quality.

| Proxy | Captures | Strengths | Weaknesses |
|---|---|---|---|
| **Restatements** | Egregious failure | Concrete, observable, attributable | Rare; often discovered years later; only captures detected failures |
| **AAERs** (US) | SEC enforcement of misstatement | Highly specific to fraud | Very rare; selection bias toward egregious cases |
| **Going-concern opinions (GCOs)** | Auditor communication of concern | Auditor-direct decision | Many false positives; client-pressure may bias issuance |
| **Discretionary accruals (DAC)** | Within-GAAP earnings management | High frequency; available for everyone | Noisy proxy; poor agreement with practitioner assessments (Aobdia 2019) |
| **Earnings response coefficients (ERCs)** | Market perception of earnings credibility | Captures perceived quality | Indirect; affected by many factors beyond audit |
| **Audit adjustments** (China only via MoF) | Errors detected by auditor and corrected | Direct measure of process | Available only for Chinese listed firms 2006-2015 |
| **Financial irregularities (China)** | Restatement + CSRC sanction | Comprehensive; China-relevant | Country-specific; institutional differences |

### 2.2 Input-based proxies (what the auditor brings)

These are characteristics or contractual features that should correlate with quality.

| Proxy | Captures | Strengths | Weaknesses |
|---|---|---|---|
| **Big 4 vs non-Big 4** | Firm-level reputation/competence | Clean binary; high power | Endogeneity (Lawrence-Minutti-Meza-Zhang 2011 critique) |
| **Audit fees** | Effort + risk premium | Continuous; available | Conflates effort, risk premium, and demand-side factors |
| **Industry specialist** | Firm or office expertise | Mechanism-grounded | Multiple competing measures (market share vs portfolio share) |
| **Audit office size** | Office-level resources | Direct competence measure | Less variation than firm-level |
| **Auditor tenure** | Familiarity vs independence trade-off | Continuous | Theoretical ambiguity (cuts both ways) |
| **Auditor partner characteristics** | Individual-level (gender, education, experience, networks, IQ, narcissism, conscientiousness, cultural background) | Most granular | Available primarily in China + a few EU countries; partner rotation since 2017 in US |

### 2.3 Critical update from Aobdia 2019 JAE

Aobdia (2019) compares 15 academic audit-quality proxies to PCAOB internal-inspection assessments. Key findings:

- **Restatements** correlate with practitioner assessments — defensible proxy.
- **Discretionary accruals** do NOT correlate with PCAOB assessments — weak proxy.
- **Going-concern opinions** show modest correlation, but only for distressed firms.
- **Audit fees** correlate negatively with PCAOB assessments (controversial — fees may capture risk premium not effort).

**Implication for writing.** When using DAC as a proxy, the writer should:
1. Cite Aobdia (2019) as a known limitation
2. Triangulate with at least one other proxy (restatements, GCOs)
3. Frame DAC as capturing "within-GAAP earnings management" specifically, not "audit quality" broadly

---

## 3. Demand-side framework (client-driven)

### What drives client demand for audit quality

| Driver | Standard reference | China analogue |
|---|---|---|
| Agency costs (separation of ownership/control) | Jensen & Meckling 1976 | Higher in SOEs with diffuse ownership |
| Cost of capital reduction | Khurana & Raman 2004 | Particularly relevant for IPO-stage firms |
| Information asymmetry | Glosten & Milgrom 1985 | High in early-stage / cross-listed firms |
| Audit committee competence | Klein 2002 | Less developed; mandatory committee 2006+ |
| Internal audit function | Prawitt et al. 2009 | Less archival evidence in China |

### Client competencies (post-SOX expanded literature)

- Independent audit committees → choose higher-quality auditors
- Financial-expert audit committees → fewer restatements
- Strong internal controls → fewer material weaknesses
- These are **complements** to external audit, not substitutes

---

## 4. Supply-side framework (auditor-driven)

### What drives auditor supply of audit quality

| Driver | Mechanism |
|---|---|
| Reputation risk | Loss of future clients if quality fails |
| Litigation risk | Direct financial penalties |
| Regulatory sanctions | Loss of license, restrictions on practice |
| Auditor competency (firm) | Big 4 vs non-Big 4, industry specialization |
| Auditor competency (office) | Office size, geographical concentration |
| Auditor competency (partner) | Individual education, experience, networks, traits |

### The competence-vs-independence trade-off (DeFond 2024)

Recent research has emphasized that auditor characteristics don't always pull in the same direction:
- **Strong client connections** → higher competence (information advantage), but threaten independence
- **Long tenure** → higher familiarity (competence), but reduced skepticism (independence)
- **Industry specialization** → deep expertise (competence), but cognitive entrenchment (Dekeyser 2024 critique)

The empirical question: which dominates? Modern audit papers explicitly frame this trade-off in their hypothesis development.

---

## 5. Regulatory framework (from DeFond-Zhang 2014 + 2025)

### Key regulatory regimes

| Regime | Year | Effect on audit market |
|---|---|---|
| Sarbanes-Oxley (SOX) | 2002 | Established PCAOB, banned most non-audit services, mandated internal control audits |
| PCAOB inspections | 2003+ | Large-firm triennial, small-firm triennial, public reports of deficiencies |
| Mandatory partner rotation | Various | China since 1996 (5-year), US since 2003 (5-year senior, 7-year coordinating) |
| Engagement partner disclosure | US 2017+ | PCAOB Form AP — finally enables US partner-level research |
| Critical Audit Matters (CAMs) | US 2019+ | Auditors must disclose specific risk areas |
| Key Audit Matters (KAMs) | International 2016+ | Similar; ISA 701 |

### China-specific regulatory milestones

| Year | Event |
|---|---|
| 1992 | Shanghai/Shenzhen exchanges open; CPA profession recasts |
| 1996 | Mandatory 5-year partner rotation |
| 2002 | Tax-sharing reform between central and local governments |
| 2005 | Top-executive disclosure expands |
| 2006 | New PRC accounting standards converge with IFRS |
| 2010 | Mandatory disclosure of audit adjustments to MoF |
| 2017 | Pilot audit centralization program (6 provinces) |

---

## 6. The 2025 DeFond-Zhang "Audit Failures" update

Key additions to the 2014 framework from DeFond-Zhang 2025:

- **Audit failure definition refined.** Not all GAAP violations are audit failures; some are within auditor's reasonable control, others are not. Audit failure = failure to do what a reasonable auditor would have done.
- **Litigation-driven regulation.** Most modern audit regulation has been reactive to highly visible failures (Enron, Lehman), and has had **mixed empirical support** (DeFond & Lennox 2017 find PCAOB inspections improve internal-control audits; less clear effect on financial-statement audits).
- **Reputation as the disciplinary mechanism.** Reputation > litigation in driving partner-level behavior. Recent evidence: Chen et al. 2022 JAR finds career consequences for individual auditors.
- **The rise of partner-level research.** Until 2017, US partner identities were unavailable. Now, papers like Khurana 2026 (cultural trust) and He 2026 (conscientiousness) exemplify the new partner-level identification regime.

---

## 7. Lennox-Li-Wang 2025 update (newer survey)

Companion-piece to DeFond-Zhang 2014/2025. Key additions:

- **Methodological progress.** Better identification (natural experiments, regulatory shocks) has tightened the audit-quality literature since 2014.
- **Geographic expansion.** Most growth has been outside the US — China, EU partner-level data, Australia.
- **Open questions** highlighted by Lennox et al. 2025:
  - Does auditor effort actually increase audit quality? (separate from selection)
  - Do auditor traits compensate for or substitute for firm-level quality controls?
  - How does technology (AI in auditing) reshape the production function?

---

## 8. How to use this framework when writing

### When stating your dependent variable

Always anchor in the DeFond-Zhang 2014 framework:

> "Following DeFond and Zhang (2014), we measure audit quality using [specific proxy], which captures [output / input dimension]."

> "We acknowledge that no single proxy provides a complete picture of audit quality (DeFond and Zhang 2014). To address this, we triangulate using [proxy 1, proxy 2, proxy 3]."

### When describing your auditor characteristic

Frame in terms of the supply-side competency/incentives split:

> "We examine [auditor characteristic X] as a determinant of audit quality through its effect on auditor [competency / incentives / both]."

### When describing your contribution

Map your contribution to one of these literature anchors:
- Output-based proxies → DeFond-Zhang 2014, Aobdia 2019
- Input-based proxies → Lawrence-Minutti-Meza-Zhang 2011, DeFond-Erkens-Zhang 2017 (for Big-N selection)
- Partner-level → Lennox-Wu 2018 review, Gul-Wu-Yang 2013
- China audit → Lennox-Wu 2022 review, DeFond-Zhang-Zhang 2021

## 9. Glossary of audit-research terms (alphabetical)

- **AAER (Accounting and Auditing Enforcement Release)** — SEC enforcement action; rare and severe.
- **AAS (Audit Adjustment Schedule)** — China MoF data on errors corrected during audit.
- **Audit committee** — Board subcommittee overseeing the external audit.
- **Audit failure** — Failure to detect or report a material misstatement that a reasonable auditor would have caught.
- **Audit risk** — Probability the auditor issues an unqualified opinion on materially misstated statements. = Inherent × Control × Detection.
- **Big 4 / Big N** — Deloitte, EY, KPMG, PwC. "Big N" includes the historical Big 5/6/8.
- **CTA (Certified Tax Agent)** — Chinese tax-expertise designation, separate from CPA.
- **DAC (Discretionary Accruals)** — Earnings management proxy; usually estimated as residuals from a Jones model or modified Jones model.
- **Engagement partner** — Lead audit partner on a specific engagement.
- **Engagement risk** — Total risk to the auditor from an engagement = client business risk + audit risk + auditor business risk.
- **GAAP / IFRS** — Generally Accepted Accounting Principles; International Financial Reporting Standards.
- **GCO (Going Concern Opinion)** — Opinion that flags substantial doubt about client's ability to continue.
- **Industry specialist** — Auditor (firm/office/partner) with high market share or portfolio concentration in a specific industry.
- **KAM / CAM (Key / Critical Audit Matter)** — Audit-report disclosure of significant risk areas.
- **LMG (Lawrence, Minutti-Meza, Zhang 2011)** — The PSM critique of Big-N audit-quality differences.
- **MoF (Ministry of Finance)** — Chinese regulator that collects audit-adjustment data.
- **NAS (Non-Audit Services)** — Services beyond financial-statement audit (tax, advisory, etc.).
- **PCAOB** — Public Company Accounting Oversight Board (US, est. 2002).
- **Restatement** — Public revision of previously issued financial statements due to error or fraud.
- **Type I error (audit)** — GCO issued for a non-bankrupting client (false positive).
- **Type II error (audit)** — No GCO issued for a client that subsequently bankrupts (false negative; more costly to auditors).

# Corpus Manifest — Evidentiary Base of the `audit-write-*` Suite

**What this is.** Every structural rule, frequency claim, verb register, and verbatim
example in the `audit-write-*` pattern files is distilled from a fixed, named corpus of
published / preprint audit-research papers. This file is that corpus's provenance record.
It exists so a user can (a) decode the shorthand codes used throughout the pattern files,
(b) judge how far a claim generalizes, and (c) verify any quote against source.

**Licensing.** The skill ships the *distilled patterns only*. It does **not** redistribute
the source PDFs (they are third-party copyrighted articles). Citations below let you
obtain the papers from their publishers; the suite is usable without them.

---

## 1. Shorthand-code decode table (the 6 empirical template papers)

> **These 6 are a subset, not the whole base.** The suite was developed against a
> **29-paper DeFond-primary reading corpus** (DeFond-led, with Lennox / Zuo / Aobdia /
> partner-trait lineages as support — see §3 and `audit_writing_corpus/CORPUS_INDEX.md`).
> The 6 below are simply the empirical papers given **shorthand codes** because they are
> quoted verbatim as *structural-frequency templates* in the pattern files; the other ~23
> feed framework, vocabulary, design, and journal-culture guidance without per-move counts.
> Stage-1 (2026-05) added 16 more coded pilot papers (§1b). So the evidentiary base is
> ~29 reading + 22 structurally-coded, not "only 6."

The pattern files (`intro_patterns.md`, `hypothesis_patterns.md`, `design_patterns.md`,
`results_patterns.md`, `robustness_patterns.md`, `abstract_patterns.md`) reference papers
by these codes. All six are empirical articles used as structural templates.

| Code | Citation (author, year, journal) | Topic | Source filename |
|---|---|---|---|
| `07-DHT` | DeFond, Hung & Trezevant (2007, *JAE*) | Investor protection & earnings informativeness; cross-country | `2007_JAE_DeFond_Hung_Trezevant_Investor_Protection.pdf` |
| `16-DLZ` | DeFond, Lim & Zang (2016, *TAR*) | Client conservatism & auditor–client contracting | `2016_TAR_DeFond_Lim_Zang_Client_Conservatism.pdf` |
| `24-DLWW` | DeFond, Li, Wong & Wu (2024, *JAE*) | Auditor competence vs. independence; auditor social networks (China) | `2024_JAE_DeFond_Competence_vs_Independence.pdf` |
| `24-DHXZ` | Dekeyser, He, Xiao & Zuo (2024, *JAE*) | Auditor industry range | `2024_JAE_Dekeyser_Auditor_Industry_Range.pdf` |
| `25-DQSZ` | DeFond, Qi, Si & Zhang (2025, *JAE*) | Signatory-auditor tax expertise & tax aggressiveness (China) | `2025_JAE_DeFond_Qi_Tax_Expertise_Signatory.pdf` |
| `26-KLYY` | Khurana, Li, Yeung & Yu (2026, *JAE*) | Audit-partner cultural trust & going-concern / reporting quality | `2026_JAE_Khurana_Audit_Partner_Cultural_Trust.pdf` |

A 7th paper — DeFond & Zhang (2014, *JAE*), *A review of archival auditing research* —
supplies the **conceptual framework** (see `audit_quality_framework.md`), not an intro
template. It is deliberately excluded from the empirical-structure counts.

---

## 1b. Stage-1 pilot decode table (16 papers; added 2026-05-21)

These 16 archival audit papers were distilled across intro / hypothesis / results in
Stage-1 Phase C. Their annotated staging tables live in
`corpus_inventory/track_b_drafts/<code>_{intro,hypothesis,results}.md`; source PDFs are
third-party (filenames in `corpus_inventory/gold_set_pilot.md`, not redistributed). They
are the basis for the `n=22` re-derived frequencies (§2 item 5).

| Code | Citation (author, year, journal) | Topic |
|---|---|---|
| `19-JWW` | Jiang, Wang & Wang (2019, *TAR*) | Big N auditors & audit quality; M&A quasi-experiments (US) |
| `22-LNS` | Lee, Naiker & Stewart (2022, *TAR*) | Audit-office labor-market proximity to universities |
| `23-ACN` | Aobdia, Choudhary & Newberger (2023, *TAR*) | Economics of audit production; middle managers (PCAOB data) |
| `20-WY` | Wu & Ye (2020, *JAR*) | Public attention & auditor behavior; Hurun Rich List (China) |
| `22-CHLP` | Chen, Huang, Li & Pittman (2022, *JAR*) | Auditor social connections & mutual-fund portfolios (China) |
| `22-Dug` | Duguay (2022, *JAR*) | Financial-audit regulation in the charitable sector |
| `23-ZBLM` | Zimmerman, Barr-Pulliam, Lee & Minutti-Meza (2023, *JAR*) | Auditors' use of in-house specialists |
| `24-Chen` | Chen (2024, *JAR*) | Employee lawsuits & talent acquisition in audit offices |
| `24-DGZZ` | De Franco, Guan, Zhou & Zhu (2024, *JAR*) | Credit-market development & auditor choice; banking deregulation |
| `19-Aob` | Aobdia (2019, *JAE*) | Practitioner assessments vs academic AQ proxies; PCAOB inspections |
| `19-BGH` | Beck, Gunn & Hallman (2019, *JAE*) | Geographic decentralization of audit firms |
| `20-CKMS` | Cook, Kowaleski, Minnis, Sutherland & Zehms (2020, *JAE*) | Auditor-client matching; US broker-dealer market |
| `16-DLLN` | Dhaliwal, Lamoreaux, Litov & Neyland (2016, *JAE*) | Shared auditors in M&A (substituted for out-of-scope survey paper 22-HS) |
| `23-PSZ` | Pan, Shroff & Zhang (2023, *JAE*) | Dark side of audit-market competition; bullet-train shock (China) |
| `22-FHKF` | Fedyk, Hodson, Khimich & Fedyk (2022, *RAST*) | Is AI improving the audit process; mixed-methods |
| `22-FW` | Fox & Wilson (2022, *RAST*) | IRS attention to financial-accounting restatements |

---

## 2. Verifiability note (read this before trusting a "k/6")

1. **Frequency claims are over THIS corpus, not the universe of audit papers.**
   "6/6 papers do X", "appears in 4/6" describe the six template papers above. They are
   strong, named priors — *not* universal law and *not* journal policy. A future pass of
   this suite will re-grade the "hard rules" into priors/defaults; until then, read
   "never / always" as "the template corpus is unanimous, deviate with reason."
2. **Quotes and ¶-anchors are traceable.** The six template papers plus the 2014
   framework review have plain-text extractions in `audit_writing_corpus/txt/`. A
   verbatim quote or `¶NNN` anchor in a pattern file refers to a paragraph index in the
   *extracted text*, not a journal page. Any quote can be checked against that source.
3. **Recency caveat.** Several template papers (2024–2026) were recent or forthcoming at
   build time. Treat specific quoted numbers / p-values in demos as illustrative of the
   *rhetorical move*, not as citable findings; verify against the published PDF before
   relying on any specific figure.
4. **Small, correlated sample.** n = 6, several DeFond-coauthored, mostly China-setting
   partner-trait designs. The register it teaches is real and high-value for that target
   (JAE/JAR/TAR audit-quality papers) but is a *style*, not a guarantee of acceptance.
5. **2026-05-21 Stage-1 update — corpus expanded to n = 22.** Sixteen Stage-1 pilot papers
   (§1b below) were distilled across intro / hypothesis / results. **Headline intro-move
   frequencies are now re-derived over n = 22** (6 template + 16 pilot) and written `k/22`
   in the pattern files, with the full per-paper coding in
   `corpus_inventory/move_presence_matrix.md`. Claims still written `k/6 (template)` refer to
   the **original 6 template papers only** — they are not yet re-coded over the pilot. Key
   re-derivations: M4 tension is no longer "6/6 unanimous" (canonical-form 7/22, any-form
   14/22, absent-from-intro 8/22); the "forbidden 0/6" opener rule has 2 counter-examples
   (20-WY anecdote, 22-Dug policy-motivation, both JAR); a new **M3-first / RQ-first opener
   family** (5/22) and new magnitude forms **F7 time-decline**, **F8 odds-ratio**, plus
   **F6 spatial / internal** sub-variants were added. The pilot is still correlated
   (audit × top-5 journals) but materially broadens journals (adds JAR/RAST), eras
   (2016–2024), and topics (M&A, AI, regulation, labor, mobility).

---

## 3. Full evidentiary set (29 items, tiered by role)

Built from a reference-manager export of an audit-research reading library. Tiers
indicate the role each item plays in the suite, not paper quality.

### Tier 1 — Framework / methodological core (5)

| Citation | Role in suite |
|---|---|
| DeFond & Zhang (2014, *JAE*) — archival auditing review ★ | Canonical audit-quality framework; input/output/outcome proxy taxonomy |
| DeFond & Zhang (2025) — audit failures | Updated perspective on causes of audit failure; pair with the 2014 review |
| DeFond, Li, Wong & Wu (2024, *JAE*) | Recent DeFond intro/structure exemplar (= `24-DLWW`) |
| DeFond, Qi, Si & Zhang (2025, *JAE*) | Signatory-auditor / partner-level identification exemplar (= `25-DQSZ`) |
| DeFond, Francis & Hallman (2018, *CAR*) | Going-concern outcome + spillover/awareness mechanism rhetoric |

### Tier 2 — DeFond empirical exemplars (4)

| Citation | Role |
|---|---|
| Becker, DeFond, Jiambalvo & Subramanyam (1998, *CAR*) | Founding DA-based audit-quality paper; early DeFond voice |
| DeFond, Hung & Trezevant (2007, *JAE*) | Clean cross-jurisdiction writing (= `07-DHT`) |
| DeFond, Lim & Zang (2016, *TAR*) | Auditor-conservatism mechanism; TAR-culture exemplar (= `16-DLZ`) |
| DeFond, Hu, Hung & Li (2020, *JAE*) | Recent DeFond JAE writing; cross-country setting |

### Tier 3 — Lennox lineage / China audit (5)

| Citation | Role |
|---|---|
| Lennox, Li & Wang (2025, preprint) | Updated companion to DeFond–Zhang 2014; cite alongside it |
| Lennox, Li & Qu (2025, *JAE*) | Reputation-spillover identification design |
| Lennox & Wu (2022, *JAE*) | 25-year China-audit review; institutional baseline for referees |
| Chu, Fisman, Wang & Ye (2026, *JAE*) | Cutting-edge China-audit quasi-experiment |
| Dekeyser, He, Xiao & Zuo (2024, *JAE*) | Zuo-lineage JAE auditing exemplar (= `24-DHXZ`) |

### Tier 4 — Measurement methodology (3)

| Citation | Role |
|---|---|
| Aobdia (2019, *JAE*) ★ | State of the art on whether DA / restatement proxies validly capture audit quality; must-cite |
| Rajgopal, Srinivasan & Zheng (2021, *RAS*) | Modern measurement framework; pair with DeFond–Zhang 2014 |
| Nelson & Tan (2005, *AJPT*) | Older review-structure benchmark |

### Tier 5 — Zuo lineage / review style (3)

| Citation | Role |
|---|---|
| He, Kothari, Xiao & Zuo (2022, *CAR*) | DiD design in China audit; polished writing |
| Hanlon, Yeung & Zuo (2022, *CAR*) | Review-paper style; useful for the framework section |
| Lin, Shi, Yuan & Zuo (2024, book ch.) | Synthesis of China-audit institutional setting |

### Tier 6 — Individual-auditor / partner-trait identification (4)

| Citation | Role |
|---|---|
| Gul, Wu & Yang (2013, *CAR*) | Foundational individual-auditor paper (China); widely cited |
| Kallunki, Kallunki, Niemi, Nilsson & Aobdia (2019, *CAR*) | Individual-auditor trait → audit quality design |
| He, Pittman, Rui & Wu (2017, *CAR*) | Social-tie identification chain |
| Chen, Chen, Han & Yuan (2022, *JAR*) | Recent JAR individual-auditor accountability exemplar |

### Tier 7 — Recent partner-trait / culture exemplars (5)

| Citation | Role |
|---|---|
| Khurana, Li, Yeung & Yu (2026, *JAE*) ★ | Primary structural template for partner-trait papers; pair-prediction device (= `26-KLYY`) |
| Jiang, He & Wang (2025, *JAE*) | Concise modern JAE partner-trait writing |
| Pandey et al. (2025, *JAE* conf.) | Recent JAE conference exemplar |
| He, Pittman, Sun & Zhuang (2026, *TAR*) | Partner-personality TAR paper; novel measurement section |
| Sharma, Wu & Xing (2026, *TAR*) | Recent China-TAR exemplar |

★ = anchor paper for its tier.

---

## 4. Known gap

| Missing | Affects | Workaround |
|---|---|---|
| DeFond, Erkens & Zhang (2017, *Management Science*) — PSM critique of the Big-N audit-quality effect | `audit-write-robustness` (post-2017 PSM-language) | Extract the PSM-critique rhetoric secondhand from the references *to* this paper inside DeFond & Zhang (2014) and DeFond et al. (2024); or obtain the SSRN working-paper version. The robustness skill's matching-language guidance is built from these secondary sources, not the primary paper. |

---

## 5. Adding to the corpus

If you extend or replace the corpus for your own field, keep this manifest in sync:
1. Add the citation to the relevant tier (and the decode table if it becomes a template paper with a shorthand code).
2. Add a `txt/` extraction if you want quotes from it to be verifiable.
3. Re-derive any frequency claim you change in the pattern files — do not leave a "k/6" that no longer matches the corpus size.

Filename convention: `<YEAR>_<JOURNAL>_<FirstAuthor>_<short_topic>.pdf`
(`JAE` J Acct & Econ · `JAR` J Acct Research · `TAR` The Accounting Review ·
`CAR` Contemporary Acct Res · `RAST` (a.k.a. RAS) Review of Acct Studies · `AJPT` Auditing: A J P&T ·
preprint / book chapter labeled explicitly).

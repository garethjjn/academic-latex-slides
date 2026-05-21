# Gold-set pilot — Stage 1 Track A (16 papers)

**Date assigned:** 2026-05-20
**Source:** marks in `corpus_inventory/audit_papers_to_curate.md`
**Pool:** 59 audit × top_acct papers from `paper/`

Used for Phase C distillation (15 papers × 3 sections = 45 annotated exemplars, per plan; we accept 16 for slight extra signal).

## Stratification check (vs plan §"Pilot scope")

| Stratum | Target | Got | Status |
|---|---|---|---|
| TAR | ≥ 2 | 3 | ✅ |
| JAR | ≥ 2 | 6 | ✅ |
| JAE | ≥ 2 | 5 | ✅ |
| RAST | ≥ 2 | 2 | ✅ |
| CAR | ≥ 2 | 0 | ❌ |
| 2013–2016 bucket | ≥ 4 | 0 | ❌ |
| 2017–2020 bucket | ≥ 4 | 5 | ✅ |
| 2021–2024 bucket | ≥ 4 | 11 | ✅ |

**Gaps:** zero CAR + zero pre-2017 in the pilot. Compensated in the held-out set (2 CAR + 6 pre-2017 there) — so Phase F re-eval will explicitly test whether the pilot's modern-JAE/JAR-era patterns generalize to older / CAR-style papers. If Phase F lift is positive on the early-CAR held-out tasks, that's strong evidence; if it's negative, the gap matters and Stage 1.5 needs CAR/early-era exemplars.

## Topical coverage (informal — fills `corpus_manifest.md` gaps)

| Topic | Pilot papers covering it |
|---|---|
| Audit fees / pricing | 23-PSZ (Pan-Shroff-Zhang), 22-LNS (Lee-Naiker-Stewart) |
| Partner traits | 19-Aob (Aobdia), 19-BGH (Beck-Gunn-Hallman), 22-CHLP (Chen-Huang-Li-Pittman), 24-DGZZ (De Franco) |
| PCAOB / regulation | 22-HS (Hanlon-Shroff), 23-ACN (Aobdia-Choudhary-Newberger), 22-Dug (Duguay) |
| Big-N / audit-firm econ | 19-JWW (Jiang-Wang-Wang), 23-PSZ |
| Restatement / misconduct | (limited — covered in held-out via 14-HLM Hennes, 22-FW Fox-Wilson) |
| Audit technology / AI | 22-FHKF (Fedyk-Hodson) |
| China-setting | 20-WY (Wu-Ye Hurun) |
| Auditor labor / mobility | 24-Chen (Employees lawsuits), 22-LNS (labor market proximity) |
| Going concern | (gap — not directly covered) |
| Internal control | (gap — covered in held-out via 14-BDE Badolato) |
| M&A audit | (gap — covered in held-out via 16-CKPW Cai) |

## The 16 pilot papers

Shorthand format: `YY-AABB` (year + 1st letter of up to 4 surnames; 3-letter form for single-author cases).

| # | Shorthand | Journal | Year | Authors | Title (short) |
|---|---|---|---|---|---|
| 1 | `19-JWW` | TAR | 2019 | Jiang, Wang, Wang | Big N / quasi-experiments |
| 2 | `22-LNS` | TAR | 2022 | Lee, Naiker, Stewart | Audit office labor proximity |
| 3 | `23-ACN` | TAR | 2023 | Aobdia, Choudhary, Newberger | Economics of audit production |
| 4 | `20-WY` | JAR | 2020 | Wu, Ye | Hurun rich list / China |
| 5 | `22-CHLP` | JAR | 2022 | Chen, Huang, Li, Pittman | Auditor social connections / mutual funds |
| 6 | `22-Dug` | JAR | 2022 | Duguay | Audit reg / charitable sector |
| 7 | `23-ZBLM` | JAR | 2023 | Zimmerman, Barr-Pulliam, Lee, Minutti-Meza | In-house specialists |
| 8 | `24-Chen` | JAR | 2024 | Chen | Employee lawsuits / audit offices |
| 9 | `24-DGZZ` | JAR | 2024 | De Franco, Guan, Zhou, Zhu | Credit market / auditor choice |
| 10 | `19-Aob` | JAE | 2019 | Aobdia | Practitioner assessments / PCAOB |
| 11 | `19-BGH` | JAE | 2019 | Beck, Gunn, Hallman | Geographic decentralization |
| 12 | `20-CKMS` | JAE | 2020 | Cook, Kowaleski, Minnis, Sutherland (+Zehms) | Auditors known by companies |
| 13 | `16-DLLN` | JAE | 2016 | Dhaliwal, Lamoreaux, Litov, Neyland | Shared auditors in M&A (substituted 2026-05-21 for 22-HS which was a survey-methodology paper out of scope) |
| 14 | `23-PSZ` | JAE | 2023 | Pan, Shroff, Zhang | Dark side of competition |
| 15 | `22-FHKF` | RAST | 2022 | Fedyk, Hodson, Khimich, Fedyk | AI improving audit process |
| 16 | `22-FW` | RAST | 2022 | Fox, Wilson | IRS / restatements |

## Filenames (paper/ source)

| Shorthand | Filename |
|---|---|
| `19-JWW` | `2019 - Jiang, Wang, Wang - The Accounting Review - Big N Auditors and Audit Quality New Evidence from Quasi-Experiments.pdf` |
| `22-LNS` | `2022 - Lee, Naiker, Stewart - The Accounting Review - Audit Office Labor Market Proximity and Audit Quality.pdf` |
| `23-ACN` | `2023 - Aobdia, Choudhary, Newberger - The Accounting Review - The Economics of Audit Production What Matters for Audit Quality An Empirical Analysis of the Role.pdf` |
| `20-WY` | `2020 - Wu, Ye - Journal of Accounting Research - Public Attention and Auditor Behavior The Case of Hurun Rich List in China.pdf` |
| `22-CHLP` | `2022 - Chen, Huang, Li, Pittman - Journal of Accounting Research - It's a Small World The Importance of Social Connections with Auditors to Mutual Fund Managers' Port.pdf` |
| `22-Dug` | `2022 - Duguay - Journal of Accounting Research - The Economic Consequences of Financial Audit Regulation in the Charitable Sector.pdf` |
| `23-ZBLM` | `2023 - Zimmerman, Barr‐Pulliam, Lee, Minutti‐Meza - Journal of Accounting Research - Auditors' Use of In‐House Specialists.pdf` |
| `24-Chen` | `2024 - Chen - Journal of Accounting Research - When Employees Go to Court Employee Lawsuits and Talent Acquisition in Audit Offices 3.pdf` |
| `24-DGZZ` | `2024 - De Franco, Guan, Zhou, Zhu - Journal of Accounting Research - The Impact of Credit Market Development on Auditor Choice Evidence from Banking Deregulation.pdf` |
| `19-Aob` | `2019 - Aobdia - Journal of Accounting and Economics - Do Practitioner Assessments Agree with Academic Proxies for Audit Quality Evidence from PCAOB and I.pdf` |
| `19-BGH` | `2019 - Beck, Gunn, Hallman - Journal of Accounting and Economics - The Geographic Decentralization of Audit Firms and Audit Quality.pdf` |
| `20-CKMS` | `2020 - Cook, Kowaleski, Minnis, Sutherland, Zehms - Journal of Accounting and Economics - Auditors Are Known by the Companies They Keep.pdf` |
| `16-DLLN` | `2016 - Dhaliwal, Lamoreaux, Litov, Neyland - Journal of Accounting and Economics - Shared Auditors in Mergers and Acquisitions.pdf` |
| `23-PSZ` | `2023 - Pan, Shroff, Zhang - Journal of Accounting and Economics - The Dark Side of Audit Market Competition.pdf` |
| `22-FHKF` | `2022 - Fedyk, Hodson, Khimich, Fedyk - Review of Accounting Studies - Is Artificial Intelligence Improving the Audit Process.pdf` |
| `22-FW` | `2022 - Fox, Wilson - Review of Accounting Studies - Double Trouble Irs's Attention to Financial Accounting Restatements.pdf` |

## Cross-corpus availability

8 of the 16 pilot papers also exist in `audit_writing_corpus/` (the working text-extracted corpus the existing audit-write skill uses). Verified by grep of CORPUS_INDEX during this session's earlier inventory. The other 8 will use paper/ PDFs via PyMuPDF in Phase C.

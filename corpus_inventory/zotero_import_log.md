# Zotero import log — audit-write Stage 1 candidates

**Date:** 2026-05-20
**Source:** `d:/OneDrive/tools/paper/` (audit × top_acct, not previously in Zotero)
**Target collection:** `audit-write_stage1_candidates` (key `IZWDUHTJ`)
**Tags applied:** `audit`, `stage1_candidate`, `imported_from_paper_dir`
**Total imported:** 53 PDFs (1 test + 52 batch) — 0 net failures, 0 final duplicates.

## Incident note (kept for transparency)

The first verification round mis-diagnosed Batches 2–5 as having "phantom-failed" because:
1. `zotero_get_item_metadata` returned 404 on freshly-created keys (eventual-consistency lag in Zotero's local API server)
2. `zotero_get_recent` did not yet show items past index ~24

Acting on that wrong diagnosis, 7 retries were attempted and ALL 7 actually landed — creating 7 true duplicates. Subsequently:
- `zotero_find_duplicates` (method=title, scoped to collection IZWDUHTJ) confirmed exactly 7 duplicate groups
- `zotero_merge_duplicates` consolidated each pair, keeping the original (first import) and trashing the retry
- Trashed retry keys (recoverable from Zotero Trash): `XFSJVQNA`, `N6BWE96F`, `6HSDTK6R`, `4WB9HRKP`, `JUGH73R7`, `RM37VN4V`, `RRZ6FIEZ`
- Final state verified: 53 unique items, 0 duplicates.

**Lesson:** After bulk MCP writes, wait ≥ a few seconds before verifying via `get_item_metadata` (it lags). Use `zotero_find_duplicates` on the target collection rather than per-item 404 checks.

## Import-key → paper/ filename map

| Zotero key | Year | Authors | Filename hint |
|---|---|---|---|
| `77D6KF9E` | 2014 | Badolato, Donelson, Ege | Audit Committee Financial Expertise and Earnings Management |
| `5EF6N2BC` | 2013 | Libby, Brown | Financial Statement Disaggregation Decisions |
| `5SAZFTZW` | 2013 | Lobo, Zhao | Relation between audit effort and financial report misstatements |
| `UDSN5NGD` | 2013 | Markelevich, Rosner | Auditor Fees and Fraud Firms |
| `77AJUPU2` | 2013 | Minutti-Meza | Auditor Industry Specialization |
| `94D5E65Q` | 2014 | Chakravarthy, deHaan, Rajgopal | Reputation Repair After a Serious Restatement |
| `I6I4V6GP` | 2014 | Francis, Pinnuck, Watanabe | Auditor style and financial statement comparability |
| `A23CREC5` | 2014 | Goodwin, Wu | Industry Expertise on Audit Pricing |
| `HGVUN3J7` | 2014 | Lennox, Li | Accounting Misstatements Following Lawsuits Against Auditors |
| `E6ECXKWB` | 2015 | Aobdia, Lin, Petacchi | Capital Market Consequences of Audit Partner Quality |
| `FGZZT2X5` | 2015 | Jayaraman, Milbourn | CEO Equity Incentives and Auditor Expertise |
| `NSXASMNR` | 2015 | Rice, Weber, Wu | SOX 404 / failure to report internal control weaknesses |
| `GDVU7CCJ` | 2015 | Robert Knechel, Vanstraelen, Zerni | Identity of Engagement Partners |
| `WM5GZ5VA` | 2016 | Cai, Kim, Park, White | Common auditors in M&A transactions |
| `DJCI559V` | 2016 | Dhaliwal, Lamoreaux, Litov, Neyland | Shared Auditors in M&A |
| `KQZGE287` | 2016 | Kausar, Shroff, White | Real Effects of the Audit Choice |
| `QA8A7M78` | 2016 | Newton, Persellin, Wang, Wilkins | Internal Control Opinion Shopping |
| `SQMGA2ZI` | 2016 | Schroeder, Shepardson | SOX 404 Control Audits |
| `ZRVU4QUW` | 2017 | Chi, Myers, Omer, Xie | Audit Partner Pre-Client / Client-Specific Experience |
| `VKG3QMBA` | 2018 | He, Kothari, Xiao, Zuo | Long-Term Impact of Economic Conditions on Auditors' Judgment |
| `22KQFQQD` | 2019 | Beck, Gunn, Hallman | Geographic Decentralization of Audit Firms |
| `GB7K5SH8` | 2019 | Drake, Lamoreaux, Quinn, Thornock | Auditor Benchmarking of Client Disclosures |
| `2V99W7IH` | 2019 | Jiang, Wang, Wang | Big N Auditors and Audit Quality (Quasi-Experiments) |
| `H59WGZ2P` | 2020 | Chen, Feng, Li | Family entrenchment and internal control |
| `EGHMKWNS` | 2020 | Cook, Kowaleski, Minnis, Sutherland, Zehms | Auditors Are Known by the Companies They Keep |
| `4PUT5SAS` | 2020 | Shroff | Real Effects of PCAOB International Inspections |
| `NUR4DT5K` | 2020 | Wu, Ye | Public Attention and Auditor Behavior (Hurun Rich List) |
| `464VBDTC` | 2021 | Austin, Carpenter, Christ, Nielson | Data Analytics Journey |
| `QEMHRN98` | 2021 | Chapman, Drake, Schroeder, Seidel | Earnings Announcement Delays + Auditor-Client |
| `T7NBAZWQ` | 2021 | Knechel, Mao, Qi, Zhuang | Brain Drain in Auditing |
| `C9UZZ292` | 2022 | Chen, Huang, Li, Pittman | Small World / Social Connections / Auditors / Mutual Funds |
| `TQZNTJ4B` | 2022 | Cowle, Rowe | Don't Make Me Look Bad |
| `52Q6FB5D` | 2022 | Duguay | Financial Audit Regulation in Charitable Sector |
| `Q5KFQ35C` | 2022 | Ege, Seidel, Sterin, Wood | Management's Internal Audit Experience on EM |
| `C6ZAIBB5` | 2022 | Eulerich, Pawlowski, Waddoups, Wood | RPA for Audit Tasks |
| `XNQN8TUX` | 2022 | Fox, Wilson | Double Trouble / IRS / Restatements |
| `K6SHC7CI` | 2022 | Hanlon, Shroff | Auditor Public Oversight Boards |
| `F89FNJJ6` | 2022 | Hendricks, Landsman, Peña-Romera | Revolving Door / PCAOB |
| `KKBJGF68` | 2022 | Lee, Naiker, Stewart | Audit Office Labor Market Proximity |
| `2KB97GMQ` | 2022 | Ranasinghe, Yi, Zhou | Client Business Risk Premium / Derivatives |
| `XXNUE6UJ` | 2023 | Aobdia, Choudhary, Newberger | Economics of Audit Production |
| `J6GDGFS4` | 2023 | Blann, Kleppe, Shipman | PCAOB 2009 Office Expansion |
| `WUDF3JGP` | 2023 | Burke, Hoitash, Hoitash, Xiao | Critical Audit Matters (US) |
| `D2MBNGQD` | 2023 | Condie, Lisic, Seidel, Truelson, Zimmerman | Gender/Ethnic Diversity Among Audit Partners |
| `JHR2RJZH` | 2023 | Ege, Kim, Wang | Internal Auditors / Accounting and Operational Failures |
| `3Q9F8I6M` | 2023 | Eulerich, Masli, Pickerd, Wood | Audit Technology on Audit Task Outcomes |
| `P53AGTSQ` | 2023 | Pan, Shroff, Zhang | Dark Side of Audit Market Competition |
| `9NUD3B7V` | 2023 | Zimmerman, Barr‐Pulliam, Lee, Minutti‐Meza | Auditors' Use of In-House Specialists |
| `M6IXA2CP` | 2024 | Chen | When Employees Go to Court / Audit Offices |
| `N9D3GQPU` | 2024 | De Franco, Guan, Zhou, Zhu | Credit Market Development on Auditor Choice |
| `5NHR9TV8` | 2024 | Ege, Kim, Wang | Auditor Distraction / Outside Job Opportunities |
| `4KRII8PU` | 2024 | Frost, Jing, Shang, Su | Foreign Labor and Audit Quality / H-1B |
| `FF7CUPGJ` | 2024 | Heflin, Tan, Ton, Wang | Auditor style on non-GAAP disclosure |

## Notes

- The collection `audit-write_stage1_candidates` (key `IZWDUHTJ`) was created clean for this batch — it does NOT mix with the user's existing `integrity_propaganda_audit` collection. The user can move/merge later.
- All items have PDF attached (DOI extraction attempted automatically by Zotero).
- Some items will have rich metadata (DOI found), others may need manual metadata cleanup if Zotero's DOI extraction failed for that PDF. Verify in Zotero UI by skimming each item.
- Semantic search NOT indexed (chromadb not installed locally) — does not affect Stage 1 distillation workflow which is metadata-based.

## Reversal command (if needed)

To remove all 53 items from Zotero, in the Zotero desktop UI: right-click the `audit-write_stage1_candidates` collection → "Delete Collection and Items" → confirm. (The PDFs in `d:/OneDrive/tools/paper/` are NOT affected — only their Zotero copies are removed.)

# Held-out set — Stage 1 Phases B + F (10 papers)

**Date assigned:** 2026-05-20
**Source:** auto-selected from unmarked papers in `audit_papers_to_curate.md` (user marked pilot but not held-out)
**Pool:** 59 audit × top_acct papers from `paper/`, minus 16 pilot picks

These 10 papers are **never read during Phase C distillation, Phase D frequency derivation, or Phase E manifest updates**. They are reserved for:
- **Phase B baseline eval** (3 papers, 1 section each — see assignment below)
- **Phase F re-eval + ablation** (same 3 + 1 new = 4 total tasks)

## Selection rationale

The pilot is heavily 2019–2024, top-tier-JAR/JAE, no CAR, no pre-2017. To make the eval set a meaningful test of generalization, the held-out is **deliberately biased the opposite way** — heavy on CAR + pre-2017. If Phase F lift is positive here, the pilot's patterns generalize across journals and eras; if negative, the gap matters and Stage 1.5 needs to backfill.

Stratification:

| Stratum | Held-out | Comp vs pilot |
|---|---|---|
| TAR | 2 | pilot=3 |
| JAR | 1 | pilot=6 |
| JAE | 3 | pilot=5 |
| RAST | 2 | pilot=2 |
| CAR | 2 | pilot=0 ← critical fill |
| 2013–2016 | 8 | pilot=0 ← critical fill |
| 2017–2020 | 1 | pilot=5 |
| 2021–2024 | 1 | pilot=11 |

## Scope constraint (2026-05-20 clarification)

**The `audit-write` skill suite is positioned for ARCHIVAL audit research only — NOT experimental / behavioral / survey methods.** Papers using auditor experiments (e.g., Libby-Brown 2013) are out of scope and should not be used for baseline / evaluation tasks. The original auto-selection of `13-LB` Libby-Brown 2013 (experimental) is invalid; it is replaced by **14-FPW Francis-Pinnuck-Watanabe 2014 TAR "Auditor style and financial statement comparability"** (archival, classic Francis-era).

## The 10 held-out papers

| # | Shorthand | Journal | Year | Authors | Title (short) | Topic angle |
|---|---|---|---|---|---|---|
| 1 | `14-FPW` | TAR | 2014 | Francis, Pinnuck, Watanabe | Auditor style and financial statement comparability | Auditor-style proxy / consistency |
| 2 | `14-HLM` | TAR | 2014 | Hennes, Leone, Miller | Auditor dismissals after restatements | Restatement / consequence |
| 3 | `13-MM` | JAR | 2013 | Minutti-Meza | Industry specialization | Audit-firm-level / PSM |
| 4 | `14-LL` | JAE | 2014 | Lennox, Li | Misstatements after lawsuits | Litigation / restatement |
| 5 | `14-BDE` | JAE | 2014 | Badolato, Donelson, Ege | Audit committee expertise + EM | Audit committee / EM |
| 6 | `16-CKPW` | JAE | 2016 | Cai, Kim, Park, White | Common auditors / M&A | M&A audit |
| 7 | `14-GW` | RAST | 2014 | Goodwin, Wu | Industry expertise on pricing | Audit pricing / partner-vs-office |
| 8 | `17-CMOX` | RAST | 2017 | Chi, Myers, Omer, Xie | Partner pre-client experience | Partner traits |
| 9 | `13-MR` | CAR | 2013 | Markelevich, Rosner | Auditor fees / fraud firms | Fraud / audit fees |
| 10 | `15-KVZ` | CAR | 2015 | Knechel, Vanstraelen, Zerni | Engagement partners matter | Partner-level reporting |

## Phase B assignments (3 papers, 1 section each)

Phase B baseline drafts will use the sub-skills on these (section-stripped) held-out papers, then `audit-write-critic` scores the drafts.

| Section | Paper | Shorthand | Why this paper |
|---|---|---|---|
| **intro** | Francis, Pinnuck, Watanabe 2014 (TAR) | `14-FPW` | Classic archival auditor-style paper, TAR-canonical intro; in-scope (archival), pre-2017 era |
| **hypothesis** | Chi, Myers, Omer, Xie 2017 (RAST) | `17-CMOX` | Partner-trait paper, hypothesis-rich (5+ predictions); tests baseline hypothesis development |
| **results** | Hennes, Leone, Miller 2014 (TAR) | `14-HLM` | Clear empirical setup (restatement → dismissal); tests baseline results-section quality |

Phase F will re-test on the SAME 3 + 1 new (likely 16-CKPW or 14-BDE for variety).

## Filenames (paper/ source)

| Shorthand | Filename |
|---|---|
| `14-FPW` | `2014 - Francis, Pinnuck, Watanabe - The Accounting Review - Auditor style and financial statement comparability.pdf` |
| `14-HLM` | `2014 - Hennes, Leone, Miller - The Accounting Review - Determinants and Market Consequences of Auditor Dismissals After Accounting Restatements.pdf` |
| `13-MM` | `2013 - Minutti-Meza - Journal of Accounting Research - Does Auditor Industry Specialization Improve Audit Quality Does Auditor Industry Specialization Im.pdf` |
| `14-LL` | `2014 - Lennox, Li - Journal of Accounting and Economics - Accounting Misstatements Following Lawsuits Against Auditors.pdf` |
| `14-BDE` | `2014 - Badolato, Donelson, Ege - Journal of Accounting and Economics - Audit Committee Financial Expertise and Earnings Management The Role of Status.pdf` |
| `16-CKPW` | `2016 - Cai, Kim, Park, White - Journal of Accounting and Economics - Common auditors in M&A transactions.pdf` |
| `14-GW` | `2014 - Goodwin, Wu - Review of Accounting Studies - Is the Effect of Industry Expertise on Audit Pricing an Office-Level or a Partner-Level Phenomenon.pdf` |
| `17-CMOX` | `2017 - Chi, Myers, Omer, Xie - Review of Accounting Studies - The Effects of Audit Partner Pre-Client and Client-Specific Experience on Audit Quality and on Perce.pdf` |
| `13-MR` | `2013 - Markelevich, Rosner - Contemporary Accounting Research - Auditor Fees and Fraud Firms.pdf` |
| `15-KVZ` | `2015 - Knechel, Vanstraelen, Zerni - Contemporary Accounting Research - Does the Identity of Engagement Partners Matter An Analysis of Audit Partner Reporting Decisions.pdf` |

## Anti-leakage protocol

- During Phase C/D/E, I will NOT open these 10 PDFs for any purpose other than the Phase B baseline drafting prompt (where only abstract + tables + setup paragraph are extracted, not the section being drafted).
- After Phase B, the held-out PDFs are quarantined from my reading until Phase F.
- For B3 Track B validation (separate from these held-outs), I use the 4 corpus_manifest exemplars (16-DLZ, 24-DLWW, 25-DQSZ, 26-KLYY) which are different papers and have ground-truth annotations to compare against.

## What about the remaining 33 unmarked papers?

The remaining `59 - 16 pilot - 10 held-out = 33 unmarked` papers are reserved as **future expansion** for Stage 1.5 (after Phase F decides go/no-go) or Stage 2/3 spokes. They are NOT touched during Stage 1.

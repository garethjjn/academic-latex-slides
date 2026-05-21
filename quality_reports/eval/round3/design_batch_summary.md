# R3 design pilot — generation phase summary (2026-05-22)

## Infra (Step 0)
- pdf_section_split.py: added abstract/design/robustness section vocabularies + per-section excludes.
- batch_generate_results_drafts.py: generalized to --section (SECTION_CONFIG); results behaviour unchanged.

## Design extraction: 13/16 OK
- FAIL (3, no API spent): 23-ACN, 20-WY, 16-DLLN — header-detection pollution in their .clean.txt
  (author names / dates misread as section headers). Deeper splitter fix; deferred.

## Generation (qwen3.6-plus, 13 papers)
- Quote+lint gates: 3 PASS (22-CHLP, 22-Dug, 24-DGZZ); 10 NEEDS_REVIEW; lint clean except 19-JWW.
- Deterministic repair (repair_draft_quotes.py --apply): fixed 13 quotes; 21 residuals.
- Post-repair audit: each draft has 12-15 verified quotes + 1-7 residual notfound (paraphrase /
  table-row / footnote-marker artifacts e.g. "OLS.10", "2001e2017"). Residuals stay flagged in
  the DRAFT staging files (status DRAFT, pending human review).

## Verdict
13 design drafts are sufficient raw material for the design digest. Next: baseline (held-out
design task) -> author digest into design_patterns.md -> verify/strengthen C5 gate -> held-out
regression (accept iff >= baseline) -> commit. Residual-quote handling (drop vs LLM-repair vs
leave-flagged) is a decision before committing the staging drafts.

## Cleanup applied (2026-05-22)
- drop_failing_quotes.py (new reusable tool) --min-keep=8 --apply: all 13 design drafts now
  quote-clean against their .clean.txt source (8-15 verified quotes each; residuals removed).
- TOOLING NOTE / debt: audit_draft_quotes.py globs the RAW .txt while the batch quote gate +
  drop_failing_quotes use the .clean.txt companion (preclean output, = what the model was given).
  They disagree on a few quotes. Authoritative source = .clean.txt. Reconcile audit_draft_quotes
  to prefer .clean.txt in a later cleanup (not blocking the pilot).

## State at checkpoint
- Infra (splitter + generator + drop tool) + 13 clean design drafts: WORKING TREE, uncommitted.
- Next (design closed loop): baseline (held-out design task + critic) -> author digest into
  design_patterns.md -> verify/strengthen design C5 + SKILL Step-3 + golden tests -> held-out
  regression (accept iff >= baseline) -> commit pilot.

## Design pilot regression (2026-05-22) — go/no-go MET
- Held-out 14-FPW design, identical brief, blind drafter+critic.
- Pre-deepen baseline: **82** (Dim1 Weak — no descriptive-stats, flat controls, no Petersen cite).
- Post-deepen (digest + strengthened C5 + SKILL Step-3 gate): **82** (Dim1 still Weak).
- Accept: 82 >= 82 (no regression). PASS.

## Key finding (carry-forward, confirms enforcement > content)
- The new C5 gate FORCED a descriptive-statistics block (baseline lacked it) -> that element fixed.
- BUT control-tiering (categorical control groups) was taught only in the digest (§13b item 3),
  NOT mechanized -> the drafter still produced a FLAT control list -> Dim1 stayed Weak -> score
  held at 82 instead of lifting. Exactly the Round-2 lesson: content alone doesn't move the
  held-out score; only a mechanical gate does.
- NEXT LEVER (to push design >82): add a control-tiering heuristic check to check_structure
  --section design (detect >=2 named control categories). Deferred — pilot go/no-go already met.

## Pilot verdict: METHOD VALIDATED
Infra generalized (splitter+generator+drop tool), 13 design drafts distilled into design_patterns
§13b digest, design C5 strengthened (+golden tests 12/12), SKILL Step-3 gate added, held-out
held at baseline. Ready to replicate to abstract (needs pre-intro extractor) + robustness.

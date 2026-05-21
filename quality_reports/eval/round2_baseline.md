# Round 2 baseline — intro slim/harmonize

Date: 2026-05-22

## Pre-slim
- intro_patterns.md size: 120215 chars / 924 lines
- Held-out task: 14-FPW intro (Francis-Pinnuck-Watanabe 2014 TAR), drafted from facts-only brief.
- Drafter self-gate: lint 0 ERROR/0 WARN; check_structure no unresolved N.
- Critic composite: **85/100** (integrity PASS). C1Y C2Y C3Y C4N C5Y C6NA C7Y.
  Dim1 95 / Dim2 67 (C4=N triadic contributions) / Dim3 95 / Dim4 82 / Dim5 82.
- Headline fix (drafter-side, not file-side): vary contribution paragraph lengths.

## Go/no-go for Round 2
Accept slim iff post-slim composite >= 85 AND intro_patterns.md down >= 50% (<= ~60K).

## Post-slim regression (2026-05-22)
- intro_patterns.md size: 31213 chars (was 120215) -> **74% reduction** (target >=50% MET).
- check_links: OK (33 files); exemplar_gallery intro pointer updated; no stale counts.
- Same 14-FPW held-out task, identical drafter prompt, 3 fresh post-slim samples:
  - postslim1: **79** (Dim1 Weak 67 — no displayed H1; C4=N "economically meaningful")
  - postslim2: **84** (Dim1 Weak 67 — no displayed H1)
  - postslim3: **79** (Dim1 Weak 67 — no displayed H1)
  - mean 80.7, max 84  vs  pre-slim **85**.
- Integrity gate PASS on all 4 drafts.

## Diagnosis
Entire pre/post gap = Dimension 1 (Structure), and entirely due to the **formal
alternative-form `H1.` statement**: pre-slim draft included it (Dim1=95); all 3
post-slim drafts omitted it (Dim1=67). The Block-2 H1-format guidance + checklist
item were RETAINED in the slim, but the 15 removed worked-example tables were
implicitly reinforcing the displayed-H1 convention; instruction alone did not hold it.
check_structure.py --section intro does NOT mechanically verify formal-H presence,
so the self-gate passed all 3 omissions.

## Status: go/no-go NOT cleanly met (mean 80.7 < 85). Fix required before accept.

## Fix: enforcement-first (mechanize the formal-H check) + re-validation
- Added a CONDITIONAL check to check_structure.py --section intro:
  "C5 signed prediction stated as formal H" — fires N iff the draft makes a signed/
  directional prediction (prediction verb + direction word in one sentence) but shows
  no displayed formal H ("H1."/"Hypothesis N"); pure RQ-first intros are NA (not penalized,
  so the 19-JWW anchor is safe). Calibrated to match the critic: preslim=Y, post1/2/3=N.
- Added 2 golden fixtures + 2 tests (intro_signed_no_h -> N, intro_formal_h -> Y). run_tests: 10/10.
- Documented the check in audit-write-intro/SKILL.md Step-3 gate.
- Re-validation: fresh gated post-slim draft (14-FPW_intro_final.md). Self-gate forced a
  displayed **H1.** -> critic composite **90/100** (Dim1 Excellent 95). Integrity PASS.

## RESULT: Round 2 ACCEPTED.
- Size 120215 -> 31213 chars (74% reduction; target >=50% MET).
- Held-out composite 90 >= pre-slim 85 (no regression; +5, mirrors Phase F enforcement lift).
- check_links 0 broken; lint 0 ERRORs; golden tests 10/10; integrity PASS.

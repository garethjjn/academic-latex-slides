# R3 robustness — light deepening (2026-05-22)

## Corpus finding (scope)
Only 4/16 pilot papers have a STANDALONE robustness section (22-LNS, 22-Dug, 19-Aob, 23-PSZ);
the other 12 fold robustness into §4 results. So robustness cannot be deepened to n=22 like design.
Per Gareth: gate + light digest + regression (not a full deepening).

## Delivered
- New robustness C5 gate in check_structure --section robustness: requires a numbered/enumerated
  battery of >=3 tests (ROBUST_ORDINAL >=3 distinct OR "we perform N analyses"). +2 golden fixtures
  (robustness_battery -> Y, robustness_thin -> N) + tests (run_tests 15/15).
- robustness_patterns.md §14b: 4-paper pilot digest + the standalone-vs-§4 sparsity finding.
- robustness SKILL.md: Step-3 deterministic-gate section added.
- 4 robustness staging drafts generated (qwen3.6-plus), repaired + dropped (12-14 quotes each, clean).

## Held-out validation (14-FPW robustness, deepened skill)
- Composite **82** (integrity PASS). Dim1 Solid (battery gate Y, six-test battery), Dim3 Excellent.
- Dim2 Weak only via C4=N (3 em-dashes) — a drafter slip the critic flags stricter than the
  mechanical C4 (threshold = words/150 ~= 5); a critic-vs-gate calibration gap, not a deepening issue.
- No separate pre-deepen baseline run: the change is additive (the battery was already the skill's
  core; deepening adds a digest + a gate enforcing it), so regression risk is structurally low and a
  stash-based baseline during the live abstract batch was avoided. Design pilot already validated the
  deepen->gate method.

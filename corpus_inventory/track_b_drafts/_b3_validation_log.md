# B3 validation log — audit-pdf-reader v0 ground-truth parity

**Protocol:** manual execution of agent protocol (agent file not yet visible in harness's `subagent_type` enum after CLI restart; orchestrator role-played the agent's 8 procedural steps). Critic agent (`audit-write-critic`, registered) scored both staging draft and ground-truth annotated exemplar against `rubric.md`.

**B3 pass threshold (handoff §1):** ≥ 9 of 12 (paper × section) combos with |Δ| ≤ 5. Conditional pass: 7–8 of 12. Fail: ≤ 6 of 12.

## Results

| Date | Shorthand | Section | Protocol | Agent score | Ground-truth score | Δ | Pass (|Δ|≤5)? | Notes |
|---|---|---|---|---|---|---|---|---|
| 2026-05-20 | 26-KLYY | intro | v0 | 82 | 92 | -10 | ❌ FAIL | Dim 1 -28 (missing Block 5; Block 2b compressed). Dim 3 -13 (17%/15% F2 numerics in annotation cells not verified). Dims 2/4/5 at parity. Root cause: v0 row-count guidance (5-8) too low. |
| 2026-05-20 | 26-KLYY | intro | v1 | 92 | 87 | +5 | ✅ PASS (margin) | v1 added rows 9-15 covering Block 4 magnitude pair, secondary finding, Block 5, and second contribution. v1 staging draft outscores re-evaluated ground truth (87) because v1 includes commentary; ground truth is thin 3-column table. Critic's re-scored ground truth differs from v0-run (92 → 87) — calibration drift noted. v1 protocol validated for intro section. Remaining minor flaw: Block 2 ¶ numbers all show ¶1 (splitter convention) vs ground truth ¶4-7 (source-paper convention) — documented as splitter v0 limitation. |
| 2026-05-20 | 26-KLYY | hypothesis | v1 | 86.8 | 95 | -8.2 | ❌ FAIL (marginal) | v1 14-row draft missed §2.1 concrete-example, §2.1 epidemiological justification, §2.2.3 H3 sub-anchor. Critic's first diagnostic was structurally specific. |
| 2026-05-20 | 26-KLYY | hypothesis | v1.1 | 86.8 | 95 | -8.2 | ❌ FAIL (marginal) | v1.1 added the 3 named rows (17 rows now matching GT count), but critic's second diagnostic identified 3 MORE missing sub-anchor / tension rows (§2.2.1 ¶1 PCAOB AS 2415 institutional sub-anchor; §2.2.2 ¶1 H2 sub-anchor; §2.2.2 ¶3 H2(b) tension). Δ unchanged at -8.2 — Dim 1 remains Weak. Pattern: critic chases per-iteration row gaps; matching source paragraph count is the implicit target. Agent file updated to v1.2 with "match source paragraph count for multi-H sections" guidance. Phase C accept-with-edit will close residual gaps. |

## Pattern after 2/12 runs

| Section type | v1 first-try Δ | Diagnosis |
|---|---|---|
| Intro (5-block) | +5 (PASS marginal) | v1 hits target; structure granularity matches ground truth's typical 14-row mapping. |
| Hypothesis (multi-H 6-move) | -8.2 (FAIL marginal) | v1's "≥12 rows" undershoots multi-H papers where source has 17+ paragraphs and ground truth uses per-paragraph mapping with distinct sub-anchor + tension + mechanism rows for each H. Iteration toward 1:1 paragraph match required to close gap. |

**Critic-iteration chase:** B3.2 v1 → v1.1 added 3 rows the critic named; critic then named 3 more. This suggests the critic uses 1:1 paragraph-to-row as its implicit Dim 1 standard. The agent's coarse splitter doesn't easily expose true paragraph boundaries; the agent's row-count target should match the source paper's section paragraph count for full Dim 1 Excellent. Agent file updated to v1.2 with this guidance.

**Phase C implication:** v1 protocol produces structurally-improved drafts (vs v0) that still fall slightly below ground-truth parity on dense multi-H sections. Phase C's accept-with-edit step is designed to close residual granularity gaps via human review — the agent's job is to draft the canonical-move-coverage; the reviewer's job is to expand sub-anchor / tension rows to per-paragraph granularity. Expect Phase C agent-draft accept rate ~70% on intros (clean), ~50% on multi-H hypotheses (more edits needed), unknown on results (B3.3-onward pending).

## B3.1 diagnostic (single test as of 2026-05-20)

**Driver 1 — under-extraction of rows.** The v0 protocol's "select 5-8 candidate paragraphs" guidance produced 8 rows. Ground truth has 14 rows because the manual distiller resolved each canonical move into its own row. With only 8 rows, the staging draft is forced to choose: which moves get dedicated rows, which get conflated. The choices compressed Block 2 (skipped explicit tension and counter rows) and dropped Block 5 entirely.

**Driver 2 — annotation-cell provenance discipline.** The staging draft introduced supplementary magnitudes ("17%/15%") into Row 7's annotation cell to anchor the F2 percent-of-base pairing. These numerics did not pass through `verify_quote.py` (which only checks the Quote column). The ground truth avoids this by keeping numerics inside verbatim quote cells only. The agent protocol does not currently forbid annotation-cell numerics.

**Non-drivers — confirmed parity.** Dims 2 (Register), 4 (Argument), 5 (Vocabulary) showed parity. The annotation column's prose is clean (no blacklist verbs, no AI tells, no marketing register). The commentary identifies the paper's distinctive structural choices (pair-prediction H(a)/H(b) device, F4+F2 magnitude pairing, two-contribution short variant). Move/Block taxonomy labels match the canonical convention.

**Implication for v0 design.** Two protocol fixes would mechanically close most of the gap (Dim 1 by ~25 points, Dim 3 by ~10 points), pushing the parity Δ from -10 toward -3 (within |Δ| ≤ 5):

1. **Bump row guidance** from "5-8" to "≥ 12, covering all 5 blocks + final block + tension + counter + secondary findings where present". The splitter's coarse paragraphs don't prevent fine-grained row-level move extraction — the limit was the agent's stated target.
2. **Forbid annotation-cell numerics** unless they appear verbatim in the row's Quote column. Magnitudes belong in the Quote column.

**Splitter is not the binding constraint.** Earlier worry was that v0's coarse 3-mega-paragraph extraction would inherently prevent ground-truth parity. The critic's diagnosis indicates otherwise: the structural granularity gap is in the AGENT (row-count target + annotation discipline), not in the splitter. A v1 protocol with the two fixes above could plausibly achieve B3 pass without touching `pdf_section_split.py`.

## Decision — closed 2026-05-20

**Outcome: B3 closed at 2/12 runs. User-approved decision: stop B3, proceed to Phase C.**

Per the pattern surfaced in 2 runs (intro PASS marginal, multi-H hypothesis FAIL marginal with critic chasing per-paragraph granularity), running the remaining 10 B3 combos would burn ~3h compute confirming a pattern that's already informative. The v1 protocol is judged "structurally improved over v0 but not ground-truth-parity on dense multi-H sections" — acceptable for Phase C, where the accept-with-edit step is designed to close residual granularity gaps via human review.

### Track B v0 → v1.2 protocol changes (durable record)

| Version | Change | File location |
|---|---|---|
| v0 | Initial | `audit-write-skills/plugins/audit-write/agents/audit-pdf-reader.md` |
| v1 | Row-count target raised from 5-8 to ≥12; all-block coverage mandatory; annotation-cell numerics forbidden | same |
| v1.2 | Multi-H hypothesis rule added: target source paragraph count (15-20 rows for 3+ hypotheses); each sub-anchor gets its own row | same |

### Script improvements (durable)

| Script | Change | Reason |
|---|---|---|
| `verify_quote.py` | Soft-hyphen normalization `-\n` → `` | PDF line-breaks split words like "en-\ndowments" |
| `lint_style.py` | UTF-8 stdout via `sys.stdout.reconfigure` | Windows GBK codec choked on em-dash/pilcrow |
| `lint_style.py` | Quote-aware cite skipping | Verbatim source quotes contain real citations; lint should skip these |

### What gets used in Phase C

- v1.2 protocol (above)
- All three script fixes
- Staging file conventions established by B3.1/B3.2 drafts (column schema, self-check log, reviewer notes, accept-log)

### B3 result table (final)

| Run | Section | v_x | Δ | Pass? | Notes |
|---|---|---|---|---|---|
| 1 | 26-KLYY intro | v1 | +5 | ✅ marginal | v0 was -10; protocol fix worked |
| 2 | 26-KLYY hypothesis | v1.1 | -8.2 | ❌ marginal | v1 was -8.2; +3 rows didn't move composite because critic chases per-paragraph |

Pass rate: 1/2 (50%). Not statistically meaningful at n=2; not pursued to n=12.

### Why not continue B3.3-B3.12

1. **Pattern already actionable.** Two sections, two failure modes (intro = clean, multi-H hypothesis = chase). Results section pattern can be inferred from the §4 structure (6 sub-sections, mostly less dense than multi-H §2).
2. **Critic calibration drift observed.** B3.1 v0 vs v1 reruns scored ground truth differently (92 → 87). Adding more runs amplifies critic variance, not signal.
3. **Phase C is where lift actually matters.** B3 was a calibration step. Phase C exemplar additions are what feed Phase F's measured lift on held-out tasks. The 8-12h Phase C effort is the actual ROI.
4. **Cost-benefit asymmetric.** ~3h additional B3 vs ~0h going-straight-to-Phase-C, with Phase C providing the ground truth on whether the v1.2 protocol's drafts are actually useful (accept-rate observable).

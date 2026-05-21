---
status: ROADMAP (living doc)
date: 2026-05-21
owner: Gareth + Claude
scope: audit-write skill suite (post Stage-1 GREEN)
---

# audit-write — long-term optimization roadmap

## Guiding principles (earned from Stage 1)

1. **Enforcement > content.** The decisive Phase F result: enforcing the suite's own
   deterministic gate during drafting moved blind-eval composite from +1.0 to +5.0 on the
   *same* corpus content. Every future round should first ask "can this be a mechanical
   gate?" before "should we distill more papers?".
2. **Measure every change.** Nothing ships on vibes. `scripts/eval_harness.py` is the
   regression: run `gates` before/after a change; a change that doesn't hold or raise the
   held-out scores is reverted. Build the cheap deterministic signal first; reserve the
   Claude critic for periodic calibrated scoring.
3. **Integrity is non-negotiable.** Verbatim-quote verification (`verify_quote.py`) and the
   no-fabrication rule cap everything. DeepSeek's Stage-1 results batch proved a model that
   paraphrases is unusable here regardless of cost; prefer select-by-sentence-ID generation
   (LLM returns IDs, quote looked up from real source) so fabrication is impossible.
4. **Context economy.** Pattern files are loaded into context on every invocation. Smaller,
   denser, retrieval-fed beats large static inlining.

## Status snapshot

- **Stage 1 (corpus deepening 6→22): COMPLETE, GREEN.** intro/hypothesis/results deepened;
  frequencies re-derived over n=22; go/no-go +5.0.
- **Optimization Round 1 (mechanize the gate + eval harness): COMPLETE** (commit b10d053).
  lint_style + check_structure now catch C4/C5/C7 + ordering; harness is re-runnable.
- **Optimization Round 2 (slim + harmonize intro): COMPLETE.** intro_patterns.md 120K→31K
  (74%↓); pilot digest mirrors hypothesis/results; held-out 14-FPW composite **90 ≥ 85**
  baseline (no regression). The regression check surfaced a formal-H reliability gap that
  was closed enforcement-first: a new conditional `check_structure` rule (signed prediction
  must be a displayed H) lifted the gated draft +5 — Phase F's lesson again.

## Capability map (Task 2 lens): 9 functions × 4 tiers

The **Rounds are the execution spine** (dependency-sequenced, enforcement-first). Task 2 names
the *capabilities* those rounds build, grouped by leverage × dependency into four tiers. This
section is the capability overlay; the mapping table below ties the two together. Overall aim:
an end-to-end accounting-writing suite (idea → outline → draft → polish → final), **deepened**
(material/style/citation depth per spoke), **widened** (new sub-field spokes / writing forms),
**hardened** (grammar · anti-AI · traceability gates), and **automated** (PDF intake, retrieval,
eval). audit-write is the highest-quality seed.

| Tier | # | Capability | Type | Status (2026-05-21) | Home (round / track) |
|---|---|---|---|---|---|
| **T1 foundation** | 0 | Workflow protocol ("how to use the whole suite") | cross-cutting | PARTIAL — `progressive_outline.md` (Stage 0–4) + Round-1 gate shipped; needs a consolidated WORKFLOW doc | XC: workflow-doc · R1 |
| | 8 | PDF-reader agent (auto-distillation) | automation multiplier | SHIPPED v1.2, now **private** (`.claude/agents/audit-pdf-reader.md`); feeds every corpus expansion | XC: corpus · R3 · R5 |
| | 1 | More corpus material | content | Stage 1 DONE (audit 6→22); other spokes still on 6-paper template | R3 · XC: measured expansion |
| **T2 depth** | 2 | Writing-style depth (`style_dna` per-subfield register) | content | NOT STARTED | **R6 (new)** |
| | 5 | Literature-referenceable (Zotero MCP into drafting) | retrieval | NOT STARTED; Zotero MCP available | R4 (Stage 1.5) |
| **T3 process** | 3 | More outline types (theory-led / lit-led / null-result / replication …) | structure | NOT STARTED | **R7 (new)** |
| | 7 | Outline management (create / validate / store as artifact) | tooling | NOT STARTED | **R8 (new)** |
| **T4 quality gate** | 6 | Grammar check (LanguageTool / Vale) | surface | NOT STARTED | XC: gate (Q4 hardening) |
| | 4 | Anti-AI-detection (deepen `lint_style` + GPTZero cross-check) | surface | PARTIAL — `lint_style.py` C4 tells exist | XC: gate (Q4 hardening) |

**Dependency law (must hold):** `T1 (0·8·1) → T2 (2·5) → T3 (3·7) → T4 (6·4)`, where T1's corpus (1)
and PDF agent (8) continuously feed the statistical base under T3/T4. Round 2 (context economy) is
the connective tissue that makes T2 retrieval feasible.

## The rounds (sequenced)

### Round 2 — Slim + harmonize the pattern files  ·  NEXT  ·  effort: S–M
**Goal.** Convert `intro_patterns.md` (17 full annotated tables, ~110K chars) to the compact
digest form already used by hypothesis/results, keeping 1–2 anchor exemplars + the canonical
5-block guidance; move the full tables to staging.
**Why.** Every intro invocation currently loads ~110K chars (instruction dilution + cost). The
two-tier inconsistency (intro verbose, hyp/results digest) should be resolved one way.
**Depends on.** Nothing. **Unblocks.** Round 4 (retrieval).
**Success metric.** `eval_harness.py gates` + a fresh critic score on a held-out intro shows
**no composite regression** after slimming; file size down ≥ 50%.
**Detailed plan:** `2026-05-21_intro-slim-harmonize.md`.

### Round 3 — Deepen the remaining sub-skills to n=22  ·  effort: M
**Goal.** Apply the Stage-1 distillation method to `abstract`, `design`, `robustness`,
`audit-referee-response` (still on the 6-paper template corpus).
**Why.** Completes coverage. *Now safer/cheaper* than Stage 1 because the mechanized gate +
harness keep new drafts compliant and measurable, and the QWEN batch script does generation.
**Depends on.** Round 2's digest format (so new sub-skills inherit the lean form).
**Method.** QWEN batch → deterministic verify/repair (`audit_draft_quotes.py` /
`repair_draft_quotes.py`) → digest integration → add a Step-3 mechanical gate to each
SKILL.md → harness regression. Each sub-skill also needs its C5 structural check added to
`check_structure.py` (design: identification-machinery-deferred already exists; add abstract
zero-magnitude, robustness battery-completeness).
**Success metric.** Per sub-skill held-out task, composite ≥ its baseline, integrity PASS.

### Round 4 — Stage 1.5: runtime retrieval  ·  effort: L
**Goal.** Retrieve the top-k relevant exemplars + move/frequency guidance at invocation
instead of statically inlining the whole bank.
**Why.** Scales past ~22 papers; the static pattern files don't.
**Depends on.** Round 2 (lean digests + staging-file exemplar store).
**Carry forward (MUST).** The mandatory mechanical gate (Round 1) stays — retrieval improves
content fit, the gate ensures compliance; both are needed.
**Open design.** Zotero MCP semantic search vs a committed local embedding store; retrieval
granularity (whole-paper vs per-move rows); preserving the verify_quote chain on dynamically
retrieved exemplars. **Scoping:** `2026-05-21_stage1.5_scoping.md`.

### Round 5 — Stage 2: `disclosure-write` spoke  ·  effort: L
**Goal.** Replicate the validated architecture for disclosure research (MD&A / 10-K /
voluntary disclosure / earnings calls / ESG).
**Why.** The architecture is corpus-agnostic; first proof it transfers.
**Depends on.** Ideally Round 4 (so the disclosure corpus need not be statically inlined),
but can run in parallel. **Scoping:** `2026-05-21_stage2_scoping.md`.

### Round 6 — `style_dna` v2: per-subfield register depth  ·  effort: M  ·  [T2 / func 2]
**Goal.** Deepen `style_dna.md` from a single audit register into a calibrated, per-subfield
register layer (verb whitelist/blacklist, hedging vocabulary, magnitude idiom) re-derived over
the n=22 corpus and ready to fork per spoke (audit and disclosure differ).
**Why.** Style is currently one-size; the n=22 corpus now supports subfield-specific calibration.
**Depends on.** R3 (deepened corpus); ideally R4 (retrieval can serve register exemplars).
**Method.** Frequency-derive register markers from the corpus; add a "register profile" block per
subfield to `style_dna.md`; extend `lint_style.py` with any newly mechanizable marker; harness
regression.
**Success metric.** Held-out drafts: composite ≥ baseline, register-marker lint clean, no regression.

### Round 7 — outline-type template library  ·  effort: M  ·  [T3 / func 3]
**Goal.** Add named outline templates beyond the single default per section — e.g. theory-led vs
lit-led intro, null-result results, replication/extension, multi-H pair-prediction — selectable in
the progressive-outline ratchet (Stage 1).
**Why.** Different papers need different skeletons; one canonical arc under-serves the corpus's
documented variant families (the move bank already records RQ-first, off-canon openers, etc.).
**Depends on.** `progressive_outline.md` (shipped), per-section depth (R3), move-bank variants.
**Method.** Encode each template as a selectable skeleton in the ratchet; add a variant-aware mode
to `check_structure.py` so the gate validates against the *chosen* template, not just the default.
**Success metric.** Each template yields a structurally valid skeleton that passes its variant gate.

### Round 8 — outline-management skill  ·  effort: M  ·  [T3 / func 7]
**Goal.** A skill/tool to create, validate, store, and reuse an `outline.md` as a first-class
artifact (versioned, gate-checked, retrievable across sessions) — productizing the Stage-1 skeleton
beyond a transient in-conversation step.
**Why.** Outlines are the highest-leverage edit surface (the suite's core thesis); they deserve
persistence + validation, not just a transient ratchet step.
**Depends on.** R7 (templates to manage), the ratchet, `check_structure.py`.
**Method.** Define the artifact schema; add create/validate/store verbs; wire validation to the
variant-aware structural gate; persist to the working dir alongside `paper-spec.md`.
**Success metric.** Round-trip create → validate (gate) → store → reload → re-validate is lossless.

## Cross-cutting tracks (run alongside)

- **Critic calibration.** The critic showed run-to-run drift (B3: 92→87 on the same ground
  truth) and large drafter variance (±8–10/task). Add few-shot score anchors to `rubric.md`
  and/or have the harness average 2 critic runs per task. Improves measurement quality for
  every round.
- **The deferred ablation.** Stage 1 measured enforcement (v1→v2) but not content-depth in
  isolation. Run old-skill vs new-skill with the drafter method held constant (harness makes
  this one command now) to quantify how much the corpus expansion alone contributed.
- **Corpus expansion.** When a round needs more papers, the natural adds are the 8 unmarked
  2023–2026 CAR/TAR audit papers (CAMs, auditor distraction, audit technology) + a genuine
  2025/2026 Zotero-only paper — see `corpus_inventory/audit_papers_to_curate.md`. Do this
  *inside* a round (with the gate + harness), never as an unmeasured bulk add.
- **Mechanize even more of the gate.** Remaining critic checks that are still judgment-only:
  C6 magnitude-form correctness, contribution-formula variety, journal-specific roadmap rule.
  Each that becomes deterministic is a permanent compliance win.
- **T4 quality-gate hardening [func 6 grammar · func 4 anti-AI].** Two surface gates that run
  alongside `lint_style.py`, not after it: (a) **grammar** — integrate LanguageTool / Vale as an
  advisory pass; (b) **anti-AI** — deepen `lint_style.py`'s AI-tell detectors and add an optional
  GPTZero-class cross-check. Both feed into `audit-write-critic`. Incremental wins anytime; the
  dedicated push (external-tool integration) is the Q4 hardening milestone. Keep them advisory —
  never let a grammar tool rewrite calibrated DeFond register.
- **Workflow doc consolidation [func 0].** `progressive_outline.md` + the Round-1 gate already
  encode the protocol; consolidate them into one discoverable WORKFLOW doc ("how to use the whole
  suite, end to end") so the spokes stop re-stating it. Light, high-leverage; do early (Q1–Q2).

## Round ↔ function ↔ tier ↔ quarter (bidirectional map)

| Round / track | Capability (Task 2 #) | Tier | Target quarter | Status |
|---|---|---|---|---|
| R1 mechanize gate + harness | enables 4 & 6 mechanization | T1/T4 | Q1 | DONE (b10d053) |
| R2 slim/harmonize intro | context economy (enables 5) | T1 | Q1 | NEXT |
| R3 deepen abstract/design/robustness/referee | 1 more corpus | T1 | Q2 | planned |
| R4 Stage 1.5 retrieval | 5 lit-referenceable | T2 | Q2–Q3 | scoped |
| R6 `style_dna` v2 | 2 style depth | T2 | Q2 | new |
| R5 disclosure-write spoke | 拓宽 (new spoke) | — | Q3 | scoped |
| R7 outline-type library | 3 outline types | T3 | Q3 | new |
| R8 outline-management skill | 7 outline mgmt | T3 | Q4 | new |
| XC gate hardening | 4 anti-AI · 6 grammar | T4 | Q4 (incremental anytime) | new |
| XC workflow doc | 0 workflow | T1 | Q1–Q2 | partial |
| XC corpus + PDF agent | 1 · 8 | T1 | anytime | shipped/ongoing |

## Quarterly targets (Task 2 calendar, reconciled — targets, not hard gates)

- **Q1 (now):** R1 ✓ · Stage 1 ✓ (func 1) · PDF agent v1 ✓ (func 8) · workflow seed ✓ (func 0).
  **Remaining: R2 (intro slim).**
- **Q2 — depth + retrieval [T2]:** R3 (finish corpus depth) · R6 (style v2) · start R4 (retrieval).
- **Q3 — widen + outline templates [拓宽 + T3]:** finish R4 · R5 (disclosure spoke) · R7 (outline types).
- **Q4 — process + quality gates [T3 + T4]:** R8 (outline mgmt) · gate hardening (grammar + anti-AI
  into `audit-write-critic`).

### Two ordering tensions, resolved
1. **Retrieval (Q2) vs deepen-rest (R3):** no real conflict — R3 and R4 both land in Q2; R4 depends
   on R2's lean digests and R3 also depends on R2, so `R2 → {R3, R4}` holds and matches the Q2
   "depth + retrieval" theme.
2. **Disclosure-spoke timing:** Task 2 places it Q3; the prose roadmap framed it "last (R5)".
   Resolved to **Q3, after retrieval (R4) exists** so the disclosure corpus need not be statically
   inlined. Dependency order governs; quarters are targets.

## Sequencing summary

```
Round 1 (done)
  → Round 2 (next, slim/harmonize)            [T1 context economy]
      → Round 3 (deepen rest)  ─┐             [T1 corpus depth]
      → Round 6 (style v2)      ├→ Round 4 (retrieval)        [T2]
                                │     → Round 5 (disclosure spoke)   [拓宽]
                                │     → Round 7 (outline types)      [T3]
                                │         → Round 8 (outline mgmt)   [T3]
cross-cutting (anytime): gate hardening [T4: anti-AI · grammar] · critic calibration ·
                         ablation · measured corpus expansion · workflow doc
```

## Decision log
- 2026-05-21: enforcement-first principle adopted after Phase F.
- 2026-05-21: Round 1 shipped (b10d053). Round 2 selected as next.
- 2026-05-21: integrated Task 2 (9-function × 4-tier × quarterly) as a capability overlay; Rounds
  remain the execution spine (per Gareth). Added R6 (style v2), R7 (outline types), R8 (outline
  mgmt); T4 gates (grammar/anti-AI) fold into the gate-hardening cross-cutting track with a Q4
  milestone; func 0 (workflow) and func 8 (PDF agent) tracked as T1 foundations.
- 2026-05-21: resolved disclosure-spoke timing to Q3-after-R4 (dependency governs over calendar).
- 2026-05-21: audit-pdf-reader (func 8) moved out of the published plugin to private
  `.claude/agents/`; remains the corpus-distillation multiplier for R3/R5.

---
status: PLAN (approved-to-write; execute later)
date: 2026-05-22
owner: Gareth + Claude
scope: audit-write — next three optimization rounds (review system · style depth · knowledge base)
supersedes_sequence: re-prioritizes the prior roadmap (retrieval / disclosure / outline-type rounds move later)
---

# Next-step plan — Round 4 (review) → Round 5 (style depth) → Round 6 (knowledge base)

## Why these three, in this order

Three gaps surfaced after R3 (Gareth, 2026-05-22):
1. **DeFond style learning is thin** — `style_dna.md` is distilled from **7** papers; `audit_writing_corpus/` holds **29** PDFs (only 8 cleaned), many unused DeFond originals. Several move counts are still `k/6 (template)`.
2. **No audit-research knowledge base** — the only domain bank is `audit_quality_framework.md` (the DeFond-Zhang AQ taxonomy). No structured reference for constructs/measures, institutions, identification strategies, or a literature map.
3. **Review system is thin + noisy** — `audit-write-critic.md` is 44 lines; documented critic drift (92→87 on identical input), drafter variance (±8–10), and a **critic-vs-gate calibration gap** (R3: the critic flagged 3 em-dashes as C4=N while the mechanical C4 threshold is ~5/section).

**Sequencing decision (Gareth):** review system **first** — it is the measurement instrument; until it is reliable we cannot trust the held-out gains from style/knowledge work (the suite's "measure every change" principle). Then style depth (mine all 29), then a static knowledge-base bank.

This re-prioritizes the earlier roadmap: the prior R4 (Stage 1.5 retrieval), R5 (disclosure spoke), R7/R8 (outline types/management) shift to *after* these three. R6 (style v2) is absorbed/expanded into Round 5 here.

---

## Round 4 — Harden the review / evaluation system  ·  effort: M  ·  [#3, T4 + critic-calibration]

**Goal.** Make the critic + eval harness a *reliable, single-source* measurement instrument: critic and mechanical gate must agree, run-to-run variance must drop, and more of the rubric must be mechanized so the critic judges less.

**Problem recap.** Critic↔gate disagreement (em-dash C4); run-to-run critic drift; thin critic doc; many rubric checks still judgment-only.

**Steps.**
1. **Single source of truth for the C-checklist.** Update `agents/audit-write-critic.md` + `rubric.md` so that for every C-item with a mechanical detector (`check_structure.py`), the critic **ingests the script's Y/N/NA verdict** rather than re-judging with its own threshold. The critic only judges what is *not* mechanized. This closes the em-dash-style splits. (The critic prompt should instruct: "run/ья read the check_structure output first; treat C1–C6 mechanical verdicts as authoritative; do not override an em-dash/threshold call the detector already made.")
2. **Calibration anchors in `rubric.md`.** Add 2–3 *anchor scores* per dimension (a short Weak / Solid / Excellent exemplar snippet with the band it earns) so the critic bands consistently across runs. Optionally one or two full anchor drafts with consensus composites.
3. **Multi-run averaging in `eval_harness.py`.** Add a mode that emits K critic prompts per task (default K=2) and averages the composites in `report`, with the spread reported. Reduces the run-to-run drift's effect on the measured number.
4. **Mechanize more judgment-only checks** (the roadmap's "mechanize even more of the gate"): pick the highest-value still-manual items — e.g. C6 magnitude-form correctness (pp / % of base / SD shapes), contribution-count (3–4 numbered), journal-roadmap rule (TAR keep / JAE-JAR drop). Each one moved into `check_structure.py` shrinks the critic's judgment surface (less variance) and adds a golden test.
5. **A calibration test set + variance measurement.** Build a small fixed set of drafts with agreed "consensus" composites (reuse the R2/R3 held-out drafts: 14-FPW intro/design/abstract, 14-FPW robustness). Re-run the critic K times on each; record the variance. This is the *measurement of the measurement instrument* and the round's go/no-go evidence.
6. **Strengthen `audit-write-critic.md`** (44 → fuller): explicit deterministic-first procedure (run gates → ingest C-line → band only non-mechanized dimensions → emit canonical Score block), the anchored bands inline, and the fixed output format.

**Success metric.** (a) critic↔gate agreement on mechanized C-items = **100%** (no em-dash-style splits); (b) critic re-score **variance on a fixed draft ≤ ~3 pts** (down from the observed ~5–8); (c) **≥1** previously-manual check newly mechanized with a golden test; (d) golden tests still green; (e) the calibration set + its variance numbers are committed as the baseline for future rounds.

**Depends on.** Nothing (uses existing held-out drafts). **Unblocks.** Trustworthy measurement for Rounds 5 & 6.

---

## Round 5 — Deepen the DeFond style register from the full 29-paper corpus  ·  effort: M–L  ·  [#1, expands old R6]

**Goal.** Rebuild `style_dna.md` (and re-derive the stale `k/6` move counts) on the **full `audit_writing_corpus` (29 papers)** instead of 7, so the register/voice rests on a broad, traceable evidence base.

**Steps.**
1. **Clean the corpus.** `preclean_corpus.py` over all 29 `audit_writing_corpus/*.pdf` → `.clean.txt` (only 8 exist now). Verify extraction.
2. **Mine the register (not just moves).** Extend the `--section`-general pipeline (or a focused script) to harvest, across the 29: finding/hedging verbs, magnitude idiom, opener types, contribution formulas, banned/AI-tell incidence. Tabulate frequencies with per-paper provenance.
3. **`style_dna.md` v2.** Re-derive the verb whitelist/blacklist, hedging vocabulary, and register rules over the larger base; cite **N≫7** papers; where the register differs by era/journal/author, note it (a per-profile register layer, dovetailing with `journal_profile_bank.md`).
4. **Re-code the stale move counts.** The corpus_manifest flags counts still written `k/6 (template)`; re-derive them over the larger coded set and update `move_presence_matrix.md` + the pattern files (keep provenance honest: `k/N`).
5. **Optionally extend `lint_style.py`** with any newly robust verb/idiom signal the larger corpus reveals; add golden tests.
6. **Held-out eval** (using the Round-4-hardened critic): re-draft a held-out section with style_dna v2; accept iff register-dimension band ≥ baseline and no composite regression.

**Success metric.** `style_dna.md` provenance ≥ ~20 papers; stale `k/6` claims re-derived to `k/N`; held-out register band holds/improves under the (now reliable) critic; lint clean.

**Depends on.** Round 4 (so the held-out eval is trustworthy). **Note.** This is the natural place to also fold in the 16 pilot papers' register, unifying the style evidence base.

---

## Round 6 — Build a static audit-research knowledge-base bank  ·  effort: L  ·  [#2, NEW]

**Goal.** Give the suite a domain-knowledge spine: a small set of **static reference banks** the sub-skills consult, so a draft can use correct construct definitions, measures, institutional facts, and literature anchors without fabrication.

**Form (Gareth's choice).** Static shared banks now; a Zotero-MCP retrieval layer is a *later* extension (depends on the retrieval round).

**Proposed banks (distilled from the 29 corpus + 22 pilot + existing framework).**
1. `constructs_and_measures.md` — the audit-quality DV/IV zoo: discretionary-accruals models, going-concern opinions, restatements, audit fees, PCAOB Part-I findings, audit-quality proxies — each with a one-line definition, how it is measured, the standard caveat, and the canonical source. (Extends `audit_quality_framework.md`, which stays as the taxonomy.)
2. `institutional_settings.md` — PCAOB inspection regime, mandatory audit-firm/partner rotation, the China engagement-partner signatory regime, Big-N structure, key regulatory shocks used as identification (SOX, AS-numbers, deregulations). Facts + dates + the papers that exploit them.
3. `identification_catalog.md` — consolidate/extend the identification moves already split across `null_and_identification_protocols.md` and design §5: rotation, regulatory-shock DiD, IV, falsification/placebo, entropy balancing, FE escalation — with when-to-use and the corpus exemplar.
4. `literature_map.md` — per subfield (audit quality, partner traits, fees, competition, AI/technology, China), the few anchor papers and what each established — so contribution statements can name a *real* literature (currently `[AUTHOR:]` slots only).

**Integrity discipline (critical).** Every knowledge entry must be **traceable to a source paper** (corpus code or citation); the integrity gate forbids inventing measures/facts/citations. The knowledge base is *curated and reviewed*, not model-confabulated — generate candidates from the corpus, then human/critic review before commit. Substantive citations in *user drafts* remain `[AUTHOR:]` slots; the knowledge base informs the agent, it does not license hard cites.

**Wiring.** Sub-skills reference the relevant bank (design → constructs/measures + identification; intro/hypothesis → literature map + institutions; results → measures). Lazy-load per the context-economy policy.

**Success metric.** A held-out draft uses correct construct definitions / institutional facts with zero fabrication; sub-skills cite the banks; `check_links` clean; the banks are corpus-traceable.

**Depends on.** Rounds 4 (measurement) & 5 (corpus already cleaned). Big effort — may be split into per-bank sub-deliverables.

---

## Cross-cutting / carried forward
- **Reconcile `audit_draft_quotes.py` to prefer `.clean.txt`** (R3 tooling-drift finding) — fold into Round 4 (it's review-tooling hygiene).
- **`audit-referee-response` deepening** (from the O1–O8 objection bank) — still its own future round.
- **Prior roadmap rounds** (Stage 1.5 retrieval, disclosure-write spoke, outline-type library, outline-management) — deferred to after Rounds 4–6; retrieval (old R4) becomes the natural Round 7 and would also upgrade the Round-6 knowledge base from static to retrieval-fed.

## Sequencing
```
Round 4 (review hardening)  ──►  Round 5 (style depth, 29-corpus)  ──►  Round 6 (knowledge banks)
   measurement instrument         trustworthy held-out eval             domain spine
later: retrieval (old R4) → disclosure spoke → outline rounds → referee-response deepening
```

## Decision log
- 2026-05-22: three new gaps raised (style depth / knowledge base / review robustness); sequenced review-first per measure-everything; knowledge base = static banks to start; style corpus = all 29 `audit_writing_corpus` papers. Execute later.

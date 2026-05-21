# R3 abstract — deepening (2026-05-22)

## Generation
- 16/16 abstracts extracted (new pre-intro extractor) + generated (qwen3.6-plus, --min-quotes 6).
- repair + drop (--min-keep=5): all 16 quote-clean (7-14 quotes each).

## Deepening delivered
- abstract_patterns.md: 16-paper Stage-1 pilot digest (move-count 3-6 variants; opener variants:
  setup/RQ/finding-forward/shock; M2-tension often folded/absent; single-author "I"; null pairing;
  zero-effect-number rule with prevalence/sample-window exceptions noted).
- abstract SKILL.md: Step-3 deterministic-gate section added (zero-magnitude C5 already existed + tested).

## Held-out validation (14-FPW abstract)
- Pre-deepen baseline: **90** (skill already near-ceiling; 5-move + zero-mag well-encoded).
- Post-deepen, CLEAN A/B (baseline-identical prompt): **92** (+2, no regression). Accept (>=90).
- Note: a first regression attempt scored 85 but used an extra "theory-level closer" prompt nudge
  that backfired on C7 (no named literature) — a PROMPT artifact, not a digest regression. Re-run
  with the baseline-identical prompt isolated the digest effect -> 92. Lesson: keep pre/post prompts
  identical; only the file (digest) may differ.

# Plan: Polish interview script (bilingual, tiered)

**Status:** APPROVED — 2026-05-17

## Goal

Improve `academic-latex-slides` skill performance by rewriting the interview
protocol from an abstract field spec into a bilingual, tiered, inference-first
interview script. Three targeted gains: extract more accurately, lower friction,
more natural phrasing.

## Approach

Three performance defects → three changes:

1. **Extraction accuracy** — add an Inference pass (read user message + attached
   materials first, echo back extracted structure/results/citations, only ask
   gaps); replace vague questions with specificity-forcing ones.
2. **Friction** — three tiers: Tier 1 blocking (template/archetype/language/core
   message — cannot infer), Tier 2 shaping (audience/timing/material readiness —
   defaulted), Tier 3 adaptive deep-dive (gated on material sufficiency); add a
   "use defaults" escape hatch that still passes the outline approval gate.
3. **Phrasing** — each question gets one natural EN + ZH opener; interview in the
   user's language; Tier 1+2 batched as one human-sounding consultant message.

Preserved: template-selection rule (never infer template), academic-integrity
red line (never fabricate), outline approval gate (scripted into the closing),
the sparse-material path (folded into tier logic), all 9 core fields covered.

## Files to modify (edit canonical → sync mirror)

1. `skills/academic-latex-slides/references/interview-protocol.md` — full rewrite.
2. `skills/academic-latex-slides/SKILL.md` — Phase 1 wording (language + infer
   first), keep lean.
3. `skills/academic-latex-slides/agents/openai.yaml` — default_prompt invites
   topic+materials up front; short_description aligned.
4. Run `python scripts/sync_distributions.py` to mirror into `plugins/`.

## Verification

- Byte-identical diff between canonical and plugin mirror after sync.
- Self-check: 9 core fields still covered, integrity rule intact, approval gate
  intact, SKILL.md reference filenames still valid.

## Out of scope

- No separate good/bad transcript doc (deliverable form chosen = bilingual
  script; inline a one-line natural-vs-form-filling contrast instead).
- No change to `scaffold.py`.
- No git commit (canonical `skills/` currently untracked — flag at wrap-up).

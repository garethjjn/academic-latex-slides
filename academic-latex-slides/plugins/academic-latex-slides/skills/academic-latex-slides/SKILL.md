---
name: academic-latex-slides
description: Create compile-ready academic LaTeX Beamer projects for lectures and research talks. Use when the user wants AI-generated academic slides in MSU, SJTU, or CityU visual styles and needs the agent to interview them thoroughly before producing a modular LaTeX deck.
---

# Academic LaTeX Slides

Create modular academic Beamer projects only after understanding the talk.

## Non-negotiable rules

1. Support only new-slide generation from scratch.
2. Interview before generating. Never jump straight from a vague request to `.tex` files.
3. Use one of three visual variants only: `MSU`, `SJTU`, or `CityU`.
4. Use one of two deck archetypes only: `lecture` or `research talk`.
5. If the user lacks content, create structure and placeholders; do **not** invent results, citations, data, or claims.
6. Present a requirements summary, slide-by-slide outline, and missing-materials list before generation.
7. Wait for explicit outline approval before creating the project.
8. Generate a modular project with `main.tex`, `sections/`, `figures/`, `references.bib`, and the selected template assets.
9. Target `latexmk -xelatex` for all outputs.

## Workflow

### Phase 1 — Interview

Read [references/interview-protocol.md](references/interview-protocol.md).

- Ask all required core questions.
- Ask the archetype-specific follow-ups for `lecture` or `research talk`.
- Confirm whether the deck needs formulas, figures, references, and appendix material.
- If the user has only a topic, keep the workflow moving but mark unknown material explicitly.

### Phase 2 — Outline gate

Read [references/deck-blueprints.md](references/deck-blueprints.md).

- Convert the interview into:
  1. requirements summary
  2. slide-by-slide outline
  3. missing-materials list
- Stop and wait for explicit user approval.
- Revise the outline if the user corrects scope, pacing, or emphasis.

### Phase 3 — Generate

Read:

- [references/templates.md](references/templates.md)
- [references/latex-generation.md](references/latex-generation.md)

Then:

1. Run `scripts/scaffold.py` with the chosen template, deck type, language, and metadata.
2. Replace the starter section files with the approved content plan.
3. Reserve explicit section slots for formulas, figures, references, and appendix material whenever the approved outline calls for them.
4. Add those academic components only when supported by the interview or user-supplied materials.
5. Keep claims faithful to supplied evidence.
6. Return the project path and the compile command.

## Resource map

- `references/interview-protocol.md` — mandatory questions, adaptive follow-ups, approval gate
- `references/deck-blueprints.md` — lecture and research-talk narrative defaults
- `references/templates.md` — MSU, SJTU, CityU selection and bundled assets
- `references/latex-generation.md` — project structure, slide-writing rules, compile conventions
- `assets/templates/` — copyable template assets
- `scripts/scaffold.py` — deterministic starter-project generator

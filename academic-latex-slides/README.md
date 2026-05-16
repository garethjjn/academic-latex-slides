# Academic LaTeX Slides

A Claude Code skill/plugin for generating academic Beamer projects after a deliberate pre-build interview.

## What it does

`academic-latex-slides` creates modular, compile-ready LaTeX slide projects for two academic contexts:

- `lecture`
- `research talk`

It ships with three visual variants that share the same workflow and content logic:

- `MSU`
- `SJTU`
- `CityU`

The skill does **not** fabricate academic content to fill space. If the user only has a topic, it creates a structure, placeholders, and a missing-materials list instead of inventing results, citations, or data.

## Core workflow

1. Interview the user before writing slides.
2. Collect the required metadata, audience, duration, page target, material readiness, and academic-component needs.
3. Ask adaptive follow-up questions for `lecture` or `research talk`.
4. Present a requirements summary, slide-by-slide outline, and missing-materials list.
5. Wait for explicit outline approval.
6. Generate a modular Beamer project:

```text
main.tex
sections/
figures/
references.bib
```

## Plugin layout

```text
.claude-plugin/marketplace.json
plugins/academic-latex-slides/
  .claude-plugin/plugin.json
  skills/academic-latex-slides/
    SKILL.md
    references/
    assets/templates/
    scripts/scaffold.py
```

## Template assets

- `MSU`: simplified Michigan State-inspired academic deck
- `SJTU`: minimal runtime subset of the SJTU Beamer theme
- `CityU`: simplified City University of Hong Kong-inspired academic deck

All variants target `latexmk -xelatex` so Chinese and English decks can share one build path.

## Scaffold helper

Generate a starter project:

```bash
python plugins/academic-latex-slides/skills/academic-latex-slides/scripts/scaffold.py ^
  --template sjtu ^
  --deck-type lecture ^
  --language zh ^
  --title "资产定价导论" ^
  --subtitle "Lecture 1" ^
  --author "Your Name" ^
  --institute "Your Institute" ^
  --date "2026-05-17" ^
  output/slides
```

Compile the result with:

```bash
latexmk -xelatex main.tex
```

## Scope

Version 1 is intentionally narrow:

- from-scratch generation only
- no PPT conversion
- no HTML presentation output
- no automatic PDF export

The narrowness is deliberate: academic decks become better when the agent spends its energy on understanding the talk before it writes.

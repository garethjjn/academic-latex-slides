# Academic LaTeX Slides

A portable academic-slide skill that can be installed in **Codex** as a standalone skill or distributed to **Claude Code** as a plugin.

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

## Portable layout

```text
skills/academic-latex-slides/              # canonical skill source for Codex/manual install
.claude-plugin/marketplace.json             # Claude Code marketplace metadata
plugins/academic-latex-slides/
  .claude-plugin/plugin.json
  skills/academic-latex-slides/             # synced mirror for Claude Code plugin install
scripts/
  sync_distributions.py
  build_portable_packages.py
```

Edit the canonical skill under `skills/academic-latex-slides/`, then run the sync script before packaging or installing the Claude Code plugin mirror.

## Template assets

- `MSU`: simplified Michigan State-inspired academic deck
- `SJTU`: minimal runtime subset of the SJTU Beamer theme
- `CityU`: simplified City University of Hong Kong-inspired academic deck

All variants target `latexmk -xelatex` so Chinese and English decks can share one build path.

## Install on Codex

### Manual copy

Copy the canonical skill folder to the target machine's Codex skill directory:

```bash
# macOS / Linux
cp -R skills/academic-latex-slides ~/.codex/skills/
```

```powershell
# Windows PowerShell
Copy-Item -Recurse skills\academic-latex-slides $HOME\.codex\skills\
```

Then start a new Codex session and invoke it as:

```text
Use $academic-latex-slides to create a research-talk deck.
```

### Portable ZIP

Build a ready-to-transfer ZIP:

```bash
python scripts/build_portable_packages.py
```

The script writes:

- `dist/academic-latex-slides-codex-skill.zip`
- `dist/academic-latex-slides-claude-plugin.zip`

Extract the Codex ZIP so that the final folder on the target machine is:

```text
~/.codex/skills/academic-latex-slides/
```

## Install on Claude Code

On the target machine, keep or extract this repository, then from Claude Code run:

```text
/plugin marketplace add /absolute/path/to/academic-latex-slides
/plugin install academic-latex-slides@academic-latex-slides
```

If you transfer only the plugin ZIP, extract it first, then point `marketplace add` at the extracted repository folder.

## Maintenance commands

```bash
# Copy the canonical skill into the Claude Code plugin mirror
python scripts/sync_distributions.py

# Build both portable ZIP packages
python scripts/build_portable_packages.py
```

Run `sync_distributions.py` after editing the canonical skill and before sharing the project with another device.

## Scaffold helper

Generate a starter project:

```bash
python skills/academic-latex-slides/scripts/scaffold.py ^
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

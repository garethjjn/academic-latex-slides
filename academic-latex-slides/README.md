# Academic LaTeX Slides

> An interview-first agent skill that turns a talk into a compile-ready,
> modular LaTeX Beamer project — without fabricating academic content.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Engine: XeLaTeX](https://img.shields.io/badge/engine-XeLaTeX-blue.svg)](#requirements)
[![Scaffold: Python 3.8+](https://img.shields.io/badge/scaffold-Python%203.8%2B-3776ab.svg)](#scaffold-helper-standalone)
[![Hosts: Claude Code · Codex](https://img.shields.io/badge/hosts-Claude%20Code%20%C2%B7%20Codex-8a3ffc.svg)](#installation)

`academic-latex-slides` is a portable skill that can be installed in **Codex**
as a standalone skill or distributed to **Claude Code** as a plugin. It does one
thing well: it **interviews you before it writes anything**, then generates a
modular Beamer deck you can compile immediately.

Its defining rule: **it never invents results, citations, data, or claims to
fill space.** If you only have a topic, it produces a structure, placeholders,
and an explicit missing-materials list — not a confident, wrong deck.

---

## Table of Contents

- [Features](#features)
- [Why interview-first](#why-interview-first)
- [Requirements](#requirements)
- [Repository layout](#repository-layout)
- [Installation](#installation)
  - [Claude Code](#claude-code)
  - [Codex](#codex)
  - [Building portable ZIPs](#building-portable-zips)
- [Usage](#usage)
  - [The workflow](#the-workflow)
  - [End-to-end walkthrough](#end-to-end-walkthrough)
  - [Generated project structure](#generated-project-structure)
  - [Compiling the deck](#compiling-the-deck)
- [Scaffold helper (standalone)](#scaffold-helper-standalone)
- [Template variants](#template-variants)
- [Development & maintenance](#development--maintenance)
- [Scope](#scope)
- [Acknowledgements](#acknowledgements)
- [License](#license)

---

## Features

- **Two deck archetypes** — `lecture` and `research talk`, each with its own
  narrative spine.
- **Four visual variants** — `MSU`, `SJTU`, `CityU`, and `Generic`
  (institution-neutral, no branding). Same content logic; choose by visual
  identity only.
- **Bilingual interview** — the agent interviews you in your language
  (Chinese in → Chinese out) using tiered, scripted questions.
- **Inference-first** — it reads your attached materials and existing notes,
  echoes back what it extracted, and asks only the gaps.
- **Low-friction** — blocking questions vs. defaulted shaping questions, plus a
  "use defaults" escape hatch (the outline approval gate always still applies).
- **No fabrication** — missing evidence becomes a `TODO` placeholder and a
  missing-materials line, never an invented number or citation.
- **Modular output** — `main.tex` + `sections/` + `figures/` + `references.bib`.
- **One build path** — every variant targets `latexmk -xelatex`, so Chinese and
  English decks compile the same way.
- **Deterministic scaffold** — a dependency-free Python script generates the
  starter project; the agent then fills in approved content.

## Why interview-first

Academic decks get better when the agent spends its effort understanding the
talk before it writes LaTeX. The skill therefore enforces three gates:

1. **Interview** before generating — never jump from a vague request to `.tex`.
2. **Outline approval** — a requirements summary, slide-by-slide outline, and
   missing-materials list are presented, and generation waits for your explicit
   approval.
3. **Academic integrity** — empirical findings, citations, data descriptions,
   theorem statements, and numerical magnitudes are never invented.

## Requirements

| Purpose | Requirement |
| --- | --- |
| Run the skill | An agent host: **Claude Code** (plugin) or **Codex** (skill) |
| Compile decks | A LaTeX distribution with **XeLaTeX** — TeX Live (full scheme recommended) or MiKTeX |
| Bibliography | **`biber`** (ships with TeX Live; latexmk invokes it automatically) |
| Build automation | **`latexmk`** (recommended) |
| Scaffold script | **Python 3.8+** (standard library only — no `pip install`) |

> **Note on fonts.** All four templates use the `ctexbeamer` document class, so
> *even English-only decks* compile through XeLaTeX with Chinese font support
> loaded. A full TeX Live install (which bundles the Fandol CJK fonts and the
> `ctex`/`biblatex` packages) is the friction-free choice. On MiKTeX, allow
> on-the-fly package installation on first compile.

## Repository layout

```text
academic-latex-slides/
├── skills/academic-latex-slides/        # canonical skill source — EDIT HERE
│   ├── SKILL.md
│   ├── references/                      # interview protocol, blueprints, rules
│   ├── assets/templates/                # MSU / SJTU / CityU / Generic template assets
│   ├── scripts/scaffold.py              # deterministic starter generator
│   └── agents/openai.yaml               # Codex interface metadata
├── plugins/academic-latex-slides/       # synced mirror for the Claude Code plugin
│   ├── .claude-plugin/plugin.json
│   └── skills/academic-latex-slides/    # generated copy — DO NOT edit by hand
├── .claude-plugin/marketplace.json      # Claude Code marketplace metadata
├── scripts/
│   ├── sync_distributions.py            # copy canonical → plugin mirror
│   └── build_portable_packages.py       # build transfer ZIPs
├── README.md
└── LICENSE
```

The canonical source lives under `skills/academic-latex-slides/`. The
`plugins/` tree is a **generated mirror** — always edit the canonical source and
run the sync script (see [Development & maintenance](#development--maintenance)).

## Installation

### Claude Code

From a machine that has this repository (cloned or extracted), run inside
Claude Code:

```text
/plugin marketplace add /absolute/path/to/academic-latex-slides
/plugin install academic-latex-slides@academic-latex-slides
```

If you transferred only the plugin ZIP, extract it first and point
`marketplace add` at the extracted repository folder.

### Codex

**Manual copy** — copy the canonical skill folder into Codex's skill directory:

```bash
# macOS / Linux
cp -R skills/academic-latex-slides ~/.codex/skills/
```

```powershell
# Windows PowerShell
Copy-Item -Recurse skills\academic-latex-slides $HOME\.codex\skills\
```

Then start a new Codex session and invoke it:

```text
Use $academic-latex-slides to create a research-talk deck.
```

### Building portable ZIPs

To transfer the skill to another machine without git:

```bash
python scripts/build_portable_packages.py
```

This writes:

- `dist/academic-latex-slides-codex-skill.zip`
- `dist/academic-latex-slides-claude-plugin.zip`

Extract the Codex ZIP so the final folder on the target machine is
`~/.codex/skills/academic-latex-slides/`. Extract the Claude ZIP and point
`/plugin marketplace add` at the extracted folder.

## Usage

### The workflow

The agent always runs three phases:

| Phase | What happens |
| --- | --- |
| **1. Interview** | Inference pass on your materials, then tiered bilingual questions; gated archetype follow-ups. |
| **2. Outline gate** | Requirements summary + slide-by-slide outline + missing-materials list; **stops and waits for your approval**. |
| **3. Generate** | Runs the scaffold, replaces starter sections with approved content, returns the project path and compile command. |

### End-to-end walkthrough

A realistic session, from request to compiled PDF.

**1 — You ask.** Give the agent your topic and any materials up front:

```text
Use $academic-latex-slides. I'm giving a 20-minute research talk on
"Audit partner rotation and earnings quality". CityU style, slides in English.
Here are my notes and the regression table. (attaches notes.md, table1.tex)
```

**2 — The agent interviews you** (inference pass first, then only the gaps):

```text
I read your notes and Table 1. Here's what I extracted:
  • RQ: does mandatory partner rotation change discretionary accruals?
  • Sample: 2008–2020 Chinese listed firms; main coeff ≈ -0.013 (p<0.05)
  • Identification: staggered rotation, firm + year FE

A few things so I build the right deck —
  • If the audience remembers one number, is it the -0.013, or an economic-
    magnitude restatement?
  • What does a skeptical referee attack first — selection, or the FE design?
  • Title / author / institute / date? (placeholders are fine — I'll flag them)
  • I'll assume figures + inline author-year citations (e.g., “Gul, Wu, and
    Yang 2013”) — no separate references slide, no appendix. Right?
```

**3 — The agent presents the outline and waits** (the approval gate):

```text
REQUIREMENTS SUMMARY
  Template: CityU · Archetype: research talk · Language: EN
  Timing: ~20 min → ~13 content slides · Audience: accounting peers (default)

SLIDE-BY-SLIDE OUTLINE
  1 Title   2 Motivation   3 Research question / gap   4 Contribution
  5 Data & sample   6 Identification   7 Main result (Table 1)
  8 Economic magnitude   9 Robustness   10 Heterogeneity   11 Conclusion

MISSING MATERIALS
  • TODO: economic-magnitude restatement of -0.013
  • TODO: robustness table not yet supplied

Here's what I'll build, and what I can't fill without your input.
Reply 'approved' to generate, or correct the scope and I'll revise.
```

**4 — You approve.** The agent runs the scaffold and writes the sections:

```text
approved
```

**5 — The agent generates and hands back:**

```text
Created research-talk project with the cityu template at output/audit-talk
Compile:  cd output/audit-talk && latexmk -xelatex main.tex
```

**6 — You compile:**

```bash
cd output/audit-talk
latexmk -xelatex main.tex
```

Sections backed by your materials are filled; unsupported claims remain as
clearly marked `TODO:` placeholders for you to complete.

### Generated project structure

```text
output/audit-talk/
├── main.tex                 # template-rendered preamble + \input wiring
├── sections/
│   ├── 01_motivation.tex
│   ├── 02_design.tex
│   ├── 03_results.tex
│   ├── 04_conclusion.tex
│   └── 90_appendix.tex      # \appendix stub, used only when requested
├── figures/                 # your figures (empty by default)
├── references.bib           # your bibliography (empty by default)
└── <template assets>        # logos / theme .sty files for the chosen variant
```

### Compiling the deck

```bash
latexmk -xelatex main.tex
```

`latexmk` runs the XeLaTeX passes and invokes `biber` automatically. Without
`latexmk`, compile manually:

```bash
xelatex main.tex
biber main
xelatex main.tex
xelatex main.tex
```

## Scaffold helper (standalone)

The agent runs this for you, but you can also generate a starter project
directly. It is deterministic and has **no third-party dependencies**.

```bash
python skills/academic-latex-slides/scripts/scaffold.py \
  --template sjtu \
  --deck-type lecture \
  --language zh \
  --title "资产定价导论" \
  --subtitle "Lecture 1" \
  --author "Your Name" \
  --institute "Your Institute" \
  --date "2026-05-17" \
  output/slides
```

```powershell
# Windows PowerShell (use backtick for line continuation)
python skills\academic-latex-slides\scripts\scaffold.py `
  --template sjtu --deck-type lecture --language zh `
  --title "资产定价导论" --subtitle "Lecture 1" `
  --author "Your Name" --institute "Your Institute" `
  --date "2026-05-17" output\slides
```

| Argument | Required | Values / notes |
| --- | --- | --- |
| `output_dir` (positional) | yes | target directory |
| `--template` | yes | `msu` · `sjtu` · `cityu` · `generic` |
| `--deck-type` | yes | `lecture` · `research-talk` |
| `--language` | yes | `en` · `zh` (selects starter section language) |
| `--title` | yes | LaTeX-escaped automatically |
| `--subtitle` | no | defaults to empty |
| `--author` | yes | LaTeX-escaped automatically |
| `--institute` | yes | LaTeX-escaped automatically |
| `--date` | yes | free text, e.g. `2026-05-17` |
| `--force` | no | allow writing into a non-empty directory |

Then compile with `latexmk -xelatex main.tex`.

## Template variants

All variants share the same content logic, interview flow, and modular output.
Choose by visual identity only — the agent will not infer the template from
your language, institution, or talk type.

| Variant | Visual character | Good fit | Bundled assets |
| --- | --- | --- | --- |
| **MSU** | Green academic palette, classic Beamer feel | General talks, seminars, internal presentations | `msu.png`, `Logo.png` |
| **SJTU** | Formal institutional theme with a strong cover system | Polished lectures, formal academic events | SJTU theme `.sty` files, `vi/` identity assets |
| **CityU** | Purple academic palette, restrained clean title page | Compact lectures, concise reports, clean seminars | `CityULogo.pdf` |
| **Generic** | Institution-neutral stock Beamer theme, no logo or branded colors | Cross-institution talks, drafts, brand-free decks | none (template only) |

## Development & maintenance

**Always edit the canonical source, then sync the mirror.** The `plugins/` tree
is generated — hand edits there are overwritten.

```bash
# 1. Edit files under skills/academic-latex-slides/

# 2. Copy the canonical skill into the Claude Code plugin mirror
python scripts/sync_distributions.py

# 3. (Optional) build both transfer ZIPs
python scripts/build_portable_packages.py
```

`build_portable_packages.py` runs the sync step first, so the ZIPs always
reflect the canonical source. After a sync, the canonical and mirror trees are
byte-identical.

## Scope

Version 1 is intentionally narrow:

- from-scratch generation only
- no PPT conversion
- no HTML presentation output
- no automatic PDF export

The narrowness is deliberate: academic decks become better when the agent
spends its energy on understanding the talk before it writes.

## Acknowledgements

The SJTU variant bundles a minimal runtime subset of the **SJTU Beamer theme**;
the MSU and CityU variants are simplified academic decks inspired by the visual
identities of Michigan State University and City University of Hong Kong
respectively. These assets are included only to make the generated decks
compile out of the box. The Generic variant carries no institutional identity —
it uses only a stock Beamer theme and ships no bundled assets.

## License

[MIT](LICENSE) © Gareth

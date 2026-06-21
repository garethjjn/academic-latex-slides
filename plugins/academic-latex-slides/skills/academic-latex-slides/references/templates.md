# Template Variants

All variants share the same content logic, interview flow, and modular output structure. Choose by visual identity only.

## MSU

- Visual character: green academic palette, classic Beamer feel
- Good fit: general academic talks, seminars, internal presentations
- Bundled runtime assets:
  - `msu.png`
  - `Logo.png`

## SJTU

- Visual character: formal institutional theme with stronger cover system
- Good fit: polished lectures, university talks, formal academic events
- Bundled runtime assets:
  - SJTU theme `.sty` files (upstream `sjtubeamer` v3.0.1, untouched)
  - `sjtuaccents.sty` — official SJTU 2022 VIS accent palette (plugin add-on)
  - `vi/` visual identity assets, including six optional campus cover photos
    `vi/sjtu-vi-campus-1.jpg` … `sjtu-vi-campus-6.jpg` (饮水思源 monument, red
    clock tower, night library, autumn/sunset scenes)
  - `snippets/` reusable SJTU-VIS chart/diagram blocks (see below)

### SJTU VIS accent palette (`sjtuaccents.sty`)

Loaded automatically by `main.tex.template`. Use these for on-brand emphasis,
callout boxes, and figures instead of generic LaTeX colors:

| Color name        | RGB           | VIS name | Typical use                          |
|-------------------|---------------|----------|--------------------------------------|
| `sjtuRedPrimary`  | 166,32,56     | 交大红   | primary emphasis, structure (default)|
| `sjtuLightGold`   | 224,207,189   | 浅金     | example-block tabs, accent fills     |
| `sjtuLightGray`   | 191,191,191   | 浅灰     | transitions, footer rules            |
| `sjtuYouthBlue`   | 23,95,139     | 青春蓝   | secondary palette / blue accents     |
| `sjtuBrightGreen` | 146,208,80    | 亮绿     | contrast / "positive" accent         |

Convenience macros: `\sjtuemph{...}` (brand-red bold, the template's standard
emphasis), `\sjtured{...}`, `\sjtugold{...}`, `\sjtugray{...}`. Example blocks
(`\begin{exampleblock}`) automatically render with the VIS gold callout style.

### Swapping the cover background

The default cover uses the bundled `vi/sjtu-vi-sjtuphoto.jpg`. To use a campus
photo (`sjtu-vi-campus-1.jpg` … `sjtu-vi-campus-6.jpg`), uncomment a
`\titlegraphic{...}` line in `main.tex` (the template ships options commented in
the preamble).

### Chart / diagram snippets (`snippets/`)

Reusable, on-brand LaTeX/TikZ blocks rebuilt from the official 图表 layout pages,
already colored with the VIS palette. Drop one into a section file with
`\input{snippets/<name>}` (each file is a complete `\begin{frame}…\end{frame}`,
edit the placeholder data):

| Snippet                  | What it gives you                              | Extra package |
|--------------------------|------------------------------------------------|---------------|
| `table-styled.tex`       | Red-header, banded-row results table + gold note | `booktabs` (preloaded) |
| `timeline.tex`           | Milestone timeline with year markers (TikZ)    | — (theme TikZ) |
| `process-steps.tex`      | Four gold-numeral step boxes (01–04)           | — |
| `chart-bar.tex`          | VIS-colored grouped bar chart                  | `pgfplots` (commented line in preamble — uncomment) |

Use them as starting points, not decoration: keep one chart/diagram per slide
and replace the placeholder data with the user's real content.

## CityU

- Visual character: purple academic palette, restrained clean title page
- Good fit: compact lectures, concise reports, clean seminar decks
- Bundled runtime assets:
  - `CityULogo.pdf`

## NTU

- Visual character: NTU red/blue palette, smoothbars header with frame
  navigation, automatic section/subsection table-of-contents frames
- Good fit: technical talks, thesis defenses, research seminars
- Bundled runtime assets:
  - `NTU.sty` theme
  - `ntu-logo.png`

## Generic

- Visual character: institution-neutral, clean stock Beamer theme (no logo,
  no university branding, no branded color scheme)
- Good fit: cross-institution talks, drafts, any deck that should carry no
  school identity
- Bundled runtime assets:
  - none (template only; zero extra package dependencies)

## Selection rule

- Ask the user to choose explicitly during interview.
- Do not infer template from language, institution, or talk type.
- Do not change narrative structure when the user changes template.

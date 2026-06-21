# LaTeX Generation Rules

## Output structure

Generate:

```text
main.tex
sections/
figures/
references.bib
```

Keep reusable template assets in the project root when required by the selected variant.

## Build target

- Use XeLaTeX-compatible source.
- Standard compile command:

```bash
latexmk -xelatex main.tex
```

- Use a modular `\input{sections/...}` structure in `main.tex`.

## Slide-writing rules

- Keep one idea per slide.
- Prefer short titles that reveal the slide’s claim or purpose.
- Split dense content instead of shrinking fonts aggressively.
- Use formulas only when they carry the argument.
- Introduce notation before using it.
- Use figures only when the source is supplied or clearly specified by the user.
- Cite sources **inline with author-year** (e.g., “Gul, Wu, and Yang 2013”), using biblatex `\textcite` / `\parencite` with entries in `references.bib`. **Do not generate a dedicated references / bibliography slide (`\printbibliography`) by default** — add one only when the user explicitly asks for it.
- Keep appendix material available when requested, but do not force it into every deck.
- When formulas, figures, a bibliography slide, or appendix slides are explicitly requested, reserve dedicated approved slots for them during generation rather than bolting them on after the deck is drafted.

## Template colors

- Use the variant's own palette for emphasis, callout boxes, and figure accents
  rather than ad-hoc `\color{red}` / `\textbf` everywhere.
- **SJTU**: `sjtuaccents.sty` is loaded automatically. Use `\sjtuemph{...}` for
  primary emphasis (brand-red bold) and the named VIS colors `sjtuLightGold`,
  `sjtuLightGray`, `sjtuYouthBlue`, `sjtuBrightGreen` for accents. Prefer
  `exampleblock` for asides (it renders in the VIS gold callout style). See
  `references/templates.md` for the full palette table.
- Keep emphasis sparing — one or two accented elements per slide, matching the
  restrained official template look.

## Academic integrity rules

- Never invent citations, empirical results, theorem statements, or numerical magnitudes.
- Mark missing content explicitly with placeholders such as `TODO: insert user-supplied result`.
- When evidence is incomplete, say so in the generated deck notes or placeholders rather than smoothing over the gap.

## Recommended section splitting

- `lecture`: learning goals, core content, examples/applications, summary
- `research talk`: motivation, design, results, conclusion

Use the approved outline to refine or replace these defaults.

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
- Keep references and appendix material available when requested, but do not force them into every deck.
- When formulas, figures, references, or appendix slides are requested, reserve dedicated approved slots for them during generation rather than bolting them on after the deck is drafted.

## Academic integrity rules

- Never invent citations, empirical results, theorem statements, or numerical magnitudes.
- Mark missing content explicitly with placeholders such as `TODO: insert user-supplied result`.
- When evidence is incomplete, say so in the generated deck notes or placeholders rather than smoothing over the gap.

## Recommended section splitting

- `lecture`: learning goals, core content, examples/applications, summary
- `research talk`: motivation, design, results, conclusion

Use the approved outline to refine or replace these defaults.

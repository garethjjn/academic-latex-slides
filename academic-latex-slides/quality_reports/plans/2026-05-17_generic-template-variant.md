# Plan: Add a fourth "generic" (no-branding) template variant

**Status:** APPROVED — 2026-05-17

## Goal

Add a 4th visual variant `generic` alongside `msu` / `sjtu` / `cityu`: a clean,
institution-neutral Beamer deck with no university logo or branded theme, using
only a stock Beamer theme so it shares the same `ctexbeamer` + XeLaTeX + biber
build path and adds zero package dependencies.

## Design

- New `assets/templates/generic/main.tex.template`: `ctexbeamer`,
  `\usetheme{Boadilla}` (stock, neutral blue, footline + frame numbers, no
  logo), navigation symbols removed, same nine `{{PLACEHOLDERS}}`, Outline
  frame + neutral `\AtBeginSection` divider. No bundled asset files — the
  `generic/` dir contains only `main.tex.template`.
- `scaffold.py`: single change — add `"generic"` to `TEMPLATE_CHOICES`.
  section/render/copy logic is already template-agnostic and asset-safe.

## Files to modify (canonical → sync → refresh installs)

1. NEW `skills/academic-latex-slides/assets/templates/generic/main.tex.template`
2. `skills/academic-latex-slides/scripts/scaffold.py` — TEMPLATE_CHOICES
3. `skills/academic-latex-slides/references/templates.md` — add Generic entry
4. `skills/academic-latex-slides/references/interview-protocol.md` — Tier 1
   template script + nine-fields row include Generic (EN/ZH)
5. `skills/academic-latex-slides/SKILL.md` — rule #3 "three→four", frontmatter
   description
6. `skills/academic-latex-slides/agents/openai.yaml` — short_description
7. `README.md` (root) — intro, Features, Template-variants table, scaffold
   `--template` values
8. `.claude-plugin/marketplace.json` + `plugins/.../.claude-plugin/plugin.json`
   — variant lists in descriptions (plugin.json not covered by sync script)
9. Run `scripts/sync_distributions.py` (mirrors items 1–6)
10. Refresh on-machine installs (no `/plugin` available):
    - Codex: re-copy canonical → `~/.codex/skills/academic-latex-slides`
    - Claude cache: re-copy canonical → `…/plugins/cache/academic-latex-slides/
      academic-latex-slides/1.0.0/skills/academic-latex-slides`
    - Keep plugin version `1.0.0` (bumping breaks the version-pinned cache dir
      while `/plugin update` is unavailable; note as follow-up).

## Verification

- Compile smoke test: scaffold `generic` for `en` and `zh`, run
  `latexmk -xelatex main.tex`, confirm a PDF is produced (also validates this
  machine's XeLaTeX/biber/ctex chain).
- `scaffold.py -h` shows 4 template choices.
- Canonical == plugin mirror == Codex copy == Claude cache (byte-identical).
- Grep self-check: no stale "three variants" / "MSU, SJTU, or CityU" /
  "MSU/SJTU/CityU" enumerations left without Generic.

## Out of scope

- No plugin version bump (operational reasons above).
- No git commit unless the user asks (offer at wrap-up).

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
  - SJTU theme `.sty` files
  - `vi/` visual identity assets

## CityU

- Visual character: purple academic palette, restrained clean title page
- Good fit: compact lectures, concise reports, clean seminar decks
- Bundled runtime assets:
  - `CityULogo.pdf`

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

# Paper Spec — canonical context object

**What this is.** The single structured spec that the `audit-write-interview` skill
emits and **every** sub-skill consumes. Before this existed, each of the 7 sub-skills
re-asked the same context questions ("what's your DV / IV / setting / finding?") — that
duplication is now centralized here. A sub-skill should **prefer an existing
`paper-spec.md`** in the working directory; only if it is absent should it gather the
fields inline or invoke `/audit-write-interview`.

Persist as `paper-spec.md` in the user's working directory so it survives context
compaction and is reused across every section.

---

## Field set

Each field carries a status tag: **CLEAR** (user-supplied / confirmed) ·
**ASSUMED** (reasonable default, user may override) · **BLOCKED** (cannot proceed
until answered). Mirror the repo's requirements-spec discipline.

```markdown
# Paper Spec

- **Working title:** … | status: …
- **Target journal:** JAE | JAR | TAR | AJPT — status: …
  (drives roadmap rule, abstract norms, identification bar — see journal_profile_bank.md)
- **Research question:** one sentence — status: …
- **Dependent variable (DV):** proxy + which audit-quality dimension
  (output/input, per audit_quality_framework.md) — status: …
  - proxy caveats acknowledged? (e.g., Aobdia 2019 on DAC) — status: …
- **Independent variable (IV):** the auditor/firm/client characteristic + how built
  (bottom-up construction) — status: …
- **Setting:** country · period · unit of observation — status: …
- **Sample:** N + source database — status: … (use [AUTHOR: N over PERIOD] if unknown)
- **Identification strategy:** quasi-experiment / shock / PSM / cross-sectional+FE — status: …
- **Headline finding + magnitude:** direction + pp + % of base + benchmark
  (or [AUTHOR: …] if pre-results) — status: …
- **Mechanism:** the FOR argument (1–2 sentences) — status: …
- **Tension / counter-force:** the AGAINST argument — status: …
- **Pejorative-reading risk?** (drives the H(a)/H(b) pair-prediction device) — status: …
- **Intended contributions:** 3–4, each mapped to a named literature
  (see move_bank.md M6 / contribution_formulas.md) — status: …
- **Known limitations / scope:** (single-country? no clean experiment?) — status: …
```

## Rules

- **Never invent field values to "complete" the spec.** Unknown → `[AUTHOR: …]` +
  status BLOCKED/ASSUMED. The `rubric.md` integrity gate applies to specs too.
- A spec with any **BLOCKED** field stops the progressive-outline ratchet at Stage 0
  until resolved.
- The spec is the **only** context object sub-skills should need; if a sub-skill finds
  itself re-asking a field already in the spec, that is a DRY regression.

See `progressive_outline.md` for how the spec feeds the staged drafting ratchet.

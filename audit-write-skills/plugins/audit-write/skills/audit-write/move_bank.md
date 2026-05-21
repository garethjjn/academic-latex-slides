# Move Bank (single source — cross-section reusable moves)

**What this is.** A compact canonical catalog of the rhetorical "moves" reused across
*more than one* section, so they are defined once and the section pattern files keep
only their section-specific *application notes* and worked examples (which stay — they
are the verifiable corpus exemplars per `corpus_manifest.md` §2).

This is an **index of moves**, not a relocation. When a pattern file's move duplicates
one below, it should link here for the canonical form and keep its local example.

Provenance / prior-not-law caveat: `corpus_manifest.md` §2.

> **Frequency provenance (Stage-1 update 2026-05-21).** A bare `k/6 (template)` count is over the 6 original template papers (`corpus_manifest.md` §1). Headline intro-move frequencies have been **re-derived over n=22** (6 template + 16 Stage-1 pilot) and are written `k/22` with a pointer to `corpus_inventory/move_presence_matrix.md`. Do not read a `k/6 (template)` as if it were n=22.

---

## M1 — Intro opening moves (4)

| Move | When | Full treatment |
|---|---|---|
| A. Lit-baseline ("A large body of research finds…") | default; safest | `../audit-write-intro/intro_patterns.md` Block 1 |
| B. Lit-contradiction ("Prior research finds X; however these studies…") | contribution overturns a prior finding | same |
| C. Theory-grounded ("Economic theories of X emphasize…") | contribution imports outside theory | same |
| D. Construct-introduction ("X is a qualitative characteristic that…") | known construct, new angle | same |
| E. RQ-first ("In this study we examine whether…" before any lit anchor) | design-driven / methods / concordance papers | `../audit-write-intro/intro_patterns.md` Block 1 |

n=22 opener distribution (6 template + 16 Stage-1 pilot; `corpus_inventory/move_presence_matrix.md`): **M1A 11/22** (dominant default), M1D 2/22, M1B/M1C 1 pure each (+ hybrids), **M3-first (RQ-before-anchor) 5/22 — a recognized variant, not a violation** (19-JWW, 19-Aob, 22-FHKF, 23-ZBLM, 16-DLLN).

Forbidden openings: anecdote/news, policy motivation, epigraph in ¶1, "auditing is important",
"the literature lacks". NOTE: previously stated "0/6"; the n=22 corpus has **2 counter-examples**
(anecdote 20-WY, policy-motivation 22-Dug — both JAR, pre-2023). Treat as rare/risky and
JAR-tolerated only when the hook carries genuine resonance; still avoid at JAE/TAR post-2023.

## M2 — Gap statement (3 forms)

Direct ("the effects of X have not been explored") · Conditional ("these studies,
however, examine [confounded setting]") · Construct-tension ("while research documents
[benefit], evidence on whether X→Y is limited"). Must appear by end of Block 1.

## M3 — Research-question statement

"The purpose of this study is to examine whether […]" / "We attempt to fill this gap by
investigating whether […]" / "In this paper we extend this literature by investigating
whether […]". Usually the last sentence of Block 1.

## M4 — Tension openers (strong default, NOT universal — re-derived n=22)

"We note, however, that there is tension in our prediction" · "Several factors may work
against our prediction" · "However, there are also reasons why [the opposite may hold]".
Placement before- or after-H is ~50/50. **Re-derived over n=22** (was claimed "6/6
corpus-unanimous"): canonical-form **7/22**, any-form (canonical + variants: active-phrasing,
enumerated, head-placed, in-¶1, three-sided, methodological) **14/22**, absent-from-intro
**8/22** (frequently deferred to §2). See `corpus_inventory/move_presence_matrix.md`. Per
`corpus_manifest.md` §2 this is a strong prior, not a law. Pejorative-trait tensions pair with the H(a)/H(b)
device → `../audit-write-hypothesis/SKILL.md`; objections to pre-empt → `referee_objection_bank.md`.

## M5 — Magnitude framing forms (6 core + 2 DV-specific variants) — for intro Block 4 & results main-magnitude block

| Form | Shape |
|---|---|
| F1 percentage-point change | "a 2.1 pp decline" |
| F2 percent of base rate | "a 19% decline vs the mean of 10.4%" |
| F6 literature benchmark | "comparable to mandatory rotation ([AUTHOR: cite])" |
| F4 standard-deviation shift | "a one-SD increase in [IV] …" |
| F3 decile/quartile shift | "bottom→top decile" |
| F5 interquartile change | "an IQR change in [IV]" |
| F7 time-decline (latency DV) | "from over 600 days to just two days" |
| F8 odds-ratio (logit/probit DV) | "increases the odds of [outcome] by 50%" |

Stage-1 pilot also surfaced two **F6 sub-variants**: *spatial-distance* threshold ("within 185 kilometers", 19-BGH) and *internal-benchmark* (comparator is the same regression's other coefficient — "half as important as client size", 20-CKMS). F7 (22-FW) and F8 (19-BGH, 23-ZBLM) are for latency and logit/probit DVs respectively; see `corpus_inventory/move_presence_matrix.md`.

**Canonical corpus frequencies (k/6) for F1–F6 live in
`../audit-write-results/results_patterns.md` §"magnitude framing" — this index does
not re-state them, to avoid a divergent copy (`corpus_manifest.md` §5.3).** Default
headline pattern **F1 + F2 + F6**; the 3-sentence translation move + worked example are
in that same file. Abstracts use **no** magnitude forms (`journal_profile_bank.md`).

## M6 — Contribution formulas (8) — intro Final block & referee O6/O8

1 add-to-literature · 2 contribute-on-dimension · 3 first-to-examine · 4 complement/extend
· 5 implications-for-audience · 6 fill-a-gap · 7 single-country-as-method-asset ·
8 novel-measure. Combination patterns A–D and the **full templates + corpus examples**:
`../audit-write-intro/contribution_formulas.md` (single home — do not duplicate; link).
Forbidden: "sheds light", "paves the way", "pivotal/groundbreaking", self-praise adjectives.

## M7 — Closing scope/limitation move (optional 5th intro element)

"We acknowledge, however, that [limitation]. In particular, [nuance]. Nonetheless,
[reframe as feature/scope]." Include for single-country/unusual-sample/no-clean-experiment;
omit if US data + natural experiment (would read defensive). Never inside the contribution
paragraphs. Full template: `../audit-write-intro/contribution_formulas.md` §closing limitation.

## M8 — IV-build move (design Part 2 & referee O8)

"We construct [IV] in [k] steps. First [raw]. Second [aggregation]. Third [final form]."
For a novel measure, append a validation sentence (convergent check + robustness to an
alternative construction). Full treatment: `../audit-write-design/design_patterns.md`.

---

## Rule when editing a move

Change the canonical form **here**, then make sure no pattern file silently re-defines a
divergent version. Frequency tags ("k/6") are over the named corpus (`corpus_manifest.md`
§2) — if the corpus changes, re-derive them; do not leave a stale count.

# Audit-Writing Scoring Rubric (shared instrument)

**What this is.** The single, anchored 0–100 instrument used by **every** `audit-write-*`
Mode-C audit and by the `audit-write-critic` subagent. Before this file, each skill
emitted an ad-hoc `Score [X/100]` with no defined anchors → scores drifted run-to-run
and were not comparable. This rubric fixes the anchors so a "82" means the same thing
in every section and every session.

Use it verbatim. Do not invent alternative dimensions or weights per section. The only
thing that varies by section is the **structural anatomy** plugged into Dimension 1
(each sub-skill names its own canonical structure; the rubric scores conformance to it).

---

## The integrity gate (apply FIRST, before scoring)

This is pass/fail and **overrides the weighted score**:

> If the text contains **any fabricated citation, invented empirical result, or invented
> numeric magnitude** presented as real (i.e., not a `[AUTHOR: …]` / `[ILLUSTRATIVE]`
> placeholder), the total score is **capped at 55/100 (FAIL)** regardless of how good
> the other dimensions are, and the audit must name every offending span.

Rationale: the suite's entire credibility rests on never manufacturing evidence
(`corpus_manifest.md` §2). A beautifully structured section built on a fake citation is
worth less than an ugly honest one. This gate operationalizes the "integrity rules stay
hard" principle — conventions are priors, integrity is not.

---

## The 5 dimensions, weights, and band anchors

| # | Dimension | Weight |
|---|---|---|
| 1 | Structure / template compliance | 20 |
| 2 | DeFond style register | 20 |
| 3 | Magnitude & evidentiary discipline | 25 |
| 4 | Argument & contribution clarity | 20 |
| 5 | Audit vocabulary & framework anchoring | 15 |

Each dimension is scored into one band; the band's midpoint × weight, summed, gives the
composite (then apply the integrity gate).

### Band scale (applies to every dimension)

| Band | Range | Midpoint used |
|---|---|---|
| Excellent | 90–100 | 95 |
| Solid | 75–89 | 82 |
| Weak | 60–74 | 67 |
| Failing | 0–59 | 45 |

Composite = Σ (dimension midpoint × weight) / 100, then integrity-gate cap if triggered.

---

### Dimension 1 — Structure / template compliance (weight 20)

Scores conformance to the section's canonical anatomy (the calling sub-skill supplies
it: e.g., intro = 5-block; abstract = 5-move; hypothesis = 4-/6-move arc; design =
5-part; results = 6-sub-section; robustness = numbered battery; referee = 4-move).

- **90–100** All required blocks/moves present, in canonical order, correctly proportioned.
- **75–89** All present; one mis-ordered or mis-proportioned; no missing mandatory element.
- **60–74** One mandatory element missing or two mis-placed (e.g., no tension paragraph; identification in §3).
- **0–59** Multiple mandatory elements missing; structure not recognizable as the target section.

### Dimension 2 — DeFond style register (weight 20)

Verb whitelist/blacklist (`style_dna.md`), calibrated confidence, no marketing
adjectives describing own work, no AI tells, sentence/paragraph mechanics.

- **90–100** Zero blacklist verbs; zero self-praise adjectives; zero AI tells; hedging calibrated.
- **75–89** ≤2 minor register slips, none changing a claim's epistemic strength.
- **60–74** A banned verb in a results/contribution sentence, or ≥1 marketing adjective on own work, or an AI tell.
- **0–59** Pervasive over-claiming ("show that/prove/demonstrate"), boastful or chatty register.

### Dimension 3 — Magnitude & evidentiary discipline (weight 25, highest)

Magnitudes anchored (pp / % of base / benchmark, per section rules); placeholder
discipline; provenance honest. *Interacts with the integrity gate.*

- **90–100** Every reported effect magnitude-anchored where the section requires it; all unknowns are `[AUTHOR: …]`; no provenance overclaim.
- **75–89** One unanchored magnitude or one vague quantifier ("substantial") where a number is expected.
- **60–74** Multiple unanchored magnitudes, or a result reported as coefficient-only where translation is mandatory.
- **0–59** Vague-effect language throughout, OR triggers the integrity gate (→ capped 55).

### Dimension 4 — Argument & contribution clarity (weight 20)

Gap → prediction → finding → contribution coherence; tension present where mandated;
contributions mapped to identifiable literatures (not marketing).

- **90–100** Clean logical chain; explicit tension; 3–4 contributions each to a named literature.
- **75–89** Chain intact; tension compressed; contributions present but one is vague.
- **60–74** Gap or tension implicit/missing; contributions generic ("adds to the literature").
- **0–59** No discernible gap or contribution; claims not connected to a prediction.

### Dimension 5 — Audit vocabulary & framework anchoring (weight 15)

Correct DeFond-Zhang framework terms (`audit_quality_framework.md`); proxy named with
its dimension; no loose "good/bad audits".

- **90–100** Framework-correct throughout; DV anchored to the taxonomy; proxy caveats acknowledged where relevant (e.g., Aobdia on DAC).
- **75–89** Mostly correct; one loose term ("auditing quality", "abnormal accruals").
- **60–74** Several loose terms; DV not anchored to the framework.
- **0–59** Non-standard vocabulary; audit-quality construct used naively.

---

## Output format (every Mode-C audit ends with this block)

```markdown
## Score

| Dim | Band | Pts |
|---|---|---|
| 1 Structure | [Excellent/Solid/Weak/Failing] | [midpoint] |
| 2 Register | … | … |
| 3 Evidentiary | … | … |
| 4 Argument | … | … |
| 5 Vocabulary | … | … |
| **Composite** |  | **[X]/100** |

Integrity gate: [PASS / FAIL — capped 55; offending spans: …]
Headline: [one sentence — the single highest-leverage fix]
```

Quality thresholds (suite convention, aligned with the repo's 80/90 gates):
**≥90 ship-ready · 75–89 revise-then-ship · <75 do not ship.**

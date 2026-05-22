# DeFond / Zuo / Khurana Audit-Writing Style DNA

**Source.** Distilled from 7 corpus papers (DeFond 2007, 2014, 2016, 2024, 2025; Khurana 2026; Dekeyser 2024) covering JAE, TAR, and recent JAE conference papers.

This file is the **shared style guide** for all `audit-write-*` sub-skills. The intro skill, abstract skill, design skill, etc. all consult it.

---

## 1. Verb whitelist (use these freely)

### For stating findings

✅ **Recommended:**
- `find` / `we find that ...`
- `document` / `we document evidence that ...`
- `observe` / `we observe that ...`
- `report` / `we report that ...`
- `provide evidence` / `provides evidence consistent with ...`

✅ **For describing prior literature:**
- `examines`, `investigates`, `studies`, `analyzes`
- `concludes`, `argues`, `posits`, `theorizes`
- `documents`, `provides evidence that`
- `finds` (use this when summarizing concrete results)

### For stating predictions

✅ **Recommended:**
- `hypothesize that ...` ★ DeFond signature
- `posit that ...` ★ DeFond signature
- `predict that ...`
- `conjecture that ...`
- `expect ...`
- `argue that ...`

### For interpreting results

✅ **Recommended:**
- `consistent with ...` ★ ★ DeFond signature — appears 30+ times in the 6 empirical intros combined
- `suggests that ...`
- `implies ...`
- `is consistent with the notion that ...`
- `is consistent with our prediction that ...`
- `aligns with the argument that ...`

### For acknowledging limitations

✅ **Recommended:**
- `we acknowledge that ...`
- `we cannot fully rule out that ...` (use sparingly, in conclusion not intro)
- `our results may not generalize to ...`

---

## 2. Verb blacklist (NEVER use these in audit-paper writing)

### Banned outright

❌ `prove` / `proves` — auditors don't prove, they assess
❌ `show that` (declarative claim) — DeFond uses "find" or "document"
❌ `demonstrate definitively`
❌ `establish definitively`
❌ `confirms beyond doubt`
❌ `delve` / `delves into` (AI-generated tell)
❌ `leverage` (as verb meaning "use")
❌ `pivotal` / `groundbreaking` / `paradigm-shifting`
❌ `shed light on`
❌ `pave the way`
❌ `paramount`
❌ `multifaceted`
❌ `landscape` (used metaphorically)
❌ `nuanced` (overused; use specific descriptor)

### Conditionally banned (allowed only in narrow contexts)

⚠️ `prove` — OK only in math/proof context for theory papers, not for empirical claims
⚠️ `demonstrate` — OK only in "demonstrate the importance of [setting]" sense (description), NEVER for empirical claims
⚠️ `significant` — only in statistical-significance context with specification of level (e.g., "significant at the 1% level"); NEVER as standalone adjective
⚠️ `important` — never as self-praise of own contribution; OK when describing the question's importance to the field
⚠️ `novel` — once per intro is acceptable, but only if defensible

### Why these are banned in DeFond/Zuo style

The DeFond writing voice is **calibrated confidence**: claims are precise, falsifiable, and presented without rhetorical inflation. "Show that" implies certainty beyond what archival evidence can deliver. "Prove" violates auditing's core epistemic stance. Marketing adjectives ("groundbreaking", "novel", "important") are abandoned in favor of letting the reader judge.

---

## 3. Hedging templates

### Standard hedge phrases (use these)

- `Consistent with [our hypothesis / prior research / theory], we find ...`
- `[X] is consistent with [interpretation A] but is also consistent with [interpretation B]. To distinguish, we ...`
- `[Result] is consistent with the notion that [mechanism]`
- `Our results are robust to [specification]`
- `While our setting may [limit X], the results [are still informative because Y]`
- `We acknowledge, however, that ...`
- `We cannot fully rule out [alternative], but our analysis is consistent with [main interpretation]`

### Negation hedges (use these for confidence)

- `Our results are not driven by ...`
- `Our findings are not explained by [alternative] ...`
- `These results are inconsistent with [opposing hypothesis]`
- `We find no evidence of [confounding alternative]`

### Forbidden hedges (don't use)

❌ `It can be argued that ...` — passive, weak
❌ `Some might suggest that ...` — anonymous strawman
❌ `One could potentially interpret ...` — over-hedged

---

## 4. Audit-quality terminology (canonical vocabulary)

### Audit quality (the central construct)

Use the **DeFond-Zhang 2014 framework** terminology consistently:

- **"Audit quality"** — preferred over "auditing quality" or "quality of auditing"
- **"Higher audit quality"** / **"lower audit quality"** — preferred over "good/bad audits"
- **"Output-based audit quality measures"** — restatements, going-concern opinions, accruals
- **"Input-based audit quality measures"** — auditor characteristics, audit fees
- **"Material misstatements"** — preferred over "errors" or "mistakes"
- **"Going-concern opinion (GCO)"** or **"GC opinion"** — both fine; be consistent within paper
- **"Discretionary accruals (DAC)"** — preferred over "abnormal accruals"
- **"Audit adjustments"** (Lennox-Wu lineage) — only when using MoF data or partner-level
- **"Restatements"** — preferred over "earnings restatements" (redundant)

### Auditor structure terminology

- **"Big N auditor"** or **"Big 4 auditor"** — both acceptable; use Big N for cross-sample, Big 4 for post-2002
- **"Engagement partner"** / **"signatory auditor"** — interchangeable in China context (note: Chinese audit reports are signed by TWO partners — top is review, bottom is engagement)
- **"Audit firm-level"** vs **"audit office-level"** vs **"audit partner-level"** — be precise about which level the analysis is at
- **"Industry specialist"** / **"industry expertise"** — preferred over "industry expert"

### Engagement-risk terminology (DeFond 2016 framework)

- **"Engagement risk"** = client business risk + audit risk + auditor business risk
- **"Inherent risk"** / **"control risk"** / **"detection risk"** — components of audit risk
- **"Litigation risk"** / **"reputation risk"** — components of auditor business risk

### China-specific terminology

- **"Financial reporting irregularities (FinIrreg)"** — preferred for Chinese restatement-equivalent (DeFond 2024)
  - Restatement (material accounting error)
  - + CSRC enforcement action for financial misrepresentation
- **"CSRC sanction"** — China Securities Regulatory Commission enforcement
- **"Mandatory partner rotation"** — required every 5 years in China
- **"State-owned enterprise (SOE)"** — preferred over "government-owned firm"
- **"Province-level"** / **"city-level"** government — be specific

---

## 5. Citation conventions

### How to introduce a citation

✅ **Preferred:**
- `(Smith and Jones, 2018)` — standard parenthetical
- `Smith and Jones (2018) find that ...` — narrative
- `Prior research finds that [claim] (Smith 2015; Jones 2017; Lee 2020)` — multiple cites for one claim
- `(see [Author, Year] for a review)` — review citation

### Multi-author citations

- **2 authors:** `Smith and Jones (2018)` — always spelled out
- **3+ authors:** `Smith et al. (2018)` — first cite includes all? (Style varies. JAE/TAR allow et al. throughout.)

### A note on citation choice

Citation choices belong to the user, not to this skill. When the user has not specified which references to cite for a given claim, leave a `[AUTHOR: cite for X]` placeholder rather than guessing. The skill's job is structure and voice, not picking the user's literature anchors.

### Citation density

Corpus median: **~30 citations per intro page**. JAE/TAR introductions are heavy on citations — every claim needs a backing reference.

---

## 6. Sentence-level mechanics

### Voice

- **First person plural ("we")** is universal in audit-paper writing — even single-authored papers use "we" (referring to author + reader, or convention).
- **Passive voice OK** for: methodology descriptions ("Standard errors are clustered by audit firm"), table notes, and limitations ("Limitations include ...")
- **Passive voice NOT OK** for: hypotheses, results, contributions, intro narrative

### Tense

- **Present tense** for prior literature: `Smith (2018) finds that...`
- **Present tense** for own findings: `We find that auditors...`
- **Past tense** for sample/data: `We collected data over the period 2005–2018.` (often becomes present in the actual writing — both acceptable)

### Sentence length

- Median sentence length in corpus: **22 words**
- Vary length: alternate short (10-15 words) with long (30-40 words)
- Never go above 50 words without breaking up

### Paragraph length

- Median paragraph length in corpus intros: **120 words / 5 sentences**
- One idea per paragraph
- Topic sentence at the start
- Avoid paragraphs over 250 words

---

## 7. Numbers, magnitudes, and units

### Always concrete, never vague

✅ "auditors with strong connections lower the probability of [outcome] by 2.1 percentage points"
✅ "a 19% decline in the average incidence of financial irregularities"
✅ "moving from the bottom to the top decile of conservatism decreases audit fees by 29 percent"

❌ "a substantial reduction in misstatements"
❌ "auditors significantly lower the rate of restatements"  (without magnitude)
❌ "we find a meaningful effect"

### Significant digits

- Coefficients in tables: **3 decimal places** (0.041, not 0.04108)
- Magnitudes in text: **1 decimal place for percentage points** (2.1%, not 2.13%)
- Sample sizes: **commas every 3 digits** (20,778, not 20778)
- p-values: report as `p < 0.01`, `p < 0.05`, or `p > 0.10`

### Required magnitude framing

Every result statement in the introduction must include at least ONE of:
- Absolute change (e.g., percentage points)
- Relative change (% of base rate or sample mean)
- Standard-deviation framing
- Decile / quartile shift
- Comparison to a known benchmark ("equivalent to the effect of mandatory rotation")

---

## 8. Audit-paper-specific structural conventions

### Where the hypothesis is stated

- In introduction: **alternative form, formal**
  > "**H1.** Audit partners' cultural trust is negatively associated with the likelihood of issuing going concern opinions, ceteris paribus."

- In hypothesis-development section: **narrative form, with theory**
  > "Following the [theory], we hypothesize that..."

- Both must appear in the paper. Hypothesis text should be VERBATIM identical between the two locations.

### Where to put theory

- In Section 2 (Hypothesis Development), NOT in the introduction
- Introduction has only the **intuition** for the hypothesis (1-2 sentences), not the full theory
- Detailed theory citations belong in the body

### Where to put limitations

- A 1-paragraph scope/limitation acknowledgment goes at the **end of the introduction**, after contributions, in 4/6 corpus papers
- Detailed limitations belong in the **conclusion**
- Never inside Block 4 (results) — undermines the headline finding

### Where to NOT have a roadmap (modern JAE style)

- Modern JAE papers (2020+): drop the roadmap entirely
- CAR / RAST: drop the roadmap (modern archival convention)
- TAR: keep a short 3-sentence roadmap
- JAR: optional; check 2-3 recent JAR papers in your area for the convention

---

## 9. Anti-AI patterns specifically applicable to audit writing

In addition to the generic econ-write anti-AI list, audit papers have these specific tells:

### AI tells in audit writing

- ❌ "Robust audit framework" (generic adjective + noun)
- ❌ "Comprehensive analysis of audit quality" (when author has done a single-test analysis)
- ❌ "Crucial role" / "critical role" (overused — replace with concrete description)
- ❌ "In the realm of auditing"
- ❌ "Auditors play a vital role in ensuring..." (broad-claim filler)
- ❌ "It is well-known that..." (lazy)
- ❌ "It goes without saying..." (then don't say it)
- ❌ Numbered lists of contributions where each contribution has the same length (real DeFond papers have varied paragraph lengths per contribution)

### Generic AI-slop tells (corroborated externally — see `../../docs/external-validation-ng.md`)

AI slop reads acceptably one sentence at a time but is collectively thin. In
audit prose these surface as:

- ❌ **Em-dash (—) overuse.** AI uses the em-dash far more than human academic
  writing. Audit prose rarely needs it: prefer a comma, a colon, or two
  sentences. (Mechanically flagged at ≥3 em-dashes + above-threshold density by
  `../../scripts/lint_style.py`.)
- ❌ **Rule-of-three / triadic lists** ("A, B, and C") used reflexively where two
  items, or one precise noun, would do. Vary list length; do not pad to three.
- ❌ **"not X but Y" / "not just about X, it's about Y"** with X and Y both vague
  abstractions ("not about infrastructure, it's about architecture"). Empty but
  self-important. Use the plain claim instead.
- ❌ **Noun-poverty / vague-adjective principle.** AI substitutes adjective+noun
  for a concrete noun ("robust instruction", "highly insightful paper",
  "comprehensive framework"). Every claim in audit prose carries a concrete noun,
  a number, or a reference — never a mood adjective standing in for content. This
  generalises the "robust audit framework" tell above into a rule.
- ❌ **Big, empty-but-self-important sentences** ("but it does change
  everything") — a grand claim with no referent and no magnitude. Delete it or
  attach the specific result.

> Note: heavy AI use is making human writing drift toward these patterns
> (*delve* is rising in human speech). Vigilance is required even on prose a
> human "wrote".

### Pattern enforcement

When auditing or rewriting text, search for these specific patterns:
1. "show that" → replace with "find that" or "document"
2. "demonstrate" → replace with "find" or "show" (only OK if showing means "exhibit", not "prove")
3. "robust audit" / any mood-adjective + abstract noun → replace with the specific quality dimension or a concrete noun
4. Three-sentences-each contributions → vary lengths
5. Adjectives describing own work ("important contribution", "novel finding") → delete the adjective
6. Em-dash (—) → replace with comma / colon / sentence split unless genuinely parenthetical and rare
7. "not X but Y" / "not just about X, it's about Y" → state the plain claim
8. Reflexive triads ("A, B, and C") → keep only the items that carry information

---

## 10. Mood / register

### The DeFond/Zuo voice is:

- **Confident but not boastful** — claims are calibrated, never inflated
- **Specific** — every claim has a number or concrete reference
- **Patient with the reader** — assumes intelligent reader who is NOT an expert in your subfield
- **Defensive against the next reviewer** — preempts objections in the introduction itself
- **Conservative with causal language** — uses "consistent with causal interpretation" rather than "we identify the causal effect"
- **Generous with prior literature** — cites broadly, never insults prior authors

### NOT the audit voice:

- ❌ Over-hedged ("It can be argued that perhaps auditors might possibly...")
- ❌ Boastful ("We make a groundbreaking contribution...")
- ❌ Vague ("Auditors play an important role...")
- ❌ Aggressive toward prior literature ("Smith (2018) gets it wrong because...")
- ❌ Casual / chatty ("Interestingly..." "Surprisingly..." — these are conversational tells)

The mood is **professional, careful, and specific**. Adjust accordingly.

# Audit-Paper Hypothesis Development: Section-2 Anatomy

**Source corpus.** Extracted from the 6 empirical hypothesis-development sections:
- DeFond, Hung, Trezevant 2007 JAE — `(07-DHT)` — multi-hypothesis (4), country-level
- DeFond, Lim, Zang 2016 TAR — `(16-DLZ)` — UNIQUE: no formal numbered H, narrative arc only
- DeFond, Li, Wong, Wu 2024 JAE — `(24-DLWW)` — single hypothesis, sub-divided 2.1/2.2 (pro/con)
- Dekeyser, He, Xiao, Zuo 2024 JAE — `(24-DHXZ)` — single hypothesis, theory-first arc
- DeFond, Qi, Si, Zhang 2025 JAE — `(25-DQSZ)` — single hypothesis with explicit "tension" paragraph
- Khurana, Li, Yeung, Yu 2026 JAE — `(26-KLYY)` — multi-hypothesis (3 pairs: H1, H2(a)/H2(b), H3(a)/H3(b))

The 7th paper (DeFond-Zhang 2014 JAE *Archival Auditing Review*) has no empirical H-development section and is excluded by design.

---

> **Frequency provenance (Stage-1 update 2026-05-21).** A bare `k/6 (template)` count is over the 6 original template papers (`corpus_manifest.md` §1). Headline move frequencies re-derived over **n=22** (6 template + 16 Stage-1 pilot) are written `k/22` with a pointer to `corpus_inventory/move_presence_matrix.md`. Do not read a `k/6 (template)` as if it were n=22.


## TL;DR — the actionable five

1. **The single-H modern paper has a 4-move arc**: literature/theory anchor → mechanism FOR prediction → counter-arguments / "tension" → formal H statement. ~1,200–1,800 words. Use `(24-DLWW)` and `(25-DQSZ)` as templates.
2. **The multi-H paper has a 2-tier arc**: a shared theory umbrella (Section 2.1) + per-hypothesis sub-section, each with mini-arc inside (Section 2.2.1, 2.2.2, …). Use `(26-KLYY)` as template.
3. **"Stated in alternative form" is the safest DeFond default** — appears verbatim in 5/6 (template) original papers immediately before the H block. Stage-1 pilot papers show legitimate exceptions: null-form Hs, RQ-only sections, narrative predictions, and RAST "Prediction 1/2/3" labels. Use the default unless the paper's theory is explicitly unsigned or exploratory.
4. **The tension paragraph is a strong default, not a law** — appears in 6/6 (template) original papers, but Stage-1 pilot papers show tension can be thin, head-placed, converted into moderators, embedded symmetrically in FOR/AGAINST structure, or absent in RQ-only / mixed-methods designs. If omitted, state the reason.
5. **Hypotheses are predictions, not claims** — verbs are "we hypothesize that…", "we posit that…", "we expect…", "we argue that…". Verbs to NEVER use: "we will show", "we prove", "common sense suggests", "obviously".

---

## The canonical arc — 4 moves for single-H, 6 moves for multi-H

### Single-hypothesis arc (single-H): 4 moves

```
Move 1: ANCHOR
        (a) Theory anchor — "Economic theories of X suggest…" / "Drawing on prior research in psychology…"
        (b) Literature anchor — "Prior literature finds that X…" / "A growing literature in X shows…"
        Length: 1–3 paragraphs.

Move 2: MECHANISM (argument FOR predicted direction)
        Build the chain: cause → mechanism → predicted outcome.
        Use specific examples ("connections with customers should improve the auditor's
        ability to evaluate revenue recognition…").
        Length: 2–4 paragraphs (often the longest move).

Move 3: TENSION (counter-arguments)
        "However, there are reasons why…" / "While X should also Y…"
        Length: 1–2 paragraphs.

Move 4: FORMAL HYPOTHESIS
        Bridge sentence: "Based on the above arguments we posit the following
                          hypothesis in the alternative form:"
        Display H statement (bold "Hypothesis." or "H1." inline).
        OPTIONAL: post-H "we emphasize that there is tension…" wrap-up paragraph.
```

### Multi-hypothesis arc (multi-H): 6 moves

```
Move 1: SHARED THEORY UMBRELLA (Section 2.1, all sub-hypotheses inherit from it)
        E.g., "Cultural trust" (26-KLYY 2.1), "Investor protection institutions" (07-DHT
        opening paragraph of 2).
        Length: 3–10 paragraphs.

Move 2: BRIDGING PARAGRAPH (Section 2.2 opener, NOT yet a hypothesis)
        "In this study, we examine the role of [X] in [setting]…"
        States the conceptual framing for ALL sub-hypotheses.
        Length: 1 paragraph.

Move 3 → 6 (or n): PER-HYPOTHESIS SUB-SECTIONS (2.2.1, 2.2.2, …)
        Each sub-section is a mini single-H arc:
            (a) Sub-anchor (1 short paragraph) — context for THIS hypothesis
            (b) Mechanism + tension (1–3 paragraphs)
            (c) Formal H statement (display)
        Length per sub-section: 200–400 words.

Move 7 (optional): CROSS-SECTIONAL PREVIEWS
        "We perform a number of cross-sectional tests to shed light on the specific
         conditions in which these predictions hold." (26-KLYY)
        Bridges H section to research-design section.
```

---

## Move 1: Anchoring patterns (theory vs literature vs both)

| Anchor type | Frequency | Example | When to use |
|---|---|---|---|
| **Theory-first** | 2/6 (template) | "A growing literature in economics, finance, and accounting shows that a person's experiences significantly affect her judgment and decision making beyond 'the information set' considered in traditional economic models" `(24-DHXZ)` | When importing theory from psychology/economics into accounting |
| **Literature-first** | 3/6 (template) | "Prior literature finds that auditors who are socially connected to their client's executives and audit committee chairs, provide lower quality audits (Guan et al., 2016; He et al., 2017)." `(24-DLWW)` | When you are extending an audit-literature chain |
| **Theory + Literature combined** | 1/6 (template) | "The traditional approach in economics, finance, and accounting is to take individual beliefs and preferences as exogenous… More recently, economic theories endogenize these attitude endowments, arguing that individual beliefs and preferences are shaped by two key mechanisms (Bisin and Verdier, 2000)." `(26-KLYY)` | When you need a deep theory umbrella because you have multiple hypotheses |

**Hard observation:** in 5/6 (template) papers, the anchor cites at least **one** non-accounting source (psychology, sociology, economics, neuroscience). The DeFond-Zuo style explicitly **imports** theory. Pure within-accounting anchoring (like 07-DHT) is the older style — modern (2024+) papers all reach outside.

### Anchor verbs (whitelist)

- "Prior research finds that…"
- "A growing literature in [X] shows that…"
- "Economic theories of [X] suggest that…"
- "Building on this line of research, we argue…"
- "Drawing on prior research in [X], we…"
- "[Authors] (year) document that…"
- "Following [Authors] (year), we…"

### Anchor verbs (blacklist)

- ❌ "It is well-known that…" (assumes consensus)
- ❌ "Common sense suggests…" (no theory)
- ❌ "Anecdotal evidence indicates…" (not citation-grade)
- ❌ "It seems intuitive that…" (no theory)

---

## Move 2: Mechanism construction — the FOR argument

The mechanism move is **the longest** move in the section (2–4 paragraphs in 5/6 (template) papers). It must:

1. **Specify a causal chain** in plain English — cause → mechanism → outcome.
2. **Provide 2–4 concrete examples** (not abstract claims).
3. **Cite supporting theory or evidence** for each link in the chain.

### Verbatim example of a clean mechanism build (24-DLWW, ¶2 of 2.1)

> "We extend the research that examines auditors' social ties by examining auditors' social connections to their clients' business communities. Strong connections within their clients' communities should increase an auditor's competency in auditing their clients. **For example,** connections with customers should improve the auditor's ability to evaluate their clients' revenue recognition practices, estimate the collectability of accounts receivable and assess the obsolescence of inventories. **Connections with their clients' suppliers should help auditors assess** the potential for increasing costs or supply chain disruptions that may threaten their clients' ability to service their customers. **Connections with their clients' bankers should enhance the auditor's assessment of their clients'** ability to secure future financing." `(24-DLWW)`

The pattern: 1 abstract claim → 3 parallel "Connections with X should help Y" examples. **Parallelism is canonical.**

### Verbatim example of theory-driven mechanism (24-DHXZ)

> "Our thesis builds on an extensive body of research in psychology and cognitive science that differentiates between high-validity and low-validity environments. The term 'validity' is used to describe 'the causal and statistical structure of the relevant environment' (Kahneman and Klein, 2009, p. 520). In a high-validity environment, common patterns repeat themselves, and feedback is often rapid and accurate. … In contrast, in a low-validity environment, the rules of the game are not well defined, observed patterns may not repeat themselves, and feedback is often delayed or inaccurate. … Auditors often work in a low-validity environment with evolving business practices and accounting standards." `(24-DHXZ)`

The pattern: theoretical concept → contrast (high vs low) → application to auditing setting. **Three-step abstraction reduction.**

### Mechanism verbs (whitelist, in order of frequency)

- "We argue that…" — most common; appears in 5/6 (template) papers, sometimes 6+ times in one section
- "We posit that…" — slightly more formal, signals a deductive prediction
- "We expect [X] to…" — for direct empirical predictions
- "We hypothesize that…" — usually reserved for the formal H statement
- "We conjecture that…" — when prediction is more speculative
- "[X] should [Y]" — the workhorse phrase for mechanism descriptions
- "This is consistent with…" — when invoking supporting evidence
- "The above arguments suggest that…" — closer of mechanism move

### Mechanism verbs (blacklist)

- ❌ "We will show that…" (begs the empirical question)
- ❌ "We expect to find that…" (semantically empty — just say "we expect")
- ❌ "We will demonstrate that…" (overclaims pre-data)
- ❌ "It is clear that…" / "Obviously…" (style violations)
- ❌ "It is reasonable to believe that…" (weak hedge that adds nothing)

---

## Move 3: Tension / counter-argument structure

### Original-corpus default: the tension paragraph appears in 6/6 (template) papers

The original six-paper corpus has **zero** instances of a hypothesis section without a counter-argument paragraph. Treat this as the default reviewer expectation, but not as a universal law. Stage-1 pilot drafts add several disciplined exceptions: no-formal-H / RQ-only sections (`19-JWW`, `23-ACN`, `24-DGZZ`), narrative-prediction sections with only thin tension (`22-LNS`), mixed-methods prediction sections (`22-FHKF`), and sections where the counter-argument is converted into a moderator (`16-DLLN`). Phase D will re-count the exact `k/N`; until then, write "strong default" rather than "non-negotiable."

### Two structural placements (50/50 split)

**Placement A: BEFORE the H statement** (16-DLZ, 24-DLWW, 26-KLYY-H1, 24-DHXZ implicit)
- Structure: Mechanism → Tension → "Based on the above arguments…" → H
- Use when: you want H to feel like a "balanced" net prediction

**Placement B: AFTER the H statement** (25-DQSZ, 26-KLYY-H2-onward)
- Structure: Mechanism → H → "We emphasize that there is tension…"
- Use when: H is the lead and tension is preempting the reviewer

### Verbatim tension openers (memorize these)

| Opener | Paper | Notes |
|---|---|---|
| "However, there are reasons why [X] may [opposite]…" | 16-DLZ | Most common; safe |
| "However, there are also reasons why [X]…" | 16-DLZ | Slight variant |
| "However, auditors also have strong incentives to maintain their independence, because…" | 24-DLWW | Auditor-specific framing |
| "However, there are several reasons why this relation may not hold empirically." | 26-KLYY | Three-reason enumeration follows |
| "We emphasize that there is tension in our prediction." | 25-DQSZ | Modern explicit signpost |
| "We note, however, that…" | (intro corpus) | Used in intros, not H sections |

### The "three reasons" enumeration (26-KLYY)

26-KLYY uses an explicit three-numbered counter-argument list:

> "However, there are several reasons why this relation may not hold empirically. **First,** if accounting firms have in-house rules for implementing auditing standards, then one could argue that individual differences among audit partners should play only a minor role… **Second,** market forces could lead to contracts and incentive schemes that overcome individual differences. **Third,** audit partners' tendency to trust could be influenced more by their local environment (oblique socialization) than by their cultural heritage (direct socialization). To the extent that these countervailing arguments hold, they would work against finding results supporting our hypothesis." `(26-KLYY)`

Pattern: signpost paragraph + numbered list + closing "to the extent that…" sentence. Use this when you have ≥3 distinct counter-arguments.

### The "however, there are reasons" 2-camp framing (16-DLZ)

16-DLZ devotes entire paragraphs to **two** competing camps:

> "**However, there are reasons why conservatism may increase audit engagement risk.** One is that timelier recognition of bad news may trigger more frequent debt covenant violations, thereby increasing client default risk and auditor business risk. … **Another reason why conservatism may increase engagement risk is because it reduces earnings informativeness and persistence**, which exposes auditors to higher reputation risk." `(16-DLZ)`

Pattern: signpost → "One is that…" → second paragraph "Another reason…". Use when counter-arguments are weighty enough to need separate paragraphs.

### Resolution language (when prediction direction is genuinely ambiguous)

When you cannot resolve the tension, signal it explicitly:

- "Whether the net effect is [X] is ultimately an empirical question." (intro convention)
- "Therefore, given the difficulty in predicting which strategies auditors are likely to choose…, we perform tests that examine each strategy individually" `(16-DLZ)`
- "Thus, we are unable to predict whether [X] will increase, decrease, or have no overall net effect on [Y]." `(07-DHT)` — leads to a non-directional H4
- "we form the following hypothesis [in alternative form]" — non-committal format

---

## Move 4: Hypothesis statement format

### Verbatim formats from the corpus

```
07-DHT (4 hypotheses, all displayed and centered):
"Hypothesis 1. Countries with higher earnings quality have more informative annual
                earnings announcements."

24-DLWW (single hypothesis, "Hypothesis." label):
"Based on the above arguments we posit the following hypothesis in the alternative form:
 Hypothesis.
 Chinese engagement auditors with stronger social networks in their clients' communities
 provide higher quality audits."

24-DHXZ (single hypothesis, "Hypothesis." label, no transition phrase):
"Therefore, we form the following hypothesis.
 Hypothesis.
 Auditors with a wide range of industry experiences are associated with higher audit
 quality than auditors with a narrow range of industry experiences."

25-DQSZ (single hypothesis, "Hypothesis." label, with "in alternative form" qualifier):
"This leads to the following hypothesis (in alternative form):
 Hypothesis.
 Clients of signatory auditors with tax expertise exhibit less tax aggressiveness than
 clients of signatory auditors without tax expertise."

26-KLYY (3 hypotheses with paired sub-hypotheses, "H1.", "H2(a).", "H2(b).", etc.):
"Thus, we state our first hypothesis, in the alternative form, as follows:
 H1.
 Audit partners' cultural trust is negatively associated with the likelihood of issuing
 going concern opinions, ceteris paribus."
```

### Formal H statement — required ingredients (in order)

1. **Bridge sentence** — varies by paper, but ALL 5/6 (template) (excluding 16-DLZ) use one of:
   - "Based on the above arguments we posit the following hypothesis [in the alternative form]:"
   - "This leads to the following hypothesis (in alternative form):"
   - "Therefore, we form the following hypothesis."
   - "Thus, we state our [first/second/third] hypothesis, in the alternative form, as follows:"
   - "We state our [N-th] hypothesis as the following pair of predictions:"

2. **Label** — bold or italic, on its own line:
   - "Hypothesis." (single-H papers, 24-DLWW / 24-DHXZ / 25-DQSZ)
   - "Hypothesis 1." / "Hypothesis 2." (multi-H, older 07-DHT style)
   - "H1." / "H2(a)." / "H2(b)." / "H3(a)." / "H3(b)." (modern multi-H, 26-KLYY style)

3. **Hypothesis content** — declarative sentence stating predicted direction:
   - "[Subject] is [positively / negatively] associated with [outcome], ceteris paribus."
   - OR "[Subject] [verb] more / less [outcome] than [comparison]."
   - OR "Auditors with [X] are associated with [higher / lower] [outcome]."

4. **"ceteris paribus"** appears in 1/6 (template) papers (26-KLYY uses it on every H; older papers omit it).

### When to omit a formal H statement

`(16-DLZ)` was the original-corpus **outlier** — its Section 2 ("Research Issues") never states a numbered formal hypothesis. Instead, it concludes with a directional but non-formal sentence pair:

> "Therefore, if conservative clients impose less (more) risk, then we expect auditors to issue fewer (more) GCOs."
> "Therefore, if conservative clients impose less (more) risk, then we expect auditors to resign less (more) frequently."

**Use this style only if:** (a) target is TAR/JAR/RAST and the published comparator supports it, (b) prediction direction is genuinely ambiguous and you want to test multiple outcomes, (c) the paper is RQ-only / "what matters" / concordance-measurement / mixed-methods, or (d) the theory is deliberately unsigned and the identification design will adjudicate the direction.

**Modern JAE papers (2024+) still usually state at least one formal "Hypothesis." or "H1." block.** The Stage-1 pilot shows exceptions outside that narrow modern-JAE lane: `19-JWW` and `20-CKMS` use narrative / RQ-style theory sections, `23-ACN` uses formal RQs, `24-DGZZ` ends with an empirical-question resolution, and `22-FHKF` uses "Prediction 1/2/3."

### "in alternative form" — when to include it

The phrase "in alternative form" / "in the alternative form" appears in:
- 07-DHT (every hypothesis): "stated in alternative form" / "stated again in alternative form"
- 24-DLWW: "we posit the following hypothesis in the alternative form"
- 25-DQSZ: "the following hypothesis (in alternative form)"
- 26-KLYY: "we state our first hypothesis, in the alternative form"
- 24-DHXZ: omits — uses "we form the following hypothesis"
- 16-DLZ: omits — no formal H

**Default:** include "in the alternative form" or "(in alternative form)" — it is the safer DeFond convention. Omit deliberately when the section uses a null-form H (`23-PSZ`, `23-ZBLM`, `24-Chen`), RQ-only framing (`23-ACN`), narrative prediction (`19-JWW`, `20-CKMS`, `22-LNS`, `24-DGZZ`), or RAST-style "Prediction" labels (`22-FHKF`). Never omit silently.

---

## Move 5: Sub-hypothesis decomposition (multi-H papers)

### When to split into multiple hypotheses

| Trigger | Example |
|---|---|
| Different outcomes from same treatment | 26-KLYY: trust → GC opinion likelihood (H1) vs. trust → Type I/II accuracy (H2) vs. trust → financial reporting quality (H3) |
| Different treatments for same outcome | 07-DHT: 4 country-level institutions → earnings announcement informativeness |
| Pair-wise predictions from same theory | 26-KLYY: H2(a) Type I error vs. H2(b) Type II error — same partner trait, opposite directions |

### Sub-section ordering principles (from 26-KLYY)

26-KLYY orders its 5 hypotheses (H1, H2a, H2b, H3a, H3b) using the following logic:

1. **Foundational H first.** H1 (the going-concern likelihood prediction) is the simplest "first-order" association. All later hypotheses are conditional on H1.
2. **Mechanism-decomposition next.** H2(a) and H2(b) decompose H1 into Type I vs Type II errors, asking "what kind of error reduction explains H1?"
3. **Boundary / cost analysis last.** H3(a) and H3(b) ask "but what does the same trait do in a different audit dimension (within-GAAP vs GAAP-violating earnings management)?"

The arc moves from **broad → specific → boundary**.

### Pair-prediction format (the H2(a)/H2(b) device)

When predictions are competing, use the pair format (26-KLYY innovation):

```
H2(a). [Subject] is [predicted direction] associated with [outcome A], ceteris paribus.
H2(b). [Subject] is NOT associated with [outcome B], ceteris paribus.
```

Pair-predictions allow you to:
- **Reject the naïve interpretation** (e.g., "trusting auditors are gullible")
- **Sharpen identification** — supporting H2(a) AND H2(b) simultaneously is harder than just supporting a single direction

This is the most surprising and modern device in the corpus. It is **not** present in 07-DHT or 24-DLWW.

### Cross-sectional preview paragraph (multi-H bridge)

26-KLYY uses a single paragraph at the end of Section 2.2.2 to preview cross-sectional tests:

> "In H2(a) and H2(b), we focus on the average effect of audit partner trust and predict that audit partner trust reduces Type I errors with minimal impact on Type II errors. However, we do not expect the effects of audit partner trust to hold uniformly across all engagements. Therefore, we perform a number of cross-sectional tests to shed light on the specific conditions in which these predictions hold. First, we examine whether the reduction in Type I errors is primarily observed in settings where audit partners tend to be more conservative…"

Pattern: state main H is "average effect" → acknowledge heterogeneity → preview cross-sectional axis. Bridges H section to research design.

---

## Length patterns

### Word counts by paper (approximate, hypothesis section only)

| Paper | Section | Word count | Paragraphs | H count |
|---|---|---|---|---|
| 07-DHT | Section 2 | ~1,400 | 8 | 4 |
| 16-DLZ | Section II ("Research Issues") | ~2,500 | 10 | 0 (informal) |
| 24-DLWW | Section 2 | ~900 | 6 | 1 |
| 24-DHXZ | Sections 2 + 3 (combined) | ~1,800 | 11 | 1 |
| 25-DQSZ | Section 2 (incl. motivation 2.1, setting 2.2, lit 2.3, etc.) | ~3,200 | 18 | 1 |
| 26-KLYY | Section 2 | ~2,500 | 13 | 5 |

**Median:** ~2,200 words / 11 paragraphs.
**Range:** 900–3,200 words.

### Calibration heuristic

- **Short H section (~900–1,400 words):** when the theory chain is well-established and the contribution is empirical. Use 24-DLWW as template.
- **Medium H section (~1,800–2,500 words):** default for partner-trait or cultural papers; multi-hypothesis papers fit here. Use 26-KLYY as template.
- **Long H section (~3,000+ words):** when the H section also covers institutional setting, prior literature review, AND hypothesis. 25-DQSZ does this because it combines "Motivation and Hypothesis development." Use only when journal/topic demands extensive setup.

### Length per move (median for single-H papers)

| Move | Median words | Range |
|---|---|---|
| 1. Anchor (theory + literature) | 350 | 200–800 |
| 2. Mechanism (FOR argument) | 500 | 300–900 |
| 3. Tension (counter-arguments) | 250 | 150–500 |
| 4. Formal H statement (incl. bridge) | 50 | 30–100 |
| **Total** | **~1,200** | **900–2,200** |

---

## Verb / phrase whitelist for hypothesis development

### Theory anchor verbs

- "Prior research finds that…" / "Prior literature finds that…"
- "A growing literature in [X] shows…"
- "Economic theories of [X] suggest…"
- "Drawing on prior research in [X], we…"
- "Building on this line of research, we…"
- "Following [Authors] (year), we…"
- "[Authors] (year) document that…"
- "[Authors] (year) argue that…"

### Mechanism / argument verbs

- "We argue that…"
- "We posit that…"
- "We expect [X] to…"
- "[X] should [Y]" — the workhorse mechanism phrase
- "The above arguments suggest that…"
- "This is consistent with…"
- "We extend [X] by examining…"
- "We conjecture that…"

### Tension / counter-argument verbs

- "However, there are reasons why…"
- "However, there are several reasons why this relation may not hold empirically."
- "While [X] should [Y], it also…"
- "We emphasize that there is tension in our prediction."
- "We note, however, that…"
- "Conversely, if [X], then…"
- "On the other hand, …"
- "Another reason why [X] may [opposite] is…"

### Bridge to formal hypothesis

- "Based on the above arguments we posit the following hypothesis in the alternative form:"
- "This leads to the following hypothesis (in alternative form):"
- "Therefore, we form the following hypothesis."
- "Thus, we state our [Nth] hypothesis, in the alternative form, as follows:"
- "We state our [Nth] hypothesis as the following pair of predictions:"
- "We formalize this hypothesis as follows, stated in alternative form:"
- "Our [Nth] hypothesis is therefore as follows, stated again in alternative form:"

### Hypothesis-statement verbs (the H sentence itself)

- "is [positively / negatively] associated with"
- "are associated with [higher / lower] [Y]"
- "exhibit [more / less] [Y]"
- "have more [informative / accurate] [Y]"
- "is not associated with [Y]" (for null pair-predictions like H2(b), H3(b))
- "provide higher (lower) quality [Y]"

---

## Forbidden moves

The corpus contains **zero** instances of these:

- ❌ **"We will show that…"** — begs the empirical question; substitute "We hypothesize that…"
- ❌ **"We expect to find that…"** — semantically empty; substitute "We expect [X] to…"
- ❌ **"We will demonstrate that…"** — overclaims pre-data; substitute "We posit that…"
- ❌ **"Common sense suggests…"** — no theory; cite a paper
- ❌ **"It is obvious that…"** / "Clearly…" / "Obviously…" — style violation
- ❌ **"It is well-known that…"** without citation — assumes consensus
- ❌ **"Anecdotal evidence indicates…"** — not citation-grade
- ❌ **"In the real world…"** — break in academic register
- ❌ **Hypothesis stated as a question** ("Do auditors with X provide higher Y?") — H must be a declarative prediction
- ❌ **Hypothesis stated as null** ("There is no association between X and Y") — H is always the directional alternative; the null is implicit
- ❌ **No tension paragraph** — if your H is one-sided, you have not thought enough
- ❌ **"Simple" / "trivial" / "intuitive"** as adjectives modifying your prediction — these read as defensive
- ❌ **Stat phrases inside H** ("at the 1% level…") — stat reporting belongs in results, not in H statement
- ❌ **Future-tense "will" verbs in H** — H is a timeless association, not a future event
- ❌ **First person plural "we believe"** — substitute "we argue", "we posit", or "we hypothesize"

---

## Variable / proxy justification within H-development

Across the 6 papers, a clear pattern: **the proxy is named in the H statement and lightly justified in Move 1 or 2; the formal proxy operationalization belongs in research design.**

### Pattern A: Proxy in H sentence + 1-sentence proxy justification in mechanism

`(24-DLWW)` H states "auditors with stronger social networks". In the mechanism move, networks are defined narratively ("connections with customers… connections with suppliers…"), and a single sentence — **"In countries such as China, that rely heavily on relationship-based contracting, the auditors' ties with their clients' business community should be particularly beneficial."** — justifies why the operationalization makes sense. Detailed measurement (school ties, work ties, business vs government) goes in §3.1.

### Pattern B: Setting subsection precedes H

`(25-DQSZ)` has a dedicated **§2.2 "The advantages of the China setting"** between literature review (§2.1) and H development (§2.5). The CTA designation is justified institutionally (test rates, professional structure) before the H statement uses it.

### Pattern C: Proxy fully developed inside H section

`(24-DHXZ)` is unusual — Section 2 is "Related literature" and Section 3 is "Hypothesis development", but Section 4 has the formal "Measures of auditor industry range" subsection. The H statement uses "wide range of industry experiences" without operationalizing.

### Pattern D: Proxy = country-level institution (older style)

`(07-DHT)` justifies each country-level proxy (CIFAR index, Bhattacharya-Daouk insider trading dummy, etc.) in 1–2 sentences immediately after the H statement, using the form **"We measure [construct] using [source/measure] from [authors]…"**.

### Rule of thumb

- **Top-3 modern style (2024+):** name the construct in H, give 1–3 sentences in mechanism on why your proxy captures it, defer measurement details to research design.
- **Avoid:** putting the full measurement equation inside the H section. If your section has math, you have over-specified.

---

## Bridging from intro to hypothesis section

How do papers transition from the end of the introduction to the start of Section 2? The 6 papers fall into 3 styles:

### Style 1: No bridge sentence, clean section break (3/6 (template))

The Section 2 opener does not reference the introduction. It begins **inside the literature**, identical to a fresh start. Examples:

- `(24-DLWW)` §2.1: "Prior literature finds that auditors who are socially connected to their client's executives…"
- `(24-DHXZ)` §3 (note: numbering different): "A growing literature in economics, finance, and accounting shows…"
- `(26-KLYY)` §2.1: "The traditional approach in economics, finance, and accounting…"

### Style 2: Section-internal "in this section we…" preamble (2/6 (template))

Use a 2–3 sentence Section 2 preamble before the first sub-section:

- `(07-DHT)` §2 (before §2.1): "Recent research on investor protection institutions has several implications for the structural factors in countries' financial reporting environments that are likely to influence how investors respond to earnings announcements. **In this section we appeal to this literature to identify those factors…**"
- `(26-KLYY)` §2.2 (before §2.2.1): "**In this study, we examine the role of cultural trust in the auditing setting**, focusing on how audit partners' cultural trust influences the likelihood and accuracy of their going concern opinions and their clients' financial reporting quality."

### Style 3: First sub-section IS the bridge (1/6 (template))

`(25-DQSZ)` has §2.1 "Motivation and background" — this section is essentially a literature-review bridge that re-narrates what the introduction said about the relevant tax-expertise and NAS-conflict studies (`[AUTHOR:]`). The H is then introduced in §2.5.

### Recommendation

For a modern single-hypothesis partner-trait paper, use **Style 1** (clean break, start inside literature). For a multi-hypothesis paper with shared theory, use **Style 2** (Section preamble).

---

## Annotated example: 26-KLYY hypothesis development (multi-H modern template)

This is the single best structural template for a multi-hypothesis partner-trait paper. Move-by-move annotation:

| ¶ | Verbatim opening | Move |
|---|---|---|
| §2.1 ¶1 | "The traditional approach in economics, finance, and accounting is to take individual beliefs and preferences as exogenous…" | **Move 1: Theory umbrella** — establishes Bisin-Verdier cultural transmission framework |
| §2.1 ¶2 | "To illustrate the basic features of these models, consider the following example. Suppose that there are two attitudes in the population: a and b…" | **Move 1 cont.** — concrete example to make theory tangible |
| §2.1 ¶3 | "Cultural trust has been documented in many settings (e.g., Dohmen et al., 2012)…" | **Move 1 cont.** — empirical evidence FOR the theory's broad applicability |
| §2.1 ¶4 | "Our work also complements research that investigates the consequences of cross-country differences in trust…" | **Move 1 cont.** — distinguishes from cross-country studies (epidemiological approach justification) |
| §2.2 ¶1 | "In this study, we examine the role of cultural trust in the auditing setting, focusing on how audit partners' cultural trust influences the likelihood and accuracy of their going concern opinions and their clients' financial reporting quality." | **Move 2: Bridging paragraph** for all sub-hypotheses |
| §2.2.1 ¶1 | "Under PCAOB AS 2415, auditors are required to assess their client's ability to continue to operate…" | **Sub-anchor for H1** — institutional grounding |
| §2.2.1 ¶2 | "Following prior research, we conceptualize trust as the subjective probability that an agent assigns…" | **Mechanism for H1** — links trust → believing management → no GC opinion |
| §2.2.1 ¶3 | "**H1.** Audit partners' cultural trust is negatively associated with the likelihood of issuing going concern opinions, ceteris paribus." | **Formal H1** |
| §2.2.1 ¶4 | "However, there are several reasons why this relation may not hold empirically. First, … Second, … Third, …" | **Tension for H1** — three numbered counter-arguments |
| §2.2.2 ¶1 | "To further assess how cultural trust influences audit partners' going concern opinions, we next examine how audit partners' cultural trust relates to Type I errors and Type II errors." | **Sub-anchor for H2** — refines H1 question |
| §2.2.2 ¶2 | "We argue that these two potential outcomes depend on how audit partners approach professional skepticism." | **Mechanism for H2(a)/H2(b)** — Nelson presumptive doubt vs neutrality |
| §2.2.2 ¶3 | "At the same time, we argue that audit partners' cultural trust does not necessarily translate to 'naïve' acceptance of management's assertions…" | **Tension for H2(b)** — explains why trust does NOT imply Type II errors increase |
| §2.2.2 ¶4 | "**H2(a).** Audit partners' cultural trust is negatively associated with the likelihood of Type I errors, ceteris paribus. **H2(b).** Audit partners' cultural trust is not associated with the likelihood of Type II errors, ceteris paribus." | **Pair-prediction H2** |
| §2.2.2 ¶5 | "In H2(a) and H2(b), we focus on the average effect…" | **Cross-sectional preview** — bridges to research design |
| §2.2.3 ¶1 | "Thus far, our hypotheses suggest that audit partners' cultural trust can attenuate excessive conservatism…" | **Sub-anchor for H3** — recaps prior H, signals new direction |
| §2.2.3 ¶2 | "We argue that trusting audit partners may facilitate greater within-GAAP earnings management… However, we do not expect that cultural trust extends to tolerating violations of GAAP…" | **Mechanism + tension for H3(a)/H3(b)** |
| §2.2.3 ¶3 | "**H3(a).** Audit partners' cultural trust is positively associated with within-GAAP earnings management, ceteris paribus. **H3(b).** Audit partners' cultural trust is not associated with earnings management that violates GAAP, ceteris paribus." | **Pair-prediction H3** |

**Key takeaways from 26-KLYY for a similar partner-trait paper:**

1. The shared theory umbrella (§2.1) does the heavy citation lifting. It is ~4 paragraphs and cites 8–10 papers.
2. Each sub-section (§2.2.1, §2.2.2, §2.2.3) is short — 3–5 paragraphs each.
3. **Pair predictions (H2a/H2b, H3a/H3b) are used to claim that the trait operates with discrimination**, not naively. This is the central rhetorical move that makes the contribution feel non-obvious.
4. Tension is placed BEFORE the H for H1 (entire ¶ after H1), but woven INTO the mechanism for H2 and H3.
5. No proxy operationalization in Section 2; defers to §3.

---

## Annotated example: 24-DLWW hypothesis development (single-H modern template)

This is the cleanest single-H template. Note its **two-sub-section split** — §2.1 makes the FOR argument, §2.2 makes the AGAINST argument, then a bare "Hypothesis." statement.

| ¶ | Verbatim opening | Move |
|---|---|---|
| §2.1 (titled "Auditors' social networks and auditor competency") ¶1 | "Prior literature finds that auditors who are socially connected to their client's executives and audit committee chairs, provide lower quality audits…" | **Move 1: Literature anchor** + gap statement ("the effects of auditors' connections with members of their clients' larger business community have not been explored") |
| §2.1 ¶2 | "We extend the research that examines auditors' social ties by examining auditors' social connections to their clients' business communities. Strong connections within their clients' communities should increase an auditor's competency…" | **Move 2: Mechanism FOR** — 3 parallel "Connections with X" examples (customers / suppliers / bankers) |
| §2.1 ¶3 | "In countries such as China, that rely heavily on relationship-based contracting, the auditors' ties with their clients' business community should be particularly beneficial…" | **Move 2 cont.** — China-setting justification + `[AUTHOR:]` network theory |
| §2.1 ¶4 | "The above arguments suggest that signatory auditors with extensive network connections within their clients' business community should be more competent in assessing the risk of financial misreporting…" | **Move 2 closer** — summary of FOR argument |
| §2.2 (titled "Auditors' social networks and threats to auditor independence") ¶1 | "While strong ties within their clients' community should increase auditor competency, it also threatens auditor independence, because…" | **Move 3: Tension** — independence threat |
| §2.2 ¶2 | "However, auditors also have strong incentives to maintain their independence, because failure to do can impose costs on the auditor…" | **Move 3 cont.** — counter-counter-argument; `[AUTHOR:]` reputation/career-cost mechanism |
| §2.2 ¶3 | "Thus, the auditors' network relationships might essentially serve as a collateral bond that incentivizes the auditor to remain independent." | **Move 3 closer** — `[AUTHOR:]` quasi-rent reframing |
| §2.2 ¶4 | "Based on the above arguments we posit the following hypothesis in the alternative form: **Hypothesis.** Chinese engagement auditors with stronger social networks in their clients' communities provide higher quality audits." | **Move 4: Formal H** |

**Key takeaways from 24-DLWW for a similar single-H paper:**

1. Splitting H section into "FOR" and "AGAINST" sub-sections (§2.1, §2.2) is a **legitimate organizational alternative** to mechanism→tension within one section. Use this when the FOR and AGAINST arguments are roughly equal in weight.
2. Even within the AGAINST section, the paper introduces a counter-counter-argument (auditors have incentives to remain independent) before the H. This 3-stage dialectic — for, against, but-wait — is more sophisticated than a binary for/against.
3. The H statement is single-sentence and bare. No "ceteris paribus" qualifier (older convention).
4. Total length: ~900 words. This is **the short end** of the range and works because the theory chain (social networks → competence) is well-established.

---

## Stage-1 Phase-C pilot digest (16 archival papers; 2026-05-21)

The full annotated row tables for these 16 pilot sections live as staging files named `<code>_hypothesis.md` in the Track B drafts directory. This pattern file stores the distilled guidance: which structural variants are reusable, which old rules need re-counting, and which examples to retrieve when drafting.

`22-HS` was rejected as survey-methodology and replaced by `16-DLLN` per the archival-only scope rule.

| Code | Section type | H / RQ format | Reusable pattern | Rule implication |
|---|---|---|---|---|
| `19-JWW` | TAR background / related lit | No formal H; RQ restatement | Institutional-exogeneity defense + comparator differentiation chain | No-formal-H can work when identification, not theory, carries the paper |
| `22-LNS` | TAR background / research question | Narrative prediction | Three-reason FOR mechanism; thin "Nevertheless" tension | Tension can be embedded in the closer, but this is weaker than canonical M4 |
| `23-ACN` | TAR research questions | RQ1-RQ4 | Role-decomposition RQs + credence-goods fee RQs | RQ-only is legitimate for "what matters" exploratory production papers |
| `20-WY` | JAR multi-H | H1-H4 colon labels | Two-channel audit-risk scaffold + post-H tension | Intro M4 omission can be repaired in Section 2 |
| `22-CHLP` | JAR single-H | "Hypothesis 1:" inline | Four-prior anchor chain + post-H four-mechanism tension | Directional H plus empirical-question hedge is a valid hybrid |
| `22-Dug` | JAR single-author narrative | "I predict" narrative | Public-good / moral-hazard theory + four-reason counter block | Single-author JAR can use "I"; formal H block not always needed |
| `23-ZBLM` | JAR single null-H | Null-form H1 | Four-issue specialist-use tension enumeration | Null-form H is valid when net effect is genuinely ambiguous |
| `24-Chen` | JAR single-author two-H | Two null-form Hs | Employer-reputation theory + three-channel mechanism | Null-form H can be explicit: "I state my hypothesis in null form" |
| `24-DGZZ` | JAR no-formal-H | Empirical-question closer | Head-placed M4 + four-perspective mechanism walk | Tension may be declared before mechanisms, then developed in parallel |
| `19-Aob` | JAE concordance / measurement | No formal H | Three-advantage FOR enumeration + data-source-specific tensions | Measurement-concordance papers can replace H with prediction framework |
| `19-BGH` | JAE multi-H | H1 + H2a/H2b/H2c | H1 decomposed into monitoring / knowledge / resource channels | Conditional-strength sub-Hs are a clean way to unpack a mechanism |
| `20-CKMS` | JAE theory framework | Narrative central hypothesis | Credence-good reputation theory + portfolio-screening prediction | "Central hypothesis" narrative can substitute for H block, but M4 is absent |
| `16-DLLN` | JAE multi-H | Hypothesis 1-5 | Lit-only multi-H; tension converted into moderators | Older JAE permits no shared theory umbrella and no ceteris paribus |
| `23-PSZ` | JAE single-H | Bare `H:` null form | Symmetric FOR/AGAINST competition theory | Null H is acceptable when theory is balanced and design adjudicates sign |
| `22-FHKF` | RAST mixed-methods | Prediction 1-3 | Interview synthesis converted into predictions | Mixed-methods papers may use "Prediction" labels, not H labels |
| `22-FW` | RAST multi-H | H1/H2a/H2b/H3 colon labels | Three-reason FOR + three-reason AGAINST symmetry | Symmetric 3-vs-3 mechanism/tension is a strong template |

### New reusable variants surfaced by the pilot

1. **Formal-H is not binary.** The expanded corpus now has displayed H blocks, inline colon Hs, null-form Hs, narrative predictions, formal RQs, and "Prediction" labels. Use displayed directional Hs for the DeFond/JAE default; use the alternatives only when the paper's own theory is unsigned, exploratory, or mixed-methods.
2. **Tension has at least six shapes.** Canonical single paragraph; three-reason enumeration; four-issue enumeration; symmetric FOR/AGAINST architecture; head-placed M4 before mechanisms; and tension-as-moderator. "No tension" is now observed, but should be treated as a risky exception, not a template.
3. **Three-numbered devices work on both sides.** The original corpus highlighted the three-reason counter-argument (`26-KLYY`). Pilot papers also use three-reason FOR mechanisms (`22-LNS`, `24-Chen`) and symmetric three-vs-three mechanism/tension (`22-FW`).
4. **RQ-only is a distinct family, not a failure.** `19-JWW`, `23-ACN`, and `24-DGZZ` document archival audit papers that develop research questions or empirical-question resolutions instead of directional Hs. This works best when the design is the contribution and the theory is deliberately unsigned.
5. **Null-form Hs need explicit justification.** `23-PSZ`, `23-ZBLM`, and `24-Chen` use null Hs because the net effect is theoretically ambiguous. Do not state a null H merely to sound conservative; the preceding section must make the ambiguity visible.
6. **Mixed-methods H sections need separate treatment.** `22-FHKF` uses partner interviews as the bridge from literature to predictions. This is acceptable for RAST-style mixed-methods evidence, but is not the default for JAE/TAR archival-only papers.

### Drafting retrieval guide

| If your paper has... | Retrieve |
|---|---|
| partner trait with asymmetric errors | `26-KLYY` |
| single-H competence vs independence tradeoff | `24-DLWW` |
| audit-labor / talent channel | `24-Chen` or `22-LNS` |
| no signed prediction because mechanisms balance | `23-PSZ`, `23-ZBLM`, or `24-DGZZ` |
| multiple mechanism channels under one treatment | `19-BGH`, `20-WY`, or `22-FW` |
| measurement-concordance / proxy-validation framing | `19-Aob` |
| production / "what matters" exploratory RQs | `23-ACN` |
| mixed-methods technology evidence | `22-FHKF` |
| M&A shared-auditor setting | `16-DLLN` |
| two-sided auditor-client matching theory | `20-CKMS` |

---

## Self-audit checklist (15 items)

Before finalizing a hypothesis development section, verify:

- [ ] Section 2 opens with a theory anchor or literature anchor (Move 1), not with motivational rhetoric or anecdote
- [ ] At least one anchor citation is from outside accounting (psychology, economics, sociology, neuroscience) — modern style requires this for non-replication papers
- [ ] Mechanism move uses 2–4 concrete parallel examples ("connections with customers… with suppliers… with bankers…"), not abstract claims only
- [ ] Mechanism verbs are from the whitelist ("We argue…", "We posit…", "X should Y") — none from blacklist ("We will show", "obviously", "common sense")
- [ ] At least one explicit tension paragraph exists, opening with "However, …" / "While …, also" / "We emphasize that there is tension"
- [ ] Tension cites at least 2 distinct counter-mechanisms (not just hedging language)
- [ ] Bridge sentence to H uses one of the canonical phrases ("Based on the above arguments we posit…", "This leads to the following hypothesis…")
- [ ] H statement uses the "in the alternative form" qualifier (or omits it deliberately for non-directional H)
- [ ] H statement is declarative, directional, single sentence, with verb "is associated with" or equivalent
- [ ] H statement does NOT contain stat language, future tense "will", or proxy operationalization details
- [ ] If multi-H, sub-hypotheses are ordered foundational → mechanism-decomposition → boundary
- [ ] If using pair predictions (H2(a)/H2(b)), the second prediction is "is not associated with" (null) and is justified by an asymmetric cost argument
- [ ] Length: single-H section ~1,000–1,500 words; multi-H section ~2,000–3,000 words. Anything outside this range needs a reason.
- [ ] Proxy is named in H but not operationalized in Section 2; measurement details deferred to research design
- [ ] If targeting JAE/TAR, formal "Hypothesis." or "H1." block is present and displayed (not inline). 16-DLZ TAR-style absence is permissible only with deliberate justification.

---

## Quick-reference comparison table

| Dimension | 07-DHT | 16-DLZ | 24-DLWW | 24-DHXZ | 25-DQSZ | 26-KLYY |
|---|---|---|---|---|---|---|
| Hypothesis count | 4 | 0 (informal) | 1 | 1 | 1 | 5 (1 + 2 pairs) |
| Section title | "Hypothesis development" | "Research Issues" | "Hypothesis development" | "Hypothesis development" | "Motivation and Hypothesis development" | "Literature review and hypothesis development" |
| H label format | "Hypothesis 1." | none | "Hypothesis." | "Hypothesis." | "Hypothesis." | "H1." / "H2(a)." / "H2(b)." / "H3(a)." / "H3(b)." |
| "in alternative form" qualifier | YES (every H) | n/a | YES | NO | YES | YES |
| "ceteris paribus" in H | NO | n/a | NO | NO | NO | YES (every H) |
| Anchor type | Literature | Theory + Auditing handbook | Literature | Theory (psychology/cognitive) | Literature + Setting | Theory + Literature |
| Tension placement | per-H | within-section | dedicated §2.2 | within ¶ | post-H ("we emphasize") | post-H1, woven for H2/H3 |
| Pair predictions | NO | NO | NO | NO | NO | YES (H2 + H3) |
| Cross-sectional preview | NO | YES (sub-section "Auditors' Strategic Responses") | NO | NO | NO | YES (post-H2) |
| Word count | ~1,400 | ~2,500 | ~900 | ~1,800 | ~3,200 | ~2,500 |

---

## Most surprising / actionable findings

1. **The pair-prediction format (H2(a)/H2(b), H3(a)/H3(b)) is a 2026 innovation in 26-KLYY** that does NOT appear in any of the older corpus papers. It is a direct response to the "naïve trust" critique a reviewer would raise. Any partner-trait paper should consider this device whenever the trait could be read pejoratively (gullibility, capture, cynicism, tribalism, etc.).

2. **16-DLZ is the original TAR-era outlier** — it deliberately avoids a numbered formal hypothesis. This works for TAR but would likely draw a referee complaint at JAE. If targeting JAE/JAR, do NOT model the H section after 16-DLZ without a deliberate reason.

3. **Tension placement varies more than the existence of tension.** 50% of papers put tension BEFORE the H statement (more common in old style), 50% put it AFTER ("We emphasize that there is tension in our prediction" — modern style, 25-DQSZ). The post-H placement is harder to do well but signals greater confidence.

4. **Modern (2024+) JAE papers all import theory from outside accounting.** 24-DHXZ uses cognitive psychology, 24-DLWW uses Granovetter sociology + Klein-Williamson contract theory, 25-DQSZ uses Donohoe-Knechel auditing complexity theory + Bianchi-McGuire NAS-conflict, 26-KLYY uses Bisin-Verdier cultural transmission. The single-anchor "we extend [audit lit X]" style of 07-DHT is the older convention.

5. **Proxy operationalization is firmly OUT of the H section.** 5/6 (template) papers defer measurement details to Section 3 (Research Design) or later. The H section names the construct ("social networks", "industry range", "tax expertise", "cultural trust") and provides 1–3 sentences of conceptual justification, no more.

6. **The "However, there are several reasons why this relation may not hold empirically" structure with 3 numbered counter-arguments (26-KLYY)** is the single most efficient device for handling tension when 3+ alternative explanations exist. Memorize this template.

# Consistency Review Protocol (pattern file for `audit-write-review`, CONSISTENCY mode)

**What this is.** A whole-paper **internal-consistency** audit: does the manuscript agree
with *itself*? It checks citation coverage, acronym/notation consistency, and claim parity
across sections — the class of error a section-by-section read misses. Offline and
read-only: a bundled stdlib Python script does the deterministic extraction, then you layer
judgment on the things a regex cannot decide.

> **Inspired by, but not, `jusi-aalto/crossref`.** That tool validates a bibliography
> against the live Crossref REST API. This mode deliberately uses **no network**: instead of
> checking references against the world, it checks the paper against itself (cite↔bib
> coverage, notation drift, claim parity). The shared idea is only the shape — a SKILL doc
> plus a bundled `.py`. If a user wants live DOI/author/venue validation, that is out of
> scope here (point 6 was scoped to internal + citation-coverage, offline).

This is the cheapest mode and orthogonal to the other three: a paper can score well on
substance (COMPREHENSIVE) and writing (WRITING) and still contradict itself — define a
variable one way in §3 and use it differently in §5, cite a paper that isn't in the
bibliography, or report a magnitude in the abstract that the results table doesn't support.

---

## Procedure

### Step 1 — Run the extractor (deterministic layer)

The orchestrator has already located the manuscript. Run the bundled script via `Bash`
(stdlib only — no install). Pass the `.bib` if the user has one (LaTeX projects usually do):

```bash
python scripts/consistency_check.py PAPER.tex --bib refs.bib
# or, for a structured object you can parse:
python scripts/consistency_check.py PAPER.tex --bib refs.bib --json
```

(Resolve the script path relative to this skill folder. If no `.bib` is supplied, the
citation-coverage section still runs but can only count in-text keys — say so in the report.)

The script emits four blocks:
1. **Citation coverage** — in-text `\cite*` keys vs `.bib` entry keys → **cited-but-missing**
   (a real bug) and **defined-but-unused** (worth a look).
2. **Acronyms** — used-before-defined, defined-more-than-once, used-often-but-never-spelled-out.
3. **Notation** — variable/term definitions; terms defined multiple times (possible drift).
4. **Magnitude inventory** — numeric effect sizes per section (abstract / intro / results),
   for *your* claim-parity check.

### Step 2 — Layer judgment (the model's job)

The script flags candidates; **you decide**. Read the relevant passages and resolve:

- **Notation / terminology drift.** For each term the script flags as defined-multiple-times
  (and any you notice), read both definitions: is `DAC` "discretionary accruals" in §3 and
  "abnormal accruals" in §5? Is a variable's sign or scaling described inconsistently? A
  regex can find the candidate; only you can judge whether the two definitions conflict.
- **Claim parity (abstract ↔ intro ↔ results).** Using the magnitude inventory: does the
  abstract's directional claim match the intro's magnitude and the results table? (Recall the
  suite rule: the **abstract carries no effect-size numbers** — so a number appearing there
  is itself a flag.) Does a contribution claimed in the intro actually appear in the results?
- **Citation coverage.** Confirm the script's cited-but-missing list (these will break
  compilation / leave `(?)` marks). Note defined-but-unused entries the author may want to cut.
- **Hypothesis ↔ test alignment.** Is the hypothesis stated in §2 the one actually tested in
  §4 (same variable, same direction)?

Never invent a fix that requires a citation or number you don't have — flag the gap with
`[AUTHOR: …]` and let the author resolve it. Read-only: you do **not** edit the manuscript.

---

## Report template (`consistency_review.md`)

Lead with the plain-language headline, then the specifics, then a prioritized fix list.

```markdown
# Consistency Review: [Paper Title]
**Date:** YYYY-MM-DD   **Reviewer:** audit-write-review (consistency mode)   **File:** [path]
**Bibliography:** [refs.bib | none supplied]

## Headline
[One sentence: e.g. "Two citation keys are missing from the bibliography and DAC is defined
two different ways across §3 and §5; otherwise internally consistent."]

## Citation coverage
| Check | Count | Items |
|---|:---:|---|
| In-text cite keys | N | — |
| Bibliography entries | M | — |
| **Cited but missing from .bib** | k | `key1`, `key2` |
| Defined but never cited | j | `keyA`, … |

## Notation & terminology
| Term / symbol | Issue | §A says | §B says | Verdict |
|---|---|---|---|---|
| DAC | defined twice | "discretionary accruals" (§3.1) | "abnormal accruals" (§5.2) | reconcile wording |

## Acronyms
- Used before defined: [list, with where] — define on first use.
- Used 3+ times, never spelled out: [list].

## Claim parity (abstract ↔ intro ↔ results)
- [e.g. "Abstract reports '1.8 pp' — abstracts should carry direction only; move the number
  to the intro/results."]
- [e.g. "Intro claims a 'going-concern' contribution not supported by any §4 table."]

## Prioritized fix list
1. **[Critical]** [missing-cite / contradictory-definition — would break or mislead]
2. **[Major]** [notation drift / claim mismatch]
3. **[Minor]** [unused bib entry / undefined acronym]
```

---

## Hard rules (this mode)

1. **Read-only.** The script reads; you diagnose. Neither edits the manuscript.
2. **Offline.** No network, no Crossref/DOI API — internal + cite-coverage only.
3. **Heuristic, not gospel.** The script's flags are candidates; confirm each by reading the
   passage before you report it. `[?]` items especially need a human (your) judgment.
4. **Never invent** a citation or number to "resolve" a gap — flag it `[AUTHOR: …]`.

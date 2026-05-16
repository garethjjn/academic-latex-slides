# Interview Protocol

Use this before generating any slides.

## Core questions

Collect every field below before proposing an outline:

| Field | Required choices / detail |
| --- | --- |
| Template | `MSU`, `SJTU`, or `CityU` |
| Archetype | `lecture` or `research talk` |
| Language | Chinese or English |
| Metadata | title, subtitle if any, author, institute, date |
| Audience | who they are and what they already know |
| Timing | presentation length and target slide count |
| Material readiness | full content, rough outline, or topic only |
| Learning/message goal | what the audience should remember at the end |
| Academic components | formulas, figures, references, appendix: yes/no for each |

Ask these as one compact batch when practical. If the user already supplied a field, acknowledge it and do not ask again.

## Adaptive follow-ups

### If `lecture`

Ask:

- Where does this lecture sit in the course sequence?
- What are the learning objectives?
- What prerequisites should students already know?
- Should the deck include worked examples?
- Should it include in-class exercises or discussion prompts?
- Should it include a recap / summary slide?

### If `research talk`

Ask:

- What is the research question?
- What is the contribution relative to prior work?
- What data and method are used?
- What are the core results?
- Should the deck include mechanism, robustness, or appendix slides?
- Which result is the one the audience most needs to remember?

## Material sufficiency rule

- If the user provides full content, use it.
- If the user provides a rough outline, refine structure while marking details that still need source material.
- If the user provides only a topic, create a deck skeleton and missing-materials list. Do not fabricate:
  - empirical findings
  - citation entries
  - data descriptions
  - theorem statements
  - numerical magnitudes

## Required pre-generation output

Before writing files, provide:

1. **Requirements summary**
2. **Slide-by-slide outline**
3. **Missing-materials list**

Then stop and wait for an explicit confirmation such as “approved”, “go ahead”, or equivalent.

## Approval gate

Do not generate the LaTeX project until the user has approved the outline. If they revise the outline, update it and ask for confirmation again.

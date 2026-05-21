# Draft annotated exemplar - 23-ZBLM / results (API draft)

*STATUS: DRAFT - Source PDF: paper/2023 - Zimmerman, Barr‐Pulliam, Lee, Minutti‐Meza - Journal of Accounting Research - Auditors' Use of In‐House Specialists.pdf - Source TXT: paper/2023 - Zimmerman, Barr‐Pulliam, Lee, Minutti‐Meza - Journal of Accounting Research - Auditors' Use of In‐House Specialists.txt*

## Annotated example (draft): Zimmerman, Barr-Pulliam, Lee, Minutti-Meza 2023 (`23-ZBLM`)

| Para | Quote (verbatim, <=25 words) | Block | Move | Annotation | Conf |
|---|---|---|---|---|---|
| ¶1 | "Table 2 provides descriptive analyses illustrating the use of specialists over time, by type, and by industry." | ¶1 | descriptive statistics | Opens the descriptive-statistics sub-section by signalling a table that maps specialist use across years, types, and industries. | high |
| ¶11 | "the mean incidence of Part I inspection findings and restatements related to the use of complex estimates (PART1_COMPLEX and REST_COMPLEX) are 16% and 5%, respectively.22" | ¶11 | descriptive statistics | Reports key dependent-variable means; the 16% Part I deficiency rate sets the benchmark for the primary audit-quality test. | high |
| ¶57 | "Panel A presents descriptive statistics for the main variables. Variable definitions are provided in appendix A." | ¶57 | table column/panel walk | Standard walk-through sentence for Table 3 Panel A, guiding the reader to variable listing and supporting definitions. | high |
| ¶60 | "These univariate tests provide initial evidence that the use of specialists is positively related to the incidence of audit process deficiencies." | ¶60 | primary result lead | Univariate lead that previews the direction of the main multivariate finding; functions as a bridge from descriptive statistics to the regression results. | high |
| ¶72 | "Table 5 shows our audit quality analyses (model 1) and constitutes the primary test of H1." | ¶72 | primary result lead | Canonical "Table N shows" archetype (A) opening the principal multivariate result. | high |
| ¶72 | "the use of specialists is positively and significantly associated with PART1_COMPLEX (coef. = 4.302, z-stat = 2.13) and ABSDA (coef. = 0.159, t-stat = 1.79)" | ¶72 | coefficient / significance statement | Provides exact coefficients and significance for the logit (PART1_COMPLEX) and OLS (ABSDA) models; uses z‑ and t‑statistics transparently. | high |
| ¶72 | "a sense of the economic magnitude of our findings on audit process deficiencies, using the model in column 7, we estimate an odds ratio of" | ¶72 | economic magnitude translation | Translates the coefficient into an odds-ratio interpretation; the 1.5 figure is a compact, reader‑friendly magnitude statement. | high |
| ¶72 | "However, using entropy balancing, we only find a positive and statistically significant coefficient in column 7" | ¶72 | identification / falsification | Highlights that the main result holds only after entropy balancing on the tercile partition, implicitly addressing selection-on-observables concerns. | high |
| ¶94 | "We document a positive and statistically significant coefficient on H_SPEC_USE3 only in column 1." | ¶94 | cross-section / heterogeneity | Opens the cross‑sectional analysis (board accounting expertise) by stating where the specialist-use coefficient is significant. | high |
| ¶94 | "board accounting expertise is a salient condition for better coordination between auditors and specialists in the audit of complex estimates" | ¶94 | cross-section / heterogeneity | Interprets the cross‑sectional heterogeneity; frames board expertise as a moderating mechanism, consistent with a coordination narrative. | high |
| ¶101 | "We find that the high use of specialists has a positive and statistically significant association with the likelihood of impairments in both partitions (coef" | ¶101 | mechanism / channel | Tests a specific complex-estimate channel (goodwill/intangibles impairments) to see whether specialist involvement correlates with a tangible FVM outcome. | medium |
| ¶106 | "The results in columns 1 and 2 do not show evidence that the use of specialists has a statistically significant association with the discount rate" | ¶106 | null / mixed-result handling | Transparently reports a null result for pension discount rate, avoiding over‑claiming and distinguishing the outcome from impairment findings. | high |
| ¶93 | "our findings must be interpreted with caution. Although we are among the first to document a pervasive association" | ¶93 | section closer | Cautions that the observed association is not causal; acknowledges the novel contribution while calling for further research-typical section‑closing modesty. | high |

## Commentary

This results section follows the canonical multi‑sub‑section structure common in the JAE audit‑corpus (descriptive statistics → baseline test → identification/cross‑section → mechanism/secondary outcomes → audit costs → additional tests). The paper opens with rich graphical and tabular descriptive evidence on specialist hours, then transitions to a multivariate audit‑quality model that uses both continuous and indicator‑based measures and entropy balancing to address selection. The primary lead sentence ("Table 5 shows our audit quality analyses …") is a pure Archetype‑A opener. The main result on PART1_COMPLEX is presented with both coefficient/z‑stat and an economic‑magnitude translation (odds ratio), both captured in the exemplar. Identification is approached through entropy balancing rather than a separate falsification or placebo section. The cross‑section on board accounting expertise is a classic heterogeneity test. The impairment and pension‑discount‑rate models serve as channel/component tests, with one delivering a positive result and the other a candid null. Audit‑cost models appear as a separate sub‑section (4.7) bridging to the additional analyses (4.8). The results section closes with a cautious "interpret with caution" paragraph. Overall, the structure is conventional and the moves are clearly signed.

## Self-check log

- All 13 quotes were extracted verbatim from the provided results section text.
- Each quote was checked for length; all are ≤25 words.
- Quotes use ASCII straight double quotes, no curly characters.
- Move labels align with the canonical family list (descriptive statistics, primary result lead, coefficient/significance, economic magnitude, identification/falsification, cross‑section/heterogeneity, mechanism/channel, null/mixed‑result handling, section closer, table column/panel walk).
- Block identifiers correspond to the paragraph numbers in the source.
- No invented citations, figures, or numeric magnitudes; any author references use [AUTHOR:] placeholder only in annotations where needed, but here none were required.
- Each row occupies a single physical line; no internal line breaks in table cells.

## Reviewer notes (for human)

- The paper does not have a standalone "alternative measures / fixed‑effects" sub‑section inside the results. Entropy balancing and the inclusion of audit‑firm, FF12, and year fixed effects are described within the primary model discussion, and robustness/sensitivity tests are largely relegated to the online appendix (Section 4.8 refs A1-A10). If a dedicated robustness sub‑section is expected in the inventory, this exemplar should note that the main text only flags these tests without detailed coefficient tables.
- The "mechanism / channel" move is assigned to the impairment model (Table 7) because it targets a specific complex‑estimate channel. However, the paper frames impairment as an additional outcome rather than a formal mediation. Annotators may prefer to classify it as "secondary outcome" if the pattern guide is strict about mediation structures.
- The primary‑result lead from univariate tests (¶60) is included to show how the paper uses preliminary evidence before the multivariate results; that may be redundant if the inventory prefers only the main regression opener.
- The section closer (¶93) also embeds a discussion of limitations; its cautionary tone is typical of JAE but some inventories may separate "limitations" from a pure results‑section closer.

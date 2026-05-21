# Briefing — 14-FPW (Francis, Pinnuck & Watanabe 2014, TAR) — TASK: write the RESEARCH DESIGN (§3)

You are drafting the **research design / methodology section (§3)** of this paper from facts
only. You have NOT seen the paper's own §3. Use the `audit-write-design` skill's pattern file.

## Facts (non-target-section briefing)

- **Title:** "Auditor Style and Financial Statement Comparability." Journal: TAR, 2014.
- **Research question:** does shared Big 4 audit style increase the comparability of reported
  earnings within an auditor's clientele?
- **Dependent variable (comparability):** a *pairwise* measure. For each pair of firms in the
  same industry-year, the DV captures how similar their accruals / earnings structures are.
  Construct it by comparing the firms' accrual-generating functions (regress accruals on cash
  flows / fundamentals firm-by-firm, then compare predicted accruals for the pair). Higher =
  more comparable. [PLACEHOLDER: exact estimation window / functional form if needed].
- **Independent variable of interest:** `SAME AUDITOR` — an indicator = 1 if both firms in the
  pair are audited by the same Big 4 firm (same "style"), 0 if audited by two different Big 4 firms.
- **Setting / sample:** U.S. public companies, 1987–2011; unit of analysis = firm-pair-year within
  the same industry-year; Big 4 (Big N) clients. [PLACEHOLDER: final N of firm-pairs].
- **Baseline model:** an OLS regression of pairwise comparability on `SAME AUDITOR` plus controls;
  the coefficient on `SAME AUDITOR` tests H1.
- **Controls (groups):** pairwise differences in firm fundamentals (size, leverage, growth,
  operating cash flows, loss frequency); industry-year fixed effects; [PLACEHOLDER: any
  same-industry / same-size-decile matching].
- **Standard errors:** clustered [PLACEHOLDER: by industry-year or two-way], to handle the
  non-independence of overlapping firm-pairs.

## Drafting rules
- Follow the `audit-write-design` §3 structure; apply the calibrated audit-research register.
- Use `[PLACEHOLDER: ...]` for any specific number / measure detail / citation not given above —
  do NOT fabricate. Identification machinery (rotation, shocks, falsification, FE escalation)
  belongs in §4/results, NOT here — keep §3 to DV defense, IV build, the numbered baseline
  equation, control groups, and FE + clustering.
- Output ONLY the research-design section prose (no commentary).

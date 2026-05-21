## 3. Research Design

### 3.1 Measuring Financial Statement Comparability

We measure financial statement comparability at the level of a firm pair. Comparability is an inherently relational property: a single firm's statements are not "comparable" in isolation, but only relative to those of another firm facing similar economic circumstances. We therefore construct our dependent variable, Comparability, for each pair of firms in the same industry-year, where higher values indicate that the two firms translate similar economic events into more similar accounting numbers.

We build Comparability from the firms' accrual-generating functions. For each firm we estimate the relation between accruals and the underlying economic fundamentals that generate them (cash flows and other firm fundamentals) over [PLACEHOLDER: estimation window]. We then hold the economic inputs fixed and compare the predicted accruals that each firm's estimated function would produce, so that any remaining difference reflects differences in the firms' accounting systems rather than differences in their economics. Comparability is increasing in the similarity of the two firms' predicted accruals; less similar predicted accruals indicate lower comparability. [PLACEHOLDER: exact functional form of the accrual model].

Comparability is an appealing proxy because it isolates the accounting mapping from the underlying economics. The auditor's responsibility is to assure that a client's financial statements faithfully represent its economic transactions, and a shared audit style operates precisely on this mapping. While alternative comparability proxies exist [PLACEHOLDER: cite alternative comparability measures], the pairwise accrual-based measure has the advantage of being constructed entirely from reported outputs and being defined at the unit of analysis, the firm pair, at which our hypothesis applies.

### 3.2 Measuring Shared Auditor Style

Our independent variable of interest is SameAuditor, an indicator that captures whether the two firms in a pair share an audit style. We construct SameAuditor in two steps. First, for each firm-year we identify the firm's Big 4 audit firm [PLACEHOLDER: data source for auditor identity]. Second, for each firm pair in the same industry-year we set SameAuditor equal to one if both firms are audited by the same Big 4 firm, and zero if the two firms are audited by two different Big 4 firms. The measure thus compares pairs that share a single Big 4 firm's house style against pairs spanning two distinct Big 4 styles, holding constant that both firms are audited by a large auditor.

### 3.3 Empirical Model

We test our hypothesis by estimating the following ordinary least squares (OLS) model:

> Comparability_{i,j,t} = α + β·SameAuditor_{i,j,t} + γ·Diff_{i,j,t} + Industry × Year FE + ε_{i,j,t}    (1)

where _i_ and _j_ index the two firms in a pair, _t_ indexes the year, Diff is the vector of pairwise control variables described below, and the pair belongs to a single industry-year. The coefficient of interest is β; H1 predicts β > 0, indicating that pairs sharing the same Big 4 audit style report more comparable earnings than pairs audited by two different Big 4 firms. All variables are defined in Appendix A.

### 3.4 Controls, Fixed Effects, and Clustering

Because the unit of analysis is a firm pair, every control is measured as a pairwise characteristic of the two firms rather than as a single-firm attribute. We group the controls into two categories. The first category comprises pairwise differences in client characteristics: the difference between the two firms in size, in the debt-to-assets ratio, in growth, in operating cash flows, and in loss frequency. We include these client-level controls because two firms that are more alike in their underlying economics will tend to report more comparable accounting numbers regardless of their auditors, and we want SameAuditor to capture the incremental role of shared style. The second category comprises industry characteristics that affect comparability across the pair; we absorb these industry-level controls through the fixed-effect structure described next. [PLACEHOLDER: any additional client-level attributes used as pairwise differences].

We include industry-year fixed effects so that each firm pair is compared only with other pairs drawn from the same industry in the same year, absorbing industry-wide and time-varying shocks to comparability. [PLACEHOLDER: any same-industry / same-size-decile matching applied to form the pairs]. Standard errors are clustered [PLACEHOLDER: by industry-year or two-way] to account for the non-independence of overlapping firm pairs, since each firm appears in many pairs within its industry-year.

### 3.5 Sample Construction

Our sample period is 1987 through 2011 and covers U.S. public companies audited by Big 4 (Big N) firms. The unit of observation is the firm-pair-year, formed by pairing firms within the same industry-year. We begin with [PLACEHOLDER: starting universe of firm-years], from which we form all eligible within-industry-year firm pairs. We exclude [PLACEHOLDER: pairs with missing data needed to construct Comparability], [PLACEHOLDER: pairs with missing pairwise control data], and [PLACEHOLDER: any further filters]. The final sample comprises [PLACEHOLDER: final N] firm-pair-year observations across [PLACEHOLDER: number of unique firms] unique firms over the period 1987 to 2011. Variable definitions are provided in Appendix A.

### 3.6 Descriptive Statistics

Table 1 reports descriptive statistics for the variables used in Equation (1). [PLACEHOLDER: mean and standard deviation of Comparability]. [PLACEHOLDER: proportion of firm pairs for which SameAuditor equals one]. [PLACEHOLDER: means and standard deviations of the pairwise difference controls]. Table 2 reports the pairwise correlations among these variables. [PLACEHOLDER: sign and magnitude of the correlation between SameAuditor and Comparability].

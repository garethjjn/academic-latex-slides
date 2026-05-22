# Model comparison: results-draft task

Generated: 2026-05-21T20:59:21
Papers: 23-PSZ, 22-FHKF  |  temp=0.2  max_tokens=16384
Gate thresholds: >= 12 quotes, <= 25 words/quote

| Paper | Model | Latency | Out chars | Quotes | Prompt tok | Compl tok | Contract | Quote gate | Lint |
|---|---|--:|--:|--:|--:|--:|---|---|---|
| 23-PSZ | qwen3.7-max | 22s | 5916 | 12 | 10495 | 4290 | OK | OK | FAIL |
| 22-FHKF | qwen3.7-max | 33s | 6427 | 12 | 10661 | 6448 | OK | OK | OK |

## Gate details
- **23-PSZ / qwen3.7-max** -> `23-PSZ__qwen3.7-max.md`
  - quote: 12/12 quotes verified against paper/2023 - Pan, Shroff, Zhang - Journal of Accounting and Economics - The Dark Side of Audit Market Competition.clean.txt
  - lint: lint_style: 1 ERROR(s), 0 WARN(s) — FAIL
- **22-FHKF / qwen3.7-max** -> `22-FHKF__qwen3.7-max.md`
  - quote: 12/12 quotes verified against paper/2022 - Fedyk, Hodson, Khimich, Fedyk - Review of Accounting Studies - Is Artificial Intelligence Improving the Audit Process.clean.txt
  - lint: lint_style: 0 ERRORs, 0 WARN(s) — OK

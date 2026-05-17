# Academic LaTeX Slides

> 一个“先访谈、后生成”的智能体技能:把一场报告变成可直接编译的、
> 模块化的 LaTeX Beamer 工程 —— 且绝不杜撰学术内容。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Engine: XeLaTeX](https://img.shields.io/badge/engine-XeLaTeX-blue.svg)](#环境要求)
[![Scaffold: Python 3.8+](https://img.shields.io/badge/scaffold-Python%203.8%2B-3776ab.svg)](#脚手架脚本独立使用)
[![Hosts: Claude Code · Codex](https://img.shields.io/badge/hosts-Claude%20Code%20%C2%B7%20Codex-8a3ffc.svg)](#安装)

[English](README.md) · **简体中文**

`academic-latex-slides` 是一个可移植技能:既能作为独立技能安装到 **Codex**,
也能作为插件分发到 **Claude Code**。它只把一件事做好:**在写任何内容之前先
访谈你**,然后生成一份可立即编译的模块化 Beamer 演示文稿。

它的核心铁律:**绝不为了填充篇幅而编造结果、引用、数据或论断。** 如果你
手头只有一个题目,它会产出结构、占位符,以及一份明确的“缺失材料清单”——
而不是一份自信却错误的演示文稿。

---

## 目录

- [功能特性](#功能特性)
- [为什么先访谈](#为什么先访谈)
- [环境要求](#环境要求)
- [仓库结构](#仓库结构)
- [安装](#安装)
  - [Claude Code](#claude-code)
  - [Codex](#codex)
  - [构建可移植 ZIP 包](#构建可移植-zip-包)
- [使用](#使用)
  - [工作流程](#工作流程)
  - [访谈内部机制](#访谈内部机制)
  - [演示文稿蓝图](#演示文稿蓝图)
  - [端到端示例](#端到端示例)
  - [生成的项目结构](#生成的项目结构)
  - [编译演示文稿](#编译演示文稿)
- [脚手架脚本(独立使用)](#脚手架脚本独立使用)
- [模板变体](#模板变体)
- [故障排查](#故障排查)
- [开发与维护](#开发与维护)
- [适用范围](#适用范围)
- [致谢](#致谢)
- [许可证](#许可证)

---

## 功能特性

- **两种演示文稿原型** —— `lecture`(教学讲课)与 `research talk`(研究报告),
  各有专属的叙事主线。
- **四种视觉变体** —— `MSU`、`SJTU`、`CityU` 与 `Generic`(无机构品牌、
  无任何院校标识)。内容逻辑完全一致,只按视觉风格选择。
- **双语访谈** —— 智能体用你的语言与你访谈(中文进 → 中文出),采用分层、
  脚本化的提问。
- **推断优先** —— 它会先读你附上的材料和已有笔记,把提取到的内容回读给你
  确认,只就空缺处发问。
- **低摩擦** —— 区分“阻断性问题”与“带默认值的塑形问题”,并提供“用默认值”
  的快捷出口(但大纲审批关卡始终生效)。
- **两轮确认** —— 给出大纲后,智能体会运行内容驱动的 **A 轮**(基于大纲、
  确认大纲本身无法决定的逐页选择)与 **B 轮**(基于缺失材料清单、逐项决定
  每个空缺的去向),然后等待你明确批准。某一轮若无实质内容可决定,会用
  一行说明跳过。
- **绝不杜撰** —— 缺失证据一律变为 `TODO` 占位符并写入“缺失材料”行,
  绝不编造数字或引用。
- **模块化输出** —— `main.tex` + `sections/` + `figures/` + `references.bib`。
- **统一构建路径** —— 每种变体都以 `latexmk -xelatex` 为目标,中英文演示
  文稿编译方式完全相同。
- **确定性脚手架** —— 一个无依赖的 Python 脚本生成起始工程,智能体再
  填入经批准的内容。

## 为什么先访谈

学术演示文稿的质量,取决于智能体在动手写 LaTeX 之前是否充分理解了这场
报告。因此本技能强制三道关卡:

1. **先访谈再生成** —— 绝不从一个模糊请求直接跳到 `.tex`。先做一次推断
   通读你的材料,分层提问只问真正的空缺。
2. **大纲审批** —— 产出“需求摘要 + 逐页大纲 + 缺失材料清单”,再经两轮
   内容驱动的确认(先基于大纲,后基于缺失材料)精修;生成会等待你对
   确认后方案的明确批准。
3. **学术诚信** —— 实证结果、引用、数据描述、定理陈述、数值量级,
   一律不得编造。

设立这些关卡的原因是:建立在误读原始材料之上的访谈,会产出一份自信却
错误的演示文稿。本技能把精力花在理解报告上,让它写出的 LaTeX 反而成了
最轻松的部分。

## 环境要求

| 用途 | 要求 |
| --- | --- |
| 运行本技能 | 一个智能体宿主:**Claude Code**(插件)或 **Codex**(技能) |
| 编译演示文稿 | 含 **XeLaTeX** 的 LaTeX 发行版 —— TeX Live(推荐完整方案)或 MiKTeX |
| 参考文献 | **`biber`**(TeX Live 自带;latexmk 会自动调用) |
| 构建自动化 | **`latexmk`**(推荐) |
| 脚手架脚本 | **Python 3.8+**(仅标准库 —— 无需 `pip install`) |

> **关于字体的说明。** 四种模板都使用 `ctexbeamer` 文档类,因此*即便是
> 纯英文演示文稿*也会经由 XeLaTeX 并加载中文字体支持。安装完整版 TeX Live
>(自带 Fandol 中文字体以及 `ctex`/`biblatex` 宏包)是最省心的选择。
> 若使用 MiKTeX,请在首次编译时允许“按需自动安装宏包”。

## 仓库结构

```text
academic-latex-slides/
├── skills/academic-latex-slides/        # 规范技能源 —— 在此编辑
│   ├── SKILL.md
│   ├── references/                      # 访谈协议、蓝图、规则
│   ├── assets/templates/                # MSU / SJTU / CityU / Generic 模板资源
│   ├── scripts/scaffold.py              # 确定性起始工程生成器
│   └── agents/openai.yaml               # Codex 接口元数据
├── plugins/academic-latex-slides/       # 供 Claude Code 插件使用的同步镜像
│   ├── .claude-plugin/plugin.json
│   └── skills/academic-latex-slides/    # 生成的副本 —— 请勿手工编辑
├── .claude-plugin/marketplace.json      # Claude Code marketplace 元数据
├── scripts/
│   ├── sync_distributions.py            # 复制 规范源 → 插件镜像
│   └── build_portable_packages.py       # 构建可传输 ZIP 包
├── README.md
└── LICENSE
```

规范源位于 `skills/academic-latex-slides/`。`plugins/` 目录是**生成的镜像**——
请始终编辑规范源,然后运行同步脚本(见[开发与维护](#开发与维护))。

## 安装

### Claude Code

本插件通过 Claude Code marketplace(`.claude-plugin/marketplace.json`)分发。
可从 **GitHub 仓库**或**本地路径**安装。

**从 GitHub 安装**(把 `<owner>/<repo>` 替换为宿主仓库):

```text
/plugin marketplace add <owner>/<repo>
/plugin install academic-latex-slides@academic-latex-slides
```

**从本地克隆或解压的 ZIP 安装:**

```text
/plugin marketplace add /absolute/path/to/academic-latex-slides
/plugin install academic-latex-slides@academic-latex-slides
```

marketplace 名称与插件名称同为 `academic-latex-slides`(因此写作
`academic-latex-slides@academic-latex-slides`)。对于**私有** GitHub 仓库,
宿主会使用你已有的 git 凭据进行认证。之后要获取新版本:

```text
/plugin marketplace update academic-latex-slides
```

然后重启 Claude Code(或重新加载插件),让刷新后的技能生效。如果你此前
是从本地路径添加的,先移除那条记录(`/plugin marketplace remove <旧名称>`)
以避免名称冲突。

### Codex

**手动复制** —— 把规范技能文件夹复制进 Codex 的技能目录:

```bash
# macOS / Linux
cp -R skills/academic-latex-slides ~/.codex/skills/
```

```powershell
# Windows PowerShell
Copy-Item -Recurse skills\academic-latex-slides $HOME\.codex\skills\
```

然后新开一个 Codex 会话并调用它:

```text
Use $academic-latex-slides to create a research-talk deck.
```

### 构建可移植 ZIP 包

要在没有 git 的情况下把技能传到另一台机器:

```bash
python scripts/build_portable_packages.py
```

它会生成:

- `dist/academic-latex-slides-codex-skill.zip`
- `dist/academic-latex-slides-claude-plugin.zip`

解压 Codex 包,使目标机器上的最终文件夹为
`~/.codex/skills/academic-latex-slides/`。解压 Claude 包后,把
`/plugin marketplace add` 指向解压出的文件夹。

## 使用

### 工作流程

智能体始终按三个阶段运行:

| 阶段 | 发生什么 |
| --- | --- |
| **1. 访谈** | 先对你的材料做推断通读,再分层双语提问(第 1 层阻断 → 第 2 层塑形 → 受门控的第 3 层深挖)。 |
| **2. 大纲关卡** | 构建“需求摘要 + 逐页大纲 + 缺失材料清单”,经 **A 轮**(基于大纲)与 **B 轮**(基于缺失材料)精修,然后**停下并等待你的批准**。 |
| **3. 生成** | 运行脚手架,用经批准的内容替换起始小节,在需要时为公式/图/附录预留位置,返回工程路径与编译命令。 |

### 访谈内部机制

访谈是决定演示文稿质量的关键环节,因此它是结构化的,而非随意而为。

**推断通读(永远第一步)。** 智能体会重读你的请求与每一个附件,填好任何
可安全推断的字段,并把提取到的内容(结构、核心结果、数据、引用)回读给
你确认或纠正。它只问真正的空缺。视觉模板是唯一**绝不**推断的字段——
始终显式询问。

在产出任何大纲之前,**九个核心字段**都会被解析(询问、推断或取默认):

| 字段 | 你不指定时的默认 |
| --- | --- |
| 模板(`MSU` / `SJTU` / `CityU` / `Generic`) | 无 —— 始终询问 |
| 原型(`lecture` / `research talk`) | 由上下文推断,否则询问 |
| 语言 | 与你的语言一致 |
| 核心信息(只需记住的那一件事) | 无 —— 始终询问 |
| 元数据(标题、作者、单位、日期) | 标为 `TODO` 占位符 |
| 受众 | 本领域研究生水平的同行 |
| 时长 + 目标页数 | 约每 1.5 分钟一张内容页 |
| 材料完备度(完整 / 大纲 / 仅题目) | 由你提供的内容推断 |
| 学术组件(公式 / 图 / 引用 / 附录) | 由原型推断;正文内作者-年份引用,不单独做参考文献页 |

**分层提问,合并为一条同行口吻的消息:**

- **第 1 层 —— 阻断:** 模板、原型、语言、核心信息。无法安全取默认。
- **第 2 层 —— 塑形:** 元数据、受众、时长、材料完备度、学术组件。
  每项都给出明示默认,你可用一个词接受。
- **第 3 层 —— 受门控的深挖:** 针对原型的尖锐问题,**仅当**你提供了
  大纲或完整内容时才问。若你只有一个题目,本层跳过——针对缺失内容的
  深问只会制造杜撰压力。

**快捷出口。** 说一句*“用默认”*(或英文 *"use defaults"*),所有第 2/3 层
项都会被填入默认值并明示。大纲审批关卡仍然生效——默认值只是加快访谈,
绝不跳过关卡。

**大纲后的两轮确认。** 三件产出成形后,在审批关卡之前,智能体会再确认
两轮:

- **A 轮 —— 基于大纲:** 大纲本身无法决定的逐页选择(深度/层次、
  以哪个结果开场、拆分还是合并、超时先砍什么、记号或例题选择、章节顺序)。
- **B 轮 —— 基于缺失材料:** 逐项处理每个空缺——现在给、稍后给
 (留带日期的 `TODO`)、去掉该页/该论断,或保留一个清晰标注的占位符。

两轮都是**内容驱动**的:某一轮若没有实质内容可决定,会用一行说明跳过,
绝不用编造的问题凑数。每一轮之后都会更新这三件产出,这样你批准的是一份
准确的方案,而非初步猜测。

### 演示文稿蓝图

每种原型都有一条默认叙事主线;访谈厘清报告后,智能体会据此调整(绝非
僵硬套用模板)。

**Lecture(教学讲课)** —— 重在教学、铺垫、例子与回顾,而非新颖性:

> 标题 → 学习目标 → 课程地图 / 本讲位置 → 核心概念 →
> 推导或例题 → 练习 / 应用 → 小结与要点

**Research talk(研究报告)** —— 围绕贡献进行说服;快速交付
“问题 → 设计 → 结果”链条:

> 标题 → 研究动机 → 研究问题 / 缺口 → 贡献 →
> 数据与设计 → 主要结果 → 补充分析 → 结论

**节奏。** 默认约每 1.5 分钟一张内容页。`lecture` 侧重讲解、例题与
回顾;`research talk` 侧重动机、识别、结果与解读。时间紧张时,先砍
广度,后动叙事主线。该蓝图可跨领域适配——一场面板数据计量报告、
一堂实验流程讲课、一场数值方法研讨,用的是同一条主线、不同的页面角色。

### 端到端示例

一次真实会话,从请求到编译出 PDF。

**1 —— 你提出请求。** 一开始就把题目和材料一并给智能体:

```text
Use $academic-latex-slides. I'm giving a 20-minute research talk on
"Audit partner rotation and earnings quality". CityU style, slides in English.
Here are my notes and the regression table. (attaches notes.md, table1.tex)
```

**2 —— 智能体与你访谈**(先推断通读,再只问空缺):

```text
I read your notes and Table 1. Here's what I extracted:
  • RQ: does mandatory partner rotation change discretionary accruals?
  • Sample: 2008–2020 Chinese listed firms; main coeff ≈ -0.013 (p<0.05)
  • Identification: staggered rotation, firm + year FE

A few things so I build the right deck —
  • If the audience remembers one number, is it the -0.013, or an economic-
    magnitude restatement?
  • What does a skeptical referee attack first — selection, or the FE design?
  • Title / author / institute / date? (placeholders are fine — I'll flag them)
  • I'll assume figures + inline author-year citations (e.g., “Gul, Wu, and
    Yang 2013”) — no separate references slide, no appendix. Right?
```

**3 —— 智能体给出大纲并等待**(审批关卡):

```text
REQUIREMENTS SUMMARY
  Template: CityU · Archetype: research talk · Language: EN
  Timing: ~20 min → ~13 content slides · Audience: accounting peers (default)

SLIDE-BY-SLIDE OUTLINE
  1 Title   2 Motivation   3 Research question / gap   4 Contribution
  5 Data & sample   6 Identification   7 Main result (Table 1)
  8 Economic magnitude   9 Robustness   10 Heterogeneity   11 Conclusion

MISSING MATERIALS
  • TODO: economic-magnitude restatement of -0.013
  • TODO: robustness table not yet supplied

Here's what I'll build, and what I can't fill without your input.
Reply 'approved' to generate, or correct the scope and I'll revise.
```

**4 —— 你批准。** 智能体运行脚手架并写入各小节:

```text
approved
```

**5 —— 智能体生成并交还:**

```text
Created research-talk project with the cityu template at output/audit-talk
Compile:  cd output/audit-talk && latexmk -xelatex main.tex
```

**6 —— 你编译:**

```bash
cd output/audit-talk
latexmk -xelatex main.tex
```

有你材料支撑的小节会被填好;无支撑的论断保留为清晰标注的 `TODO:`
占位符,留待你补全。

### 生成的项目结构

```text
output/audit-talk/
├── main.tex                 # 模板渲染的导言区 + \input 接线
├── sections/
│   ├── 01_*.tex             # 按原型而定的起始小节
│   ├── 02_*.tex
│   ├── 03_*.tex
│   ├── 04_*.tex
│   └── 90_appendix.tex      # \appendix 桩,仅在需要时使用
├── figures/                 # 你的图(默认为空)
├── references.bib           # 你的参考文献(默认为空)
└── <template assets>        # 所选变体的 logo / 主题 .sty 文件
```

起始小节的文件名取决于原型:

| 原型 | 起始小节 |
| --- | --- |
| `research-talk` | `01_motivation` · `02_design` · `03_results` · `04_conclusion` |
| `lecture` | `01_learning_goals` · `02_core_content` · `03_examples` · `04_summary` |

小节*标题*随 `--language`(英文或中文)而变;文件名保持不变。智能体会用
经批准的内容替换这些起始小节,并可能为匹配批准后的大纲而增删、拆分或
重命名小节。

### 编译演示文稿

```bash
latexmk -xelatex main.tex
```

`latexmk` 会跑完 XeLaTeX 各遍并自动调用 `biber`。若没有 `latexmk`,
手动编译:

```bash
xelatex main.tex
biber main
xelatex main.tex
xelatex main.tex
```

## 脚手架脚本(独立使用)

智能体会替你运行它,但你也可以直接生成起始工程。它是确定性的,且
**无任何第三方依赖**。

```bash
python skills/academic-latex-slides/scripts/scaffold.py \
  --template sjtu \
  --deck-type lecture \
  --language zh \
  --title "资产定价导论" \
  --subtitle "Lecture 1" \
  --author "Your Name" \
  --institute "Your Institute" \
  --date "2026-05-17" \
  output/slides
```

```powershell
# Windows PowerShell(续行用反引号)
python skills\academic-latex-slides\scripts\scaffold.py `
  --template sjtu --deck-type lecture --language zh `
  --title "资产定价导论" --subtitle "Lecture 1" `
  --author "Your Name" --institute "Your Institute" `
  --date "2026-05-17" output\slides
```

| 参数 | 必填 | 取值 / 说明 |
| --- | --- | --- |
| `output_dir`(位置参数) | 是 | 目标目录 |
| `--template` | 是 | `msu` · `sjtu` · `cityu` · `generic` |
| `--deck-type` | 是 | `lecture` · `research-talk` |
| `--language` | 是 | `en` · `zh`(选择起始小节语言) |
| `--title` | 是 | 自动做 LaTeX 转义 |
| `--subtitle` | 否 | 默认为空 |
| `--author` | 是 | 自动做 LaTeX 转义 |
| `--institute` | 是 | 自动做 LaTeX 转义 |
| `--date` | 是 | 自由文本,例如 `2026-05-17` |
| `--force` | 否 | 允许写入非空目录 |

随后用 `latexmk -xelatex main.tex` 编译。

## 模板变体

所有变体共享相同的内容逻辑、访谈流程与模块化输出。只按视觉风格选择——
智能体不会从你的语言、机构或报告类型去推断模板。

| 变体 | 视觉特征 | 适用场景 | 自带资源 |
| --- | --- | --- | --- |
| **MSU** | 绿色学术配色,经典 Beamer 质感 | 通用报告、研讨会、内部演示 | `msu.png`、`Logo.png` |
| **SJTU** | 正式机构主题,封面系统较强 | 精致讲课、正式学术活动 | SJTU 主题 `.sty` 文件、`vi/` 视觉识别资源 |
| **CityU** | 紫色学术配色,标题页简洁克制 | 紧凑讲课、简洁报告、清爽研讨 | `CityULogo.pdf` |
| **Generic** | 机构中性的原生 Beamer 主题,无 logo、无品牌色 | 跨机构报告、草稿、无品牌演示 | 无(仅模板) |

## 故障排查

| 症状 | 原因与解决 |
| --- | --- |
| `Output directory is not empty: ...` | 脚手架拒绝写入非空目录。改用空目录,或加 `--force` 与现有文件并存。 |
| `biber: command not found` / 引用显示为 `[?]` 或粗体键名 | `biber` 缺失或未运行。安装完整版 TeX Live(自带 `biber`),并用 `latexmk -xelatex` 编译以自动跑 biber。手动编译需 `xelatex → biber → xelatex → xelatex`。 |
| `Package fontspec/ctex error` 或缺中文字形 | 四种模板都用 `ctexbeamer`,XeLaTeX 总会加载中文支持。用完整版 TeX Live(自带 Fandol 字体),或在 MiKTeX 首次编译时允许按需装包。 |
| 用 `pdflatex` 编译失败 | 属预期——构建目标**仅限 XeLaTeX**。请始终用 `latexmk -xelatex`(或 `xelatex`)。 |
| PDF 里图丢失 | 演示文稿引用 `figures/` 里的文件;智能体不会编造图。编译前把你的图放进去(或在访谈时提供)。 |
| Claude Code 里看不到插件改动 | 运行 `/plugin marketplace update academic-latex-slides`,再重启 Claude Code。若你自己改了技能,请编辑 `skills/academic-latex-slides/` 下的**规范**源并运行 `python scripts/sync_distributions.py`(`plugins/` 镜像是生成的)。 |
| 智能体只产出占位符而非内容 | 这是设计如此——你提供的是题目或不完整原始材料,无支撑的论断会留作标注的 `TODO:` 行。补上缺失材料(或在 B 轮决定其去向)后请智能体填充。 |

## 开发与维护

**始终编辑规范源,然后同步镜像。** `plugins/` 目录是生成的——在那里
手工改动会被覆盖。

```bash
# 1. 编辑 skills/academic-latex-slides/ 下的文件

# 2. 把规范技能复制进 Claude Code 插件镜像
python scripts/sync_distributions.py

# 3.(可选)构建两个传输 ZIP 包
python scripts/build_portable_packages.py
```

`build_portable_packages.py` 会先执行同步步骤,因此 ZIP 包始终反映
规范源。同步之后,规范树与镜像树逐字节一致。

## 适用范围

第 1 版刻意保持窄聚焦:

- 仅从零生成
- 不做 PPT 转换
- 不输出 HTML 演示
- 不自动导出 PDF

这种窄聚焦是刻意的:把精力花在动手前理解报告上,学术演示文稿才会更好。

## 致谢

SJTU 变体打包了 **SJTU Beamer 主题**的一个最小运行时子集;MSU 与 CityU
变体是受密歇根州立大学与香港城市大学视觉识别启发的简化学术演示文稿。
这些资源仅为让生成的演示文稿开箱即可编译而附带。Generic 变体不携带任何
机构标识——它只用原生 Beamer 主题,且不附带任何资源。

## 许可证

[MIT](LICENSE) © Gareth

# Interview Protocol

Run this before generating any slides. The interview decides slide quality more
than the LaTeX does — spend the agent's effort here.

## Operating principles

1. **Interview in the user's language.** Detect it from the user's request. If
   they write Chinese, interview in Chinese; if English, in English. Every
   question below ships with an EN and a ZH script — use the matching one.
2. **Infer before asking.** Never dump a blank form. Read what the user already
   said and anything they attached, fill what you can, then ask only the gaps.
3. **One human batch, not an interrogation.** Combine all open questions into a
   single consultant-style message. Sound like a colleague scoping a talk, not a
   form. Natural: *"A few things so I build the right deck —"*. Avoid:
   *"Field 1: ... Field 2: ... Field 3: ..."*.
4. **Never fabricate.** Missing evidence becomes a placeholder and a
   missing-materials line, never an invented result.

## Step 0 — Inference pass

Before writing any question:

1. Re-read the user's request and **read every attached file** (paper, notes,
   prior slides, outline). Do not ask the user to retype anything a file already
   contains.
2. Internally fill any of the nine core fields the user already stated or that
   are safely inferable from context.
3. If the user attached substantive material, **echo back what you extracted** —
   structure, core results, data, citations — in a few lines, then ask only:
   *"Did I read this right, and what should the deck emphasize?"* This is the
   single biggest accuracy lever; an interview built on a misread source
   produces a confident wrong deck.
4. **Template is the one field you must never infer** — not from language, not
   from institution, not from talk type. Always ask it explicitly (see
   `templates.md` selection rule).

## The nine core fields

Every field must be resolved (asked, inferred, or defaulted) before the outline.
Each is tagged with the tier that resolves it.

| Field | Tier | Default if user defers |
| --- | --- | --- |
| Template (`MSU` / `SJTU` / `CityU` / `Generic`) | 1 | none — must ask |
| Archetype (`lecture` / `research talk`) | 1 | infer from context, else ask |
| Language (deck language) | 1 | match the user's language |
| Core message (one thing to remember) | 1 | none — must ask |
| Metadata (title, subtitle, author, institute, date) | 2 | placeholders flagged as TODO |
| Audience (who they are, what they know) | 2 | graduate peers in the field |
| Timing + slide target | 2 | ≈ 1 content slide per 1.5 min |
| Material readiness (full / outline / topic) | 2 | infer from how much they gave |
| Academic components (formulas / figures / citations / appendix) | 2 | infer from archetype; citations are inline author-year by default — no references/bibliography slide unless explicitly asked |

## Tier 1 — Blocking questions (must ask; cannot be safely defaulted)

Ask these whenever the Inference pass did not already resolve them.

- **Template**
  EN: *"Which visual style — MSU, SJTU, CityU, or Generic (no branding)?"*
  ZH: *“用哪个视觉风格 —— MSU、SJTU、CityU,还是 Generic(无品牌通用版)?”*
- **Archetype** (only if context is ambiguous)
  EN: *"Is this a teaching lecture or a research talk? They get different spines."*
  ZH: *“这是教学讲课还是研究报告?两者的叙事主线不同。”*
- **Language** (only if it differs from the conversation language)
  EN: *"Slides in English or Chinese?"*
  ZH: *“幻灯片用中文还是英文?”*
- **Core message** — the spine of the whole deck:
  EN: *"When it's over and people remember exactly one thing, what is it?"*
  ZH: *“讲完之后,如果听众只记住一件事,那应该是什么?”*

## Tier 2 — Shaping questions (ask once, batched, each with a default)

Fold these into the same single message as any unresolved Tier 1 items. State
the default inline so the user can accept with one word.

- **Metadata**
  EN: *"Title, author, institute, date? (placeholders are fine — I'll flag them)"*
  ZH: *“标题、作者、单位、日期?(可先留占位,我会标 TODO)”*
- **Audience**
  EN: *"Who's in the room and what do they already know? (default: grad-level peers in the field)"*
  ZH: *“听众是谁、已经懂什么?(默认:本领域研究生水平的同行)”*
- **Timing + slides**
  EN: *"How long do you have? (I'll target ~1 content slide per 1.5 min unless you want denser/sparser)"*
  ZH: *“你有多长时间?(默认每约 1.5 分钟一张内容页,可调密/调疏)”*
- **Material readiness**
  EN: *"Do you have the full content, a rough outline, or just the topic right now?"*
  ZH: *“目前是完整内容、粗略大纲,还是只有题目?”*
- **Academic components** — confirm an inference, do not ask four yes/nos:
  EN (research talk): *"I'll assume figures and inline author-year citations (e.g., “Gul, Wu, and Yang 2013”) — no separate references/bibliography slide and no appendix unless you ask. Right?"*
  EN (lecture): *"I'll assume formulas and worked examples, no appendix — right?"*
  ZH (研究报告): *“我默认要图、正文内用作者-年份引用(如“Gul, Wu, and Yang 2013”),不单独做参考文献页、暂不加附录 —— 对吗?”*
  ZH (讲课): *“我默认要公式和例题、暂不加附录 —— 对吗?”*

## Escape hatch

If the user says *"use defaults"* / *“用默认”* / signals impatience: fill every
Tier 2 and Tier 3 item with the defaults above, **state explicitly what you
defaulted**, and proceed straight to the outline. The outline approval gate
still applies — defaults speed the interview, they never skip the gate.

## Tier 3 — Adaptive deep-dive (gated)

Gate: ask Tier 3 **only** when material readiness is *outline* or *full*, and
**only** the items not already answered. If material is *topic only*, skip the
deep-dive — go straight to a skeleton plus a missing-materials list; deep
questions about absent content only produce fabrication pressure.

These questions are deliberately sharp — they extract the deck's real shape, not
generic restatements.

### If `lecture`

- EN: *"Where does this sit in the course — what was the last lecture, what's next?"*
  ZH: *“这一讲在课程里的位置 —— 上一讲讲了什么、下一讲是什么?”*
- EN: *"What do students most often get **wrong** about this topic?"* (this is the real teaching target)
  ZH: *“学生在这个主题上最常**搞错**什么?”*(这才是真正的教学靶心)
- EN: *"What should they be able to **do** afterwards, not just know?"*
  ZH: *“课后他们应该能**做到**什么,而不只是知道什么?”*
- EN: *"Which prerequisites can I assume vs. must re-cap in one slide?"*
  ZH: *“哪些前置知识可以直接假设、哪些需要用一页快速回顾?”*
- EN: *"Worked example, in-class exercise, recap slide — which of these?"*
  ZH: *“例题、课堂练习、小结页 —— 要哪些?”*

### If `research talk`

- EN: *"One sentence: what's the contribution **relative to prior work**?"*
  ZH: *“一句话:相对已有文献,你的贡献是什么?”*
- EN: *"If they remember only one **number or result**, which one?"*
  ZH: *“如果只记住一个**数字或结果**,是哪一个?”*
- EN: *"What does a skeptical referee attack first?"* (this sets how much robustness to show)
  ZH: *“最挑剔的审稿人会先攻击哪里?”*(这决定稳健性要展开多少)
- EN: *"Data and identification in one or two lines?"*
  ZH: *“数据与识别策略,一两句话?”*
- EN: *"Mechanism, heterogeneity, robustness, appendix — which earn slide time?"*
  ZH: *“机制、异质性、稳健性、附录 —— 哪些值得占页?”*

## Material sufficiency rule

- **Full content** — use it; the interview only resolves emphasis and pacing.
- **Rough outline** — refine structure; mark every detail that still needs a
  source with a TODO and a missing-materials line.
- **Topic only** — build a skeleton and a missing-materials list. Do **not**
  fabricate, to fill space, any of:
  - empirical findings
  - citation entries
  - data descriptions
  - theorem statements
  - numerical magnitudes

## Required pre-generation output

Before writing any file, deliver three artifacts:

1. **Requirements summary** — the nine fields as resolved, with every defaulted
   item explicitly marked `(default)` so the user can override fast.
2. **Slide-by-slide outline.**
3. **Missing-materials list** — what the user must supply before any TODO can
   become real content.

Do **not** jump from these artifacts to the approval gate. First run the two
confirmation rounds below; they refine the artifacts so the user approves an
accurate plan, not a first guess.

## Post-outline confirmation (two rounds)

After the three artifacts exist, interview the user twice more — one round
driven by the **outline**, one by the **missing-materials list**. Same rules as
the rest of this protocol: interview in the user's language, one batched message
per round, sound like a colleague, never fabricate, honor the *"use defaults"*
escape hatch.

**Content-gated, not mandatory filler.** Each round surfaces *only* genuinely
decision-relevant items. If a round has nothing real to confirm, say so in one
line — EN: *"The outline is unambiguous — nothing to confirm there."* / ZH:
*“大纲没有歧义,这一轮无需确认。”* — and move on. Never manufacture questions
to fill a round. Run Round A before Round B (Round A can change what is missing).

### Round A — Outline-driven confirmation

Walk the slide-by-slide outline and flag only the per-slide decisions the
outline alone cannot settle: depth/level, which result or number leads, split
vs. merge, what gets cut if the deck runs long, notation or worked-example
choice, section ordering. Batch them into one message, referencing slides by
number. Example phrasings:

- EN: *"Slide 7 (Main result) — lead with the coefficient or the economic magnitude?"*
  ZH: *“第 7 页(主结果)—— 先放系数还是先放经济量级?”*
- EN: *"Slides 9–10 are tight for 20 minutes; if we run long, cut robustness or heterogeneity?"*
  ZH: *“9–10 页对 20 分钟偏紧;超时的话先砍稳健性还是异质性?”*
- EN: *"Slide 4 (Contribution) — one bullet per prior-work gap, or a single positioning sentence?"*
  ZH: *“第 4 页(贡献)—— 每个文献缺口一条,还是一句定位?”*

After Round A, update the outline. Round A answers can add or remove gaps, so
re-derive the missing-materials list before Round B.

### Round B — Missing-materials-driven confirmation

Go through the missing-materials list **item by item**. For each gap, make the
user choose its fate explicitly — never let the agent guess or fabricate. Offer
four options per item: supply it now, supply later (keep a dated TODO), drop the
slide/claim, or keep a clearly-marked placeholder. Batch as one numbered message
mirroring the list. Example phrasings:

- EN: *"Missing item 1 — economic-magnitude restatement of −0.013: give me the number now, supply later, drop the slide, or keep a `TODO` placeholder?"*
  ZH: *“缺料 1 —— −0.013 的经济量级换算:现在给数字、稍后补、去掉该页,还是留 `TODO` 占位?”*
- EN: *"Missing item 2 — robustness table: attach it now, or drop the robustness slide for this version?"*
  ZH: *“缺料 2 —— 稳健性表:现在附上,还是这一版先去掉稳健性页?”*

After Round B, update the missing-materials list and the requirements summary so
each gap's resolution is recorded.

## Approval gate (scripted close)

Present the three **post-confirmation** artifacts, then end the message with
this close (use the matching language):

EN: *"Here's what I'll build, and here's what I can't fill without your input.
Reply 'approved' to generate, or correct the scope and I'll revise."*
ZH: *“以上是我会生成的内容,以及没有你的输入我无法填的部分。回复『approved』我就生成,或指出要改的范围,我会修订。”*

Do not generate the LaTeX project until the user approves. If the user revises
scope, pacing, or emphasis, update all three artifacts and ask again.

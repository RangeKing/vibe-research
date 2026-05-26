# Vibe Research

[English README](./README.md)

Vibe Research 是一个面向 Codex、Claude Code 和 OpenClaw 的跨平台 managed research harness 与论文写作 skill。

它覆盖的是“科研判断 + 写作执行”之间的工作带：研究方向梳理、项目评估、去风险、claim 校准、期刊匹配、正文改写、语言润色，以及基于审稿意见的修改。
对接近投稿的任务，它还默认要求做一次**参考文献充分性审查**，避免只润色文字和图，却放过 citation coverage、格式顺序和关键 claim 无支撑的问题。
当存在目标期刊或 Codex Goal 模式提供的外部目标时，它也可以生成 **target-journal scorecard**，用分数、封顶阻断项和差距修复循环来衡量当前稿件/投稿包离目标期刊还有多远。

## 这个仓库是什么

这个仓库不是论文模板，也不是一组零散提示词。

它更像一个结构化的 research harness，包含：

- 作为 brain 的 coordinator
- 负责恢复、packetize、delegate、merge 的 harness 层
- 用于延续项目状态的 durable session artifacts
- 面向具体任务的 specialist routes
- 按需加载的参考资料
- 用于交付物的模板
- 面向不同宿主平台的薄适配层

根文件 [SKILL.md](./SKILL.md) 是唯一事实源。

## 范围：这里的「全流程」指什么

在本仓库中，**全流程**指从选题与框架到 **major revision / resubmission** 的 **稿件与决策链**，并与 coordinator + 8 条 routes 一致。另明确纳入：

- **系统综述（PRISMA）**：流程、报告体例、与证据合成相关的决策与文稿组织—不包含**自动化文献检索引擎或爬虫实现**。
- **图表叙事**：图与正文 claim 对齐、图注与主信息、常见 integrity 与翻车点—不包含**具体绘图软件操作教程**。
- **轻量持久记忆**：以可复用的 conversation artifacts 和模板形式保存经验，而不是数据库或后台 runtime。

**不在本 skill 默认承诺内**（一句话边界）：湿实验 SOP、原始数据到成稿的**统计分析 pipeline 全包**、自动化数据库/文献爬取、期刊政策**实时在线核验**、以**经费标书全文**为主交付物等。

## 这个 Skill 适合解决什么问题

适合的任务包括：

- 选择或重构研究方向
- 判断一个 idea 是否值得继续做
- 评估稿件当前是否接近投稿
- 检查参考文献数量、覆盖面和期刊适配是否达标
- 为生成的论文或投稿包打分，估计距离目标期刊要求的差距
- 找出最关键的证据缺口
- 降低 overclaim 或因果表述过强的问题
- 重写标题、摘要、引言、结果、讨论等部分
- 选择目标期刊或构建 journal ladder
- 在不改变科学立场的前提下润色文本
- 让文本更像高水平期刊作者的表达，而不是 AI 腔或翻译腔
- 处理审稿人、编辑或合作者反馈
- 从既有 checkpoint 继续一个研究 campaign
- 比较多个方向并保留被排除路径的原因
- 总结失败实验或多轮修改中沉淀出的经验

## 核心设计

这个 skill 采用四层 managed-harness 结构：

- Brain：coordinator 的判断、路由、校验与最终综合
- Harness：preflight、packetize、compact、wake、delegate、merge
- Hands：`assess`、`claim`、`draft`、`revise` 等具体 route
- Session：脱离当前上下文窗口而存在的 durable artifacts

这样设计的目的，是避免科研辅助里最常见的问题之一：把诊断、改写、选刊、rebuttal 和 campaign 状态全都揉成一个模糊的大回答。

## 路由体系

主要 routes 如下：

- `/framing`：研究方向、one-liner、假设、killer experiment、research brief
- `/assess`：评估稿件或项目现状，不默认进入重写
- `/de-risk`：falsifier、negative control、kill criteria、审稿风险扫描
- `/claim`：claim 强度、因果边界、机制措辞、limitations
- `/draft`：科研文本起草与改写
- `/journal`：期刊匹配、受众匹配、投稿定位
- `/polish`：无外部反馈驱动的润色
- `/revise`：基于反馈的修改与回复策略

每个 route 的窄职责定义见 [roles/](./roles/)。

分数驱动的工作使用 [references/target-journal-scorecard.md](./references/target-journal-scorecard.md) 和 [templates/target_journal_scorecard.md](./templates/target_journal_scorecard.md)。这个分数是结构化 readiness / gap 诊断，不是录用概率预测。

## Harness 工作方式

默认情况下，coordinator 会按照以下生命周期工作：

1. 内部 preflight，也就是 `doctor`
2. 如果存在 continuation artifact，则先 `wake`
3. 必要时生成 task packet
4. 进入最合适的 route 执行
5. 对照证据边界和交付物要求做校验
6. 在合适时蒸馏为可复用的 memory artifacts
7. 为后续续跑生成 checkpoint
8. 只有在多个独立 hands 参与时才做 merge
9. 以“下一步最优动作”收尾

这个机制特别适合处理真实场景里的复杂输入，例如：

- 一大段草稿外加 reviewer comments
- 只有部分证据的项目总结
- 一个同时混合选刊、改写和 claim 审查的请求
- 一个需要从既有研究记忆继续推进的长期项目

## 证据边界与学术完整性

这个 skill 明确要求 evidence-bound。

它不应该：

- 编造数据、实验、参考文献、审稿意见或期刊决定
- 把推测性的措辞说成已经被证明的事实
- 在用户没有提供原文时假装“已经完整修改”
- 在证据不足时承诺某稿件能发某个具体期刊

相关 guardrails 见 [system/guardrails.md](./system/guardrails.md)。

## 仓库结构

```text
.
├── SKILL.md                      # Canonical skill definition
├── agents/openai.yaml            # Codex 侧 UI 元数据
├── system/                       # Coordinator、routing、guardrails
├── roles/                        # 窄职责 specialist routes
├── references/                   # 按需加载的判断资料
├── templates/                    # 交付模板与 compact 对象
└── platforms/                    # 各宿主平台的薄适配层
```

关键文件：

- [SKILL.md](./SKILL.md)：主工作流与路由契约
- [system/coordinator.md](./system/coordinator.md)：控制面行为
- [system/routing.md](./system/routing.md)：路由选择规则
- [system/guardrails.md](./system/guardrails.md)：学术完整性边界
- [references/harness-engineering.md](./references/harness-engineering.md)：维护这个 skill 本身时的 harness 设计说明
- [references/managed-harness-patterns.md](./references/managed-harness-patterns.md)：把 managed-agent 设计原则映射到本 skill 的速查说明
- [references/evolution-loop.md](./references/evolution-loop.md)：受 EvoScientist 启发的 campaign 逻辑与轻量 memory 哲学
- [references/prisma-systematic-review.md](./references/prisma-systematic-review.md)：PRISMA 向系统综述结构与 task packet 配合方式
- [references/figure-storytelling.md](./references/figure-storytelling.md)：图表、图注与正文 claim 对齐
- [references/high-journal-expression.md](./references/high-journal-expression.md)：面向润色任务的高水平期刊表达规则
- [references/reference-adequacy-audit.md](./references/reference-adequacy-audit.md)：面向投稿前任务的参考文献数量、覆盖面与编号顺序检查
- [templates/research_task_packet.md](./templates/research_task_packet.md)：复杂任务的紧凑控制对象
- [templates/reference_coverage_map.md](./templates/reference_coverage_map.md)：当 citation 太少或覆盖不均时的 claim-bucket / 插入计划模板
- [templates/campaign_checkpoint.md](./templates/campaign_checkpoint.md)：长期任务的可续接状态
- [templates/research_memory.md](./templates/research_memory.md)：可复用经验蒸馏
- [templates/research_session_log.md](./templates/research_session_log.md)：长程或多 hand 任务的 append-only session 状态
- [templates/direction_tournament.md](./templates/direction_tournament.md)：多个候选路径的结构化比较
- [templates/polish_pass.md](./templates/polish_pass.md)：以直接改写为主的润色交付模板
- [templates/writing_quality_review.md](./templates/writing_quality_review.md)：结构化写作质量审查模板

## 平台适配

仓库采用“一套主逻辑 + 多个平台薄适配”的方式：

- [platforms/codex/README.md](./platforms/codex/README.md)
- [platforms/claude-code/README.md](./platforms/claude-code/README.md)
- [platforms/openclaw/README.md](./platforms/openclaw/README.md)

适配层应该保持轻量。如果修改影响了实际推理流程，应该先更新 [SKILL.md](./SKILL.md)。

## 使用示例

### Codex

```text
$vibe-research /assess this manuscript status
$vibe-research continue this project from this checkpoint
$vibe-research /polish this abstract without changing the claims
$vibe-research /revise these reviewer comments
$vibe-research 评估这篇稿子当前最关键的问题
$vibe-research 从这个 checkpoint 继续，并找出下一步
$vibe-research 回复这些审稿意见，并给出修改策略
```

### Claude Code

```text
/assess evaluate this abstract and tell me what is missing before submission
/claim this discussion overstates causality; rewrite it safely
/revise turn these reviewer comments into a response strategy
```

### OpenClaw

典型模式是：

- coordinator 负责最终综合
- 只有在确实降低歧义时才并行 specialist routes
- 对于宽而乱的任务，先 compact，再并行

## 如何维护这个 Skill

更新时建议遵循：

1. 始终把 [SKILL.md](./SKILL.md) 当作 source of truth。
2. 让 role 文件保持窄职责，不要把控制逻辑塞进去。
3. 详细维护说明放到 [references/](./references/) 中，避免根 skill 过胖。
4. 如果同一种控制对象或交付物反复出现，就新增或复用模板。
5. 平台适配层保持同步，但不要写厚。

仓库已经包含一份轻量维护说明 [references/harness-engineering.md](./references/harness-engineering.md)，里面也给出了后续迭代时可用的 regression prompt 形态。
另外新增了 [references/managed-harness-patterns.md](./references/managed-harness-patterns.md)，用于快速查看 managed-harness 接口设计。
每次做较大修改后，可以运行 [scripts/quick_validate.py](./scripts/quick_validate.py) 做本地结构校验。

## 适用人群

这个 skill 适合：

- 正在探索或挽救研究方向的研究者
- 希望提升稿件质量与发表定位、面向更高标准投稿目标的作者
- 需要处理 rebuttal、major revision 或 resubmission 的团队
- 想构建研究型 AI skill、而不是平铺提示词的人

它不能替代真实科学证据、同行评审，也不能替代对具体期刊最新政策的人工核验。

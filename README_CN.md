# Vibe Research

[English README](./README.md)

Vibe Research 是一个面向 Codex、Claude Code 和 OpenClaw 的跨平台演化式 research harness 与论文写作 skill。

它覆盖的是“科研判断 + 写作执行”之间的工作带：研究方向梳理、项目评估、去风险、claim 校准、期刊匹配、正文改写、语言润色，以及基于审稿意见的修改。

## 这个仓库是什么

这个仓库不是论文模板，也不是一组零散提示词。

它更像一个结构化的 research harness，包含：

- 作为控制面的 coordinator
- 用于延续项目状态的 checkpoint / memory artifacts
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
- 找出最关键的证据缺口
- 降低 overclaim 或因果表述过强的问题
- 重写标题、摘要、引言、结果、讨论等部分
- 选择目标期刊或构建 journal ladder
- 在不改变科学立场的前提下润色文本
- 处理审稿人、编辑或合作者反馈
- 从既有 checkpoint 继续一个研究 campaign
- 比较多个方向并保留被排除路径的原因
- 总结失败实验或多轮修改中沉淀出的经验

## 核心设计

这个 skill 采用两层结构：

- 控制面：preflight、路由、范围控制、上下文压缩、campaign 延续、验证后蒸馏、恢复、收尾
- 执行面：`assess`、`claim`、`draft`、`revise` 等具体 route

这样设计的目的，是避免科研辅助里最常见的问题之一：把诊断、改写、选刊和 rebuttal 全都揉成一个模糊的大回答。

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

## Harness 工作方式

默认情况下，coordinator 会按照以下生命周期工作：

1. 内部 preflight，也就是 `doctor`
2. 必要时生成 task packet
3. 进入最合适的 route 执行
4. 对照证据边界和交付物要求做校验
5. 在合适时蒸馏为可复用的 memory / checkpoint artifacts
6. 如果任务过载，则先 compact 或做恢复
7. 以“下一步最优动作”收尾

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
- [references/evolution-loop.md](./references/evolution-loop.md)：受 EvoScientist 启发的 campaign 逻辑与轻量 memory 哲学
- [references/prisma-systematic-review.md](./references/prisma-systematic-review.md)：PRISMA 向系统综述结构与 task packet 配合方式
- [references/figure-storytelling.md](./references/figure-storytelling.md)：图表、图注与正文 claim 对齐
- [templates/research_task_packet.md](./templates/research_task_packet.md)：复杂任务的紧凑控制对象
- [templates/campaign_checkpoint.md](./templates/campaign_checkpoint.md)：长期任务的可续接状态
- [templates/research_memory.md](./templates/research_memory.md)：可复用经验蒸馏
- [templates/direction_tournament.md](./templates/direction_tournament.md)：多个候选路径的结构化比较

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

## 适用人群

这个 skill 适合：

- 正在探索或挽救研究方向的研究者
- 希望提升稿件质量与发表定位、面向更高标准投稿目标的作者
- 需要处理 rebuttal、major revision 或 resubmission 的团队
- 想构建研究型 AI skill、而不是平铺提示词的人

它不能替代真实科学证据、同行评审，也不能替代对具体期刊最新政策的人工核验。

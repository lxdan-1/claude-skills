# Claude 技能使用指南

> 最后更新：2026-05-15 | 技能总数：23

本文档列出所有可用技能、调用方式和触发关键词。产品工作流技能部分在新增技能后自动更新。

---

## 调用方式

技能有两种调用方式：

1. **斜杠命令**：输入 `/技能名称`，例如 `/需求分析`、`/PRD写作`
2. **关键词触发**：在对话中自然输入触发关键词，Claude 会自动识别并调用对应技能

> 不确定用哪个技能？输入 `/技能调度器` 或直接描述目标，让调度器帮你选路。

---

## 快速参考表

| 技能名称 | 斜杠命令 | 主要触发关键词 | 用途简述 |
|---------|---------|--------------|---------|
| 技能调度器 | `/技能调度器` | 不知道用哪个技能 | 自动选路，推荐合适技能 |
| 需求分析 | `/需求分析` | 需求分析、需求拆解、需求澄清 | 把模糊想法转成结构化需求 |
| PRD写作 | `/PRD写作` | PRD写作、需求文档、功能说明 | 输出可评审可开发的PRD |
| 规则逻辑速查 | `/规则逻辑速查` | 规则逻辑、条件判断、逻辑梳理 | 快速整理业务规则 |
| 交互页面生成 | `/交互页面生成` | 交互页面、HTML原型、页面设计 | 生成可运行HTML原型 |
| 评审检查 | `/评审检查` | 评审检查、方案评审、PRD评审 | 结构化评审需求和方案 |
| 问题答疑 | `/问题答疑` | 问题答疑、快速解释、文档解读 | 基于文档快速回答问题 |
| 提示词优化 | `/提示词优化` | 提示词优化、prompt优化 | 优化AI提示词质量 |
| 市场调研 | `/市场调研` | 市场调研、竞品分析、行业扫描 | 收集市场和竞品信息 |
| 操作手册生成 | `/操作手册生成` | 操作手册、截图生成手册 | 从截图生成操作文档 |
| html-prototype-workflow | `/html-prototype-workflow` | 按方法论生成原型、七步工作流 | 政务/医疗系统HTML原型 |
| brainstorming | `/brainstorming` | 创意工作前（自动触发） | 创意和功能设计前置分析 |
| frontend-design | `/frontend-design` | 前端界面、网页组件、UI设计 | 生成高质量前端代码 |
| update-config | `/update-config` | 配置设置、自动化行为、权限 | 修改settings.json配置 |
| keybindings-help | `/keybindings-help` | 快捷键、键位绑定 | 自定义键盘快捷键 |
| simplify | `/simplify` | 代码简化、代码质量 | 检查并简化代码 |
| fewer-permission-prompts | `/fewer-permission-prompts` | 减少权限提示 | 优化权限提示配置 |
| loop | `/loop` | 循环任务、定时执行 | 设置定时重复任务 |
| claude-api | `/claude-api` | Claude API、Anthropic SDK | Claude API开发调试 |
| init | `/init` | 初始化文档 | 初始化CLAUDE.md |
| review | `/review` | PR评审、代码评审 | 评审Pull Request |
| security-review | `/security-review` | 安全审查、安全检查 | 代码安全审查 |

---

## 产品工作流技能

> 以下技能存储在 `d:\claude\skills\` 目录，新增技能后自动更新本节内容。

<!-- AUTO_UPDATE_START -->

### brainstorming

**功能**："You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation."

**调用方式**：`/brainstorming`

---

### frontend-design

**功能**：Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applications. Generates creative, polished code that avoids generic AI aesthetics.

**调用方式**：`/frontend-design`

---

### html-prototype-workflow

**功能**：从技术要求文档生成政务/医疗/监管类系统 HTML 交互原型的七步工作流。当用户提供技术要求文档并想生成原型、说"按方法论生成原型"、"帮我走一遍原型工作流"、"根据技术要求生成HTML"时使用。

**调用方式**：`/html-prototype-workflow`

---

### PRD写作

**功能**：将需求分析结果整理成结构化 PRD 文档，按业务系统类或规则逻辑类分别输出可供设计、研发、测试和评审使用的说明。

**触发关键词**：PRD写作 / PRD整理 / 需求文档输出 / 功能说明撰写 / 方案沉淀 / 或需要把需求分析结果转成正式文档。

**调用方式**：`/PRD写作`

---

### 交互页面生成

**功能**：根据需求分析或 PRD 结果直接生成可运行的 HTML 原型文件，包含页面结构、交互流程、状态设计和真实合理的模拟数据。

**触发关键词**：交互页面生成 / HTML原型 / 页面方案设计 / 原型说明 / 页面结构拆解 / 列表页设计

**调用方式**：`/交互页面生成`

---

### 市场调研

**功能**：收集并整理市场、竞品、用户、方案和趋势信息，形成可比较的调研结论与建议。

**触发关键词**：市场调研 / 竞品分析 / 行业扫描 / 方案对比 / 用户需求洞察 / 或需要形成调研报告。

**调用方式**：`/市场调研`

---

### 技能调度器

**功能**：根据用户目标在产品工作流技能之间自动选路，决定是否需要前置步骤、应调用哪些 skills 以及调用顺序。

**调用方式**：`/技能调度器`

---

### 提示词优化

**功能**：优化产品工作流中的提示词，包括需求分析、PRD写作、HTML原型生成和评审检查等场景，提升输出稳定性、配套性和可执行性。

**触发关键词**：提示词优化 / prompt优化 / 提示词重写 / 工作流提示词设计 / 指令增强 / AI输出不稳定

**调用方式**：`/提示词优化`

---

### 操作手册生成

**功能**：识别大屏/页面截图中的具体指标名称、图表类型、数据展示方式，根据图片内容自动补充或生成操作手册的详细内容。

**调用方式**：`/操作手册生成`

---

### 规则逻辑速查

**功能**：快速定位并整理规则逻辑，提炼触发条件、判断过程、执行动作、例外情况和影响范围。

**触发关键词**：规则逻辑速查 / 规则查询 / 条件判断说明 / 逻辑梳理 / 规则口径统一 / 或需要快速解释复杂业务规则。

**调用方式**：`/规则逻辑速查`

---

### 评审检查

**功能**：按目标、范围、流程、规则、交互、数据、依赖和验收标准维度检查需求、PRD 或配套 HTML 原型质量，输出分级问题、待确认项和评审结论。

**触发关键词**：评审检查 / 方案评审 / PRD评审 / 原型评审 / 需求评审 / 上线前检查

**调用方式**：`/评审检查`

---

### 问题答疑

**功能**：基于已有文档、规则、代码或上下文，快速定位依据并回答问题，必要时说明不确定点和信息缺口。

**触发关键词**：问题答疑 / 快速解释 / 文档解读 / 方案说明 / 逻辑说明 / 或需要根据现有材料给出清晰回答。

**调用方式**：`/问题答疑`

---

### 需求分析

**功能**：拆解模糊需求，识别需求类型，补齐目标、角色、场景、流程、规则、数据、范围和风险，并输出结构化需求分析结果。

**触发关键词**：需求分析 / 需求拆解 / 需求澄清 / 范围界定 / 用户故事梳理 / 需求整理

**调用方式**：`/需求分析`

---

<!-- AUTO_UPDATE_END -->

---

## 内置系统技能

> 以下技能为系统内置，不在 `skills` 目录根目录中，需手动维护。

### update-config

### update-config

**功能**：通过修改 settings.json 配置自动化行为、权限设置、环境变量和 hooks。需要"每次X时自动Y"类需求时必用。

**触发关键词**：配置设置 / 自动化行为 / 权限设置 / 添加权限 / 设置环境变量 / hooks配置 / from now on when X

**调用方式**：`/update-config`

---

### keybindings-help

**功能**：自定义键盘快捷键，修改 `~/.claude/keybindings.json`，支持和弦绑定。

**触发关键词**：快捷键 / 键位绑定 / rebind / 自定义快捷键 / chord shortcut

**调用方式**：`/keybindings-help`

---

### simplify

**功能**：检查已修改代码的复用性、质量和效率，发现问题后直接修复。

**触发关键词**：代码简化 / 代码质量 / 优化代码 / simplify

**调用方式**：`/simplify`

---

### fewer-permission-prompts

**功能**：扫描对话记录中常见的只读 Bash 和 MCP 工具调用，生成优先级 allowlist 减少权限提示。

**触发关键词**：减少权限提示 / 权限太多 / allowlist

**调用方式**：`/fewer-permission-prompts`

---

### loop

**功能**：按指定间隔循环执行某个提示词或斜杠命令（默认10分钟），适合定时轮询或重复任务。

**触发关键词**：循环任务 / 定时执行 / 每X分钟 / 重复运行 / keep running

**调用方式**：`/loop 5m /命令名`

---

### claude-api

**功能**：构建、调试和优化 Claude API / Anthropic SDK 应用，包含 prompt caching、thinking、tool use 等特性。

**触发关键词**：Claude API / Anthropic SDK / prompt caching / 模型版本迁移

**调用方式**：`/claude-api`

---

### init

**功能**：为当前代码库初始化 CLAUDE.md 文档，记录项目结构、约定和开发指南。

**触发关键词**：初始化文档 / 初始化CLAUDE.md / init

**调用方式**：`/init`

---

### review

**功能**：评审当前分支上的 Pull Request，输出结构化评审意见。

**触发关键词**：PR评审 / 代码评审 / review PR

**调用方式**：`/review`

---

### security-review

**功能**：对当前分支的待提交变更进行完整安全审查。

**触发关键词**：安全审查 / 安全检查 / security review

**调用方式**：`/security-review`

---

## 技能组合推荐

| 场景 | 推荐组合 |
|-----|---------|
| 从零做一个新功能 | `/需求分析` → `/PRD写作` → `/交互页面生成` → `/评审检查` |
| 快速出原型 | `/需求分析` → `/交互页面生成` |
| 政务/医疗系统原型 | `/html-prototype-workflow` |
| 不知道从哪里开始 | `/技能调度器` |
| 梳理复杂业务规则 | `/规则逻辑速查` → `/PRD写作` |
| 做竞品调研后出方案 | `/市场调研` → `/需求分析` → `/PRD写作` |
| 上线前质量把关 | `/评审检查` |

---

## 自动更新机制

新增技能后，`产品工作流技能` 节（`<!-- AUTO_UPDATE_START -->` 到 `<!-- AUTO_UPDATE_END -->` 之间）会由脚本自动重新生成。

更新脚本位置：[scripts/update_skills_guide.py](scripts/update_skills_guide.py)

触发方式：每次在 `d:\claude\skills\` 目录下写入新的 `SKILL.md` 文件时，PostToolUse hook 自动执行脚本。

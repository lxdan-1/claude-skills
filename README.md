# Claude Skills & Config

产品经理工作流技能库 + 自动更新脚本，配合 Claude Code 使用。

## 包含内容

| 路径 | 说明 |
|------|------|
| `skills/` | 产品工作流技能（需求分析、PRD写作、评审检查等） |
| `scripts/update_skills_guide.py` | 新增技能后自动更新 SKILLS_GUIDE.md 的脚本 |
| `.claude/settings.json` | PostToolUse hook 配置，触发自动更新 |
| `SKILLS_GUIDE.md` | 所有技能的调用方式和关键词说明文档 |

## 在新电脑上复用

### 1. 安装前提

- [Claude Code](https://claude.ai/code) 已安装
- Python 3.x 已安装
- Git 已安装

### 2. 克隆仓库

```bash
git clone https://github.com/lxdan-1/claude-skills.git d:/claude
```

> 路径建议保持 `d:/claude`，脚本中硬编码了该路径。如需修改，见下方说明。

### 3. 配置 Claude Code 识别技能目录

打开 Claude Code，确认 `d:/claude/skills/` 已被识别为技能目录（通常自动生效）。

### 4. 恢复第三方技能包（可选）

以下技能体积较大或有版权限制，未纳入仓库，需手动安装：

- **frontend-design**：从 Claude Code 插件市场安装
- **claude-code**：Anthropic 官方提供
- **skill-router-mcp**：MCP 服务，参考原安装文档

### 5. 修改路径（如果不用 d:/claude）

编辑 `scripts/update_skills_guide.py` 顶部的两个常量：

```python
SKILLS_DIR = Path("d:/claude/skills")
GUIDE_PATH = Path("d:/claude/SKILLS_GUIDE.md")
```

同时更新 `.claude/settings.json` 中的 hook 命令路径。

## 自动更新机制

每次在 `skills/` 下新建技能目录并写入 `SKILL.md` 时，PostToolUse hook 自动触发脚本，重新生成 `SKILLS_GUIDE.md` 中的产品工作流技能章节。

## 技能列表

详见 [SKILLS_GUIDE.md](SKILLS_GUIDE.md)。

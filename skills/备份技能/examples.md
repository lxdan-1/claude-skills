# 备份技能 - 使用示例

## 示例 1：快速备份（最常用）

**用户输入**：
> 帮我备份技能

**Claude 执行**：
```bash
cd d:/claude/skills
bash backup.sh
```

**预期结果**：
```
📦 开始备份 Claude Skills...
提交信息: Auto backup: 2026-04-21 14:30:00
🚀 推送到 GitHub...
✅ 备份成功！
📍 仓库地址: https://github.com/lxdan-1/claude-skills
```

---

## 示例 2：备份并说明更新内容

**用户输入**：
> 我刚才优化了 PRD 写作 skill，帮我备份一下

**Claude 执行**：
```bash
cd d:/claude/skills
bash backup.sh "优化了 PRD 写作 skill 的提示词"
```

**预期结果**：
```
📦 开始备份 Claude Skills...
提交信息: 优化了 PRD 写作 skill 的提示词
[main 7f8c9d2] 优化了 PRD 写作 skill 的提示词
 1 file changed, 15 insertions(+)
🚀 推送到 GitHub...
✅ 备份成功！
📍 仓库地址: https://github.com/lxdan-1/claude-skills
```

---

## 示例 3：新增 skill 后备份

**用户输入**：
> 我新增了一个"市场调研"skill，保存到 GitHub

**Claude 执行**：
```bash
cd d:/claude/skills
bash backup.sh "新增了市场调研 skill"
```

**预期结果**：
```
📦 开始备份 Claude Skills...
提交信息: 新增了市场调研 skill
[main a1b2c3d] 新增了市场调研 skill
 3 files changed, 120 insertions(+)
🚀 推送到 GitHub...
✅ 备份成功！
📍 仓库地址: https://github.com/lxdan-1/claude-skills
```

---

## 示例 4：定期备份

**用户输入**：
> 保存一下我的技能库

**Claude 执行**：
```bash
cd d:/claude/skills
bash backup.sh
```

**预期结果**：
```
📦 开始备份 Claude Skills...
提交信息: Auto backup: 2026-04-21 15:45:30
[main 9e8f7g6] Auto backup: 2026-04-21 15:45:30
 2 files changed, 8 insertions(+)
🚀 推送到 GitHub...
✅ 备份成功！
📍 仓库地址: https://github.com/lxdan-1/claude-skills
```

---

## 示例 5：检查备份状态

**用户输入**：
> 帮我查一下技能库有没有备份到 GitHub

**Claude 执行**：
```bash
cd d:/claude/skills
git log --oneline -5
```

**预期结果**：
```
a1b2c3d (HEAD -> main, origin/main) 新增了市场调研 skill
7f8c9d2 优化了 PRD 写作 skill 的提示词
9e8f7g6 Auto backup: 2026-04-21 15:45:30
2h3i4j5 初始化技能库
```

然后访问 https://github.com/lxdan-1/claude-skills 验证最新提交。

---

## 示例 6：处理备份失败

**用户输入**：
> 帮我备份技能

**如果出现错误**：
```
❌ 推送失败，请检查网络或凭证
```

**Claude 建议**：
1. 检查网络连接
2. 验证 GitHub 凭据是否正确
3. 查看 BACKUP_GUIDE.md 中的故障排除部分
4. 尝试手动运行：`git push origin main`

---

## 示例 7：自定义提交信息的最佳实践

### ✅ 好的提交信息
```bash
bash backup.sh "新增需求分析 skill 和优化 PRD 写作提示词"
bash backup.sh "修复了交互页面生成 skill 的 bug"
bash backup.sh "更新了所有 skill 的文档"
```

### ❌ 不好的提交信息
```bash
bash backup.sh "更新"
bash backup.sh "修改"
bash backup.sh "fix"
```

清晰的提交信息便于日后查看历史和理解每次备份的内容。

---

## 工作流建议

### 日常工作流
1. 修改或新增 skill
2. 在 Claude Code 中说："帮我备份技能"
3. Claude 自动执行备份
4. 查看成功提示

### 周期性备份
- 每周末：`bash backup.sh "周末定期备份"`
- 重大更新后：`bash backup.sh "重大更新：新增 X 个 skill"`

### 跨设备同步
1. 在新电脑上：`git clone https://github.com/lxdan-1/claude-skills.git`
2. 获取最新的所有 skill
3. 继续修改和备份

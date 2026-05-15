# Claude Skills 自动备份指南

## 快速备份

### 方式 1：使用备份脚本（推荐）

```bash
# 进入 skills 目录
cd d:/claude/skills

# 运行备份脚本
bash backup.sh "更新了 PRD 写作 skill"
```

如果不提供提交信息，会自动生成时间戳：
```bash
bash backup.sh
```

### 方式 2：手动 Git 命令

```bash
cd d:/claude/skills
git add .
git commit -m "你的提交信息"
git push origin main
```

---

## 首次使用需要配置

第一次推送时，Git 会要求输入 GitHub 用户名和密码（或 Personal Access Token）：

1. **用户名**：`lxdan-1`
2. **密码**：使用 GitHub Personal Access Token（推荐）
   - 访问 https://github.com/settings/tokens
   - 创建新 token（勾选 `repo` 权限）
   - 复制 token 作为密码输入

之后 Git 会记住凭证，下次不用再输入。

---

## 验证备份

推送成功后，访问仓库查看：
https://github.com/lxdan-1/claude-skills

---

## 可选：设置定时自动备份

如果想要每天自动备份，可以用 Windows 任务计划程序：

1. 打开"任务计划程序"
2. 创建基本任务
3. 触发器：每天 18:00
4. 操作：运行程序
   - 程序：`bash`
   - 参数：`d:/claude/skills/backup.sh "Daily auto backup"`

---

## 常见问题

**Q: 推送失败，显示"Authentication failed"**
A: 检查 GitHub 凭证是否正确，或使用 Personal Access Token

**Q: 如何查看备份历史？**
A: 访问 https://github.com/lxdan-1/claude-skills/commits/main

**Q: 能否从 GitHub 恢复？**
A: 可以，使用 `git clone` 或 `git pull` 恢复最新版本

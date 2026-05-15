# 备份技能 Skill

## 概述
自动将 skills 目录中的所有文件备份到 GitHub，保留你的工作成果。支持自定义提交信息，一句话即可完成备份。

## 使用场景
- 修改或新增了某个 skill，想要保存到 GitHub
- 定期备份所有技能文件，防止丢失
- 在不同电脑或账号间同步技能库
- 记录技能的更新历史

## 核心功能
1. **自动备份** - 一键将所有更改推送到 GitHub
2. **灵活提交信息** - 支持自定义备份说明
3. **完整性检查** - 验证备份是否成功
4. **错误处理** - 清晰的错误提示和解决方案

## 执行流程

### 快速备份（推荐）
```bash
cd d:/claude/skills
bash backup.sh
```
脚本会自动生成时间戳提交信息，例如：`备份技能 - 2026-04-21 14:30:00`

### 自定义提交信息
```bash
cd d:/claude/skills
bash backup.sh "更新了 PRD 写作技能"
```

### 手动 Git 命令
```bash
cd d:/claude/skills
git add .
git commit -m "你的提交信息"
git push origin main
```

## 参数说明

| 参数 | 说明 | 示例 |
|------|------|------|
| 提交信息 | 可选，描述本次备份的内容 | "新增了需求分析 skill" |
| 无参数 | 使用默认时间戳提交信息 | `bash backup.sh` |

## 常见用法

### 场景 1：修改了某个 skill 后备份
```bash
bash backup.sh "优化了 PRD 写作 skill 的提示词"
```

### 场景 2：新增了 skill 后备份
```bash
bash backup.sh "新增了市场调研 skill"
```

### 场景 3：定期备份（不需要特殊说明）
```bash
bash backup.sh
```

## 前置条件
- ✅ 已安装 Git
- ✅ 已配置 GitHub 账号和 Personal Access Token
- ✅ 已初始化本地 Git 仓库
- ✅ 已关联远程 GitHub 仓库

## 验证备份成功

### 方法 1：查看终端输出
成功的输出应该包含：
```
[main abc1234] 备份技能 - 2026-04-21 14:30:00
 2 files changed, 10 insertions(+)
备份成功！已推送到 GitHub
```

### 方法 2：访问 GitHub 仓库
打开浏览器访问：https://github.com/lxdan-1/claude-skills

应该能看到最新的提交记录和文件更新。

## 故障排除

### 问题 1：bash 命令找不到
**原因**：使用的是 PowerShell 而不是 Git Bash

**解决方案**：
- 在 VS Code 终端选择 Git Bash
- 或使用 PowerShell 命令：`.\backup.sh`

### 问题 2：Permission denied
**原因**：脚本没有执行权限

**解决方案**：
```bash
chmod +x backup.sh
bash backup.sh
```

### 问题 3：GitHub 认证失败
**原因**：未配置 GitHub 凭据或 Token 过期

**解决方案**：
- 参考 BACKUP_GUIDE.md 中的"GitHub 凭据配置"部分
- 使用 Personal Access Token 而不是密码

### 问题 4：nothing to commit
**原因**：没有新的更改需要备份

**解决方案**：
- 确认你修改了 skills 目录中的文件
- 使用 `git status` 查看当前状态

## 相关文件
- `backup.sh` - 自动化备份脚本
- `BACKUP_GUIDE.md` - 详细的备份指南
- `.gitignore` - Git 忽略规则配置

## 提示
- 💡 建议每次修改 skill 后立即备份
- 💡 提交信息要清晰，便于日后查看历史
- 💡 可以配置 Windows Task Scheduler 实现定时自动备份
- 💡 备份前确保网络连接正常

#!/bin/bash

# Claude Skills 自动备份脚本
# 使用方法: bash backup.sh "你的提交信息"

SKILLS_DIR="d:/claude/skills"
COMMIT_MSG="${1:-Auto backup: $(date '+%Y-%m-%d %H:%M:%S')}"

cd "$SKILLS_DIR"

echo "📦 开始备份 Claude Skills..."
echo "提交信息: $COMMIT_MSG"

# 检查是否有变化
if git diff-index --quiet HEAD --; then
    echo "✅ 没有新的变化，无需备份"
    exit 0
fi

# 添加所有变化
git add .

# 提交
git commit -m "$COMMIT_MSG"

# 推送到 GitHub
echo "🚀 推送到 GitHub..."
git push origin main

if [ $? -eq 0 ]; then
    echo "✅ 备份成功！"
    echo "📍 仓库地址: https://github.com/lxdan-1/claude-skills"
else
    echo "❌ 推送失败，请检查网络或凭证"
    exit 1
fi

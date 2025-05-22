#!/bin/bash

# 自动上传到GitHub的脚本
echo "开始自动上传到GitHub..."

# 获取当前日期和时间作为提交信息
COMMIT_MESSAGE="自动更新 $(date '+%Y-%m-%d %H:%M:%S')"

# 添加所有更改
git add .

# 提交更改
git commit -m "$COMMIT_MESSAGE"

# 推送到GitHub
git push origin master

echo "上传完成！" 
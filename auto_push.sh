#!/bin/bash

# 自动上传到GitHub的脚本
LOG_FILE="git_push.log"

echo "$(date '+%Y-%m-%d %H:%M:%S') - 开始自动上传到GitHub..." | tee -a $LOG_FILE

# 首先运行RSS程序获取最新文章
echo "$(date '+%Y-%m-%d %H:%M:%S') - 运行RSS程序获取最新文章..." | tee -a $LOG_FILE
python rss.py >> $LOG_FILE 2>&1
if [ $? -ne 0 ]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - RSS程序运行失败，请检查日志文件" | tee -a $LOG_FILE
    exit 1
fi

# 获取当前日期和时间作为提交信息
COMMIT_MESSAGE="自动更新 $(date '+%Y-%m-%d %H:%M:%S')"

# 添加所有更改
echo "$(date '+%Y-%m-%d %H:%M:%S') - 添加更改到Git..." | tee -a $LOG_FILE
git add . >> $LOG_FILE 2>&1
if [ $? -ne 0 ]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Git add失败，请检查日志文件" | tee -a $LOG_FILE
    exit 1
fi

# 检查是否有更改需要提交
if git diff-index --quiet HEAD --; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - 没有更改需要提交" | tee -a $LOG_FILE
    exit 0
fi

# 提交更改
echo "$(date '+%Y-%m-%d %H:%M:%S') - 提交更改..." | tee -a $LOG_FILE
git commit -m "$COMMIT_MESSAGE" >> $LOG_FILE 2>&1
if [ $? -ne 0 ]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Git commit失败，请检查日志文件" | tee -a $LOG_FILE
    exit 1
fi

# 推送到GitHub
echo "$(date '+%Y-%m-%d %H:%M:%S') - 推送到GitHub..." | tee -a $LOG_FILE
git push origin master >> $LOG_FILE 2>&1
if [ $? -ne 0 ]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Git push失败，请检查日志文件" | tee -a $LOG_FILE
    
    # 尝试使用SSH方式推送
    echo "$(date '+%Y-%m-%d %H:%M:%S') - 尝试使用SSH方式推送..." | tee -a $LOG_FILE
    REPO_NAME=$(git remote get-url origin | sed 's/.*\/\([^\/]*\)$/\1/' | sed 's/\.git$//')
    GITHUB_USERNAME=$(git remote get-url origin | sed 's/.*github.com\/\([^\/]*\).*/\1/')
    
    git push git@github.com:$GITHUB_USERNAME/$REPO_NAME.git master >> $LOG_FILE 2>&1
    if [ $? -ne 0 ]; then
        echo "$(date '+%Y-%m-%d %H:%M:%S') - SSH推送也失败，请检查网络或GitHub设置" | tee -a $LOG_FILE
        exit 1
    fi
fi

echo "$(date '+%Y-%m-%d %H:%M:%S') - 上传完成！" | tee -a $LOG_FILE 
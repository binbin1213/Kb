#!/bin/bash

# RSS程序运行脚本
LOG_FILE="rss_run.log"

echo "$(date '+%Y-%m-%d %H:%M:%S') - 开始运行RSS程序..." | tee -a $LOG_FILE

# 激活虚拟环境（如果有）
if [ -d "venv" ]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - 激活虚拟环境..." | tee -a $LOG_FILE
    source venv/bin/activate
fi

# 运行RSS程序
echo "$(date '+%Y-%m-%d %H:%M:%S') - 运行RSS程序..." | tee -a $LOG_FILE
python rss.py | tee -a $LOG_FILE

# 检查运行结果
if [ ${PIPESTATUS[0]} -ne 0 ]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - RSS程序运行失败" | tee -a $LOG_FILE
    exit 1
fi

echo "$(date '+%Y-%m-%d %H:%M:%S') - RSS程序运行完成" | tee -a $LOG_FILE 
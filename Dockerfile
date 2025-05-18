FROM python:3.11-slim
ENV RSS_URL=""
ENV DOWNLOAD_DIR=/app/downloads

# 修复系统时间和时区
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends -qq tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    apt-get purge -y tzdata && \
    rm -rf /var/lib/apt/lists/*

# 替换为清华镜像源
RUN sed -i 's/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list

COPY . /app
RUN mkdir -p /app/downloads
WORKDIR /app

# 安装基础工具
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends -qq \
    ca-certificates \
    apt-transport-https \
    gnupg && \
    rm -rf /var/lib/apt/lists/*

# 添加 Debian 官方密钥（使用清华镜像源后可能不需要此步骤）
RUN apt-key adv --keyserver hkps://keyserver.ubuntu.com --recv-keys \
    0x6ED0E03149E3848D00EC303140C3FF3F80B4E835 \
    0x3B4FE6ACC0B21F32 \
    0x2EBF116D50311AEB271CCD902949D1121B8D4E80

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 安装 cron 和 git
RUN apt-get update -y && \
    apt-get install -y -qq cron git && \
    echo "0 4 * * * python /app/rss.py && git -C /app add . && git -C /app commit -m 'Auto upload from Docker' && git -C /app push" > /etc/cron.d/rss-cron && \
    chmod 0644 /etc/cron.d/rss-cron && \
    crontab /etc/cron.d/rss-cron && \
    rm -rf /var/lib/apt/lists/*

CMD ["cron", "-f"]

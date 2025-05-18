FROM python:3.11-slim
ENV RSS_URL=""
ENV DOWNLOAD_DIR=/app/downloads

COPY . /app
RUN mkdir -p /app/downloads
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y cron git\nRUN echo "0 4 * * * python /app/rss.py && git -C /app add . && git -C /app commit -m 'Auto upload from Docker' && git -C /app push" > /etc/cron.d/rss-cron\nRUN chmod 0644 /etc/cron.d/rss-cron\nRUN crontab /etc/cron.d/rss-cron\n\nCMD ["cron", "-f"]
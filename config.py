# 支持多订阅源存储
RSS_URLS = ["https://rss.binbino.cn:88/feeds/all.atom"]
DATA_FILE = os.path.join(os.getenv('DOWNLOAD_DIR', '.'), 'data.json')
import os
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
TIMEOUT = 25
RETRIES = 3
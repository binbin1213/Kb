import os
import json
import feedparser
import ssl
import urllib3
import re
import certifi
from datetime import datetime
from typing import List, Dict, Any
import logging
from bs4 import BeautifulSoup
from dateutil import parser
import html2text
from urllib.parse import urljoin
import config
from md_formatter import html_to_markdown

# 支持多订阅源
RSS_URLS = config.RSS_URLS

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATA_FILE = config.DATA_FILE
USER_AGENT = config.USER_AGENT
TIMEOUT = config.TIMEOUT
RETRIES = config.RETRIES

def load_downloaded() -> Dict:
    """加载并验证已下载记录"""
    valid_records = {}
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                records = json.load(f)
                
                for link, record in records.items():
                    file_path = record.get('path', '')
                    if os.path.exists(file_path):
                        # 添加文件修改时间校验
                        record_mtime = record.get('mtime', 0)
                        current_mtime = os.path.getmtime(file_path)
                        
                        if current_mtime == record_mtime:
                            valid_records[link] = record
                        else:
                            logger.warning(f'文件修改时间不一致: {file_path}')
                    else:
                        logger.warning(f'记录文件不存在: {file_path}')
    
    except Exception as e:
        logger.error(f"加载记录失败: {str(e)}")
    return valid_records

def save_downloaded(data: Dict):
    """保存下载记录"""
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        logger.error(f"保存记录失败: {str(e)}")

def sanitize_filename(name: str) -> str:
    """
    清理文件名中的非法字符，去除 Windows 和 Unix 系统中不允许的字符，并截取前100个字符。

    Args:
        name (str): 原始文件名。

    Returns:
        str: 清理后的文件名。
    """
    if not isinstance(name, str):
        name = str(name)
    return re.sub(r'[\\/*?:"<>|]', '', name).strip()[:100]

def process_images(html: str, base_url: str) -> str:
    """图片处理"""
    soup = BeautifulSoup(html, 'html.parser')
    for img in soup.find_all('img'):
        src = img.get('data-src') or img.get('src')
        if src:
            img['src'] = urljoin(base_url, src)
        for attr in ['data-src', 'data-ratio', 'data-w', 'data-original']:
            if attr in img.attrs:
                del img[attr]
        img['style'] = "max-width: 100%; height: auto;"
    return str(soup)

def fetch_article_content(url: str) -> str:
    """获取文章内容"""
    try:
        headers = {
            "User-Agent": USER_AGENT,
            "Referer": "https://www.google.com/",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        }
        
        logger.info(f'正在获取文章内容: {url}')
        with urllib3.PoolManager(
            headers=headers,
            retries=urllib3.Retry(total=RETRIES, backoff_factor=0.3),
            cert_reqs='CERT_NONE',  # 禁用SSL验证
            ca_certs=certifi.where(),
        ) as http:
            response = http.request('GET', url, timeout=TIMEOUT)
            if response.status != 200:
                logger.warning(f'获取文章内容失败，状态码: {response.status}')
                return ""
                
            content_type = response.headers.get('Content-Type', '')
            logger.info(f'文章内容类型: {content_type}')
            
            # 尝试确定编码
            encoding = 'utf-8'
            if 'charset=' in content_type:
                encoding = content_type.split('charset=')[-1].strip()
            
            html_content = response.data.decode(encoding, errors='replace')
            logger.info(f'文章HTML长度: {len(html_content)}')
            
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # 针对不同网站尝试不同的选择器
            content_div = None
            
            # 少数派
            if 'sspai.com' in url:
                content_div = soup.find('div', class_='normal-article-content')
            # 阮一峰的博客
            elif 'ruanyifeng.com' in url:
                content_div = soup.find('div', class_='entry-content')
            # 微信公众号
            elif 'mp.weixin.qq.com' in url:
                content_div = soup.find('div', class_='rich_media_content')
            # 36kr
            elif '36kr.com' in url:
                content_div = soup.find('div', class_='article-content')
            # 知乎
            elif 'zhihu.com' in url:
                content_div = soup.find('div', class_='Post-RichTextContainer')
            # 通用方案，尝试一些常见的内容容器类名
            else:
                for class_name in ['article-content', 'post-content', 'entry-content', 'content', 'article', 'post']:
                    content_div = soup.find('div', class_=class_name)
                    if content_div:
                        break
            
            if not content_div:
                logger.warning(f'无法找到文章内容: {url}')
                # 保存第一个主要div作为备选
                main_div = soup.find('div', id='main') or soup.find('main') or soup.find('article')
                if main_div:
                    content_div = main_div
                else:
                    # 最后的备选：使用body
                    content_div = soup.find('body')
            
            if content_div:
                processed_content = process_images(str(content_div), url)
                return html_to_markdown(processed_content)
            else:
                return "无法解析文章内容"
    except Exception as e:
        logger.error(f"内容抓取失败 {url}: {str(e)}")
        return ""

def parse_rss(rss_url: str) -> List[Dict[str, Any]]:
    """解析RSS订阅"""
    articles = []
    # 进一步增加重试次数
    max_retries = RETRIES * 5
    for attempt in range(max_retries):
        try:
            ssl_context = ssl.create_default_context(cafile=certifi.where())
            ssl_context.check_hostname = True
            ssl_context.verify_mode = ssl.CERT_REQUIRED
            with urllib3.PoolManager(
                ssl_context=ssl_context,
                headers={"User-Agent": USER_AGENT}
            ) as http:
                # 增加超时时间
                response = http.request('GET', rss_url, timeout=TIMEOUT * 5)
                logger.info(f'RSS源 {rss_url} 状态码: {response.status}')
                
                # 打印RSS源返回的内容前500个字符（调试用）
                content_preview = response.data.decode('utf-8', errors='replace')[:500]
                logger.info(f'RSS源内容预览: {content_preview}')
                
                feed = feedparser.parse(response.data)
                
                # 打印解析后的feed信息
                if hasattr(feed, 'feed') and hasattr(feed.feed, 'title'):
                    logger.info(f'RSS源标题: {feed.feed.title}')
                if hasattr(feed, 'entries'):
                    logger.info(f'RSS源条目数量: {len(feed.entries)}')
                else:
                    logger.warning('RSS源没有entries属性')
                
            break
        except Exception as e:
            if attempt < max_retries - 1:
                # 优化错误日志
                logger.warning(f'RSS解析尝试 {attempt + 1}/{max_retries} 失败，将在3秒后重试: {str(e)}')
                import time
                time.sleep(3)
            else:
                logger.error(f'RSS解析失败，已达到最大重试次数: {str(e)}')
                return []

    if hasattr(feed, 'entries'):
        for entry in feed.entries:
            try:
                # 修复公众号名称提取逻辑
                author = "未知公众号"
                
                # 方法1：尝试从author字段获取
                if hasattr(entry, 'author'):
                    author = sanitize_filename(str(entry.author))
                
                # 方法2：尝试从分类信息获取（适用于某些Atom源）
                elif hasattr(entry, 'tags') and entry.tags:
                    author = sanitize_filename(str(entry.tags[0].term))
                
                # 方法3：尝试从标题前缀提取（示例："【公众号名】文章标题"）
                elif hasattr(entry, 'title'):
                    match = re.match(r'【(.*?)】', str(entry.title))
                    if match:
                        author = sanitize_filename(match.group(1))
                
                # 尝试使用feed标题作为作者
                elif hasattr(feed, 'feed') and hasattr(feed.feed, 'title'):
                    author = sanitize_filename(str(feed.feed.title))
                
                # 解析日期
                date_str = ''
                if hasattr(entry, 'published'):
                    date_str = entry.published
                elif hasattr(entry, 'updated'):
                    date_str = entry.updated
                
                if not date_str:
                    # 如果没有日期，使用当前时间
                    published = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    logger.warning(f'文章没有日期信息，使用当前时间: {published}')
                else:
                    published = parser.parse(str(date_str)).strftime("%Y-%m-%d %H:%M:%S")
                
                # 确保标题和链接存在
                try:
                    title = str(getattr(entry, 'title', "无标题")).strip()
                except:
                    title = "无标题"
                
                try:
                    link = str(getattr(entry, 'link', ""))
                except:
                    link = ""
                
                if not link:
                    logger.warning(f'文章没有链接，跳过: {title}')
                    continue
                
                articles.append({
                    "title": title,
                    "link": link,
                    "author": author,
                    "published": published
                })
                logger.info(f'成功解析文章: {title}')
            except Exception as e:
                logger.warning(f"解析条目失败: {str(e)}", exc_info=True)
    else:
        logger.warning(f'RSS源不包含任何文章条目')
    
    logger.info(f'从RSS源 {rss_url} 解析到 {len(articles)} 篇文章')
    return articles if articles else []


def main():
    logger.info('开始执行主函数')
    downloaded = load_downloaded()
    logger.info(f'已加载 {len(downloaded)} 条下载记录')
    all_articles = []
    for url in RSS_URLS:
        articles = parse_rss(url)
        all_articles.extend(articles)
    articles = all_articles
    logger.info(f'解析到 {len(articles)} 篇文章')
    
    if not articles:
        logger.warning('未获取到文章')
        return

    new_count = 0
    for article in articles:
        # 检查是否已下载
        # 检查记录和文件是否存在
        record = downloaded.get(article['link'])
        file_exists = False
        
        if record:
            file_path = record.get('path', '')
            file_exists = os.path.exists(file_path)
            
            if not file_exists:
                del downloaded[article['link']]
                logger.warning(f'发现无效记录：{file_path} 文件已不存在，已清理该记录')
                continue

            # 检查文件修改时间是否一致
            current_mtime = os.path.getmtime(file_path)
            if current_mtime != record.get('mtime', 0):
                logger.warning(f'文件修改时间不一致: {file_path}')
                file_exists = False
            
        if record and file_exists:
            logger.info(f'文章 {article["title"]} 已存在，跳过')
            continue
        
        logger.info(f'开始抓取文章 {article["title"]} 内容')
        content = fetch_article_content(article['link'])
        if not content:
            logger.warning(f'文章 {article["title"]} 内容抓取失败，跳过')
            continue
        
        # 创建公众号目录
        author_dir = sanitize_filename(article['author'])
        os.makedirs(author_dir, exist_ok=True)
        logger.info(f'已创建/使用公众号目录 {author_dir}')
        
        # 生成文件名
        safe_title = sanitize_filename(article['title'])
        try:
            date_part = datetime.strptime(article['published'], "%Y-%m-%d %H:%M:%S").strftime("%Y%m%d")
        except ValueError:
            logger.warning(f'日期格式解析失败，使用当前日期替代: {article["published"]}')
            date_part = datetime.now().strftime("%Y%m%d")
        
        filename = f"{date_part}_{safe_title}.md"
        month_dir = os.path.join(author_dir, date_part[:6])
        os.makedirs(month_dir, exist_ok=True)
        filepath = os.path.join(month_dir, filename)
        
        # 保存文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {article['title']}\n\n")
            f.write(f"**公众号**: {article['author']}\n")
            f.write(f"**发布日期**: {article['published']}\n\n")
            f.write(content)
        
        # 更新记录
        downloaded[article['link']] = {
            "title": article['title'],
            "author": article['author'],
            "date": article['published'],
            "path": filepath,
            "mtime": os.path.getmtime(filepath)
        }
        new_count += 1
        logger.info(f'已保存: {filepath}')
    
    if new_count > 0:
        save_downloaded(downloaded)
        logger.info(f'成功下载 {new_count}/{len(articles)} 篇新文章')
    else:
        logger.info('没有发现新文章')
    logger.info('主函数执行结束')

if __name__ == "__main__":
    main()
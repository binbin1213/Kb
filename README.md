# RSS阅读器

这是一个用Python编写的RSS阅读器，可以从多个RSS源获取文章并保存为Markdown格式。

## 功能特点

- 支持多个RSS订阅源
- 自动下载文章内容
- 将文章保存为Markdown格式
- 优化Markdown格式，使其更加易读
- 按照公众号/作者和日期组织文件
- 自动跟踪已下载的文章，避免重复下载

## 使用方法

1. 在`config.py`中配置RSS订阅源
2. 运行`python rss.py`下载文章
3. 文章将按照作者和日期保存在相应目录中

## 自动化

项目已配置自动上传到GitHub，每天凌晨2点会自动运行并上传最新更改。

## 依赖库

- feedparser：解析RSS源
- beautifulsoup4：解析HTML
- html2text：将HTML转换为Markdown
- urllib3：HTTP请求
- certifi：SSL证书验证

## 目录结构

```
/
├── rss.py          # 主程序
├── config.py       # 配置文件
├── md_formatter.py # Markdown格式化工具
├── data.json       # 已下载文章记录
├── auto_push.sh    # 自动上传脚本
└── README.md       # 项目说明
```

🙏 版权声明
所有内容仅限个人学习使用

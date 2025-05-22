#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import html2text

def clean_markdown(text):
    """
    清理和优化从HTML转换来的Markdown文本
    """
    # 替换奇怪的编号格式如 **0****1** 为 ### 1.
    text = re.sub(r'\*\*0\*\*\*\*(\d+)\*\*', r'### \1.', text)
    
    # 修复格式如 **02****活动名额** 为 ### 2. 活动名额
    text = re.sub(r'\*\*(\d+)\*\*\*\*([^*]+)\*\*', r'### \1. \2', text)
    
    # 修复格式如 ****市民卡乘地铁8折、公交5折优惠**** 为 ## 市民卡乘地铁8折、公交5折优惠
    text = re.sub(r'\*\*\*\*([^*]+)\*\*\*\*', r'## \1', text)
    
    # 替换连续的空行（超过2个）为最多2个空行
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # 修复列表格式
    text = re.sub(r'(\n\s*)-\s+', r'\1- ', text)
    
    # 修复标题格式（确保#后有空格）
    text = re.sub(r'(#+)([^#\s])', r'\1 \2', text)
    
    # 修复链接格式
    text = re.sub(r'\[\s+([^\]]+)\s+\]', r'[\1]', text)
    
    # 修复图片格式中的多余空格
    text = re.sub(r'!\[\s+([^\]]*)\s+\]', r'![\1]', text)
    
    # 修复粗体和斜体格式
    text = re.sub(r'\*\*\s+([^*]+)\s+\*\*', r'**\1**', text)
    text = re.sub(r'\*\s+([^*]+)\s+\*', r'*\1*', text)
    
    # 删除多余的HTML标签
    text = re.sub(r'</?span[^>]*>', '', text)
    
    # 修复标题后面紧跟内容的问题
    text = re.sub(r'(#+\s+[^\n]+)\n([^\n#])', r'\1\n\n\2', text)
    
    # 修复标题与内容之间没有空行的问题
    text = re.sub(r'(### \d+\.\s+[^\n]+)([^\n])', r'\1\n\n\2', text)
    
    # 修复标题格式不正确的问题
    text = re.sub(r'(#+)(\*\*[^*]+\*\*)', r'\1 \2', text)
    
    # 修复 **05****活动须知** 这种格式
    text = re.sub(r'\*\*(\d+)\*\*\*\*([^*]+)\*\*', r'### \1. \2', text)
    
    # 修复标题后直接跟文本的问题
    lines = text.split('\n')
    result_lines = []
    for i, line in enumerate(lines):
        result_lines.append(line)
        if i < len(lines) - 1:
            # 如果当前行是标题，下一行不是空行，则添加空行
            if re.match(r'^#+\s+', line) and lines[i+1].strip() and not re.match(r'^#+\s+', lines[i+1]):
                result_lines.append('')
    
    text = '\n'.join(result_lines)
    
    return text

def html_to_markdown(html):
    """
    将HTML转换为优化的Markdown格式
    """
    # 使用html2text进行基础转换
    converter = html2text.HTML2Text()
    converter.body_width = 0  # 不自动换行
    converter.ignore_images = False
    converter.images_as_html = True
    
    # 进行基础转换
    md_text = converter.handle(html).strip()
    
    # 清理和优化Markdown
    return clean_markdown(md_text)

if __name__ == "__main__":
    # 测试代码
    html_sample = """
    <div>
        <h1>测试标题</h1>
        <p>这是一个<strong>粗体</strong>测试</p>
        <p>这是一个<em>斜体</em>测试</p>
        <p>这是一个<strong>0</strong><strong>1</strong>奇怪的格式</p>
        <p>这是一个<strong>02</strong><strong>活动名额</strong>奇怪的格式</p>
        <p>这是一个<strong></strong><strong>市民卡乘地铁8折、公交5折优惠</strong><strong></strong>奇怪的格式</p>
        <ul>
            <li>列表项1</li>
            <li>列表项2</li>
        </ul>
    </div>
    """
    print(html_to_markdown(html_sample))
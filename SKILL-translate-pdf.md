# PDF翻译工具 SKILL

## 功能描述
将英文PDF/PPT文件提取文本并翻译为中文，保存为txt和md格式。

## 前置条件
1. 安装 pdftotext 工具 (poppler-utils): `pacman -S poppler`
2. Python 3.x 环境
3. 网络访问 MyMemory 翻译API (免费，每秒1次请求)

## 快速开始

### 单文件翻译
```bash
# 1. 提取PDF文本
pdftotext -layout input.pdf output.txt

# 2. 使用翻译脚本
python translator.py input.txt output_zh.txt

# 3. 转为Markdown
cp output_zh.txt output_zh.md
```

### 批量处理
编辑 `translate_batch.py` 中的文件列表，然后运行：
```bash
python translate_batch.py
```

## 核心代码 (可直接嵌入使用)

### translate_text() - 翻译函数
```python
import json
import urllib.parse
import urllib.request
import time
import random

def translate_text(text, max_retries=3):
    """
    使用MyMemory API翻译英文到中文
    
    参数:
        text: 要翻译的英文文本
        max_retries: 最大重试次数
        
    返回:
        翻译后的中文文本
    """
    if not text.strip():
        return text
    
    # 分段处理 (API限制每次400字符)
    max_len = 400
    segments = [text[i:i+max_len] for i in range(0, len(text), max_len)]
    
    translated_segments = []
    for seg in segments:
        success = False
        for attempt in range(max_retries):
            try:
                url = f"https://api.mymemory.translated.net/get?q={urllib.parse.quote(seg)}&langpair=en|zh"
                req = urllib.request.Request(url)
                req.add_header('User-Agent', 'Mozilla/5.0')
                
                with urllib.request.urlopen(req, timeout=30) as response:
                    result = json.loads(response.read().decode())
                
                if result.get('responseStatus') == 200:
                    translated_segments.append(result['responseData']['translatedText'])
                    success = True
                else:
                    translated_segments.append(seg)
                    success = True
                
                time.sleep(1.0 + random.random() * 0.5)  # 避免频率限制
                break
                
            except Exception:
                if attempt < max_retries - 1:
                    time.sleep(2)
                else:
                    translated_segments.append(seg)
        
        if not success:
            translated_segments.append(seg)
    
    return ''.join(translated_segments)
```

### txt_to_md() - 转换函数
```python
def txt_to_md(txt_file, md_file, title=""):
    """将txt文件转换为Markdown"""
    with open(txt_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 添加标题
    if title:
        md_content = f"# {title}\n\n{content}"
    else:
        md_content = content
    
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md_content)
```

## 批量处理模板 (translate_batch.py)
```python
def main():
    base = "你的工作目录"
    
    # 定义要处理的文件
    files = [
        # (原始txt, 输出txt, 输出md, 标题)
        ("course/Week1/lecture1.txt", "course/第一周/lecture1.txt", "course/第一周/lecture1.md", "第一讲"),
        ("course/Week1/lecture2.txt", "course/第一周/lecture2.txt", "course/第一周/lecture2.md", "第二讲"),
    ]
    
    for txt_orig, txt_zh, md_file, title in files:
        translate_and_convert(txt_orig, txt_zh, md_file, title)

if __name__ == "__main__":
    main()
```

## 常用命令速查

| 操作 | 命令 |
|------|------|
| 提取PDF文本 | `pdftotext -layout input.pdf output.txt` |
| 翻译txt | `python translator.py input.txt output.txt` |
| 批量翻译 | `python translate_batch.py` |
| txt转md | `cp file.txt file.md` |

## 注意事项
1. **频率限制**: MyMemory免费API限制约每秒1次请求
2. **文本长度**: 每段不超过400字符，否则会被截断
3. **PPT/PPTX**: 需要额外工具提取文本 (如 python-pptx 库)
4. **PDF扫描件**: 无法提取文本，需要OCR处理

## 文件清单
```
translator.py       - 核心翻译模块 (translate_text函数)
translate_batch.py - 批量处理脚本
SKILL-translate-pdf.md - 本文档
```
#!/usr/bin/env python3
"""Convert reveal.js lecture HTML to structured Markdown.
Extracts sections (slides), headings, lists, tables, code, math ($...$, \\(..\\)) as-is."""
import sys, re, glob, os
from html.parser import HTMLParser
from html import unescape

class SlideParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.slides = []          # list of slide dicts
        self.cur = None           # current slide buffer
        self.stack = []           # tag stack
        self.buf = None           # text buffer for current block
        self.block = None         # block type being captured
        self.list_stack = []      # ('ul'|'ol', indent)
        self.in_pre = False
        self.skip = 0             # depth of skipped tags (script/style/aside notes)

    # ---- helpers ----
    def flush_block(self):
        if self.buf is not None:
            text = re.sub(r'[ \t]+', ' ', self.buf).strip()
            text = re.sub(r'\s*\n\s*', '\n', text)
            if text:
                if self.block == 'li':
                    indent = '  ' * max(0, len(self.list_stack) - 1)
                    self.cur['body'].append(f"{indent}- {text}")
                elif self.block == 'table':
                    self.cur['body'].append(text)
                else:
                    self.cur['body'].append(text)
            self.buf = None

    def new_slide(self, attrs):
        if self.cur is not None:
            self.slides.append(self.cur)
        self.cur = {'title': '', 'body': []}

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('script', 'style', 'aside', 'nav'):
            self.skip += 1
            return
        if self.skip:
            return
        if tag == 'section':
            self.new_slide(attrs)
        elif self.cur is None:
            return
        elif tag in ('h1', 'h2', 'h3', 'h4'):
            self.flush_block()
            self.block, self.buf = 'h', ''
        elif tag == 'li':
            self.flush_block()
            self.block, self.buf = 'li', ''
        elif tag in ('ul', 'ol'):
            self.list_stack.append(tag)
            self.flush_block()
        elif tag == 'table':
            self.flush_block()
            self.block, self.buf = 'table', ''
        elif tag == 'tr':
            if self.block == 'table' and self.buf is not None:
                self.buf += '\n|'
            else:
                self.block, self.buf = 'table', '\n|'
        elif tag in ('td', 'th'):
            if self.block != 'table' or self.buf is None:
                self.block, self.buf = 'table', '\n|'
            self.buf += ' '
        elif tag == 'pre':
            self.flush_block()
            self.in_pre = True
            self.block, self.buf = 'pre', ''
        elif tag == 'br':
            if self.buf is not None:
                self.buf += '\n'
        elif tag == 'img':
            src = a.get('src', '')
            alt = a.get('alt', '')
            if src and not src.startswith('data:'):
                self.cur['body'].append(f"![{alt}]({src})")

    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'aside', 'nav'):
            self.skip = max(0, self.skip - 1)
            return
        if self.skip or self.cur is None:
            return
        if tag in ('h1', 'h2', 'h3', 'h4'):
            if self.buf is not None:
                t = re.sub(r'\s+', ' ', self.buf).strip()
                if t:
                    lvl = '#' * (int(tag[1]) + 1)  # h2 -> ###
                    if not self.cur['title']:
                        self.cur['title'] = t
                    self.cur['body'].insert(0, f"{lvl} {t}")
                self.buf, self.block = None, None
        elif tag == 'li':
            self.flush_block()
        elif tag in ('ul', 'ol'):
            if self.list_stack: self.list_stack.pop()
            self.flush_block()
        elif tag == 'table':
            self.flush_block()
        elif tag == 'pre':
            self.in_pre = False
            if self.buf is not None:
                code = self.buf.strip('\n')
                self.cur['body'].append(f"```\n{code}\n```")
                self.buf, self.block = None, None
        elif tag in ('p', 'div', 'span', 'figcaption'):
            self.flush_block()

    def handle_data(self, data):
        if self.skip or self.cur is None:
            return
        if self.buf is not None:
            self.buf += data
        else:
            text = data.strip()
            if text:
                self.cur['body'].append(text)

def convert(path):
    with open(path, encoding='utf-8') as f:
        html = f.read()
    # strip chalkboard canvas etc.
    html = re.sub(r'<canvas[^>]*>.*?</canvas>', '', html, flags=re.S)
    p = SlideParser()
    p.feed(html)
    if p.cur:
        p.slides.append(p.cur)
    out = []
    for i, s in enumerate(p.slides, 1):
        title = s['title'] or f'(slide {i})'
        out.append(f"\n<!-- slide {i} -->\n## {title}\n")
        body = [b for b in s['body'] if b.strip()]
        # dedupe consecutive identical lines
        dedup = []
        for b in body:
            if not dedup or dedup[-1] != b:
                dedup.append(b)
        out.append('\n'.join(dedup))
    md = '\n'.join(out)
    # collapse excess blank lines
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md

if __name__ == '__main__':
    src_dir, out_dir = sys.argv[1], sys.argv[2]
    for f in sorted(glob.glob(os.path.join(src_dir, 'html_*.html'))):
        name = os.path.basename(f)[5:-5]
        md = convert(f)
        with open(os.path.join(out_dir, name + '.md'), 'w', encoding='utf-8') as o:
            o.write(md)
        print(f"{name}.md: {len(md)} chars, ", len(md.splitlines()), "lines")

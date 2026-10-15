#!/usr/bin/env python3
"""Flatten slide-structured MD into continuous documents:
drop slide markers, no-title headings, images, and duplicate headings."""
import re, glob, os

def clean(text):
    # normalize heading levels first (### / #### per-slide -> ##)
    text = re.sub(r'^#### ', '## ', text, flags=re.M)
    text = re.sub(r'^### ', '## ', text, flags=re.M)
    lines = text.splitlines()
    out = []
    for ln in lines:
        s = ln.strip()
        # slide markers & no-title headings & images & XKCD credits
        if re.match(r'^<!-- slide \d+ -->$', s):
            continue
        if re.match(r'^#+ \(slide \d+\)$', s):
            continue
        if re.match(r'^!\[.*\]\(.*\)$', s):
            continue
        if s == 'XKCD':
            continue
        # duplicate headings separated only by blanks
        m = re.match(r'^(#{2,4}) (.+)$', s)
        if m:
            # find last non-blank emitted line
            j = len(out) - 1
            while j >= 0 and not out[j].strip():
                j -= 1
            if j >= 0:
                pm = re.match(r'^(#{2,4}) (.+)$', out[j].strip())
                if pm and pm.group(2) == m.group(2):
                    continue
        out.append(ln)
    text = '\n'.join(out)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip() + '\n'

if __name__ == '__main__':
    for f in sorted(glob.glob('md/*.md')):
        with open(f, encoding='utf-8') as fh:
            t = clean(fh.read())
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(t)
        print(f"{f}: {len(t.splitlines())} lines")

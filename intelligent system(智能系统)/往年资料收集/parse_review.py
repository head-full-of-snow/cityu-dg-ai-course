import re, html, sys

raw = open('review_experience.html', encoding='utf-8', errors='ignore').read()

# find script/data references
for m in re.finditer(r'(fetch\([^)]*\)|["\']([^"\']*\.(?:json|js|md))["\'])', raw):
    print("REF:", m.group(0)[:150])

print("---BODY TEXT---")
text = re.sub(r'<script.*?</script>|<style.*?</style>', '', raw, flags=re.S)
text = re.sub(r'<[^>]+>', ' ', text)
print(html.unescape(re.sub(r'\s+', ' ', text))[:1500])

"""Find keys in zh.json that still use English fallback values."""
import json, os

BASE = r'C:\Users\MTS\Music\Coding\MTSWebsite\2digix-business-it-solutions-html-template-2025-09-21-06-46-01-utc\digix-main\lang'

with open(os.path.join(BASE, 'en.json'), 'r', encoding='utf-8') as f:
    en = json.load(f)
with open(os.path.join(BASE, 'zh.json'), 'r', encoding='utf-8') as f:
    zh = json.load(f)

same = [k for k in en if k in zh and zh[k] == en[k]]
diff = [k for k in en if k in zh and zh[k] != en[k]]

print(f'Keys with English fallback (need Chinese translation): {len(same)}')
print(f'Keys already translated: {len(diff)}')
print()

# Group by category
categories = {}
for k in same:
    cat = k.split('.')[0]
    categories.setdefault(cat, []).append(k)

for cat in sorted(categories):
    keys = categories[cat]
    print(f'--- {cat} ({len(keys)} keys) ---')
    for k in keys[:10]:
        print(f'  {k}: {en[k][:60]}')
    if len(keys) > 10:
        print(f'  ... and {len(keys)-10} more')
    print()

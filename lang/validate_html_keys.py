import json, os, re, glob

srcdir = r'C:\Users\MTS\Music\Coding\MTSWebsite\2digix-business-it-solutions-html-template-2025-09-21-06-46-01-utc\digix-main'
lang_dir = os.path.join(srcdir, 'lang')

with open(os.path.join(lang_dir, 'en.json'), 'r', encoding='utf-8') as f: en = json.load(f)
with open(os.path.join(lang_dir, 'fr.json'), 'r', encoding='utf-8') as f: fr = json.load(f)
with open(os.path.join(lang_dir, 'zh.json'), 'r', encoding='utf-8') as f: zh = json.load(f)

missing_in_en = []
missing_in_fr = []
missing_in_zh = []

for html_file in sorted(glob.glob(os.path.join(srcdir, '*.html'))):
    with open(html_file, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    refs = re.findall(r'data-i18n[-a-z]*=[\"\']([^\"\']+)[\"\']', content)
    for ref in refs:
        if ref not in en:
            missing_in_en.append((os.path.basename(html_file), ref))
        if ref not in fr:
            missing_in_fr.append((os.path.basename(html_file), ref))
        if ref not in zh:
            missing_in_zh.append((os.path.basename(html_file), ref))

print(f'Missing in en.json: {len(missing_in_en)}')
for f, k in missing_in_en[:20]:
    print(f'  {f}: {k}')
print(f'Missing in fr.json: {len(missing_in_fr)}')
for f, k in missing_in_fr[:20]:
    print(f'  {f}: {k}')
print(f'Missing in zh.json: {len(missing_in_zh)}')
for f, k in missing_in_zh[:20]:
    print(f'  {f}: {k}')

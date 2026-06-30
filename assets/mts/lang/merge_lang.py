import json, os

d = r'C:\Users\MTS\Music\Coding\MTSWebsite\2digix-business-it-solutions-html-template-2025-09-21-06-46-01-utc\digix-main\lang'

with open(os.path.join(d, 'en.json'), 'r', encoding='utf-8') as f:
    en = json.load(f)
with open(os.path.join(d, 'fr.json'), 'r', encoding='utf-8') as f:
    fr = json.load(f)
with open(os.path.join(d, 'zh.json'), 'r', encoding='utf-8') as f:
    zh = json.load(f)

# Add missing keys with English fallback
added_fr = 0
added_zh = 0
for k, v in en.items():
    if k not in fr:
        fr[k] = v
        added_fr += 1
    if k not in zh:
        zh[k] = v
        added_zh += 1

# Write back
with open(os.path.join(d, 'fr.json'), 'w', encoding='utf-8') as f:
    json.dump(fr, f, ensure_ascii=False, indent=4)
with open(os.path.join(d, 'zh.json'), 'w', encoding='utf-8') as f:
    json.dump(zh, f, ensure_ascii=False, indent=4)

print(f"en.json: {len(en)} keys")
print(f"fr.json: {len(fr)} keys (+{added_fr} English fallback)")
print(f"zh.json: {len(zh)} keys (+{added_zh} English fallback)")

# Validate
for name, data in [('en', en), ('fr', fr), ('zh', zh)]:
    keys = set(data.keys())
    en_keys = set(en.keys())
    missing = en_keys - keys
    extra = keys - en_keys
    print(f"{name}: missing={len(missing)}, extra={len(extra)}")
    if missing:
        for k in sorted(missing)[:5]:
            print(f"  missing: {k}")

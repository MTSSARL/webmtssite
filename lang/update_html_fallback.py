"""
Update fallback text in all HTML files to match en.json values.
For each element with data-i18n="KEY", replaces the visible text content
with the corresponding value from en.json.
"""
import re, json, os

BASE = r'C:\Users\MTS\Music\Coding\MTSWebsite\2digix-business-it-solutions-html-template-2025-09-21-06-46-01-utc\digix-main'

with open(os.path.join(BASE, 'lang', 'en.json'), 'r', encoding='utf-8') as f:
    en = json.load(f)

html_files = [f for f in sorted(os.listdir(BASE)) if f.endswith('.html') and 'hiolle' not in f]

def html_escape(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

def read_html(path):
    """Try UTF-8 first, fall back to Latin-1, then re-save as UTF-8."""
    with open(path, 'rb') as f:
        raw = f.read()
    try:
        return raw.decode('utf-8')
    except UnicodeDecodeError:
        text = raw.decode('latin-1')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
        return text

def update_file(filepath):
    html = read_html(filepath)

    original = html

    # Sort keys by length descending to avoid partial key matches
    keys = sorted(en.keys(), key=len, reverse=True)

    for key, value in en.items():
        if not value:
            continue

        escaped_key = re.escape(key)
        safe_value = html_escape(value)

        # 1. Meta tags: <meta ... data-i18n="KEY" ... content="OLD">
        meta_pat = re.compile(
            rf'(<meta[^>]*?data-i18n="{escaped_key}"[^>]*?content=)"([^"]*)"',
            re.IGNORECASE
        )
        html = meta_pat.sub(r'\1"' + safe_value.replace('"', '&quot;') + '"', html)

        # 2. Title tag: <title data-i18n="KEY">OLD</title>
        title_pat = re.compile(
            rf'(<title[^>]*?data-i18n="{escaped_key}"[^>]*?>)(.*?)(</title>)',
            re.IGNORECASE | re.DOTALL
        )
        html = title_pat.sub(r'\1' + safe_value + r'\3', html)

        # 3. Regular elements with data-i18n attribute (not meta/title)
        # Capture tag name as group 2 for backreference in closing tag
        elem_pat = re.compile(
            rf'(<(\w+)[^>]*?data-i18n="{escaped_key}"[^>]*?>)([\s\S]*?)(</\2>)',
            re.IGNORECASE
        )

        def make_replacer(k, v, sv):
            def replacer(m):
                open_tag = m.group(1)
                content = m.group(3)
                close_tag = m.group(4)

                # SplitText headings: replace only the inner text span's content
                if 'rts-text-anime-style-1' in open_tag:
                    span_pat = re.compile(r'<span>([\s\S]*?)</span>')
                    replaced = False
                    for sp_match in span_pat.finditer(content):
                        inner = sp_match.group(1)
                        if '<img' not in inner and '<span' not in inner:
                            start = sp_match.start(1)
                            end = sp_match.end(1)
                            content = content[:start] + v + content[end:]
                            replaced = True
                            break
                    if not replaced:
                        # No text span found, replace entire content
                        content = v
                    return open_tag + content + close_tag

                # For <span> elements that themselves have data-i18n, the content is the text
                return open_tag + v + close_tag
            return replacer

        html = elem_pat.sub(make_replacer(key, safe_value, safe_value), html)

    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        return True
    return False

count = 0
for fname in html_files:
    fpath = os.path.join(BASE, fname)
    if update_file(fpath):
        print(f"Updated: {fname}")
        count += 1
    else:
        print(f"No changes: {fname}")

print(f"\nDone. {count}/{len(html_files)} files updated.")

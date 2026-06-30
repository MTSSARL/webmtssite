"""Update client and partner logo references in index.html."""
import os, re

BASE = r'C:\Users\MTS\Music\Coding\MTSWebsite\2digix-business-it-solutions-html-template-2025-09-21-06-46-01-utc\digix-main'
CLIENT_DIR = os.path.join(BASE, 'assets', 'images', 'client-logos')
PARTNER_DIR = os.path.join(BASE, 'assets', 'images', 'partner-logos')

# --- Create missing partner SVG logos ---
partner_svgs = {
    'sick.svg': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 60"><rect width="200" height="60" fill="#FFED00" rx="4"/><text x="100" y="38" font-family="Arial,sans-serif" font-size="24" font-weight="bold" fill="#000" text-anchor="middle">SICK</text></svg>',
    'abb.svg': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 60"><rect width="200" height="60" fill="#fff" rx="4"/><text x="100" y="38" font-family="Arial,sans-serif" font-size="28" font-weight="bold" fill="#E30613" text-anchor="middle">ABB</text></svg>',
    'omron.svg': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 60"><rect width="200" height="60" fill="#fff" rx="4"/><text x="100" y="38" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#00A4E4" text-anchor="middle">OMRON</text></svg>',
    'smc.svg': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 60"><rect width="200" height="60" fill="#fff" rx="4"/><text x="100" y="38" font-family="Arial,sans-serif" font-size="24" font-weight="bold" fill="#003399" text-anchor="middle">SMC</text></svg>',
}

for fname, content in partner_svgs.items():
    fpath = os.path.join(PARTNER_DIR, fname)
    if not os.path.exists(fpath):
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Created: {fname}')

# --- Update index.html ---
fpath = os.path.join(BASE, 'index.html')
with open(fpath, 'r', encoding='utf-8') as f:
    html = f.read()

# Client logos: 10 slides with 7 MTS clients + 3 repeats
client_logos = [
    ('Marelli', 'marelli.svg'),
    ('APTIV', 'aptiv.svg'),
    ('TE Connectivity', 'te-connectivity.svg'),
    ('OPmobility', 'opmobility.svg'),
    ('SOGEFI', 'sogefi.svg'),
    ('Triumph', 'triumph.svg'),
    ('ECI', 'eci.svg'),
    ('Marelli', 'marelli.svg'),
    ('APTIV', 'aptiv.svg'),
    ('TE Connectivity', 'te-connectivity.svg'),
]

# Replace client logos by counting occurrences
client_pattern = '<img src="assets/images/client-logos/placeholder.svg" alt="Client Logo">'
for i, (name, svg_file) in enumerate(client_logos):
    new = f'<img src="assets/images/client-logos/{svg_file}" alt="{name}">'
    html = html.replace(client_pattern, new, 1)
    print(f'Client {i+1}: {name}')

# Partner logos: replace both src and alt by position
# Original HTML order: 1.Siemens 2.Keyence 3.Festo 4.Schneider 5.Allen-Bradley 6.SMC 7.Mitsubishi 8.Omron 9.ABB 10.Beckhoff
# New order:              1.Siemens 2.Fanuc  3.Cognex 4.Keyence   5.SICK       6.ABB 7.Omron   8.SMC   9.Mitsubishi 10.Beckhoff
partner_updates = [
    ('Siemens', 'siemens.svg'),
    ('Fanuc', 'fanuc.svg'),
    ('Cognex', 'cognex.svg'),
    ('Keyence', 'keyence.svg'),
    ('SICK', 'sick.svg'),
    ('ABB', 'abb.svg'),
    ('Omron', 'omron.svg'),
    ('SMC', 'smc.svg'),
    ('Mitsubishi Electric', 'placeholder.svg'),
    ('Beckhoff', 'placeholder.svg'),
]

# Use regex to find each partner-logo-item and replace the img inside
# Find all partner-logo-item divs
pat = re.compile(r'(<div class="partner-logo-item">\s*<img[^>]*>)(\s*</div>)')
matches = list(pat.finditer(html))

for i, m in enumerate(matches):
    if i >= len(partner_updates):
        break
    name, svg_file = partner_updates[i]
    if svg_file != 'placeholder.svg':
        new_img = f'<img src="assets/images/partner-logos/{svg_file}" alt="{name}">'
        new_div = f'<div class="partner-logo-item">{new_img}</div>'
        html = html.replace(m.group(0), new_div, 1)
        print(f'Partner {i+1}: {name} -> {svg_file}')
    else:
        # Keep placeholder but update alt text
        new_img = f'<img src="assets/images/partner-logos/placeholder.svg" alt="{name}">'
        new_div = f'<div class="partner-logo-item">{new_img}</div>'
        html = html.replace(m.group(0), new_div, 1)
        print(f'Partner {i+1}: {name} (placeholder)')

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(html)

print('\nDone. index.html updated.')

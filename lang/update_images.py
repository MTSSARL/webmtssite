import shutil, os

base = r'C:\Users\MTS\Music\Coding\MTSWebsite\2digix-business-it-solutions-html-template-2025-09-21-06-46-01-utc\digix-main'
temp = os.path.join(base, 'assets', 'images', 'temp')

# Map: (old_path, new_filename) -> (source_in_temp, description)
entries = [
    ('about/01.webp',       'factory-automation.jpg',       'mts-automation-scene.jpg',      'Factory automation scene'),
    ('about/02.webp',       'control-panel.jpg',            'mts-control-panel.jpg',         'Electrical control panel'),
    ('case/01.webp',        'robot-arm.jpg',                'mts-robotic-arm.jpg',           'Industrial robot arm'),
    ('case/02.webp',        'assembly-line.jpg',            'mts-assembly-line.jpg',         'Automated assembly line'),
    ('case/03.webp',        'automotive-manufacturing.jpg', 'mts-automotive.jpg',            'Automotive manufacturing'),
    ('case/04.webp',        'vision-inspection.jpg',        'mts-vision-inspection.jpg',     'Machine vision inspection'),
    ('achievement/01.webp', 'conveyor-system.jpg',          'mts-conveyor-system.jpg',       'Conveyor system'),
    ('blog/01.webp',        'engineer-control-panel.jpg',   'mts-engineer-panel.jpg',        'Engineer at control panel'),
    ('blog/02.webp',        'quality-inspection.jpg',       'mts-quality-control.jpg',       'Quality inspection'),
    ('blog/03.webp',        'industrial-workshop.jpg',      'mts-industrial-workshop.jpg',   'Industrial workshop'),
    ('service/13.webp',     'control-panel.jpg',            'mts-electrical-cabinet.jpg',    'Electrical cabinet'),
]

html_files = [
    'index.html', 'about.html', 'service.html', 'service-details.html',
    'team.html', 'team-single.html', 'contact.html',
    'why-choose-us.html', 'partner.html', 'industry.html',
]

copied = []
for old_rel, src_name, dst_name, desc in entries:
    src_path = os.path.join(temp, src_name)
    if not os.path.exists(src_path):
        print(f"  SKIP {src_name} (not found)")
        continue
    dst_dir = os.path.join(base, 'assets', 'images', os.path.dirname(old_rel))
    dst_path = os.path.join(dst_dir, dst_name)
    os.makedirs(dst_dir, exist_ok=True)
    shutil.copy2(src_path, dst_path)
    print(f"  OK   {src_name} -> {dst_name}  ({desc})")
    copied.append((old_rel, dst_name))

if not copied:
    print("No images were copied!")
    exit(1)

print(f"\nCopied {len(copied)} images. Updating HTML references...")

total_updates = 0
for html_name in html_files:
    html_path = os.path.join(base, html_name)
    if not os.path.exists(html_path):
        continue
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    changed_any = False
    for old_rel, dst_name in copied:
        old_path = f'assets/images/{old_rel}'
        new_path = f'assets/images/{os.path.dirname(old_rel)}/{dst_name}'
        for attr in ['src="', "src='", 'poster="', 'srcset="']:
            old_ref = f'{attr}{old_path}'
            new_ref = f'{attr}{new_path}'
            if old_ref in content:
                content = content.replace(old_ref, new_ref)
                changed_any = True
    if changed_any:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Updated {html_name}")
        total_updates += 1
    else:
        print(f"  No changes in {html_name}")

print(f"\nDone! Updated {total_updates} HTML files.")
print("All images from Pexels (free for commercial use, no attribution required).")

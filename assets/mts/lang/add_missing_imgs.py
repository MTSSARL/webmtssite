import json, os

d = r'C:\Users\MTS\Music\Coding\MTSWebsite\2digix-business-it-solutions-html-template-2025-09-21-06-46-01-utc\digix-main\lang'

for fname in ['en.json', 'fr.json', 'zh.json']:
    with open(os.path.join(d, fname), 'r', encoding='utf-8') as f:
        data = json.load(f)

    en = data if fname == 'en.json' else None
    if fname == 'en.json':
        data['industry.banner.img'] = 'Industries We Serve'
        data['industry.railway.img'] = 'Railway Systems'
        data['industry.aerospace.img'] = 'Aerospace & Defense'
        data['team.banner.img'] = 'Our Team'
    elif fname == 'fr.json':
        data['industry.banner.img'] = 'Secteurs d\'Activit\u00e9'
        data['industry.railway.img'] = 'Syst\u00e8mes Ferroviaires'
        data['industry.aerospace.img'] = 'A\u00e9rospatial & D\u00e9fense'
        data['team.banner.img'] = 'Notre \u00c9quipe'
    elif fname == 'zh.json':
        data['industry.banner.img'] = '我们服务的行业'
        data['industry.railway.img'] = '铁路系统'
        data['industry.aerospace.img'] = '航空航天与国防'
        data['team.banner.img'] = '我们的团队'

    with open(os.path.join(d, fname), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

print('Added 4 missing image alt keys to all 3 files')

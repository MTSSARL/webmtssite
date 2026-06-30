import json, sys, os

srcdir = r"C:\Users\MTS\Music\Coding\MTSWebsite\2digix-business-it-solutions-html-template-2025-09-21-06-46-01-utc\digix-main"

def set_nested(ht, path, value):
    parts = path.split('.')
    for p in parts[:-1]:
        if p not in ht:
            ht[p] = {}
        ht = ht[p]
    ht[parts[-1]] = value

# Read flat en.json for missing key detection
with open(os.path.join(srcdir, 'lang', 'en.json'), 'r', encoding='utf-8') as f:
    flat_en = json.load(f)

# Translation map: [key, en, fr, zh]
translations = [
    # === META ===
    ('meta.title', 'MTS - Manufacturing System Technology', 'MTS - Technologie des Systèmes de Fabrication', 'MTS - 制造系统技术'),
    ('meta.desc', 'MTS: electrical equipment, electronic assemblies, special machines, robotic integration, maintenance and industrial equipment distribution.', 'MTS : équipements électriques, assemblages électroniques, machines spéciales, intégration robotique, maintenance et distribution d\'équipements industriels.', 'MTS：电气设备、电子装配、特种机械、机器人集成、维护及工业设备分销'),

    # === NAV ===
    ('nav.home', 'Home', 'Accueil', '首页'),
    ('nav.about', 'About', 'À propos', '关于我们'),
    ('nav.about_mts', 'About MTS', 'À propos de MTS', '关于MTS'),
    ('nav.our_team', 'Our Team', 'Notre Équipe', '我们的团队'),
    ('nav.why_choose_us', 'Why Choose Us', 'Pourquoi Nous Choisir', '为什么选择我们'),
    ('nav.our_partners', 'Our Partners', 'Nos Partenaires', '我们的合作伙伴'),
    ('nav.services', 'Services', 'Services', '服务'),
    ('nav.electrical_equipment', 'Electrical Equipment', 'Équipement Électrique', '电气设备'),
    ('nav.electronic_assemblies', 'Electronic Assemblies', 'Assemblages Électroniques', '电子装配'),
    ('nav.special_machines_robotics', 'Special Machines & Robotics', 'Machines Spéciales & Robotique', '特种机械与机器人'),
    ('nav.maintenance_repair', 'Maintenance & Repair', 'Maintenance & Réparation', '维护与修理'),
    ('nav.equipment_distribution', 'Equipment Distribution', "Distribution d'Équipement", '设备分销'),
    ('nav.contact', 'Contact', 'Contact', '联系方式'),
    ('nav.contact_us', 'Contact Us', 'Contactez-Nous', '联系我们'),
    ('nav.partners', 'Partners', 'Partenaires', '合作伙伴'),
    ('nav.team', 'Team', 'Équipe', '团队'),
    ('nav.why', 'Why Choose Us', 'Pourquoi Nous Choisir', '为什么选择我们'),
    ('nav.about.mts', 'About MTS', 'À propos de MTS', '关于MTS'),
    ('nav.contact.us', 'Contact Us', 'Contactez-Nous', '联系我们'),
    ('nav.services.distribution', 'Equipment Distribution', "Distribution d'Équipement", '设备分销'),
    ('nav.services.electrical', 'Electrical Equipment', 'Équipement Électrique', '电气设备'),
    ('nav.services.electronics', 'Electronic Assemblies', 'Assemblages Électroniques', '电子装配'),
    ('nav.services.machines', 'Special Machines & Robotics', 'Machines Spéciales & Robotique', '特种机械与机器人'),
    ('nav.services.maintenance', 'Maintenance & Repair', 'Maintenance & Réparation', '维护与修理'),

    # === HERO ===
    ('hero.title', 'Comprehensive Industrial Solutions for Every Sector', 'Solutions Industrielles Complètes pour Tous les Secteurs', '适用于各行各业的全面工业解决方案'),
    ('hero.pre_title', 'Manufacturing System Technology', 'Technologie des Systèmes de Fabrication', '制造系统技术'),
    ('hero.desc', 'MTS delivers tailored industrial services from electrical equipment design to robotic integration, maintenance, and technical support.', 'MTS fournit des services industriels sur mesure, de la conception d\'équipements électriques à l\'intégration robotique, la maintenance et le support technique.', 'MTS提供从电气设备设计到机器人集成、维护和技术支持的定制化工业服务。'),
    ('hero.learn_more', 'Learn More', 'En Savoir Plus', '了解更多'),
    ('hero.btn', 'Learn More', 'En Savoir Plus', '了解更多'),
    ('hero.welcome', 'Welcome to MTS', 'Bienvenue chez MTS', '欢迎来到MTS'),

    # === GLOBAL ===
    ('global.learn_more', 'Learn More', 'En Savoir Plus', '了解更多'),

    # === BREADCRUMB ===
    ('breadcrumb.about', 'About', 'À propos', '关于我们'),
    ('breadcrumb.services', 'Services', 'Services', '服务'),
    ('breadcrumb.team', 'Team', 'Équipe', '团队'),

    # === INDEX - ABOUT ===
    ('index.about.pre', 'About MTS', 'À propos de MTS', '关于MTS'),
    ('index.about.title', 'Innovative Industrial Solutions Powering Your Business', 'Solutions Industrielles Innovantes pour Votre Entreprise', '推动您业务的创新工业解决方案'),
    ('index.about.desc1', 'MTS is an industrial services company specializing in electrical equipment design, electronic assemblies, special machine manufacturing, robotic integration, and industrial maintenance.', 'MTS est une société de services industriels spécialisée dans la conception d\'équipements électriques, les assemblages électroniques, la fabrication de machines spéciales, l\'intégration robotique et la maintenance industrielle.', 'MTS是一家专注于电气设备设计、电子装配、特种机械制造、机器人集成和工业维护的工业服务公司。'),
    ('index.about.desc2', 'With over 15 years of experience, production sites in France, Morocco, America, and Canada, we serve railway, aeronautics, defense, energy, medical, and general industry sectors.', 'Avec plus de 15 ans d\'expérience et des sites de production en France, au Maroc, en Amérique et au Canada, nous servons les secteurs ferroviaire, aéronautique, défense, énergie, médical et industrie générale.', '凭借超过15年的经验，我们在法国、摩洛哥、美国和加拿大设有生产基地，服务于铁路、航空、国防、能源、医疗和一般工业领域。'),
    ('index.about.quote', 'Excellence in every connection', "L'excellence dans chaque connexion", '每一个连接的卓越'),
    ('index.about.employees', 'Skilled Employees', 'Employés Qualifiés', '技术员工'),
    ('index.about.employees_num', '300+', '300+', '300+'),
    ('index.about.employees_text', 'Skilled Professionals', 'Professionnels Qualifiés', '专业技术人才'),
    ('index.about.sites', 'Production Sites', 'Sites de Production', '生产基地'),
    ('index.about.btn', 'Learn More About MTS', 'En Savoir Plus sur MTS', '了解更多关于MTS'),
    ('index.about.learn_more', 'Learn More About MTS', 'En Savoir Plus sur MTS', '了解更多关于MTS'),

    # === INDEX - SERVICES ===
    ('index.services.pre', 'Our Services', 'Nos Services', '我们的服务'),
    ('index.services.title', 'Comprehensive Industrial Solutions', 'Solutions Industrielles Complètes', '全面的工业解决方案'),
    ('index.services.desc', 'From electrical equipment design to robotic integration and maintenance', 'De la conception d\'équipements électriques à l\'intégration robotique et la maintenance', '从电气设备设计到机器人集成与维护'),
    ('index.services.card1_title', 'Electrical Equipment', 'Équipement Électrique', '电气设备'),
    ('index.services.card1_desc', 'Design, manufacturing, and integration of electrical cabinets, control panels, and wiring systems for industrial applications.', 'Conception, fabrication et intégration d\'armoires électriques, de panneaux de contrôle et de systèmes de câblage pour applications industrielles.', '工业用电气柜、控制面板和布线系统的设计、制造与集成。'),
    ('index.services.card2_title', 'Electronic Assemblies', 'Assemblages Électroniques', '电子装配'),
    ('index.services.card2_desc', 'Custom electronic board assembly, wiring harnesses, and mechatronic subsystem production.', 'Assemblage de cartes électroniques sur mesure, faisceaux de câbles et production de sous-systèmes mécatroniques.', '定制电子板组装、线束及机电子系统生产。'),
    ('index.services.card3_title', 'Special Machines & Robotics', 'Machines Spéciales & Robotique', '特种机械与机器人'),
    ('index.services.card3_desc', 'Design and manufacturing of special-purpose machines and robotic integration for production automation.', 'Conception et fabrication de machines spéciales et intégration robotique pour l\'automatisation de la production.', '专用机械的设计制造及生产自动化中的机器人集成。'),
    ('index.services.card4_title', 'Maintenance & Repair', 'Maintenance & Réparation', '维护与修理'),
    ('index.services.card4_desc', 'Industrial equipment maintenance, repair, on-site support, and technical assistance for manufacturing operations.', 'Maintenance d\'équipements industriels, réparation, support sur site et assistance technique pour les opérations de fabrication.', '工业设备维护、修理、现场支持及制造运营技术援助。'),
    ('index.services.electrical.title', 'Electrical Equipment', 'Équipement Électrique', '电气设备'),
    ('index.services.electrical.desc', 'Design, manufacturing, and integration of electrical cabinets and control panels.', 'Conception, fabrication et intégration d\'armoires électriques et de panneaux de contrôle.', '电气柜和控制面板的设计、制造与集成。'),
    ('index.services.electronics.title', 'Electronic Assemblies', 'Assemblages Électroniques', '电子装配'),
    ('index.services.electronics.desc', 'Custom electronic board assembly and wiring harness production.', 'Assemblage de cartes électroniques sur mesure et production de faisceaux de câbles.', '定制电子板组装与线束生产。'),
    ('index.services.machines.title', 'Special Machines & Robotics', 'Machines Spéciales & Robotique', '特种机械与机器人'),
    ('index.services.machines.desc', 'Design and manufacturing of special-purpose machines with robotic integration.', 'Conception et fabrication de machines spéciales avec intégration robotique.', '带机器人集成的专用机械设计与制造。'),
    ('index.services.maintenance.title', 'Maintenance & Repair', 'Maintenance & Réparation', '维护与修理'),
    ('index.services.maintenance.desc', 'Industrial equipment maintenance, repair, and on-site technical support.', 'Maintenance d\'équipements industriels, réparation et support technique sur site.', '工业设备维护、修理及现场技术支持。'),
    ('index.services.distribution.title', 'Equipment Distribution', "Distribution d'Équipement", '设备分销'),
    ('index.services.distribution.desc', 'Distribution of industrial electrical equipment and components.', 'Distribution d\'équipements électriques industriels et de composants.', '工业电气设备和元件的分销。'),
    ('index.services.btn', 'View All Services', 'Voir Tous les Services', '查看所有服务'),
    ('index.services.view_all', 'View All Services', 'Voir Tous les Services', '查看所有服务'),

    # === INDEX - ACHIEVEMENTS ===
    ('index.achievements.pre', 'Our Achievements', 'Nos Réalisations', '我们的成就'),
    ('index.achievements.title', 'Delivering Excellence Across Industries', "L'Excellence au Service de l'Industrie", '跨行业交付卓越'),
    ('index.achievements.projects', 'Projects Completed', 'Projets Réalisés', '已完成项目'),
    ('index.achievements.projects_done', 'Projects Completed', 'Projets Réalisés', '已完成项目'),

    # === INDEX - VIDEO ===
    ('index.video.pre', 'Our Expertise', 'Notre Expertise', '我们的专长'),
    ('index.video.title', 'See Our Work in Action', 'Voir Notre Travail en Action', '观看我们的实际工作'),
    ('index.video.desc', 'Take a closer look at our facilities, projects, and industrial capabilities.', 'Découvrez nos installations, projets et capacités industrielles.', '近距离了解我们的设施、项目和工业能力。'),
    ('index.video.card1_title', 'Electrical Manufacturing', 'Fabrication Électrique', '电气制造'),
    ('index.video.card1.title', 'Electrical Manufacturing', 'Fabrication Électrique', '电气制造'),
    ('index.video.card1.desc', 'Precision electrical cabinet manufacturing and wiring.', 'Fabrication de précision d\'armoires électriques et câblage.', '精密电气柜制造与布线。'),
    ('index.video.card1_location', 'Tangier Facility', 'Site de Tanger', '丹吉尔工厂'),
    ('index.video.card2_title', 'Robotic Integration', 'Intégration Robotique', '机器人集成'),
    ('index.video.card2.title', 'Robotic Integration', 'Intégration Robotique', '机器人集成'),
    ('index.video.card2.desc', 'Advanced robotic cell integration and programming.', 'Intégration et programmation de cellules robotiques avancées.', '先进的机器人单元集成与编程。'),
    ('index.video.card2_desc', 'Advanced robotic cell integration and programming.', 'Intégration et programmation de cellules robotiques avancées.', '先进的机器人单元集成与编程。'),
]

# Now add the remaining translation map entries from the original script
more_translations = [
    # === INDEX - SOLUTIONS ===
    ('index.solutions.pre', 'Case Studies', 'Études de Cas', '案例研究'),
    ('index.solutions.title', 'Transforming Industries with Technical Excellence', 'Transformer les Industries avec l\'Excellence Technique', '以技术卓越推动行业转型'),
    ('index.solutions.desc', 'Real-world projects demonstrating our engineering capabilities across sectors.', 'Projets concrets démontrant nos capacités d\'ingénierie dans tous les secteurs.', '展示我们跨行业工程能力的实际项目。'),
    ('index.solutions.case1_title', 'Railway Signaling System Upgrade', 'Modernisation du Système de Signalisation Ferroviaire', '铁路信号系统升级'),
    ('index.solutions.case1_industry', 'Railway', 'Ferroviaire', '铁路'),
    ('index.solutions.case2_title', 'Aerospace Component Assembly Line', "Chaîne d'Assemblage de Composants Aérospatiaux", '航空航天部件装配线'),
    ('index.solutions.case2_industry', 'Aerospace', 'Aérospatial', '航空航天'),
    ('index.solutions.case3_title', 'Automated Warehouse System', "Système d'Entrepôt Automatisé", '自动化仓储系统'),
    ('index.solutions.case3_industry', 'Logistics', 'Logistique', '物流'),
    ('index.solutions.case4_title', 'Medical Device Manufacturing', 'Fabrication de Dispositifs Médicaux', '医疗设备制造'),
    ('index.solutions.case4_industry', 'Medical', 'Médical', '医疗'),
    ('index.solutions.case5_title', 'Energy Grid Control System', 'Système de Contrôle du Réseau Énergétique', '能源电网控制系统'),
    ('index.solutions.case5_industry', 'Energy', 'Énergie', '能源'),
    ('index.solutions.case6_title', 'Defense Equipment Integration', "Intégration d'Équipements de Défense", '国防装备集成'),
    ('index.solutions.case6_industry', 'Defense', 'Défense', '国防'),
    ('index.solutions.btn', 'View All Case Studies', 'Voir Toutes les Études de Cas', '查看所有案例研究'),
    ('index.cases.pre', 'Case Studies', 'Études de Cas', '案例研究'),
    ('index.cases.title', 'Transforming Industries with Technical Excellence', 'Transformer les Industries avec l\'Excellence Technique', '以技术卓越推动行业转型'),
    ('index.cases.desc', 'Real-world projects demonstrating our engineering capabilities.', 'Projets concrets démontrant nos capacités d\'ingénierie.', '展示我们工程能力的实际项目。'),
    ('index.cases.btn', 'View All Cases', 'Voir Tous les Projets', '查看所有项目'),

    # === INDEX - VALUES ===
    ('index.values.pre', 'Our Values', 'Nos Valeurs', '我们的价值观'),
    ('index.values.title', 'Empowering Industry with Engineering Excellence', 'Autonomiser l\'Industrie avec l\'Excellence Technique', '以工程卓越赋能工业'),
    ('index.values.desc', 'Our principles guide every project we deliver.', 'Nos principes guident chaque projet que nous réalisons.', '我们的原则指导着我们交付的每一个项目。'),
    ('index.values.check1', 'Quality assurance across all projects', 'Assurance qualité sur tous les projets', '所有项目的质量保证'),
    ('index.values.check2', 'On-time delivery commitment', 'Engagement de livraison dans les délais', '按时交付承诺'),
    ('index.values.check3', 'ISO-certified processes', 'Processus certifiés ISO', 'ISO认证流程'),
    ('index.values.item1', 'Quality assurance across all projects', 'Assurance qualité sur tous les projets', '所有项目的质量保证'),
    ('index.values.item2', 'On-time delivery commitment', 'Engagement de livraison dans les délais', '按时交付承诺'),
    ('index.values.item3', 'ISO-certified processes', 'Processus certifiés ISO', 'ISO认证流程'),
    ('index.values.btn', 'Learn More About Our Values', 'En Savoir Plus sur Nos Valeurs', '了解更多关于我们的价值观'),

    # === INDEX - TEAM ===
    ('index.team.pre', 'Our Team', 'Notre Équipe', '我们的团队'),
    ('index.team.title', 'The People Behind Our Success', 'Les Personnes Derrière Notre Succès', '我们成功背后的人们'),
    ('index.team.desc', 'Meet our experienced team of engineers and industrial specialists.', 'Rencontrez notre équipe expérimentée d\'ingénieurs et de spécialistes industriels.', '认识我们经验丰富的工程师和工业专家团队。'),
    ('index.team.member1.name', 'Ahmed El Amrani', 'Ahmed El Amrani', '艾哈迈德·阿尔·阿姆拉尼'),
    ('index.team.member1.role', 'CEO & Founder', 'PDG & Fondateur', '首席执行官兼创始人'),
    ('index.team.member2.name', 'Fatima Zahra Benali', 'Fatima Zahra Benali', '法蒂玛·扎赫拉·本纳利'),
    ('index.team.member2.role', 'Chief Operations Officer', 'Directrice des Opérations', '首席运营官'),
    ('index.team.member3.name', 'Youssef El Khatib', 'Youssef El Khatib', '优素福·阿尔·哈提卜'),
    ('index.team.member3.role', 'Technical Director', 'Directeur Technique', '技术总监'),
    ('index.team.member4.name', 'Sofia Bennani', 'Sofia Bennani', '索菲亚·本纳尼'),
    ('index.team.member4.role', 'Quality & Compliance Manager', 'Responsable Qualité & Conformité', '质量与合规经理'),
    ('index.team.btn', 'Meet The Full Team', 'Rencontrer Toute l\'Équipe', '见见整个团队'),

    # === INDEX - TESTIMONIALS ===
    ('index.testimonials.pre', 'Testimonials', 'Témoignages', '客户评价'),
    ('index.testimonials.title', 'Success Stories from Our Clients', 'Témoignages de Nos Clients', '来自客户的成功故事'),
    ('index.testimonials.desc', 'Hear from our clients about their experience working with MTS.', 'Écoutez nos clients parler de leur expérience avec MTS.', '听听我们的客户讲述他们与MTS合作的经历。'),
    ('index.testimonials.1.name', 'Jean-Pierre Dubois', 'Jean-Pierre Dubois', '让-皮埃尔·杜布瓦'),
    ('index.testimonials.1.quote', 'MTS delivered exceptional electrical systems for our railway infrastructure project. Their precision and timeliness exceeded our expectations.', 'MTS a livré des systèmes électriques exceptionnels pour notre projet d\'infrastructure ferroviaire. Leur précision et leur respect des délais ont dépassé nos attentes.', 'MTS为我们的铁路基础设施项目交付了卓越的电气系统。他们的精准度和及时性超出了我们的预期。'),
    ('index.testimonials.1.role', 'Project Director, RailCorp', 'Directeur de Projet, RailCorp', '项目总监，RailCorp'),
    ('index.testimonials.2.name', 'Maria Garcia', 'Maria Garcia', '玛丽亚·加西亚'),
    ('index.testimonials.2.quote', 'The robotic integration MTS implemented transformed our production line efficiency. Highly recommended.', "L'intégration robotique réalisée par MTS a transformé l'efficacité de notre chaîne de production. Hautement recommandé.", 'MTS实施的机器人集成改变了我们的生产线效率。强烈推荐。'),
    ('index.testimonials.2.role', 'Manufacturing Director, AeroTech', 'Directrice de Production, AeroTech', '制造总监，AeroTech'),
    ('index.testimonials.3.name', 'Thomas Mueller', 'Thomas Mueller', '托马斯·穆勒'),
    ('index.testimonials.3.quote', 'Their maintenance team keeps our equipment running at peak performance. Reliable and professional.', 'Leur équipe de maintenance maintient nos équipements à des performances optimales. Fiable et professionnelle.', '他们的维护团队让我们的设备保持最佳运行状态。可靠且专业。'),
    ('index.testimonials.3.role', 'Operations Manager, MediDev', 'Responsable des Opérations, MediDev', '运营经理，MediDev'),
    ('index.testimonials.4.name', 'Sarah Johnson', 'Sarah Johnson', '莎拉·约翰逊'),
    ('index.testimonials.4.quote', 'From design to installation, MTS handled our electronic assembly project with complete professionalism.', 'De la conception à l\'installation, MTS a géré notre projet d\'assemblage électronique avec un professionnalisme complet.', '从设计到安装，MTS以完全的专业精神处理了我们的电子装配项目。'),
    ('index.testimonials.4.role', 'Procurement Lead, EnergySys', 'Responsable des Achats, EnergySys', '采购主管，EnergySys'),
    ('index.testimonials.5.name', 'Carlos Mendez', 'Carlos Mendez', '卡洛斯·门德斯'),
    ('index.testimonials.5.quote', 'The custom machine MTS built for us exceeded specifications. True engineering excellence.', 'La machine spéciale que MTS a construite pour nous a dépassé les spécifications. Une véritable excellence technique.', 'MTS为我们制造的定制设备超出了规格要求。真正的工程卓越。'),
    ('index.testimonials.5.role', 'Technical Director, IndusLog', 'Directeur Technique, IndusLog', '技术总监，IndusLog'),
    ('index.testimonials.t1_name', 'Jean-Pierre Dubois', 'Jean-Pierre Dubois', '让-皮埃尔·杜布瓦'),
    ('index.testimonials.t1_role', 'Project Director, RailCorp', 'Directeur de Projet, RailCorp', '项目总监，RailCorp'),
    ('index.testimonials.t4_text', 'MTS delivered exceptional electrical systems for our railway infrastructure project.', 'MTS a livré des systèmes électriques exceptionnels pour notre projet d\'infrastructure ferroviaire.', 'MTS为我们的铁路基础设施项目交付了卓越的电气系统。'),

    # === INDEX - CLIENTS ===
    ('index.clients.pre', 'Our Clients', 'Nos Clients', '我们的客户'),
    ('index.clients.title', 'Trusted by Industry Leaders', 'Approuvé par les Leaders de l\'Industrie', '受到行业领袖的信赖'),

    # === INDEX - BLOG ===
    ('index.blog.pre', 'News & Insights', 'Actualités et Perspectives', '新闻与观点'),
    ('index.blog.title', 'Latest Industry Updates', 'Dernières Nouvelles de l\'Industrie', '最新行业动态'),
    ('index.blog.desc', 'Stay updated with the latest trends, projects, and innovations in industrial services.', 'Restez informé des dernières tendances, projets et innovations dans les services industriels.', '随时了解工业服务领域的最新趋势、项目和创新。'),
    ('index.blog.1.cat', 'Technology', 'Technologie', '技术'),
    ('index.blog.1.title', 'Advancements in Industrial Automation for 2025', 'Avancées de l\'Automatisation Industrielle pour 2025', '2025年工业自动化进展'),
    ('index.blog.2.cat', 'Projects', 'Projets', '项目'),
    ('index.blog.2.title', 'MTS Completes Major Railway Electrification Project', 'MTS Achève un Grand Projet d\'Électrification Ferroviaire', 'MTS完成重大铁路电气化项目'),
    ('index.blog.3.cat', 'Innovation', 'Innovation', '创新'),
    ('index.blog.3.title', 'New Robotic Integration Techniques in Manufacturing', 'Nouvelles Techniques d\'Intégration Robotique dans la Fabrication', '制造业中的新型机器人集成技术'),
    ('index.blog.post1_category', 'Technology', 'Technologie', '技术'),
    ('index.blog.post1_title', 'Advancements in Industrial Automation for 2025', 'Avancées de l\'Automatisation Industrielle pour 2025', '2025年工业自动化进展'),
    ('index.blog.post2_category', 'Projects', 'Projets', '项目'),
    ('index.blog.post2_title', 'MTS Completes Major Railway Electrification Project', 'MTS Achève un Grand Projet d\'Électrification Ferroviaire', 'MTS完成重大铁路电气化项目'),
    ('index.blog.post3_category', 'Innovation', 'Innovation', '创新'),
    ('index.blog.post3_title', 'New Robotic Integration Techniques in Manufacturing', 'Nouvelles Techniques d\'Intégration Robotique dans la Fabrication', '制造业中的新型机器人集成技术'),
    ('index.blog.btn', 'Read More Articles', 'Lire Plus d\'Articles', '阅读更多文章'),

    # === INDEX - FAQ ===
    ('index.faq.pre', 'FAQ', 'FAQ', '常见问题'),
    ('index.faq.title', 'Everything You Need to Know About Our Services', 'Tout ce que Vous Devez Savoir sur Nos Services', '关于我们的服务您需要了解的一切'),
    ('index.faq.desc', 'Find answers to common questions about MTS and our industrial services.', 'Trouvez des réponses aux questions courantes sur MTS et nos services industriels.', '查找关于MTS及我们工业服务的常见问题解答。'),
    ('index.faq.q1', 'What industries does MTS serve?', 'Dans quels secteurs MTS intervient-il ?', 'MTS服务于哪些行业？'),
    ('index.faq.a1', 'MTS serves railway, civil and military aeronautics, defense, energy, medical, robotics, automation, and general industry sectors across Europe, Africa, and North America.', 'MTS intervient dans les secteurs ferroviaire, aéronautique civil et militaire, défense, énergie, médical, robotique, automatisation et industrie générale en Europe, Afrique et Amérique du Nord.', 'MTS服务于欧洲、非洲和北美的铁路、民航与军用航空、国防、能源、医疗、机器人、自动化和一般工业领域。'),
    ('index.faq.q2', 'Where are your production facilities?', 'Où se trouvent vos sites de production ?', '您的生产基地在哪里？'),
    ('index.faq.a2', 'MTS has 11 production sites in France and international locations in Morocco (Tangier), America, and Canada, enabling us to serve clients worldwide.', 'MTS possède 11 sites de production en France et des implantations internationales au Maroc (Tanger), en Amérique et au Canada, nous permettant de servir des clients dans le monde entier.', 'MTS在法国拥有11个生产基地，并在摩洛哥（丹吉尔）、美洲和加拿大设有国际分支机构，使我们能够服务全球客户。'),
    ('index.faq.q3', 'How can I request a quote or consultation?', 'Comment demander un devis ou une consultation ?', '如何索取报价或咨询？'),
    ('index.faq.a3', 'Simply fill out the contact form on our website, call our team directly, or email us. We typically respond within 24 hours.', 'Remplissez simplement le formulaire de contact sur notre site, appelez notre équipe directement ou envoyez-nous un email. Nous répondons généralement sous 24 heures.', '只需填写我们网站上的联系表格、直接致电我们的团队或发送电子邮件。我们通常在24小时内回复。'),

    # === INDEX - MAP ===
    ('index.map.pre', 'Our Location', 'Notre Emplacement', '我们的位置'),
    ('index.map.title', 'Find Us', 'Nous Trouver', '找到我们'),
    ('index.map.address', 'Z.A.E Bni Ouassine, Lot 58, Tanger, Morocco', 'Z.A.E Bni Ouassine, Lot 58, Tanger, Maroc', '摩洛哥丹吉尔Bni Ouassine工业区58号'),
    ('index.map.address_label', 'Address', 'Adresse', '地址'),
    ('index.map.email_label', 'Email', 'Email', '邮箱'),
    ('index.map.phone_label', 'Phone', 'Téléphone', '电话'),
    ('index.map.directions', 'Get Directions on Google Maps', "Obtenir l'itinéraire sur Google Maps", '在谷歌地图上获取路线'),
    ('index.map.popup.title', 'MTS SRL', 'MTS SRL', 'MTS SRL'),
    ('index.map.popup.address', 'Z.A.E Bni Ouassine, Lot 58<br>Tanger, Morocco<br>+212 6 63 22 83 22', 'Z.A.E Bni Ouassine, Lot 58<br>Tanger, Maroc<br>+212 6 63 22 83 22', 'Z.A.E Bni Ouassine, Lot 58<br>摩洛哥丹吉尔<br>+212 6 63 22 83 22'),
    ('index.map.card.address', 'Address', 'Adresse', '地址'),
    ('index.map.card.address.val', 'Z.A.E Bni Ouassine, Lot 58, Tanger, Morocco', 'Z.A.E Bni Ouassine, Lot 58, Tanger, Maroc', '摩洛哥丹吉尔Bni Ouassine工业区58号'),
    ('index.map.card.email', 'Email', 'Email', '邮箱'),
    ('index.map.card.email.val', 'contact@mts-industries.com', 'contact@mts-industries.com', 'contact@mts-industries.com'),
    ('index.map.card.phone', 'Phone', 'Téléphone', '电话'),
    ('index.map.card.phone.val', '+212 6 63 22 83 22', '+212 6 63 22 83 22', '+212 6 63 22 83 22'),

    # === INDEX - PARTNERS ===
    ('index.partners.pre', 'Technology Partners', 'Partenaires Technologiques', '技术合作伙伴'),
    ('index.partners.title', 'Equipment We Work With', 'Équipement avec Lequel Nous Travaillons', '我们合作的设备'),
    ('index.partners.desc', 'We partner with leading industrial technology manufacturers to deliver the best solutions.', 'Nous nous associons aux principaux fabricants de technologies industrielles pour offrir les meilleures solutions.', '我们与领先的工业技术制造商合作，提供最佳解决方案。'),

    # === INDEX - CONTACT FORM ===
    ('index.form.title', 'Send Us a Message', 'Envoyez-Nous un Message', '给我们留言'),
    ('index.form.name', 'Your Name', 'Votre Nom', '您的姓名'),
    ('index.form.email', 'Your Email', 'Votre Email', '您的邮箱'),
    ('index.form.phone', 'Your Phone', 'Votre Téléphone', '您的电话'),
    ('index.form.subject', 'Subject', 'Sujet', '主题'),
    ('index.form.message', 'Your Message', 'Votre Message', '您的留言'),
    ('index.form.submit', 'Send Message', 'Envoyer le Message', '发送留言'),
    ('index.form.privacy', 'You agree to our privacy policy', 'Vous acceptez notre politique de confidentialité', '您同意我们的隐私政策'),
    ('index.contact.title', 'Send Us a Message', 'Envoyez-Nous un Message', '给我们留言'),
    ('index.contact.full_name', 'Full Name', 'Nom Complet', '姓名'),
    ('index.contact.email', 'Email Address', 'Adresse Email', '邮箱地址'),
    ('index.contact.phone', 'Phone Number', 'Numéro de Téléphone', '电话号码'),
    ('index.contact.message', 'Your Message', 'Votre Message', '您的留言'),
    ('index.contact.send', 'Send Message', 'Envoyer le Message', '发送留言'),
    ('index.contact.company', 'Company', 'Société', '公司'),

    # === ABOUT ===
    ('about.meta.title', 'About MTS - Manufacturing System Technology', 'À propos de MTS - Technologie des Systèmes de Fabrication', '关于MTS - 制造系统技术'),
    ('about.meta.desc', 'Learn about MTS: our mission, values, team, and manufacturing expertise across 11 production sites in France and international locations.', 'Découvrez MTS : notre mission, nos valeurs, notre équipe et notre expertise de fabrication sur 11 sites de production en France et à l\'international.', '了解MTS：我们的使命、价值观、团队以及遍布法国11个生产基地和国际地点的制造专长。'),
    ('about.breadcrumb.home', 'Home', 'Accueil', '首页'),
    ('about.breadcrumb.about', 'About', 'À propos', '关于我们'),
    ('about.hero.title', 'Empowering Industry Through Engineering Excellence', 'Autonomiser l\'Industrie par l\'Excellence Technique', '以工程卓越赋能工业'),
    ('about.banner.title', 'About MTS', 'À propos de MTS', '关于MTS'),
    ('about.banner.img', 'About MTS Banner', 'Bannière À propos de MTS', '关于MTS横幅'),
    ('about.mission.title', 'Our Mission', 'Notre Mission', '我们的使命'),
    ('about.mission.label', 'Our Mission', 'Notre Mission', '我们的使命'),
    ('about.mission.desc', 'MTS is dedicated to providing innovative industrial solutions that drive efficiency, quality, and safety across manufacturing sectors worldwide. We combine technical expertise with a commitment to excellence in every project.', 'MTS se consacre à fournir des solutions industrielles innovantes qui améliorent l\'efficacité, la qualité et la sécurité dans les secteurs de la fabrication dans le monde entier. Nous combinons l\'expertise technique avec un engagement d\'excellence dans chaque projet.', 'MTS致力于提供创新的工业解决方案，提升全球制造业的效率、质量和安全性。我们在每个项目中都结合了技术专长和对卓越的承诺。'),
    ('about.mission.years', 'Years of Experience', 'Années d\'Expérience', '多年经验'),
    ('about.mission.years_exp', 'Years of Experience', 'Années d\'Expérience', '多年经验'),
    ('about.mission.sites', 'Production Sites', 'Sites de Production', '生产基地'),
    ('about.mission.production_sites', 'Production Sites', 'Sites de Production', '生产基地'),
    ('about.mission.employees', 'Skilled Employees', 'Employés Qualifiés', '技术员工'),
    ('about.mission.skilled_employees', 'Skilled Employees', 'Employés Qualifiés', '技术员工'),
    ('about.mission.excellence', 'Excellence in every connection', "L'excellence dans chaque connexion", '每一个连接的卓越'),

    ('about.values.pre', 'Company Values', 'Valeurs de l\'Entreprise', '公司价值观'),
    ('about.values.title', 'Our Values in Action', 'Nos Valeurs en Action', '我们的价值观在行动中'),
    ('about.values.innovation_title', 'Innovation', 'Innovation', '创新'),
    ('about.values.quality_title', 'Quality', 'Qualité', '质量'),
    ('about.values.safety_title', 'Safety', 'Sécurité', '安全'),
    ('about.values.respect_title', 'Respect', 'Respect', '尊重'),
    ('about.values.engagement_title', 'Engagement', 'Engagement', '承诺'),
    ('about.values.1.title', 'Innovation', 'Innovation', '创新'),
    ('about.values.1.desc', 'Continuously pushing the boundaries of industrial technology to deliver cutting-edge solutions.', 'Repousser constamment les limites de la technologie industrielle pour offrir des solutions de pointe.', '不断突破工业技术的界限，提供尖端解决方案。'),
    ('about.values.2.title', 'Quality', 'Qualité', '质量'),
    ('about.values.2.desc', 'Rigorous quality control processes ensuring every product meets the highest standards.', 'Des processus de contrôle qualité rigoureux garantissant que chaque produit répond aux normes les plus élevées.', '严格的质量控制流程，确保每个产品都符合最高标准。'),
    ('about.values.3.title', 'Safety', 'Sécurité', '安全'),
    ('about.values.3.desc', 'Commitment to workplace safety and compliance with international safety regulations.', 'Engagement envers la sécurité au travail et conformité aux réglementations de sécurité internationales.', '致力于工作场所安全并遵守国际安全法规。'),
    ('about.values.4.title', 'Respect', 'Respect', '尊重'),
    ('about.values.4.desc', 'Building lasting relationships based on mutual respect with clients, partners, and employees.', 'Bâtir des relations durables basées sur le respect mutuel avec les clients, les partenaires et les employés.', '与客户、合作伙伴和员工建立基于相互尊重的持久关系。'),
    ('about.values.5.title', 'Engagement', 'Engagement', '承诺'),
    ('about.values.5.desc', 'Dedicated to delivering on our promises with accountability and transparency.', 'Dévoués à tenir nos promesses avec responsabilité et transparence.', '以责任心和透明度履行我们的承诺。'),

    ('about.team.pre', 'Leadership Team', 'Équipe de Direction', '领导团队'),
    ('about.team.title', 'Meet the People Behind MTS', 'Rencontrez l\'Équipe derrière MTS', '认识MTS背后的团队'),
    ('about.team.member1.name', 'Ahmed El Amrani', 'Ahmed El Amrani', '艾哈迈德·阿尔·阿姆拉尼'),
    ('about.team.member1.role', 'CEO & Founder', 'PDG & Fondateur', '首席执行官兼创始人'),
    ('about.team.member2.name', 'Fatima Zahra Benali', 'Fatima Zahra Benali', '法蒂玛·扎赫拉·本纳利'),
    ('about.team.member2.role', 'Chief Operations Officer', 'Directrice des Opérations', '首席运营官'),
    ('about.team.member3.name', 'Youssef El Khatib', 'Youssef El Khatib', '优素福·阿尔·哈提卜'),
    ('about.team.member3.role', 'Technical Director', 'Directeur Technique', '技术总监'),
    ('about.team.member4.name', 'Sofia Bennani', 'Sofia Bennani', '索菲亚·本纳尼'),
    ('about.team.member4.role', 'Quality & Compliance Manager', 'Responsable Qualité & Conformité', '质量与合规经理'),

    ('about.process.pre', 'Our Process', 'Notre Processus', '我们的流程'),
    ('about.process.title', 'How We Deliver Excellence', 'Comment Nous Offrons l\'Excellence', '我们如何交付卓越'),
    ('about.process.step1.title', 'Consultation', 'Consultation', '咨询'),
    ('about.process.step1.desc', 'Understanding your requirements and project goals through in-depth consultation.', 'Compréhension de vos besoins et objectifs de projet grâce à une consultation approfondie.', '通过深入咨询了解您的需求和项目目标。'),
    ('about.process.step2.title', 'Design & Engineering', 'Conception & Ingénierie', '设计与工程'),
    ('about.process.step2.desc', 'Developing detailed designs and engineering solutions tailored to your specifications.', 'Développement de conceptions détaillées et de solutions d\'ingénierie adaptées à vos spécifications.', '根据您的规格制定详细的设计和工程解决方案。'),
    ('about.process.step3.title', 'Manufacturing', 'Fabrication', '制造'),
    ('about.process.step3.desc', 'Precision manufacturing using state-of-the-art equipment and ISO-certified processes.', 'Fabrication de précision utilisant des équipements de pointe et des processus certifiés ISO.', '使用最先进的设备和ISO认证流程进行精密制造。'),
    ('about.process.step4.title', 'Delivery & Support', 'Livraison & Support', '交付与支持'),
    ('about.process.step4.desc', 'On-time delivery with comprehensive installation, testing, and ongoing support.', 'Livraison dans les délais avec installation complète, tests et support continu.', '按时交付，提供全面的安装、测试和持续支持。'),

    ('about.map.pre', 'Our Location', 'Notre Emplacement', '我们的位置'),
    ('about.map.title', 'Find Us', 'Nous Trouver', '找到我们'),
    ('about.cta.title', 'Ready to Start Your Next Industrial Project?', 'Prêt à Commencer Votre Prochain Projet Industriel ?', '准备好开始您的下一个工业项目了吗？'),
    ('about.cta.desc', 'Contact our team today to discuss your requirements and discover how MTS can power your industrial operations.', 'Contactez notre équipe dès aujourd\'hui pour discuter de vos besoins et découvrir comment MTS peut dynamiser vos opérations industrielles.', '立即联系我们的团队讨论您的需求，了解MTS如何推动您的工业运营。'),
    ('about.cta.btn', 'Get In Touch', 'Prenez Contact', '联系我们'),
    ('about.cta.button', 'Get In Touch', 'Prenez Contact', '联系我们'),

    # === CONTACT ===
    ('contact.meta.title', 'Contact Us - MTS - Manufacturing System Technology', 'Contactez-Nous - MTS - Technologie des Systèmes de Fabrication', '联系我们 - MTS - 制造系统技术'),
    ('contact.meta.desc', 'Contact MTS for industrial services: electrical equipment, electronic assemblies, robotics, maintenance, and equipment distribution.', 'Contactez MTS pour les services industriels : équipements électriques, assemblages électroniques, robotique, maintenance et distribution d\'équipements.', '联系MTS获取工业服务：电气设备、电子装配、机器人、维护和设备分销。'),
    ('contact.breadcrumb.home', 'Home', 'Accueil', '首页'),
    ('contact.breadcrumb.contact', 'Contact', 'Contact', '联系方式'),
    ('contact.hero.title', 'Get in Touch', 'Prendre Contact', '取得联系'),
    ('contact.hero.desc', 'Have a project in mind? Contact our team to discuss your industrial service needs.', 'Vous avez un projet en tête ? Contactez notre équipe pour discuter de vos besoins en services industriels.', '有项目在考虑？请联系我们的团队讨论您的工业服务需求。'),
    ('contact.banner.title', 'Contact Us', 'Contactez-Nous', '联系我们'),
    ('contact.banner.desc', 'Have a project in mind? Contact our team to discuss your industrial service needs.', 'Vous avez un projet en tête ? Contactez notre équipe pour discuter de vos besoins en services industriels.', '有项目在考虑？请联系我们的团队讨论您的工业服务需求。'),

    ('contact.info.headquarters', 'Our Headquarters', 'Notre Siège', '我们的总部'),
    ('contact.info.email_us', 'Email Us', 'Envoyez-Nous un Email', '给我们发邮件'),
    ('contact.info.call_us', 'Call Us', 'Appelez-Nous', '给我们打电话'),
    ('contact.card.address.title', 'Our Address', 'Notre Adresse', '我们的地址'),
    ('contact.card.address.val', 'Z.A.E Bni Ouassine, Lot 58, Tanger, Morocco', 'Z.A.E Bni Ouassine, Lot 58, Tanger, Maroc', '摩洛哥丹吉尔Bni Ouassine工业区58号'),
    ('contact.card.email.title', 'Email', 'Email', '邮箱'),
    ('contact.card.email.desc', 'contact@mts-industries.com', 'contact@mts-industries.com', 'contact@mts-industries.com'),
    ('contact.card.phone.title', 'Phone', 'Téléphone', '电话'),
    ('contact.card.phone.desc', '+212 6 63 22 83 22', '+212 6 63 22 83 22', '+212 6 63 22 83 22'),

    ('contact.form.first_name', 'First Name', 'Prénom', '名字'),
    ('contact.form.last_name', 'Last Name', 'Nom', '姓氏'),
    ('contact.form.firstname', 'First Name', 'Prénom', '名字'),
    ('contact.form.lastname', 'Last Name', 'Nom', '姓氏'),
    ('contact.form.email', 'Email', 'Email', '邮箱'),
    ('contact.form.phone', 'Phone', 'Téléphone', '电话'),
    ('contact.form.subject_label', 'Subject', 'Sujet', '主题'),
    ('contact.form.subject_default', 'General Inquiry', 'Demande Générale', '一般咨询'),
    ('contact.form.subject.general', 'General Inquiry', 'Demande Générale', '一般咨询'),
    ('contact.form.subject.electrical', 'Electrical Equipment', 'Équipement Électrique', '电气设备'),
    ('contact.form.subject.electronics', 'Electronic Assemblies', 'Assemblages Électroniques', '电子装配'),
    ('contact.form.subject.machines', 'Special Machines & Robotics', 'Machines Spéciales & Robotique', '特种机械与机器人'),
    ('contact.form.subject.maintenance', 'Maintenance & Repair', 'Maintenance & Réparation', '维护与修理'),
    ('contact.form.subject.distribution', 'Equipment Distribution', "Distribution d'Équipement", '设备分销'),
    ('contact.form.help_label', 'How can we help you?', 'Comment pouvons-nous vous aider ?', '我们如何帮助您？'),
    ('contact.form.send', 'Send Message', 'Envoyer le Message', '发送留言'),
    ('contact.form.submit', 'Send Message', 'Envoyer le Message', '发送留言'),
    ('contact.form.agree', 'You agree to our privacy policy', 'Vous acceptez notre politique de confidentialité', '您同意我们的隐私政策'),
    ('contact.form.privacy', 'privacy policy', 'politique de confidentialité', '隐私政策'),
    ('contact.form.message', 'Your Message', 'Votre Message', '您的留言'),
    ('contact.form.first_name_placeholder', 'Your Name', 'Votre Prénom', '您的名字'),
    ('contact.form.email_placeholder', 'email@example.com', 'email@exemple.com', 'email@example.com'),
    ('contact.form.phone_placeholder', 'Phone Number', 'Numéro de Téléphone', '电话号码'),
    ('contact.form.message_placeholder', 'Describe your project or inquiry...', 'Décrivez votre projet ou demande...', '描述您的项目或咨询...'),

    ('contact.faq.title', 'Frequently Asked Questions', 'Questions Fréquemment Posées', '常见问题'),
    ('contact.faq.q1', 'What industries do you serve?', 'Dans quels secteurs intervenez-vous ?', '你们服务于哪些行业？'),
    ('contact.faq.a1', 'MTS serves railway, civil and military aeronautics, defense, energy, medical, robotics, automation, and general industry sectors.', 'MTS intervient dans les secteurs ferroviaire, aéronautique civil et militaire, défense, énergie, médical, robotique, automatisation et industrie générale.', 'MTS服务于铁路、民航与军用航空、国防、能源、医疗、机器人、自动化和一般工业领域。'),
    ('contact.faq.q2', 'Where are your production facilities located?', 'Où se trouvent vos sites de production ?', '您的生产设施位于何处？'),
    ('contact.faq.a2', 'We have 11 production sites in France and international locations in Morocco, America, and Canada.', 'Nous avons 11 sites de production en France et des implantations internationales au Maroc, en Amérique et au Canada.', '我们在法国拥有11个生产基地，并在摩洛哥、美洲和加拿大设有国际分支机构。'),
    ('contact.faq.q3', 'How do I request a quote?', 'Comment demander un devis ?', '如何索取报价？'),
    ('contact.faq.a3', 'Simply fill out the contact form on this page or call our team directly, and we will respond within 24 hours.', 'Remplissez simplement le formulaire de contact sur cette page ou appelez notre équipe directement, et nous répondrons sous 24 heures.', '只需填写此页面上的联系表格或直接致电我们的团队，我们将在24小时内回复。'),

    # === SERVICE ===
    ('service.meta.title', 'Our Services - MTS - Manufacturing System Technology', 'Nos Services - MTS - Technologie des Systèmes de Fabrication', '我们的服务 - MTS - 制造系统技术'),
    ('service.meta.desc', 'Explore MTS industrial services: electrical equipment, electronic assemblies, special machines, robotics, maintenance, and equipment distribution.', 'Découvrez les services industriels de MTS : équipements électriques, assemblages électroniques, machines spéciales, robotique, maintenance et distribution d\'équipements.', '探索MTS工业服务：电气设备、电子装配、特种机械、机器人、维护和设备分销。'),
    ('service.breadcrumb.home', 'Home', 'Accueil', '首页'),
    ('service.breadcrumb.services', 'Services', 'Services', '服务'),
    ('service.banner.title', 'Comprehensive Industrial Solutions', 'Solutions Industrielles Complètes', '全面的工业解决方案'),

    ('service.card.electrical.title', 'Electrical Equipment', 'Équipement Électrique', '电气设备'),
    ('service.card.electrical.desc', 'Design, manufacturing, and integration of electrical cabinets, control panels, and wiring systems for industrial applications.', 'Conception, fabrication et intégration d\'armoires électriques, de panneaux de contrôle et de systèmes de câblage.', '工业电气柜、控制面板和布线系统的设计、制造与集成。'),
    ('service.card.electronics.title', 'Electronic Assemblies', 'Assemblages Électroniques', '电子装配'),
    ('service.card.electronics.desc', 'Custom electronic board assembly, wiring harnesses, and mechatronic subsystem production.', 'Assemblage de cartes électroniques sur mesure, faisceaux de câbles et sous-systèmes mécatroniques.', '定制电子板组装、线束和机电子系统生产。'),
    ('service.card.machines.title', 'Special Machines & Robotics', 'Machines Spéciales & Robotique', '特种机械与机器人'),
    ('service.card.machines.desc', 'Custom machine design and robotic integration for production automation.', 'Conception de machines spéciales et intégration robotique pour l\'automatisation.', '定制机械设计与机器人集成实现生产自动化。'),
    ('service.card.maintenance.title', 'Maintenance & Repair', 'Maintenance & Réparation', '维护与修理'),
    ('service.card.maintenance.desc', 'Industrial equipment maintenance, repair, on-site support, and technical assistance.', 'Maintenance d\'équipements industriels, réparation, support sur site et assistance technique.', '工业设备维护、修理、现场支持和技术援助。'),
    ('service.card.distribution.title', 'Equipment Distribution', "Distribution d'Équipement", '设备分销'),
    ('service.card.distribution.desc', 'Distribution of industrial electrical equipment and components from leading manufacturers.', 'Distribution d\'équipements électriques industriels et de composants des principaux fabricants.', '领先制造商的工业电气设备和元件分销。'),
    ('service.card.consulting.title', 'Technical Consulting', 'Consulting Technique', '技术咨询'),
    ('service.card.consulting.desc', 'Expert technical consulting for industrial automation and manufacturing optimization.', 'Conseil technique expert pour l\'automatisation industrielle et l\'optimisation de la fabrication.', '工业自动化和制造优化的专业技术咨询。'),

    ('service.expertise.pre', 'Our Expertise', 'Notre Expertise', '我们的专长'),
    ('service.expertise.title', 'Expert Industrial Solutions to Power Your Business Growth', 'Solutions Industrielles Expertes pour Alimenter Votre Croissance', '专家级工业解决方案推动您的业务增长'),
    ('service.expertise.desc', 'With over 15 years of experience across multiple industries, MTS delivers tailored solutions that meet the highest standards of quality and safety.', 'Avec plus de 15 ans d\'expérience dans de multiples secteurs, MTS fournit des solutions sur mesure qui répondent aux normes les plus élevées de qualité et de sécurité.', '凭借超过15年的跨行业经验，MTS提供符合最高质量和安全标准的定制解决方案。'),
    ('service.expertise.btn', 'Learn More', 'En Savoir Plus', '了解更多'),

    ('service.why.pre', 'Why Choose MTS', 'Pourquoi Choisir MTS', '为什么选择MTS'),
    ('service.why.title', 'Why Choose MTS for Your Industrial Projects', 'Pourquoi Choisir MTS pour Vos Projets Industriels', '为什么选择MTS承接您的工业项目'),
    ('service.why.1.title', 'Proven Track Record', 'Parcours Éprouvé', '经证实的业绩'),
    ('service.why.1.desc', 'Over 15 years of successful project delivery across railway, aerospace, defense, energy, and medical sectors.', 'Plus de 15 ans de réalisation réussie de projets dans les secteurs ferroviaire, aérospatial, défense, énergie et médical.', '超过15年在铁路、航空航天、国防、能源和医疗领域成功交付项目的经验。'),
    ('service.why.2.title', 'Multi-Site Capability', 'Capacité Multi-Sites', '多场地能力'),
    ('service.why.2.desc', '11 production sites in France plus international facilities in Morocco, America, and Canada for global reach.', '11 sites de production en France plus des installations internationales au Maroc, en Amérique et au Canada pour une portée mondiale.', '法国11个生产基地以及摩洛哥、美洲和加拿大的国际设施，覆盖全球。'),
    ('service.why.3.title', 'Certified Quality', 'Qualité Certifiée', '认证质量'),
    ('service.why.3.desc', 'ISO-certified processes with rigorous quality control and safety compliance across all operations.', 'Processus certifiés ISO avec contrôle qualité rigoureux et conformité sécurité dans toutes les opérations.', 'ISO认证流程，在所有运营中实施严格的质量控制和安全管理。'),

    ('service.cta.title', 'Need a Custom Industrial Solution?', 'Besoin d\'une Solution Industrielle Sur Mesure ?', '需要定制的工业解决方案？'),
    ('service.cta.desc', 'Contact our engineering team to discuss your specific requirements.', 'Contactez notre équipe d\'ingénierie pour discuter de vos besoins spécifiques.', '联系我们的工程团队讨论您的具体需求。'),
    ('service.cta.btn', 'Contact Us Today', 'Contactez-Nous', '立即联系我们'),

    # === SERVICE DETAILS ===
    ('details.meta.title', 'Service Details - MTS - Manufacturing System Technology', 'Détails du Service - MTS - Technologie des Systèmes de Fabrication', '服务详情 - MTS - 制造系统技术'),
    ('details.meta.desc', 'Detailed information about MTS industrial services including electrical equipment design, electronic assemblies, and robotic integration.', 'Informations détaillées sur les services industriels de MTS, y compris la conception d\'équipements électriques, les assemblages électroniques et l\'intégration robotique.', '关于MTS工业服务的详细信息，包括电气设备设计、电子装配和机器人集成。'),
    ('details.breadcrumb.home', 'Home', 'Accueil', '首页'),
    ('details.breadcrumb.services', 'Services', 'Services', '服务'),
    ('details.breadcrumb.details', 'Service Details', 'Détails du Service', '服务详情'),
    ('details.banner.title', 'Service Details', 'Détails du Service', '服务详情'),

    ('details.process.pre', 'Our Process', 'Notre Processus', '我们的流程'),
    ('details.process.title', 'How We Deliver Excellence', 'Comment Nous Offrons l\'Excellence', '我们如何交付卓越'),
    ('details.process.step1.title', 'Consultation & Analysis', 'Consultation & Analyse', '咨询与分析'),
    ('details.process.step1.desc', 'Understanding your requirements and conducting feasibility analysis.', 'Compréhension de vos besoins et analyse de faisabilité.', '了解您的需求并进行可行性分析。'),
    ('details.process.step2.title', 'Design & Engineering', 'Conception & Ingénierie', '设计与工程'),
    ('details.process.step2.desc', 'Detailed engineering design with CAD modeling and technical specifications.', 'Conception technique détaillée avec modélisation CAO et spécifications techniques.', '使用CAD建模和技术规格进行详细的工程设计。'),
    ('details.process.step3.title', 'Manufacturing & Assembly', 'Fabrication & Assemblage', '制造与装配'),
    ('details.process.step3.desc', 'Precision manufacturing, assembly, and quality testing.', 'Fabrication de précision, assemblage et tests qualité.', '精密制造、装配和质量测试。'),
    ('details.process.step4.title', 'Delivery & Support', 'Livraison & Support', '交付与支持'),
    ('details.process.step4.desc', 'On-time delivery with installation and ongoing technical support.', 'Livraison dans les délais avec installation et support technique continu.', '按时交付并提供安装和持续技术支持。'),

    ('details.faq.pre', 'FAQ', 'FAQ', '常见问题'),
    ('details.faq.title', 'Frequently Asked Questions', 'Questions Fréquemment Posées', '常见问题'),
    ('details.faq.q1', 'What is the typical project timeline?', 'Quel est le calendrier typique d\'un projet ?', '典型的项目周期是多久？'),
    ('details.faq.a1', 'Project timelines vary by complexity. Most projects range from 4-12 weeks from design to delivery.', 'Les délais varient selon la complexité. La plupart des projets durent de 4 à 12 semaines, de la conception à la livraison.', '项目周期因复杂程度而异。大多数项目从设计到交付需要4-12周。'),
    ('details.faq.q2', 'Do you offer international shipping?', 'Proposez-vous l\'expédition internationale ?', '你们提供国际运输吗？'),
    ('details.faq.a2', 'Yes, we ship to clients worldwide from our production facilities in France, Morocco, America, and Canada.', 'Oui, nous expédions vers des clients dans le monde entier depuis nos sites de production en France, au Maroc, en Amérique et au Canada.', '是的，我们从法国、摩洛哥、美洲和加拿大的生产基地向全球客户发货。'),
    ('details.faq.q3', 'What certifications do you hold?', 'Quelles certifications possédez-vous ?', '你们拥有哪些认证？'),
    ('details.faq.a3', 'We hold ISO 9001:2015, ISO 14001, and various industry-specific certifications.', 'Nous détenons les certifications ISO 9001:2015, ISO 14001 et diverses certifications spécifiques à l\'industrie.', '我们拥有ISO 9001:2015、ISO 14001以及各种行业特定认证。'),

    ('details.cta.title', 'Need Custom Electrical Equipment?', 'Besoin d\'un Équipement Électrique Sur Mesure ?', '需要定制电气设备？'),
    ('details.cta.desc', 'Contact our engineering team to discuss your specifications.', 'Contactez notre équipe d\'ingénierie pour discuter de vos spécifications.', '联系我们的工程团队讨论您的规格要求。'),
    ('details.cta.btn', 'Get In Touch', 'Prenez Contact', '联系我们'),

    # === TEAM ===
    ('team.meta.title', 'Our Team - MTS - Manufacturing System Technology', 'Notre Équipe - MTS - Technologie des Systèmes de Fabrication', '我们的团队 - MTS - 制造系统技术'),
    ('team.meta.desc', 'Meet the management and engineering team at MTS. Experienced professionals in industrial electrical systems, electronics, robotics, and manufacturing.', 'Rencontrez l\'équipe de direction et d\'ingénierie de MTS. Des professionnels expérimentés dans les systèmes électriques industriels, l\'électronique, la robotique et la fabrication.', '认识MTS的管理和工程团队。工业电气系统、电子、机器人和制造领域经验丰富的专业人士。'),
    ('team.breadcrumb.home', 'Home', 'Accueil', '首页'),
    ('team.breadcrumb.team', 'Our Team', 'Notre Équipe', '我们的团队'),
    ('team.banner.title', 'Our Team', 'Notre Équipe', '我们的团队'),
    ('team.banner.desc', 'Meet the experienced professionals driving industrial excellence at MTS.', 'Rencontrez les professionnels expérimentés qui stimulent l\'excellence industrielle chez MTS.', '认识MTS推动工业卓越的经验丰富的专业人士。'),

    ('team.team.pre', 'Leadership', 'Direction', '领导层'),
    ('team.team.title', 'The People Behind Our Success', 'Les Personnes Derrière Notre Succès', '我们成功背后的人们'),
    ('team.team.desc', 'Our team of experienced engineers and industry specialists.', 'Notre équipe d\'ingénieurs expérimentés et de spécialistes industriels.', '我们经验丰富的工程师和行业专家团队。'),
    ('team.team.member1.name', 'Ahmed El Amrani', 'Ahmed El Amrani', '艾哈迈德·阿尔·阿姆拉尼'),
    ('team.team.member1.role', 'CEO & Founder', 'PDG & Fondateur', '首席执行官兼创始人'),
    ('team.team.member2.name', 'Fatima Zahra Benali', 'Fatima Zahra Benali', '法蒂玛·扎赫拉·本纳利'),
    ('team.team.member2.role', 'Chief Operations Officer', 'Directrice des Opérations', '首席运营官'),
    ('team.team.member3.name', 'Youssef El Khatib', 'Youssef El Khatib', '优素福·阿尔·哈提卜'),
    ('team.team.member3.role', 'Technical Director', 'Directeur Technique', '技术总监'),
    ('team.team.member4.name', 'Sofia Bennani', 'Sofia Bennani', '索菲亚·本纳尼'),
    ('team.team.member4.role', 'Quality & Compliance Manager', 'Responsable Qualité & Conformité', '质量与合规经理'),

    ('team.testimonials.pre', 'Testimonials', 'Témoignages', '客户评价'),
    ('team.testimonials.title', 'Client Feedback', 'Avis Clients', '客户反馈'),
    ('team.testimonials.1.name', 'Jean-Pierre Dubois', 'Jean-Pierre Dubois', '让-皮埃尔·杜布瓦'),
    ('team.testimonials.1.quote', 'MTS delivered exceptional electrical systems for our railway infrastructure project. Their precision and timeliness exceeded our expectations.', 'MTS a livré des systèmes électriques exceptionnels pour notre projet d\'infrastructure ferroviaire. Leur précision et leur respect des délais ont dépassé nos attentes.', 'MTS为我们的铁路基础设施项目交付了卓越的电气系统。他们的精准度和及时性超出了我们的预期。'),
    ('team.testimonials.1.role', 'Project Director, RailCorp', 'Directeur de Projet, RailCorp', '项目总监，RailCorp'),
    ('team.testimonials.2.name', 'Maria Garcia', 'Maria Garcia', '玛丽亚·加西亚'),
    ('team.testimonials.2.quote', 'The robotic integration MTS implemented transformed our production line efficiency. Highly recommended.', "L'intégration robotique réalisée par MTS a transformé l'efficacité de notre chaîne de production. Hautement recommandé.", 'MTS实施的机器人集成改变了我们的生产线效率。强烈推荐。'),
    ('team.testimonials.2.role', 'Manufacturing Director, AeroTech', 'Directrice de Production, AeroTech', '制造总监，AeroTech'),
    ('team.testimonials.3.name', 'Thomas Mueller', 'Thomas Mueller', '托马斯·穆勒'),
    ('team.testimonials.3.quote', 'Their maintenance team keeps our equipment running at peak performance. Reliable and professional.', 'Leur équipe de maintenance maintient nos équipements à des performances optimales. Fiable et professionnelle.', '他们的维护团队让我们的设备保持最佳运行状态。可靠且专业。'),
    ('team.testimonials.3.role', 'Operations Manager, MediDev', 'Responsable des Opérations, MediDev', '运营经理，MediDev'),

    ('team.why.title', 'Why Work With Us', 'Pourquoi Travailler Avec Nous', '为什么与我们合作'),
    ('team.why.desc', 'Join a team committed to engineering excellence and industrial innovation.', 'Rejoignez une équipe engagée dans l\'excellence technique et l\'innovation industrielle.', '加入一个致力于工程卓越和工业创新的团队。'),
    ('team.why.item1', 'Innovative projects across multiple industries', 'Projets innovants dans de multiples secteurs', '跨多个行业的创新项目'),
    ('team.why.item2', 'Professional development opportunities', 'Opportunités de développement professionnel', '专业发展机会'),
    ('team.why.item3', 'International work environment', 'Environnement de travail international', '国际工作环境'),
    ('team.why.item4', 'Competitive compensation and benefits', 'Rémunération et avantages compétitifs', '有竞争力的薪酬和福利'),
    ('team.why.btn', 'Join Our Team', 'Rejoignez Notre Équipe', '加入我们的团队'),

    ('team.cta.title', 'Ready to Join Our Team?', 'Prêt à Rejoindre Notre Équipe ?', '准备好加入我们的团队了吗？'),
    ('team.cta.desc', 'Explore career opportunities at MTS and become part of our growing family.', 'Explorez les opportunités de carrière chez MTS et faites partie de notre famille en pleine croissance.', '探索MTS的职业机会，成为我们不断发展的大家庭的一员。'),
    ('team.cta.btn', 'View Open Positions', 'Voir les Postes Ouverts', '查看空缺职位'),

    # === TEAM SINGLE ===
    ('single.meta.title', 'Team Member - MTS - Manufacturing System Technology', 'Membre de l\'Équipe - MTS - Technologie des Systèmes de Fabrication', '团队成员 - MTS - 制造系统技术'),
    ('single.meta.desc', 'Detailed profile of MTS team members, their expertise, experience, and role in the organization.', 'Profil détaillé des membres de l\'équipe MTS, leur expertise, leur expérience et leur rôle dans l\'organisation.', 'MTS团队成员的详细资料，包括他们的专长、经验以及在组织中的角色。'),
    ('single.breadcrumb.home', 'Home', 'Accueil', '首页'),
    ('single.breadcrumb.team', 'Team', 'Équipe', '团队'),
    ('single.breadcrumb.member', 'Team Member', 'Membre de l\'Équipe', '团队成员'),
    ('single.banner.name', 'Team Member', 'Membre de l\'Équipe', '团队成员'),
    ('single.banner.role', 'Professional Profile', 'Profil Professionnel', '专业简介'),
    ('single.banner.desc', 'Detailed profile and professional background', 'Profil détaillé et parcours professionnel', '详细资料和专业背景'),
    ('single.banner.follow', 'Follow', 'Suivre', '关注'),

    ('single.stats.award', 'Industry Awards', 'Récompenses Industrielles', '行业奖项'),
    ('single.stats.certification', 'Certifications', 'Certifications', '认证'),
    ('single.stats.delivery', 'Projects Delivered', 'Projets Livrés', '已交付项目'),

    ('single.feedback.pre', 'Feedback', 'Avis', '反馈'),
    ('single.feedback.title', 'Client Feedback', 'Avis Clients', '客户反馈'),

    ('single.cta.title', 'Need Expert Industrial Support?', 'Besoin d\'un Support Industriel Expert ?', '需要专业的工业支持？'),
    ('single.cta.desc', 'Contact our team to discuss how our expertise can help your project.', 'Contactez notre équipe pour discuter de la façon dont notre expertise peut aider votre projet.', '联系我们的团队，了解我们的专长如何帮助您的项目。'),
    ('single.cta.btn', 'Contact Us', 'Contactez-Nous', '联系我们'),

    # === WHY CHOOSE US ===
    ('why.meta.title', 'Why Choose Us - MTS - Manufacturing System Technology', 'Pourquoi Nous Choisir - MTS - Technologie des Systèmes de Fabrication', '为什么选择我们 - MTS - 制造系统技术'),
    ('why.meta.desc', 'Discover why leading industrial companies choose MTS for electrical equipment, electronic assemblies, robotics, and maintenance services.', 'Découvrez pourquoi les principales entreprises industrielles choisissent MTS pour les équipements électriques, les assemblages électroniques, la robotique et les services de maintenance.', '了解为什么领先的工业公司选择MTS提供电气设备、电子装配、机器人和维护服务。'),
    ('why.breadcrumb.home', 'Home', 'Accueil', '首页'),
    ('why.breadcrumb.why', 'Why Choose Us', 'Pourquoi Nous Choisir', '为什么选择我们'),
    ('why.banner.title', 'Experience the Difference with MTS', 'Découvrez la Différence avec MTS', '体验MTS的不同之处'),
    ('why.intro', 'Why Choose MTS', 'Pourquoi Choisir MTS', '为什么选择MTS'),

    ('why.features.title', 'What Sets Us Apart', 'Ce Qui Nous Distingue', '我们的优势'),
    ('why.features.item1', 'ISO-certified manufacturing processes', 'Processus de fabrication certifiés ISO', 'ISO认证的制造流程'),
    ('why.features.item2', '300+ skilled professionals', '300+ professionnels qualifiés', '300+名专业技术人员'),
    ('why.features.item3', '11 production sites across France and international locations', '11 sites de production en France et à l\'international', '遍布法国和国际的11个生产基地'),
    ('why.features.item4', 'Proven track record across multiple industries', 'Parcours éprouvé dans de multiples secteurs', '在多个行业拥有经证实的业绩'),

    ('why.planning.pre', 'Our Approach', 'Notre Approche', '我们的方法'),
    ('why.planning.title', 'Strategic Industrial Solutions to Drive Manufacturing', 'Solutions Industrielles Stratégiques pour Dynamiser la Fabrication', '推动制造业发展的战略工业解决方案'),
    ('why.planning.step1.title', 'Understanding Your Needs', 'Comprendre Vos Besoins', '了解您的需求'),
    ('why.planning.step1.desc', 'In-depth analysis of your requirements, challenges, and goals.', 'Analyse approfondie de vos besoins, défis et objectifs.', '深入分析您的需求、挑战和目标。'),
    ('why.planning.step2.title', 'Tailored Solution Design', 'Conception de Solution Sur Mesure', '定制解决方案设计'),
    ('why.planning.step2.desc', 'Custom engineering solutions designed for your specific application.', 'Solutions d\'ingénierie personnalisées conçues pour votre application spécifique.', '为您的特定应用设计的定制工程解决方案。'),
    ('why.planning.step3.title', 'Execution & Delivery', 'Exécution & Livraison', '执行与交付'),
    ('why.planning.step3.desc', 'Precision manufacturing with rigorous quality control and on-time delivery.', 'Fabrication de précision avec un contrôle qualité rigoureux et une livraison dans les délais.', '精密制造，严格的质量控制和按时交付。'),

    ('why.cta.title', 'Ready to Experience the MTS Difference?', 'Prêt à Découvrir la Différence MTS ?', '准备好体验MTS的不同之处了吗？'),
    ('why.cta.desc', 'Contact us today to discuss how we can support your industrial projects.', 'Contactez-nous dès aujourd\'hui pour discuter de la façon dont nous pouvons soutenir vos projets industriels.', '立即联系我们，讨论我们如何支持您的工业项目。'),
    ('why.cta.btn', 'Get In Touch', 'Prenez Contact', '联系我们'),

    # === PARTNER ===
    ('partner.meta.title', 'Our Partners - MTS - Manufacturing System Technology', 'Nos Partenaires - MTS - Technologie des Systèmes de Fabrication', '我们的合作伙伴 - MTS - 制造系统技术'),
    ('partner.meta.desc', 'MTS partners with leading industrial technology manufacturers to deliver the best solutions for our clients across all sectors.', 'MTS s\'associe aux principaux fabricants de technologies industrielles pour offrir les meilleures solutions à nos clients dans tous les secteurs.', 'MTS与领先的工业技术制造商合作，为各行业客户提供最佳解决方案。'),
    ('partner.breadcrumb.home', 'Home', 'Accueil', '首页'),
    ('partner.breadcrumb.partners', 'Our Partners', 'Nos Partenaires', '我们的合作伙伴'),
    ('partner.banner.title', 'Our Partners & Collaborators', 'Nos Partenaires & Collaborateurs', '我们的合作伙伴与协作者'),
    ('partner.banner.desc', 'We collaborate with industry-leading technology manufacturers to deliver excellence.', 'Nous collaborons avec les fabricants de technologies de pointe pour offrir l\'excellence.', '我们与行业领先的技术制造商合作，交付卓越成果。'),

    ('partner.features.title', 'Why Our Partnerships Matter', 'Pourquoi Nos Partenariats Comptent', '为什么我们的合作伙伴关系很重要'),
    ('partner.features.item1', 'Access to latest industrial technologies', 'Accès aux dernières technologies industrielles', '获取最新的工业技术'),
    ('partner.features.item2', 'Certified components and equipment', 'Composants et équipements certifiés', '认证的组件和设备'),
    ('partner.features.item3', 'Extended warranty and support', 'Garantie et support étendus', '延长保修和支持'),
    ('partner.features.item4', 'Preferred pricing for clients', 'Tarifs préférentiels pour les clients', '为客户提供优惠价格'),

    ('partner.brands.desc', 'We are proud to work with leading industrial technology brands.', 'Nous sommes fiers de travailler avec les plus grandes marques de technologies industrielles.', '我们很自豪能与领先的工业技术品牌合作。'),
    ('partner.reviews.trust', 'Trusted by Industry Leaders', 'Approuvé par les Leaders de l\'Industrie', '受到行业领袖的信赖'),
    ('partner.reviews.score', 'Client Satisfaction Score', 'Score de Satisfaction Client', '客户满意度评分'),
    ('partner.reviews.count', 'Partners Worldwide', 'Partenaires dans le Monde', '全球合作伙伴'),
    ('partner.reviews.revenue', 'Combined Revenue', 'Chiffre d\'Affaires Combiné', '合并收入'),

    ('partner.cta.title', 'Interested in Becoming a Partner?', 'Intéressé à Devenir Partenaire ?', '有兴趣成为合作伙伴？'),
    ('partner.cta.desc', 'Contact our partnerships team to explore collaboration opportunities.', 'Contactez notre équipe partenariats pour explorer les opportunités de collaboration.', '联系我们的合作伙伴团队，探索合作机会。'),
    ('partner.cta.btn', 'Contact Us', 'Contactez-Nous', '联系我们'),

    # === INDUSTRY ===
    ('industry.meta.title', 'Industries We Serve - MTS - Manufacturing System Technology', 'Secteurs d\'Activité - MTS - Technologie des Systèmes de Fabrication', '我们服务的行业 - MTS - 制造系统技术'),
    ('industry.meta.desc', 'MTS serves railway, aerospace, defense, energy, medical, and general industry sectors with industrial electrical and electronic solutions.', 'MTS sert les secteurs ferroviaire, aérospatial, défense, énergie, médical et industrie générale avec des solutions électriques et électroniques industrielles.', 'MTS为铁路、航空航天、国防、能源、医疗和一般工业领域提供工业和电气电子解决方案。'),
    ('industry.breadcrumb.home', 'Home', 'Accueil', '首页'),
    ('industry.breadcrumb.industries', 'Industries', 'Secteurs d\'Activité', '行业'),
    ('industry.banner.title', 'Industries We Serve', 'Secteurs d\'Activité', '我们服务的行业'),
    ('industry.banner.desc', 'Delivering industrial solutions across multiple sectors.', 'Fournir des solutions industrielles dans plusieurs secteurs.', '在多个行业提供工业解决方案。'),
    ('industry.banner.btn', 'Explore Our Services', 'Découvrir Nos Services', '探索我们的服务'),

    ('industry.railway.title', 'Railway', 'Ferroviaire', '铁路'),
    ('industry.railway.desc', 'Electrical systems, signaling equipment, and control panels for railway infrastructure and rolling stock.', 'Systèmes électriques, équipements de signalisation et panneaux de contrôle pour l\'infrastructure ferroviaire et le matériel roulant.', '铁路基础设施和机车车辆的电气系统、信号设备和控制面板。'),
    ('industry.railway.item1', 'Signaling and control systems', 'Systèmes de signalisation et de contrôle', '信号与控制系统'),
    ('industry.railway.item2', 'Electrical cabinet manufacturing', 'Fabrication d\'armoires électriques', '电气柜制造'),
    ('industry.railway.item3', 'Rolling stock electrical systems', 'Systèmes électriques pour matériel roulant', '机车车辆电气系统'),
    ('industry.railway.item4', 'Maintenance and repair services', 'Services de maintenance et de réparation', '维护和修理服务'),
    ('industry.railway.item5', 'Infrastructure automation', 'Automatisation d\'infrastructure', '基础设施自动化'),

    ('industry.aerospace.title', 'Aerospace', 'Aérospatial', '航空航天'),
    ('industry.aerospace.desc', 'Precision electronic assemblies, wiring systems, and quality-certified components for civil and military aviation.', 'Assemblages électroniques de précision, systèmes de câblage et composants certifiés pour l\'aviation civile et militaire.', '为民用和军用航空提供精密电子装配、布线系统和质量认证组件。'),
    ('industry.aerospace.item1', 'Electronic board assembly', 'Assemblage de cartes électroniques', '电子板组装'),
    ('industry.aerospace.item2', 'Wiring harness manufacturing', 'Fabrication de faisceaux de câbles', '线束制造'),
    ('industry.aerospace.item3', 'Quality-certified production', 'Production certifiée qualité', '质量认证生产'),
    ('industry.aerospace.item4', 'Mechatronic subsystems', 'Sous-systèmes mécatroniques', '机电子系统'),
    ('industry.aerospace.item5', 'Prototype development', 'Développement de prototypes', '样机开发'),

    ('industry.benefits.title', 'Benefits Across All Industries', 'Avantages dans Tous les Secteurs', '跨行业优势'),
    ('industry.benefits.desc', 'Our multi-industry experience brings cross-sector innovation to every project.', 'Notre expérience multi-sectorielle apporte l\'innovation transversale à chaque projet.', '我们的跨行业经验为每个项目带来跨领域创新。'),
    ('industry.benefits.item1', 'Cross-industry best practices', 'Meilleures pratiques intersectorielles', '跨行业最佳实践'),
    ('industry.benefits.item2', 'Regulatory compliance expertise', 'Expertise en conformité réglementaire', '法规合规专业知识'),
    ('industry.benefits.item3', 'Scalable solutions for any project size', 'Solutions évolutives pour toute taille de projet', '适用于任何项目规模的可扩展解决方案'),
    ('industry.benefits.item4', 'Dedicated project management', 'Gestion de projet dédiée', '专属项目管理'),

    ('industry.cta.title', 'Need a Solution for Your Industry?', 'Besoin d\'une Solution pour Votre Secteur ?', '需要适合您行业的解决方案？'),
    ('industry.cta.desc', 'Contact our team to discuss how our expertise can benefit your organization.', 'Contactez notre équipe pour discuter de la façon dont notre expertise peut bénéficier à votre organisation.', '联系我们的团队，了解我们的专长如何使您的组织受益。'),
    ('industry.cta.btn', 'Contact Our Team', 'Contactez Notre Équipe', '联系我们的团队'),

    # === FOOTER ===
    ('footer.desc', 'Industrial electrical equipment, electronic assemblies, special machines, robotic integration and maintenance.', 'Équipements électriques industriels, assemblages électroniques, machines spéciales, intégration robotique et maintenance.', '工业电气设备、电子装配、特种机械、机器人集成与维护。'),
    ('footer.company', 'Company', 'Société', '公司'),
    ('footer.about_us', 'About Us', 'À propos de Nous', '关于我们'),
    ('footer.about', 'About Us', 'À propos de Nous', '关于我们'),
    ('footer.company.about', 'About Us', 'À propos de Nous', '关于我们'),
    ('footer.company.partners', 'Our Partners', 'Nos Partenaires', '我们的合作伙伴'),
    ('footer.company.contact', 'Contact', 'Contact', '联系方式'),
    ('footer.services_title', 'Services', 'Services', '服务'),
    ('footer.services', 'Services', 'Services', '服务'),
    ('footer.services.electrical', 'Electrical Equipment', 'Équipement Électrique', '电气设备'),
    ('footer.services.electronics', 'Electronic Assemblies', 'Assemblages Électroniques', '电子装配'),
    ('footer.services.machines', 'Special Machines & Robotics', 'Machines Spéciales & Robotique', '特种机械与机器人'),
    ('footer.services.maintenance', 'Maintenance & Repair', 'Maintenance & Réparation', '维护与修理'),
    ('footer.services.distribution', 'Equipment Distribution', "Distribution d'Équipement", '设备分销'),
    ('footer.resources', 'Resources', 'Ressources', '资源'),
    ('footer.resources.certifications', 'Certifications', 'Certifications', '认证'),
    ('footer.resources.support', 'Support', 'Support', '支持'),
    ('footer.resources.why', 'Why Choose Us', 'Pourquoi Nous Choisir', '为什么选择我们'),
    ('footer.certifications', 'Certifications', 'Certifications', '认证'),
    ('footer.support', 'Support', 'Support', '支持'),
    ('footer.team', 'Team', 'Équipe', '团队'),
    ('footer.social_media', 'Social Media', 'Réseaux Sociaux', '社交媒体'),
    ('footer.social', 'Social Media', 'Réseaux Sociaux', '社交媒体'),
    ('footer.social.facebook', 'Facebook', 'Facebook', '脸书'),
    ('footer.social.linkedin', 'LinkedIn', 'LinkedIn', '领英'),
    ('footer.social.twitter', 'Twitter', 'Twitter', '推特'),
    ('footer.social.youtube', 'YouTube', 'YouTube', '优兔'),
    ('footer.facebook', 'Facebook', 'Facebook', '脸书'),
    ('footer.linkedin', 'LinkedIn', 'LinkedIn', '领英'),
    ('footer.twitter', 'Twitter', 'Twitter', '推特'),
    ('footer.youtube', 'YouTube', 'YouTube', '优兔'),
    ('footer.copyright', 'Copyright ', 'Droits d\'Auteur ', '版权所有 '),
    ('footer.copyright_rest', '. MTS. All Rights Reserved.', '. MTS. Tous Droits Réservés.', '. MTS. 保留所有权利。'),
    ('footer.rights', 'All Rights Reserved.', 'Tous Droits Réservés.', '保留所有权利。'),

    # === SIDEBAR ===
    ('sidebar.desc', 'MTS delivers industrial solutions across multiple sectors.', 'MTS fournit des solutions industrielles dans plusieurs secteurs.', 'MTS在多个行业提供工业解决方案。'),
    ('sidebar.about', 'About MTS', 'À propos de MTS', '关于MTS'),
    ('sidebar.about_title', 'About MTS', 'À propos de MTS', '关于MTS'),
    ('sidebar.about_text', 'Industrial electrical equipment, electronic assemblies, special machines, robotic integration and maintenance.', 'Équipements électriques industriels, assemblages électroniques, machines spéciales, intégration robotique et maintenance.', '工业电气设备、电子装配、特种机械、机器人集成与维护。'),
    ('sidebar.about.link', 'About MTS', 'À propos de MTS', '关于MTS'),
    ('sidebar.useful_links', 'Useful Links', 'Liens Utiles', '实用链接'),
    ('sidebar.links', 'Useful Links', 'Liens Utiles', '实用链接'),
    ('sidebar.our_services', 'Our Services', 'Nos Services', '我们的服务'),
    ('sidebar.services.link', 'Our Services', 'Nos Services', '我们的服务'),
    ('sidebar.get_in_touch', 'Get In Touch', 'Prenez Contact', '联系我们'),
    ('sidebar.getintouch', 'Get In Touch', 'Prenez Contact', '联系我们'),
    ('sidebar.contact.link', 'Contact Us', 'Contactez-Nous', '联系我们'),

    # === MAP ===
    ('map.popup_title', 'MTS SRL', 'MTS SRL', 'MTS SRL'),
    ('map.popup_text', 'Z.A.E Bni Ouassine, Lot 58<br>Tanger, Morocco<br>+212 6 63 22 83 22', 'Z.A.E Bni Ouassine, Lot 58<br>Tanger, Maroc<br>+212 6 63 22 83 22', 'Z.A.E Bni Ouassine, Lot 58<br>摩洛哥丹吉尔<br>+212 6 63 22 83 22'),
]

# Combine
all_translations = translations + more_translations

# Build nested objects
en_nested = {}
fr_nested = {}
zh_nested = {}

for t in all_translations:
    set_nested(en_nested, t[0], t[1])
    set_nested(fr_nested, t[0], t[2])
    set_nested(zh_nested, t[0], t[3])

# Check for missing keys from flat en.json
missing = [k for k in flat_en if k not in flat_en]  # will always be empty this way

# Actually find missing keys properly
translation_keys = set(t[0] for t in all_translations)
for key in flat_en:
    if key not in translation_keys:
        missing.append(key)
        val = flat_en[key]
        set_nested(en_nested, key, val)
        set_nested(fr_nested, key, val)
        set_nested(zh_nested, key, val)

if missing:
    print(f"Missing keys ({len(missing)}):")
    for m in missing:
        print(f"  {m} -> {flat_en[m]}")

# Write EN (keep flat format for compatibility)
output_en = json.dumps(en_nested, ensure_ascii=False, indent=4)
with open(os.path.join(srcdir, 'lang', 'en.json'), 'w', encoding='utf-8') as f:
    f.write(output_en)

# Write FR
output_fr = json.dumps(fr_nested, ensure_ascii=False, indent=4)
with open(os.path.join(srcdir, 'lang', 'fr.json'), 'w', encoding='utf-8') as f:
    f.write(output_fr)

# Write ZH
output_zh = json.dumps(zh_nested, ensure_ascii=False, indent=4)
with open(os.path.join(srcdir, 'lang', 'zh.json'), 'w', encoding='utf-8') as f:
    f.write(output_zh)

print(f"Done! EN keys: {len(flat_en)}, FR keys: {len(missing)} missing with English fallback")

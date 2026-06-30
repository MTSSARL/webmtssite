"""
Generate updated fr.json with French translations matching new en.json content.
Keys not explicitly translated get English fallback.
"""
import json, os

d = r'C:\Users\MTS\Music\Coding\MTSWebsite\2digix-business-it-solutions-html-template-2025-09-21-06-46-01-utc\digix-main\lang'

with open(os.path.join(d, 'en.json'), 'r', encoding='utf-8') as f:
    en = json.load(f)
with open(os.path.join(d, 'fr.json'), 'r', encoding='utf-8') as f:
    fr = json.load(f)

# French translations for the new/updated English content
fr_updates = {
    # === META ===
    'meta.title': 'MTS — Technologie des Systèmes de Fabrication | Automatisation Industrielle Maroc',
    'meta.desc': 'MTS est un intégrateur marocain en automatisation industrielle spécialisé dans les machines spéciales, la robotique, la vision industrielle, les convoyeurs et l\'ingénierie électrique pour l\'automobile et l\'industrie.',

    # === HERO ===
    'hero.title': "L'Innovation pour votre Productivité",
    'hero.pre_title': 'Intégrateur en Automatisation Industrielle — Maroc',
    'hero.desc': 'MTS livre des solutions clé en main d\'automatisation industrielle — machines spéciales, cellules robotisées, vision industrielle et systèmes de convoyage. Basé à Tanger, au service des leaders automobile de premier rang au Maroc et à l\'international.',
    'hero.btn': 'Découvrir Notre Expertise',
    'hero.learn_more': 'Découvrir Notre Expertise',

    # === NAV ===
    'nav.electrical_equipment': 'Ingénierie Électrique',
    'nav.electronic_assemblies': 'Vision Industrielle',
    'nav.special_machines_robotics': 'Machines Spéciales & Robotique',
    'nav.maintenance_repair': 'Maintenance & Support',
    'nav.equipment_distribution': 'Systèmes de Convoyage',
    'nav.services.distribution': 'Systèmes de Convoyage',
    'nav.services.electrical': 'Ingénierie Électrique',
    'nav.services.electronics': 'Vision Industrielle',
    'nav.services.machines': 'Machines Spéciales & Robotique',
    'nav.services.maintenance': 'Maintenance & Support',

    # === INDEX - ABOUT ===
    'index.about.title': 'Votre Partenaire en Automatisation Industrielle au Maroc',
    'index.about.desc1': 'MTS — Manufacturing Technology System est un intégrateur marocain en automatisation industrielle basé à Tanger. Nous concevons, fabriquons et mettons en service des solutions clé en main pour l\'industrie : machines spéciales, cellules robotisées, systèmes de vision industrielle, convoyeurs et ingénierie électrique.',
    'index.about.desc2': 'Avec une équipe d\'ingénieurs et techniciens qualifiés, nous servons des géants automobile de premier rang dont Marelli, APTIV, TE Connectivity, OPmobility, SOGEFI et Triumph. De la conception à la mise en service, nous livrons des solutions d\'automatisation de qualité qui boostent la productivité.',
    'index.about.quote': "L'Innovation pour votre Productivité",
    'index.about.employees': 'Professionnels Qualifiés',
    'index.about.employees_num': '50+',
    'index.about.employees_text': 'Ingénieurs & Techniciens Qualifiés',
    'index.about.sites': 'Sites de Production',

    # === INDEX - SERVICES ===
    'index.services.pre': 'Notre Expertise',
    'index.services.title': 'Solutions Complètes d\'Automatisation Industrielle',
    'index.services.desc': 'Des machines spéciales à la robotique, en passant par la vision, les convoyeurs et l\'ingénierie électrique — MTS livre l\'automatisation intégrale pour l\'industrie.',
    'index.services.card1_title': 'Machines Spéciales',
    'index.services.card1_desc': 'Lignes d\'assemblage automatisées, postes de travail manuels et semi-automatiques, intégration de marquage et vissage, bols vibrants, gabarits et montages.',
    'index.services.card2_title': 'Vision Industrielle',
    'index.services.card2_desc': 'Détection de défauts, contrôle dimensionnel, lecture de codes-barres, solutions d\'inspection intelligente par deep learning pour l\'assurance qualité.',
    'index.services.card3_title': 'Robotique',
    'index.services.card3_desc': 'Pick and place, dépalettisation et palettisation, décarionnage et encartonnage, collage et dosage robotisés, outillage de fin de bras (EOAT).',
    'index.services.card4_title': 'Systèmes de Convoyage',
    'index.services.card4_desc': 'Convoyeurs à palettes indexées, convoyeurs à chaîne, courroie et bande, convoyeurs carrousel pour la manutention automatisée.',
    'index.services.electrical.title': 'Ingénierie Électrique',
    'index.services.electrical.desc': 'Câblage d\'armoires électriques et pneumatiques, conception de tableaux de distribution, programmation PLC et IHM, installation et mise en service sur site.',
    'index.services.electronics.title': 'Vision Industrielle',
    'index.services.electronics.desc': 'Détection de défauts, inspection dimensionnelle, lecture de codes-barres et inspection visuelle par deep learning.',
    'index.services.machines.title': 'Machines Spéciales & Robotique',
    'index.services.machines.desc': 'Conception et fabrication de machines spéciales avec intégration robotique pour l\'automatisation de production.',
    'index.services.maintenance.title': 'Maintenance & Support',
    'index.services.maintenance.desc': 'Maintenance d\'équipements industriels, réparation, support sur site et assistance technique.',
    'index.services.distribution.title': 'Systèmes de Convoyage',
    'index.services.distribution.desc': 'Convoyeurs à palettes indexées, convoyeurs à bande et systèmes carrousel pour la manutention automatisée.',
    'index.services.btn': 'Voir Tous les Services',
    'index.services.view_all': 'Voir Tous les Services',

    # === INDEX - ACHIEVEMENTS ===
    'index.achievements.title': 'L\'Excellence en Automatisation à Travers le Maroc',

    # === INDEX - VIDEO ===
    'index.video.pre': 'Nos Installations',
    'index.video.title': 'Voir Notre Travail en Action',
    'index.video.desc': 'Découvrez notre site de Tanger, nos projets d\'automatisation et nos capacités industrielles.',
    'index.video.card1_title': 'Fabrication de Machines Spéciales',
    'index.video.card1.title': 'Fabrication de Machines Spéciales',
    'index.video.card1.desc': 'Conception et assemblage de postes de travail automatisés sur mesure.',
    'index.video.card1_location': 'Site de Tanger',
    'index.video.card2_title': 'Intégration Robotique',
    'index.video.card2.title': 'Intégration Robotique',
    'index.video.card2.desc': 'Intégration et programmation de cellules robotiques avancées.',
    'index.video.card2_desc': 'Intégration et programmation de cellules robotiques avancées.',

    # === INDEX - SOLUTIONS ===
    'index.solutions.pre': 'Nos Projets',
    'index.solutions.title': 'Transformer l\'Industrie avec l\'Automatisation',
    'index.solutions.desc': 'Projets d\'automatisation concrets démontrant nos capacités d\'ingénierie dans les secteurs automobile et industriel.',
    'index.solutions.case1_title': 'Ligne d\'Assemblage Automatisée — Marelli',
    'index.solutions.case1_industry': 'Automobile',
    'index.solutions.case2_title': 'Système d\'Inspection Vision — APTIV',
    'index.solutions.case2_industry': 'Électronique Automobile',
    'index.solutions.case3_title': 'Cellule de Palettisation Robotisée — OPmobility',
    'index.solutions.case3_industry': 'Automobile',
    'index.solutions.case4_title': 'Système de Convoyage — TE Connectivity',
    'index.solutions.case4_industry': 'Électronique',
    'index.solutions.case5_title': 'Mise à Niveau PLC & IHM — SOGEFI',
    'index.solutions.case5_industry': 'Industrie',
    'index.solutions.case6_title': 'Intégration Vision & Robotique — ECI',
    'index.solutions.case6_industry': 'Faisceaux de Câbles',
    'index.cases.pre': 'Nos Projets',
    'index.cases.title': 'Transformer l\'Industrie avec l\'Automatisation',
    'index.cases.desc': 'Projets d\'automatisation concrets démontrant nos capacités d\'ingénierie.',
    'index.cases.btn': 'Voir Tous les Projets',

    # === INDEX - VALUES ===
    'index.values.title': 'Ce Qui Nous Anime',
    'index.values.desc': 'Nos principes guident chaque projet d\'automatisation que nous livrons.',
    'index.values.check1': 'Ingénierie axée sur la qualité pour tous les projets',
    'index.values.check2': 'Engagement de livraison dans les délais',
    'index.values.check3': 'Collaboration étroite avec le client',
    'index.values.item1': 'Ingénierie axée sur la qualité pour tous les projets',
    'index.values.item2': 'Engagement de livraison dans les délais',
    'index.values.item3': 'Collaboration étroite avec le client',

    # === INDEX - TEAM ===
    'index.team.member1.name': 'Ahmed El Amrani',
    'index.team.member1.role': 'PDG & Fondateur',
    'index.team.member2.name': 'Fatima Zahra Benali',
    'index.team.member2.role': 'Directrice des Opérations',
    'index.team.member3.name': 'Youssef El Khatib',
    'index.team.member3.role': 'Directeur Technique',
    'index.team.member4.name': 'Sofia Bennani',
    'index.team.member4.role': 'Responsable Qualité & Conformité',

    # === INDEX - TESTIMONIALS ===
    'index.testimonials.title': 'Ce Que Disent Nos Clients',
    'index.testimonials.desc': 'Écoutez nos clients parler de leur expérience avec MTS.',
    'index.testimonials.1.name': 'Jean-Pierre Dubois',
    'index.testimonials.1.quote': 'MTS a livré une ligne d\'assemblage automatisée complexe pour notre usine automobile. Le projet a été terminé dans les délais et a dépassé nos attentes qualité.',
    'index.testimonials.1.role': 'Directeur d\'Usine, Marelli',
    'index.testimonials.2.name': 'Maria Garcia',
    'index.testimonials.2.quote': 'L\'intégration robotique réalisée par MTS a transformé l\'efficacité de notre ligne de production. Hautement recommandé.',
    'index.testimonials.2.role': 'Directrice de Production, APTIV',
    'index.testimonials.3.name': 'Thomas Mueller',
    'index.testimonials.3.quote': 'Leur solution de vision industrielle a réduit notre taux de défauts de 98%. Une équipe fiable et professionnelle.',
    'index.testimonials.3.role': 'Responsable Qualité, TE Connectivity',
    'index.testimonials.4.name': 'Sarah Johnson',
    'index.testimonials.4.quote': 'De la conception à la mise en service, MTS a géré notre projet de système de convoyage avec un professionnalisme complet.',
    'index.testimonials.4.role': "Directrice des Opérations, OPmobility",
    'index.testimonials.5.name': 'Carlos Mendez',
    'index.testimonials.5.quote': 'La machine spéciale que MTS a construite pour nous a dépassé les spécifications. Une véritable excellence technique à un prix compétitif.',
    'index.testimonials.5.role': 'Directeur Technique, SOGEFI',
    'index.testimonials.t1_name': 'Jean-Pierre Dubois',
    'index.testimonials.t1_role': "Directeur d'Usine, Marelli",
    'index.testimonials.t4_text': 'MTS a livré une ligne d\'assemblage automatisée complexe pour notre usine automobile, terminée dans les délais et dépassant nos attentes qualité.',

    # === INDEX - CLIENTS ===
    'index.clients.title': 'Approuvé par les Leaders Automobile & Industriels',

    # === INDEX - BLOG ===
    'index.blog.desc': 'Restez informé des dernières tendances en automatisation industrielle, robotique et fabrication au Maroc.',
    'index.blog.1.cat': 'Automatisation',
    'index.blog.1.title': "Comment l'Intégration Robotique Transforme l'Industrie Automobile au Maroc",
    'index.blog.2.cat': 'Projets',
    'index.blog.2.title': "MTS Achève un Projet Majeur de Ligne d'Assemblage pour Marelli",
    'index.blog.3.cat': 'Technologie',
    'index.blog.3.title': 'Progrès de la Vision Industrielle pour le Contrôle Qualité',
    'index.blog.post1_category': 'Automatisation',
    'index.blog.post1_title': "Comment l'Intégration Robotique Transforme l'Industrie Automobile au Maroc",
    'index.blog.post2_category': 'Projets',
    'index.blog.post2_title': "MTS Achève un Projet Majeur de Ligne d'Assemblage pour Marelli",
    'index.blog.post3_category': 'Technologie',
    'index.blog.post3_title': 'Progrès de la Vision Industrielle pour le Contrôle Qualité',

    # === INDEX - FAQ ===
    'index.faq.desc': 'Trouvez des réponses aux questions courantes sur MTS et nos services d\'automatisation industrielle.',
    'index.faq.q1': 'Quels secteurs MTS dessert-il ?',
    'index.faq.a1': 'MTS dessert principalement l\'industrie automobile et ses fournisseurs de premier rang, incluant les fabricants de connecteurs, d\'électronique, de systèmes de filtration et de faisceaux de câbles. Nous servons également l\'industrie manufacturière en général.',
    'index.faq.q2': 'Où se trouvent vos installations ?',
    'index.faq.a2': 'MTS est basé dans la Zone d\'Activités Économiques de Bni Ouassine, Tanger, Maroc. Nous servons des clients au Maroc et à l\'international.',
    'index.faq.q3': 'Comment demander un devis ?',
    'index.faq.a3': 'Remplissez le formulaire de contact sur notre site, appelez-nous au +212 610 764 921 ou envoyez un email à contact@multitechniques-services.ma. Nous répondons sous 24 heures.',

    # === INDEX - MAP ===
    'index.map.address': 'Lot n°58, Zone d\'Activités Économiques, Bni Ouassine, Province Fahs-Anjra, Tanger, Maroc',
    'index.map.popup.address': 'Lot n°58, ZAE Bni Ouassine<br>Province Fahs-Anjra, Tanger, Maroc<br>+212 610 764 921',
    'index.map.card.address.val': 'Lot n°58, Zone d\'Activités Économiques, Bni Ouassine, Tanger, Maroc',
    'index.map.card.email.val': 'contact@multitechniques-services.ma',
    'index.map.card.phone.val': '+212 610 764 921',

    # === INDEX - PARTNERS ===
    'index.partners.title': 'Marques & Technologies avec Lesquelles Nous Travaillons',
    'index.partners.desc': 'Nous intégrons les principales technologies d\'automatisation dont Siemens, Fanuc, Cognex, Keyence, Sick et plus.',

    # === INDEX - CONTACT FORM ===
    'index.form.title': 'Demander un Devis',
    'index.form.subject': 'Sujet',
    'index.form.message': 'Parlez-nous de votre projet',
    'index.contact.title': 'Demander un Devis',
    'index.contact.message': 'Parlez-nous de votre projet',
    'index.contact.company': 'Société',

    # === ABOUT ===
    'about.meta.title': 'À propos de MTS — Intégrateur en Automatisation Industrielle Maroc',
    'about.meta.desc': 'Découvrez MTS : notre mission, notre équipe et notre expertise en automatisation industrielle. Basé à Tanger, Maroc, au service des clients automobile de premier rang.',
    'about.hero.title': 'Votre Partenaire de Confiance en Automatisation au Maroc',
    'about.banner.title': 'À propos de MTS',
    'about.banner.img': 'À propos de MTS — Site de Tanger',
    'about.mission.title': 'Notre Mission',
    'about.mission.label': 'Notre Mission',
    'about.mission.desc': 'MTS se consacre à fournir des solutions innovantes d\'automatisation industrielle qui améliorent la productivité, la qualité et la compétitivité des fabricants au Maroc et au-delà. Nous combinons l\'expertise technique avec un engagement d\'excellence dans chaque projet.',
    'about.mission.excellence': "L'Innovation pour votre Productivité",
    'about.mission.employees': 'Professionnels Qualifiés',
    'about.mission.skilled_employees': 'Professionnels Qualifiés',

    'about.values.title': 'Nos Valeurs en Action',
    'about.values.1.desc': 'Repousser constamment les limites de l\'automatisation industrielle pour offrir des solutions de pointe à nos clients.',
    'about.values.2.desc': 'Un contrôle qualité rigoureux garantissant que chaque système d\'automatisation répond aux normes les plus élevées de performance et de fiabilité.',
    'about.values.3.desc': 'Engagement envers la sécurité au travail et conformité aux réglementations de sécurité internationales dans toutes nos installations.',
    'about.values.4.desc': 'Bâtir des relations durables basées sur le respect mutuel avec les clients, les partenaires et les employés.',
    'about.values.5.desc': 'Dévoués à tenir nos promesses avec responsabilité et transparence.',
    'about.values.engagement_title': 'Engagement',

    'about.team.member1.name': 'Ahmed El Amrani',
    'about.team.member1.role': 'PDG & Fondateur',
    'about.team.member2.name': 'Fatima Zahra Benali',
    'about.team.member2.role': 'Directrice des Opérations',
    'about.team.member3.name': 'Youssef El Khatib',
    'about.team.member3.role': 'Directeur Technique',
    'about.team.member4.name': 'Sofia Bennani',
    'about.team.member4.role': 'Responsable Qualité & Conformité',

    'about.process.pre': 'Notre Processus',
    'about.process.title': 'Comment Nous Livrons les Solutions d\'Automatisation',
    'about.process.step1.title': 'Consultation & Analyse',
    'about.process.step1.desc': 'Compréhension de vos besoins de production, défis et objectifs d\'automatisation grâce à une consultation approfondie.',
    'about.process.step2.title': 'Conception & Ingénierie',
    'about.process.step2.desc': 'Développement de conceptions détaillées et de solutions d\'ingénierie adaptées à votre environnement de fabrication.',
    'about.process.step3.title': 'Fabrication & Intégration',
    'about.process.step3.desc': 'Fabrication de précision, assemblage et intégration de systèmes d\'automatisation dans notre site de Tanger.',
    'about.process.step4.title': 'Mise en Service & Support',
    'about.process.step4.desc': 'Installation sur site, mise en service et support technique continu pour garantir des performances optimales.',

    'about.cta.title': 'Prêt à Automatiser Votre Production ?',
    'about.cta.desc': 'Contactez notre équipe dès aujourd\'hui pour discuter de vos besoins en automatisation et découvrir comment MTS peut transformer votre fabrication.',
    'about.cta.btn': 'Prenez Contact',
    'about.cta.button': 'Prenez Contact',

    # === CONTACT ===
    'contact.meta.title': 'Contactez MTS — Automatisation Industrielle Maroc',
    'contact.meta.desc': 'Contactez MTS pour des solutions d\'automatisation industrielle : machines spéciales, robotique, vision industrielle, convoyeurs et ingénierie électrique au Maroc.',
    'contact.hero.desc': 'Vous avez un projet en tête ? Contactez notre équipe pour discuter de vos besoins en automatisation.',
    'contact.banner.desc': 'Vous avez un projet en tête ? Contactez notre équipe pour discuter de vos besoins en automatisation.',

    'contact.info.headquarters': 'Notre Siège',
    'contact.card.address.val': 'Lot n°58, Zone d\'Activités Économiques, Bni Ouassine, Province Fahs-Anjra, Tanger, Maroc',
    'contact.card.email.desc': 'contact@multitechniques-services.ma',
    'contact.card.phone.desc': '+212 610 764 921',

    'contact.form.subject_label': 'Sujet',
    'contact.form.subject_default': 'Demande Générale',
    'contact.form.subject.general': 'Demande Générale',
    'contact.form.subject.electrical': 'Ingénierie Électrique',
    'contact.form.subject.electronics': 'Vision Industrielle',
    'contact.form.subject.machines': 'Machines Spéciales & Robotique',
    'contact.form.subject.maintenance': 'Maintenance & Support',
    'contact.form.subject.distribution': 'Systèmes de Convoyage',
    'contact.form.help_label': 'Comment pouvons-nous vous aider ?',
    'contact.form.message': 'Parlez-nous de votre projet',
    'contact.form.message_placeholder': 'Décrivez votre projet d\'automatisation ou votre demande...',

    'contact.faq.q1': 'Quels secteurs desservez-vous ?',
    'contact.faq.a1': 'MTS dessert principalement l\'industrie automobile et ses fournisseurs de premier rang au Maroc. Nous servons également l\'industrie manufacturière, l\'électronique et les secteurs industriels en général.',
    'contact.faq.q2': 'Où se trouve MTS ?',
    'contact.faq.a2': 'MTS est basé dans la Zone d\'Activités Économiques de Bni Ouassine, Province Fahs-Anjra, Tanger, Maroc.',
    'contact.faq.q3': 'Comment demander un devis ?',
    'contact.faq.a3': 'Remplissez le formulaire de contact sur cette page, appelez le +212 610 764 921 ou envoyez un email à contact@multitechniques-services.ma. Nous répondons sous 24 heures.',

    # === SERVICE ===
    'service.meta.title': 'Nos Services — MTS Automatisation Industrielle Maroc',
    'service.meta.desc': 'Découvrez les services d\'automatisation industrielle de MTS : machines spéciales, robotique, vision industrielle, convoyeurs et ingénierie électrique pour l\'automobile et l\'industrie.',
    'service.banner.title': 'Solutions Complètes d\'Automatisation Industrielle',

    'service.card.electrical.title': 'Ingénierie Électrique',
    'service.card.electrical.desc': 'Câblage d\'armoires électriques et pneumatiques, conception de tableaux de distribution, programmation PLC et IHM, installation et mise en service sur site.',
    'service.card.electronics.title': 'Vision Industrielle',
    'service.card.electronics.desc': 'Détection de défauts, contrôle dimensionnel, lecture de codes-barres et solutions d\'inspection intelligente par deep learning.',
    'service.card.machines.title': 'Machines Spéciales & Robotique',
    'service.card.machines.desc': 'Lignes d\'assemblage automatisées sur mesure, cellules robotisées, pick and place, palettisation et outillage de fin de bras.',
    'service.card.maintenance.title': 'Maintenance & Support',
    'service.card.maintenance.desc': 'Maintenance d\'équipements industriels, réparation, support sur site et assistance technique pour systèmes d\'automatisation.',
    'service.card.distribution.title': 'Systèmes de Convoyage',
    'service.card.distribution.desc': 'Convoyeurs à palettes indexées, convoyeurs à chaîne et à bande, systèmes carrousel pour la manutention automatisée.',
    'service.card.consulting.title': 'Conseil en Automatisation',
    'service.card.consulting.desc': 'Conseil expert pour l\'automatisation de fabrication, études de faisabilité et optimisation de lignes de production.',

    'service.expertise.pre': 'Notre Expertise',
    'service.expertise.title': "Solutions d'Automatisation Industrielle Intégrales",
    'service.expertise.desc': 'Du concept à la mise en service, MTS livre des solutions d\'automatisation clé en main adaptées à vos besoins de fabrication. Nous combinons conception mécanique, ingénierie électrique, robotique et vision industrielle pour résoudre des défis de production complexes.',
    'service.expertise.btn': 'En Savoir Plus',

    'service.why.pre': 'Pourquoi Choisir MTS',
    'service.why.title': 'Pourquoi Choisir MTS pour Vos Projets d\'Automatisation',
    'service.why.1.title': 'Expertise Automobile Prouvée',
    'service.why.1.desc': 'Approuvé par des géants automobile de premier rang dont Marelli, APTIV, TE Connectivity, OPmobility et SOGEFI pour des projets d\'automatisation complexes.',
    'service.why.2.title': 'Proximité Marocaine, Standards Globaux',
    'service.why.2.desc': 'Basé dans la Zone Franche de Tanger, nous offrons l\'avantage d\'une présence locale avec des prix compétitifs par rapport aux intégrateurs européens, sans compromis sur la qualité.',
    'service.why.3.title': 'Capacité Intégrale',
    'service.why.3.desc': 'De la conception mécanique et l\'ingénierie électrique à la programmation PLC et la mise en service sur site, nous gérons chaque aspect de votre projet d\'automatisation.',

    'service.cta.title': 'Besoin d\'une Solution d\'Automatisation ?',
    'service.cta.desc': 'Contactez notre équipe d\'ingénierie pour discuter de vos besoins spécifiques.',
    'service.cta.btn': 'Contactez-Nous Aujourd\'hui',

    # === SERVICE DETAILS ===
    'details.meta.title': 'Détails du Service — MTS Automatisation Industrielle',
    'details.meta.desc': 'Informations détaillées sur les services d\'automatisation industrielle de MTS : machines spéciales, robotique, systèmes de vision, convoyeurs et ingénierie électrique.',
    'details.banner.title': 'Solutions d\'Automatisation Industrielle',
    'details.banner.img': 'Automatisation Industrielle',

    'details.process.pre': 'Notre Processus',
    'details.process.title': 'Comment Nous Livrons les Solutions d\'Automatisation',
    'details.process.step1.title': 'Analyse des Besoins',
    'details.process.step1.desc': 'Nous commençons par comprendre en profondeur vos exigences de production, spécifications techniques et objectifs d\'automatisation.',
    'details.process.step2.title': 'Conception & Prototypage',
    'details.process.step2.desc': 'Notre équipe d\'ingénierie crée des conceptions détaillées et des prototypes pour votre approbation avant la production en série.',
    'details.process.step3.title': 'Production & Livraison',
    'details.process.step3.desc': 'La fabrication a lieu dans notre site de Tanger, suivie de tests rigoureux et d\'une livraison dans les délais.',
    'details.process.step4.title': 'Mise en Service & Support',
    'details.process.step4.desc': 'Installation sur site, mise en service et support technique continu pour garantir des performances optimales.',
    'details.process.img': 'Processus d\'Automatisation',

    'details.work.pre': 'Notre Expertise',
    'details.work.title': 'Machines Spéciales, Robotique & Solutions d\'Automatisation',
    'details.work.service1.title': 'Lignes d\'Assemblage Automatisées',
    'details.work.service1.desc': 'Conception et fabrication de lignes d\'assemblage automatisées sur mesure pour l\'automobile et l\'industrie.',
    'details.work.service1.tag1': 'Assemblage',
    'details.work.service1.tag2': 'Automobile',
    'details.work.service1.tag3': 'Automatisation',
    'details.work.service2.title': 'Cellules Robotisées',
    'details.work.service2.desc': 'Intégration robotique incluant pick and place, palettisation, collage et outillage de fin de bras.',
    'details.work.service2.tag1': 'Robotique',
    'details.work.service2.tag2': 'Intégration',
    'details.work.service2.tag3': 'Automatisation',
    'details.work.service3.title': 'Systèmes de Vision Industrielle',
    'details.work.service3.desc': 'Solutions d\'inspection vision pour la détection de défauts, le contrôle dimensionnel et l\'assurance qualité.',
    'details.work.service3.tag1': 'Vision',
    'details.work.service3.tag2': 'Qualité',
    'details.work.service3.tag3': 'Inspection',

    'details.faq.desc': 'Questions courantes sur nos services et solutions d\'automatisation industrielle.',
    'details.faq.q1': 'Quel est le délai typique pour un projet d\'automatisation ?',
    'details.faq.a1': 'Les délais varient selon la complexité. La plupart des projets durent de 8 à 20 semaines, de la conception à la mise en service.',
    'details.faq.q2': 'Proposez-vous l\'installation sur site et la formation ?',
    'details.faq.a2': 'Oui, nous offrons l\'installation complète sur site, la mise en service et la formation des opérateurs pour tous les systèmes d\'automatisation.',
    'details.faq.q3': 'Avec quelles marques d\'automatisation travaillez-vous ?',
    'details.faq.a3': 'Nous intégrons les principales marques dont Siemens PLC, Fanuc et KUKA robots, Cognex et Keyence systèmes de vision, et Sick capteurs.',

    'details.cta.title': 'Besoin d\'une Solution d\'Automatisation sur Mesure ?',
    'details.cta.desc': 'Contactez notre équipe d\'ingénierie pour discuter de vos besoins et obtenir une solution adaptée.',
    'details.cta.btn': 'Demander un Devis',

    # === TEAM ===
    'team.meta.title': 'Notre Équipe — MTS Automatisation Industrielle Maroc',
    'team.meta.desc': 'Rencontrez l\'équipe MTS : ingénieurs en automatisation, spécialistes en robotique et professionnels en ingénierie électrique basés à Tanger, Maroc.',
    'team.banner.title': 'Notre Équipe d\'Experts',
    'team.banner.desc': 'MTS rassemble des ingénieurs, techniciens et spécialistes dédiés à livrer des solutions d\'automatisation industrielle fiables.',
    'team.banner.img': 'Notre Équipe',

    'team.team.title': 'Les Personnes Derrière Notre Succès',
    'team.team.desc': 'Notre succès est porté par une équipe dévouée d\'ingénieurs en automatisation et de spécialistes industriels qui apportent leur expertise à chaque projet.',
    'team.team.member1.name': 'Ahmed El Amrani',
    'team.team.member1.role': 'PDG & Fondateur',
    'team.team.member2.name': 'Fatima Zahra Benali',
    'team.team.member2.role': 'Directrice des Opérations',
    'team.team.member3.name': 'Youssef El Khatib',
    'team.team.member3.role': 'Directeur Technique',
    'team.team.member4.name': 'Sofia Bennani',
    'team.team.member4.role': 'Responsable Qualité & Conformité',
    'team.team.link': 'À propos de MTS',

    'team.testimonials.title': 'Ce Que Disent Nos Clients',
    'team.testimonials.1.name': 'Jean-Pierre Dubois',
    'team.testimonials.1.quote': 'MTS a livré une ligne d\'assemblage automatisée complexe pour notre usine automobile. Le projet a été terminé dans les délais et a dépassé nos attentes qualité.',
    'team.testimonials.1.role': "Directeur d'Usine, Marelli",
    'team.testimonials.2.name': 'Maria Garcia',
    'team.testimonials.2.quote': 'L\'intégration robotique réalisée par MTS a transformé l\'efficacité de notre ligne de production. Hautement recommandé.',
    'team.testimonials.2.role': 'Directrice de Production, APTIV',
    'team.testimonials.3.name': 'Thomas Mueller',
    'team.testimonials.3.quote': 'Leur solution de vision industrielle a réduit notre taux de défauts de 98%. Une équipe fiable et professionnelle.',
    'team.testimonials.3.role': 'Responsable Qualité, TE Connectivity',

    'team.why.title': 'Pourquoi Travailler Avec Nous',
    'team.why.desc': 'Rejoignez une équipe engagée dans l\'excellence technique et l\'innovation en automatisation industrielle.',
    'team.why.item1': 'Projets innovants pour les grandes marques automobiles',
    'team.why.item2': 'Opportunités de développement et de formation professionnelle',
    'team.why.item3': 'Environnement de travail international à Tanger',
    'team.why.item4': 'Rémunération et avantages compétitifs',

    'team.cta.title': 'Solutions d\'Automatisation Fiables. Équipe Expérimentée. Résultats Prouvés.',
    'team.cta.desc': 'Des machines spéciales à l\'intégration robotique, MTS livre des solutions d\'automatisation industrielle clé en main dignes de confiance.',
    'team.cta.btn': 'Contactez-Nous',

    # === TEAM SINGLE ===
    'single.meta.title': "Membre de l'Équipe — MTS Automatisation Industrielle",
    'single.meta.desc': 'Profil détaillé des membres de l\'équipe MTS, leur expertise, expérience et rôle dans l\'organisation.',

    'single.banner.follow': 'Suivre',

    'single.stats.award': 'Projets Livrés',
    'single.stats.certification': 'Années d\'Expérience',
    'single.stats.delivery': 'Projets Réussis',

    'single.feedback.title': 'Ce Que Disent Nos Clients',

    'single.cta.title': "Besoin d'un Support d'Automatisation Expert ?",
    'single.cta.desc': 'Contactez notre équipe pour discuter de la façon dont notre expertise peut aider votre projet.',
    'single.cta.btn': 'Contactez-Nous',

    # === WHY CHOOSE US ===
    'why.meta.title': 'Pourquoi Nous Choisir — MTS Automatisation Industrielle Maroc',
    'why.meta.desc': 'Découvrez pourquoi les grandes entreprises automobiles choisissent MTS pour les machines spéciales, la robotique, les systèmes de vision, les convoyeurs et l\'ingénierie électrique.',
    'why.banner.title': 'Découvrez la Différence MTS',
    'why.intro': 'Nous sommes plus qu\'un simple intégrateur d\'automatisation – nous sommes votre partenaire dédié à la productivité industrielle. Chaque solution est adaptée à votre environnement de production, garantissant des performances et une fiabilité optimales.',

    'why.features.title': 'Choisissez MTS pour Vos Projets d\'Automatisation',
    'why.features.item1': 'Expertise prouvée auprès des leaders automobile de premier rang',
    'why.features.item2': 'Proximité marocaine avec des prix compétitifs',
    'why.features.item3': 'Solutions intégrales de la conception à la mise en service',
    'why.features.item4': 'Ingénierie axée sur la qualité et livraison dans les délais',
    'why.features.tag1': 'Automobile',
    'why.features.tag2': 'Automatisation',
    'why.features.tag3': 'Ingénierie',

    'why.planning.title': 'Solutions d\'Automatisation Stratégiques pour l\'Industrie',
    'why.planning.step1.title': 'Consultation Initiale & Analyse des Besoins',
    'why.planning.step1.desc': 'Nous évaluons votre environnement de fabrication actuel et créons une feuille de route personnalisée alignant les solutions d\'automatisation sur vos objectifs de production.',
    'why.planning.step1.tag1': 'Conseil',
    'why.planning.step1.tag2': 'Analyse',
    'why.planning.step1.tag3': 'Planification',
    'why.planning.step2.title': 'Conception & Ingénierie',
    'why.planning.step2.desc': 'Notre équipe d\'ingénierie conçoit des solutions d\'automatisation sur mesure utilisant la modélisation CAD, la simulation et les spécifications techniques.',
    'why.planning.step2.tag1': 'Conception',
    'why.planning.step2.tag2': 'Ingénierie',
    'why.planning.step2.tag3': 'Simulation',
    'why.planning.step3.title': 'Implémentation & Mise en Service',
    'why.planning.step3.desc': 'Fabrication de précision dans notre site de Tanger suivie d\'installation sur site, de tests et de mise en service.',
    'why.planning.step3.tag1': 'Fabrication',
    'why.planning.step3.tag2': 'Installation',
    'why.planning.step3.tag3': 'Mise en Service',

    'why.team.title': 'Les Personnes Derrière Notre Succès',
    'why.team.desc': 'Notre succès est porté par une équipe dévouée de professionnels de l\'automatisation qui apportent leur expertise et leur engagement à chaque projet.',
    'why.team.link': 'Contactez-Nous',
    'why.team.member1.name': 'Ahmed El Amrani',
    'why.team.member1.role': 'PDG & Fondateur',
    'why.team.member2.name': 'Fatima Zahra Benali',
    'why.team.member2.role': 'Directrice des Opérations',
    'why.team.member3.name': 'Youssef El Khatib',
    'why.team.member3.role': 'Directeur Technique',
    'why.team.member4.name': 'Sofia Bennani',
    'why.team.member4.role': 'Responsable Qualité & Conformité',

    'why.cta.title': 'Solutions d\'Automatisation Fiables. Équipe Expérimentée. Résultats Prouvés.',
    'why.cta.desc': 'Des machines spéciales à l\'intégration robotique, MTS livre des solutions d\'automatisation industrielle clé en main dignes de confiance.',
    'why.cta.btn': 'Contactez-Nous',

    # === PARTNER ===
    'partner.meta.title': 'Nos Partenaires — MTS Automatisation Industrielle Maroc',
    'partner.meta.desc': 'MTS collabore avec les principaux fabricants automobile et industriels dont Marelli, APTIV, TE Connectivity, OPmobility, SOGEFI et Triumph.',
    'partner.banner.title': 'Nos Partenaires & Collaborateurs',
    'partner.banner.desc': 'Nous sommes fiers de collaborer avec les principaux fabricants automobile et industriels au Maroc et à l\'international.',
    'partner.features.title': 'Pourquoi Nos Partenariats Comptent',
    'partner.features.item1': 'Collaboration à long terme avec les leaders automobile de premier rang',
    'partner.features.item2': 'Compréhension approfondie des normes qualité automobile',
    'partner.features.item3': 'Parcours éprouvé de livraison de projets réussis',
    'partner.features.item4': 'Partenaire de confiance pour l\'automatisation critique de production',
    'partner.features.tag1': 'Automobile',
    'partner.features.tag2': 'Industrie',
    'partner.features.tag3': 'Automatisation',

    'partner.brands.desc': 'Nous sommes fiers de travailler avec les plus grandes marques automobile et industrielles',
    'partner.reviews.trust': 'Approuvé par les Leaders de l\'Industrie',
    'partner.reviews.score': 'Satisfaction Client',
    'partner.reviews.count': 'Années d\'Expérience',
    'partner.reviews.revenue': 'Projets Livrés',

    'partner.cta.title': 'Intéressé à Travailler Avec MTS ?',
    'partner.cta.desc': 'Contactez notre équipe pour discuter de la façon dont nous pouvons soutenir vos besoins en automatisation de fabrication.',
    'partner.cta.btn': 'Contactez-Nous',

    # === INDUSTRY ===
    'industry.meta.title': 'Secteurs d\'Activité — MTS Automatisation Industrielle',
    'industry.meta.desc': 'MTS dessert les secteurs automobile, électronique, industrie manufacturière avec des solutions d\'automatisation depuis notre site de Tanger, Maroc.',
    'industry.banner.title': 'Secteurs d\'Activité',
    'industry.banner.desc': 'MTS livre des solutions d\'automatisation industrielle dans les secteurs automobile, électronique et industrie manufacturière.',
    'industry.banner.btn': 'Découvrir Nos Solutions',
    'industry.banner.img': 'Secteurs d\'Activité',

    'industry.railway.title': 'Industrie Automobile',
    'industry.railway.desc': 'MTS fournit des lignes d\'assemblage automatisées, des cellules robotisées et des systèmes d\'inspection vision pour les fournisseurs automobile de premier rang. Nos solutions aident les constructeurs à atteindre un rendement supérieur, une qualité constante et des coûts de production réduits.',
    'industry.railway.item1': 'Lignes d\'Assemblage Automatisées',
    'industry.railway.item2': 'Pick and Place Robotisé',
    'industry.railway.item3': 'Systèmes d\'Inspection Vision',
    'industry.railway.item4': 'Outillage de Fin de Bras',
    'industry.railway.item5': 'Intégration PLC & IHM',
    'industry.railway.img': 'Industrie Automobile',

    'industry.aerospace.title': 'Électronique & Industrie',
    'industry.aerospace.desc': 'MTS livre des solutions d\'automatisation de précision pour l\'industrie électronique, incluant l\'assemblage de composants, l\'intégration de connecteurs et les systèmes d\'inspection qualité pour les producteurs de faisceaux de câbles et d\'électronique.',
    'industry.aerospace.item1': 'Automatisation d\'Assemblage de Composants',
    'industry.aerospace.item2': 'Intégration de Connecteurs',
    'industry.aerospace.item3': 'Assemblage de Faisceaux de Câbles',
    'industry.aerospace.item4': 'Systèmes de Contrôle Qualité',
    'industry.aerospace.item5': 'Solutions de Manutention',
    'industry.aerospace.img': 'Électronique & Industrie',

    'industry.benefits.title': 'Avantages des Solutions d\'Automatisation MTS',
    'industry.benefits.desc': 'Nos solutions d\'automatisation industrielles s\'appuient sur une expertise approfondie en génie mécanique, robotique, vision industrielle et ingénierie électrique pour résoudre des défis de fabrication complexes.',
    'industry.benefits.item1': 'Augmentation du Rendement de Production',
    'industry.benefits.item2': 'Qualité Produit Constante',
    'industry.benefits.item3': 'Réduction des Coûts d\'Exploitation',
    'industry.benefits.item4': 'Amélioration de la Sécurité au Travail',

    'industry.cta.title': 'Besoin d\'une Solution d\'Automatisation pour Votre Secteur ?',
    'industry.cta.desc': 'Contactez notre équipe pour découvrir comment MTS peut soutenir vos besoins spécifiques de fabrication.',
    'industry.cta.btn': 'Contactez-Nous',

    # === FOOTER ===
    'footer.desc': 'Intégrateur en automatisation industrielle basé à Tanger, Maroc. Machines spéciales, robotique, vision industrielle, convoyeurs et ingénierie électrique pour l\'industrie.',
    'footer.services.electrical': 'Ingénierie Électrique',
    'footer.services.electronics': 'Vision Industrielle',
    'footer.services.machines': 'Machines Spéciales & Robotique',
    'footer.services.maintenance': 'Maintenance & Support',
    'footer.services.distribution': 'Systèmes de Convoyage',
    'footer.copyright': 'Droits d\'Auteur © ',
    'footer.copyright_rest': '. MTS. Tous Droits Réservés.',
    'footer.rights': 'Tous Droits Réservés.',

    # === SIDEBAR ===
    'sidebar.desc': 'MTS est un intégrateur marocain en automatisation industrielle spécialisé dans les machines spéciales, la robotique, les systèmes de vision, les convoyeurs et l\'ingénierie électrique.',
    'sidebar.about_text': 'Machines spéciales, robotique, vision industrielle, convoyeurs et ingénierie électrique pour l\'automobile et l\'industrie.',

    # === MAP ===
    'map.popup_text': 'Lot n°58, ZAE Bni Ouassine<br>Province Fahs-Anjra, Tanger, Maroc<br>+212 610 764 921',

    # === CONTACT UPDATES ===
    'contact.info.call_us': 'Appelez-Nous',
    'contact.info.email_us': 'Envoyez-Nous un Email',
    'contact.card.phone.title': 'Téléphone',
    'contact.card.email.title': 'Email',
    'contact.card.address.title': 'Notre Adresse',
    'contact.hero.title': 'Prenez Contact',
    'contact.banner.title': 'Contactez-NOUS',
    'contact.form.first_name': 'Prénom',
    'contact.form.last_name': 'Nom',
    'contact.form.firstname': 'Prénom',
    'contact.form.lastname': 'Nom',
    'contact.form.email': 'Email',
    'contact.form.phone': 'Téléphone',
    'contact.form.send': 'Envoyer le Message',
    'contact.form.submit': 'Envoyer le Message',
    'contact.form.agree': 'Vous acceptez notre politique de confidentialité',
    'contact.form.first_name_placeholder': 'Votre Prénom',
    'contact.form.email_placeholder': 'email@exemple.com',
    'contact.form.phone_placeholder': 'Numéro de Téléphone',

    # === INDEX CONTACT FORM FR ===
    'index.form.name': 'Votre Nom',
    'index.form.email': 'Votre Email',
    'index.form.phone': 'Votre Téléphone',
    'index.form.submit': 'Envoyer le Message',
    'index.form.privacy': 'Vous acceptez notre politique de confidentialité',
    'index.contact.full_name': 'Nom Complet',
    'index.contact.email': 'Adresse Email',
    'index.contact.phone': 'Numéro de Téléphone',
    'index.contact.send': 'Envoyer le Message',

    # === ADDITIONAL MISSING FR ===
    'single.testimonials.1.name': 'Jean-Pierre Dubois',
    'single.testimonials.1.role': "Directeur d'Usine, Marelli",
    'single.testimonials.1.quote': 'MTS a livré une ligne d\'assemblage automatisée complexe pour notre usine automobile. Le projet a été terminé dans les délais et a dépassé nos attentes qualité.',
    'single.testimonials.2.name': 'Maria Garcia',
    'single.testimonials.2.role': 'Directrice de Production, APTIV',
    'single.testimonials.2.quote': 'L\'intégration robotique réalisée par MTS a transformé l\'efficacité de notre ligne de production. Hautement recommandé.',
    'single.testimonials.3.name': 'Thomas Mueller',
    'single.testimonials.3.role': 'Responsable Qualité, TE Connectivity',
    'single.testimonials.3.quote': 'Leur solution de vision industrielle a réduit notre taux de défauts de 98%. Une équipe fiable et professionnelle.',
    'single.testimonials.4.name': 'Sarah Johnson',
    'single.testimonials.4.role': "Directrice des Opérations, OPmobility",
    'single.testimonials.4.quote': 'De la conception à la mise en service, MTS a géré notre projet de système de convoyage avec un professionnalisme complet.',
}

# Apply FR updates
for k, v in fr_updates.items():
    if k in fr:
        fr[k] = v
    else:
        fr[k] = v  # Add if missing too

with open(os.path.join(d, 'fr.json'), 'w', encoding='utf-8') as f:
    json.dump(fr, f, ensure_ascii=False, indent=4)

# Sync ZH with English fallback for any keys that were updated
with open(os.path.join(d, 'zh.json'), 'r', encoding='utf-8') as f:
    zh = json.load(f)

for k, v in en.items():
    if k not in zh:
        zh[k] = v  # English fallback for missing keys

with open(os.path.join(d, 'zh.json'), 'w', encoding='utf-8') as f:
    json.dump(zh, f, ensure_ascii=False, indent=4)

print(f"Updated fr.json: {len(fr_updates)} changes, total {len(fr)} keys")
print(f"Synced zh.json: {len(zh)} keys")

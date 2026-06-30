$jsonPath = "C:\Users\MTS\Music\Coding\MTSWebsite\2digix-business-it-solutions-html-template-2025-09-21-06-46-01-utc\digix-main\lang\en.json"
$content = [System.IO.File]::ReadAllText($jsonPath, [System.Text.UTF8Encoding]::new($false))

function Apply-Replacement {
    param($key, $oldVal, $newVal)
    # Escape regex special chars in old value
    $escapedOld = [regex]::Escape($oldVal)
    $pattern = '"' + $key + '":\s*"' + $escapedOld + '"'
    $replacement = '"' + $key + '": "' + $newVal + '"'
    if ($content -match $pattern) {
        $script:content = $content -replace $pattern, $replacement
        return $true
    }
    return $false
}

# Each update: key, old value, new value
$updates = @(
    @('details.banner.title', 'Our Manufacturing System Technology Services', 'Electrical Equipment Design & Integration'),
    @('details.cta.title', 'Have a Specific Project in Mind?', 'Need Custom Electrical Equipment?'),
    @('details.cta.desc', 'Contact our engineering team for a detailed consultation and customized quote.', 'Contact our engineering team to discuss your project requirements and get a tailored solution.'),
    @('details.faq.q1', 'How do you ensure quality in your manufacturing?', 'What certifications do your electrical products meet?'),
    @('details.faq.a1', 'We maintain ISO 9001, IRIS, and EN9100 certifications with regular audits and continuous improvement processes across all facilities.', 'All our electrical equipment is manufactured under ISO 9001, IRIS, EN9100, and UL certified processes, meeting the strictest industry standards.'),
    @('details.faq.q2', 'Can you handle custom-designed equipment?', 'What is the typical lead time for custom cabinets?'),
    @('details.faq.a2', 'Yes. Our engineering team works closely with clients to design, prototype, and manufacture custom equipment tailored to their exact specifications.', 'Lead times vary by complexity but typically range from 4 to 12 weeks depending on design requirements and certification needs.'),
    @('details.faq.q3', 'What is your typical project turnaround time?', 'Do you provide on-site installation?'),
    @('details.faq.a3', 'Timelines depend on project scope and complexity. We provide detailed schedules during the quotation phase and communicate regularly throughout production.', 'Yes, we offer full on-site installation, integration, and commissioning services for all electrical equipment.'),
    @('single.banner.name', 'Pierre Laurent', 'Daniel Brown'),
    @('single.banner.desc', 'Pierre Laurent brings over 20 years of leadership experience in industrial manufacturing and system technology. Under his guidance, MTS has grown into a trusted partner for leading companies in railway, aeronautics, defense, and energy sectors across Europe and beyond.', 'Daniel is a seasoned industrial engineer with extensive experience in electrical systems, automation, and manufacturing technologies. He plays a pivotal role in delivering reliable industrial solutions at MTS.'),
    @('single.banner.follow', 'Follow Me', 'Follow Me:'),
    @('single.cta.title', 'Have a Question for Pierre?', 'Reliable Industrial Solutions. Experienced Team. Proven Results.'),
    @('single.cta.desc', 'Reach out to our team and we will connect you with the right expert.', 'From electrical equipment to robotic integration, MTS delivers end-to-end industrial services you can trust.'),
    @('partner.cta.title', 'Become a Partner?', 'Reliable Industrial Solutions. Experienced Team. Proven Results.'),
    @('partner.cta.desc', 'Interested in partnering with MTS? We are always looking to collaborate with innovative technology providers.', 'From electrical equipment to robotic integration, MTS delivers end-to-end industrial services you can trust.'),
    @('industry.cta.title', "Let\u0027s Discuss Your Industry Needs", 'Reliable Industrial Solutions. Experienced Team. Proven Results.'),
    @('service.cta.title', 'Ready to Transform Your Industrial Operations?', 'Need a Custom Industrial Solution?'),
    @('service.cta.desc', 'Contact our team of experts to discuss your project requirements.', "Let\u0027s discuss your project requirements. Our engineering team is ready to design the right solution for your needs."),
    @('service.why.title', 'What Sets Us Apart', 'Certified Quality Across Every Project'),
    @('service.why.1.title', 'Certified Quality', 'International Certifications'),
    @('service.why.1.desc', 'ISO 9001, IRIS, and EN9100 certifications ensuring the highest standards across all our operations.', 'ISO 9001, IRIS, EN9100, ISO 13485, UL, FAA, PART 145, PART 21G \u2014 we meet the strictest industry standards.'),
    @('service.why.2.title', 'Proven Expertise', 'Multi-Sector Expertise'),
    @('service.why.2.desc', '25+ years of industrial experience serving leading companies in railway, aeronautics, defense, energy, and medical sectors.', "Railway, aeronautics, defense, medical, energy, automation \u2014 we adapt to your sector\u0027s specific requirements."),
    @('service.why.3.title', 'Global Reach', '11 Production Sites'),
    @('service.why.3.desc', '11 production sites across France and international locations in Morocco, America, and Canada.', 'With facilities across France and international presence, we deliver locally with global capabilities.'),
    @('team.banner.desc', 'Our people are our greatest asset. With decades of combined experience in industrial manufacturing and system technology, our team delivers excellence on every project.', 'MTS brings together engineers, technicians, and specialists dedicated to delivering reliable industrial solutions across electrical equipment, automation, and maintenance.'),
    @('team.cta.title', 'Join Our Team of Experts?', 'Reliable Industrial Solutions. Experienced Team. Proven Results.'),
    @('team.cta.desc', 'We are always looking for talented professionals to join MTS. Get in touch to explore career opportunities.', 'From electrical equipment to robotic integration, MTS delivers end-to-end industrial services you can trust.'),
    @('team.team.pre', 'Our Team', 'Team Member'),
    @('team.team.title', 'The People Behind MTS', 'The People Behind Our Success'),
    @('team.team.desc', 'Get to know the skilled professionals driving innovation at MTS.', 'our success is driven by a dedicated team of engineers, technicians, and industrial specialists who bring their expertise and commitment to every project.'),
    @('team.team.member1.name', 'Pierre Laurent', 'Daniel Brown'),
    @('team.team.member2.name', 'Marc Dubois', 'Christopher Henry'),
    @('team.team.member3.name', 'Sophie Martin', 'Sarah Mitchell'),
    @('team.team.member4.name', 'Thomas Bernard', 'John Smith'),
    @('team.team.member1.role', 'Chief Executive Officer', 'Chief Executive Officer'),
    @('team.team.member2.role', 'Technical Director', 'Chief Operating Officer'),
    @('team.team.member3.role', 'Operations Director', 'Head of Operations'),
    @('team.team.member4.role', 'Quality Director', 'Senior Automation Engineer'),
    @('team.testimonials.title', 'What People Say About Us', 'What clients said'),
    @('team.testimonials.1.name', 'Jean Moreau', 'Marc Dubois'),
    @('team.testimonials.1.role', 'Operations Director, Alstom', 'Production Director, Alstom'),
    @('team.testimonials.1.quote', 'The team at MTS consistently delivers high-quality electrical solutions. Their professionalism and technical expertise are outstanding.', "Working with MTS has been a game-changer for our operations. Their electrical equipment and automation solutions have significantly improved our production efficiency. Their reliability and expertise are unmatched."),
    @('team.testimonials.2.name', 'Marie Lambert', 'Marc Dubois'),
    @('team.testimonials.2.role', 'Procurement Manager, Safran', 'Production Director, Alstom'),
    @('team.testimonials.2.quote', 'Working with MTS has been a great experience. Their attention to detail and commitment to deadlines is remarkable.', "Working with MTS has been a game-changer for our operations. Their electrical equipment and automation solutions have significantly improved our production efficiency. Their reliability and expertise are unmatched."),
    @('team.testimonials.3.name', 'Philippe Garnier', 'Marc Dubois'),
    @('team.testimonials.3.role', 'Plant Manager, Michelin', 'Production Director, Alstom'),
    @('team.testimonials.3.quote', 'MTS robotic solutions have transformed our production line. Highly recommended for any industrial automation project.', "Working with MTS has been a game-changer for our operations. Their electrical equipment and automation solutions have significantly improved our production efficiency. Their reliability and expertise are unmatched."),
    @('team.why.title', 'Why Work With Us?', 'Why Work With Us'),
    @('team.why.desc', 'At MTS, we combine technical expertise with a client-first approach to deliver industrial solutions that make a difference.', 'Join a team committed to engineering excellence and industrial innovation'),
    @('team.why.item1', 'Over 25 years of industry experience', 'A collaborative environment focused on technical excellence.'),
    @('team.why.item2', 'ISO 9001, IRIS \u0026 EN9100 certified', 'Opportunities to work on complex industrial and railway projects.'),
    @('team.why.item3', 'End-to-end project management', 'Continuous training and professional development programs.'),
    @('team.why.item4', '11 production sites worldwide', 'Competitive compensation and comprehensive benefits package.'),
    @('why.banner.title', 'Why MTS Stands Out', 'Experience the Difference with MTS'),
    @('why.intro', 'MTS combines decades of industrial expertise with certified quality standards to deliver manufacturing system technology solutions that our clients trust. Here is what makes us different.', "we\u0027re more than just an IT service provider \u2013 we\u0027re your dedicated partner in growth. Every solution is tailored to your manufacturing environment, ensuring peak performance and reliability. We prioritize quality, efficiency, and reliability, working closely with you to deliver measurable results."),
    @('why.cta.title', 'Ready to Experience the MTS Difference?', 'Reliable Industrial Solutions. Experienced Team. Proven Results.'),
    @('why.cta.desc', 'Contact us today to discuss your project and discover how our expertise can benefit your operations.', 'From electrical equipment to robotic integration, MTS delivers end-to-end industrial services you can trust.'),
    @('why.planning.title', 'How We Approach Every Project', 'Strategic Industrial Solutions to Drive Manufacturing and Growth'),
    @('why.planning.step1.title', 'Understanding Your Needs', 'Initial Consultation \u0026 Needs Assessment'),
    @('why.planning.step1.desc', 'We invest time in understanding your technical requirements, industry standards, and project goals before proposing any solution.', 'We assess your current manufacturing environment and create a customized roadmap that aligns industrial solutions with your production objectives.'),
    @('why.planning.step2.title', 'Tailored Solution Design', 'Strategy Development \u0026 Roadmap Creation'),
    @('why.planning.step2.desc', 'Our engineers design solutions specifically tailored to your application, ensuring optimal performance and compliance.', 'We assess your current manufacturing environment and create a customized roadmap that aligns industrial solutions with your production objectives.'),
    @('why.planning.step3.title', 'Flawless Execution', 'Implementation \u0026 Integration'),
    @('why.planning.step3.desc', 'We execute with precision, adhering to the highest quality standards and delivering on time, every time.', 'We assess your current manufacturing environment and create a customized roadmap that aligns industrial solutions with your production objectives.'),
    @('partner.banner.title', 'Trusted Partnerships for Superior Solutions', 'Our Partners \u0026 Collaborators'),
    @('partner.banner.desc', 'We collaborate with the world\u0027s leading industrial technology manufacturers to deliver the best solutions for our clients.', 'Partner with MTS to deliver reliable industrial solutions across manufacturing and automation'),
    @('partner.features.title', 'Key Benefits', 'Choose MTS Industrial Partners for:'),
    @('partner.features.item1', 'Access to cutting-edge technology from global leaders', 'Industrial Equipment Expertise'),
    @('partner.features.item2', 'Genuine certified components and full manufacturer warranty', 'Custom Machinery \u0026 Automation'),
    @('partner.features.item3', 'Technical support directly from OEM partners', 'Electrical \u0026 Electronic Assemblies'),
    @('partner.features.item4', 'Competitive pricing through strategic partnerships', 'Robotic Integration \u0026 Maintenance'),
    @('partner.brands.desc', 'MTS collaborates with leading global manufacturers to provide our clients with the highest quality industrial equipment and components. Our strategic partnerships ensure access to cutting-edge technology, genuine parts, and comprehensive technical support.', 'Collaborated with globally recognized brands and partners'),
    @('partner.reviews.trust', 'TrustScore 4.8', 'TrustScore 4.8 2k reviews'),
    @('industry.banner.desc', 'MTS delivers specialized manufacturing system technology solutions across a wide range of industrial sectors.', 'MTS delivers manufacturing system technology solutions across railway, aeronautics, defense, energy, and general industry sectors.'),
    @('industry.railway.title', 'Railway \u0026 Transportation', 'Railway \u0026 Transportation Systems'),
    @('industry.railway.desc', 'We design and manufacture electrical and electronic systems for the railway industry, including control cabinets, cable assemblies, and embedded electronic solutions for rolling stock and infrastructure.', 'MTS engineers and manufactures electrical systems, electronic assemblies, and control panels for railway rolling stock and infrastructure projects across Europe.'),
    @('industry.railway.item1', 'Control cabinets for rolling stock', 'Electrical System Engineering'),
    @('industry.railway.item2', 'Cable assemblies and harnesses', 'Control Panel Manufacturing'),
    @('industry.railway.item3', 'Embedded electronic systems', 'Railway Signaling Solutions'),
    @('industry.railway.item4', 'Signal processing equipment', 'Predictive Maintenance Systems'),
    @('industry.railway.item5', 'On-board diagnostic systems', 'Onboard Power Distribution'),
    @('industry.aerospace.title', 'Aerospace \u0026 Defense', 'Aerospace \u0026 Defense Manufacturing'),
    @('industry.aerospace.desc', 'MTS is EN9100 certified and supports civil and military aeronautics clients with high-precision electronic assemblies, special machines, and maintenance services for mission-critical applications.', 'In aerospace and defense, precision and compliance are critical. MTS manufactures high-reliability electronic assemblies and special-purpose machines that meet stringent MIL, aerospace, and nuclear standards'),
    @('industry.aerospace.item1', 'High-precision electronic assemblies', 'MIL-SPEC Electronic Assemblies'),
    @('industry.aerospace.item2', 'Test benches for avionics', 'Precision Machining \u0026 Fabrication'),
    @('industry.aerospace.item3', 'Special machines for defense manufacturing', 'Defense System Integration'),
    @('industry.aerospace.item4', 'Maintenance and repair of aerospace equipment', 'Compliance \u0026 Certification'),
    @('industry.aerospace.item5', 'Wiring and interconnection systems', 'Special-Purpose Machines'),
    @('industry.benefits.title', 'Cross-Industry Benefits', 'Benefits of MTS Industrial Services'),
    @('industry.benefits.desc', 'Our expertise benefits clients across all sectors with consistent quality, innovative solutions, and reliable support.', 'Our industrial services draw on decades of expertise in electrical engineering, automation, robotics, and system integration to solve complex manufacturing challenges'),
    @('industry.benefits.item1', 'Certified quality across all industries (ISO, IRIS, EN9100)', 'Custom Electrical Design'),
    @('industry.benefits.item2', 'Custom solutions tailored to each sector\u0027s regulations', 'Industrial Automation'),
    @('industry.benefits.item3', 'Dedicated project management for complex multi-site deployments', 'System Integration'),
    @('industry.benefits.item4', 'Ongoing technical support and maintenance programs', 'Preventive Maintenance')
)

$updated = 0
$notFound = @()
foreach ($u in $updates) {
    $key = $u[0]
    $oldVal = $u[1]
    $newVal = $u[2]
    $escapedOld = [regex]::Escape($oldVal)
    $pattern = '"' + $key + '":\s*"' + $escapedOld + '"'
    $replacement = '"' + $key + '": "' + $newVal + '"'
    if ($content -match $pattern) {
        $content = $content -replace $pattern, $replacement
        $updated++
    } else {
        $notFound += $key
    }
}

Write-Host "Updated $updated keys"
if ($notFound.Count -gt 0) {
    Write-Host "NOT FOUND ($($notFound.Count)):"
    $notFound | ForEach-Object { Write-Host "  $_" }
}

# Add new keys before closing brace
$newKeys = @()
$newKeys += '"details.banner.img": "Electrical Equipment"'
$newKeys += '"details.process.img": "Electrical process"'
$newKeys += '"details.faq.img": "FAQ"'
$newKeys += '"details.faq.desc": "We understand that every project is unique. Here are answers to common questions about our electrical equipment services."'
$newKeys += '"details.work.pre": "Our Expertise"'
$newKeys += '"details.work.title": "Electrical Equipment Design, Manufacturing \u0026 Integration"'
$newKeys += '"details.work.service1.title": "Cable Harnesses \u0026 Interconnections"'
$newKeys += '"details.work.service1.desc": "Design and manufacturing of custom cable harnesses and interconnection systems for railway, aeronautics, and defense applications."'
$newKeys += '"details.work.service1.tag1": "Railway"'
$newKeys += '"details.work.service1.tag2": "Aeronautics"'
$newKeys += '"details.work.service1.tag3": "Defense"'
$newKeys += '"details.work.service2.title": "Electrical Cabinets \u0026 Control Panels"'
$newKeys += '"details.work.service2.desc": "Low-voltage design, manufacturing, and installation of electrical cabinets and control panels tailored to your facility requirements."'
$newKeys += '"details.work.service2.tag1": "Low-Voltage"'
$newKeys += '"details.work.service2.tag2": "Control Systems"'
$newKeys += '"details.work.service2.tag3": "Integration"'
$newKeys += '"details.work.service3.title": "Embedded Electrical Equipment"'
$newKeys += '"details.work.service3.desc": "Specialized embedded electrical equipment for demanding environments including motorsport, medical, and industrial automation."'
$newKeys += '"details.work.service3.tag1": "Embedded Systems"'
$newKeys += '"details.work.service3.tag2": "Motorsport"'
$newKeys += '"details.work.service3.tag3": "Medical"'

1..4 | ForEach-Object {
    $newKeys += "`"single.testimonials.$_.name`": `"Sarah Williams`""
    $newKeys += "`"single.testimonials.$_.role`": `"Production Director, Alstom`""
    $newKeys += "`"single.testimonials.$_.quote`": `"The team at MTS truly understands our brand \u0026 audience. Their social media have not only boosted our engagement but also helped connect with customers.`""
}

$newKeys += '"partner.breadcrumb.home": "Home"'
$newKeys += '"partner.breadcrumb.partners": "Partner"'
$newKeys += '"partner.features.tag1": "Equipment Supply"'
$newKeys += '"partner.features.tag2": "Industrial Solutions"'
$newKeys += '"partner.features.tag3": "Field Services"'
$newKeys += '"team.team.link": "About MTS"'
$newKeys += '"why.breadcrumb.home": "Home"'
$newKeys += '"why.breadcrumb.why": "Why Choose Us"'
$newKeys += '"why.features.title": "Choose MTS Industrial Solutions for:"'
$newKeys += '"why.features.item1": "Expertise You Can Trust"'
$newKeys += '"why.features.item2": "Precision Engineering \u0026 Quality"'
$newKeys += '"why.features.item3": "End-to-End Industrial Solutions"'
$newKeys += '"why.features.item4": "Reliable Maintenance \u0026 Support"'
$newKeys += '"why.features.tag1": "Industrial Automation"'
$newKeys += '"why.features.tag2": "Electrical Engineering"'
$newKeys += '"why.features.tag3": "Engineering Services"'
$newKeys += '"why.planning.step1.tag1": "Industrial Consulting"'
$newKeys += '"why.planning.step1.tag2": "Electrical Engineering"'
$newKeys += '"why.planning.step1.tag3": "Engineering Services"'
$newKeys += '"why.planning.step2.tag1": "Industrial Automation"'
$newKeys += '"why.planning.step2.tag2": "Electrical Engineering"'
$newKeys += '"why.planning.step2.tag3": "Engineering Services"'
$newKeys += '"why.planning.step3.tag1": "Industrial Consulting"'
$newKeys += '"why.planning.step3.tag2": "Systems Integration"'
$newKeys += '"why.planning.step3.tag3": "Engineering Services"'
$newKeys += '"why.team.pre": "Team Member"'
$newKeys += '"why.team.title": "The People Behind Our Success"'
$newKeys += '"why.team.desc": "our success is driven by a dedicated team of industrial professionals who bring their expertise, skill and dedication to every project."'
$newKeys += '"why.team.link": "Contact Us"'
$newKeys += '"why.team.member1.name": "Daniel Brown"'
$newKeys += '"why.team.member1.role": "Chief Executive Officer"'
$newKeys += '"why.team.member2.name": "Christopher Henry"'
$newKeys += '"why.team.member2.role": "Chief Executive Officer"'
$newKeys += '"why.team.member3.name": "Marketing Director"'
$newKeys += '"why.team.member3.role": "Chief Executive Officer"'
$newKeys += '"why.team.member4.name": "John Smith"'
$newKeys += '"why.team.member4.role": "Senior Developer"'

# Insert before last line
$lines = $content -split "`r`n|`n"
$lastLine = $lines[-1].Trim()
if ($lastLine -eq '}') {
    $lines = $lines[0..($lines.Length-2)]
    $newKeysSorted = $newKeys | Sort-Object
    foreach ($k in $newKeysSorted) {
        $lines += "    $k,"
    }
    $lines += "}"
    $content = $lines -join "`r`n"
}

[System.IO.File]::WriteAllText($jsonPath, $content, [System.Text.UTF8Encoding]::new($false))
Write-Host "Done! Added $($newKeys.Count) new keys"

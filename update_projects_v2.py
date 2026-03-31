import os

projects = [
    {"name": "Personal Cloud", "file": "personal-cloud.html", "icon": "☁️", "feedback": "Mujeeb built a secure, high-performance cloud for us. The UI is slick and the file handling is robust. Highly recommend for any cloud projects."},
    {"name": "Mehwish Online Institute", "file": "mehwish-butt-tutor.html", "icon": "🎓", "feedback": "Mujeeb is very patient and highly skilled. The LMS he built for my institute is incredible and has made student management seamless. Highly recommended!"},
    {"name": "Library Management", "file": "library-management.html", "icon": "📚", "feedback": "A very professional desktop application. It handled our 5000+ book database without a single hitch. Great work on the reporting system."},
    {"name": "Pharmacy IMS", "file": "pharmacy-management.html", "icon": "💊", "feedback": "Mujeeb went above and beyond to deliver our pharmacy POS. The real-time sync between mobile and desktop is a life-saver for my business. - Ahmad Raza"},
    {"name": "Inventory Management", "file": "hostel-management.html", "icon": "📦", "feedback": "Adamesa: Mujeeb is very patient I need a pharmacy POS systems he went above and beyond to deliver my systems as described. Highly recommended his services. Thank you"},
    {"name": "JARVIS AI", "file": "jarvis-ai.html", "icon": "🎙️", "feedback": "The level of OS automation Mujeeb achieved with JARVIS is impressive. Voice recognition works flawlessly. Truly 'Tony Stark' level work."},
    {"name": "AI Photo Generator", "file": "ai-photo-generator.html", "icon": "🖼️", "feedback": "Impressive use of AI. The product photos generated are studio-quality. This tool is a game-changer for our e-commerce business."},
    {"name": "Weather Dashboard", "file": "weather-dashboard.html", "icon": "🌤️", "feedback": "A beautifully visualized weather dash. The real-time API sync and the map overlays are top-notch. Perfect for our field research."},
    {"name": "Video Editing Portfolio", "file": "video-portfolio.html", "icon": "🎬", "feedback": "Mujeeb's creative eye for video editing is outstanding. The motion graphics and cinematic cuts in the reel are breathtakingly professional."},
    {"name": "Custom Occasions", "file": "custom-occasions.html", "icon": "🎉", "feedback": "We needed a dynamic event site at the last minute and Mujeeb delivered a masterpiece. The interactive RSVP and theme system are brilliant."},
    {"name": "Portfolio Site", "file": "portfolio-site.html", "icon": "👔", "feedback": "This portfolio itself is a testament to Mujeeb's skills. Glassmorphism, animations, and high-end aesthetics throughout. A true pro."}
]

project_dir = r"h:\themujeeb.py\projects"

for i, p in enumerate(projects):
    filepath = os.path.join(project_dir, p["file"])
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Favicon & Background Script Fix
    if '<link rel="icon"' not in content:
        content = content.replace('</head>', '  <link rel="icon" type="image/png" href="../assets/fevicon.png">\n</head>')
    else:
        import re
        content = re.sub(r'<link rel="icon".*?>', '<link rel="icon" type="image/png" href="../assets/fevicon.png">', content)
    
    if 'assets/background.js' not in content:
        content = content.replace('</head>', '  <script src="../assets/background.js" defer></script>\n</head>')

    # 2. Navigation (Prev/Next)
    prev_idx = (i - 1) % len(projects)
    next_idx = (i + 1) % len(projects)
    prev_p = projects[prev_idx]
    next_p = projects[next_idx]
    
    nav_html = f'''
    <!-- Project Navigation -->
    <div class="flex flex-col md:flex-row justify-between items-center gap-8 py-16 border-t border-white/5 fade-up">
        <a href="{prev_p['file']}" class="group flex items-center gap-4 text-left">
            <div class="w-12 h-12 rounded-full border border-white/10 flex items-center justify-center group-hover:bg-amber-500 group-hover:text-black transition duration-300">←</div>
            <div>
                <span class="text-xs text-gray-500 uppercase block mb-1">Previous Project</span>
                <span class="font-bold group-hover:text-amber-500 transition">{prev_p['name']}</span>
            </div>
        </a>
        <a href="{next_p['file']}" class="group flex items-center gap-4 text-right">
            <div>
                <span class="text-xs text-gray-500 uppercase block mb-1">Next Project</span>
                <span class="font-bold group-hover:text-amber-500 transition">{next_p['name']}</span>
            </div>
            <div class="w-12 h-12 rounded-full border border-white/10 flex items-center justify-center group-hover:bg-amber-500 group-hover:text-black transition duration-300">→</div>
        </a>
    </div>
    '''
    
    # Insert before footer OR end of main
    if '<!-- Project Navigation -->' not in content:
        content = content.replace('</main>', nav_html + '\n  </main>')

    # 3. Specific Feedback
    feedback_html = f'''
    <section class="mb-24 fade-up">
        <h2 class="text-3xl font-bold mb-12 text-center">Project Feedback</h2>
        <div class="max-w-3xl mx-auto glass-card p-12 text-center relative overflow-hidden">
            <div class="text-6xl text-amber-500/10 absolute top-4 left-4 font-serif">"</div>
            <p class="text-xl text-white mb-8 italic relative z-10">"{p['feedback']}"</p>
            <div class="flex items-center justify-center gap-4 relative z-10">
                <div class="w-12 h-12 rounded-full bg-amber-500 flex items-center justify-center text-black font-bold">
                    {p['icon']}
                </div>
                <div class="text-left">
                    <h4 class="font-bold">Verified Client</h4>
                    <div class="text-amber-500 text-xs">★★★★★</div>
                </div>
            </div>
        </div>
    </section>
    '''
    # Replace old testimonials section
    import re
    content = re.sub(r'<!-- Testimonials -->.*?<section class="mb-24">.*?</section>', feedback_html, content, flags=re.DOTALL)
    
    # 4. CV & Live Buttons
    # If project is Mehwish LMS, Pharmacy IMS, AI Photo or Weather Dash, assume live link exists (placeholder for now)
    live_label = "View Live"
    live_icon = "🌐"
    is_live = p['name'] in ["Mehwish Online Institute", "Weather Dashboard", "Portolio Site"]
    
    # Fix CV/Live Button Logic
    cv_link = '../Mujeeb ur Rehman.pdf'
    content = content.replace('href="' + cv_link + '"', f'href="{cv_link}" target="_blank" download')
    
    # Save back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done!")

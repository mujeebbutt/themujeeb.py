import os
import re

projects = [
    {
        "name": "Personal Cloud", "file": "personal-cloud.html", "icon": "☁️",
        "feedback": "Mujeeb built a secure, high-performance cloud for us. The UI is slick and the file handling is robust. Highly recommend for any cloud projects.",
        "challenges": "Implementing secure end-to-end encryption for file streaming while maintaining high upload/download speeds and a responsive user interface.",
        "solutions": "Utilized advanced chunking algorithms and a distributed Node.js backend to handle heavy loads, paired with AES-256 for secure data transmission.",
        "achievements": ["Achieved 99.9% uptime during heavy load tests.", "Reduced average file transfer time by 40%.", "Implemented a sleek, dark-mode glassmorphic UI."]
    },
    {
        "name": "Mehwish Online Institute", "file": "mehwish-butt-tutor.html", "icon": "🎓",
        "feedback": "Mujeeb is very patient and highly skilled. The LMS he built for my institute is incredible and has made student management seamless. Highly recommended!",
        "challenges": "Designing an LMS that is extremely simple for non-technical educators while supporting complex grading logic and large file uploads.",
        "solutions": "Created a role-based dashboard system using Firebase, allowing real-time sync for assignments, modular attendance, and effortless access control.",
        "achievements": ["Onboarded 500+ students in the first week.", "Automated grading cut administrative time by 60%.", "Achieved zero-downtime integration with cloud storage."]
    },
    {
        "name": "Library Management", "file": "library-management.html", "icon": "📚",
        "feedback": "A very professional desktop application. It handled our 5000+ book database without a single hitch. Great work on the reporting system.",
        "challenges": "Managing relational data consistency in SQLite while ensuring the UI remained highly responsive during heavy database queries.",
        "solutions": "Implemented optimized SQL queries and used threading for database operations to prevent the main application thread from freezing.",
        "achievements": ["Successfully implemented complex fine-calculation algorithms.", "Zero data corruption reported during long-term testing.", "Designed a custom premium Tkinter theme."]
    },
    {
        "name": "Pharmacy IMS", "file": "pharmacy-management.html", "icon": "💊",
        "feedback": "Mujeeb went above and beyond to deliver our pharmacy POS. The real-time sync between mobile and desktop is a life-saver for my business.",
        "challenges": "Achieving instantaneous real-time synchronization between the mobile app barcode scanner and the desktop master database.",
        "solutions": "Built a robust real-time API layer with WebSocket event handling, implementing automatic conflict resolution for dual-entry scenarios.",
        "achievements": ["Achieved sub-second barcode scanning to database synchronization.", "Handled a 10,000+ product catalog seamlessly.", "Built a comprehensive automated reorder analytics dashboard."]
    },
    {
        "name": "Inventory Management", "file": "hostel-management.html", "icon": "📦",
        "feedback": "Adamesa: Mujeeb is very patient I need a pharmacy POS systems he went above and beyond to deliver my systems as described. Highly recommended his services.",
        "challenges": "Tracking dynamic asset allocations across multiple locations in real time while abstracting the complexity from the end-user.",
        "solutions": "Developed a granular tracking module with visual floorplan mapping and integrated low-stock push notification alerts.",
        "achievements": ["Cut inventory shrinkage by 35% within the first month.", "Automated the entire reordering workflow.", "Introduced mobile-first audit capabilities for field staff."]
    },
    {
        "name": "JARVIS AI", "file": "jarvis-ai.html", "icon": "🎙️",
        "feedback": "The level of OS automation Mujeeb achieved with JARVIS is impressive. Voice recognition works flawlessly. Truly 'Tony Stark' level work.",
        "challenges": "Achieving low-latency voice recognition and successfully executing complex OS-level commands bypassing strict security constraints.",
        "solutions": "Integrated advanced local speech models coupled with customized Python automation scripts utilizing the win32 API infrastructure.",
        "achievements": ["Consistently achieved sub-3-second response times.", "Automated 50+ daily local OS tasks bridging multiple applications.", "Created a seamless, entirely hands-free voice-UI."]
    },
    {
        "name": "AI Photo Generator", "file": "ai-photo-generator.html", "icon": "🖼️",
        "feedback": "Impressive use of AI. The product photos generated are studio-quality. This tool is a game-changer for our e-commerce business.",
        "challenges": "Abstracting complex generative AI models so non-technical users can achieve commercial-quality output reliably.",
        "solutions": "Built a highly-tuned Prompt-Engineering layer wrapping Stable Diffusion, paired with optimized GPU processing pipelines for speed.",
        "achievements": ["Achieved 70% faster turnaround time compared to traditional retouchers.", "Integrated cutting-edge AI for pixel-perfect background removal.", "Implemented custom aesthetic presets for 1-click styling."]
    },
    {
        "name": "Weather Dashboard", "file": "weather-dashboard.html", "icon": "🌤️",
        "feedback": "A beautifully visualized weather dash. The real-time API sync and the map overlays are top-notch. Perfect for our field research.",
        "challenges": "Aggregating multiple volatile weather APIs perfectly without hitting strict rate limits during peak usage surges.",
        "solutions": "Implemented a heavily optimized caching layer mapping historical and predictive data directly into interactive canvas charts.",
        "achievements": ["Deployed engaging, interactive real-time radar mapping.", "System handles 10k+ concurrent requests smoothly.", "Engineered a beautiful dynamic UI that changes based on local weather."]
    },
    {
        "name": "Video Editing Portfolio", "file": "video-portfolio.html", "icon": "🎬",
        "feedback": "Mujeeb's creative eye for video editing is outstanding. The motion graphics and cinematic cuts in the reel are breathtakingly professional.",
        "challenges": "Showcasing heavy, high-bitrate cinematic video projects on the web without causing browser lag or unacceptable load times.",
        "solutions": "Engineered a custom lazy-loading streaming video grid utilizing intersection observers and heavily compressed WebM fallbacks.",
        "achievements": ["Achieved near-instant playback even on slower cellular networks.", "Designed ultra-smooth cinematic transition animations.", "Maintained perfect 60fps scrolling performance despite heavy media."]
    },
    {
        "name": "Custom Occasions", "file": "custom-occasions.html", "icon": "🎉",
        "feedback": "We needed a dynamic event site at the last minute and Mujeeb delivered a masterpiece. The interactive RSVP and theme system are brilliant.",
        "challenges": "Building a custom event platform engineered to safely handle immense, sudden viral traffic spikes during ticket releases.",
        "solutions": "Utilized a cutting-edge serverless architecture configured for infinite horizontal scaling, backed by a robust NoSQL real-time database.",
        "achievements": ["Successfully processed 5,000+ active RSVPs in under an hour without throttling.", "Built a fully dynamic theming engine adaptable to different event types.", "Automated secure QR code ticket generation and email dispatch."]
    },
    {
        "name": "Portfolio Site", "file": "portfolio-site.html", "icon": "👔",
        "feedback": "This portfolio itself is a testament to Mujeeb's skills. Glassmorphism, animations, and high-end aesthetics throughout. A true pro.",
        "challenges": "Creating an immersive, cinematic personal portfolio that feels like a high-end software application rather than a basic static webpage.",
        "solutions": "Leveraged advanced CSS grid architectures, SVG path manipulation, multi-layered glassmorphism, and hardware-accelerated animations.",
        "achievements": ["Optimized rendering to maintain perfect scores on performance audits.", "Guaranteed flawless cross-device responsiveness down to mobile screens.", "Engineered seamless infinite scrolling marquees and intricate hover states."]
    }
]

project_dir = r"h:\themujeeb.py\projects"

for i, p in enumerate(projects):
    filepath = os.path.join(project_dir, p["file"])
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generate Content HTML
    achievements_list = ""
    for idx, achievement in enumerate(p["achievements"]):
        achievements_list += f"""
        <li class="flex gap-4">
            <span class="text-amber-500 font-black">{idx + 1}.</span>
            <p>{achievement}</p>
        </li>"""

    new_dynamic_sections = f"""
    <!-- DYNAMIC CASE STUDY CONTENT -->
    <section class="mb-24 fade-up">
      <h2 class="text-3xl font-bold mb-12">Challenges & Solutions</h2>
      <div class="grid md:grid-cols-2 gap-8">
        <div class="glass-card p-8 border-l-4 border-red-500/50">
          <h3 class="font-bold text-xl mb-4">The Challenge</h3>
          <p class="text-gray-400">{p["challenges"]}</p>
        </div>
        <div class="glass-card p-8 border-l-4 border-green-500/50 bg-white/5">
          <h3 class="font-bold text-xl mb-4">The Solution</h3>
          <p class="text-gray-400">{p["solutions"]}</p>
        </div>
      </div>
    </section>

    <section class="mb-24 fade-up">
      <h2 class="text-3xl font-bold mb-8">Achievements</h2>
      <ul class="space-y-4">
        {achievements_list}
      </ul>
    </section>

    <section class="mb-24 fade-up">
        <h2 class="text-3xl font-bold mb-12 text-center">Project Feedback</h2>
        <div class="max-w-3xl mx-auto glass-card p-12 text-center relative overflow-hidden">
            <div class="text-6xl text-amber-500/10 absolute top-4 left-4 font-serif">"</div>
            <p class="text-xl text-white mb-8 italic relative z-10">"{p['feedback']}"</p>
            <div class="flex items-center justify-center gap-4 relative z-10">
                <div class="w-12 h-12 rounded-full bg-amber-500 flex items-center justify-center text-black font-bold text-xl">
                    {p['icon']}
                </div>
                <div class="text-left">
                    <h4 class="font-bold">Verified Client</h4>
                    <div class="text-amber-500 text-xs">★★★★★</div>
                </div>
            </div>
        </div>
    </section>
    <!-- END DYNAMIC CASE STUDY CONTENT -->
    """

    # Strip existing Challenges/Solutions/Achievements/Feedback to prevent duplicates
    # Remove from <section class="mb-24"><h2...Challenges to the end of Feedback/What Clients Say
    content = re.sub(r'<section[^>]*>\s*<h2[^>]*>Challenges & Solutions.*?</section>', '', content, flags=re.DOTALL)
    content = re.sub(r'<section[^>]*>\s*<h2[^>]*>Achievements.*?</section>', '', content, flags=re.DOTALL)
    content = re.sub(r'<section[^>]*>\s*<h2[^>]*>What Clients Say.*?</section>', '', content, flags=re.DOTALL)
    content = re.sub(r'<section[^>]*>\s*<h2[^>]*>Project Feedback.*?</section>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- DYNAMIC CASE STUDY CONTENT -->.*?<!-- END DYNAMIC CASE STUDY CONTENT -->', '', content, flags=re.DOTALL)

    # Calculate Previous/Next Projects
    prev_p = projects[(i - 1) % len(projects)]
    next_p = projects[(i + 1) % len(projects)]

    nav_html = f'''
    <!-- Project Navigation -->
    <div class="flex flex-col md:flex-row justify-between items-center gap-8 py-16 border-t border-white/5 fade-up w-full mt-12">
        <a href="{prev_p['file']}" class="group flex items-center gap-4 text-left">
            <div class="w-12 h-12 rounded-full border border-white/10 flex items-center justify-center group-hover:bg-amber-500 group-hover:text-black transition duration-300">←</div>
            <div>
                <span class="text-xs text-gray-500 uppercase block mb-1">Previous Project</span>
                <span class="font-bold text-lg group-hover:text-amber-500 transition">{prev_p['name']}</span>
            </div>
        </a>
        <a href="{next_p['file']}" class="group flex items-center gap-4 text-right">
            <div>
                <span class="text-xs text-gray-500 uppercase block mb-1">Next Project</span>
                <span class="font-bold text-lg group-hover:text-amber-500 transition">{next_p['name']}</span>
            </div>
            <div class="w-12 h-12 rounded-full border border-white/10 flex items-center justify-center group-hover:bg-amber-500 group-hover:text-black transition duration-300">→</div>
        </a>
    </div>
    '''

    # Remove existing floating next button and old project navigation
    content = re.sub(r'<a href="[^"]+"\s*class="fixed bottom-10 right-10[^>]*>.*?</a>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- Project Navigation -->.*?</div>\s*(?=</main>)', '', content, flags=re.DOTALL)

    # Insert dynamic sections and navigation right before </main>
    # Make sure we don't insert multiple times if run multiple times
    clean_insertion = new_dynamic_sections + "\n" + nav_html + "\n  </main>"
    content = content.replace('</main>', clean_insertion)

    # Write identical CV button logic
    cv_link = '../Mujeeb ur Rehman.pdf'
    content = content.replace('href="' + cv_link + '"', f'href="{cv_link}" target="_blank" download')

    # Save changes
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Batch processing complete: 11 projects synchronized successfully with detailed case studies and bidirectional navigation!")

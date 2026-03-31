import os
import re

projects_dir = r"h:\themujeeb.py\projects"
files = [f for f in os.listdir(projects_dir) if f.endswith(".html")]

styles_to_add = """
        .mobile-menu {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100vh;
            background: rgba(10, 10, 10, 0.98);
            backdrop-filter: blur(20px);
            z-index: 40;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 2rem;
        }

        .mobile-menu.active {
            display: flex;
        }
    </style>"""

script_to_add = """
    <script>
        const observerOptions = { threshold: 0.1 };
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) entry.target.classList.add('visible');
            });
        }, observerOptions);
        document.querySelectorAll('section, h1, header, .glass-card').forEach(el => {
            el.classList.add('fade-up');
            observer.observe(el);
        });

        // Mobile Menu Toggle
        const mobileToggle = document.getElementById('mobile-toggle');
        const mobileMenu = document.getElementById('mobile-menu');
        const mobileClose = document.getElementById('mobile-close');

        if (mobileToggle && mobileMenu && mobileClose) {
            mobileToggle.addEventListener('click', () => {
                mobileMenu.classList.add('active');
                document.body.style.overflow = 'hidden';
            });

            mobileClose.addEventListener('click', () => {
                mobileMenu.classList.remove('active');
                document.body.style.overflow = 'auto';
            });

            // Close menu on link click
            mobileMenu.querySelectorAll('a').forEach(link => {
                link.addEventListener('click', () => {
                    mobileMenu.classList.remove('active');
                    document.body.style.overflow = 'auto';
                });
            });
        }
    </script>"""

for filename in files:
    filepath = os.path.join(projects_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already updated
    if 'id="mobile-toggle"' in content:
        print(f"Skipping {filename} - already updated.")
        continue

    # 1. Update Styles
    content = content.replace("    </style>", styles_to_add)

    # 2. Update Navbar
    nav_match = re.search(r'<nav id="navbar".*?>(.*?)</nav>', content, re.DOTALL)
    if nav_match:
        nav_inner = nav_match.group(1)
        name_match = re.search(r'class="text-2xl font-black text-white hover:text-amber-500 transition">(.*?)</a>', nav_inner)
        project_name = name_match.group(1) if name_match else "themujeeb.py"
        
        github_match = re.search(r'href="(https://github.com/.*?)"', nav_inner)
        github_link = github_match.group(1) if github_match else "https://github.com/mujeebbutt"

        new_nav = f"""    <nav id="navbar"
        class="fixed top-0 w-full z-50 transition-all duration-300 py-4 px-6 md:px-12 flex justify-between items-center nav-blur">
        <a href="../index.html" class="text-xl md:text-2xl font-black text-white hover:text-amber-500 transition">{project_name}</a>
        
        <!-- Desktop Menu -->
        <div class="hidden md:flex gap-8 text-sm font-medium text-gray-300">
            <a href="../index.html#home" class="hover:text-amber-500 transition border-b-2 border-transparent hover:border-amber-500">Home</a>
            <a href="../index.html#about" class="hover:text-amber-500 transition border-b-2 border-transparent hover:border-amber-500">About</a>
            <a href="../index.html#projects" class="hover:text-amber-500 transition border-b-2 border-transparent hover:border-amber-500">Projects</a>
            <a href="../index.html#skills" class="hover:text-amber-500 transition border-b-2 border-transparent hover:border-amber-500">Skills</a>
            <a href="../index.html#contact" class="hover:text-amber-500 transition border-b-2 border-transparent hover:border-amber-500">Contact</a>
        </div>

        <div class="flex items-center gap-4">
            <a href="{github_link}" target="_blank" class="hidden sm:block text-white transition text-2xl">
                <i class="fab fa-github"></i>
            </a>
            <a href="https://www.fiverr.com/s/BRVAD5b" target="_blank"
                class="bg-[#f5a623] hover:bg-[#c47a00] text-black px-4 md:px-6 py-2 rounded-full text-sm md:text-base font-bold transition">Hire
                Me</a>
            
            <!-- Mobile Toggle -->
            <button id="mobile-toggle" class="md:hidden text-white text-2xl focus:outline-none">
                <i class="fas fa-bars"></i>
            </button>
        </div>
    </nav>

    <!-- Mobile Menu Overlay -->
    <div id="mobile-menu" class="mobile-menu">
        <button id="mobile-close" class="absolute top-6 right-8 text-white text-3xl">&times;</button>
        <a href="../index.html#home" class="text-2xl font-bold text-white hover:text-amber-500 transition">Home</a>
        <a href="../index.html#about" class="text-2xl font-bold text-white hover:text-amber-500 transition">About</a>
        <a href="../index.html#projects" class="text-2xl font-bold text-white hover:text-amber-500 transition">Projects</a>
        <a href="../index.html#skills" class="text-2xl font-bold text-white hover:text-amber-500 transition">Skills</a>
        <a href="../index.html#contact" class="text-2xl font-bold text-white hover:text-amber-500 transition">Contact</a>
        <div class="flex gap-6 mt-4">
            <a href="{github_link}" target="_blank" class="text-white text-3xl">
                <i class="fab fa-github"></i>
            </a>
            <a href="https://linkedin.com/in/themujeebpy" target="_blank" class="text-white text-3xl">
                <i class="fab fa-linkedin"></i>
            </a>
        </div>
    </div>"""
        content = re.sub(r'<nav id="navbar".*?</nav>', new_nav, content, flags=re.DOTALL)

    # 3. Update Header
    content = content.replace('<header class="mb-16">', '<header class="mb-16 pt-8 md:pt-0">')
    content = content.replace('text-[clamp(36px,6vw,64px)]', 'text-[clamp(32px,7vw,64px)]')
    
    # Use regex for text-xl mb-8 to be more robust
    content = re.sub(r'text-xl mb-8">', 'text-lg md:text-xl mb-8 max-w-2xl">', content)
    
    content = content.replace('<div class="flex gap-4">', '<div class="flex flex-col sm:flex-row gap-4">')
    content = content.replace('px-8 py-3 rounded-lg font-bold transition">', 'px-8 py-3 rounded-lg font-bold transition text-center">')

    # 4. Update Grids
    content = content.replace('text-3xl font-bold mb-12 text-center">Key Features</h2>', 'text-2xl md:text-3xl font-bold mb-12 text-center">Key Features</h2>')

    # 5. Update Script
    content = re.sub(r'<script>.*?</script>', script_to_add, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

print(f"Completed.")

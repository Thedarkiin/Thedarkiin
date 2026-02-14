<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=220&color=0:001219,50:003049,100:005f73&text=Yassin%20Asermouh&fontSize=44&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Data%20Science%20Student&descAlignY=60&descSize=18" alt="ocean header"/>
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1200&color=00B4D8&center=true&vCenter=true&width=700&lines=Mathematics;Physics;Psychology;Climbing+%7C+Volleyball+%7C+Sea" alt="typing line"/>
</p>

---

<!-- INTERACTIVE 3D SKILL VISUALIZATION -->
<svg viewBox="0 0 1200 500" width="1200" height="500" xmlns="http://www.w3.org/2000/svg" style="margin: 40px auto; display: block;">
  <defs>
    <style>
      @keyframes rotate3d {
        0% { transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg); }
        100% { transform: rotateX(360deg) rotateY(360deg) rotateZ(180deg); }
      }
      @keyframes float { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-15px); } }
      @keyframes pulse { 0%, 100% { r: 35px; opacity: 0.8; } 50% { r: 42px; opacity: 1; } }
      @keyframes glow { 0%, 100% { filter: drop-shadow(0 0 8px rgba(0, 180, 216, 0.4)); } 50% { filter: drop-shadow(0 0 20px rgba(0, 180, 216, 0.9)); } }
      @keyframes orbit { 0% { transform: rotate(0deg) translateX(180px) rotate(0deg); } 100% { transform: rotate(360deg) translateX(180px) rotate(-360deg); } }
      
      .skill-orb { animation: float 2.5s ease-in-out infinite; cursor: pointer; }
      .skill-orb:hover { animation: float 1.2s ease-in-out infinite; }
      .skill-orb:hover circle { filter: drop-shadow(0 0 25px rgba(0, 180, 216, 1)); }
      .core { animation: glow 2s ease-in-out infinite, pulse 3s ease-in-out infinite; }
      .tech-name { font-family: 'Fira Code', monospace; font-size: 13px; font-weight: 600; fill: #fff; pointer-events: none; text-anchor: middle; }
    </style>
    
    <radialGradient id="core-glow" cx="30%" cy="30%">
      <stop offset="0%" style="stop-color:#00d4ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#005f73;stop-opacity:1" />
    </radialGradient>
    <radialGradient id="python-grad" cx="30%" cy="30%">
      <stop offset="0%" style="stop-color:#3776AB;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#1a4a6f;stop-opacity:1" />
    </radialGradient>
    <radialGradient id="torch-grad" cx="30%" cy="30%">
      <stop offset="0%" style="stop-color:#EE4C2C;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#8b2410;stop-opacity:1" />
    </radialGradient>
    <radialGradient id="web-grad" cx="30%" cy="30%">
      <stop offset="0%" style="stop-color:#F7DF1E;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#7d6f00;stop-opacity:1" />
    </radialGradient>
    <radialGradient id="data-grad" cx="30%" cy="30%">
      <stop offset="0%" style="stop-color:#150458;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#08022d;stop-opacity:1" />
    </radialGradient>
  </defs>
  
  <rect width="1200" height="500" fill="#001219" opacity="0"/>
  
  <!-- Core -->
  <circle cx="600" cy="250" r="55" fill="url(#core-glow)" class="core"/>
  <text x="600" y="260" class="tech-name" font-size="18">STACK</text>
  
  <!-- Orbital rings -->
  <circle cx="600" cy="250" r="180" fill="none" stroke="rgba(0, 180, 216, 0.1)" stroke-width="1"/>
  <circle cx="600" cy="250" r="220" fill="none" stroke="rgba(0, 180, 216, 0.05)" stroke-width="1"/>
  
  <!-- First orbit -->
  <g style="animation: orbit 25s linear infinite;">
    <circle cx="780" cy="250" r="35" fill="url(#python-grad)" class="skill-orb"/>
    <text x="780" y="258" class="tech-name">Python</text>
  </g>
  
  <g style="animation: orbit 25s linear infinite; animation-delay: 6.25s;">
    <circle cx="600" cy="70" r="35" fill="url(#torch-grad)" class="skill-orb"/>
    <text x="600" y="78" class="tech-name">PyTorch</text>
  </g>
  
  <g style="animation: orbit 25s linear infinite; animation-delay: 12.5s;">
    <circle cx="420" cy="250" r="35" fill="url(#web-grad)" class="skill-orb"/>
    <text x="420" y="258" class="tech-name">JavaScript</text>
  </g>
  
  <g style="animation: orbit 25s linear infinite; animation-delay: 18.75s;">
    <circle cx="600" cy="430" r="35" fill="url(#data-grad)" class="skill-orb"/>
    <text x="600" y="438" class="tech-name">SQL</text>
  </g>
  
  <!-- Secondary orbit (faster, reverse) -->
  <g style="animation: orbit 30s linear infinite reverse;">
    <circle cx="750" cy="140" r="30" fill="url(#python-grad)" opacity="0.7" class="skill-orb"/>
    <text x="750" y="147" class="tech-name" font-size="11">NumPy</text>
  </g>
  
  <g style="animation: orbit 30s linear infinite reverse; animation-delay: 7.5s;">
    <circle cx="810" cy="360" r="30" fill="url(#torch-grad)" opacity="0.7" class="skill-orb"/>
    <text x="810" y="367" class="tech-name" font-size="11">Pandas</text>
  </g>
  
  <g style="animation: orbit 30s linear infinite reverse; animation-delay: 15s;">
    <circle cx="450" cy="360" r="30" fill="url(#web-grad)" opacity="0.7" class="skill-orb"/>
    <text x="450" y="367" class="tech-name" font-size="11">React</text>
  </g>
  
  <g style="animation: orbit 30s linear infinite reverse; animation-delay: 22.5s;">
    <circle cx="390" cy="140" r="30" fill="url(#data-grad)" opacity="0.7" class="skill-orb"/>
    <text x="390" y="147" class="tech-name" font-size="11">Git</text>
  </g>
</svg>

---

## About
Data Science student at INSEA. I value clarity, mathematical rigor, and reproducible code.  
Curiosity drives my work — I study mathematics, physics, and human cognition. Outside of study: climbing, volleyball, calisthenics, gaming, and the sea.

---

<!-- PROFICIENCY BARS -->
<svg viewBox="0 0 800 380" width="800" height="380" xmlns="http://www.w3.org/2000/svg" style="margin: 30px auto; display: block;">
  <defs>
    <style>
      @keyframes fill { 0% { width: 0%; } 100% { width: var(--w, 85%); } }
      @keyframes slide-in { 0% { opacity: 0; transform: translateX(-20px); } 100% { opacity: 1; transform: translateX(0); } }
      .bar-bg { fill: #003049; rx: 8; }
      .bar-fill { rx: 8; animation: fill 2.2s cubic-bezier(0.34, 1.56, 0.64, 1) forwards; }
      .bar-label { font-family: 'Fira Code'; font-size: 13px; font-weight: 600; fill: #00B4D8; animation: slide-in 0.6s ease-out forwards; }
      .bar-value { font-family: 'Fira Code'; font-size: 12px; fill: #00B4D8; font-weight: 700; }
    </style>
    <linearGradient id="barGrad1" x1="0%" x2="100%">
      <stop offset="0%" style="stop-color:#005f73"/>
      <stop offset="100%" style="stop-color:#00B4D8"/>
    </linearGradient>
    <linearGradient id="barGrad2" x1="0%" x2="100%">
      <stop offset="0%" style="stop-color:#0096c7"/>
      <stop offset="100%" style="stop-color:#00B4D8"/>
    </linearGradient>
    <linearGradient id="barGrad3" x1="0%" x2="100%">
      <stop offset="0%" style="stop-color:#003049"/>
      <stop offset="100%" style="stop-color:#00B4D8"/>
    </linearGradient>
  </defs>
  
  <rect width="800" height="380" fill="#001219" opacity="0"/>
  
  <text x="50" y="35" class="bar-label" font-size="18" font-weight="700">Proficiency</text>
  
  <text x="50" y="75" class="bar-label" style="animation-delay: 0s;">Python</text>
  <rect x="180" y="60" width="580" height="20" class="bar-bg"/>
  <rect x="180" y="60" width="522" height="20" fill="url(#barGrad1)" class="bar-fill" style="animation-delay: 0.2s; width: 0%;"/>
  <text x="770" y="78" class="bar-value">95%</text>
  
  <text x="50" y="135" class="bar-label" style="animation-delay: 0.1s;">PyTorch</text>
  <rect x="180" y="120" width="580" height="20" class="bar-bg"/>
  <rect x="180" y="120" width="464" height="20" fill="url(#barGrad2)" class="bar-fill" style="animation-delay: 0.4s; width: 0%;"/>
  <text x="770" y="138" class="bar-value">85%</text>
  
  <text x="50" y="195" class="bar-label" style="animation-delay: 0.2s;">JavaScript</text>
  <rect x="180" y="180" width="580" height="20" class="bar-bg"/>
  <rect x="180" y="180" width="494" height="20" fill="url(#barGrad1)" class="bar-fill" style="animation-delay: 0.6s; width: 0%;"/>
  <text x="770" y="198" class="bar-value">90%</text>
  
  <text x="50" y="255" class="bar-label" style="animation-delay: 0.3s;">Data Science</text>
  <rect x="180" y="240" width="580" height="20" class="bar-bg"/>
  <rect x="180" y="240" width="522" height="20" fill="url(#barGrad3)" class="bar-fill" style="animation-delay: 0.8s; width: 0%;"/>
  <text x="770" y="258" class="bar-value">92%</text>
  
  <text x="50" y="315" class="bar-label" style="animation-delay: 0.4s;">Web Stack</text>
  <rect x="180" y="300" width="580" height="20" class="bar-bg"/>
  <rect x="180" y="300" width="464" height="20" fill="url(#barGrad2)" class="bar-fill" style="animation-delay: 1s; width: 0%;"/>
  <text x="770" y="318" class="bar-value">88%</text>
  
  <text x="50" y="375" class="bar-label" style="animation-delay: 0.5s; font-size: 11; opacity: 0.7;">Mathematics & Systems</text>
</svg>

---

<!-- TECH STACK BADGES -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React"/>
  <img src="https://img.shields.io/badge/SQL-003B57?style=for-the-badge&logo=mysql&logoColor=white" alt="SQL"/>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
</p>

---

<!-- ANIMATED STATS -->
<svg viewBox="0 0 1000 220" width="1000" height="220" xmlns="http://www.w3.org/2000/svg" style="margin: 30px auto; display: block;">
  <defs>
    <style>
      @keyframes card-pop { 0% { opacity: 0; transform: scale(0.8) translateY(20px); } 100% { opacity: 1; transform: scale(1) translateY(0); } }
      @keyframes number-bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }
      .stat-card { animation: card-pop 0.5s cubic-bezier(0.34, 1.56, 0.64, 1) forwards; }
      .stat-card:nth-child(2) { animation-delay: 0.1s; }
      .stat-card:nth-child(3) { animation-delay: 0.2s; }
      .stat-card:nth-child(4) { animation-delay: 0.3s; }
      .stat-num { font-family: 'Fira Code'; font-size: 42px; font-weight: 700; fill: #00B4D8; animation: number-bounce 2s ease-in-out infinite; }
      .stat-txt { font-family: 'Fira Code'; font-size: 12px; fill: #005f73; font-weight: 600; letter-spacing: 1px; }
      .card-border { stroke: #00B4D8; stroke-width: 2; fill: #001219; rx: 10; }
    </style>
  </defs>
  
  <rect width="1000" height="220" fill="#001219" opacity="0"/>
  
  <g class="stat-card">
    <rect x="40" y="20" width="200" height="180" class="card-border"/>
    <text x="140" y="70" class="stat-num" text-anchor="middle">12+</text>
    <text x="140" y="120" class="stat-txt" text-anchor="middle">PROJECTS</text>
    <text x="140" y="140" class="stat-txt" text-anchor="middle" opacity="0.6" font-size="10">Shipped & Live</text>
  </g>
  
  <g class="stat-card">
    <rect x="270" y="20" width="200" height="180" class="card-border"/>
    <text x="370" y="70" class="stat-num" text-anchor="middle">50K+</text>
    <text x="370" y="120" class="stat-txt" text-anchor="middle">LINES CODE</text>
    <text x="370" y="140" class="stat-txt" text-anchor="middle" opacity="0.6" font-size="10">Written & Tested</text>
  </g>
  
  <g class="stat-card">
    <rect x="500" y="20" width="200" height="180" class="card-border"/>
    <text x="600" y="70" class="stat-num" text-anchor="middle">15+</text>
    <text x="600" y="120" class="stat-txt" text-anchor="middle">TECH SKILLS</text>
    <text x="600" y="140" class="stat-txt" text-anchor="middle" opacity="0.6" font-size="10">Languages & Tools</text>
  </g>
  
  <g class="stat-card">
    <rect x="730" y="20" width="230" height="180" class="card-border"/>
    <text x="845" y="70" class="stat-num" text-anchor="middle">∞</text>
    <text x="845" y="120" class="stat-txt" text-anchor="middle">LEARNING</text>
    <text x="845" y="140" class="stat-txt" text-anchor="middle" opacity="0.6" font-size="10">Always Growing</text>
  </g>
</svg>

---

## Skills
- Numerical methods & applied mathematics  
- Time series and forecasting fundamentals  
- Model evaluation, uncertainty estimation, and reproducibility  
- Clean, modular code and small automated tests  
- Data wrangling and feature engineering

---

<!-- CONTACT SECTION -->
<p align="center">
  <a href="https://thedarkiin.github.io/portfolio/">
    <img src="https://img.shields.io/badge/Portfolio-Visit-005f73?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio"/>
  </a>
  <a href="mailto:asermouhyassin@gmail.com">
    <img src="https://img.shields.io/badge/Email-Contact-003049?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
  </a>
  <a href="https://github.com/Thedarkiin">
    <img src="https://img.shields.io/badge/GitHub-Profile-001219?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
</p>

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=120&color=0:005f73,100:001219&section=footer" alt="ocean footer"/>
</p>

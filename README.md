<!--
  High-temperature, design-forward GitHub Profile README
  - No emojis, no CV content
  - Animated typing header (SVG)
  - Animated gradient banner (inline SVG, no external JS)
  - Minimal, modular sections with personality
-->

<!-- Hero / header -->
<div align="center">

  <!-- animated gradient banner (inline SVG, lightweight) -->
  <svg width="100%" height="140" viewBox="0 0 1200 140" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <defs>
      <linearGradient id="g" x1="0%" x2="100%" y1="0%" y2="0%">
        <stop offset="0%" stop-color="#0f172a">
          <animate attributeName="stop-color" dur="8s" repeatCount="indefinite"
            values="#0f172a;#0b1220;#07273a;#0f172a" />
        </stop>
        <stop offset="50%" stop-color="#002b36">
          <animate attributeName="stop-color" dur="8s" repeatCount="indefinite"
            values="#002b36;#003b4a;#0b3a4a;#002b36" />
        </stop>
        <stop offset="100%" stop-color="#001219">
          <animate attributeName="stop-color" dur="8s" repeatCount="indefinite"
            values="#001219;#001827;#011e2f;#001219" />
        </stop>
      </linearGradient>

      <!-- subtle moving mask used to give a slow parallax wave illusion -->
      <pattern id="p" x="0" y="0" width="1200" height="140" patternUnits="userSpaceOnUse">
        <rect x="0" y="0" width="1200" height="140" fill="url(#g)"/>
      </pattern>
    </defs>

    <!-- base rect with gradient -->
    <rect width="1200" height="140" fill="url(#g)"/>

    <!-- three semi-transparent sine layers to suggest movement -->
    <g fill-opacity="0.12" stroke="none">
      <path d="M0 90 C150 70 300 110 450 90 C600 70 750 110 900 90 C1050 70 1200 110 1350 90 L1350 140 L0 140 Z" fill="#ffffff">
        <animateTransform attributeName="transform" attributeType="XML" type="translate" dur="10s" repeatCount="indefinite" values="0 0; -150 0; 0 0"/>
      </path>
      <path d="M0 100 C200 80 400 120 600 100 C800 80 1000 120 1200 100 C1400 80 1600 120 1800 100 L1800 140 L0 140 Z" fill="#000000">
        <animateTransform attributeName="transform" attributeType="XML" type="translate" dur="14s" repeatCount="indefinite" values="0 0; -220 0; 0 0"/>
      </path>
    </g>

    <!-- centered title text (plain, no emoji) -->
    <text x="50%" y="55" text-anchor="middle" dominant-baseline="middle" font-family="Inter, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial" font-size="24" fill="#D1D5DB">
      Yassin Asermouh — Data Science student (INSEA)
    </text>
  </svg>

  <!-- animated typing line (external SVG generator) -->
  <p>
    <img alt="typing" src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&pause=1500&color=D1D5DB&center=true&width=720&lines=modular+engineer;volleyball+player;climber+%7C+sea+enthusiast;calisthenics+practitioner;drawer+occasionally" />
  </p>

</div>

---

## About me

I am a Data Science student at INSEA. I prefer **modular code** over notebooks — I design reproducible components, unit-testable modules, and deterministic pipelines.

Outside of code: volleyball, soccer, climbing, calisthenics, gaming, the sea, and occasional drawing.

---

## Interests & curiosity

- Neurons · Mathematics · Psychology  
- Physics and the foundational side of computation  
- Systems thinking: treat ML as production systems, not one-off notebooks

---

## Quick facts

| Role | Location | Portfolio |
|---:|:---|:---|
| Student — Data Science (INSEA) | Rabat, Morocco | https://thedarkiin.github.io/portfolio/ |

---

<details>
<summary>Skills & habits (expand)</summary>

- Languages & tools (concise): Python · PyTorch · Scikit-learn · NumPy · Pandas  
- Engineering habits: modular code, reproducible pipelines, structured logging, small tests  
- Learning focus: mathematical rigor, neuro-inspired ideas, causal thinking
</details>

---

## Small touches you can enable

- **Typing animation** — uses a small dynamic SVG service (example pattern above) to produce a typewriter effect. See: readme-typing-svg. :contentReference[oaicite:1]{index=1}  
- **Animated gradient / wave** — inline SVG uses SMIL/CSS animations for a lightweight, moving banner (no JS). See generators and wave examples. :contentReference[oaicite:2]{index=2}  
- **(Optional)** GitHub stat cards (language & commits) from `github-readme-stats` if you want compact analytics in the header. :contentReference[oaicite:3]{index=3}

---

## Contact

Portfolio: https://thedarkiin.github.io/portfolio/  
Email: asermouhyassin@gmail.com


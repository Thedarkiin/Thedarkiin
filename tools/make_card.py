"""Generate assets/card-dark.svg and assets/card-light.svg.

Run from the github_profile folder:  python tools/make_card.py
Edit INFO below to change the text. No dependency beyond Python.
"""
import math
from pathlib import Path
from xml.sax.saxutils import escape

INFO = [
    ("title", "yassin@asermouh"),
    ("rule", ""),
    ("kv", "Role", "Researcher, freelancer"),
    ("kv", "Studies", "Data Science"),
    ("kv", "Works on", "AI, and the UIs around it"),
    ("gap", ""),
    ("head", "exploring"),
    ("item", "causal inference"),
    ("item", "data engineering (Apache, HDFS, Snowflake)"),
    ("item", "systems design"),
    ("item", "neuroplasticity"),
    ("item", "3D medical segmentation (U-Net, SegResNet)"),
    ("item", "human-like learning in RL-free models"),
    ("gap", ""),
    ("head", "stack"),
    ("kv", "AI", "Python, PyTorch, TensorFlow, Pandas"),
    ("kv", "Data", "Snowflake"),
    ("kv", "UI", "React, TypeScript, Tailwind, Figma"),
    ("gap", ""),
    ("quote", "I like problems where the answer isn't obvious"),
    ("quote", "and the data is messy."),
]

THEMES = {
    "dark": dict(bg="#0d1117", bar="#161b22", line="#30363d", text="#c9d1d9",
                 dim="#8b949e", accent="#2dd4bf", accent2="#7ee8d8", art=("#134e4a", "#0f766e", "#14b8a6", "#5eead4")),
    "light": dict(bg="#ffffff", bar="#f6f8fa", line="#d0d7de", text="#1f2328",
                  dim="#59636e", accent="#0d7377", accent2="#0a5c5f", art=("#99d5cf", "#3aa8a0", "#0d7377", "#07484b")),
}

COLS, ROWS = 46, 25
CHARS = " .:-=+*#%@"


def brain():
    """ASCII side view of a brain: a lobed outline shaded by folded ridges."""
    grid = []
    for r in range(ROWS):
        row = []
        y = (r - 10.5) / 10.5
        for c in range(COLS):
            x = (c - 21.5) / 21.5
            # Cerebrum: flattened underside, slightly bumpy outline.
            angle = math.atan2(y, x)
            bump = 1 + 0.045 * math.sin(9 * angle) + 0.03 * math.sin(17 * angle)
            flat = 1.0 if y < 0 else 1.32
            cerebrum = math.hypot(x, y * flat) < 0.93 * bump
            # Cerebellum at the back (left), brain stem below it.
            cere = math.hypot((x + 0.42) / 0.36, (y - 0.74) / 0.34) < 1
            stem = abs(x + 0.08 + 0.12 * (y - 1)) < 0.075 and 0.55 < y < 1.32
            value = None
            if cerebrum:
                # Gyri: two warped sine fields give the folded surface.
                warp = 0.9 * math.sin(2.1 * x + 1.3 * y)
                fold = math.sin(8.5 * x + 4.5 * warp) * math.cos(10.5 * y - 3.5 * warp)
                light = 0.55 - 0.32 * y + 0.12 * x
                value = light + 0.42 * fold
            elif cere:
                value = 0.45 + 0.4 * math.sin(26 * y)
            elif stem:
                value = 0.5
            if value is None:
                row.append(" ")
            else:
                level = max(1, min(len(CHARS) - 1, int(value * (len(CHARS) - 1))))
                row.append(CHARS[level])
        grid.append("".join(row).rstrip())
    return grid


def art_svg(grid, colors, x0, y0, lh, cw):
    out = []
    for r, line in enumerate(grid):
        if not line:
            continue
        spans = []
        for ch, group in _runs(line):
            if ch is None:
                spans.append(" " * len(group))
            else:
                spans.append(f'<tspan fill="{colors[ch]}">{escape(group)}</tspan>')
        delay = 0.03 * r
        out.append(
            f'<text class="art" style="animation-delay:{delay:.2f}s" x="{x0}" y="{y0 + r * lh}" '
            f'textLength="{len(line) * cw:.1f}" lengthAdjust="spacingAndGlyphs" xml:space="preserve">'
            + "".join(spans) + "</text>"
        )
    return "\n".join(out)


def _runs(line):
    """Group characters by colour band (None for spaces)."""
    def band(c):
        if c == " ":
            return None
        return min(3, CHARS.index(c) * 4 // len(CHARS))
    cur, buf = band(line[0]), line[0]
    for c in line[1:]:
        b = band(c)
        if b == cur:
            buf += c
        else:
            yield cur, buf
            cur, buf = b, c
    yield cur, buf


def info_svg(t, x0, y0, lh):
    out, y, n = [], y0, 0
    for row in INFO:
        kind = row[0]
        attrs = f'class="info" style="animation-delay:{0.5 + 0.05 * n:.2f}s" x="{x0}" y="{y}"'
        if kind == "title":
            out.append(f'<text {attrs} font-weight="700" fill="{t["accent"]}">{escape(row[1])}</text>')
        elif kind == "rule":
            out.append(f'<text {attrs} fill="{t["line"]}">{"-" * 15}</text>')
        elif kind == "kv":
            out.append(f'<text {attrs}><tspan fill="{t["accent"]}" font-weight="700">{escape(row[1])}</tspan>'
                       f'<tspan fill="{t["dim"]}">: </tspan><tspan fill="{t["text"]}">{escape(row[2])}</tspan></text>')
        elif kind == "head":
            out.append(f'<text {attrs} font-weight="700" fill="{t["accent2"]}">{escape(row[1])}</text>')
        elif kind == "item":
            out.append(f'<text {attrs}><tspan fill="{t["accent"]}">&gt; </tspan>'
                       f'<tspan fill="{t["text"]}">{escape(row[1])}</tspan></text>')
        elif kind == "quote":
            out.append(f'<text {attrs} font-style="italic" fill="{t["dim"]}">{escape(row[1])}</text>')
        y += lh if kind != "gap" else lh * 0.55
        n += 1
    return "\n".join(out), y


def card(name):
    t = THEMES[name]
    width, bar_h, lh_art, cw = 900, 34, 15.2, 7.6
    grid = brain()
    art_x, art_y = 24, bar_h + 42
    info_x = art_x + COLS * cw + 28
    info, end_y = info_svg(t, info_x, bar_h + 34, 19)
    height = int(max(end_y, art_y + ROWS * lh_art) + 18)
    colors = dict(enumerate(t["art"]))
    dots = "".join(f'<circle cx="{20 + 20 * i}" cy="17" r="6" fill="{c}"/>'
                   for i, c in enumerate(("#ff5f56", "#ffbd2e", "#27c93f")))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="Terminal card for Yassin Asermouh with an ASCII drawing of a brain">
<style>
text {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "DejaVu Sans Mono", "Liberation Mono", monospace; font-size: 13.5px; }}
.art {{ font-size: 12.5px; opacity: 0; animation: show .35s ease-out forwards; }}
.info {{ opacity: 0; animation: show .35s ease-out forwards; }}
@keyframes show {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
@media (prefers-reduced-motion: reduce) {{ .art, .info {{ animation: none; opacity: 1; }} }}
</style>
<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="10" fill="{t['bg']}" stroke="{t['line']}"/>
<path d="M1 {bar_h}V11a10 10 0 0 1 10-10H{width - 11}a10 10 0 0 1 10 10V{bar_h}Z" fill="{t['bar']}"/>
{dots}
<text x="{width / 2}" y="22" text-anchor="middle" fill="{t['dim']}">asermouh ~ neofetch</text>
{art_svg(grid, colors, art_x, art_y, lh_art, cw)}
{info}
</svg>
'''


def main():
    out = Path(__file__).resolve().parent.parent / "assets"
    out.mkdir(exist_ok=True)
    for name in THEMES:
        (out / f"card-{name}.svg").write_text(card(name), encoding="utf-8")
    print("\n".join(brain()))


if __name__ == "__main__":
    main()

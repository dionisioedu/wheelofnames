#!/usr/bin/env python3
"""
Generate the complete Wheel Of List favicon / icon family from a single
programmatic brand mark (Pillow, no external assets).

Design (matches icons/icon-512x512.png):
  - Deep indigo "starry night" background (#2E1A47) with scattered white dots
  - 8-segment wheel with a thick golden rim (#F6B93B)
  - Golden centre hub, golden pointer triangle at 12 o'clock

Outputs:
  favicon.ico                       (multi-res: 16, 32, 48)
  icons/favicon-16x16.png
  icons/favicon-32x32.png
  icons/favicon-96x96.png
  icons/favicon-128x128.png
  icons/icon-192x192.png            (PWA "any")
  icons/icon-512x512.png            (PWA "any" + maskable source)

The maskable icon gets ~20% safe padding so the full wheel survives Android's
circular/rounded mask crop.

Usage:  python3 _gen/gen_favicons.py
"""
import math
import os
import random

from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICONS = os.path.join(ROOT, "icons")

# ---- Palette -------------------------------------------------------------
BG = (46, 26, 71)          # #2E1A47 deep indigo
RIM = (246, 185, 59)       # #F6B93B golden
HUB_OUTER = (246, 185, 59)
HUB_INNER = (249, 231, 159)  # #F9E79F pale yellow
SEGMENTS = [
    (231, 76, 60),    # #E74C3C crimson  (top-right)
    (52, 152, 219),   # #3498DB royal blue
    (39, 174, 96),    # #27AE60 emerald
    (142, 68, 173),   # #8E44AD amethyst
    (243, 156, 18),   # #F39C12 tangerine
    (241, 196, 15),   # #F1C40F golden yellow
    (26, 188, 156),   # #1ABC9C turquoise
    (22, 160, 133),   # #16A085 darker teal
]

# supersampling factor for crisp anti-aliased small icons
SS = 4


def draw_stars(draw, size, seed=7):
    """Scatter small white dots for the starry background (density scales with area)."""
    rng = random.Random(seed)
    n = max(10, int((size / 64) ** 2 * 3))  # ~3 stars per 64px cell
    for _ in range(n):
        x = rng.uniform(0, size)
        y = rng.uniform(0, size)
        r = rng.uniform(size * 0.004, size * 0.011)
        a = rng.randint(90, 210)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 255, a))


def render_mark(size, padding_ratio=0.0):
    """Render the brand mark at `size` px (square), with optional safe padding."""
    S = size * SS
    img = Image.new("RGBA", (S, S), BG + (255,))
    draw = ImageDraw.Draw(img, "RGBA")

    # starry background (drawn across full canvas including padding margin)
    draw_stars(draw, S)

    # geometry
    cx = cy = S / 2
    pad = S * padding_ratio
    outer_r = S / 2 - pad - S * 0.02          # wheel outer radius
    rim_w = max(2, int(S * 0.055))            # rim thickness
    seg_r = outer_r - rim_w                   # radius of coloured segments

    # coloured segments (8 x 45deg), start at top going clockwise
    start = -90.0
    for i, color in enumerate(SEGMENTS):
        a0 = start + i * 45.0
        a1 = a0 + 45.0
        draw.pieslice(
            [cx - seg_r, cy - seg_r, cx + seg_r, cy + seg_r],
            start=a0, end=a1, fill=color + (255,),
        )

    # thin light dividers between segments — keeps the wheel legible when tiny
    divider = max(1, int(S * 0.006))
    for i in range(8):
        a = math.radians(start + i * 45.0)
        x = cx + seg_r * math.cos(a)
        y = cy + seg_r * math.sin(a)
        draw.line([(cx, cy), (x, y)], fill=(255, 255, 255, 120), width=divider)

    # golden outer rim
    draw.ellipse(
        [cx - outer_r, cy - outer_r, cx + outer_r, cy + outer_r],
        outline=RIM + (255,), width=rim_w,
    )

    # centre hub
    hub_r = seg_r * 0.17
    draw.ellipse([cx - hub_r, cy - hub_r, cx + hub_r, cy + hub_r],
                 fill=HUB_OUTER + (255,))
    inner_r = hub_r * 0.62
    draw.ellipse([cx - inner_r, cy - inner_r, cx + inner_r, cy + inner_r],
                 fill=HUB_INNER + (255,))

    # pointer triangle at 12 o'clock, pointing down into the wheel
    tip_y = cy - seg_r + seg_r * 0.42
    base_y = cy - outer_r - S * 0.005
    half = outer_r * 0.20
    draw.polygon(
        [(cx, tip_y), (cx - half, base_y), (cx + half, base_y)],
        fill=RIM + (255,),
    )

    return img.resize((size, size), Image.LANCZOS)


def save_png(img, path):
    img.save(path, "PNG")
    print("wrote", os.path.relpath(path, ROOT))


def main():
    os.makedirs(ICONS, exist_ok=True)

    # Standard favicon PNGs
    for s in (16, 32, 96, 128, 180):
        save_png(render_mark(s), os.path.join(ICONS, f"favicon-{s}x{s}.png"))

    # PWA icons — maskable variant gets safe padding so the wheel isn't cropped
    save_png(render_mark(192), os.path.join(ICONS, "icon-192x192.png"))
    save_png(render_mark(512), os.path.join(ICONS, "icon-512x512.png"))
    save_png(render_mark(512, padding_ratio=0.20),
             os.path.join(ICONS, "icon-512x512-maskable.png"))
    save_png(render_mark(192, padding_ratio=0.20),
             os.path.join(ICONS, "icon-192x192-maskable.png"))

    # Multi-resolution favicon.ico at the root (16/32/48)
    ico_src = render_mark(256)
    ico_path = os.path.join(ROOT, "favicon.ico")
    ico_src.save(ico_path, format="ICO",
                 sizes=[(16, 16), (32, 32), (48, 48)])
    print("wrote", os.path.relpath(ico_path, ROOT))

    print("done.")


if __name__ == "__main__":
    main()

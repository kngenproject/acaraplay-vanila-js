#!/usr/bin/env python3
"""
generate_icons.py — Buat icons/icon-192.png dan icons/icon-512.png
untuk AcaraPlay PWA. Jalankan sekali sebelum upload ke GitHub.

Requirements: pip install Pillow
"""
import os
from PIL import Image, ImageDraw

os.makedirs("icons", exist_ok=True)

def make_icon(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Background rounded rect
    radius = size // 5
    bg_color = (13, 13, 13, 255)
    draw.rounded_rectangle([0, 0, size-1, size-1], radius=radius, fill=bg_color)

    # Accent circle
    pad = size // 6
    accent = (232, 168, 56, 255)
    draw.ellipse([pad, pad, size-pad, size-pad], fill=accent)

    # Play triangle
    tri_pad = size // 3
    tri_x1 = int(size * 0.38)
    tri_x2 = int(size * 0.78)
    tri_y_mid = size // 2
    tri_top = int(size * 0.28)
    tri_bot = int(size * 0.72)
    draw.polygon(
        [(tri_x1, tri_top), (tri_x1, tri_bot), (tri_x2, tri_y_mid)],
        fill=(13, 13, 13, 255)
    )

    return img

for size in [192, 512]:
    icon = make_icon(size)
    path = f"icons/icon-{size}.png"
    icon.save(path, "PNG")
    print(f"✓ {path} ({size}x{size})")

print("\nIkon berhasil dibuat! Siap di-upload ke GitHub.")

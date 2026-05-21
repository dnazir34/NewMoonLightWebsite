"""
Run once: python generate-favicons.py
Requires: pip install cairosvg Pillow
Generates favicon PNG files from favicon.svg
"""
import os, sys

try:
    import cairosvg
    from PIL import Image
    import io
except ImportError:
    print("Installing required packages...")
    os.system(f"{sys.executable} -m pip install cairosvg Pillow")
    import cairosvg
    from PIL import Image
    import io

svg_path = os.path.join(os.path.dirname(__file__), "favicon.svg")

sizes = {
    "favicon-16x16.png":   16,
    "favicon-32x32.png":   32,
    "favicon-48x48.png":   48,
    "apple-touch-icon.png": 180,
    "android-chrome-192x192.png": 192,
    "android-chrome-512x512.png": 512,
}

for filename, size in sizes.items():
    png_bytes = cairosvg.svg2png(url=svg_path, output_width=size, output_height=size)
    out_path = os.path.join(os.path.dirname(__file__), filename)
    with open(out_path, "wb") as f:
        f.write(png_bytes)
    print(f"Created {filename} ({size}x{size})")

# Also create favicon.ico (16+32+48 multi-size)
imgs = []
for s in [16, 32, 48]:
    png_bytes = cairosvg.svg2png(url=svg_path, output_width=s, output_height=s)
    imgs.append(Image.open(io.BytesIO(png_bytes)).convert("RGBA"))

ico_path = os.path.join(os.path.dirname(__file__), "favicon.ico")
imgs[0].save(ico_path, format="ICO", sizes=[(16,16),(32,32),(48,48)], append_images=imgs[1:])
print("Created favicon.ico (16+32+48)")

print("\nAll done! Upload all files to moonlightautocare.com root folder.")

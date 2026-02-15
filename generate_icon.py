#!/usr/bin/env python3
"""
Icon Generator for Keyboard Tester
Membuat icon keyboard sederhana untuk aplikasi
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_keyboard_icon():
    """Create a simple keyboard icon"""
    # Create image with transparent background
    size = 256
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Background - rounded rectangle
    padding = 20
    bg_color = (30, 30, 46, 255)  # Dark background
    draw.rounded_rectangle(
        [(padding, padding), (size-padding, size-padding)],
        radius=20,
        fill=bg_color
    )
    
    # Draw keyboard keys
    key_color = (137, 180, 250, 255)  # Blue
    key_size = 30
    key_spacing = 8
    
    # Top row (numbers)
    start_x = 45
    start_y = 60
    for i in range(6):
        x = start_x + i * (key_size + key_spacing)
        draw.rounded_rectangle(
            [(x, start_y), (x + key_size, start_y + key_size)],
            radius=5,
            fill=key_color
        )
    
    # Middle row
    start_y = 100
    for i in range(6):
        x = start_x + i * (key_size + key_spacing)
        draw.rounded_rectangle(
            [(x, start_y), (x + key_size, start_y + key_size)],
            radius=5,
            fill=key_color
        )
    
    # Bottom row
    start_y = 140
    for i in range(5):
        x = start_x + 15 + i * (key_size + key_spacing)
        draw.rounded_rectangle(
            [(x, start_y), (x + key_size, start_y + key_size)],
            radius=5,
            fill=key_color
        )
    
    # Space bar
    space_width = 120
    space_x = (size - space_width) // 2
    start_y = 180
    draw.rounded_rectangle(
        [(space_x, start_y), (space_x + space_width, start_y + key_size)],
        radius=5,
        fill=key_color
    )
    
    return img

def main():
    """Generate icon files"""
    print("🎨 Generating keyboard icon...")
    
    # Create icon
    icon = create_keyboard_icon()
    
    # Save as PNG (for Linux and general use)
    icon.save('keyboard_icon.png', 'PNG')
    print("✅ Created: keyboard_icon.png")
    
    # Save multiple sizes for ICO (Windows)
    icon_sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
    icons = []
    for size in icon_sizes:
        resized = icon.resize(size, Image.Resampling.LANCZOS)
        icons.append(resized)
    
    # Save as ICO
    icons[0].save('keyboard_icon.ico', format='ICO', sizes=[(s[0], s[1]) for s in icon_sizes])
    print("✅ Created: keyboard_icon.ico")
    
    print("\n✨ Icon files ready!")
    print("📁 Files created:")
    print("   - keyboard_icon.png (for Linux)")
    print("   - keyboard_icon.ico (for Windows)")

if __name__ == '__main__':
    try:
        main()
    except ImportError:
        print("❌ PIL/Pillow not installed")
        print("📦 Installing Pillow...")
        import subprocess
        subprocess.run(['pip3', 'install', 'Pillow'])
        print("\n🔄 Please run this script again")

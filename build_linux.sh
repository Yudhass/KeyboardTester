#!/bin/bash

# Build script for Linux
# Script untuk build aplikasi Keyboard Tester menjadi executable

echo "========================================="
echo "  Keyboard Tester - Build Script (Linux)"
echo "========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 tidak ditemukan. Silakan install Python3 terlebih dahulu."
    exit 1
fi

echo "✅ Python3 ditemukan: $(python3 --version)"
echo ""

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 tidak ditemukan. Silakan install pip3 terlebih dahulu."
    exit 1
fi

echo "✅ pip3 ditemukan"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Gagal install dependencies"
    exit 1
fi

echo "✅ Dependencies terinstall"
echo ""

# Clean previous build
if [ -d "build" ]; then
    echo "🧹 Membersihkan build sebelumnya..."
    rm -rf build
fi

if [ -d "dist" ]; then
    rm -rf dist
fi

if [ -f "KeyboardTester.spec" ]; then
    rm -f KeyboardTester.spec
fi

echo ""

# Build executable
echo "🔨 Building executable..."
echo ""

# Check if icon exists, if not generate it
if [ ! -f "keyboard_icon.png" ]; then
    echo "⚠️  Icon tidak ditemukan, generating..."
    python3 generate_icon.py
    echo ""
fi

pyinstaller --onefile \
            --windowed \
            --name="KeyboardTester" \
            --icon=keyboard_icon.png \
            keyboard.py

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Build gagal"
    exit 1
fi

echo ""
echo "========================================="
echo "  ✅ Build berhasil!"
echo "========================================="
echo ""
echo "📁 Executable berada di: ./dist/KeyboardTester"
echo ""
echo "Untuk menjalankan:"
echo "  ./dist/KeyboardTester"
echo ""
echo "Atau copy ke lokasi lain:"
echo "  cp ./dist/KeyboardTester ~/Desktop/"
echo ""

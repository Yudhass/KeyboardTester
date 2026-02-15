# 🚀 Quick Start Guide - Keyboard Tester

## Cara Tercepat untuk Memulai

### Linux (Anda saat ini di sini)

1. **Jalankan langsung tanpa build:**
   ```bash
   ./run.sh
   ```
   
   Atau:
   ```bash
   python3 keyboard_tester.py
   ```

2. **Build menjadi executable:**
   ```bash
   ./build_linux.sh
   ```
   
   Kemudian jalankan:
   ```bash
   ./dist/KeyboardTester
   ```

### Windows

1. **Jalankan langsung tanpa build:**
   ```cmd
   run.bat
   ```
   
   Atau:
   ```cmd
   python keyboard_tester.py
   ```

2. **Build menjadi executable:**
   ```cmd
   build_windows.bat
   ```
   
   Kemudian double-click:
   ```
   dist\KeyboardTester.exe
   ```

## Fitur Utama

✅ **Tiga Ukuran Keyboard:**
- Full Size (100%) - Keyboard lengkap dengan numpad
- TKL (80%) - Tanpa numpad
- 60% - Keyboard kompak

✅ **Visual Status Tombol:**
- Abu-abu = Belum pernah ditekan
- Biru = Sudah pernah ditekan
- Hijau = Sedang ditekan sekarang

✅ **Kontrol:**
- Dropdown untuk pilih ukuran keyboard
- Tombol Reset untuk mulai dari awal
- Display tombol terakhir yang ditekan
- Counter total tombol yang sudah ditekan

## Troubleshooting Cepat

**Error: "tkinter not found" (Linux)**
```bash
sudo apt-get install python3-tk
```

**Error: "python not found"**
- Install Python 3.8+ dari python.org

**Aplikasi tidak merespons keyboard:**
- Pastikan window aplikasi dalam kondisi fokus/aktif
- Klik pada window aplikasi terlebih dahulu

## Tips

- Untuk testing keyboard mekanik, gunakan mode Full Size
- Untuk laptop, mode 60% atau TKL lebih sesuai
- Gunakan tombol Reset setelah testing selesai untuk mulai fresh
- Aplikasi bisa berjalan tanpa internet

---

**Selamat mencoba! Jika ada pertanyaan, lihat README.md untuk dokumentasi lengkap.**

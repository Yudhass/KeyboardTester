# ⌨️ Keyboard Tester

Aplikasi desktop modern untuk testing keyboard dengan antarmuka GUI yang intuitif. Mendukung Windows dan Linux dengan kemampuan untuk menampilkan berbagai ukuran keyboard (Full Size, TKL, 60%).

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey.svg)

## ✨ Fitur

- 🎨 **Tampilan Modern:** UI dengan tema dark mode yang nyaman di mata
- ⌨️ **3 Ukuran Keyboard:** Full Size (100%), TKL (80%), dan 60%
- 🎯 **Visual Feedback:** Tiga status berbeda untuk setiap tombol:
  - Belum pernah ditekan (Abu-abu)
  - Pernah ditekan (Biru)
  - Sedang ditekan (Hijau)
- 🔄 **Reset Function:** Tombol untuk mereset semua status
- 📊 **Statistik:** Menampilkan total tombol yang sudah ditekan
- 🖥️ **Cross-Platform:** Berjalan di Windows dan Linux
- 📦 **Offline:** Tidak memerlukan koneksi internet

## 📋 Persyaratan

- Python 3.8 atau lebih tinggi
- tkinter (sudah termasuk dalam instalasi Python standar)

## 🚀 Cara Menjalankan

### Metode 1: Jalankan Langsung dengan Python

1. **Clone atau Download Repository**
   ```bash
   cd /home/yudhas/Dokumen/GIT_DESKTOP/KeyboardTester
   ```

2. **Jalankan Aplikasi**
   ```bash
   python3 keyboard_tester.py
   ```
   
   Di Windows:
   ```cmd
   python keyboard_tester.py
   ```

### Metode 2: Build Executable (Recommended untuk Distribusi)

#### Untuk Linux:

1. **Install Dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

2. **Build Executable**
   ```bash
   pyinstaller --onefile --windowed --name="KeyboardTester" keyboard_tester.py
   ```

3. **Hasil build ada di folder `dist/`**
   ```bash
   ./dist/KeyboardTester
   ```

#### Untuk Windows:

1. **Install Dependencies**
   ```cmd
   pip install -r requirements.txt
   ```

2. **Build Executable**
   ```cmd
   pyinstaller --onefile --windowed --name="KeyboardTester" keyboard_tester.py
   ```

3. **Hasil build ada di folder `dist\`**
   ```cmd
   dist\KeyboardTester.exe
   ```

## 📖 Cara Menggunakan

1. **Pilih Ukuran Keyboard**
   - Gunakan dropdown di bagian atas untuk memilih ukuran keyboard yang sesuai
   - Pilihan: Full Size (100%), TKL (80%), atau 60%

2. **Mulai Testing**
   - Tekan tombol apa saja di keyboard Anda
   - Tombol akan berubah warna sesuai status:
     - **Abu-abu**: Belum pernah ditekan
     - **Biru**: Sudah pernah ditekan
     - **Hijau**: Sedang ditekan (aktif)

3. **Lihat Informasi**
   - "Tombol Terakhir" menampilkan tombol yang baru saja ditekan
   - "Total tombol ditekan" menampilkan jumlah tombol unik yang sudah ditekan

4. **Reset Testing**
   - Klik tombol "🔄 Reset" untuk mengulang dari awal
   - Semua tombol akan kembali ke status awal (abu-abu)

## 🎨 Tema Warna

Aplikasi menggunakan skema warna Catppuccin-inspired:
- Background: Dark (#1e1e2e)
- Tombol belum ditekan: Abu-abu (#45475a)
- Tombol sudah ditekan: Biru (#89b4fa)
- Tombol aktif: Hijau (#a6e3a1)
- Teks: Light (#cdd6f4)

## 🛠️ Build Lanjutan dengan Custom Icon

Jika Anda ingin menambahkan icon khusus:

1. **Siapkan file icon** (keyboard.ico untuk Windows, keyboard.png untuk Linux)

2. **Build dengan icon:**

   Linux:
   ```bash
   pyinstaller --onefile --windowed --name="KeyboardTester" --icon=keyboard.png keyboard_tester.py
   ```
   
   Windows:
   ```cmd
   pyinstaller --onefile --windowed --name="KeyboardTester" --icon=keyboard.ico keyboard_tester.py
   ```

## 🐛 Troubleshooting

### Tkinter tidak ditemukan (Linux)

Jika Anda mendapat error tentang tkinter, install dengan:

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**Fedora:**
```bash
sudo dnf install python3-tkinter
```

**Arch Linux:**
```bash
sudo pacman -S tk
```

### PyInstaller build error

Jika ada masalah dengan PyInstaller, coba install ulang:
```bash
pip uninstall pyinstaller
pip install pyinstaller==6.3.0
```

### Aplikasi tidak dapat fokus pada keyboard input

Pastikan window aplikasi dalam kondisi aktif/fokus. Klik pada window aplikasi sebelum menekan tombol keyboard.

## 📝 Struktur Proyek

```
KeyboardTester/
├── keyboard_tester.py      # File aplikasi utama
├── requirements.txt         # Dependencies Python
├── README.md               # Dokumentasi (file ini)
└── target.md               # File target/notes
```

## 🔧 Kustomisasi

Anda dapat mengkustomisasi aplikasi dengan mengedit `keyboard_tester.py`:

- **Warna**: Edit dictionary `self.colors` di method `__init__`
- **Layout Keyboard**: Modifikasi method `get_fullsize_layout()`, `get_tkl_layout()`, atau `get_60_layout()`
- **Ukuran Window**: Ubah parameter di `self.root.geometry()`
- **Font**: Ganti font family di berbagai widget

## 📄 Lisensi

MIT License - Bebas digunakan untuk keperluan pribadi maupun komersial.

## 🤝 Kontribusi

Kontribusi selalu diterima! Silakan buat pull request atau laporkan issues yang ditemukan.

## 📞 Support

Jika Anda menemui masalah atau memiliki pertanyaan, silakan buat issue di repository ini.

---

**Selamat mencoba aplikasi Keyboard Tester! 🎉**

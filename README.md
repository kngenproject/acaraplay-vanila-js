# 🎵 AcaraPlay

**Music player PWA** untuk acara, event, dan penggunaan sehari-hari.  
Full offline, installable, dan berjalan 100% di browser tanpa backend.

---

## ✨ Fitur

- 🎵 Multi-playlist dengan rename & drag-and-drop urutan lagu
- 🔊 Volume slider vertikal (landscape) + horizontal (portrait)
- 🌊 Fade In / Fade Out manual & crossfade otomatis
- 🔀 Shuffle, Loop lagu, Loop semua
- ⏱️ Timer mulai putar otomatis (jadwal waktu)
- 🎛️ EQ visualizer real-time (Web Audio API)
- 🖥️ Mode Fullscreen
- 🎨 8 pilihan warna aksen
- ⌨️ Keyboard shortcuts lengkap
- 📱 Responsive: portrait & landscape
- 💾 Data tersimpan di IndexedDB (tetap ada setelah reload)
- 📲 **Installable sebagai PWA** (Android, iOS, Desktop)
- ✈️ **Full offline** via Service Worker

---

## ⌨️ Keyboard Shortcuts

| Tombol | Aksi |
|--------|------|
| `Space` | Play / Pause |
| `← / →` | Lagu sebelumnya / berikutnya |
| `↑ / ↓` | Volume naik / turun |
| `M` | Mute |
| `G` | Fade In |
| `F` | Fade Out |
| `S` | Toggle Shuffle |
| `L` | Toggle Loop |
| `Esc / T` | Buka / tutup Fullscreen |

---

## 🚀 Deploy ke GitHub Pages

### 1. Buat repository baru di GitHub
```bash
git init
git add .
git commit -m "init: AcaraPlay PWA"
git branch -M main
git remote add origin https://github.com/USERNAME/acaraplay.git
git push -u origin main
```

### 2. Aktifkan GitHub Pages
- Buka repo → **Settings** → **Pages**
- Source: **Deploy from a branch** → branch `main` → folder `/ (root)`
- Klik **Save**

### 3. Akses aplikasi
```
https://USERNAME.github.io/acaraplay/
```

> **Catatan:** Setelah deploy, tunggu ~1 menit lalu buka URL di atas. Service Worker akan aktif otomatis dan app bisa digunakan offline.

---

## 📁 Struktur File

```
acaraplay/
├── index.html          # Aplikasi utama (HTML + CSS + JS)
├── sw.js               # Service Worker (offline cache)
├── manifest.json       # PWA manifest (install prompt)
├── icons/
│   ├── icon-192.png    # Ikon PWA 192×192
│   └── icon-512.png    # Ikon PWA 512×512
├── generate_icons.py   # Script generate ikon (opsional)
└── README.md
```

---

## 🔧 Cara Generate Ulang Ikon

Jika ingin ikon custom, edit `generate_icons.py` lalu jalankan:
```bash
pip install Pillow
python3 generate_icons.py
```

---

## 📝 Catatan Teknis

- **Audio files** tidak ter-cache di Service Worker (blob URL, dimuat dari device)
- Data playlist (nama lagu) tersimpan di **IndexedDB** — URL audio hilang saat reload, file perlu dipilih ulang
- Berfungsi optimal di Chrome, Edge, Firefox, dan Safari iOS 16+
- Untuk install di iOS: Safari → Share → **"Add to Home Screen"**

---

## 📄 Lisensi

MIT — bebas digunakan dan dimodifikasi.

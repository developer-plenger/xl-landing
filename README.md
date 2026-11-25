# Landing page XL Home — preview statis

Salinan statis dari https://pasangwifixlhome.com untuk preview. Layout, teks, dan CSS
diambil 1:1 dari situs aslinya; tidak ada React/PocketBase, jadi ringan dan bisa
langsung dibuka tanpa build step.

## Lihat preview

```bash
python3 -m http.server 8899
# buka http://localhost:8899
```

## Struktur

```
index.html            hasil build — jangan diedit manual
build.py              sumber konten (paket, FAQ, teks, nomor WA) -> index.html
assets/css/style.css  CSS hasil ekstrak dari situs asli
assets/js/main.js     nav mobile, accordion FAQ, form -> WhatsApp, banner cookie
assets/img/           gambar (beberapa ukuran untuk srcset)
```

Edit konten di `build.py`, lalu:

```bash
python3 build.py      # regenerate index.html
```

## Ganti aset

Semua gambar ada di `assets/img/`. Cukup timpa file dengan nama yang sama:

| File | Dipakai di | Rasio |
|---|---|---|
| `logo.jpg` | header + footer | 1:1 (ditampilkan 168×52) |
| `hero-*.png` | hero besar | 1280×832 |
| `advantages-*.png` | section keunggulan | 1216×896 |
| `steps-*.png` | section proses pemasangan | 1216×896 |
| `favicon.png` | ikon tab | 1:1 |

Setiap gambar punya 4 ukuran (`-375`, `-768`, `-1024`, `-1280`) untuk `srcset`.
Untuk mengganti cepat, timpa `-1280` dan biarkan ukuran lain, atau hapus atribut
`srcset` di `index.html` bila hanya ingin satu file.

## Yang beda dari situs asli

- Formulir kontak tidak punya backend: submit membuka WhatsApp dengan data
  yang diisi. Ganti handler di `assets/js/main.js` kalau nanti ada API.
- Banner cookie hanya visual (menyimpan pilihan di cookie `cc_cookie`), tanpa
  tracker.
- Nomor WhatsApp, nama sales, dan teks diatur di bagian atas `build.py`.

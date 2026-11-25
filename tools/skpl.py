"""Generate SKPL (lembar permintaan data & gambar) untuk landing page XL Home.

Template kop surat diambil dari kop-pt.docx supaya logo + identitas perusahaan ikut.
Bahasa sengaja dibuat awam: tanpa istilah teknis web.
"""
from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

TEMPLATE = "/Users/arbasya/Library/Mobile Documents/com~apple~CloudDocs/Perusahaan/kop-pt.docx"
OUT = "dokumen/SKPL-Landing-Page-XL-Home.docx"

BODY_FONT = "Times New Roman"
INK = RGBColor(0x1A, 0x1A, 0x1A)
MUTED = RGBColor(0x55, 0x55, 0x55)

doc = Document(TEMPLATE)

# ------------------------------------------------------------------ helpers
def set_font(run, size=11, bold=False, italic=False, color=INK):
    run.font.name = BODY_FONT
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    run._element.rPr.rFonts.set(qn("w:eastAsia"), BODY_FONT)


def para(text="", size=11, bold=False, italic=False, color=INK, align=None,
         space_before=0, space_after=6, line=1.25, indent=None):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing = line
    if indent:
        pf.left_indent = Cm(indent)
    if align:
        p.alignment = align
    if text:
        set_font(p.add_run(text), size, bold, italic, color)
    return p


def heading(text, size=13, space_before=16, space_after=6):
    p = para(text, size=size, bold=True, space_before=space_before, space_after=space_after)
    # never leave a heading stranded at the bottom of a page
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.keep_together = True
    return p


def bullets(items, size=11, indent=0.6):
    # template has no "List Bullet" style, so the bullet is a literal character
    for item in items:
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.left_indent = Cm(indent + 0.5)
        pf.first_line_indent = Cm(-0.5)
        pf.space_before = Pt(0)
        pf.space_after = Pt(3)
        pf.line_spacing = 1.2
        set_font(p.add_run("\u2022\u00a0\u00a0" + item), size)


def shade(cell, hex_color):
    el = OxmlElement("w:shd")
    el.set(qn("w:val"), "clear")
    el.set(qn("w:fill"), hex_color)
    cell._tc.get_or_add_tcPr().append(el)


def cell_text(cell, text, size=9.5, bold=False, color=INK, align=None):
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.line_spacing = 1.1
    if align:
        p.alignment = align
    set_font(p.add_run(text), size, bold, color=color)


def table(headers, rows, widths, header_fill="E8EDF5", size=9.5):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    for i, h in enumerate(headers):
        c = t.rows[0].cells[i]
        cell_text(c, h, size=size, bold=True)
        shade(c, header_fill)
    for row in rows:
        cells = t.add_row().cells
        for i, val in enumerate(row):
            cell_text(cells[i], val, size=size)
    for r in t.rows:
        for i, w in enumerate(widths):
            r.cells[i].width = Cm(w)
    # repeat header row on page breaks
    tr_pr = t.rows[0]._tr.get_or_add_trPr()
    el = OxmlElement("w:tblHeader")
    el.set(qn("w:val"), "true")
    tr_pr.append(el)
    para("", size=6, space_after=0)
    return t


def subheading(text):
    p = para(text, size=10.5, bold=True, space_before=6, space_after=4)
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.keep_together = True
    return p


def info_box(lines, fill="F4F7FC"):
    t = doc.add_table(rows=1, cols=1)
    t.style = "Table Grid"
    c = t.rows[0].cells[0]
    c.width = Cm(15.9)
    shade(c, fill)
    c.text = ""
    first = True
    for line, bold in lines:
        p = c.paragraphs[0] if first else c.add_paragraph()
        first = False
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.2
        set_font(p.add_run(line), 10, bold)
    para("", size=6, space_after=0)


def page_number_footer():
    footer = doc.sections[0].footer
    p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    set_font(p.add_run("Halaman "), 9, color=MUTED)
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), "18")
    rpr.append(sz)
    run.append(rpr)
    fld.append(run)
    p._p.append(fld)
    set_font(p.add_run(" dari "), 9, color=MUTED)
    fld2 = OxmlElement("w:fldSimple")
    fld2.set(qn("w:instr"), "NUMPAGES")
    run2 = OxmlElement("w:r")
    rpr2 = OxmlElement("w:rPr")
    sz2 = OxmlElement("w:sz")
    sz2.set(qn("w:val"), "18")
    rpr2.append(sz2)
    run2.append(rpr2)
    fld2.append(run2)
    p._p.append(fld2)


# ------------------------------------------------------------------ isi dokumen
doc.paragraphs[0].text = ""

para("SURAT PERMINTAAN KELENGKAPAN WEBSITE", size=14, bold=True,
     align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
para("(SKPL — Spesifikasi Kebutuhan Pengguna)", size=10, italic=True,
     align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
para("Landing Page XL Home — Pasang WiFi Rumah", size=12, bold=True,
     align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)

# --- data surat
table(
    ["Nomor Surat", "Tanggal", "Perihal", "Ditujukan kepada"],
    [["ATN/SKPL/XI-2026/01", "………………… 2026",
      "Permintaan data, gambar, dan informasi layanan",
      "Pengelola layanan XL Home"]],
    widths=[4.0, 3.6, 5.3, 3.0],
)

heading("1. Apa Isi Dokumen Ini?", space_before=6)
para(
    "Dokumen ini adalah daftar permintaan kepada Bapak/Ibu. Website contoh untuk layanan "
    "XL Home sudah selesai dibuat dan bisa dibuka di internet. Namun isi website tersebut "
    "saat ini masih memakai data contoh: foto pinjaman, nomor telepon contoh, dan harga "
    "perkiraan. Supaya website benar-benar mewakili layanan Bapak/Ibu, kami perlu data dan "
    "gambar yang asli dari Bapak/Ibu."
)
para(
    "Cara mengisinya sederhana: cukup ketik langsung di kotak-kotak yang sudah kami "
    "sediakan di bawah ini, lalu kirim kembali file dokumen ini. Tidak perlu mengerti "
    "istilah komputer. Bagian yang tidak dipakai boleh dibiarkan kosong atau ditulis "
    "“belum ada”."
)

info_box([
    ("Alamat website contoh (silakan dibuka dulu):", True),
    ("https://developer-plenger.github.io/xl-landing/", False),
    ("Semua yang perlu diganti adalah bagian yang di dokumen ini ditandai dengan kata "
     "“data contoh”.", False),
    ("Biaya pembuatan website: Rp 2.980.000 (sudah termasuk domain 1 tahun, hosting "
     "3 bulan, pendaftaran ke Google, dan garansi 3 bulan). Rinciannya ada di bagian 9.", True),
])

heading("2. Batas Waktu dan Alur")
table(
    ["Langkah", "Kegiatan", "Perkiraan waktu"],
    [
        ["1", "Bapak/Ibu melengkapi dokumen ini dan mengirimkannya kembali", "3 hari kerja"],
        ["2", "Kami memasang data dan gambar ke website, lalu mengirim tautan untuk dicek", "2 hari kerja"],
        ["3", "Bapak/Ibu memeriksa hasilnya dan memberi koreksi bila ada yang salah", "2 hari kerja"],
        ["4", "Website dinyatakan selesai dan siap dipakai", "1 hari kerja"],
    ],
    widths=[1.8, 10.6, 3.5],
)
para(
    "Nomor urut di atas bisa berubah sesuai kecepatan balasan dari kedua pihak.",
    size=9.5, italic=True, color=MUTED,
)

heading("3. Data Kontak Penjualan (Sales)")
para(
    "Data ini muncul di bagian bawah halaman dan di setiap tombol WhatsApp. "
    "Saat ini masih memakai data contoh.", space_after=8,
)
table(
    ["No", "Yang dibutuhkan", "Data contoh di website", "Data yang benar (diisi Bapak/Ibu)"],
    [
        ["1", "Nama lengkap sales", "Andrian", ""],
        ["2", "Jabatan / keterangan", "Direct Sales XL Satu", ""],
        ["3", "Nomor WhatsApp yang dipakai", "0813 8824 4662", ""],
        ["4", "Nomor telepon lain (bila ada)", "—", ""],
        ["5", "Alamat e-mail", "atn@teknostudio.id", ""],
        ["6", "Jam operasional (misal 08.00–20.00)", "—", ""],
        ["7", "Alamat kantor / basecamp (bila ada)", "—", ""],
    ],
    widths=[1.0, 5.4, 4.5, 5.0],
)

heading("4. Wilayah Layanan")
para(
    "Dipakai pada bagian “Area layanan kami” dan pada kalimat pembuka website. "
    "Silakan centang atau tulis ulang.", space_after=8,
)
table(
    ["Wilayah", "Dilayani? (Ya / Tidak)", "Catatan (kecamatan tertentu, dll.)"],
    [
        ["Jakarta Selatan", "Ya", ""],
        ["Jakarta (wilayah lain)", "Ya", ""],
        ["Bogor", "Ya", ""],
        ["Depok", "Ya", ""],
        ["Tangerang", "Ya", ""],
        ["Bekasi", "Ya", ""],
        ["Lainnya: …………………", "", ""],
    ],
    widths=[5.5, 4.5, 5.9],
)

heading("5. Gambar yang Dibutuhkan")
para(
    "Ini bagian yang paling menentukan tampilan website. Saat ini website memakai foto "
    "contoh dari internet, sehingga wajah dan rumah di dalamnya bukan pelanggan "
    "Bapak/Ibu. Kami perlu foto asli agar website terasa benar.", space_after=6,
)
subheading("Ketentuan foto (mohon diperhatikan):")
bullets([
    "Format file: JPG atau PNG (bukan tangkapan layar WhatsApp bila bisa dihindari).",
    "Ukuran minimal 1200 piksel pada sisi terlebar. Semakin besar semakin bagus.",
    "Foto harus milik sendiri atau sudah diizinkan pemiliknya. Jangan ambil dari Google.",
    "Bila foto memuat wajah orang, mohon pastikan orang tersebut setuju fotonya dipakai.",
    "Bila belum ada foto, tulis “belum ada” — kami akan bantu carikan gambar pengganti "
    "yang berlisensi aman.",
], size=10.5)

para("", size=4, space_after=4)
table(
    ["No", "Gambar untuk apa", "Tampil di bagian mana", "Status sekarang", "Sudah ada? (Ya / Belum)"],
    [
        ["1", "Logo perusahaan / XL Home", "Paling atas dan paling bawah halaman",
         "Logo XL Home (contoh)", ""],
        ["2", "Foto keluarga menggunakan internet di rumah",
         "Gambar besar di bagian paling atas", "Foto contoh dari internet", ""],
        ["3", "Foto keluarga / aktivitas di rumah",
         "Bagian “Internet rumah untuk hal-hal yang penting”", "Foto contoh dari internet", ""],
        ["4", "Foto teknisi sedang memasang internet",
         "Bagian “Cara memasang WiFi rumah XL Home”", "Foto contoh dari internet", ""],
        ["5", "Ikon kecil di tab browser (favicon)", "Tab browser, ukuran sangat kecil",
         "Ikon contoh", ""],
        ["6", "Foto tambahan (bila ada)", "Silakan sebutkan", "—", ""],
    ],
    widths=[1.0, 4.6, 4.4, 3.2, 2.7],
)

para(
    "Cara mengirim gambar: kumpulkan dalam satu folder (misalnya diberi nama "
    "“Gambar Website XL Home”), lalu kirim lewat WhatsApp dalam bentuk dokumen/arsip, "
    "atau lewat Google Drive. Mohon jangan dikirim satu per satu di chat agar tidak "
    "tercampur dengan percakapan lain.", size=10, italic=True, color=MUTED,
)

heading("6. Detail Paket yang Dijual")
para(
    "Bagian ini adalah daftar harga di website. Saat ini angkanya masih perkiraan, jadi "
    "mohon diperiksa dan diperbaiki. Bila ada paket yang tidak dijual, tulis "
    "“tidak dijual” pada kolom keterangan.", space_after=8,
)

subheading("A. Paket kabel fiber optik (FTTH)")
table(
    ["No", "Nama paket", "Kecepatan", "Harga per bulan", "Keterangan / status"],
    [
        ["1", "XL Home Smooth", "100 Mbps", "Rp 243.090", ""],
        ["2", "XL Home Value", "250 Mbps", "Rp 254.190", ""],
        ["3", "XL Home Smart", "300 Mbps", "Rp 265.290", "ditandai “Paling Dicari”"],
        ["4", "XL Home Family", "350 Mbps", "Rp 309.690", ""],
        ["5", "XL Home Super", "400 Mbps", "Rp 331.890", ""],
        ["6", "XL Home Ultimate", "600 Mbps", "Rp 555.000", ""],
        ["7", "", "", "", ""],
        ["8", "", "", "", ""],
    ],
    widths=[1.0, 4.4, 3.0, 3.6, 3.9],
)
para(
    "Baris 7 dan 8 disediakan bila ada paket tambahan.",
    size=9, italic=True, color=MUTED,
)

subheading("B. Paket tanpa kabel (FWA)")
table(
    ["No", "Nama paket", "Kecepatan", "Harga", "Keterangan / status"],
    [
        ["1", "XL HOME FWA 100 Mbps", "100 Mbps", "Rp 243.090 /bulan", "ditandai “Paling Dicari”"],
        ["2", "XL HOME FWA 50 Mbps", "50 Mbps", "Rp 721.500 /3 bulan, gratis 1 bulan", ""],
        ["3", "XL HOME FWA 100 Mbps Promo", "100 Mbps", "Rp 876.900 /3 bulan, gratis 1 bulan", ""],
        ["4", "", "", "", ""],
    ],
    widths=[1.0, 4.4, 3.0, 4.2, 3.3],
)

subheading("C. Fasilitas yang ditulis di setiap paket")
para(
    "Website saat ini menulis daftar fasilitas berikut. Mohon dicoret yang tidak benar "
    "atau ditambah yang kurang.", space_after=6,
)
table(
    ["No", "Tulisan di website", "Benar? (Ya / Tidak)"],
    [
        ["1", "Bebas biaya instalasi", ""],
        ["2", "Bebas PPN 11%", ""],
        ["3", "Unlimited tanpa FUP (untuk paket FTTH)", ""],
        ["4", "Kuota Internet 1 TB/bulan (untuk paket FWA)", ""],
        ["5", "Koneksi stabil", ""],
        ["6", "Harga flat per bulan", ""],
        ["7", "Jaringan support 5G", ""],
        ["8", "Gratis 1 ml parfum Mykonos (dari sales pribadi)", ""],
        ["9", "Tambahan lain: ………………………………", ""],
    ],
    widths=[1.0, 10.4, 4.5],
)
para(
    "Catatan penting: harga dan fasilitas yang ditampilkan di website harus sesuai "
    "ketentuan resmi XL Home. Kami tidak dapat mengubah angka tanpa persetujuan "
    "Bapak/Ibu, dan Bapak/Ibu bertanggung jawab atas kebenaran angkanya.",
    size=10, italic=True, color=MUTED,
)

heading("7. Teks dan Pertanyaan yang Sering Diajukan")
para(
    "Website punya bagian tanya-jawab. Saat ini isinya karangan kami sebagai contoh. "
    "Silakan ganti dengan jawaban yang benar, atau tambahkan pertanyaan yang sering "
    "Bapak/Ibu terima dari calon pembeli.", space_after=8,
)
table(
    ["No", "Pertanyaan", "Jawaban yang benar (diisi Bapak/Ibu)"],
    [
        ["1", "Apakah layanan tersedia di Jakarta Selatan?",
         "Ya. Kami melayani pemasangan untuk rumah dan tempat usaha di Jakarta Selatan "
         "serta wilayah Jabodetabek lainnya. Ketersediaan jaringan per alamat tetap perlu "
         "dikonfirmasi terlebih dahulu."],
        ["2", "Wilayah mana saja yang dilayani?",
         "Jakarta, Bogor, Depok, Tangerang, dan Bekasi (Jabodetabek)."],
        ["3", "Apa perbedaan paket FTTH dan FWA?",
         "FTTH memakai kabel fiber optik langsung ke rumah, FWA memakai jaringan "
         "nirkabel tanpa menarik kabel ke tiang."],
        ["4", "Bagaimana cara mendaftar?", ""],
        ["5", "Apakah perlu pengecekan jaringan sebelum pemasangan?", ""],
        ["6", "Berapa lama proses pemasangan?", ""],
        ["7", "Pertanyaan lain: ………………………………", ""],
    ],
    widths=[1.0, 5.6, 9.3],
)

para(
    "Teks lain yang boleh Bapak/Ibu sesuaikan (bila perlu): kalimat pembuka di bagian "
    "paling atas, cerita singkat tentang usaha di bagian “Tentang Kami”, dan nama website "
    "yang muncul di tab browser.", size=10, italic=True, color=MUTED,
)

heading("8. Akun dan Akses (Kredensial)")
para(
    "Supaya website bisa dipakai dengan alamat sendiri dan bisa diperbarui nanti, kami "
    "perlu tahu siapa pemegang akun-akun berikut. Mohon diisi nama pemegang akunnya saja "
    "— jangan tulis kata sandi di dokumen ini.", space_after=8,
)
table(
    ["No", "Keperluan", "Status sekarang", "Pemegang akun / keterangan"],
    [
        ["1", "Nama alamat website (domain), misal pasangwifixlhome.com",
         "Belum ada", ""],
        ["2", "Tempat menyimpan website (hosting)", "Memakai layanan gratis", ""],
        ["3", "E-mail resmi untuk dihubungi", "Belum ada", ""],
        ["4", "Akun Instagram", "Tautan contoh", ""],
        ["5", "Akun Facebook", "Tautan contoh", ""],
        ["6", "Akun TikTok", "Tautan contoh", ""],
        ["7", "Akun Google (untuk pendataan di mesin pencari)", "Belum ada", ""],
    ],
    widths=[1.0, 6.6, 3.4, 4.9],
)

info_box([
    ("Penting soal kata sandi:", True),
    ("Jangan pernah mengirim kata sandi lewat WhatsApp, e-mail, atau dokumen seperti ini.", False),
    ("Bila kami perlu masuk ke sebuah akun, kami akan meminta akses lewat cara yang aman "
     "(misalnya menambahkan kami sebagai pengelola di akun tersebut). Setelah pekerjaan "
     "selesai, silakan ganti kata sandi semua akun yang sempat kami akses.", False),
])

heading("9. Rincian Biaya")
para(
    "Berikut biaya pembuatan website ini. Harga sudah termasuk pekerjaan pemasangan data, "
    "gambar, dan penyesuaian halaman sampai bentuknya sesuai contoh yang Bapak/Ibu lihat.",
    space_after=8,
)
table(
    ["No", "Uraian", "Biaya"],
    [
        ["1", "Pembuatan website (halaman sesuai referensi, termasuk pendaftaran website "
              "ke Google / SEO, dan gratis hosting 3 bulan)", "Rp 2.700.000"],
        ["2", "Nama alamat website (domain), 1 tahun", "Rp 280.000"],
        ["3", "Jumlah yang perlu dibayar", "Rp 2.980.000"],
    ],
    widths=[1.0, 11.9, 3.0],
)
para(
    "Baris nomor 3 adalah total yang perlu dibayar, bukan tambahan dari baris 1 dan 2.",
    size=9.5, italic=True, color=MUTED,
)

subheading("A. Sudah termasuk dalam biaya di atas")
bullets([
    "Pembuatan halaman sesuai contoh (halaman yang sama, diisi data dan gambar asli "
    "dari Bapak/Ibu).",
    "Pendaftaran website ke Google dan penyiapan dasar-dasar SEO, supaya website bisa "
    "ditemukan saat orang mencari di Google.",
    "Gratis biaya penyimpanan website (hosting) selama 3 bulan pertama.",
    "Garansi 3 bulan: bila ada bagian yang tidak sesuai contoh atau tidak sesuai data "
    "yang Bapak/Ibu kirim, kami perbaiki tanpa biaya tambahan.",
    "Pemasangan data paket, nomor WhatsApp, dan gambar yang Bapak/Ibu kirimkan.",
], size=10.5)

subheading("B. Belum termasuk (dihitung terpisah bila dibutuhkan)")
bullets([
    "Perpanjangan nama alamat website (domain) setelah 1 tahun, dan perpanjangan "
    "penyimpanan website (hosting) setelah 3 bulan.",
    "Penambahan halaman atau bagian baru di luar contoh yang sudah disepakati.",
    "Penambahan fitur di luar halaman informasi, misalnya pesan dari formulir "
    "tersimpan otomatis, pembayaran online, atau halaman khusus anggota.",
    "Biaya iklan di Google atau media sosial.",
    "Pengurusan izin, materi promosi cetak, dan biaya di luar pembuatan website.",
], size=10.5)

subheading("C. Penjelasan singkat istilah")
table(
    ["Istilah", "Artinya"],
    [
        ["Domain", "Nama alamat website yang diketik orang di browser, misalnya "
                   "pasangwifixlhome.com. Disewa per tahun."],
        ["Hosting", "Tempat menyimpan file website supaya bisa dibuka kapan saja. "
                    "Disewa per bulan/tahun."],
        ["SEO", "Cara mengatur isi website supaya lebih mudah muncul di hasil pencarian "
                "Google ketika orang mencari \u201cpasang wifi XL Home\u201d."],
        ["Garansi", "Masa di mana kami memperbaiki kesalahan atau ketidaksesuaian tanpa "
                    "biaya tambahan."],
    ],
    widths=[3.2, 12.7],
)

subheading("D. Cara pembayaran")
para(
    "Pembayaran dapat dilakukan dalam dua tahap. Tahap pertama saat pekerjaan dimulai, "
    "tahap kedua setelah website selesai dan Bapak/Ibu menyatakan puas.", space_after=6,
)
table(
    ["Tahap", "Waktu", "Jumlah"],
    [
        ["Uang muka", "Saat data dan gambar mulai kami pasang", "Rp …………………"],
        ["Pelunasan", "Setelah website selesai dan disetujui", "Rp …………………"],
    ],
    widths=[3.2, 8.7, 4.0],
)
para(
    "Nominal uang muka dan pelunasan kami kosongkan agar bisa disepakati bersama. "
    "Bila Bapak/Ibu ingin dibayar sekaligus di akhir, hal itu juga bisa didiskusikan.",
    size=9.5, italic=True, color=MUTED,
)

heading("10. Hal yang Perlu Diketahui Sebelum Website Dipakai")
bullets([
    "Website ini adalah halaman informasi dan pemasaran, bukan situs resmi perusahaan XL. "
    "Penggunaan logo dan nama XL Home harus sesuai izin yang berlaku.",
    "Website tidak memproses pembayaran. Pendaftaran dan pembayaran tetap dilakukan di "
    "luar website, sesuai ketentuan layanan.",
    "Formulir di website saat ini meneruskan pesan ke WhatsApp. Bila nanti ingin pesan "
    "masuk tersimpan otomatis, itu pekerjaan tambahan dan perlu dibicarakan terpisah.",
    "Semua data yang Bapak/Ibu kirim hanya dipakai untuk keperluan pembuatan website ini.",
], size=10.5)

heading("11. Pengesahan")
para(
    "Dengan mengisi dan mengirimkan kembali dokumen ini, kedua pihak sepakat bahwa data "
    "di dalamnya menjadi dasar pembuatan website, dan menyetujui biaya sebesar "
    "Rp 2.980.000 dengan ketentuan yang tertulis di bagian 9.", space_after=14,
)

t = doc.add_table(rows=1, cols=2)
t.autofit = False
left, right = t.rows[0].cells
left.width = Cm(8.0)
right.width = Cm(8.0)
for cell, title in ((left, "Pihak Pemesan"), (right, "Pihak Pembuat")):
    cell.text = ""
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_font(p.add_run(title), 10.5, bold=True)
    for line in ("", "", ""):
        q = cell.add_paragraph()
        q.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_font(q.add_run(line or " "), 10.5)
    p2 = cell.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_font(p2.add_run("(……………………………………….)"), 10.5)
    p3 = cell.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_font(p3.add_run("Nama & tanggal"), 9.5, color=MUTED)

page_number_footer()

# ------------------------------------------------------------------ simpan
import os

os.makedirs("dokumen", exist_ok=True)
doc.save(OUT)
print("saved", OUT, os.path.getsize(OUT), "bytes")

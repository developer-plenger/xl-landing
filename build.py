"""Render index.html from the site data in build.py — one source, static output."""
import html as H

WA = "6281388244662"
WA_DISPLAY = "0813 8824 4662"
PERSON = "Andrian"
ROLE = "Direct Sales XL Satu"
AREA = "Jakarta Selatan"
AREAS = ["Jakarta", "Bogor", "Depok", "Tangerang", "Bekasi"]

HERO_MSG = (
    "Halo, saya ingin konsultasi pasang WiFi XL Home di rumah/tempat usaha saya "
    "dan mengecek ketersediaan jaringan di alamat saya (Jakarta Selatan / Jabodetabek)."
)


def wa(msg=HERO_MSG):
    from urllib.parse import quote

    return f"https://wa.me/{WA}?text={quote(msg, safe='')}"


NAV = [
    ("Beranda", "/#beranda"),
    ("Paket FTTH", "/#paket-ftth"),
    ("Paket FWA", "/#paket-fwa"),
    ("Keunggulan", "/#keunggulan"),
    ("FAQ", "/#faq"),
    ("Tentang Kami", "/#tentang"),
    ("Kontak", "/#kontak-form"),
]

FTTH_BENEFITS = [
    "Bebas biaya instalasi.",
    "Bebas PPN 11%.",
    "Unlimited tanpa FUP.",
    "Koneksi stabil.",
    "Harga flat per bulan.",
    "Jaringan support 5G.",
    "Gratis 1 ml parfum Mykonos (dari sales pribadi).",
]

FWA_BENEFITS = [
    "Bebas biaya instalasi.",
    "Bebas PPN 11%.",
    "Kuota Internet 1 TB/bulan.",
    "Koneksi stabil.",
    "Harga flat per bulan.",
    "Jaringan support 5G.",
    "Nirkabel — internet rumah tanpa tarik kabel ke tiang listrik.",
    "Gratis 1 ml parfum Mykonos (dari sales pribadi).",
]

FTTH_DESC = "Paket internet rumah XL HOME FTTH"

FTTH = [
    ("XL Home Smooth", FTTH_DESC, "243.090", "/bulan", "100", False, FTTH_BENEFITS),
    ("XL Home Value", FTTH_DESC, "254.190", "/bulan", "250", False, FTTH_BENEFITS),
    ("XL Home Smart", FTTH_DESC, "265.290", "/bulan", "300", True, FTTH_BENEFITS),
    ("XL Home Family", FTTH_DESC, "309.690", "/bulan", "350", False, FTTH_BENEFITS),
    ("XL Home Super", FTTH_DESC, "331.890", "/bulan", "400", False, FTTH_BENEFITS),
    ("XL Home Ultimate", FTTH_DESC, "555.000", "/bulan", "600", False, FTTH_BENEFITS),
]

FWA = [
    ("XL HOME FWA 100 Mbps", "Internet tanpa kabel fiber ke rumah", "243.090", "/bulan", "100", True, FWA_BENEFITS),
    ("XL HOME FWA 50 Mbps", "Paket 3 bulan, gratis 1 bulan, tanpa kabel", "721.500", "/3 bulan, gratis 1 bulan", "50", False, FWA_BENEFITS),
    ("XL HOME FWA 100 Mbps Promo", "Paket 3 bulan, gratis 1 bulan, tanpa kabel", "876.900", "/3 bulan, gratis 1 bulan", "100", False, FWA_BENEFITS),
]

ADVANTAGES = [
    ("laptop", "01", "Aktivitas sehari-hari", "Mendukung streaming, belajar, bekerja, dan browsing dari rumah atau tempat usaha Anda."),
    ("sliders-horizontal", "02", "Sesuai kebutuhan", "Pelajari detail paket dan diskusikan kebutuhan penggunaan internet dengan admin kami."),
    ("message-circle", "03", "Konsultasi via WhatsApp", "Informasi dan proses pendaftaran dapat dibicarakan langsung melalui WhatsApp."),
    ("map-pin", "04", "Cek jaringan dulu", "Konfirmasikan ketersediaan jaringan di alamat Anda sebelum berlangganan."),
]

STEPS = [
    ("clipboard-list", "Pilih paket WiFi", "Bandingkan paket XL HOME FTTH atau FWA sesuai kecepatan dan kebutuhan rumah atau tempat usaha."),
    ("message-circle", "Hubungi admin", "Klik tombol paket untuk memulai percakapan WhatsApp dengan detail paket yang dipilih."),
    ("map-pin", "Cek ketersediaan jaringan", "Sampaikan alamat rumah atau tempat usaha agar ketersediaan jaringan dapat dikonfirmasi."),
    ("wrench", "Lanjutkan pendaftaran", "Ikuti proses pendaftaran sesuai ketentuan layanan. Pembayaran dilakukan di luar website."),
]

FAQ = [
    (
        "Apakah layanan pasang WiFi XL Home tersedia di Jakarta Selatan?",
        "Ya. Kami melayani pemasangan WiFi XL Home untuk rumah dan tempat usaha di Jakarta Selatan serta wilayah Jabodetabek lainnya. Ketersediaan jaringan per alamat tetap perlu dikonfirmasi terlebih dahulu melalui WhatsApp atau formulir kontak.",
    ),
    (
        "Wilayah mana saja yang dilayani?",
        "Layanan kami mencakup Jakarta, Bogor, Depok, Tangerang, dan Bekasi (Jabodetabek). Silakan sampaikan alamat Anda kepada admin agar ketersediaan jaringan dapat dicek sebelum pendaftaran.",
    ),
    (
        "Apa perbedaan paket XL Home FTTH dan FWA?",
        "FTTH menggunakan kabel fiber optik langsung ke rumah, sementara FWA menghubungkan rumah Anda ke internet melalui jaringan nirkabel tanpa menarik kabel ke tiang. FWA cocok untuk lokasi yang belum terjangkau jaringan fiber optik.",
    ),
    (
        "Bagaimana cara mendaftar pasang WiFi XL Home?",
        "Pilih paket yang sesuai, lalu hubungi admin melalui WhatsApp atau isi formulir kontak di halaman ini. Sampaikan alamat pemasangan agar ketersediaan jaringan dapat dikonfirmasi sebelum melanjutkan pendaftaran.",
    ),
    (
        "Apakah perlu pengecekan jaringan sebelum pemasangan?",
        "Ya. Ketersediaan jaringan FTTH dan FWA berbeda di setiap alamat. Pengecekan dilakukan agar pemasangan dapat berjalan sesuai kondisi jaringan di lokasi Anda.",
    ),
    (
        "Berapa lama proses pemasangan WiFi?",
        "Waktu pemasangan bergantung pada ketersediaan jaringan dan jadwal teknisi di lokasi Anda. Detail perkiraan waktu akan disampaikan admin setelah pengecekan alamat.",
    ),
]

SERVICE_LIST = [
    "Pasang WiFi rumah XL Home untuk rumah dan tempat usaha.",
    "Informasi harga dan pilihan paket internet rumah XL Home.",
    "Layanan internet FTTH Fiber Optik dan FWA tanpa kabel.",
    "Konsultasi pemilihan paket sesuai kebutuhan internet.",
    "Pengecekan ketersediaan jaringan di lokasi pelanggan.",
    "Bantuan pendaftaran pemasangan WiFi.",
]

FWA_POINTS = [
    "Tidak memerlukan penarikan kabel fiber optik sampai ke rumah.",
    "Menggunakan jaringan nirkabel untuk akses internet.",
    "Instalasi lebih praktis, sesuai ketentuan layanan.",
    "Cocok untuk rumah atau lokasi yang belum terjangkau jaringan kabel.",
    "Mendukung aktivitas internet harian seperti browsing, belajar, dan streaming.",
]

# ---------------------------------------------------------------- icons
# Geometry copied from the live site's lucide icons so the preview matches.
ICON_SHAPES = {
    "arrow-up-right": [("path", {"d": "M7 7h10v10"}), ("path", {"d": "M7 17 17 7"})],
    "arrow-down": [("path", {"d": "M12 5v14"}), ("path", {"d": "m19 12-7 7-7-7"})],
    "cable": [
        ("path", {"d": "M17 21v-2a1 1 0 0 1-1-1v-1a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v1a1 1 0 0 1-1 1"}),
        ("path", {"d": "M19 15V6.5a1 1 0 0 0-7 0v11a1 1 0 0 1-7 0V9"}),
        ("path", {"d": "M21 21v-2h-4"}),
        ("path", {"d": "M3 5h4V3"}),
        ("path", {"d": "M7 5a1 1 0 0 1 1 1v1a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a1 1 0 0 1 1-1V3"}),
    ],
    "check": [("path", {"d": "M20 6 9 17l-5-5"})],
    "chevron-down": [("path", {"d": "m6 9 6 6 6-6"})],
    "circle-check": [
        ("circle", {"cx": "12", "cy": "12", "r": "10"}),
        ("path", {"d": "m9 12 2 2 4-4"}),
    ],
    "clipboard-list": [
        ("rect", {"width": "8", "height": "4", "x": "8", "y": "2", "rx": "1", "ry": "1"}),
        ("path", {"d": "M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"}),
        ("path", {"d": "M12 11h4"}),
        ("path", {"d": "M12 16h4"}),
        ("path", {"d": "M8 11h.01"}),
        ("path", {"d": "M8 16h.01"}),
    ],
    "laptop": [
        ("path", {"d": "M20 16V7a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v9m16 0H4m16 0 1.28 2.55a1 1 0 0 1-.9 1.45H3.62a1 1 0 0 1-.9-1.45L4 16"})
    ],
    "map-pin": [
        ("path", {"d": "M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"}),
        ("circle", {"cx": "12", "cy": "10", "r": "3"}),
    ],
    "message-circle": [("path", {"d": "M7.9 20A9 9 0 1 0 4 16.1L2 22Z"})],
    "monitor-smartphone": [
        ("path", {"d": "M18 8V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h8"}),
        ("path", {"d": "M10 19v-3.96 3.15"}),
        ("path", {"d": "M7 19h5"}),
        ("rect", {"width": "6", "height": "10", "x": "16", "y": "12", "rx": "2"}),
    ],
    "send": [
        ("path", {"d": "M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"}),
        ("path", {"d": "m21.854 2.147-10.94 10.939"}),
    ],
    "signal": [
        ("path", {"d": "M2 20h.01"}),
        ("path", {"d": "M7 20v-4"}),
        ("path", {"d": "M12 20v-8"}),
        ("path", {"d": "M17 20V8"}),
        ("path", {"d": "M22 4v16"}),
    ],
    "sliders-horizontal": [
        ("line", {"x1": "21", "x2": "14", "y1": "4", "y2": "4"}),
        ("line", {"x1": "10", "x2": "3", "y1": "4", "y2": "4"}),
        ("line", {"x1": "21", "x2": "12", "y1": "12", "y2": "12"}),
        ("line", {"x1": "8", "x2": "3", "y1": "12", "y2": "12"}),
        ("line", {"x1": "21", "x2": "16", "y1": "20", "y2": "20"}),
        ("line", {"x1": "12", "x2": "3", "y1": "20", "y2": "20"}),
        ("line", {"x1": "14", "x2": "14", "y1": "2", "y2": "6"}),
        ("line", {"x1": "8", "x2": "8", "y1": "10", "y2": "14"}),
        ("line", {"x1": "16", "x2": "16", "y1": "18", "y2": "22"}),
    ],
    "star": [
        ("path", {"d": "M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"})
    ],
    "wifi": [
        ("path", {"d": "M12 20h.01"}),
        ("path", {"d": "M2 8.82a15 15 0 0 1 20 0"}),
        ("path", {"d": "M5 12.859a10 10 0 0 1 14 0"}),
        ("path", {"d": "M8.5 16.429a5 5 0 0 1 7 0"}),
    ],
    "wrench": [
        ("path", {"d": "M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"})
    ],
    "zap": [
        ("path", {"d": "M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"})
    ],
    "menu": [
        ("line", {"x1": "4", "x2": "20", "y1": "12", "y2": "12"}),
        ("line", {"x1": "4", "x2": "20", "y1": "6", "y2": "6"}),
        ("line", {"x1": "4", "x2": "20", "y1": "18", "y2": "18"}),
    ],
    "x": [("path", {"d": "M18 6 6 18"}), ("path", {"d": "m6 6 12 12"})],
    "instagram": [
        ("rect", {"width": "20", "height": "20", "x": "2", "y": "2", "rx": "5", "ry": "5"}),
        ("path", {"d": "M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"}),
        ("line", {"x1": "17.5", "x2": "17.51", "y1": "6.5", "y2": "6.5"}),
    ],
    "facebook": [
        ("path", {"d": "M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"})
    ],
    "music2": [
        ("circle", {"cx": "8", "cy": "18", "r": "4"}),
        ("path", {"d": "M12 18V2l7 4"}),
    ],
}


def icon(name, size=24, cls="", extra=""):
    shapes = ICON_SHAPES[name]
    parts = []
    for tag, attrs in shapes:
        a = " ".join(f'{k}="{v}"' for k, v in attrs.items())
        parts.append(f"<{tag} {a}/>")
    klass = f"lucide lucide-{name}" + (f" {cls}" if cls else "")
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
        f'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        f'stroke-linecap="round" stroke-linejoin="round" class="{klass}"{extra}>'
        + "".join(parts)
        + "</svg>"
    )


e = H.escape


def package_card(pkg, kind):
    name, desc, price, period, speed, popular, benefits = pkg
    msg = (
        f"Halo, saya tertarik berlangganan paket {name}, kecepatan {speed} Mbps, "
        f"harga Rp{price} {period}. Mohon informasi lebih lanjut mengenai pendaftaran "
        f"dan ketersediaan jaringan."
    )
    # matches the live cards: FTTH uses the cable glyph, FWA the wifi glyph
    if kind == "ftth":
        cat_icon = icon("cable", 15)
        tag = "FTTH Fiber Optik"
    else:
        cat_icon = icon("wifi", 15)
        tag = "FWA Tanpa Kabel"
    badge = (
        f'\n<span class="popular-badge">{icon("star", 13)} Paling Dicari</span>' if popular else ""
    )
    items = "\n".join(
        f"<div>{icon('check', 17)}<span>{e(b)}</span></div>" for b in benefits
    )
    return f"""<article class="package-card size-standard{' is-popular' if popular else ''}">
  <div class="package-card-top">
    <span class="cat-tag">{cat_icon}{tag}</span>{badge}
  </div>
  <h3>{e(name)}</h3>
  <p class="package-description">{e(desc)}</p>
  <div class="price-block">
    <div class="price"><span class="currency">Rp</span><strong>{price}</strong><span class="period">{e(period)}</span></div>
    <div class="speed-badge">{icon('zap', 18)}<span class="speed-value">{speed}</span><span class="speed-unit">Mbps</span></div>
  </div>
  <div class="benefits">
{items}
  </div>
  <a class="button subscribe-btn" href="{wa(msg)}" target="_blank" rel="noopener noreferrer">
    {icon('message-circle', 19)} Pilih Paket Berlangganan {icon('arrow-up-right', 18)}
  </a>
  <p class="package-note">Konsultasi &amp; pendaftaran melalui WhatsApp</p>
</article>"""


def render():
    nav_links = "\n".join(f'<a href="{href}">{e(label)}</a>' for label, href in NAV)
    footer_links = "\n".join(
        f'<a href="{href}">{e(label)}</a>' for label, href in NAV if label != "Tentang Kami"
    )
    ftth_cards = "\n".join(package_card(p, "ftth") for p in FTTH)
    fwa_cards = "\n".join(package_card(p, "fwa") for p in FWA)

    advantages = "\n".join(
        f"""<article>
  {icon(ic)}
  <span class="item-index">{idx}</span>
  <h3>{e(title)}</h3>
  <p>{e(text)}</p>
</article>"""
        for ic, idx, title, text in ADVANTAGES
    )

    steps = "\n".join(
        f"""<li>
  <span class="step-number">0{idx}</span>
  <div class="step-head">{icon(ic, 18)}<h3>{e(title)}</h3></div>
  <p>{e(text)}</p>
</li>"""
        for idx, (ic, title, text) in enumerate(STEPS, start=1)
    )

    faq = "\n".join(
        f"""<div class="faq-item{' is-open' if i == 0 else ''}">
  <button type="button" class="faq-question" aria-expanded="{'true' if i == 0 else 'false'}" data-answer="{e(a)}">
    <span>{e(q)}</span>{icon('chevron-down', 20, 'faq-chevron')}
  </button>
  {'<p class="faq-answer">' + e(a) + '</p>' if i == 0 else ''}
</div>"""
        for i, (q, a) in enumerate(FAQ)
    )

    areas = "\n".join(f"<li>{icon('check', 16)} {e(a)}</li>" for a in AREAS)
    services = "\n".join(f"<li>{e(s)}</li>" for s in SERVICE_LIST)
    fwa_points = "\n".join(f"<li>{e(p)}</li>" for p in FWA_POINTS)

    return f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Pasang WiFi Rumah XL Home Jakarta Selatan &amp; Jabodetabek</title>
<meta name="description" content="Pasang WiFi XL Home Jakarta Selatan &amp; Jabodetabek. Harga paket WiFi XL Home FTTH &amp; FWA, daftar WiFi XL Home via WhatsApp {WA_DISPLAY} atau formulir kontak."/>
<meta property="og:title" content="Pasang WiFi Rumah XL Home Jakarta Selatan &amp; Jabodetabek"/>
<meta property="og:description" content="Pasang WiFi XL Home Jakarta Selatan &amp; Jabodetabek. Harga paket WiFi XL Home FTTH &amp; FWA, daftar WiFi XL Home via WhatsApp {WA_DISPLAY} atau formulir kontak."/>
<meta property="og:type" content="website"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="Pasang WiFi Rumah XL Home Jakarta Selatan &amp; Jabodetabek"/>
<meta name="twitter:description" content="Pasang WiFi XL Home Jakarta Selatan &amp; Jabodetabek. Harga paket WiFi XL Home FTTH &amp; FWA, daftar WiFi XL Home via WhatsApp {WA_DISPLAY} atau formulir kontak."/>
<meta property="og:image" content="assets/img/hero-1280.png"/>
<meta name="twitter:image" content="assets/img/hero-1280.png"/>
<link rel="icon" href="assets/img/favicon.png" type="image/png"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous"/>
<link rel="preload" as="image" href="assets/img/hero-1280.png" imagesrcset="assets/img/hero-375.png 375w, assets/img/hero-768.png 768w, assets/img/hero-1024.png 1024w, assets/img/hero-1280.png 1280w" imagesizes="(min-width: 1000px) 63vw, 100vw"/>
<link rel="preload" as="image" href="assets/img/logo.jpg"/>
<link rel="stylesheet" href="assets/css/style.css"/>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lora:wght@400;500;600&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;display=swap"/>
</head>
<body>
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="/#beranda" aria-label="XL HOME Jakarta — Beranda">
      <span class="brand-logo"><img src="assets/img/logo.jpg" alt="XL HOME Jakarta" width="320" height="120"/></span>
    </a>
    <nav aria-label="Navigasi utama" class="desktop-nav">
{nav_links}
    </nav>
    <a class="button primary header-cta" href="/#paket-ftth">Daftar Sekarang {icon('arrow-up-right', 17)}</a>
    <button class="mobile-toggle" aria-label="Buka navigasi" aria-expanded="false">{icon('menu')}</button>
  </div>
  <nav class="mobile-nav" aria-label="Navigasi seluler" hidden>
{nav_links}
    <a class="button primary" href="/#paket-ftth">{icon('arrow-up-right', 18)} Daftar Sekarang</a>
  </nav>
</header>
<main>
  <section id="beranda" class="hero">
    <div class="hero-heading">
      <span class="eyebrow"><span class="status-dot"></span> PASANG WIFI RUMAH — JAKARTA SELATAN &amp; JABODETABEK</span>
      <h1>Internet Rumah XL Home,<br/><span>Cepat &amp; Stabil</span> untuk<br class="mobile-break"/> Keluarga Anda.</h1>
      <p>Pasang WiFi XL Home dengan pilihan paket FTTH dan FWA. Layanan tersedia untuk rumah dan tempat usaha di Jakarta Selatan serta wilayah Jabodetabek.</p>
      <div class="hero-actions">
        <a class="button primary" href="#paket-ftth">Lihat Paket WiFi {icon('arrow-up-right', 19)}</a>
        <a class="text-link" href="{wa()}" target="_blank" rel="noopener noreferrer">Konsultasi via WhatsApp {icon('arrow-up-right', 17)}</a>
      </div>
    </div>
    <div class="hero-media">
      <img src="assets/img/hero-1280.png" srcset="assets/img/hero-375.png 375w, assets/img/hero-768.png 768w, assets/img/hero-1024.png 1024w, assets/img/hero-1280.png 1280w" sizes="(min-width: 1000px) 63vw, 100vw" alt="Keluarga menggunakan internet rumah XL Home di ruang keluarga yang cerah di Jakarta Selatan" width="1344" height="768" fetchpriority="high"/>
      <div class="media-label">
        {icon('wifi', 20)}
        <span>Rumah terhubung.<br/><strong>Aktivitas lebih nyaman.</strong></span>
      </div>
      <div class="hero-spec">
        <div class="spec-top"><span>XL HOME FWA</span>{icon('signal', 21)}</div>
        <span class="spec-caption">Kecepatan hingga</span>
        <div class="speed">100<span>Mbps</span></div>
        <div class="spec-bottom"><span>Teknologi jaringan</span><strong>5G</strong></div>
        <a href="#paket-fwa">Kenali paketnya {icon('arrow-up-right', 18)}</a>
      </div>
    </div>
    <div class="hero-facts">
      <span>{icon('map-pin', 19)} Jakarta Selatan &amp; Jabodetabek</span>
      <span>{icon('signal', 19)} Jaringan 5G</span>
      <span>{icon('monitor-smartphone', 19)} Untuk rumah &amp; usaha</span>
      <a href="#paket-ftth">Temukan paket Anda {icon('arrow-down', 17)}</a>
    </div>
  </section>

  <section id="paket" class="section packages-section">
    <div id="paket-ftth" class="package-block">
      <div class="section-heading">
        <span class="eyebrow">01 / PAKET FTTH</span>
        <h2>Harga paket WiFi XL Home — berlangganan XL Home FTTH</h2>
        <p>Enam pilihan internet rumah XL Home FTTH, dari 100 Mbps hingga 600 Mbps. Harga paket WiFi XL Home yang ditampilkan adalah harga per bulan sesuai informasi paket.</p>
      </div>
      <div class="package-grid">
{ftth_cards}
      </div>
    </div>

    <div id="paket-fwa" class="package-block">
      <div class="section-heading">
        <span class="eyebrow">02 / PAKET FWA</span>
        <h2>WiFi XL Home tanpa kabel — paket XL Home FWA</h2>
        <p>WiFi XL Home tanpa kabel untuk rumah tanpa instalasi kabel fiber ke rumah. Tersedia paket bulanan 100 Mbps serta pilihan 3 bulan dengan gratis 1 bulan.</p>
      </div>
      <div class="package-grid">
{fwa_cards}
      </div>
      <div class="coverage-note">
        {icon('map-pin', 23)}
        <div>
          <strong>Cek jaringan di alamat Anda</strong>
          <p>Ketersediaan layanan FTTH dan FWA perlu dikonfirmasi sebelum berlangganan.</p>
          <a class="text-link" href="{wa()}" target="_blank" rel="noopener noreferrer">Tanyakan kepada admin {icon('arrow-up-right', 16)}</a>
        </div>
      </div>
      <p class="conditions">*Kecepatan dan jumlah perangkat yang didukung bergantung pada kondisi jaringan, lokasi, dan penggunaan. Konfirmasikan detail layanan kepada admin.</p>
    </div>
  </section>

  <section id="keunggulan" class="advantages-section">
    <div class="section inner">
      <div class="advantages-top">
        <div class="section-heading">
          <span class="eyebrow">02 / KEUNGGULAN</span>
          <h2>Internet rumah untuk hal-hal yang penting.</h2>
          <p>Kebutuhan keluarga dan tempat usaha Anda menjadi awal dari setiap konsultasi pemasangan WiFi.</p>
        </div>
        <div class="advantages-media">
          <img src="assets/img/advantages-1280.png" srcset="assets/img/advantages-375.png 375w, assets/img/advantages-768.png 768w, assets/img/advantages-1024.png 1024w, assets/img/advantages-1280.png 1280w" sizes="(min-width: 1000px) 40vw, 100vw" alt="Keluarga di Jakarta Selatan menikmati internet rumah XL Home bersama-sama" width="1216" height="912" loading="lazy"/>
        </div>
      </div>
      <div class="advantages-grid">
{advantages}
      </div>
      <div class="advantages-cta">
        <a class="button primary" href="{wa()}" target="_blank" rel="noopener noreferrer">{icon('message-circle', 20)} Konsultasi sekarang {icon('arrow-up-right', 18)}</a>
      </div>
    </div>
  </section>

  <section id="cara-berlangganan" class="section steps-section">
    <div class="steps-heading">
      <div>
        <span class="eyebrow">03 / PROSES PEMASANGAN</span>
        <h2>Cara memasang WiFi rumah XL Home.</h2>
      </div>
      <a class="text-link" href="{wa()}" target="_blank" rel="noopener noreferrer">Hubungi admin {icon('arrow-up-right', 18)}</a>
    </div>
    <div class="steps-layout">
      <div class="steps-media">
        <img src="assets/img/steps-1280.png" srcset="assets/img/steps-375.png 375w, assets/img/steps-768.png 768w, assets/img/steps-1024.png 1024w, assets/img/steps-1280.png 1280w" sizes="(min-width: 1000px) 40vw, 100vw" alt="Teknisi memasang WiFi router XL Home di rumah pelanggan di Jakarta Selatan" width="1216" height="912" loading="lazy"/>
      </div>
      <ol class="steps-list">
{steps}
      </ol>
    </div>
  </section>

  <section id="faq" class="section faq-section">
    <div class="section-heading">
      <span class="eyebrow">05 / PERTANYAAN UMUM</span>
      <h2>Pertanyaan yang sering diajukan</h2>
      <p>Hal-hal yang perlu Anda ketahui sebelum memasang WiFi XL Home di rumah atau tempat usaha.</p>
    </div>
    <div class="faq-list">
{faq}
    </div>
  </section>

  <section id="panduan" class="section seo-guide">
    <div class="section-heading">
      <span class="eyebrow">PANDUAN PASANG WIFI RUMAH</span>
      <h2>Pilih paket internet rumah yang sesuai</h2>
      <p>Ringkasan perbedaan Fiber to the Home (FTTH) dan Fixed Wireless Access (FWA) untuk membantu Anda memilih layanan pasang WiFi XL Home.</p>
    </div>
    <div class="seo-columns">
      <article>
        <h3>Apa itu XL Home FTTH — Internet Kabel Fiber Optik?</h3>
        <p>FTTH (Fiber to the Home) adalah layanan internet rumah berbasis kabel fiber optik yang ditarik langsung ke rumah. Pilihan ini cocok untuk Anda yang menginginkan koneksi internet rumah stabil dengan kecepatan tinggi di Jakarta Selatan dan wilayah Jabodetabek yang sudah terjangkau jaringan fiber.</p>
        <p>Paket FTTH pada halaman ini mencakup beberapa pilihan kecepatan. Detail nama paket, kecepatan, dan harga dapat dilihat pada kartu paket di atas dan dikelola melalui halaman admin.</p>
      </article>
      <article>
        <h3>WiFi XL Home tanpa kabel — apa itu XL Home FWA?</h3>
        <p>WiFi XL Home tanpa kabel adalah layanan FWA (Fixed Wireless Access) yang menghubungkan rumah Anda ke internet melalui jaringan nirkabel, tanpa perlu menarik kabel fiber optik ke tiang listrik. Solusi ini cocok untuk lokasi yang belum terjangkau jaringan kabel fiber optik.</p>
        <ul>
{fwa_points}
        </ul>
      </article>
      <article>
        <h3>Cek ketersediaan dan pendaftaran</h3>
        <p>Ketersediaan jaringan berbeda di setiap alamat. Sebelum berlangganan, sampaikan lokasi rumah atau tempat usaha Anda melalui WhatsApp atau <a href="#kontak-form">formulir kontak</a> agar admin dapat membantu pengecekan. Pemesanan dan pembayaran dilakukan di luar website sesuai ketentuan layanan.</p>
        <p>Gunakan tombol pada kartu paket agar pesan WhatsApp sudah memuat nama paket, kecepatan, harga, dan periode yang relevan.</p>
      </article>
    </div>
  </section>

  <section class="section about-contact">
    <div id="tentang" class="about-copy">
      <span class="eyebrow">04 / TENTANG KAMI</span>
      <h2>Pasang WiFi XL Home Jakarta Selatan &amp; Jabodetabek</h2>
      <p><strong>XL Home Jakarta</strong> melayani pemasangan WiFi rumah XL Home untuk rumah, apartemen, dan tempat usaha di Jakarta Selatan serta wilayah Jabodetabek. Kami membantu Anda memilih paket internet rumah yang sesuai dengan kebutuhan dan lokasi pemasangan.</p>
      <p>Kami menyediakan informasi paket internet rumah XL Home dengan pilihan teknologi <strong>FTTH (Fiber Optik)</strong> dan <strong>FWA (Fixed Wireless Access)</strong> untuk membantu Anda mendapatkan layanan internet rumah yang stabil.</p>
      <h3>Area layanan kami</h3>
      <ul class="service-area-list">
{areas}
      </ul>
      <p>Ketersediaan jaringan berbeda di setiap alamat. Sebelum berlangganan, sampaikan lokasi rumah atau tempat usaha Anda melalui WhatsApp atau <a href="#kontak-form">formulir kontak</a> agar ketersediaan jaringan dapat dicek terlebih dahulu.</p>
      <h3>Layanan XL Home Jakarta</h3>
      <ul>
{services}
      </ul>
      <p>Konsultasi ketersediaan jaringan, pendaftaran, dan detail paket dilakukan melalui WhatsApp. Pemesanan serta pembayaran dilakukan di luar website sesuai ketentuan layanan.</p>
    </div>
    <div id="kontak" class="contact-panel">
      {icon('wifi', 34)}
      <span class="small-label">MARI TERHUBUNG</span>
      <h2>Siap memasang<br/>WiFi di rumah?</h2>
      <p>Konsultasikan kebutuhan dan alamat Anda. Mulai dengan menghubungi admin atau <a href="#kontak-form" class="contact-inline-link">isi formulir kontak</a>.</p>
      <div class="contact-number">
        <span class="contact-brand">{e(PERSON)}</span>
        <span class="contact-role">{e(ROLE)}</span>
        <a class="contact-phone" href="{wa()}" target="_blank" rel="noopener noreferrer">{WA_DISPLAY} {icon('arrow-up-right', 16)}</a>
      </div>
      <a class="button light" href="{wa()}" target="_blank" rel="noopener noreferrer">{icon('message-circle', 20)} Chat WhatsApp {icon('arrow-up-right', 18)}</a>
      <span class="contact-footnote">{icon('map-pin', 12)} Melayani Jakarta Selatan &amp; Jabodetabek — cek jaringan sebelum berlangganan</span>
    </div>
  </section>

  <section id="kontak-form" class="section contact-form-section">
    <div class="contact-form-grid">
      <div class="contact-form-copy">
        <span class="eyebrow">06 / KONSULTASI GRATIS</span>
        <h2>Daftar WiFi XL Home — siap dipasang di rumah Anda?</h2>
        <p>Isi formulir di samping untuk konsultasi pemasangan WiFi XL Home. Sampaikan nama, nomor WhatsApp, dan area pemasangan agar kami dapat mengecek ketersediaan jaringan di lokasi Anda.</p>
        <div class="contact-form-cta">
          <span class="contact-form-label">Atau hubungi langsung</span>
          <a class="button primary" href="{wa()}" target="_blank" rel="noopener noreferrer">{icon('message-circle', 20)} {WA_DISPLAY} {icon('arrow-up-right', 18)}</a>
          <span class="contact-form-person">{e(PERSON)} — {e(ROLE)}</span>
        </div>
      </div>
      <div class="contact-form-panel">
        <form class="contact-form-fields" data-lead-form>
          <h3>Formulir konsultasi pemasangan</h3>
          <label class="field">
            <span>Nama lengkap</span>
            <input type="text" name="name" required autocomplete="name" placeholder="Nama Anda"/>
          </label>
          <label class="field">
            <span>Nomor WhatsApp</span>
            <input type="tel" name="whatsapp" required autocomplete="tel" placeholder="08xx xxxx xxxx"/>
          </label>
          <label class="field">
            <span>Area pemasangan</span>
            <input type="text" name="area" required placeholder="Contoh: Jakarta Selatan"/>
          </label>
          <label class="field">
            <span>Kebutuhan Anda (opsional)</span>
            <textarea name="needs" rows="4" placeholder="Jelaskan kebutuhan internet rumah atau tempat usaha Anda"></textarea>
          </label>
          <p class="contact-form-error" hidden></p>
          <button type="submit" class="button primary contact-form-submit">{icon('send', 18)} Kirim permintaan</button>
          <p class="contact-form-note">Dengan mengirim, Anda setuju untuk dihubungi via WhatsApp. Data Anda hanya digunakan untuk konsultasi pemasangan.</p>
        </form>
      </div>
    </div>
  </section>
</main>

<footer class="site-footer">
  <div class="footer-main">
    <div class="footer-brand">
      <a class="brand" href="/#beranda" aria-label="XL HOME Jakarta">
        <span class="brand-logo is-compact"><img src="assets/img/logo.jpg" alt="XL HOME Jakarta" width="320" height="120"/></span>
      </a>
      <p>Informasi layanan pasang WiFi XL HOME untuk rumah dan tempat usaha Anda.</p>
      <div class="social-links">
        <a href="https://www.instagram.com/" target="_blank" rel="noopener noreferrer" aria-label="Instagram (tautan sementara)">{icon('instagram', 19)}</a>
        <a href="https://www.facebook.com/" target="_blank" rel="noopener noreferrer" aria-label="Facebook (tautan sementara)">{icon('facebook', 19)}</a>
        <a href="https://www.tiktok.com/" target="_blank" rel="noopener noreferrer" aria-label="TikTok (tautan sementara)">{icon('music2', 19)}</a>
      </div>
    </div>
    <div>
      <h3>Navigasi cepat</h3>
      <nav aria-label="Navigasi footer">
{footer_links}
      </nav>
    </div>
    <div class="footer-contact">
      <h3>Hubungi kami</h3>
      <span>{e(PERSON)} — {e(ROLE)}</span>
      <a href="{wa()}" target="_blank" rel="noopener noreferrer">{WA_DISPLAY} {icon('arrow-up-right', 16)}</a>
      <p>Konsultasi &amp; pendaftaran paket WiFi XL HOME melalui WhatsApp.</p>
    </div>
  </div>
  <div class="footer-disclaimer">Website ini merupakan halaman informasi dan pemasaran layanan, bukan pernyataan sebagai situs resmi perusahaan. Identitas resmi perusahaan hanya digunakan sesuai izin dan materi brand yang tersedia. Tautan media sosial masih berupa placeholder.</div>
  <div class="footer-bottom">
    <span>© 2026 XL HOME. All rights reserved.</span>
    <button type="button" data-cookie-settings>Pengaturan cookie</button>
  </div>
</footer>

<script src="assets/js/main.js" defer></script>
</body>
</html>
"""


if __name__ == "__main__":
    out = render()
    open("index.html", "w").write(out)
    print("index.html", len(out))

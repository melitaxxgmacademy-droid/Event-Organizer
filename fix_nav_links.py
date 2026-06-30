from pathlib import Path
import re

base = Path(__file__).resolve().parent

nav_template = '''<header id="header" class="header d-flex align-items-center fixed-top">
    <div class="container-fluid container-xl position-relative d-flex align-items-center justify-content-between">

      <a href="index.html" class="logo d-flex align-items-center">
        <img src="assets/img/logo.webp" alt="Event Organizer" class="logo-img" style="max-height: 50px;">
      </a>

      <nav id="navmenu" class="navmenu">
        <ul>
          <li><a href="index.html"{home}>Beranda</a></li>
          <li><a href="about.html"{about}>Tentang Kami</a></li>
          <li><a href="schedule.html"{schedule}>Jadwal</a></li>
          <li><a href="speakers.html"{speakers}>Pembicara</a></li>
          <li><a href="blog.html"{blog}>Blog</a></li>
          <li class="dropdown"><a href="#"><span>Halaman Lain</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
            <ul>
              <li><a href="speaker-details.html"{detail}>Detail Pembicara</a></li>
              <li><a href="tickets.html"{tickets}>Tiket</a></li>
              <li><a href="buy-tickets.html"{buy}>Pesan Tiket</a></li>
              <li><a href="gallery.html"{gallery}>Galeri</a></li>
              <li><a href="terms.html"{terms}>Syarat</a></li>
              <li><a href="privacy.html"{privacy}>Privasi</a></li>
            </ul>
          </li>
          <li><a href="contact.html"{contact}>Kontak</a></li>
        </ul>
        <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
      </nav>

      <a class="btn-getstarted" href="buy-tickets.html">Pesan Tiket</a>

    </div>
  </header>'''

page_active = {
    'index.html': {'home': ' class="active"'},
    'about.html': {'about': ' class="active"'},
    'schedule.html': {'schedule': ' class="active"'},
    'speakers.html': {'speakers': ' class="active"'},
    'blog.html': {'blog': ' class="active"'},
    'contact.html': {'contact': ' class="active"'},
    'venue.html': {'home': '', 'about': '', 'schedule': '', 'speakers': '', 'blog': '', 'contact': ''},
    'speaker-details.html': {'detail': ' class="active"'},
    'tickets.html': {'tickets': ' class="active"'},
    'buy-tickets.html': {'buy': ' class="active"'},
    'gallery.html': {'gallery': ' class="active"'},
    'terms.html': {'terms': ' class="active"'},
    'privacy.html': {'privacy': ' class="active"'},
    '404.html': {},
    'starter-page.html': {},
    'sponsors.html': {},
    'hotel.html': {},
}

base_attrs = {k: '' for k in ['home','about','schedule','speakers','blog','detail','tickets','buy','gallery','terms','privacy','contact']}

header_pattern = re.compile(r'<header id="header" class="header[\s\S]*?</header>', re.MULTILINE)

# build header for a file

def build_header(filename):
    attrs = base_attrs.copy()
    if filename.name in page_active:
        attrs.update(page_active[filename.name])
    return nav_template.format(**attrs)

# helper to replace exact content once

def replace_once(text, old, new):
    if old in text:
        return text.replace(old, new, 1)
    return text

file_updates = []

for html_file in sorted(base.glob('*.html')):
    text = html_file.read_text(encoding='utf-8')
    new_header = build_header(html_file)
    if header_pattern.search(text):
        text = header_pattern.sub(new_header, text, count=1)
    else:
        print(f'warning: header not found in {html_file.name}')

    if html_file.name == 'buy-tickets.html':
        text = text.replace('href="#" target="_blank">Syarat and Conditions</a>', 'href="terms.html" target="_blank">Syarat and Conditions</a>')
        text = text.replace('href="#" target="_blank">Privasi Policy</a>', 'href="privacy.html" target="_blank">Privasi Policy</a>')

    if html_file.name == 'terms.html':
        text = text.replace('href="#" class="contact-link">Kontak Support</a>', 'href="contact.html" class="contact-link">Kontak Support</a>')

    if html_file.name == 'venue.html':
        text = text.replace('href="#" class="btn btn-primary">', 'href="https://www.google.com/maps/dir/?api=1&destination=125+Innovation+Boulevard+Chicago+IL" target="_blank" class="btn btn-primary">')
        text = text.replace('href="#" class="btn btn-outline-primary">', 'href="hotel.html" class="btn btn-outline-primary">')

    if html_file.name == 'speaker-details.html':
        text = re.sub(r'href="#"\s*class="social-btn linkedin"', 'href="https://www.linkedin.com" target="_blank" class="social-btn linkedin"', text)
        text = re.sub(r'href="#"\s*class="social-btn twitter"', 'href="https://twitter.com" target="_blank" class="social-btn twitter"', text)
        text = re.sub(r'href="#"\s*class="social-btn website"', 'href="index.html" class="social-btn website"', text)
        text = re.sub(r'href="#"\s*class="btn-primary"', 'href="schedule.html" class="btn-primary"', text)
        text = re.sub(r'href="#"\s*class="btn-secondary"', 'href="speakers.html" class="btn-secondary"', text)
        text = re.sub(r'href="#"\s*class="btn-outline"', 'href="contact.html" class="btn-outline"', text)

    if html_file.name == 'speakers.html':
        text = re.sub(r'href="#"\s*class="social-link"', 'href="contact.html" class="social-link"', text)

    # fix generic social icon placeholders in footers and content sections
    text = re.sub(r'href="#"\s*>(\s*<i class="bi bi-(twitter|facebook|instagram|linkedin)"></i>\s*)</a>', r'href="contact.html">\1</a>', text)
    text = re.sub(r'href="#"\s*(class="social-btn)', 'href="contact.html" \1', text)

    # fix any remaining button placeholder on venue sections that may appear elsewhere
    text = text.replace('href="#" class="btn btn-primary">', 'href="https://www.google.com/maps/dir/?api=1&destination=125+Innovation+Boulevard+Chicago+IL" target="_blank" class="btn btn-primary">')
    text = text.replace('href="#" class="btn btn-outline-primary">', 'href="hotel.html" class="btn btn-outline-primary">')

    html_file.write_text(text, encoding='utf-8')
    file_updates.append(html_file.name)

hotel_file = base / 'hotel.html'
if not hotel_file.exists():
    hotel_html = '''<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <title>Hotel Terdekat - Event Organizer</title>
  <meta name="description" content="Temukan hotel terdekat dengan lokasi acara untuk kenyamanan peserta dan tamu Anda.">
  <meta name="keywords" content="hotel terdekat, acara, penginapan, event organizer, konferensi">

  <link href="assets/img/favicon.webp" rel="icon">
  <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">

  <link href="https://fonts.googleapis.com" rel="preconnect">
  <link href="https://fonts.gstatic.com" rel="preconnect" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&family=Rubik:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Kanit:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">

  <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">
  <link href="assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">

  <link href="assets/css/main.css?v=20260629" rel="stylesheet">
</head>

<body class="hotel-page">
''' + build_header(hotel_file) + '''

  <main class="main">
    <div class="page-title dark-background" style="background-image: url(assets/img/events/showcase-9.webp);">
      <div class="container position-relative">
        <h1>Hotel Terdekat</h1>
        <p>Temukan pilihan penginapan terbaik di sekitar lokasi acara untuk kenyamanan tim dan tamu Anda.</p>
        <nav class="breadcrumbs">
          <ol>
            <li><a href="index.html">Beranda</a></li>
            <li class="current">Hotel Terdekat</li>
          </ol>
        </nav>
      </div>
    </div>

    <section id="hotel-list" class="hotel-list section">
      <div class="container">
        <div class="row gy-5">
          <div class="col-lg-4">
            <div class="hotel-card">
              <img src="assets/img/hotel/hotel-1.webp" alt="Grand Palace Hotel" class="img-fluid rounded mb-4">
              <h3>Grand Palace Hotel</h3>
              <p>Hotel bintang 5 dengan fasilitas konferensi lengkap, hanya 5 menit dari lokasi acara.</p>
              <ul>
                <li>Ruang pertemuan bisnis</li>
                <li>WiFi gratis</li>
                <li>Shuttle bandara</li>
              </ul>
              <a href="contact.html" class="btn btn-primary">Pesan Kamar</a>
            </div>
          </div>
          <div class="col-lg-4">
            <div class="hotel-card">
              <img src="assets/img/hotel/hotel-2.webp" alt="City View Suites" class="img-fluid rounded mb-4">
              <h3>City View Suites</h3>
              <p>Akomodasi modern dekat pusat kota dengan akses cepat ke restoran dan pusat perbelanjaan.</p>
              <ul>
                <li>Kamar luas</li>
                <li>Ruang rapat kecil</li>
                <li>Area relaksasi</li>
              </ul>
              <a href="contact.html" class="btn btn-secondary">Hubungi Kami</a>
            </div>
          </div>
          <div class="col-lg-4">
            <div class="hotel-card">
              <img src="assets/img/hotel/hotel-3.webp" alt="Conference Plaza" class="img-fluid rounded mb-4">
              <h3>Conference Plaza</h3>
              <p>Solusi penginapan khusus event dengan harga paket untuk peserta dan tamu VIP.</p>
              <ul>
                <li>Penawaran grup</li>
                <li>Ruang sarapan</li>
                <li>Fasilitas kebugaran</li>
              </ul>
              <a href="contact.html" class="btn btn-outline-primary">Pelajari Lebih Lanjut</a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

  <footer id="footer" class="footer position-relative dark-background">
    <div class="container footer-top">
      <div class="row gy-4">
        <div class="col-lg-4 col-md-6 footer-about">
          <a href="index.html" class="logo d-flex align-items-center">
            <span class="sitename">Event Organizer</span>
          </a>
          <p class="footer-text pt-3">Kami merancang pengalaman acara yang kuat, mulai dari strategi hingga pelaksanaan hari-H.</p>
          <div class="footer-contact pt-3">
            <p>Jl. Sudirman No. 123</p>
            <p>Jakarta Selatan, DKI Jakarta</p>
            <p class="mt-3"><strong>Telepon:</strong> <span>+62 812 3456 7890</span></p>
            <p><strong>Email:</strong> <span>info@eventorganizer.co.id</span></p>
          </div>
          <div class="social-links d-flex mt-4">
            <a href="contact.html"><i class="bi bi-twitter"></i></a>
            <a href="contact.html"><i class="bi bi-facebook"></i></a>
            <a href="contact.html"><i class="bi bi-instagram"></i></a>
            <a href="contact.html"><i class="bi bi-linkedin"></i></a>
          </div>
        </div>
        <div class="col-lg-2 col-md-6 footer-links">
          <h4>Link Cepat</h4>
          <ul>
            <li><a href="index.html">Beranda</a></li>
            <li><a href="about.html">Tentang Kami</a></li>
            <li><a href="schedule.html">Jadwal</a></li>
            <li><a href="speakers.html">Pembicara</a></li>
            <li><a href="contact.html">Kontak</a></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="container py-4">
      <div class="copyright">
        &copy; 2026 Event Organizer. All Rights Reserved.
      </div>
    </div>
  </footer>

  <a href="#" id="scroll-top" class="scroll-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>
  <div id="preloader"></div>
</body>
</html>'''
    hotel_file.write_text(hotel_html, encoding='utf-8')
    file_updates.append('hotel.html (created)')

print('updated files:', ', '.join(file_updates))

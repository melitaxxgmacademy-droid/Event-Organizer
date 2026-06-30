import os
import re
from pathlib import Path

root = Path(__file__).resolve().parent
html_files = sorted(root.glob('*.html'))
modified = []
for path in html_files:
    text = path.read_text(encoding='utf-8')
    orig = text
    text = re.sub(r'<li>\s*<a href="venue\.html">Lokasi</a>\s*</li>', '<li><a href="blog.html">Blog</a></li>', text)
    text = text.replace('<li><a href="speaker-details.html">Detail Pembicara</a></li>\n', '')
    text = text.replace('<li><a href="speaker-details.html">Detail Pembicara</a></li>', '')
    if path.name == 'speaker-details.html':
        text = text.replace(
            '                <a href="#" class="btn-primary">\n                  <i class="bi bi-calendar-plus"></i>\n                  Add to My Jadwal\n                </a>\n                <a href="#" class="btn-secondary">\n                  <i class="bi bi-arrow-left"></i>\n                  All Pembicara\n                </a>\n                <a href="#" class="btn-outline">\n                  <i class="bi bi-share"></i>\n                  Share Profile\n                </a>',
            '                <a href="schedule.html" class="btn-primary">\n                  <i class="bi bi-calendar-plus"></i>\n                  Add to My Jadwal\n                </a>\n                <a href="speakers.html" class="btn-secondary">\n                  <i class="bi bi-arrow-left"></i>\n                  All Pembicara\n                </a>'
        )
        text = re.sub(r'<a href="#" class="btn-outline">\s*<i class="bi bi-share"></i>\s*Share Profile\s*</a>', '', text)
    if path.name == 'venue.html':
        text = text.replace(
            '                <a href="#" class="btn btn-primary">\n                  <i class="bi bi-map"></i>\n                  Petunjuk Arah\n                </a>',
            '                <a href="https://www.google.com/maps/dir/?api=1&destination=Grand+Palace+Hotel" target="_blank" class="btn btn-primary">\n                  <i class="bi bi-map"></i>\n                  Petunjuk Arah\n                </a>'
        )
        text = text.replace(
            '                <a href="#" class="btn btn-outline-primary">\n                  <i class="bi bi-building"></i>\n                  Hotel Terdekat\n                </a>',
            '                <a href="https://www.google.com/search?q=hotel+dekat+Grand+Palace+Hotel" target="_blank" class="btn btn-outline-primary">\n                  <i class="bi bi-building"></i>\n                  Hotel Terdekat\n                </a>'
        )
    if text != orig:
        path.write_text(text, encoding='utf-8')
        modified.append(path.name)

blog_path = root / 'blog.html'
created_blog = False
if not blog_path.exists():
    blog_text = '''<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <title>Blog - Event Organizer</title>
  <meta name="description" content="Blog Event Organizer untuk berita dan artikel acara profesional.">
  <meta name="keywords" content="blog event, event organizer, artikel acara, berita event">
  <link href="assets/img/favicon.png" rel="icon">
  <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">
  <link href="https://fonts.googleapis.com" rel="preconnect">
  <link href="https://fonts.gstatic.com" rel="preconnect" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&family=Rubik:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
  <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">
  <link href="assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
  <link href="assets/css/main.css?v=20260629" rel="stylesheet">
</head>

<body class="index-page">
  <header id="header" class="header d-flex align-items-center fixed-top">
    <div class="container-fluid container-xl position-relative d-flex align-items-center justify-content-between">
      <a href="index.html" class="logo d-flex align-items-center">
        <h1 class="sitename">Event Organizer</h1>
      </a>
      <nav id="navmenu" class="navmenu">
        <ul>
          <li><a href="index.html">Beranda</a></li>
          <li><a href="about.html">Tentang Kami</a></li>
          <li><a href="schedule.html">Jadwal</a></li>
          <li><a href="speakers.html">Pembicara</a></li>
          <li><a href="blog.html" class="active">Blog</a></li>
          <li class="dropdown"><a href="#"><span>Halaman Lain</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
            <ul>
              <li><a href="tickets.html">Tiket</a></li>
              <li><a href="buy-tickets.html">Pesan Tiket</a></li>
              <li><a href="gallery.html">Galeri</a></li>
              <li><a href="terms.html">Syarat</a></li>
              <li><a href="privacy.html">Privasi</a></li>
            </ul>
          </li>
          <li><a href="contact.html">Kontak</a></li>
        </ul>
        <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
      </nav>
      <a class="btn-getstarted" href="buy-tickets.html">Pesan Tiket</a>
    </div>
  </header>

  <main class="main">
    <section id="hero" class="hero section dark-background">
      <div class="background-overlay"></div>
      <div class="hero-content">
        <div class="container">
          <div class="row justify-content-center text-center">
            <div class="col-lg-9">
              <div class="hero-text">
                <h1 class="hero-title">Blog Event Organizer</h1>
                <p class="hero-subtitle">Berita, tips, dan insight acara profesional untuk membantu tim Anda sukses.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="blog" class="section pt-5">
      <div class="container">
        <div class="row gy-4">
          <div class="col-lg-4">
            <article class="blog-card">
              <h3>Strategi Acara Hybrid</h3>
              <p>Memaksimalkan kehadiran offline dan online untuk pengalaman acara yang lebih luas.</p>
              <a href="contact.html" class="read-more">Baca Selengkapnya</a>
            </article>
          </div>
          <div class="col-lg-4">
            <article class="blog-card">
              <h3>Rencana Anggaran Event</h3>
              <p>Cara membuat anggaran acara yang terukur dan mudah dijalankan.</p>
              <a href="buy-tickets.html" class="read-more">Baca Selengkapnya</a>
            </article>
          </div>
          <div class="col-lg-4">
            <article class="blog-card">
              <h3>Tips Networking</h3>
              <p>Empat langkah meningkatkan peluang relasi selama konferensi dan seminar.</p>
              <a href="speakers.html" class="read-more">Baca Selengkapnya</a>
            </article>
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
            <p><strong>Phone:</strong> +62 21 1234 5678</p>
          </div>
        </div>
        <div class="col-lg-2 col-md-6 footer-links">
          <h4>Menu Utama</h4>
          <ul>
            <li><a href="index.html">Beranda</a></li>
            <li><a href="about.html">Tentang Kami</a></li>
            <li><a href="schedule.html">Jadwal</a></li>
            <li><a href="speakers.html">Pembicara</a></li>
            <li><a href="contact.html">Kontak</a></li>
          </ul>
        </div>
        <div class="col-lg-2 col-md-6 footer-links">
          <h4>Layanan</h4>
          <ul>
            <li><a href="buy-tickets.html">Pesan Tiket</a></li>
            <li><a href="tickets.html">Tiket</a></li>
            <li><a href="gallery.html">Galeri</a></li>
            <li><a href="blog.html">Blog</a></li>
          </ul>
        </div>
        <div class="col-lg-4 col-md-6 footer-links">
          <h4>Informasi</h4>
          <ul>
            <li><a href="privacy.html">Kebijakan Privasi</a></li>
            <li><a href="terms.html">Syarat & Ketentuan</a></li>
            <li><a href="about.html">Tentang Tim</a></li>
            <li><a href="contact.html">Dukungan</a></li>
            <li><a href="speakers.html">Testimoni</a></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="container copyright text-center mt-4">
      <p>© 2026 <strong class="px-1 sitename">Event Organizer</strong>. Semua hak dilindungi.</p>
    </div>
  </footer>

  <a href="#" id="scroll-top" class="scroll-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>
  <div id="preloader"></div>
  <script src="assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="assets/vendor/php-email-form/validate.js"></script>
  <script src="assets/vendor/purecounter/purecounter_vanilla.js"></script>
  <script src="assets/vendor/swiper/swiper-bundle.min.js"></script>
  <script src="assets/vendor/glightbox/js/glightbox.min.js"></script>
  <script src="assets/js/main.js?v=20260629"></script>
</body>
</html>'''
    blog_path.write_text(blog_text, encoding='utf-8')
    created_blog = True

print('modified files:', ', '.join(modified))
if created_blog:
    print('created blog.html')
"
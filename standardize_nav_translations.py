import glob
import os
import re

# Standardized navigation HTML
nav_template = '''<nav id="navmenu" class="navmenu">
        <ul>
          <li><a href="index.html"{index_active}>Beranda</a></li>
          <li><a href="about.html"{about_active}>Tentang</a></li>
          <li><a href="schedule.html"{schedule_active}>Jadwal</a></li>
          <li><a href="speakers.html"{speakers_active}>Pembicara</a></li>
          <li><a href="venue.html"{venue_active}>Lokasi</a></li>
          <li class="dropdown"><a href="#"><span>Halaman Lain</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
            <ul>
              <li><a href="speaker-details.html"{speaker_details_active}>Detail Pembicara</a></li>
              <li><a href="tickets.html"{tickets_active}>Tiket</a></li>
              <li><a href="buy-tickets.html"{buy_tickets_active}>Pesan Tiket</a></li>
              <li><a href="gallery.html"{gallery_active}>Galeri</a></li>
              <li><a href="terms.html"{terms_active}>Syarat</a></li>
              <li><a href="privacy.html"{privacy_active}>Privasi</a></li>
              <li><a href="404.html"{page404_active}>404</a></li>
            </ul>
          </li>
          <li><a href="contact.html"{contact_active}>Kontak</a></li>
        </ul>
        <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
      </nav>'''

page_titles = {
    '404.html': '404 - Event Organizer',
    'about.html': 'Tentang - Event Organizer',
    'buy-tickets.html': 'Pesan Tiket - Event Organizer',
    'contact.html': 'Kontak - Event Organizer',
    'gallery.html': 'Galeri - Event Organizer',
    'privacy.html': 'Privasi - Event Organizer',
    'schedule.html': 'Jadwal - Event Organizer',
    'speaker-details.html': 'Detail Pembicara - Event Organizer',
    'speakers.html': 'Pembicara - Event Organizer',
    'sponsors.html': 'Sponsor - Event Organizer',
    'starter-page.html': 'Halaman Utama - Event Organizer',
    'terms.html': 'Syarat - Event Organizer',
    'tickets.html': 'Tiket - Event Organizer',
    'venue.html': 'Lokasi - Event Organizer',
    'index.html': 'Beranda - Event Organizer',
}

heading_translations = {
    'About': 'Tentang',
    'Contact': 'Kontak',
    'Gallery': 'Galeri',
    'Schedule': 'Jadwal',
    'Speakers': 'Pembicara',
    'Venue': 'Lokasi',
    'Buy Tickets': 'Pesan Tiket',
    'Tickets': 'Tiket',
    'Speaker Details': 'Detail Pembicara',
    'Terms': 'Syarat',
    'Privacy': 'Privasi',
    'Sponsors': 'Sponsor',
    'Starter Page': 'Halaman Utama',
}

meta_descriptions = {
    'default': 'Website Event Organizer profesional untuk penyelenggaraan acara perusahaan, seminar, konferensi, dan festival.',
}
meta_keywords = {
    'default': 'event organizer, EO, acara, konferensi, seminar, manajemen event, produksi acara',
}

for file_path in sorted(glob.glob('*.html')):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Standardize site name
    content = content.replace('<h1 class="sitename">Evently</h1>', '<h1 class="sitename">Event Organizer</h1>')
    content = content.replace('Template Name: Evently', 'Template Name: Event Organizer')

    # Build active state values
    active_vars = {
        'index_active': ' class="active"' if file_path == 'index.html' else '',
        'about_active': ' class="active"' if file_path == 'about.html' else '',
        'schedule_active': ' class="active"' if file_path == 'schedule.html' else '',
        'speakers_active': ' class="active"' if file_path == 'speakers.html' else '',
        'venue_active': ' class="active"' if file_path == 'venue.html' else '',
        'speaker_details_active': ' class="active"' if file_path == 'speaker-details.html' else '',
        'tickets_active': ' class="active"' if file_path == 'tickets.html' else '',
        'buy_tickets_active': ' class="active"' if file_path == 'buy-tickets.html' else '',
        'gallery_active': ' class="active"' if file_path == 'gallery.html' else '',
        'terms_active': ' class="active"' if file_path == 'terms.html' else '',
        'privacy_active': ' class="active"' if file_path == 'privacy.html' else '',
        'page404_active': ' class="active"' if file_path == '404.html' else '',
        'contact_active': ' class="active"' if file_path == 'contact.html' else '',
    }

    new_nav = nav_template.format(**active_vars)
    content = re.sub(r'<nav id="navmenu" class="navmenu">.*?</nav>', new_nav, content, flags=re.S)

    # Replace page titles
    if file_path in page_titles:
        content = re.sub(r'<title>.*?</title>', f'<title>{page_titles[file_path]}</title>', content, count=1)

    # Replace top heading titles
    for old, new in heading_translations.items():
        content = re.sub(rf'(<h1[^>]*>){old}(</h1>)', rf'\1{new}\2', content)

    # Fill missing standard meta tags in the head
    if '<meta name="description" content="">' in content:
        content = content.replace('<meta name="description" content="">', f'<meta name="description" content="{meta_descriptions["default"]}">')
    if '<meta content="" name="description">' in content:
        content = content.replace('<meta content="" name="description">', f'<meta content="{meta_descriptions["default"]}" name="description">')
    if '<meta content="" name="keywords">' in content:
        content = content.replace('<meta content="" name="keywords">', f'<meta content="{meta_keywords["default"]}" name="keywords">')

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated', file_path)
    else:
        print('No change', file_path)

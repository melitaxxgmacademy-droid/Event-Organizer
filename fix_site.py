import glob
import os
import re

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

heading_replacements = {
    'Speaker Details': 'Detail Pembicara',
    'About': 'Tentang',
    'Contact': 'Kontak',
    'Gallery': 'Galeri',
    'Schedule': 'Jadwal',
    'Speakers': 'Pembicara',
    'Venue': 'Lokasi',
    'Buy Tickets': 'Pesan Tiket',
    'Tickets': 'Tiket',
    'Terms of Service': 'Syarat Layanan',
    'Privacy Policy': 'Kebijakan Privasi',
    'Sponsors': 'Sponsor',
    'Starter Page': 'Halaman Utama',
}

schedule_day_translations = {
    'Day 1 - March 15': 'Hari 1 - 15 Maret',
    'Day 2 - March 16': 'Hari 2 - 16 Maret',
    'Day 3 - March 17': 'Hari 3 - 17 Maret',
}

contact_info_translations = {
    'Our Address': 'Alamat Kami',
    'Email Address': 'Email',
    'Hours of Operation': 'Jam Layanan',
    'Sunday-Fri: 9 AM - 6 PM': 'Minggu-Jumat: 09.00 - 18.00',
    'Saturday: 9 AM - 4 PM': 'Sabtu: 09.00 - 16.00',
}

base_meta_description = 'Website Event Organizer profesional untuk penyelenggaraan acara perusahaan, seminar, konferensi, dan festival.'
base_meta_keywords = 'event organizer, EO, acara, konferensi, seminar, manajemen event, produksi acara'

for file_path in sorted(glob.glob('*.html')):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Standardize site name and template metadata comments
    content = content.replace('<h1 class="sitename">Evently</h1>', '<h1 class="sitename">Event Organizer</h1>')
    content = content.replace('Template Name: Evently', 'Template Name: Event Organizer')

    # Replace the entire navigation block with a clean standardized nav
    active_flags = {
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
    cleaned_nav = nav_template.format(**active_flags)
    content = re.sub(r'<nav id="navmenu" class="navmenu">.*?</nav>', cleaned_nav, content, flags=re.S)

    # Replace page titles
    if file_path in page_titles:
        content = re.sub(r'<title>.*?</title>', f'<title>{page_titles[file_path]}</title>', content, count=1)

    # Standardize top headings and breadcrumb labels
    for old, new in heading_replacements.items():
        content = re.sub(rf'(<h1[^>]*>){re.escape(old)}(</h1>)', rf'\1{new}\2', content)
        content = content.replace(f'<li class="current">{old}</li>', f'<li class="current">{new}</li>')
        content = content.replace(f'>{old}<', f'>{new}<')

    # Translate schedule day labels
    for old, new in schedule_day_translations.items():
        content = content.replace(old, new)

    # Translate contact info labels
    for old, new in contact_info_translations.items():
        content = content.replace(old, new)

    if '<meta content="" name="description">' in content:
        content = content.replace('<meta content="" name="description">', f'<meta content="{base_meta_description}" name="description">')
    if '<meta content="" name="keywords">' in content:
        content = content.replace('<meta content="" name="keywords">', f'<meta content="{base_meta_keywords}" name="keywords">')
    if '<meta name="description" content="">' in content:
        content = content.replace('<meta name="description" content="">', f'<meta name="description" content="{base_meta_description}">')
    if '<meta name="keywords" content="">' in content:
        content = content.replace('<meta name="keywords" content="">', f'<meta name="keywords" content="{base_meta_keywords}">')

    # Update some page-specific texts for Event Organizer focus
    content = content.replace('Evently', 'Event Organizer')

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated', file_path)
    else:
        print('No change', file_path)

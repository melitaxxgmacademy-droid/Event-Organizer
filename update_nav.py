import glob
import re
import os

files = sorted(glob.glob('*.html'))

nav_replacements = [
    ('>Home<', '>Beranda<'),
    ('>About<', '>Tentang<'),
    ('>Schedule<', '>Jadwal<'),
    ('>Speakers<', '>Pembicara<'),
    ('>Venue<', '>Lokasi<'),
    ('>More Pages<', '>Halaman Lain<'),
    ('>Buy Tickets<', '>Pesan Tiket<'),
    ('>Tickets<', '>Tiket<'),
    ('>Gallery<', '>Galeri<'),
    ('>Terms<', '>Syarat<'),
    ('>Privacy<', '>Privasi<'),
    ('>Contact<', '>Kontak<'),
]

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

additional_translations = [
    ('Evently', 'Event Organizer'),
    ('Read more', 'Baca selengkapnya'),
    ('Read More', 'Baca Selengkapnya'),
    ('Contact Us', 'Hubungi Kami'),
    ('Book now', 'Pesan sekarang'),
    ('Our Speakers', 'Pembicara Kami'),
    ('About Us', 'Tentang Kami'),
    ('More about the event', 'Lebih lanjut tentang acara'),
    ('Get Tickets', 'Dapatkan Tiket'),
    ('24/7 Support', 'Dukungan 24/7'),
    ('Home', 'Beranda'),
    ('About', 'Tentang'),
    ('Schedule', 'Jadwal'),
    ('Speakers', 'Pembicara'),
    ('Venue', 'Lokasi'),
    ('More Pages', 'Halaman Lain'),
    ('Buy Tickets', 'Pesan Tiket'),
    ('Tickets', 'Tiket'),
    ('Gallery', 'Galeri'),
    ('Terms', 'Syarat'),
    ('Privacy', 'Privasi'),
    ('Contact', 'Kontak'),
]

for file in files:
    path = os.path.join(file)
    with open(path, 'r', encoding='utf-8') as fh:
        content = fh.read()
    original = content

    content = content.replace('<h1 class="sitename">Evently</h1>', '<h1 class="sitename">Event Organizer</h1>')
    for old, new in nav_replacements:
        content = content.replace(old, new)
    for old, new in additional_translations:
        content = content.replace(old, new)
    if file in page_titles:
        content = re.sub(r'<title>.*?</title>', '<title>' + page_titles[file] + '</title>', content, count=1)
    for old, new in heading_replacements.items():
        content = content.replace(f'<h1>{old}</h1>', f'<h1>{new}</h1>')
    content = re.sub(r'<li class="dropdown"><a href="#"><span>Dropdown</span>.*?</ul>\s*</li>', '', content, flags=re.S)
    if content != original:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(content)
        print('Updated', file)
    else:
        print('No changes', file)

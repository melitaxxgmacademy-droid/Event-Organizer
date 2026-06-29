import glob
import os
import re

replacements = [
    ('View Profile', 'Lihat Profil'),
    ('Keynote', 'Kunci'),
    ('Closing Keynote', 'Keynote Penutup'),
    ('Keynote Presentation', 'Presentasi Kunci'),
    ('Register Now', 'Daftar Sekarang'),
    ('Meet & greet with keynote speakers', 'Bertemu & sapa pembicara kunci'),
    ('Our Address', 'Alamat Kami'),
    ('Email Address', 'Email'),
    ('Hours of Operation', 'Jam Operasional'),
    ('Sunday-Fri: 9 AM - 6 PM', 'Minggu-Jumat: 09.00 - 18.00'),
    ('Saturday: 9 AM - 4 PM', 'Sabtu: 09.00 - 16.00'),
    ('If you have any questions about this Privasi Policy or our practices, please contact us:', 'Jika Anda memiliki pertanyaan tentang Kebijakan Privasi ini atau praktik kami, silakan hubungi kami:'),
    ('Speaker Details', 'Detail Pembicara'),
    ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
    ('Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
    ('If you have any questions about these Syarat, please contact us.', 'Jika Anda memiliki pertanyaan tentang Syarat ini, silakan hubungi kami.'),
    ('Convenient access via I-90 and I-94. Complimentary valet parking available for all registered attendees.', 'Akses mudah melalui I-90 dan I-94. Layanan parkir valet gratis tersedia untuk semua peserta terdaftar.'),
]

for file_path in sorted(glob.glob('*.html')):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    for old, new in replacements:
        content = content.replace(old, new)

    if file_path == 'schedule.html':
        content = content.replace('Day 1 - March 15', 'Hari 1 - 15 Maret')
        content = content.replace('Day 2 - March 16', 'Hari 2 - 16 Maret')
        content = content.replace('Day 3 - March 17', 'Hari 3 - 17 Maret')
    if file_path == 'schedule.html' or file_path == 'speaker-details.html':
        content = content.replace('Keynote', 'Keynote')

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated', file_path)
    else:
        print('No change', file_path)

import glob
import re
import os

replacements = [
    # about.html content
    ('Transforming Ideas Into Reality', 'Mengubah Ide Menjadi Kenyataan'),
    ('Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 'Kami mengelola setiap acara dengan perencanaan matang, eksekusi profesional, dan pengalaman peserta terbaik.'),
    ('Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'Kami menyediakan layanan event organizer lengkap yang memenuhi kebutuhan perusahaan, mulai dari strategi hingga pelaksanaan acara.'),
    ('"Consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam."', '"Kami menyajikan pengalaman acara terbaik dengan fokus pada hasil nyata dan kepuasan peserta."'),
    ('View Full Agenda', 'Lihat Agenda Lengkap'),
    ('3 Days', '3 Hari'),
    ('Of intensive learning and networking', 'Pembelajaran intensif dan jaringan profesional'),
    ('Expected attendees from 40+ countries', 'Diperkirakan hadir dari lebih dari 40 negara'),
    ('Industry experts and thought leaders', 'Ahli industri dan pemimpin pemikiran'),
    ('Covering technology, business & innovation', 'Mencakup teknologi, bisnis & inovasi'),
    ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.', 'Hadiri acara yang dirancang untuk memperkuat strategi bisnis dan hubungan mitra.'),
    # index.html content
    ('"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris."', '"Pelayanan event organizer yang membangun pengalaman acara profesional dan tak terlupakan."'),
    ('Future of Digital Innovation', 'Masa Depan Inovasi Digital'),
    ('Chief Technology Officer, TechCorp', 'Kepala Teknologi, TechCorp'),
    ('Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'Sesi inti yang menghadirkan wawasan praktis untuk tim event dan penyelenggara.'),
    ('Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium.', 'Kami hadirkan solusi profesional tanpa kompromi dan fokus hasil nyata.'),
    ('Ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit.', 'Diskusi interaktif yang dirancang untuk meningkatkan kapabilitas tim event Anda.'),
    ('Workshop Hall C', 'Ruang Workshop C'),
    # schedule.html
    ('Future of Digital Innovation', 'Masa Depan Inovasi Digital'),
    ('Chief Technology Officer, TechCorp', 'Kepala Teknologi, TechCorp'),
    ('Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'Sesi inti yang memberikan strategi acara praktis dan langsung dapat diterapkan.'),
    ('Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla.', 'Kami menyusun agenda yang kuat untuk pertumbuhan acara dan jaringan bisnis.'),
    ('Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium.', 'Presentasi utama dengan wawasan strategi acara yang berdampak.'),
    ('Ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit.', 'Pelatihan praktis interaktif dengan studi kasus nyata.'),
    ('Workshop Room', 'Ruang Workshop'),
    ('Hands-on Workshop', 'Workshop Praktis'),
    # speaker-details
    ('Speaker Biography', 'Biografi Pembicara'),
    ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 'Biografi pembicara yang mencerminkan pengalaman profesional dan kontribusi dalam dunia event.'),
    ('Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore.', 'Kami menyajikan sesi yang menggugah dengan pendekatan praktis dan inspiratif.'),
    ('Speaker Biography', 'Biografi Pembicara'),
    ('Areas of Expertise', 'Bidang Keahlian'),
    ('Digital Strategy', 'Strategi Digital'),
    ('Innovation Management', 'Manajemen Inovasi'),
    ('Tech Leadership', 'Kepemimpinan Teknologi'),
    ('Business Transformation', 'Transformasi Bisnis'),
    ('Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 'Kami selalu memastikan setiap acara dikelola profesional dan sesuai target klien.'),
    # speakers page
    ('Exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit voluptate.', 'Fokus pada solusi acara yang berdampak dan terukur.'),
    ('Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium totam rem aperiam.', 'Menghadirkan pionir industri dengan pendekatan acara inovatif.'),
]

for file_path in sorted(glob.glob('*.html')):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    for old, new in replacements:
        content = content.replace(old, new)

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated', file_path)
    else:
        print('No change', file_path)

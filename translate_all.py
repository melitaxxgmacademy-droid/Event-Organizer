from pathlib import Path

root = Path(__file__).parent
html_files = list(root.glob('*.html'))

replacements = {
    'Esse dolorum voluptatum ullam est sint nemo et est ipsa porro placeat quibusdam quia assumenda numquam molestias.': 'Temukan informasi penting halaman ini untuk merencanakan acara Anda dengan lebih baik.',
    'Get the Complete Jadwal': 'Unduh Jadwal Lengkap',
    'Download the full agenda as PDF or add events to your calendar': 'Unduh agenda lengkap dalam PDF atau tambahkan acara ke kalender Anda.',
    'Add to Calendar': 'Tambah ke Kalender',
    'Quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute.': 'Sesi ini dirancang untuk memberi wawasan praktis dan aksi nyata bagi tim Anda.',
    'Irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.': 'Praktik DevOps terbaik untuk tim Anda.',
    'Excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim.': 'Pembicara membagikan strategi terbaik untuk keberhasilan acara yang terencana.',
    'In voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat.': 'Penutupan sesi membahas masa depan kolaborasi lintas tim.',
    'Ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation.': 'Materi praktis ini mendukung pengembangan kapabilitas tim penyelenggara.',
    'Totam rem aperiam eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae.': 'Konten sesi berfokus pada praktik terbaik dan studi kasus.',
    'Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit sed quia.': 'Sesi ini menyoroti pengalaman peserta dan insight kunci.',
    'Download PDF': 'Unduh PDF',
    'Add to Calendar': 'Tambah ke Kalender'
}

updated = []
for fp in html_files:
    text = fp.read_text(encoding='utf-8')
    original = text
    for old, new in replacements.items():
        if old in text:
            text = text.replace(old, new)
    if text != original:
        fp.write_text(text, encoding='utf-8')
        updated.append(fp.name)

print('Updated files:')
for u in updated:
    print(u)

if not updated:
    print('No files updated.')

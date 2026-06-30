from pathlib import Path
import re

root = Path(__file__).resolve().parent
html_files = sorted(root.glob('*.html'))

for path in html_files:
    text = path.read_text(encoding='utf-8')
    orig = text

    text = text.replace('<a href="venue.html">Lokasi</a>', '<a href="blog.html">Blog</a>')
    text = text.replace('<a href="venue.html" class="active">Lokasi</a>', '<a href="blog.html" class="active">Blog</a>')
    text = text.replace('<li><a href="speaker-details.html">Detail Pembicara</a></li>\n', '')
    text = text.replace('<li><a href="speaker-details.html">Detail Pembicara</a></li>', '')
    text = text.replace('<li><a href="speaker-details.html" class="active">Detail Pembicara</a></li>\n', '')
    text = text.replace('<li><a href="speaker-details.html" class="active">Detail Pembicara</a></li>', '')

    if path.name == 'speaker-details.html':
        text = re.sub(r'<a href="#" class="btn-outline">\s*<i class="bi bi-share"></i>\s*Share Profile\s*</a>\s*', '', text, flags=re.S)
        text = text.replace(
            '                <a href="#" class="btn-primary">\n                  <i class="bi bi-calendar-plus"></i>\n                  Add to My Jadwal\n                </a>',
            '                <a href="schedule.html" class="btn-primary">\n                  <i class="bi bi-calendar-plus"></i>\n                  Add to My Jadwal\n                </a>'
        )
        text = text.replace(
            '                <a href="#" class="btn-secondary">\n                  <i class="bi bi-arrow-left"></i>\n                  All Pembicara\n                </a>',
            '                <a href="speakers.html" class="btn-secondary">\n                  <i class="bi bi-arrow-left"></i>\n                  All Pembicara\n                </a>'
        )

    if text != orig:
        path.write_text(text, encoding='utf-8')
        print(path.name)

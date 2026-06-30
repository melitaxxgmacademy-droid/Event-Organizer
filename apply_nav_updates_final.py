import re
from pathlib import Path

root = Path(__file__).resolve().parent
html_files = sorted(root.glob('*.html'))

venue_pattern = re.compile(r'<a href="venue\.html"(?:\s+class="active")?>\s*Lokasi\s*</a>', re.IGNORECASE)
speaker_pattern = re.compile(r'<a href="speaker-details\.html"(?:\s+class="active")?>\s*Detail Pembicara\s*</a>', re.IGNORECASE)
share_pattern = re.compile(r'<a href="#" class="btn-outline">\s*<i class="bi bi-share"></i>\s*Share Profile\s*</a>\s*', re.S)

modified = []
for path in html_files:
    text = path.read_text(encoding='utf-8')
    orig = text

    text = venue_pattern.sub('<a href="blog.html">Blog</a>', text)
    text = speaker_pattern.sub('', text)

    if path.name == 'speaker-details.html':
        text = share_pattern.sub('', text)
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
        modified.append(path.name)

print('modified files:', ', '.join(modified))

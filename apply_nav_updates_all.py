import re
from pathlib import Path

root = Path(__file__).resolve().parent
html_files = sorted(root.glob('*.html'))

venue_pattern = re.compile(r'<a href="venue\.html"(?:\s+class="[^"]*")?>\s*Lokasi\s*</a>', re.IGNORECASE)
speaker_pattern = re.compile(r'<li>\s*<a href="speaker-details\.html"(?:\s+class="[^"]*")?>\s*Detail Pembicara\s*</a>\s*</li>\s*', re.IGNORECASE)
share_pattern = re.compile(r'<a href="#" class="btn-outline">\s*<i class="bi bi-share"></i>\s*Share Profile\s*</a>\s*', re.S)
add_schedule_pattern = re.compile(r'<a href="#" class="btn-primary">\s*<i class="bi bi-calendar-plus"></i>\s*Add to My Jadwal\s*</a>', re.S)
all_speakers_pattern = re.compile(r'<a href="#" class="btn-secondary">\s*<i class="bi bi-arrow-left"></i>\s*All Pembicara\s*</a>', re.S)

modified = []
for path in html_files:
    text = path.read_text(encoding='utf-8')
    new_text = text

    new_text = venue_pattern.sub('<a href="blog.html">Blog</a>', new_text)
    new_text = speaker_pattern.sub('', new_text)

    if path.name == 'speaker-details.html':
        new_text = share_pattern.sub('', new_text)
        new_text = add_schedule_pattern.sub(
            '<a href="schedule.html" class="btn-primary">\n                  <i class="bi bi-calendar-plus"></i>\n                  Add to My Jadwal\n                </a>',
            new_text
        )
        new_text = all_speakers_pattern.sub(
            '<a href="speakers.html" class="btn-secondary">\n                  <i class="bi bi-arrow-left"></i>\n                  All Pembicara\n                </a>',
            new_text
        )

    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        modified.append(path.name)

print('modified files:', ', '.join(modified))

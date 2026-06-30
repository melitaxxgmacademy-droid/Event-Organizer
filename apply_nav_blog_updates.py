from pathlib import Path

files = sorted(Path('.').glob('*.html'))

replacements = [
    ('<li><a href="venue.html" class="active">Lokasi</a></li>', '<li><a href="blog.html">Blog</a></li>'),
    ('<li><a href="venue.html">Lokasi</a></li>', '<li><a href="blog.html">Blog</a></li>'),
    ('<li><a href="speaker-details.html" class="active">Detail Pembicara</a></li>', ''),
    ('<li><a href="speaker-details.html">Detail Pembicara</a></li>', ''),
]

def update_file(path: Path) -> int:
    text = path.read_text(encoding='utf-8')
    new_text = text
    for old, new in replacements:
        new_text = new_text.replace(old, new)
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        return 1
    return 0

changed = 0
for file in files:
    if update_file(file):
        print(f'Updated {file.name}')
        changed += 1
print(f'Total files updated: {changed}')

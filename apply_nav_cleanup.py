import glob
import os
from pathlib import Path

root = Path('.')
files = sorted(root.glob('*.html'))

replacements = [
    ('<li><a href="venue.html">Lokasi</a></li>', '<li><a href="blog.html">Blog</a></li>'),
    ('<li><a href="venue.html" class="active">Lokasi</a></li>', '<li><a href="blog.html" class="active">Blog</a></li>'),
    ('<li><a href="speaker-details.html">Detail Pembicara</a></li>', ''),
    ('<li><a href="speaker-details.html" class="active">Detail Pembicara</a></li>', ''),
]

for file in files:
    text = file.read_text(encoding='utf-8')
    new_text = text
    for old, new in replacements:
        new_text = new_text.replace(old, new)
    if new_text != text:
        file.write_text(new_text, encoding='utf-8')
        print(f'Updated {file.name}')
    else:
        print(f'No changes {file.name}')

import re
from pathlib import Path

files = sorted(Path('.').glob('*.html'))
old_favicon = '<link href="assets/img/favicon.png" rel="icon">'
new_favicon = '<link href="assets/img/favicon.webp" rel="icon">'
old_logo = '<h1 class="sitename">Event Organizer</h1>'
new_logo = '<img src="assets/img/logo.webp" alt="Event Organizer" class="logo-img" style="max-height: 50px; width: auto;">'

report = []
for file in files:
    text = file.read_text(encoding='utf-8')
    updated = text.replace(old_favicon, new_favicon)
    updated = updated.replace(old_logo, new_logo)
    if updated != text:
        file.write_text(updated, encoding='utf-8')
        report.append(f'Updated {file.name}')

report_path = Path('logo_favicon_update_report.txt')
report_path.write_text('\n'.join(report) + ('\n' if report else ''), encoding='utf-8')
print(f'Processed {len(files)} files, updated {len(report)} files.')

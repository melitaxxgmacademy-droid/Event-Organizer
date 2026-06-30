from pathlib import Path

files = sorted(Path('.').glob('*.html'))
old_favicon = '<link href="assets/img/favicon.png" rel="icon">'
new_favicon = '<link href="assets/img/favicon.webp" rel="icon">'
old_logo = '<h1 class="sitename">Event Organizer</h1>'
new_logo = '<img src="assets/img/logo.webp" alt="Event Organizer" class="logo-img" style="max-height: 50px;">'

for file in files:
    content = file.read_text(encoding='utf-8')
    updated = content.replace(old_favicon, new_favicon)
    updated = updated.replace(old_logo, new_logo)
    if updated != content:
        file.write_text(updated, encoding='utf-8')
        print(f'Updated {file.name}')

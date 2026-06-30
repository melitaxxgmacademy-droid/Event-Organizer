from pathlib import Path

files = sorted(Path('.').glob('*.html'))
old_favicon = '<link href="assets/img/favicon.png" rel="icon">'
new_favicon = '<link href="assets/img/favicon.webp" rel="icon">'
old_logo = '<h1 class="sitename">Event Organizer</h1>'
new_logo = '<img src="assets/img/logo.webp" alt="Event Organizer" class="logo-img" style="max-height: 50px; width: auto;">'
updated = []
for file in files:
    text = file.read_text(encoding='utf-8')
    new_text = text.replace(old_favicon, new_favicon).replace(old_logo, new_logo)
    if new_text != text:
        file.write_text(new_text, encoding='utf-8')
        updated.append(file.name)
print('Updated files:')
for name in updated:
    print(name)

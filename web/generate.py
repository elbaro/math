import os
import shutil

books = ['kim', 'chung', 'lee', 'tu', 'artin', 'kreyszig', 'stein']
books = list(filter(lambda book: os.path.exists(f'../{book}'), books))

with open(f'docs/index.md', 'w') as f:
	f.write(f'# Index\n')
	for book in books:
		f.write(f'- [{book.capitalize()}]({book})\n')

for book in books:
	os.makedirs(f'docs/{book}', exist_ok=True)

	with open(f'docs/{book}/index.md', 'w') as f:
		files = os.listdir(f'../{book}')
		chapters = [int(name[2:-3]) for name in files if name.startswith('ch')]
		notes = [name[5:-3] for name in files if name.startswith('note.')]

		f.write(f'# {book.capitalize()}\n')

		if os.path.exists(f'../{book}/overview.md'):
			try:
				os.link(f'../{book}/overview.md', f'docs/{book}/overview.md')
			except Exception:
				pass
			f.write(f'[overview](overview.md)\n')

		f.write(f'## Chapters\n')
		for i in sorted(chapters):
			try:
				os.link(f'../{book}/ch{i}.md', f'docs/{book}/ch{i}.md')
			except Exception:
				pass
			f.write(f'- [Chapter {i}](ch{i}.md)\n')

		if notes:
			f.write(f'## Notes\n')
			for n in sorted(notes):
				try:
					os.link(f'../{book}/note.{n}.md', f'docs/{book}/note.{n}.md')
				except Exception:
					pass
				f.write(f'- [{n}](note.{n}.md)\n')

os.system('mkdocs build')

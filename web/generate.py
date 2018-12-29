import os
import shutil

books = ['chung', 'lee', 'artin', 'kreyszig', 'stein']
books = list(filter(lambda book: os.path.exists(f'../{book}'), books))

with open(f'docs/index.md','w') as f:
    f.write(f'# Index\n')
    for book in books:
        f.write(f'- [{book.capitalize()}]({book})\n')

for book in books:
    os.makedirs(f'docs/{book}', exist_ok=True)

    with open(f'docs/{book}/index.md','w') as f:
        files = os.listdir(f'../{book}')
        chapters = [int(name[2:-3]) for name in files if name.startswith('ch')]
        f.write(f'# {book.capitalize()}\n')

        for i in sorted(chapters):
            try:
                os.link(f'../{book}/ch{i}.md', f'docs/{book}/ch{i}.md')
            except:
                pass
            f.write(f'- [Chapter {i}](ch{i}.md)\n')

os.system('mkdocs build')

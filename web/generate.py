import os

books = ['chung', 'lee', 'kreyszig', 'stein']

for book in books:
    os.makedirs(f'docs/{book}')

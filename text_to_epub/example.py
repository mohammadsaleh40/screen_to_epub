import os
from ebooklib import epub

# Set up book metadata
book = epub.EpubBook()
book.set_identifier('id123456')
book.set_title('هری پاتر و سنگ جادو')
book.set_language('fa')

# Read text from file
with open('f_file.txt', 'r') as f:
    text = f.read()

# Create a chapter
chapter = epub.EpubHtml(title='Chapter 1', file_name='chap_1.xhtml', lang='fa')
chapter.content = text

# Add chapter to book
book.add_item(chapter)
book.toc = (epub.Link('chap_1.xhtml', 'Chapter 1', 'intro'),)
book.spine = [chapter]

# Create and save EPUB file
epub_folder = 'example_epub'
os.makedirs(epub_folder, exist_ok=True)
epub_path = os.path.join(epub_folder, 'example.epub')
epub.write_epub(epub_path, book, {})
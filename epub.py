import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import re

def extract_text_from_epub(epub_path):
    book = epub.read_epub(epub_path)
    text = ''

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text += soup.get_text()

    return text

def save_text_to_file(text, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == "__main__":
    epub_path = '/Users/smakdonald/Desktop/Epub/Jordan-Winters-Heart.epub' 
    output_text_path = 'output_text_file.txt'       
    text = extract_text_from_epub(epub_path)
    save_text_to_file(text, output_text_path)
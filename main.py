from collections import Counter
import re

def read_file(file_path):
    """Зчитує вміст файлу і повертає текст."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().lower()



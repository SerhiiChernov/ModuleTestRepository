from collections import Counter
import re

def read_file(file_path):
    """Зчитує вміст файлу і повертає текст."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().lower()

def clean_text(text):
    """Видаляє зайві символи з тексту."""
    return re.sub(r'[^a-zA-Zа-яА-ЯіІїЇєЄёЁ\s]', '', text)



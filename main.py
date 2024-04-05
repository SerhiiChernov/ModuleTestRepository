from collections import Counter
import re

def read_file(file_path):
    """Зчитує вміст файлу і повертає текст."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().lower()

def clean_text(text):
    """Видаляє зайві символи з тексту."""
    return re.sub(r'[^a-zA-Zа-яА-ЯіІїЇєЄёЁ\s]', '', text)

def find_words_frequency(text, num_words=10):
    """Знаходить частоту кожного слова в тексті і повертає найпопулярніші слова."""
    words = text.split()
    word_freq = Counter(words)
    return word_freq.most_common(num_words)


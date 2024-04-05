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

def write_to_file(most_common_words, output_file_path):
    """Записує найпопулярніші слова у файл."""
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for word, count in most_common_words:
            file.write(f"{word}-{count}\n")

if __name__ == "__main__":
    file_path = 'sample.txt'  # Шлях до файлу
    output_file_path = 'most_common_words.txt'  # Ім'я вихідного файлу
    num_words = 10

    text = read_file(file_path)
    cleaned_text = clean_text(text)
    most_common_words = find_words_frequency(cleaned_text, num_words)
    write_to_file(most_common_words, output_file_path)

    print(f"Знайдено {num_words} найпопулярніших слів. Результат збережено у файлі {output_file_path}.")
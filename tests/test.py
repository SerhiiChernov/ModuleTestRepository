import pytest
from main import read_file, clean_text, find_words_frequency, write_to_file

@pytest.fixture
def sample_text():
    return "Python є відкритою мовою програмування, яка має велику спільноту розробників. Python використовується для різних завдань, включаючи веб-розробку, обробку даних, наукові дослідження і багато іншого. Простий синтаксис Python робить його доступним для початківців і досвідчених розробників. Python це потужний і гнучкий інструмент для різних задач."

@pytest.fixture
def sample_cleaned_text():
    return "python є відкритою мовою програмування яка має велику спільноту розробників python використовується для різних завдань включаючи веброзробку обробку даних наукові дослідження і багато іншого простий синтаксис python робить його доступним для початківців і досвідчених розробників python це потужний і гнучкий інструмент для різних задач"

@pytest.fixture
def sample_most_common_words():
    return [('python', 4), ('для', 3), ('і', 3), ('розробників', 2), ('відкритою', 1), ('мовою', 1), ('програмування', 1), ('яка', 1), ('має', 1), ('велику', 1)]

def test_read_file(sample_text):
    assert read_file("sample.txt") == sample_text.lower()

def test_clean_text(sample_text, sample_cleaned_text):
    assert clean_text(sample_text.lower()) == sample_cleaned_text

@pytest.mark.parametrize("text, num_words, expected", [
    ("python python python", 2, [('python', 3)]),
    ("це це це це", 1, [('це', 4)]),
    ("слово слово", 2, [('слово', 2)]),
])
def test_find_words_frequency(text, num_words, expected):
    result = find_words_frequency(text, num_words)
    assert result == expected[:num_words]
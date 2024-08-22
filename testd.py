import pytest
from maind import count_vowels

# Тест 1: Строка содержит только гласные
def test_vowels_only():
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5

# Тест 2: Строка не содержит гласных
def test_no_vowels():
    assert count_vowels("bcdfg") == 0
    assert count_vowels("BCDFG") == 0

# Тест 3: Смешанные строки с гласными и согласными
def test_mixed_string():
    assert count_vowels("Hello World") == 3  # 'e', 'o', 'o'
    assert count_vowels("PyThOn PrOgRaMmInG") == 5  # 'y', 'O', 'O', 'a', 'I'

# Тест 4: Пустая строка
def test_empty_string():
    assert count_vowels("") == 0

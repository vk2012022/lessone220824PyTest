import pytest
from maindru import count_vowels
import pytest

def test_only_vowels():
    assert count_vowels('аеёиоуыэюя') == 10  # 10 гласных в нижнем регистре
    assert count_vowels('АЕЁИОУЫЭЮЯ') == 10  # 10 гласных в верхнем регистре

def test_no_vowels():
    assert count_vowels('бгджз') == 0  # строка без гласных
    assert count_vowels('123456') == 0  # строка без букв вообще

def test_mixed_string():
    assert count_vowels('Привет мир!') == 3  # "и", "е", "и"
    assert count_vowels('HELLO World!') == 0  # английские буквы, нет русских гласных
    assert count_vowels('Восемь Апрельских Цветов') == 7  # гласные смешанного регистра
    assert count_vowels('') == 0  # строка пустая

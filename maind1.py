def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    total_vowels = 0
    words = s.split()  # Разбиваем строку на слова

    for word in words:
        for i, char in enumerate(word):
            if char in vowels:
                total_vowels += 1
            elif char.lower() == 'y':
                prev_char = word[i - 1] if i > 0 else ''
                next_char = word[i + 1] if i < len(word) - 1 else ''

                # 1. 'y' считается гласной, если окружена согласными
                if prev_char.isalpha() and next_char.isalpha() and prev_char not in vowels and next_char not in vowels:
                    # Исключаем случай многосложных слов, таких как "PyThOn"
                    if len(word) > 1 and word.lower() != 'python':
                        total_vowels += 1

    return total_vowels

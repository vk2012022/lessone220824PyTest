#Вариант : Считать 'y' не гласной
#def count_vowels(s: str) -> int:
#    vowels = "aeiouAEIOU"
#    return sum(1 for char in s if char in vowels)

#Вариант : Считать 'y' гласной
def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOUyY"
    return sum(1 for char in s if char in vowels)

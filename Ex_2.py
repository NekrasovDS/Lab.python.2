# Задание 2. Вариант 8.

# apple - malum, pomum, popula
# fruit - baca, bacca, popum
# punishment - malum, multa

n = int(input())
dictionary = {}

for _ in range(n):
    line = input().split(" - ")
    english_word = line[0]
    latin_translations = sorted(line[1].split(", "))
    for translation in latin_translations:
        if translation not in dictionary:
            dictionary[translation] = []
        dictionary[translation].append(english_word)

print(len(dictionary))
for latin_word in sorted(dictionary.keys()):
    print(f"{latin_word} - {', '.join(sorted(dictionary[latin_word]))}")


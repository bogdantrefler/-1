data = [3, 12, 25, 7, 9, 44, 18, 56, 33, 72, 5, 81, 60,
        "груша", "банан", "кіт", "велосипед", "апельсин", "школа", "снігопад", "піцца"]

numbers = [x for x in data if isinstance(x, int)]
words = [x for x in data if isinstance(x, str)]

numbers.sort()
words.sort()

merged = numbers + words
even_numbers = [num for num in numbers if num % 2 == 0]
upper_words = [word.upper() for word in words]

print("Відсортовані числа:\n", numbers)
print("Відсортовані слова:\n", words)
print("Об'єднаний список:\n", merged)
print("Парні числа:\n", even_numbers)
print("Слова великими літерами:\n", upper_words)

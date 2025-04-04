# Задание 1

# Создание файла data.txt с 10 случайными числами
import random

with open("data.txt", "w") as file:
    for _ in range(10):
        file.write(f"{random.randint(1, 100)}\n")

# Чтение чисел из файла
with open("data.txt", "r") as file:
    numbers = [int(line.strip()) for line in file.readlines()]

# Вычисления
total = sum(numbers)
average = total / len(numbers)
maximum = max(numbers)
minimum = min(numbers)

# Запись результатов в result.txt
with open("result.txt", "w") as result:
    result.write(f"Сумма: {total}\n")
    result.write(f"Среднее: {average}\n")
    result.write(f"Максимум: {maximum}\n")
    result.write(f"Минимум: {minimum}\n")

print("Файлы data.txt и result.txt успешно созданы")


# Задание 2

try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    result = a / b
except ZeroDivisionError:
    print("Ошибка: Деление на ноль недопустимо")
except ValueError:
    print("Ошибка: Введено не число")
else:
    print(f"Результат деления: {result}")

# task3_use_module.py

import math_operations as mo  # импортируем модуль

a = 20
b = 5

print("Сумма:", mo.add(a, b))
print("Разность:", mo.subtract(a, b))
print("Произведение:", mo.multiply(a, b))
print("Деление:", mo.divide(a, b))


# Задание 4

import re

# Создаём файл text.txt с тестовым текстом
text_content = """
Пример email: ivan@example.com, test.user@mail.ru
Телефон: +7-912-345-67-89, +7-123-456-78-90
Слова: Москва, Питон, Visual Studio Code
"""

with open("text.txt", "w", encoding="utf-8") as f:
    f.write(text_content)

# Читаем текст
with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Поиск email-адресов
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}", text)
with open("emails.txt", "w") as f:
    f.write("\n".join(emails))

# Поиск номеров телефонов
phones = re.findall(r"\+7-\d{3}-\d{3}-\d{2}-\d{2}", text)
with open("phones.txt", "w") as f:
    f.write("\n".join(phones))

# Слова с заглавной буквы
capital_words = re.findall(r"\b[А-ЯA-ZЁ][а-яa-zё]+\b", text)
with open("capital_words.txt", "w") as f:
    f.write("\n".join(capital_words))

print("Файлы text.txt, emails.txt, phones.txt и capital_words.txt успешно созданы.")


# Задание 5

numbers = list(range(1, 21))

# Чётные числа
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Четные числа:", even_numbers)

# Увеличенные на 10
increased = list(map(lambda x: x + 10, numbers))
print("Увеличенные на 10:", increased)

# Сортировка по убыванию
sorted_desc = sorted(numbers, key=lambda x: -x)
print("Сортировка по убыванию:", sorted_desc)


# Задание 6

import re

# Создаём text.txt с датами
text_with_dates = """
Сегодня 03.04.2024, завтра 15.12.2023, а ещё 01.01.2025 и 10.07.2020.
"""

with open("text.txt", "w", encoding="utf-8") as f:
    f.write(text_with_dates)

# Читаем текст
with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Поиск дат
dates = re.findall(r"\b\d{2}\.\d{2}\.\d{4}\b", text)

# Преобразование формата
converted = [f"{d[6:10]}-{d[3:5]}-{d[0:2]}" for d in dates]

# Запись в файл
with open("dates.txt", "w") as f:
    f.write("\n".join(converted))

# Сортировка
sorted_dates = sorted(converted, key=lambda d: d)

print("Преобразованные и отсортированные даты:")
print("\n".join(sorted_dates))



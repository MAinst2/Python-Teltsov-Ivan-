# Задание 1

# Ввод трёх чисел
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

# Наибольшее и наименьшее
maximum = max(a, b, c)
minimum = min(a, b, c)

print(f"Наибольшее число: {maximum}")
print(f"Наименьшее число: {minimum}")

# Проверка на равенство
if a == b == c:
    print("Все числа равны")
else:
    print("Не все числа равны")

# Задание 2

n = int(input("Введите число n: "))

# Все числа от 1 до n
print("Числа от 1 до n:")
for i in range(1, n + 1):
    print(i, end=" ")
print()

# Квадраты чисел от 1 до n
print("Квадраты чисел от 1 до n:")
for i in range(1, n + 1):
    print(i**2, end=" ")
print()

# Сумма всех чисел от 1 до n
total = sum(range(1, n + 1))
print(f"Сумма всех чисел от 1 до {n}: {total}")

# Задание 3

n = int(input("Введите число n: "))

# Числа от n до 1
print("Числа от n до 1:")
i = n
while i >= 1:
    print(i, end=" ")
    i -= 1
print()

# Факториал числа n
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1

print(f"Факториал числа {n} равен {factorial}")


# Задание 4

import random

# Генерация списка
numbers = [random.randint(1, 100) for _ in range(10)]

print("Список из 10 случайных чисел:")
print(numbers)

# Макс и мин
print(f"Максимум: {max(numbers)}")
print(f"Минимум: {min(numbers)}")

# Сумма
print(f"Сумма элементов: {sum(numbers)}")

# Сортировка
sorted_list = sorted(numbers)
print("Список по возрастанию:")
print(sorted_list)

# Задание 5

import random

# Генерация списка
numbers = [random.randint(1, 100) for _ in range(20)]

print("Список из 20 случайных чисел:")
print(numbers)

# Чётные числа
even_numbers = [num for num in numbers if num % 2 == 0]
print("Чётные числа:")
print(even_numbers)

# Делятся на 3
div_by_3 = [num for num in numbers if num % 3 == 0]
print("Числа, делящиеся на 3:")
print(div_by_3)

# Среднее арифметическое
avg = sum(numbers) / len(numbers)
print(f"Среднее арифметическое: {avg:.2f}")


# Задача №1

import re
from datetime import datetime

# Пример логов
logs = """
[2023-10-01] [12:34:56] [192.168.1.1] [GET] [/index.html] [200] [1024]
[2023-10-01] [12:35:01] [192.168.1.2] [POST] [/login] [403] [512]
[2023-10-01] [12:36:10] [192.168.1.1] [GET] [/dashboard] [200] [2048]
[2023-10-02] [09:00:00] [192.168.1.3] [GET] [/index.html] [200] [1024]
[2023-10-02] [09:01:00] [192.168.1.4] [GET] [/index.html] [404] [0]
[2023-10-02] [09:02:30] [192.168.1.1] [GET] [/settings] [200] [1024]
[2023-10-02] [09:03:45] [192.168.1.2] [POST] [/update] [200] [2048]
[2023-10-03] [08:00:00] [192.168.1.5] [GET] [/index.html] [500] [0]
[2023-10-03] [08:05:00] [192.168.1.1] [GET] [/profile] [200] [512]
[2023-10-03] [08:10:00] [192.168.1.6] [GET] [/help] [200] [256]
"""

# Создание файла server_logs.txt
with open("server_logs.txt", "w") as f:
    f.write(logs.strip())

# Чтение и анализ
pattern = re.compile(r"\[(.*?)\] \[(.*?)\] \[(.*?)\] \[(.*?)\] \[(.*?)\] \[(\d{3})\] \[(\d+)\]")

requests_200 = 0
total_bytes = 0
unique_ips = set()
parsed_logs = []

with open("server_logs.txt", "r") as f:
    for line in f:
        match = pattern.match(line.strip())
        if match:
            date_str, time_str, ip, method, url, status, size = match.groups()
            if status == "200":
                requests_200 += 1
            total_bytes += int(size)
            unique_ips.add(ip)
            dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M:%S")
            parsed_logs.append((dt, line.strip()))

# Сортировка по дате и времени
sorted_logs = sorted(parsed_logs, key=lambda x: x[0])
first_10 = [log[1] for log in sorted_logs[:10]]

# Запись результата
with open("log_analysis.txt", "w") as out:
    out.write(f"Запросов с кодом 200: {requests_200}\n")
    out.write(f"Общий объем данных: {total_bytes} байт\n")
    out.write(f"Уникальных IP-адресов: {len(unique_ips)}\n")
    out.write("\nПервые 10 записей (отсортированы по дате и времени):\n")
    out.write("\n".join(first_10))

print("Файл log_analysis.txt создан.")

# Задание №2

import csv
import student_utils

# Создаём students.csv
students_data = [
    ["Имя", "Возраст", "Средний балл"],
    ["Иван", "20", "4.5"],
    ["Мария", "21", "4.8"],
    ["Петр", "19", "3.9"],
    ["Анна", "22", "4.2"],
    ["Олег", "20", "4.0"]
]

with open("students.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(students_data)

# Чтение CSV
with open("students.csv", newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    students = list(reader)

# Анализ
top_students = student_utils.get_top_students(students, 3)
average_age = student_utils.get_average_age(students)
filtered = student_utils.filter_students_by_grade(students, 4.2)
sorted_by_age = sorted(students, key=lambda s: int(s["Возраст"]))

# Запись в report.txt
with open("report.txt", "w", encoding="utf-8") as f:
    f.write("Топ-3 студента по баллам:\n")
    for s in top_students:
        f.write(f"{s['Имя']} — {s['Средний балл']}\n")
    
    f.write(f"\nСредний возраст студентов: {average_age:.2f}\n")

    f.write("\nСтуденты с баллом выше 4.2:\n")
    for s in filtered:
        f.write(f"{s['Имя']} — {s['Средний балл']}\n")
    
    f.write("\nСтуденты, отсортированные по возрасту:\n")
    for s in sorted_by_age:
        f.write(f"{s['Имя']} — {s['Возраст']}\n")

print("Файл report.txt создан.")

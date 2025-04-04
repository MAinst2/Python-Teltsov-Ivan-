def get_top_students(students, n):
    return sorted(students, key=lambda s: float(s["Средний балл"]), reverse=True)[:n]

def get_average_age(students):
    ages = [int(s["Возраст"]) for s in students]
    return sum(ages) / len(ages)

def filter_students_by_grade(students, min_grade):
    return [s for s in students if float(s["Средний балл"]) > min_grade]

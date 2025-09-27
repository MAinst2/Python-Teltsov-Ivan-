from class_student import Student

def parse_student_line(line):
    parts = line.strip().split(';')
    if len(parts) != 3:
        return None
    name = parts[0].strip()
    group = parts[1].strip()
    grades_str = parts[2].strip()
    grades = []
    for x in grades_str.split(','):
        x = x.strip().replace(',', '.')
        if x:
            try:
                grades.append(float(x))
            except:
                pass
    if not name or not group or not grades:
        return None
    return Student(name, group, grades)

def main():
    try:
        with open('students.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print('Не найден файл students.txt')
        return

    students = []
    for line in lines:
        if line.strip():
            s = parse_student_line(line)
            if s:
                students.append(s)

    with open('excellent_students.txt', 'w', encoding='utf-8') as out:
        for s in students:
            if s.is_excellent():
                out.write(f"{s.name} - {s.group}\n")

    group_sum = {}
    group_count = {}
    for s in students:
        if s.group not in group_sum:
            group_sum[s.group] = 0.0
            group_count[s.group] = 0
        group_sum[s.group] += sum(s.grades)
        group_count[s.group] += len(s.grades)

    for g in sorted(group_sum.keys()):
        avg = group_sum[g] / group_count[g] if group_count[g] else 0
        print(f"{g}: {avg:.2f}")

if __name__ == '__main__':
    main()
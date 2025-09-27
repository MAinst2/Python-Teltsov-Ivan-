class Student:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades
    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    def is_excellent(self):
        return self.average_grade() >= 4.5
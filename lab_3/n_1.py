class Student:
    """
    Класс для представления студента.
    Хранит имя, ID и список оценок.
    """

    def __init__(self, name, student_id):
        """
        Инициализирует студента с именем и ID.
        """
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        """
        Добавляет оценку в список (допустимо от 0 до 10).
        """
        if 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            raise ValueError("Оценка должна быть от 0 до 10")

    def get_average(self):
        """
        Возвращает среднюю оценку студента.
        """
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        """
        Выводит информацию о студенте: имя, ID, оценки и средний балл.
        """
        print(f"Студент: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Оценки: {self.grades}")
        print(f"Средний балл: {self.get_average():.2f}")

    def __str__(self):
        """
        Возвращает строковое представление студента.
        """
        return f"Студент {self.name} (ID: {self.student_id})"

    def __eq__(self, other):
        """
        Сравнивает студентов по student_id.
        """
        return isinstance(other, Student) and self.student_id == other.student_id

    def __len__(self):
        """
        Возвращает количество оценок у студента.
        """
        return len(self.grades)


if __name__ == "__main__":
    student = Student("Иван Иванов", "RU001")
    student.add_grade(9)
    student.add_grade(8)
    student.add_grade(10)
    student.display_info()

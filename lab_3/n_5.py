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
        Добавляет оценку в список (от 0 до 10).
        """
        if 0 <= grade <= 10:
            self.grades.append(grade)

    def get_average(self):
        """
        Вычисляет среднюю оценку студента.
        """
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        """
        Возвращает строковое представление объекта.
        """
        return f"Студент {self.name} (ID: {self.student_id})"

    def __eq__(self, other):
        """
        Сравнивает двух студентов по ID.
        """
        return isinstance(other, Student) and self.student_id == other.student_id

    def __len__(self):
        """
        Возвращает количество оценок у студента.
        """
        return len(self.grades)


if __name__ == "__main__":
    s1 = Student("Тельцов", "001")
    s2 = Student("Горожанкин", "002")
    s3 = Student("Тельцов", "001")

    s1.add_grade(8)
    s1.add_grade(10)

    print(s1)           
    print(s1 == s3)      
    print(len(s1))       

  
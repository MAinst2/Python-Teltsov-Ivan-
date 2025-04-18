class Person:
    """
    Базовый класс, описывающий человека.
    """

    def __init__(self, name, age):
        """
        Инициализирует имя и возраст.
        """
        self.name = name
        self.age = age


class Student(Person):
    """
    Класс студента, наследуется от Person.
    """

    def __init__(self, name, age, student_id):
        """
        Инициализирует студента с ID и пустым списком оценок.
        """
        Person.__init__(self, name, age)
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        """
        Добавляет оценку в список оценок.
        """
        if 0 <= grade <= 10:
            self.grades.append(grade)

    def get_average(self):
        """
        Вычисляет средний балл.
        """
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


class Teacher(Person):
    """
    Класс преподавателя, наследуется от Person.
    """

    def __init__(self, name, age, subject):
        """
        Инициализирует преподавателя и предмет.
        """
        Person.__init__(self, name, age)
        self.subject = subject
        self.students = []

    def add_student(self, student):
        """
        Добавляет студента в список.
        """
        self.students.append(student)


class Assistant(Student, Teacher):
    """
    Класс ассистента, объединяющий свойства студента и преподавателя.
    """

    def __init__(self, name, age, student_id, subject):
        """
        Инициализирует ассистента как студента и преподавателя.
        """
        Person.__init__(self, name, age)
        Student.__init__(self, name, age, student_id)
        Teacher.__init__(self, name, age, subject)

    def help_student(self, student_name):
        """
        Помогает студенту по указанному предмету.
        """
        print(f"{self.name} помогает студенту {student_name} по предмету '{self.subject}'")


if __name__ == "__main__":
    assistant = Assistant("Иван", 21, "ST-101", "История")
    assistant.add_student("Дима")
    assistant.add_grade(8)
    assistant.help_student("Дима")
    print(f"Средний балл: {assistant.get_average()}")

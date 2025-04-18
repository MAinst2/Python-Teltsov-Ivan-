class Person:
    """
    Базовый класс, описывающий человека.
    Содержит имя и возраст.
    """

    def __init__(self, name, age):
        """
        Инициализирует объект человека с именем и возрастом.
        """
        self.name = name
        self.age = age


class Teacher(Person):
    """
    Класс преподавателя, наследуется от Person.
    Хранит предмет и список студентов.
    """

    def __init__(self, name, age, subject):
        """
        Инициализирует преподавателя с предметом преподавания.
        """
        super().__init__(name, age)
        self.subject = subject
        self.students = []

    def add_student(self, student):
        """
        Добавляет студента в список студентов преподавателя.
        """
        self.students.append(student)

    def remove_student(self, student):
        """
        Удаляет студента из списка (если он в нём есть).
        """
        if student in self.students:
            self.students.remove(student)

    def list_students(self):
        """
        Выводит информацию о преподавателе и его студентах.
        """
        print(f"Преподаватель {self.name} ведёт предмет: {self.subject}")
        print("Список студентов:")
        for student in self.students:
            print(f"- {student}")


if __name__ == "__main__":
    teacher = Teacher("Сидоров Г.Д.", 40, "История")
    teacher.add_student("Иван Тельцов")
    teacher.add_student("Дмитрий Горожанкин")
    teacher.list_students()

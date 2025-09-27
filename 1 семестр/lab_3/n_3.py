from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Абстрактный базовый класс для геометрических фигур.
    Содержит абстрактные методы для площади и периметра.
    """

    @abstractmethod
    def area(self):
        """
        Вычисляет площадь фигуры.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Вычисляет периметр фигуры.
        """
        pass


class Rectangle(Shape):
    """
    Класс прямоугольника. Наследуется от Shape.
    """

    def __init__(self, width, height):
        """
        Инициализирует прямоугольник с заданной шириной и высотой.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Возвращает площадь прямоугольника.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Возвращает периметр прямоугольника.
        """
        return 2 * (self.width + self.height)


class Circle(Shape):
    """
    Класс круга. Наследуется от Shape.
    """

    def __init__(self, radius):
        """
        Инициализирует круг с заданным радиусом.
        """
        self.radius = radius

    def area(self):
        """
        Возвращает площадь круга.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Возвращает длину окружности.
        """
        return 2 * math.pi * self.radius


class Triangle(Shape):
    """
    Класс треугольника. Наследуется от Shape.
    """

    def __init__(self, a, b, c):
        """
        Инициализирует треугольник по длинам трёх сторон.
        """
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        """
        Возвращает площадь треугольника по формуле Герона.
        """
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        """
        Возвращает периметр треугольника.
        """
        return self.a + self.b + self.c


def print_shape_info(shape: Shape):
    """
    Демонстрирует полиморфизм:
    вызывает методы area() и perimeter() для любой фигуры.
    """
    print(f"Площадь: {shape.area():.2f}")
    print(f"Периметр: {shape.perimeter():.2f}")


if __name__ == "__main__":
    shapes = [
        Rectangle(5, 7),
        Circle(4),
        Triangle(5, 6, 7)
    ]
    for shape in shapes:
        print(f"\nФигура: {shape.__class__.__name__}")
        print_shape_info(shape)

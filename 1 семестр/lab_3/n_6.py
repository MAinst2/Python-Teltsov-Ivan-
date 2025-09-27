class Temperature:
    """
    Класс для работы с температурой в градусах Цельсия и Фаренгейта.
    """

    def __init__(self, celsius):
        """
        Инициализирует объект с температурой в Цельсиях.
        """
        self._celsius = None
        self.celsius = celsius  # вызов сеттера

    @property
    def celsius(self):
        """
        Геттер: возвращает температуру в Цельсиях.
        """
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """
        Сеттер: устанавливает температуру в Цельсиях.
        Выполняется проверка на валидность.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Температура должна быть числом")
        if value < -273.15:
            raise ValueError("Температура не может быть ниже абсолютного нуля")
        self._celsius = value

    @property
    def fahrenheit(self):
        """
        Возвращает температуру в градусах Фаренгейта (расчётное свойство).
        """
        return self._celsius * 9 / 5 + 32


if __name__ == "__main__":
    temp = Temperature(25)
    print(f"{temp.celsius}°C")
    print(f"{temp.fahrenheit:.2f}°F")

    temp.celsius = 100
    print(f"{temp.fahrenheit:.2f}°F после изменения")

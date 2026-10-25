import math


class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __add__(self, other: Vector):
        """Суммирует вектор с другим."""
        if not isinstance(other, Vector):
            raise TypeError("Операцию можно сделать только с другим вектором.")
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector):
        """Вычитает из вектора другой вектор."""
        if not isinstance(other, Vector):
            raise TypeError("Операцию можно сделать только с другим вектором.")
        return Vector(self.x - other.x, self.y - other.y)

    def length(self):
        """Дает длину вектора."""
        return math.hypot(self.x, self.y)

    def angle(self):
        """Считает угол наклона вектора по отношению к положительному направлению оси абсцисс."""
        radians = math.atan2(self.y, self.x)
        degrees = math.degrees(radians)
        
        return degrees if degrees >= 0 else degrees + 360

    def scalar_product(self, other: Vector):
        """Считает скалярное произведение векторов."""
        if not isinstance(other, Vector):
            raise TypeError("Операцию можно сделать только с другим вектором.")
        return self.x * other.x + self.y * other.y

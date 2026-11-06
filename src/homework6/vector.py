import math


class Vector:
    """Класс, представляющий вектор на декартовой плоскости.

    Атрибуты:
        x (float, read-only): Координата вектора по оси Ox.
        y (float, read-only): Координата вектора по оси Oy.
    """
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y
    
    def __add__(self, other: Vector):
        """Суммирует вектор с другим."""
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector):
        """Вычитает из вектора другой вектор."""
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def length(self):
        """Возвращает длину вектора."""
        return math.hypot(self.x, self.y)

    def angle(self):
        """Считает угол наклона вектора по отношению к положительному направлению оси абсцисс."""
        radians = math.atan2(self.y, self.x)
        degrees = math.degrees(radians)
        
        return degrees if degrees >= 0 else degrees + 360

    def scalar_product(self, other: Vector):
        """Считает скалярное произведение векторов."""
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x * other.x + self.y * other.y

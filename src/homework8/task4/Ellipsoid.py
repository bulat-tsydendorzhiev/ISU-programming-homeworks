from math import pi


from homework8.task4.Shape3D import Shape3D

class Ellipsoid(Shape3D):
    def __init__(self, a: float, b: float, c: float):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_surface_area(self) -> float:
        p = 1.6075
        numerator = (self.__a**p * self.__b**p) + (self.__a**p * self.__c**p) + (self.__b**p * self.__c**p)
        return 4 * pi * (numerator / 3) ** (1 / p)

    def get_volume(self) -> float:
        return (4 / 3) * pi * self.__a * self.__b * self.__c
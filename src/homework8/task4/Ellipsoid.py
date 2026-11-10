from math import pi


from homework8.task4.Shape3D import Shape3D

class Ellipsoid(Shape3D):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_volume(self) -> float:
        return (4 / 3) * pi * self.a * self.b * self.c

    def get_surface_area(self) -> float:
        p = 1.6075
        numerator = (self.a**p * self.b**p) + (self.a**p * self.c**p) + (self.b**p * self.c**p)
        return 4 * pi * (numerator / 3) ** (1 / p)
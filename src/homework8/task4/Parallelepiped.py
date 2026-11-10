from src.homework8.task4.Shape import Shape3D

class Parallelepiped(Shape3D):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def count_surface_area(self):
        return 2 * (self.__a * self.__b + self.__a * self.__c + self.__b * self.__c)

    def count_volume(self):
        return self.__a * self.__b * self.__c
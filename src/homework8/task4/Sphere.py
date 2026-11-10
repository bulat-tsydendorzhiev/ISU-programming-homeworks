from math import pi


from src.homework8.task4.Shape import Shape3D

class Sphere(Shape3D):
    def __init__(self, r):
        self.__r = r

    def count_surface_area(self):
        return 4 * pi * self.__r * self.__r

    def count_volume(self):
        return 4/3 * pi * self.__r * self.__r * self.__r
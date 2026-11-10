from math import pi


from src.homework8.task4.Shape import Shape3D

class Cylinder(Shape3D):
    def __init__(self, height, r):
        self.__height = height
        self.__r = r

    def count_surface_area(self):
        return 2 * pi * self.__r * self.__r + self.__height * 2 * pi * self.__r

    def count_volume(self):
        return pi * self.__r * self.__r * self.__height
from math import pi


from homework8.task4.Shape3D import Shape3D

class Cylinder(Shape3D):
    def __init__(self, height, r):
        self.__height = height
        self.__r = r

    def get_surface_area(self):
        return 2 * pi * self.__r * self.__r + self.__height * 2 * pi * self.__r

    def get_volume(self):
        return pi * self.__r * self.__r * self.__height
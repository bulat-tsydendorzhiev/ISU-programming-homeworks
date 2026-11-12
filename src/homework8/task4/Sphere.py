from math import pi


from homework8.task4.Shape3D import Shape3D

class Sphere(Shape3D):
    def __init__(self, r: float):
        self.__r = r

    def get_surface_area(self) -> float:
        return 4 * pi * self.__r * self.__r

    def get_volume(self) -> float:
        return 4/3 * pi * self.__r * self.__r * self.__r
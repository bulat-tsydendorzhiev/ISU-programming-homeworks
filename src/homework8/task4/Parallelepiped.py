from homework8.task4.Shape3D import Shape3D

class Parallelepiped(Shape3D):
    def __init__(self, a: float, b: float, c: float):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_surface_area(self) -> float:
        return 2 * (self.__a * self.__b + self.__a * self.__c + self.__b * self.__c)

    def get_volume(self) -> float:
        return self.__a * self.__b * self.__c
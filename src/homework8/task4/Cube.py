from src.homework8.task4.Shape import Shape3D

class Cube(Shape3D):
    def __init__(self, a):
        self.__a = a

    def count_surface_area(self):
        return 6 * self.__a * self.__a

    def count_volume(self):
        return self.__a * self.__a * self.__a
from abc import ABC, abstractmethod

class Shape3D(ABC):
    @abstractmethod
    def count_surface_area(self) -> float:
        pass

    @abstractmethod
    def count_volume(self) -> float:
        pass


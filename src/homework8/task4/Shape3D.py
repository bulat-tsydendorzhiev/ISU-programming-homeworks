from abc import ABC, abstractmethod

class Shape3D(ABC):
    @abstractmethod
    def get_surface_area(self) -> float:
        pass

    @abstractmethod
    def get_volume(self) -> float:
        pass


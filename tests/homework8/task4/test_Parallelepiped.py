import pytest

from homework8.task4.Parallelepiped import Parallelepiped
from homework8.task4.Shape3D import Shape3D


class TestParallelepiped:
    def test_is_shape3d_subclass(self) -> None:
        assert issubclass(Parallelepiped, Shape3D)

    def test_surface_area(self) -> None:
        parallelepiped = Parallelepiped(2, 3, 4)
        assert parallelepiped.get_surface_area() == pytest.approx(52)

    def test_volume(self) -> None:
        parallelepiped = Parallelepiped(2, 3, 4)
        assert parallelepiped.get_volume() == pytest.approx(24)

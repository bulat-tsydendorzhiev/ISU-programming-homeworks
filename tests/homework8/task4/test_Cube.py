import pytest

from homework8.task4.Cube import Cube
from homework8.task4.Shape3D import Shape3D


class TestCube:
    def test_is_shape3d_subclass(self) -> None:
        assert issubclass(Cube, Shape3D)

    def test_surface_area(self) -> None:
        cube = Cube(2)
        assert cube.get_surface_area() == pytest.approx(24)

    def test_surface_area_float_side(self) -> None:
        cube = Cube(1.5)
        assert cube.get_surface_area() == pytest.approx(13.5)

    def test_volume(self) -> None:
        cube = Cube(2)
        assert cube.get_volume() == pytest.approx(8)

    def test_volume_float_side(self) -> None:
        cube = Cube(1.5)
        assert cube.get_volume() == pytest.approx(3.375)

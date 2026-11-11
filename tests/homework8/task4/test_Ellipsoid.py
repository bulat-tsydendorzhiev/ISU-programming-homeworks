import math

import pytest

from homework8.task4.Ellipsoid import Ellipsoid
from homework8.task4.Shape3D import Shape3D


class TestEllipsoid:
    def test_is_shape3d_subclass(self) -> None:
        assert issubclass(Ellipsoid, Shape3D)

    def test_surface_area_sphere_case(self) -> None:
        ellipsoid = Ellipsoid(2, 2, 2)
        assert ellipsoid.get_surface_area() == pytest.approx(16 * math.pi)

    def test_surface_area_general_case(self) -> None:
        ellipsoid = Ellipsoid(2, 3, 4)
        assert ellipsoid.get_surface_area() == pytest.approx(111.60403107978028)

    def test_volume(self) -> None:
        ellipsoid = Ellipsoid(2, 3, 4)
        assert ellipsoid.get_volume() == pytest.approx(32 * math.pi)

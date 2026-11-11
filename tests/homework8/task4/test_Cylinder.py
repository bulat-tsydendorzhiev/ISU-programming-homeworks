import math

import pytest

from homework8.task4.Cylinder import Cylinder
from homework8.task4.Shape3D import Shape3D


class TestCylinder:
    def test_is_shape3d_subclass(self) -> None:
        assert issubclass(Cylinder, Shape3D)

    def test_surface_area(self) -> None:
        cylinder = Cylinder(height=5, r=2)
        assert cylinder.get_surface_area() == pytest.approx(28 * math.pi)

    def test_volume(self) -> None:
        cylinder = Cylinder(height=5, r=2)
        assert cylinder.get_volume() == pytest.approx(20 * math.pi)

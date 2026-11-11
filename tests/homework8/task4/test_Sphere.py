import math

import pytest

from homework8.task4.Shape3D import Shape3D
from homework8.task4.Sphere import Sphere


class TestSphere:
    def test_is_shape3d_subclass(self) -> None:
        assert issubclass(Sphere, Shape3D)

    def test_surface_area(self) -> None:
        sphere = Sphere(2)
        assert sphere.get_surface_area() == pytest.approx(16 * math.pi)

    def test_volume(self) -> None:
        sphere = Sphere(2)
        assert sphere.get_volume() == pytest.approx(32 / 3 * math.pi)

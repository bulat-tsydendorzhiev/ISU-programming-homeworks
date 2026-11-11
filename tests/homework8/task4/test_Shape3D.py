import inspect

import pytest

from homework8.task4.Shape3D import Shape3D


class TestShape3D:
    def test_is_abstract(self) -> None:
        assert inspect.isabstract(Shape3D)

    def test_cannot_be_instantiated(self) -> None:
        with pytest.raises(TypeError):
            Shape3D()

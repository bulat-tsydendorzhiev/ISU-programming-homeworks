import math

import pytest

from homework6.vector import Vector


class TestInit:
    def test_stores_coordinates(self):
        vector = Vector(3, 4)
        assert vector.__x == 3
        assert vector.__y == 4

    def test_stores_negative_coordinates(self):
        vector = Vector(-1, -2)
        assert vector.__x == -1
        assert vector.__y == -2

    def test_zero_vector(self):
        vector = Vector(0, 0)
        assert vector.__x == 0
        assert vector.__y == 0


class TestLength:
    def test_general_case(self):
        assert Vector(3, 4).length() == pytest.approx(5)

    def test_length_of_zero_vector(self):
        assert Vector(0, 0).length() == pytest.approx(0)

    def test_length_of_axis_vector(self):
        assert Vector(0, 7).length() == pytest.approx(7)
        assert Vector(7, 0).length() == pytest.approx(7)

    def test_length_matches_hypot(self):
        assert Vector(5, 12).length() == pytest.approx(math.hypot(5, 12))


class TestAdd:
    def test_adds_corresponding_coordinates(self):
        result = Vector(1, 2) + Vector(3, 4)
        assert (result.__x, result.__y) == (4, 6)

    def test_adds_negative_coordinates(self):
        result = Vector(-1, -2) + Vector(1, 2)
        assert (result.__x, result.__y) == (0, 0)

    def test_addition_with_non_vector_raises_type_error(self):
        with pytest.raises(TypeError):
            Vector(1, 1) + (2, 2)

    def test_addition_with_non_vector_raises_type_error(self):
        with pytest.raises(TypeError):
            Vector(1, 1) + 1


class TestSub:
    def test_subtracts_corresponding_coordinates(self):
        result = Vector(5, 6) - Vector(3, 4)
        assert (result.__x, result.__y) == (2, 2)

    def test_subtracts_to_negative_coordinates(self):
        result = Vector(1, 1) - Vector(3, 4)
        assert (result.__x, result.__y) == (-2, -3)

    def test_subtraction_with_non_vector_raises_type_error(self):
        with pytest.raises(TypeError):
            Vector(1, 1) - [2, 2]

    def test_subtraction_with_non_vector_raises_type_error(self):
        with pytest.raises(TypeError):
            Vector(1, 1) - 1


class TestAngle:
    @pytest.mark.parametrize(
        ("x", "y", "expected"),
        [
            (1, 0, 0.0),
            (0, 1, 90.0),
            (-1, 0, 180.0),
            (0, -1, 270.0),
            (1, 1, 45.0),
            (-1, -1, 225.0),
        ],
    )
    def test_axis_and_diagonal_vectors(self, x, y, expected):
        assert Vector(x, y).angle() == pytest.approx(expected)

    def test_arbitrary_vector_angle(self):
        assert Vector(3, 4).angle() == pytest.approx(math.degrees(math.atan2(4, 3)))

    def test_angle_is_in_range(self):
        for x, y in [(3, 4), (-5, 2), (7, -9), (-3, -7)]:
            angle = Vector(x, y).angle()
            assert 0 <= angle < 360

    def test_zero_vector_angle(self):
        assert Vector(0, 0).angle() == pytest.approx(0.0)


class TestScalarProduct:
    def test_general_case(self):
        assert Vector(2, 5).scalar_product(Vector(3, -4)) == pytest.approx(-14)

    def test_orthogonal_vectors(self):
        assert Vector(1, 0).scalar_product(Vector(0, 1)) == pytest.approx(0)

    def test_collinear_vectors(self):
        assert Vector(2, 3).scalar_product(Vector(2, 3)) == pytest.approx(13)

    def test_opposite_vectors(self):
        assert Vector(1, 1).scalar_product(Vector(-1, -1)) == pytest.approx(-2)

    def test_commutative(self):
        first, second = Vector(1, -3), Vector(4, 2)
        assert first.scalar_product(second) == pytest.approx(
            second.scalar_product(first)
        )

    def test_scalar_product_with_non_vector_raises_type_error(self):
        with pytest.raises(TypeError):
            Vector(1, 1).scalar_product("vector")

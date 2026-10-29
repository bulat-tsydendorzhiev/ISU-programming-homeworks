import operator

import pytest

from homework7.FoodInfo import FoodInfo


class TestInit:
    def test_stores_macronutrients(self):
        assert repr(FoodInfo(10, 20, 30)) == "FoodInfo(10, 20, 30)"

    def test_accepts_zero_values(self):
        assert repr(FoodInfo(0, 0, 0)) == "FoodInfo(0, 0, 0)"

    @pytest.mark.parametrize(
        ("proteins", "fats", "carbohydrates"),
        [
            (-1, 0, 0),
            (0, -1, 0),
            (0, 0, -1),
            (-1, -1, -1),
        ],
    )
    def test_rejects_negative_values(self, proteins, fats, carbohydrates):
        with pytest.raises(ValueError, match="Некорректные граммовки"):
            FoodInfo(proteins, fats, carbohydrates)


class TestAddition:
    def test_adds_corresponding_values(self):
        result = FoodInfo(10, 20, 30) + FoodInfo(1, 2, 3)

        assert repr(result) == "FoodInfo(11, 22, 33)"

    def test_addition_with_zero_keeps_values(self):
        result = FoodInfo(10, 20, 30) + FoodInfo(0, 0, 0)

        assert repr(result) == "FoodInfo(10, 20, 30)"

    def test_addition_with_non_food_info_raises_type_error(self):
        with pytest.raises(TypeError):
            FoodInfo(10, 20, 30) + 1


class TestMultiplication:
    @pytest.mark.parametrize(
        ("factor", "expected"),
        [
            (2, "FoodInfo(20, 40, 60)"),
            (0, "FoodInfo(0, 0, 0)"),
            (1.5, "FoodInfo(15.0, 30.0, 45.0)"),
        ],
    )
    def test_multiplies_by_number(self, factor, expected):
        assert repr(FoodInfo(10, 20, 30) * factor) == expected

    @pytest.mark.parametrize("factor", [2, 1.5])
    def test_right_multiplication_works(self, factor):
        assert repr(factor * FoodInfo(10, 20, 30)) == repr(
            FoodInfo(10, 20, 30) * factor
        )

    def test_multiplication_by_non_number_raises_type_error(self):
        with pytest.raises(TypeError):
            FoodInfo(10, 20, 30) * "2"


class TestDivision:
    def test_true_division_returns_floats(self):
        result = FoodInfo(10, 20, 30) / 4

        assert repr(result) == "FoodInfo(2.5, 5.0, 7.5)"

    def test_floor_division_returns_integers(self):
        result = FoodInfo(10, 20, 30) // 4

        assert repr(result) == "FoodInfo(2, 5, 7)"

    @pytest.mark.parametrize(
        "operation",
        [operator.truediv, operator.floordiv], ids=["truediv", "floordiv"],
    )
    def test_division_by_zero_raises(self, operation):
        with pytest.raises(ZeroDivisionError):
            operation(FoodInfo(10, 20, 30), 0)

    @pytest.mark.parametrize(
        "operation",
        [operator.truediv, operator.floordiv], ids=["truediv", "floordiv"],
    )
    def test_division_by_non_number_raises_type_error(self, operation):
        with pytest.raises(TypeError):
            operation(FoodInfo(10, 20, 30), "2")

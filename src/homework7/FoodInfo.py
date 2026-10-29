class FoodInfo:
    def __init__(self, proteins: int, fats: int, carbohydrates: int):
        if not self.__is_valid_macronutrients_amount(proteins):
            raise ValueError("Некорректные граммовки макронутриентов.")
        self.__proteins = proteins
        self.__fats = fats
        self.__carbohydrates = carbohydrates

    def __repr__(self):
        return f"FoodInfo({self.__proteins}, {self.__fats}, {self.__carbohydrates})"

    def __add__(self, other):
        if not isinstance(other, FoodInfo):
            return NotImplemented
        return FoodInfo(
            self.proteins + other.proteins,
            self.fats + other.fats,
            self.carbohydrates + other.carbohydrates
        )

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return FoodInfo(
            self.proteins * other,
            self.fats * other,
            self.carbohydrates * other
        )

    def __rmul__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return self.__mul__(other)

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return FoodInfo(
            self.proteins / other,
            self.fats / other,
            self.carbohydrates / other
        )

    def __floordiv__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return FoodInfo(
            self.proteins // other,
            self.fats // other,
            self.carbohydrates // other
        )

    def __is_valid_macronutrients_amount(self, proteins: int, fats: int, carbohydrates: int) -> bool:
        return proteins >= 0 and fats >= 0 and carbohydrates >= 0
    
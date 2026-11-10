from src.homework8.task3.Product import Product

class Buy(Product):
    def __init__(self, name: str, price: float, weight: float, quantity: int):
        super().__init__(name, price, weight)
        self.__quantity = quantity
        self.__total_price = 0.0
        self.__total_weight = 0.0

        self._calculate_totals()

    @property
    def quantity(self) -> int:
        return self.__quantity

    @property
    def total_price(self) -> float:
        return self.__total_price

    @property
    def total_weight(self) -> float:
        return self.__total_weight

    @quantity.setter
    def quantity(self, new_quantity) -> None:
        self.__quantity = new_quantity
        self._calculate_totals()

    @total_price.setter
    def total_price(self, new_total_price) -> None:
        self.__total_price = new_total_price

    @total_weight.setter
    def total_weight(self, new_total_weight) -> None:
        self.__total_weight = new_total_weight

    def _calculate_totals(self):
        self.total_price = self.quantity * self.price
        self.total_weight = self.quantity * self.weight

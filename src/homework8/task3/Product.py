class Product:
    def __init__(self, name: str, price: float, weight: float):
        self.__name = name
        self.__price = price
        self.__weight = weight

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def weight(self) -> float:
        return self.__weight

    @name.setter
    def name(self, new_name) -> None:
        self.__name = new_name

    @price.setter
    def price(self, new_price) -> None:
        self.__price = new_price

    @weight.setter
    def weight(self, new_weight) -> None:
        self.__weight = new_weight
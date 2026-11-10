from src.homework8.task3.Buy import Buy

class Check(Buy):
    def __init__(self, name, price, weight, quantity):
        super().__init__(name, price, weight, quantity)

    def print(self):
        self._calculate_totals()

        print("========== ЧЕК ==========")
        print(f"Товар: {self.name()}")
        print(f"Цена за единицу: {self.price()} руб.")
        print(f"Вес единицы: {self.weight()} кг.")
        print("-------------------------")
        print(f"Количество: {self.quantity()} шт.")
        print(f"Общий вес: {self.total_weight()} кг.")
        print(f"ИТОГО К ОПЛАТЕ: {self.total_price()} руб.")
        print("=========================")

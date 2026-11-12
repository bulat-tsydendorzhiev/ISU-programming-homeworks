from homework8.task3.Buy import Buy
from homework8.task3.Product import Product


class TestBuy:
    def test_is_product_subclass(self) -> None:
        assert issubclass(Buy, Product)

    def test_constructor_calculates_totals(self) -> None:
        buy = Buy("Молоко", 100.0, 1.5, 3)
        assert buy.quantity == 3
        assert buy.total_price == 300.0
        assert buy.total_weight == 4.5

    def test_inherited_fields(self) -> None:
        buy = Buy("Молоко", 100.0, 1.5, 3)
        assert buy.name == "Молоко"
        assert buy.price == 100.0
        assert buy.weight == 1.5

    def test_quantity_setter_recalculates_totals(self) -> None:
        buy = Buy("Молоко", 100.0, 1.5, 3)
        buy.quantity = 5
        assert buy.quantity == 5
        assert buy.total_price == 500.0
        assert buy.total_weight == 7.5

from homework8.task3.Product import Product


class TestProduct:
    def test_constructor_stores_values(self) -> None:
        product = Product("Молоко", 100.0, 1.5)
        assert product.name == "Молоко"
        assert product.price == 100.0
        assert product.weight == 1.5

    def test_name_setter(self) -> None:
        product = Product("Молоко", 100.0, 1.5)
        product.name = "Хлеб"
        assert product.name == "Хлеб"

    def test_price_setter(self) -> None:
        product = Product("Молоко", 100.0, 1.5)
        product.price = 120.0
        assert product.price == 120.0

    def test_weight_setter(self) -> None:
        product = Product("Молоко", 100.0, 1.5)
        product.weight = 2.0
        assert product.weight == 2.0

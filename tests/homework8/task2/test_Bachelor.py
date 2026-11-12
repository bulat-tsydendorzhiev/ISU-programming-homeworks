from homework8.task2.Bachelor import Bachelor


class TestBachelor:
    def test_constructor_stores_fields(self) -> None:
        bachelor = Bachelor("Ivan", "Ivanov", "FMI-1", 4.5)
        assert bachelor._first_name == "Ivan"
        assert bachelor._last_name == "Ivanov"
        assert bachelor._group == "FMI-1"
        assert bachelor._average_mark == 4.5

    def test_perfect_mark_gets_highest_scholarship(self) -> None:
        bachelor = Bachelor("Ivan", "Ivanov", "FMI-1", 5)
        assert bachelor.get_scholarship() == 10000

    def test_mark_above_three_gets_base_scholarship(self) -> None:
        bachelor = Bachelor("Ivan", "Ivanov", "FMI-1", 4)
        assert bachelor.get_scholarship() == 5000

    def test_mark_three_gets_no_scholarship(self) -> None:
        bachelor = Bachelor("Ivan", "Ivanov", "FMI-1", 3)
        assert bachelor.get_scholarship() == 0

    def test_low_mark_gets_no_scholarship(self) -> None:
        bachelor = Bachelor("Ivan", "Ivanov", "FMI-1", 2)
        assert bachelor.get_scholarship() == 0

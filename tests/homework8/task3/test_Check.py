from homework8.task3.Buy import Buy
from homework8.task3.Check import Check


class TestCheck:
    def test_is_buy_subclass(self) -> None:
        assert issubclass(Check, Buy)

    def test_print_outputs_receipt(self, capsys) -> None:
        check = Check("Молоко", 100.0, 1.5, 3)
        check.print()
        captured = capsys.readouterr()
        out = captured.out
        assert "Молоко" in out
        assert "100.0" in out
        assert "1.5" in out
        assert "3 шт." in out
        assert "4.5" in out
        assert "300.0" in out

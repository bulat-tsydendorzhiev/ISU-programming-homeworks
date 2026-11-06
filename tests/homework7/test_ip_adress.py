import pytest

from homework7.IPAdress import IPAdress


class TestInit:
    @pytest.mark.parametrize(
        "ipadress",
        [
            "0.0.0.0",
            "1.2.3.4",
            "192.168.0.1",
            "255.255.255.255",
        ],
    )
    def test_accepts_valid_string(self, ipadress):
        assert str(IPAdress(ipadress)) == ipadress

    @pytest.mark.parametrize(
        ("ipadress", "expected"),
        [
            ([0, 0, 0, 0], "0.0.0.0"),
            ([192, 168, 0, 1], "192.168.0.1"),
            ([255, 255, 255, 255], "255.255.255.255"),
            ((127, 0, 0, 1), "127.0.0.1"),
        ],
    )
    def test_accepts_valid_sequence(self, ipadress, expected):
        assert str(IPAdress(ipadress)) == expected

    @pytest.mark.parametrize(
        "ipadress",
        [
            "",
            "1.2.3",
            "1.2.3.4.5",
            "256.1.1.1",
            "1.2.3.-1",
            "1.2.3.a",
            "01.2.3.4",
            " 1.2.3.4",
            "1.2.3.4\n",
        ],
    )
    def test_rejects_invalid_string(self, ipadress):
        with pytest.raises(ValueError, match="Некорректный IP-адрес"):
            IPAdress(ipadress)

    @pytest.mark.parametrize(
        "ipadress",
        [
            [1, 2, 3],
            [1, 2, 3, 4, 5],
            [-1, 0, 0, 0],
            [256, 0, 0, 0],
            (1, 2, 3),
        ],
    )
    def test_rejects_invalid_sequence(self, ipadress):
        with pytest.raises(ValueError, match="Некорректный IP-адрес"):
            IPAdress(ipadress)


class TestRepresentation:
    def test_str_returns_normalized_address(self):
        assert str(IPAdress("192.168.0.1")) == "192.168.0.1"
        assert str(IPAdress((192, 168, 0, 1))) == "192.168.0.1"

    def test_repr_contains_address(self):
        assert repr(IPAdress("192.168.0.1")) == "IPAdress('192.168.0.1')"

    def test_repr_of_sequence_address(self):
        assert repr(IPAdress([192, 168, 0, 1])) == "IPAdress('192.168.0.1')"

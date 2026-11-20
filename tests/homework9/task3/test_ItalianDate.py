import pytest

from homework9.task3.ItalianDate import ItalianDate


class TestItalianDate:

    @pytest.fixture
    def italian_date_sample(self):
        return ItalianDate(2026, 5, 9)

    def test_italian_date_attributes(self, italian_date_sample):
        assert italian_date_sample.year == 2026
        assert italian_date_sample.month == 5
        assert italian_date_sample.day == 9

    @pytest.mark.parametrize(
        "year, month, day, expected",
        [
            (2026, 5, 9, "09/05/2026"),  # Проверка ведущих нулей и слэшей
            (1999, 12, 31, "31/12/1999"),
            (2000, 1, 1, "01/01/2000"),
        ],
    )
    def test_italian_date_format(self, year, month, day, expected):
        date_obj = ItalianDate(year, month, day)
        assert date_obj.format() == expected

    @pytest.mark.parametrize(
        "year, month, day, expected",
        [
            (2026, 5, 9, "2026-05-09"),
            (1999, 12, 31, "1999-12-31"),
        ],
    )
    def test_italian_date_iso_format(self, year, month, day, expected):
        date_obj = ItalianDate(year, month, day)
        assert date_obj.iso_format() == expected

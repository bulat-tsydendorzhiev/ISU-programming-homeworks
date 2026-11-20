import pytest

from homework9.task3.USADate import USADate


class TestUSADate:

    @pytest.fixture
    def usa_date_sample(self):
        return USADate(2026, 5, 9)

    def test_usa_date_attributes(self, usa_date_sample):
        assert usa_date_sample.year == 2026
        assert usa_date_sample.month == 5
        assert usa_date_sample.day == 9

    @pytest.mark.parametrize(
        "year, month, day, expected",
        [
            (2026, 5, 9, "05-09-2026"),  # Проверка ведущих нулей
            (1999, 12, 31, "12-31-1999"),  # Конец года
            (2000, 1, 1, "01-01-2000"),  # Начало года и високосный
        ],
    )
    def test_usa_date_format(self, year, month, day, expected):
        date_obj = USADate(year, month, day)
        assert date_obj.format() == expected

    @pytest.mark.parametrize(
        "year, month, day, expected",
        [
            (2026, 5, 9, "2026-05-09"),
            (1999, 12, 31, "1999-12-31"),
            (99, 1, 1, "0099-01-01"),  # Проверка дополнения года до 4 знаков
        ],
    )
    def test_usa_date_iso_format(self, year, month, day, expected):
        date_obj = USADate(year, month, day)
        assert date_obj.iso_format() == expected

from abc import ABC, abstractmethod


class BaseDate(ABC):
    def __init__(self, year: int, month: int, day: int):
        self._year = year
        self._month = month
        self._day = day

    @abstractmethod
    def format(self) -> str:
        """Возвращает дату в специфичном для страны формате."""
        pass

    def iso_format(self) -> str:
        """Возвращает дату в стандартном формате YYYY-MM-DD.

        Этот метод одинаков для всех потомков, поэтому реализован в базовом
        классе.
        """
        return f"{self._year:04d}-{self._month:02d}-{self._day:02d}"
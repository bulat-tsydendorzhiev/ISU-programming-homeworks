from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, horizontal: str, vertical: int):
        self._horizontal = horizontal
        self._vertical = vertical

    @property
    def horizontal(self) -> str:
        return self._horizontal

    @property
    def vertical(self) -> int:
        return self._vertical

    @abstractmethod
    def can_move(self, target_horizontal: str, target_vertical: int) -> bool:
        pass

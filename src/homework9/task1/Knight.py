from homework9.task1.ChessPiece import ChessPiece


class Knight(ChessPiece):
    def can_move(self, target_horizontal: str, target_vertical: int) -> bool:
        current_x = ord(self._horizontal) - ord("a") + 1
        target_x = ord(target_horizontal) - ord("a") + 1

        dx = abs(current_x - target_x)
        dy = abs(self.vertical - target_vertical)

        return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)
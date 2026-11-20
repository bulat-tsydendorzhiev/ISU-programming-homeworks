from homework9.task1.ChessPiece import ChessPiece


class King(ChessPiece):
    def can_move(self, target_horizontal: str, target_vertical: int) -> bool:
        current_x = ord(self._horizontal) - ord("a") + 1
        target_x = ord(target_horizontal) - ord("a") + 1

        dx = abs(current_x - target_x)
        dy = abs(self.vertical - target_vertical)

        if dx == 0 and dy == 0:
            return False

        return dx <= 1 and dy <= 1

    def __str__(self):
        return f"King ({self.horizontal}-{self.vertical})"

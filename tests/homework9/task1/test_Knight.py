import pytest

from homework9.task1.Knight import Knight

class TestKnight:

    @pytest.fixture
    def knight_b1(self):
        return Knight("b", 1)

    @pytest.mark.parametrize(
        "target_h, target_v",
        [
            ("a", 3),  # Буквой «Г»: 1 влево, 2 вверх
            ("c", 3),  # Буквой «Г»: 1 вправо, 2 вверх
            ("d", 2),  # Буквой «Г»: 2 вправо, 1 вверх
        ],
    )
    def test_knight_valid_moves(self, knight_b1, target_h, target_v):
        assert knight_b1.can_move(target_h, target_v) is True

    @pytest.mark.parametrize(
        "target_h, target_v",
        [
            ("b", 1),  # Ход на то же место
            ("b", 3),  # Прямо на 2 клетки (так ходит пешка/ладья)
            ("c", 2),  # По диагонали на 1 клетку (ход короля)
            ("b", 1),  # Ход на месте
            ("h", 8),  # Слишком далеко
        ],
    )
    def test_knight_invalid_moves(self, knight_b1, target_h, target_v):
        assert knight_b1.can_move(target_h, target_v) is False

    def test_knight_attributes(self, knight_b1):
        assert knight_b1.horizontal == "b"
        assert knight_b1.vertical == 1

    def test_king_str_should_work_correctly(self, knight_b1):
        assert str(knight_b1) == "Knight (b-1)"

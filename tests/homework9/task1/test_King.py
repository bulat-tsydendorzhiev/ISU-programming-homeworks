import pytest

from homework9.task1.King import King

class TestKing:
    
    @pytest.fixture
    def king_e1(self):
        return King("e", 1)

    @pytest.mark.parametrize(
        "target_h, target_v",
        [
            ("e", 2),  # Вперед
            ("f", 2),  # По диагонали
            ("d", 1),  # Влево
            ("f", 1),  # Вправо
        ],
    )
    def test_king_valid_moves(self, king_e1, target_h, target_v):
        assert king_e1.can_move(target_h, target_v) is True

    @pytest.mark.parametrize(
        "target_h, target_v",
        [
            ("e", 1),  # Ход на то же место
            ("e", 3),  # Слишком далеко вперед (через клетку)
            ("g", 3),  # Слишком далеко по диагонали
            ("b", 1),  # Слишком далеко влево
            ("e", 1),  # Ход на месте невозможен
        ],
    )
    def test_king_invalid_moves(self, king_e1, target_h, target_v):
        assert king_e1.can_move(target_h, target_v) is False

    def test_king_attributes(self, king_e1):
        assert king_e1.horizontal == "e"
        assert king_e1.vertical == 1

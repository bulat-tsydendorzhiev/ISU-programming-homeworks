import pytest

from homework9.task2.Son import Son

class TestSon:

    @pytest.fixture
    def son_default(self):
        return Son()

    def test_son_attributes(self, son_default):
        assert son_default.mood == "neutral"
        assert Son("calm").mood == "calm"

    def test_son_greet(self, son_default):
        assert son_default.greet() == "Hello!"

    @pytest.mark.parametrize(
        "method_name, expected_mood",
        [
            ("be_kind", "kind"),
            ("be_strict", "strict"),
        ],
    )
    def test_son_mood_changes(self, son_default, method_name, expected_mood):
        getattr(son_default, method_name)()
        assert son_default.mood == expected_mood

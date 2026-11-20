import pytest

from homework9.task2.Daughter import Daughter

class TestDaughter:

    @pytest.fixture
    def daughter_default(self):
        return Daughter()

    def test_daughter_attributes(self, daughter_default):
        assert daughter_default.mood == "neutral"
        assert Daughter("sad").mood == "sad"

    def test_daughter_greet(self, daughter_default):
        assert daughter_default.greet() == "Hi, honey!"

    @pytest.mark.parametrize(
        "method_name, expected_mood",
        [
            ("be_kind", "kind"),
            ("be_strict", "strict"),
        ],
    )
    def test_daughter_mood_changes(self, daughter_default, method_name, expected_mood):
        getattr(daughter_default, method_name)()
        assert daughter_default.mood == expected_mood

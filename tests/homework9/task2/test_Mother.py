import pytest

from homework9.task2.Mother import Mother

class TestMother:

    @pytest.fixture
    def mother_default(self):
        return Mother()

    def test_mother_initial_mood(self, mother_default):
        assert mother_default.mood == "neutral"
        assert Mother("excited").mood == "excited"

    def test_mother_greet(self, mother_default):
        assert mother_default.greet() == "Hi, honey!"

    def test_mother_be_kind(self, mother_default):
        mother_default.be_kind()
        assert mother_default.mood == "kind"

    def test_mother_str_should_work_correctly(self, mother_default):
        assert str(mother_default) == "Mother is in a neutral mood"

import pytest

from homework9.task2.Father import Father

class TestFather:

    @pytest.fixture
    def father_default(self):
        return Father()

    def test_father_initial_mood(self, father_default):
        assert father_default.mood == "neutral"
        assert Father("happy").mood == "happy"

    def test_father_greet(self, father_default):
        assert father_default.greet() == "Hello!"

    def test_father_be_strict(self, father_default):
        father_default.be_strict()
        assert father_default.mood == "strict"

    def test_father_str_should_work_correctly(self, father_default):
        assert str(father_default) == "Father is in a neutral mood"

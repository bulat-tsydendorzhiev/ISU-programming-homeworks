import pytest

from homework7.User import User


class TestInit:
    @pytest.mark.parametrize("name", ["Ivan", "Иван", "A", "AnnaMaria"])
    def test_accepts_alphabetic_name(self, name):
        assert User(name, 20).name == name

    @pytest.mark.parametrize(
        "name",
        ["", "Ivan1", "Ivan Petrov", "Ivan-Petrov", "Ivan_Petrov", "  "],
    )
    def test_rejects_non_alphabetic_name(self, name):
        with pytest.raises(ValueError, match="Некорректное имя"):
            User(name, 20)

    @pytest.mark.parametrize("age", [0, 1, 55, 110])
    def test_accepts_age_within_range(self, age):
        assert User("Ivan", age).age == age

    @pytest.mark.parametrize("age", [-1, 111])
    def test_rejects_age_outside_range(self, age):
        with pytest.raises(ValueError, match="Некорректный возраст"):
            User("Ivan", age)


class TestProperties:
    def test_getters_return_stored_values(self):
        user = User("Ivan", 20)

        assert user.get_name() == "Ivan"
        assert user.get_age() == 20

    def test_property_setters_update_values(self):
        user = User("Ivan", 20)

        user.name = "Пётр"
        user.age = 30

        assert user.name == "Пётр"
        assert user.age == 30

    def test_set_name_and_set_age_update_values(self):
        user = User("Ivan", 20)

        user.set_name("Anna")
        user.set_age(25)

        assert user.get_name() == "Anna"
        assert user.get_age() == 25

    @pytest.mark.parametrize("new_name", ["", "Ivan1", "Ivan Petrov"])
    def test_invalid_new_name_keeps_previous_name(self, new_name):
        user = User("Ivan", 20)

        with pytest.raises(ValueError, match="Некорректное имя"):
            user.name = new_name

        assert user.name == "Ivan"

    @pytest.mark.parametrize("new_age", [-1, 111])
    def test_invalid_new_age_keeps_previous_age(self, new_age):
        user = User("Ivan", 20)

        with pytest.raises(ValueError, match="Некорректный возраст"):
            user.age = new_age

        assert user.age == 20

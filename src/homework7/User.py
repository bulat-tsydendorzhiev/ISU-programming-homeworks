class User:
    def __init__(self, name: str, age: int):
        if not self.__is_valid_name(name):
            raise ValueError("Некорректное имя.")

        if not self.__is_valid_age(age):
            raise ValueError("Некорректный возраст.")

        self.__name = name
        self._age = age

    @property
    def name(self) -> str:
        return self.get_name()

    @name.setter
    def name(self, new_name: str) -> None:
        self.set_name(new_name)

    @property
    def age(self) -> int:
        return self.get_age()

    @age.setter
    def age(self, new_age: int) -> None:
        self.set_age(new_age)

    def get_name(self) -> str:
        return self.__name

    def set_name(self, new_name: str) -> None:
        if not self.__is_valid_name(new_name):
            raise ValueError("Некорректное имя.")
        self.__name = new_name

    def get_age(self) -> int:
         return self._age

    def set_age(self, new_age: int) -> None:
        if not self.__is_valid_age(new_age):
            raise ValueError("Некорректный возраст.")
        self._age = new_age

    @staticmethod
    def __is_valid_name(name: str) -> bool:
        return str.isalpha(name)

    @staticmethod
    def __is_valid_age(age: int) -> bool:
        return 0 <= age <= 110
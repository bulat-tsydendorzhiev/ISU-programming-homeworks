import re

class IPAdress:
    def __init__(self, ipadress: str | list[int] | tuple[int]):
        if not self.__is_valid_ipadress(ipadress):
            raise ValueError("Некорректный IP-адрес.")

        if isinstance(ipadress, list) or isinstance(ipadress, tuple):
            self.__ipadress = ".".join(str(num) for num in ipadress)
            return

        self.__ipadress = ipadress

    def __repr__(self):
        return f"IPAdress('{self.__ipadress}')"

    def __str__(self):
        return self.__ipadress

    def __is_valid_ipadress(self, ipadress: str | list[int] | tuple[int]) -> bool:
        if isinstance(ipadress, str):
            ipadress_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\Z'
            return bool(re.match(ipadress_pattern, ipadress))

        return len(ipadress) == 4 and all(0 <= int(num) < 256 for num in ipadress)

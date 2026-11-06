class Word:
    def __init__(self, word: str):
        if not self.__is_valid_word(word):
            raise ValueError("Некорректное слово.")

        self.__word = word

    def __repr__(self):
        return f"Word('{self.__word}')"

    def __str__(self):
        return str.capitalize(self.__word)

    def __eq__(self, other: Word):
        if not isinstance(other, Word):
            return NotImplemented

        return self.__word == other.__word

    def __ne__(self, other: Word):
        if not isinstance(other, Word):
            return NotImplemented

        return self.__word != other.__word

    def __lt__(self, other: Word):
        if not isinstance(other, Word):
            return NotImplemented

        return self.__word < other.__word

    def __le__(self, other: Word):
        if not isinstance(other, Word):
            return NotImplemented

        return self.__word <= other.__word

    def __gt__(self, other: Word):
        if not isinstance(other, Word):
            return NotImplemented

        return self.__word > other.__word

    def __ge__(self, other: Word):
        if not isinstance(other, Word):
            return NotImplemented

        return self.__word >= other.__word

    @staticmethod
    def __is_valid_word(word: str) -> bool:
        return str.isalpha(word) and str.isascii(word)

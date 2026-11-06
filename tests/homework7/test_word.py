import operator

import pytest

from homework7.Word import Word


class TestInit:
    @pytest.mark.parametrize("word", ["a", "Hello", "HELLO", "Python"])
    def test_accepts_ascii_letters(self, word):
        assert str(Word(word)) == word.capitalize()

    @pytest.mark.parametrize(
        "word",
        ["", "Hello1", "Hello World", "Hello-World", "Hello_World", "Слово", "тест"],
    )
    def test_rejects_non_ascii_or_non_alphabetic_word(self, word):
        with pytest.raises(ValueError, match="Некорректное слово"):
            Word(word)


class TestRepresentation:
    @pytest.mark.parametrize(
        ("word", "expected"),
        [
            ("hello", "Hello"),
            ("HELLO", "Hello"),
            ("hELLo", "Hello"),
        ],
    )
    def test_str_capitalizes_word(self, word, expected):
        assert str(Word(word)) == expected

    def test_repr_contains_original_word(self):
        assert repr(Word("hELLo")) == "Word('hELLo')"


class TestComparison:
    @pytest.mark.parametrize(
        ("left", "right", "comparison", "expected"),
        [
            ("apple", "apple", operator.eq, True),
            ("apple", "banana", operator.eq, False),
            ("apple", "banana", operator.ne, True),
            ("apple", "apple", operator.ne, False),
            ("apple", "banana", operator.lt, True),
            ("banana", "apple", operator.lt, False),
            ("apple", "apple", operator.le, True),
            ("apple", "banana", operator.le, True),
            ("banana", "apple", operator.gt, True),
            ("apple", "banana", operator.gt, False),
            ("apple", "apple", operator.ge, True),
            ("banana", "apple", operator.ge, True),
        ],
    )
    def test_comparison_operators(self, left, right, comparison, expected):
        assert comparison(Word(left), Word(right)) is expected

    def test_comparison_is_case_sensitive(self):
        assert Word("apple") != Word("Apple")
        assert Word("Apple") < Word("apple")

    def test_equality_with_non_word_is_false(self):
        assert (Word("apple") == "apple") is False
        assert (Word("apple") != "apple") is True

    def test_ordering_with_non_word_raises_type_error(self):
        with pytest.raises(TypeError):
            Word("apple") < "banana"

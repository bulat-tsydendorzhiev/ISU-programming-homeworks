from random import Random
import string

import pytest

from homework3.main_version.task1 import KEY_PHRASE, decode_letter

ALPHABET = string.ascii_lowercase

MESSAGES = [
    ["hello vasya"],
    ["dear friend", "how are you", "best regards"],
    ["i finished my math homework", "the internet at the faculty is terrible"],
]

DECOY_ROWS = [
    KEY_PHRASE[:-1],
    KEY_PHRASE + ALPHABET[0],
    KEY_PHRASE.replace("quick", "qui ck"),
    KEY_PHRASE.replace(" ", ""),
    KEY_PHRASE.replace("fox", "cat"),
]


def make_table(seed: int) -> dict[int, int]:
    shuffled = list(ALPHABET)
    Random(seed).shuffle(shuffled)
    return str.maketrans(ALPHABET, "".join(shuffled))


def encode(text: str, table) -> str:
    return text.translate(table)


def build_letter(rows: list[str], seed: int, key_phrase_index: int) -> tuple[list[str], list[str]]:
    table = make_table(seed)

    letter = [encode(row, table) for row in rows]
    letter.insert(key_phrase_index, encode(KEY_PHRASE, table))

    expected = list(rows)
    expected.insert(key_phrase_index, KEY_PHRASE)

    return letter, expected


class TestNoSolutionLetter:
    def test_letter_without_key_phrase_should_return_no_solution(self):
        letter = ["i", "love", "fbccs"]
        assert decode_letter(letter) == ["No solution"]

    def test_letter_with_decoy_rows_should_return_no_solution(self):
        letter = DECOY_ROWS
        assert decode_letter(letter) == ["No solution"]


class TestDecodingLetter:
    @pytest.mark.parametrize("seed", [None, 42, 67], ids=["without_shuffle", "cipher_42", "cipher_67"])
    def test_key_phrase_is_the_only_row(self, seed):
        row = KEY_PHRASE if seed is None else encode(KEY_PHRASE, make_table(seed))
        assert decode_letter([row]) == [KEY_PHRASE]

    @pytest.mark.parametrize("rows", MESSAGES)
    def test_letter_should_be_decoded(self, rows):
        letter, expected = build_letter(rows, 67, len(rows))
        assert decode_letter(letter) == expected

    @pytest.mark.parametrize("position", [0, 1, 2, 3])
    def test_key_phrase_position_does_not_matter(self, position):
        rows = ["i", "love", "my", "groupmates"]
        letter, _ = build_letter(rows, 67, position)
        expected = rows[:position] + [KEY_PHRASE] + rows[position:]
        assert decode_letter(letter) == expected

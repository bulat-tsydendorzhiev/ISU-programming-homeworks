import pytest

from homework3.main_version.task2 import find_first_occurence, main

CASES = [
    ("1", 1),
    ("9", 9),
    ("10", 10),
    ("12", 1),
    ("11", 12),
    ("13", 16),
    ("45", 4),
    ("99", 169),
    ("100", 190),
    ("101", 10),
    ("567", 5),
    ("1000", 2890),
    ("10000", 38890),
]


@pytest.mark.parametrize(("number", "expected"), CASES)
def test_find_first_occurence(number: str, expected: int):
    assert find_first_occurence(number) == expected

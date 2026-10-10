import pytest

from homework3.optional_version.task2 import count_subprefix_matches

DICTIONARY = ["aba", "abacaba", "abc", "xabcy", "aa", "abcabc"]

CASES = [
    ("abc", 2),
    ("aba", 2),
    ("a", 3),
    ("aa", 1),
    ("ab", 0),
    ("ca", 0),
]


class TestSingleSample:
    @pytest.mark.parametrize(("sample", "expected"), CASES, ids=[f"sample_{s}" for s, _ in CASES])
    def test_count_matches_for_one_sample(self, sample: str, expected: int):
        assert count_subprefix_matches(DICTIONARY, [sample]) == {sample: expected}

    def test_sample_longer_than_word(self):
        assert count_subprefix_matches(["ab", "a"], ["abc"]) == {"abc": 0}

    def test_sample_in_the_middle_of_the_word(self):
        assert count_subprefix_matches(["xabcx"], ["abc"]) == {"abc": 0}

    def test_overlapping_occurrences_at_both_ends(self):
        assert count_subprefix_matches(["aaaa"], ["aa"]) == {"aa": 1}

    def test_word_is_counted_once_per_occurrence_of_sample(self):
        assert count_subprefix_matches(["abcabc"], ["abc"]) == {"abc": 1}

    def test_duplicated_words_are_counted_separately(self):
        assert count_subprefix_matches(["abc", "abc", "ab"], ["abc"]) == {"abc": 2}


class TestMultipleSamples:
    def test_result_contains_every_sample(self):
        samples = ["abc", "xyz", "a"]
        assert count_subprefix_matches(DICTIONARY, samples) == {"abc": 2, "xyz": 0, "a": 3}

    def test_samples_do_not_depend_on_each_other(self):
        assert count_subprefix_matches(["abcabc"], ["abc", "bca"]) == {"abc": 1, "bca": 0}
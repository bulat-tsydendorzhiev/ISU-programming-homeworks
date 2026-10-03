from homework1.task1 import get_non_unique_numbers


def test_returns_only_repeated_numbers():
    result = get_non_unique_numbers([4, 8, 0, 3, 4, 2, 0, 3])

    assert sorted(result) == [0, 3, 4]


def test_handles_numbers_repeated_more_than_twice():
    result = get_non_unique_numbers([1, 1, 1, 1, 1, 1, 1, 2, 2, 5])

    assert sorted(result) == [1, 2]


def test_returns_empty_list_when_numbers_are_unique_or_absent():
    assert get_non_unique_numbers([]) == []


def test_returns_empty_list_when_numbers_are_unique():
    assert get_non_unique_numbers([1, 2, 3]) == []


def test_returns_empty_list_for_one_number_list():
    assert get_non_unique_numbers([1]) == []


def test_each_repeated_number_is_returned_once():
    result = get_non_unique_numbers([7, 7, 7, 7, 9, 9])

    assert sorted(result) == [7, 9]


def test_handles_negative_and_zero_numbers():
    result = get_non_unique_numbers([-1, 0, -1, 5, 0, 5, 5])

    assert sorted(result) == [-1, 0, 5]


def test_does_not_modify_input_list():
    numbers = [1, 2, 1, 3, 2]
    original = list(numbers)

    get_non_unique_numbers(numbers)

    assert numbers == original

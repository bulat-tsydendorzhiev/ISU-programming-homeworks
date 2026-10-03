from homework1.task2 import get_passenger_count


def test_counts_passengers_at_entry_and_exit_times():
    intervals = [(3, 12),
                 (8, 9),
                 (5, 10),
                 (10, 12)]

    assert get_passenger_count(intervals, 10) == 3


def test_counts_passengers_inside_interval():
    intervals = [(5, 15),
                 (12, 25),
                 (1, 17)]

    assert get_passenger_count(intervals, 14) == 3


def test_counts_passengers_for_interval_boundaries():
    intervals = [(3, 5),
                 (5, 15),
                 (15, 30)]

    assert get_passenger_count(intervals, 5) == 2
    assert get_passenger_count(intervals, 15) == 2


def test_returns_zero_when_no_passengers_are_present():
    intervals = [(10, 20),
                 (30, 40)]

    assert get_passenger_count(intervals, 25) == 0
    assert get_passenger_count([], 15) == 0

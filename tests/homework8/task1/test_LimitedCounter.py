import pytest

from homework8.task1.Counter import Counter
from homework8.task1.LimitedCounter import LimitedCounter


class TestLimitedCounter:
    def test_is_counter_subclass(self) -> None:
        assert issubclass(LimitedCounter, Counter)

    def test_default_start_and_limit(self) -> None:
        counter = LimitedCounter()
        assert counter.value == 0

    def test_custom_start_below_limit(self) -> None:
        counter = LimitedCounter(start=5, limit=10)
        assert counter.value == 5

    def test_start_equal_to_limit(self) -> None:
        counter = LimitedCounter(start=10, limit=10)
        assert counter.value == 10

    def test_start_above_limit_raises(self) -> None:
        with pytest.raises(ValueError):
            LimitedCounter(start=11, limit=10)

    def test_inc_within_limit(self) -> None:
        counter = LimitedCounter(start=5, limit=10)
        counter.inc(3)
        assert counter.value == 8

    def test_inc_at_limit_does_nothing(self) -> None:
        counter = LimitedCounter(start=10, limit=10)
        counter.inc()
        assert counter.value == 10

    def test_inc_does_not_exceed_limit(self) -> None:
        counter = LimitedCounter(start=8, limit=10)
        counter.inc(5)
        assert counter.value == 10

    def test_dec_is_inherited(self) -> None:
        counter = LimitedCounter(start=5, limit=10)
        counter.dec(2)
        assert counter.value == 3

from homework8.task1.Counter import Counter
from homework8.task1.NonDecCounter import NonDecCounter


class TestNonDecCounter:
    def test_is_counter_subclass(self) -> None:
        assert issubclass(NonDecCounter, Counter)

    def test_default_start_is_zero(self) -> None:
        counter = NonDecCounter()
        assert counter.value == 0

    def test_custom_start(self) -> None:
        counter = NonDecCounter(7)
        assert counter.value == 7

    def test_inc_is_inherited(self) -> None:
        counter = NonDecCounter()
        counter.inc()
        assert counter.value == 1

    def test_dec_does_nothing(self) -> None:
        counter = NonDecCounter(5)
        counter.dec()
        assert counter.value == 5

    def test_dec_with_step_does_nothing(self) -> None:
        counter = NonDecCounter(5)
        counter.dec(3)
        assert counter.value == 5

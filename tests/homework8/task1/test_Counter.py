from homework8.task1.Counter import Counter


class TestCounter:
    def test_default_start_is_zero(self) -> None:
        counter = Counter()
        assert counter.value == 0

    def test_custom_start(self) -> None:
        counter = Counter(42)
        assert counter.value == 42

    def test_inc_with_default_step(self) -> None:
        counter = Counter()
        counter.inc()
        assert counter.value == 1

    def test_inc_with_custom_step(self) -> None:
        counter = Counter(3)
        counter.inc(7)
        assert counter.value == 10

    def test_dec_with_default_step(self) -> None:
        counter = Counter(5)
        counter.dec()
        assert counter.value == 4

    def test_dec_with_custom_step(self) -> None:
        counter = Counter(10)
        counter.dec(6)
        assert counter.value == 4

    def test_dec_at_zero_does_nothing(self) -> None:
        counter = Counter()
        counter.dec()
        assert counter.value == 0

    def test_dec_does_not_go_below_zero(self) -> None:
        counter = Counter(3)
        counter.dec(5)
        assert counter.value == 0

class Counter:
    def __init__(self, start=0):
        self._value = start

    @property
    def value(self) -> int:
        return self._value

    def inc(self, step=1) -> None:
        self._value += step

    def dec(self, step=1) -> None:
        if self._value == 0:
            return
        self._value -= step

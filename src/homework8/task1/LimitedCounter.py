from homework8.task1.Counter import Counter

class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        if start < limit:
            raise ValueError("Начальное значение не может быть больше лимита.")
        
        super().__init__(start)
        self.__limit = limit

    def inc(self, step=1) -> None:
        if self._value == self.__limit:
            return
        self._value += step

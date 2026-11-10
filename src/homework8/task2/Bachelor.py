import math

class Bachelor:
    def __init__(self, first_name, last_name, group, average_mark):
        self._first_name = first_name
        self._last_name = last_name
        self._group = group
        self._average_mark = average_mark

    def get_scholarship(self):
        if self._average_mark > 3:
            return 5000
        elif math.isclose(self._average_mark, 5):
            return 10000
        else:
            return 0
    
    
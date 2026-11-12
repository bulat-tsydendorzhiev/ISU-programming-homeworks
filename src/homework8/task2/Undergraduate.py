import math

from homework8.task2.Bachelor import Bachelor

class Undergraduate(Bachelor):
    def __init__(self, first_name, last_name, group, average_mark, research_work):
        super().__init__(first_name, last_name, group, average_mark)
        self.__research_work = research_work

    def get_scholarship(self):
        if math.isclose(self._average_mark, 5):
            return 15000
        elif self._average_mark > 3:
            return 7500
        else:
            return 0
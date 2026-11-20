from homework9.task2.Father import Father
from homework9.task2.Mother import Mother

class Son(Father, Mother):
    def __str__(self):
        return f"Son is in a {self.mood} mood"

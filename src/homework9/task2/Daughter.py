from homework9.task2.Mother import Mother
from homework9.task2.Father import Father

class Daughter(Mother, Father):
    def __str__(self):
        return f"Daughter is in a {self.mood} mood"

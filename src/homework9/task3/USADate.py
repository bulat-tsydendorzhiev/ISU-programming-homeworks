from homework9.task3.BaseDate import BaseDate

class USADate(BaseDate):
    def format(self) -> str:
        return f"{self.month:02d}-{self.day:02d}-{self.year:04d}"
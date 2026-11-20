from homework9.task3.BaseDate import BaseDate

class ItalianDate(BaseDate):
    def format(self) -> str:
        return f"{self.day:02d}/{self.month:02d}/{self.year:04d}"
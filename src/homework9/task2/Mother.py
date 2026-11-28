class Mother:
    def __init__(self, mood: str = "neutral"):
        self._mood = mood

    @property
    def mood(self) -> str:
        return self._mood

    def greet(self) -> str:
        return "Hi, honey!"

    def be_kind(self):
        self._mood = "kind"

    def __str__(self):
        return f"Mother is in a {self.mood} mood"

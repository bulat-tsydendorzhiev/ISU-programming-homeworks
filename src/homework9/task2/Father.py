class Father:
    def __init__(self, mood: str = "neutral"):
        self._mood = mood

    @property
    def mood(self) -> str:
        return self._mood

    def greet(self) -> str:
        return "Hello!"

    def be_strict(self):
        self._mood = "strict"

class Memory:
    def __init__(self):
        self.history = []

    def add(self, entry: str):
        self.history.append(entry)

    def get(self) -> str:
        if not self.history:
            return "No memory yet."
        return "\n".join(self.history)

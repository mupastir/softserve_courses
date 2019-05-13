class HappyTicket:

    def __init__(self, filepath: str, mode: str):
        self.MODES = {"moskow": self.moscow_mode,
                      "piter": self.peter_mode}
        self.filename = filepath
        self.result = {}
        self.start = self.MODES[mode.lower()]
        self.start()

    def moscow_mode(self):
        ...

    def peter_mode(self):
        ...

    def __repr__(self):
        ...


if __name__ == "__main__":
    HappyTicket('text.txt', 'Piter')

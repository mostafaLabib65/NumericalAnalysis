class InputException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self) -> str:
        return super().__str__() + self.message

    def getMessage(self):
        return self.message

import math


class HolderOfValues:
    pass


class Function:

    def __init__(self, string):
        if not string and not type(string) == str:
            raise Exception("a string representation of the function is required")
        self.function = string.replace("^", "**")
        self.holder = HolderOfValues()

    def evaluate(self, values):
        equation = self.function
        for key, value in zip(values.keys(), values.values()):
            setattr(self.holder, key, value)
            equation = str(equation).replace(key, "self.holder." + key)
        return eval(equation)

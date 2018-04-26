from math import *


class Function:

    def __init__(self, function):
        if not function and not type(function) == str:
            raise Exception("a string representation of the function is required")
        self.function = function

    def evaluate(self, values):
        equation = self.function
        for key, value in zip(values.keys(), values.values()):
            equation = str(equation).replace(key, str(value))
        return eval(equation)

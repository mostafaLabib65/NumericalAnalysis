from math import *


class Function:

    def __init__(self, function):
        if not function and not type(function) == str:
            raise Exception("a string representation of the function is required")
        self.function = function

    def evaluate(self, value):
        equation = self.function
        equation = str(equation).replace("x", str(value))
        return eval(equation)

from math import *
import sympy as sp


class Function:

    def __init__(self, function):
        if not function and not type(function) == str:
            raise Exception("a string representation of the function is required")
        self.function = function

    def evaluate(self, value):
        x = sp.symbols('x')
        return sp.sympify(self.function).subs(x, value)

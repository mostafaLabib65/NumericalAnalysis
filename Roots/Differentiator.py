import sympy as sp
from Roots.Function import Function

class Differentiator:

    def __init__(self, function):
        self.function = function
        self.x = sp.symbols('x')
        self.formulate()

    def get_function(self):
        return Function(self.function)

    def get_first_derivative(self):
        return Function(str(sp.diff(self.function, self.x)))

    def get_second_derivative(self):
        return Function(str(sp.diff(self.function, self.x, self.x)))

    def formulate(self):
        self.function = self.function.replace("^", "**")

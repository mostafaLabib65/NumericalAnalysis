import sympy as sp
from Roots.Function import Function
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application


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
        transformations = (standard_transformations + (implicit_multiplication_application,))
        self.function = sp.sympify(parse_expr(self.function, transformations=transformations))

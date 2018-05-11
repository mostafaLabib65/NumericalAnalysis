import sympy
from sympy.parsing import sympy_parser
import numpy as np

from Roots.OpenMethod import OpenMethod


class BirgeVieta(OpenMethod):
    def __init__(self, function, error=0.0001, max_iterations=50):
        super().__init__(function, error, max_iterations)

    def do(self, xi):
        return self.birge_vieta(xi)

    def birge_vieta(self, xi):
        old_root, itr, root, divergence_count, ea = 0, 0, 0, 0, 0
        data = []
        while itr < self.max_iterations:

            if divergence_count > 15:
                raise Exception("Method is diverging", data)

            b_list = self.get_b(xi)
            c_list = self.get_c(xi, b_list)

            funct_xi = b_list[-1]
            derivative_xi = c_list[-1]

            if derivative_xi == 0:
                raise Exception("Division by zero", data)
            root = float(xi - (funct_xi / derivative_xi))
            ea = abs(root - old_root)

            record = np.array([itr + 1, b_list, c_list, xi, root, ea])
            data.append(record)

            if abs(self.compute(root)) > abs(self.compute(old_root)) and itr > 0:
                divergence_count += 1
            else:
                divergence_count = 0

            if ea <= self.error:
                self.check(root, ea)
                return data
            old_root = root
            xi = root
            itr = itr + 1
        self.check(root, ea)
        return data

    def get_b(self, xi):
        a_list = self.extract_coefficients()
        b = [a_list[0]]
        for i in range(1, len(a_list)):
            b.append(a_list[i] + xi * b[-1])
        return b

    def get_c(self, xi, b_list):
        c = [b_list[0]]
        for i in range(1, len(b_list) - 1):
            c.append(b_list[i] + xi * c[-1])
        return c

    def extract_coefficients(self):
        expr = self.function.function
        polyn = sympy.Poly(expr, sympy.symbols("x"))
        coeffs = polyn.all_coeffs()
        return [x / coeffs[0] for x in coeffs]
from Roots.OpenMethod import OpenMethod
import numpy as np


class Secant(OpenMethod):
    def __init__(self, function, derivative=None, second_derivative=None, multiplicity=1, error=0.0001
                 , max_iterations=50, gx=None):
        super().__init__(function, derivative, second_derivative, multiplicity, error, max_iterations, gx)

    def do(self, xi, xi_1):
        return self.secant(xi, xi_1)

    def secant(self, xi, xi_1):
        old_root, itr, root, rel = 0, 0, 0, 0
        data = []
        while itr < self.max_iterations:

            f_xi = self.compute(xi)
            f_xi_1 = self.compute(xi_1)

            if abs(f_xi - f_xi_1) == 0:
                raise Exception("Division by zero", root, itr, rel)

            root = xi - ((f_xi * (xi_1 - xi)) / (f_xi_1 - f_xi))

            ea = abs(root - old_root)
            rel = abs(ea / root) * 100

            record = np.array([itr, xi_1, f_xi_1, xi, f_xi, root, self.compute(root), ea, rel])
            data.append(record)
            if ea <= self.error:
                return data
            xi_1 = xi
            old_root = root
            xi = root
            itr = itr + 1
        return data

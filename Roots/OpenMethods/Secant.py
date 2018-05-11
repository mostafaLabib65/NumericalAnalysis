from Roots.OpenMethod import OpenMethod
import numpy as np


class Secant(OpenMethod):
    def __init__(self, function,  error=0.0001, max_iterations=50):
        super().__init__(function,error, max_iterations)

    def do(self, xi, xi_1):
        self.initial = max(abs(xi), abs(xi_1))
        return self.secant(xi, xi_1)

    def secant(self, xi, xi_1):
        old_root, itr, root, divergence_count, ea = 0, 0, 0, 0, 0
        data = []
        while itr < self.max_iterations:
            if divergence_count > 15:
                raise Exception("Method is diverging", data)

            f_xi = self.compute(xi)
            f_xi_1 = self.compute(xi_1)

            if abs(f_xi - f_xi_1) == 0:
                raise Exception("Division by zero", data)

            root = float(xi - ((f_xi * (xi_1 - xi)) / (f_xi_1 - f_xi)))

            ea = abs(root - old_root)

            record = np.array([itr+ 1, xi_1, f_xi_1, xi, f_xi, root, self.compute(root), ea, rel])
            data.append(record)
            self.root = root

            if abs(self.compute(root)) > abs(self.compute(old_root)) and itr > 0:
                divergence_count += 1
            else:
                divergence_count = 0

            if ea <= self.error:
                self.check(root, ea)
                return data
            xi_1 = xi
            old_root = root
            xi = root
            itr = itr + 1
        self.check(root, ea)
        return data

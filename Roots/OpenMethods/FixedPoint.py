from Roots.OpenMethod import OpenMethod
import numpy as np
import sympy as sp


class FixedPoint(OpenMethod):
    def __init__(self, function, derivative=None, error=0.0001, max_iterations=50, gx=None):
        super().__init__(function, derivative, error=error, max_iterations=max_iterations, gx=gx)

    def do(self, xi):
        self.initial = xi
        if self.gx is None:
            self.function.function = sp.sympify((str(self.function.function) + " + x"))
        return self.fixed_point(xi)

    @staticmethod
    def get_headers():
        return ["Iterations", "X(i)", "Root", "G of Root", "Absolute Error"]

    def fixed_point(self, xi):
        old_root, itr, root, divergence_count, ea = 0, 0, 0, 0, 0

        derivative = self.compute_derivative(xi)
        if self.gx is None:
            derivative += 1

        data = []
        while itr < self.max_iterations:

            if divergence_count > 15:
                raise Exception("Method is diverging", data)

            root = float(self.compute(xi))
            ea = abs(root - old_root)

            record = np.array([itr + 1, xi, root, self.compute(root), ea])
            data.append(record)
            self.root = root

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

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

    def fixed_point(self, xi):
        old_root, itr, root, rel = 0, 0, 0, 0

        derivative = self.compute_derivative(xi)
        if self.gx is None:
            derivative += 1

        if abs(derivative) > 1:
            raise Exception("Function will diverge")

        data = []
        while itr < self.max_iterations:
            root = float(self.compute(xi))
            ea = abs(root - old_root)
            rel = abs(ea / root) * 100

            record = np.array([itr, xi, root, self.compute(root), ea, rel])
            data.append(record)
            self.root = root
            if ea <= self.error:
                return data
            old_root = root
            xi = root
            itr = itr + 1
        return data

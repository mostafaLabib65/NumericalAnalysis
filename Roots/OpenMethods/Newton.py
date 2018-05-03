from Roots.OpenMethod import OpenMethod
import numpy as np


class Newton(OpenMethod):
    def __init__(self, function, derivative=None, second_derivative=None, multiplicity=1, error=0.0001
                 , max_iterations=50,gx=None):
        super().__init__(function, derivative, second_derivative, multiplicity, error, max_iterations, gx)

    def do(self, xi):
        self.initial = xi
        if self.second_derivative is not None:
            return self.newton_method2(xi)
        elif self.multiplicity is not 1:
            return self.newton_method1(xi)
        return self.newton(xi)

    def newton(self, xi):
        old_root, itr, root, rel = 0, 0, 0, 0
        data = []
        while itr < self.max_iterations:
            derivative_xi = self.compute_derivative(xi)
            if derivative_xi == 0:
                raise Exception("Division by zero", root, itr, rel)
            f_xi = self.compute(xi)
            root = xi - (f_xi / derivative_xi)
            ea = abs(root - old_root)
            rel = abs(ea / root) * 100

            record = np.array([itr, xi, f_xi, derivative_xi, root, self.compute(root), ea, rel])
            data.append(record)
            self.root = root
            if ea <= self.error:
                return data
            old_root = root
            xi = root
            itr = itr + 1
        return data

    def newton_method1(self, xi):
        old_root, itr, root, rel = 0, 0, 0, 0
        data = []
        while itr < self.max_iterations:
            derivative_xi = self.compute_derivative(xi)
            if derivative_xi == 0:
                raise Exception("Division by zero", root, itr, rel)
            f_xi = self.compute(xi)
            root = xi - self.multiplicity * (f_xi / derivative_xi)
            ea = abs(root - old_root)
            rel = abs(ea / root) * 100

            record = np.array([itr, xi, f_xi, derivative_xi, root, self.compute(root), ea, rel])
            data.append(record)
            self.root = root
            if ea <= self.error:
                return data
            old_root = root
            xi = root
            itr = itr + 1
        return data

    def newton_method2(self, xi):
        old_root, itr, root, rel = 0, 0, 0, 0
        data = []
        while itr < self.max_iterations:
            derivative_xi = ((self.compute_derivative(xi)) ** 2 - self.compute_second_derivative(xi) * self.compute(xi))
            if derivative_xi == 0:
                raise Exception("Division by zero", root, itr, rel)
            f_xi = (self.compute(xi) * self.compute_derivative(xi))
            root = xi - (f_xi / derivative_xi)
            ea = abs(root - old_root)
            rel = abs(ea / root) * 100
            record = np.array([itr, xi, f_xi, derivative_xi, root, self.compute(root), ea, rel])
            data.append(record)
            self.root = root
            if ea <= self.error:
                return data
            old_root = root
            xi = root
            itr = itr + 1
        return data
from OpenMethod import OpenMethod


class FixedPoint(OpenMethod):
    def __init__(self, function, derivative=None, second_derivative=None, multiplicity=1, error=0.0001
                 , max_iterations=50, gx=None):
        super().__init__(function, derivative, second_derivative, multiplicity, error, max_iterations, gx)

    def do(self, xi):
        if self.gx is None:
            self.function += " + x"
        return self.fixed_point(xi)

    def fixed_point(self, xi):
        old_root, itr, root, rel = 0, 0, 0, 0

        derivative = self.compute_derivative(xi)

        if abs(derivative) < 1:
            raise Exception("Function will diverge")

        while itr < self.max_iterations:
            root = self.function.compute(xi)
            ea = abs(root - old_root)
            rel = abs(ea / root) * 100
            if ea <= self.error:
                return root, itr, rel
            old_root = root
            xi = root
            itr = itr + 1
        return root, rel, itr

from OpenMethod import OpenMethod


class BirgeVieta(OpenMethod):
    def __init__(self, function, derivative=None, second_derivative=None, multiplicity=1, error=0.0001
                 , max_iterations=50, gx=None):
        super().__init__(function, derivative, second_derivative, multiplicity, error, max_iterations, gx)

    def do(self, xi):
        return self.birge_vieta(xi)

    def birge_vieta(self, xi):
        old_root, itr, root, rel = 0, 0, 0, 0
        while itr < self.max_iterations:
            b_list = self.get_b(xi)
            c_list = self.get_c(xi, b_list)

            funct_xi = b_list[0]
            derivative_xi = c_list[0]
            if derivative_xi == 0:
                raise Exception("Division by zero", root, itr, rel)
            root = xi - (funct_xi / derivative_xi)
            ea = abs(root - old_root)
            rel = abs(ea / root) * 100
            if ea <= self.error:
                return root, itr, rel
            old_root = root
            xi = root
            itr = itr + 1
        return root, rel, itr

    def get_b(self, xi):
        a_list = self.function.coefficients
        b = [a_list[0]]
        for i in range(1, len(a_list)):
            b.append(a_list[i] + xi * b[-1])
        return b

    def get_c(self, xi, b_list):
        c = [b_list[0]]
        for i in range(1, len(b_list) - 1):
            c.append(b_list[i] + xi * c[-1])
        return c

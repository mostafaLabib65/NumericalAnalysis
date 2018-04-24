from Bracketer import Bracketer


class FalsePosition(Bracketer):

    def __init__(self, function, error=0.0001, max_iterations=50):
        super().__init__(function, error, max_iterations)

    def do(self, lower_bound, upper_bound):
        return self.false_pos(lower_bound, upper_bound)

    def false_pos(self, lower_bound, upper_bound):
        itr, old_root, root, rel = 0, 0, 0, 0
        lower_bound_stuck, upper_bound_stuck = 0, 0
        while itr < self.max_iterations:
            f_lower = self.compute(lower_bound)
            f_upper = self.compute(upper_bound)

            if f_lower * f_upper > 0:
                raise Exception("No valid roots in this interval")
            if f_upper - f_lower == 0:
                raise Exception("Division by zero", root, itr, rel)

            if abs(lower_bound_stuck - upper_bound_stuck) == 20:
                root = (lower_bound + upper_bound) / 2
                lower_bound_stuck, upper_bound_stuck = 0, 0
            else:
                root = (lower_bound * f_upper - upper_bound * f_lower) / (f_upper - f_lower)
            f_root = self.compute(root)

            ea = abs(root - old_root)
            rel = abs(ea / root) * 100
            if ea < self.error and itr > 1:
                return root, itr, rel

            cond = f_root * f_lower

            old_root = root
            if cond < 0:
                upper_bound = root
                upper_bound_stuck += 1
            elif f_root > 0:
                lower_bound = root
                lower_bound_stuck += 1
            else:
                return root, itr, rel

            itr = itr + 1
        return root, itr, rel

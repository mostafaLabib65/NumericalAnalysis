from Roots.Bracketer import Bracketer
import numpy as np


class FalsePosition(Bracketer):

    def __init__(self, function, error=0.0001, max_iterations=50):
        super().__init__(function, error, max_iterations)

    def do(self, lower_bound, upper_bound):
        self.lower = lower_bound
        self.upper = upper_bound
        return self.false_pos(lower_bound, upper_bound)

    def false_pos(self, lower_bound, upper_bound):
        itr, old_root, root, ea = 0, 0, 0, 0
        lower_bound_stuck, upper_bound_stuck = 0, 0

        data = []

        while itr < self.max_iterations:
            f_lower = self.compute(lower_bound)
            f_upper = self.compute(upper_bound)

            if f_lower > 0:
                lower_bound, upper_bound = upper_bound, lower_bound
                f_lower, f_upper = f_upper, f_lower

            if f_lower * f_upper > 0:
                raise Exception("No valid roots in this interval")
            if f_upper - f_lower == 0:
                raise Exception("Division by zero", data)

            if abs(upper_bound_stuck) == 20 or abs(lower_bound_stuck) == 20:
                root = (lower_bound + upper_bound) / 2
                lower_bound_stuck, upper_bound_stuck = 0, 0
            else:
                root = float((lower_bound * f_upper - upper_bound * f_lower) / (f_upper - f_lower))
            f_root = self.compute(root)

            ea = abs(root - old_root)

            record = np.array([itr + 1, lower_bound, f_lower, upper_bound, f_upper, root, f_root, ea])
            data.append(record)

            if ea < self.error and itr > 1:
                try:
                    self.check(root, ea)
                except Exception:
                    root = (lower_bound + upper_bound) / 2
                    continue
                return data

            old_root = root
            if f_root > 0:
                upper_bound = root
                upper_bound_stuck += 1
                lower_bound_stuck = 0
            elif f_root < 0:
                lower_bound = root
                lower_bound_stuck += 1
                upper_bound_stuck = 0
            else:
                return data

            itr = itr + 1
        self.check(root, ea)
        return data

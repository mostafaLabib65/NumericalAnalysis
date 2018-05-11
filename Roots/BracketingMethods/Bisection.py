from Roots.Bracketer import Bracketer
import numpy as np


class Bisection(Bracketer):

    def __init__(self, function, error=0.0001, max_iterations=50):
        super().__init__(function, error, max_iterations)

    def do(self, lower_bound, upper_bound):
        self.upper = upper_bound
        self.lower = lower_bound
        return self.bisect(lower_bound, upper_bound)

    def bisect(self, lower_bound, upper_bound):
        itr, old_root, root, rel = 0, 0, 0, 0
        f_lower = self.compute(lower_bound)
        f_upper = self.compute(upper_bound)

        if f_lower * f_upper > 0:
            raise Exception("No valid roots in this interval")
        data = []
        while itr < self.max_iterations:
            root = (lower_bound + upper_bound) / 2
            f_lower = self.compute(lower_bound)
            f_root = self.compute(root)

            ea = abs(root - old_root)
            rel = abs(ea / root) * 100

            record = np.array([itr + 1, lower_bound, f_lower, upper_bound, f_upper, root, f_root, ea, rel])
            data.append(record)

            if ea < self.error and itr > 1:
                self.check(root, ea)
                return data

            cond = f_lower * f_root

            old_root = root
            if cond < 0:
                upper_bound = root
            elif cond > 0:
                lower_bound = root
            else:
                return data

            itr = itr + 1
        self.check(root, ea)
        return data

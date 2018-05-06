from Roots.BracketingMethods.FalsePosition import FalsePosition
import numpy as np


class RootFinder:
    def __init__(self, function, lower_bound, upper_bound, num_roots, error=0.0001):
        self.function = function
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.num_roots = num_roots
        self.error = error

    def get_roots(self):
        initial_points = []
        ranges = [0.1, 0.3, 1, 3]
        for k in ranges:
            x = np.arange(0, self.upper_bound - self.lower_bound, k)
            for i in range(len(x) - 1):
                f1 = self.function.evaluate(self.lower_bound + x[i])
                f2 = self.function.evaluate(self.lower_bound + x[i+1])

                if f2*f1 < 0:
                    if f2 > 0:
                        initial_points.append(np.array([self.lower_bound + x[i], self.lower_bound + x[i+1]]))
                    else:
                        initial_points.append(np.array([self.lower_bound + x[i+1], self.lower_bound + x[i]]))

            if len(initial_points) == self.num_roots:
                break
            initial_points = []

        if len(initial_points) == 0:
            raise RuntimeError("Could not find all roots")

        false_pos = FalsePosition(self.function, self.error)
        roots = []
        for i in initial_points:
            roots.append(false_pos.do(i[0], i[1]))

        return roots
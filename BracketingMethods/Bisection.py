from Bracketer import Bracketer


class Bisection (Bracketer):

    def __init__(self, function, error=0.0001, max_iterations=50):
        super().__init__(function, error, max_iterations)

    def do(self, lower_bound, upper_bound):
        return self.bisect(lower_bound, upper_bound)

    def bisect(self, lower_bound, upper_bound):
        itr, old_root, root, rel = 0, 0, 0, 0
        f_lower = self.compute(lower_bound)
        f_upper = self.compute(upper_bound)

        if f_lower * f_upper > 0:
            raise Exception("No valid roots in this interval")

        while itr < self.max_iterations:
            root = (lower_bound + upper_bound) / 2
            f_lower = self.compute(lower_bound)
            f_root = self.compute(root)

            ea = abs(root - old_root)
            rel = abs(ea / root) * 100
            if ea < self.error and itr > 1:
                return root, itr, rel

            cond = f_lower * f_root

            old_root = root
            if cond < 0:
                upper_bound = root
            elif cond > 0:
                lower_bound = root
            else:
                return root, itr, rel

            itr = itr + 1
        return root, itr, rel

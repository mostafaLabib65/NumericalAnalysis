import abc
import numpy as np


class Bracketer:

    def __init__(self, function, error=0.0001, max_iterations=50):
        self.function = function
        self.max_iterations = max_iterations
        self.error = error
        self.upper = 0
        self.lower = 0

    def compute(self, xr):
        return self.function.evaluate(xr)

    def get_plot(self):
        x = np.arange(self.lower, self.upper+1, 0.1)
        y = []
        for i in x:
         y.append(self.compute(i))

        return x, y

    @abc.abstractclassmethod
    def do(self, lower_bound, upper_bound):
        return

    def check(self, root, data):
        y = self.compute(root)
        if not(abs(self.compute(root)) < 10*self.error):
            raise Exception("Could not find root", data)


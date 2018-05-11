import abc
import numpy as np


class OpenMethod:

    def __init__(self, function, derivative=None, second_derivative=None, multiplicity=1, error=0.0001
                 , max_iterations=50, gx=None):
        self.function = function
        self.derivative = derivative
        self.second_derivative = second_derivative
        self.multiplicity = multiplicity
        self.error = error
        self.max_iterations = max_iterations
        self.gx = gx
        self.initial = 0
        self.root = 0

    def compute(self, xr):
        return self.function.evaluate(xr)

    def compute_derivative(self, x0):
        if self.derivative is not None:
            return self.derivative.evaluate(x0)
        return None

    def compute_second_derivative(self, x0):
        if self.second_derivative is not None:
            return self.second_derivative.evaluate(x0)
        return None

    def get_plot(self):
        length = self.initial - self.root
        y = []
        if length > 0:
            x = np.arange(self.root - length - 1, self.initial + 1, 0.1)
        else:
            x = np.arange(self.initial - 1, self.root + abs(length) + 1, 0.1)
        for i in x:
            y.append(self.compute(i))

        return x, y

    @abc.abstractclassmethod
    def do(self, *args):
        return

    def check(self, root, err):
        if not(abs(self.compute(root)) < 10*self.error):
            raise Exception("Last found root is: " + str(root) + " with error:" + str(err))


import abc


class Bracketer:

    def __init__(self, function, error=0.0001, max_iterations=50):
        self.function = function
        self.max_iterations = max_iterations
        self.error = error

    def compute(self, xr):
        return self.function.evaluate({"x": xr})

    @abc.abstractclassmethod
    def do(self, lower_bound, upper_bound):
        return

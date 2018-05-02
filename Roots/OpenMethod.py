import abc


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

    def compute(self, xr):
        return self.function.evaluate({"x": xr})

    def compute_derivative(self, x0):
        if self.derivative is not None:
            return self.derivative.evaluate({"x": x0})
        return None

    def compute_second_derivative(self, x0):
        if self.second_derivative is not None:
            return self.second_derivative.evaluate({"x": x0})
        return None

    @abc.abstractclassmethod
    def do(self, *args):
        return

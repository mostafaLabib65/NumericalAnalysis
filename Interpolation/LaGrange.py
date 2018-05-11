from Interpolation.Interpolator import Interpolator
from numpy import *


class LaGrange(Interpolator):

    def __init__(self, values, order):
        super().__init__(values, order)

    def do(self, x):
        return self.interpolate(x)

    def interpolate(self, x):

        y = 0
        for i in range(shape(self.values)[0]):
            numerator = 1
            denominator = 1
            for j in range(shape(self.values)[0]):
                if j == i:
                    continue
                numerator *= (x - self.values[j][0])
                denominator *= (self.values[i][0] - self.values[j][0])
            y += (numerator * self.values[i][1] / denominator)
        return y

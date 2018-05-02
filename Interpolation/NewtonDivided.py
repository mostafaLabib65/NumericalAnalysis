from Interpolation.Interpolator import Interpolator
from numpy import *


class NewtonDivided(Interpolator):

    def __int__(self, values):
        super().__init__(values)

    def do(self, x):
        return self.interpolate(x)

    def interpolate(self, x):
        n = shape(self.values)[0]
        b = []
        for i in range(n+1):
            b.append([])

        for v in range(n):
            b[0].append(self.values[v][0])
        for v in range(n):
            b[1].append(self.values[v][1])

        for k in range(2, len(b)):
            shift = k - 1
            for i in range(shift, len(b[0])):
                b[k].append(b[0][i] - b[0][i - shift])
            for i in range(1, len(b[k-1])):
                b[k][i - 1] = (b[k-1][i] - b[k-1][i - 1]) / b[k][i - 1]
        inter = b[1][0]
        mul = 1
        for i in range(n - 1):
            mul *= (x - b[0][i])
            inter += b[i+1][0] * mul
        return inter

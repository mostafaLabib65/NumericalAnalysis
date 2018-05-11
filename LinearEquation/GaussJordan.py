from numpy import *


class GaussJordan:

    def __init__(self, values):
        self.values = values

    def solve(self):
        rows = shape(self.values)[0]
        cols = shape(self.values)[1]
        if not(rows+1 == cols):
            raise Exception("Can't solve")
        
        for k in range(rows):
            shift = k
            for i in range(rows):
                if i == k:
                    continue
                factor = self.values[i][shift]/self.values[k][shift]
                for j in range(shift, cols):
                    self.values[i][j] -= factor * self.values[k][j]
        values = []
        for k in range(rows):
            values.append(self.values[k][cols-1] / self.values[k][k])
        return values

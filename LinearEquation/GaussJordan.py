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
                if self.values[k][shift] == 0:
                    raise Exception("Division by zero")
                factor = self.values[i][shift]/self.values[k][shift]
                for j in range(shift, cols):
                    self.values[i][j] -= factor * self.values[k][j]
        values = []

        zero_flag = True
        for k in self.values[-1, :-1]:
            if k == 0.0:
                continue
            else:
                zero_flag = False
                break

        if zero_flag:
            raise Exception("No unique solution")

        for k in range(rows):
            values.append(self.values[k][cols-1] / self.values[k][k])
        return values

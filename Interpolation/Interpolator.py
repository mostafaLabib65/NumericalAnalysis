import abc
import numpy as np

class Interpolator:

    def __init__(self, values):
        self.values = values
        self.sort()

    @abc.abstractclassmethod
    def do(self, x):
        return

    def sort(self):
        flag = True

        while flag:
            flag = False
            for i in range(0, np.shape(self.values)[0] - 1):
                if self.values[i][0] > self.values[i+1][0]:
                    temp = self.values[i][0]
                    self.values[i][0] = self.values[i+1][0]
                    self.values[i+1][0] = temp

                    temp = self.values[i][1]
                    self.values[i][1] = self.values[i + 1][1]
                    self.values[i + 1][1] = temp

                    flag = True


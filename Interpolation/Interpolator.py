import abc
import numpy as np


class Interpolator:

    def __init__(self, values, order):
        self.values = values
        self.order = order
        self.sort()
        self.splice()

    @abc.abstractclassmethod
    def do(self, x):
        return

    def splice(self):
        if self.order >= np.shape(self.values)[0]:
            raise Exception("Can't interpolate")

        self.values = self.values[:self.order + 1, :]

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


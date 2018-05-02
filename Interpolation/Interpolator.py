import abc


class Interpolator:

    def __init__(self, values):
        self.values = values

    @abc.abstractclassmethod
    def do(self, x):
        return

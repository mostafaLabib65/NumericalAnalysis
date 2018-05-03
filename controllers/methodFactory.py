from models.BisectionPlot import BisectionPlot
from views.Result import Result


class DummyMethod(object):
    # example of a method
    def __init__(self, observer, eq_str, *args, **kwargs):
        super().__init__()
        self.observer = observer
        self.eq_str = eq_str
        ys = [-1, 25, -40, -30, -25, -18, 0, 15, -2, 23, 14, 0, 6, 8]
        xs = [-10, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
        xl = [0, 0, 2.25, 3.5]
        xu = [9, 4.5, 4.5, 4.5, 4.5]
        xr = [4.5, 2.25, 3.5, 4]
        self.fig = BisectionPlot(xs, ys, xr, xl, xu, *args, **kwargs)

        self.result = Result(solution="I am Groot", status="I am status Groot", figure=self.fig, iterations=3,
                             message="We are groot")

    def execute(self):
        self.observer.notify(self.result)


class MethodFactory:
    @staticmethod
    def acquire_method(method, observer, eq_str, *args, **kwargs):
        # insert models here, send parameters
        return {
            "Fixed Point": DummyMethod(observer, eq_str, *args, **kwargs)
        }[method]

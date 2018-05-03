from models.fixedpointplot import FixedPointPlot
from views.Result import Result


class DummyMethod(object):
    #example of a method
    def __init__(self, observer, eq_str, *args, **kwargs):
        super().__init__()
        self.observer = observer
        self.eq_str = eq_str
        ys = [1, .81, .43, .25, .04, 0, .04, .25, .43, .81, 1]
        xs = [-1, -.9, -.656, -.5, -.2, 0, .2, .5, .656, .9, 1]
        gx = [0.81, .656, .43, .1853, 0.03433, 0]
        x = [.9, 0.81, .656, .43, .1853, 0.03433]
        self.fig = FixedPointPlot(xs, ys, gx, x, *args, **kwargs)
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

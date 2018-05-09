from models.BisectionPlot import BisectionPlot
from models.FalsePositionPlot import FalsePositionPlot
from models.fixedpointplot import FixedPointPlot
from models import BirgeVieta
from views.Result import Result
from Roots.Differentiator import Differentiator
import numpy as np
from Roots.BracketingMethods.Bisection import Bisection as bisector
from Roots.BracketingMethods.FalsePosition import FalsePosition as falsePositioner
from Roots.OpenMethods.FixedPoint import FixedPoint as fixedPointer
from Roots.OpenMethods.BirgeVieta import BirgeVieta as birgeVietaer
from Roots.Bracketer import Bracketer
class Bisection(object):
    # example of a method
    def __init__(self, observer, eq_str, *args, **kwargs):
        super().__init__()
        self.observer = observer
        self.eq_str = eq_str
        print(eq_str)

        diff = Differentiator(eq_str)
        bis = bisector(diff.get_function())
        data = bis.do(0,7)
        xs,ys = bis.get_plot()
        xl = []
        xu = []
        xr = []
        for i in data:
            xl.append(i[1])
            xu.append(i[3])
            xr.append(i[5])
        lastIterationData = data.pop()
        solution = lastIterationData[5]
        iterations = lastIterationData[0]
        self.fig = BisectionPlot(xs, ys, xr, xl, xu, *args, **kwargs)
        self.result = Result(solution=str(solution), status="I am status Groot", figure=self.fig, iterations=iterations,
                             message="We are groot")

    def execute(self):
        self.observer.notify(self.result)
class FalsePosition(object):
    # example of a method
    def __init__(self, observer, eq_str, *args, **kwargs):
        super().__init__()
        self.observer = observer
        self.eq_str = eq_str
        diff = Differentiator(eq_str)
        falPosition = falsePositioner(diff.get_function())
        data = falPosition.do(0,7)
        xs,ys = falPosition.get_plot()
        xl = []
        xu = []
        xr = []
        Fxl = []
        Fxu = []
        for i in data:
            xl.append(i[1])
            xu.append(i[3])
            xr.append(i[5])
            Fxl.append((i[2]))
            Fxu.append(i[4])
        lastIterationData = data.pop()
        solution = lastIterationData[5]
        iterations = lastIterationData[0]
        self.fig = FalsePositionPlot(xs, ys, xr, xl,Fxl ,xu,Fxu, *args, **kwargs)
        self.result = Result(solution=str(solution), status="I am status Groot", figure=self.fig, iterations=iterations,
                             message="We are groot")

    def execute(self):
        self.observer.notify(self.result)

class BirgeVieta(object):
    # example of a method
    def __init__(self, observer, eq_str, *args, **kwargs):
        super().__init__()
        self.observer = observer
        self.eq_str = eq_str
        diff = Differentiator(eq_str)
        birgeVieta = birgeVietaer(diff.get_function())
        data = birgeVieta.do(9)
        xs,ys = birgeVieta.get_plot()
        '''xl = []
        xu = []
        xr = []
        Fxl = []
        Fxu = []
        for i in data:
            xl.append(i[1])
            xu.append(i[3])
            xr.append(i[5])
            Fxl.append((i[2]))
            Fxu.append(i[4])'''
        lastIterationData = data.pop()
        solution = lastIterationData[4]
        iterations = lastIterationData[0]
        self.fig = BirgeVieta
        self.result = Result(solution=str(solution), status="I am status Groot", figure=self.fig, iterations=iterations,
                             message="We are groot")

    def execute(self):
        self.observer.notify(self.result)


class FixedPoint(object):
    # example of a method
    def __init__(self, observer, eq_str, *args, **kwargs):
        super().__init__()
        self.observer = observer
        self.eq_str = eq_str
        diff = Differentiator(eq_str)
        fixPoint = fixedPointer(diff.get_function(),diff.get_first_derivative())
        data = fixPoint.do(1)
        xs,ys = fixPoint.get_plot()
        xi = []
        gx = []
        for i in data:
            xi.append(i[1])
            gx.append(i[3])
        lastIterationData = data.pop()
        solution = lastIterationData[3]
        iterations = lastIterationData[0]
        self.fig = FixedPointPlot(xs, ys, gx,xi, *args, **kwargs)
        self.result = Result(solution=str(solution), status="I am status Groot", figure=self.fig, iterations=iterations,
                             message="We are groot")

    def execute(self):
        self.observer.notify(self.result)

class MethodFactory:
    @staticmethod
    def acquire_method(method, observer, eq_str, *args, **kwargs):
        # insert models here, send parameters
        return {
            "Bisection": Bisection(observer, eq_str, *args, **kwargs),
            "False-Position": FalsePosition(observer, eq_str, *args, **kwargs)
            #"Fixed Point": FixedPoint(observer, eq_str, *args, **kwargs)
          #  "Bierge Vieta": BirgeVieta(observer, eq_str, *args, **kwargs)
        }[method]

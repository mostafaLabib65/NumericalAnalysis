from models.BisectionPlot import BisectionPlot
from models.FalsePositionPlot import FalsePositionPlot
from models.fixedpointplot import FixedPointPlot
from models.NewtonRaphsonPlot import NewtonRaphsonPlot
from models.SecantPlot import SecantPlot
from views.Result import Result
from Roots.Differentiator import Differentiator
from Roots.BracketingMethods.Bisection import Bisection as bisector
from Roots.BracketingMethods.FalsePosition import FalsePosition as falsePositioner
from Roots.OpenMethods.FixedPoint import FixedPoint as fixedPointer
from Roots.OpenMethods.BirgeVieta import BirgeVieta as birgeVietaer
from Roots.OpenMethods.Newton import Newton as newKg   ## ma7adesh yeshtem
from Roots.OpenMethods.Secant import Secant as secant

class Bisection(object):
    def __init__(self, observer, eq_str, start_str, end_str,*args, **kwargs):
        super().__init__()
        self.observer = observer
        self.eq_str = eq_str
        print(eq_str)

        diff = Differentiator(eq_str)
        bis = bisector(diff.get_function())
        start = float(start_str)
        end = float(end_str)
        data = bis.do(start,end)
        xs,ys = bis.get_plot()
        xl = []
        xu = []
        xr = []
        for i in data:
            xl.append(i[1])
            xu.append(i[3])
            xr.append(i[5])
        print(xl)
        lastIterationData = data.pop()
        solution = lastIterationData[5]
        iterations = lastIterationData[0]
        self.fig = BisectionPlot(xs, ys, xr, xl, xu, *args, **kwargs)
        self.result = Result(solution=str(solution), status="I am status Groot", figure=self.fig, iterations=iterations,
                             message="We are groot",data = data)

    def execute(self):
        self.observer.notify(self.result)

class FalsePosition(object):
    def __init__(self, observer, eq_str, start_str, end_str,*args, **kwargs):
        super().__init__()
        self.observer = observer
        self.eq_str = eq_str
        diff = Differentiator(eq_str)
        falPosition = falsePositioner(diff.get_function())
        data = falPosition.do(float(start_str),float(end_str))
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
                             message="We are groot",data = data)

    def execute(self):
        self.observer.notify(self.result)

class BirgeVieta(object):
    def __init__(self, observer, eq_str, start_str,*args, **kwargs):
        super().__init__()
        self.observer = observer
        self.eq_str = eq_str
        diff = Differentiator(eq_str)
        birgeVieta = birgeVietaer(diff.get_function())
        data = birgeVieta.do(float(start_str))
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
                             message="We are groot",data = data)

    def execute(self):
        self.observer.notify(self.result)

class FixedPoint(object):
    def __init__(self, observer, eq_str, start_str,*args, **kwargs):
        super().__init__()
        self.observer = observer
        self.eq_str = eq_str
        diff = Differentiator(eq_str)
        fixPoint = fixedPointer(diff.get_function(),diff.get_first_derivative())
        data = fixPoint.do(float(start_str))
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
        self.result = Result(solution=str(solution), status="done", figure=self.fig, iterations=iterations,
                             message="We are groot",data = data)

    def execute(self):
        self.observer.notify(self.result)

class Newton(object):
    def __init__(self, observer, eq_str, start_str,*args, **kwargs):
        super().__init__()
        self.observer = observer
        self.eq_str = eq_str
        diff = Differentiator(eq_str)
        newton = newKg(diff.get_function(),diff.get_first_derivative(),diff.get_second_derivative())
        data = newton.do(float(start_str))
        xs,ys = newton.get_plot()
        xr = []
        x = []
        fx = []
        for i in data:
            xr.append(float(i[4]))
            x.append(float(i[1]))
            fx.append(float(i[2]))
        lastIterationData = data.pop()
        solution = lastIterationData[4]
        iterations = lastIterationData[0]
        self.fig = NewtonRaphsonPlot(xs, ys, xr,x,fx, *args, **kwargs)
        self.result = Result(solution=str(solution), status="done", figure=self.fig, iterations=iterations,
                             message="We are groot", data = data)

    def execute(self):
        self.observer.notify(self.result)

class Secant(object):
    def __init__(self, observer, eq_str, start_str, end_str,*args, **kwargs):
        super().__init__()
        self.observer = observer
        self.eq_str = eq_str
        diff = Differentiator(eq_str)
        sec = secant(diff.get_function())
        data = sec.do(float(start_str),float(end_str))
        xs, ys = sec.get_plot()
        xr = []
        xl = []
        fxl = []
        xbl = []
        fxbl = []
        for i in data:
            xr.append(float(i[5]))
            xl.append(float(i[1]))
            fxl.append(float(i[2]))
            xbl.append(float(i[3]))
            fxbl.append(float(i[4]))
        lastIterationData = data.pop()
        solution = lastIterationData[5]
        iterations = lastIterationData[0]
        self.fig = SecantPlot(xs, ys, xr, xl, fxl,xbl,fxbl, *args, **kwargs)
        self.result = Result(solution=str(solution), status="done", figure=self.fig, iterations=iterations,
                             message="We are groot",data = data)


    def execute(self):
        self.notify(self.resul)



class MethodFactory:
    @staticmethod
    def acquire_method(method, observer, eq_str,start_str, end_str, *args, **kwargs):
        if (method == "Bisection"):
            return Bisection(observer, eq_str, start_str, end_str,*args, **kwargs)
        elif(method == "False-Position"):
            return FalsePosition(observer, eq_str, start_str, end_str,*args, **kwargs)
        elif(method == "Fixed Point"):
            return FixedPoint(observer, eq_str, start_str,*args, **kwargs)
        elif(method == "Bierge Vieta"):
            return BirgeVieta(observer, eq_str, start_str,*args, **kwargs)
        elif (method == "Newton"):
            return Newton(observer, eq_str, start_str,*args, **kwargs)
        elif (method == "Secant"):
            return Secant(observer, eq_str, start_str, end_str,*args, **kwargs)



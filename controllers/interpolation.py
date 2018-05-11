from views.Result import Result
from views.FileParameters import FileParameters
from Interpolation.LaGrange import LaGrange
from Interpolation.NewtonDivided import NewtonDivided
import numpy as np
from models.NormalFunction import NormalFunction
class Lagrange(object):
    def __init__(self, method, observer, numberOfPoints, xInput, yInput, queryPoints):
        super().__init__()
        self.observer = observer
        if xInput[0] == '[':
            x = xInput[1:len(xInput)-1].split(',')
            y = yInput[1:len(yInput) -1].split(',')
        else:
            x = xInput.split(',')
            y = yInput.split(',')
        values = []
        for i in range(0,len(x)):
            x[i] = float(x[i])

        values.append(x)
        for i in range(0,len(y)):
            y[i] = float(y[i])
        values.append(y)
        grange = LaGrange(values, int(numberOfPoints))
        if queryPoints[0] == '[':
            points = queryPoints[1:len(queryPoints) - 1].split(',')
        else:
            points = queryPoints.split(',')
        for i in range(0,len(points)):
            points[i] = float(points[i])
        results = []
        xs = np.arange(x[0],x[-1],0.1)
        ys = []
        for i in xs:
            ys.append(grange.do(i))

        for i in points:
            results.append(grange.do(i))
        self.fig = NormalFunction(xs, ys)
        self.result = Result(solution=results, status="I am status Groot",figure = self.fig,
                             message="We are groot")
    def execute(self):
        self.observer.notify(self.result)


class Newton(object):
    def __init__(self, method, observer, numberOfPoints, xInput, yInput, queryPoints):
        super().__init__()
        self.observer = observer
        if xInput[0] == '[':
            x = xInput[1:len(xInput)-1].split(',')
            y = yInput[1:len(yInput) -1].split(',')
        else:
            x = xInput.split(',')
            y = yInput.split(',')
        values = []
        for i in range(0, len(x)):
            x[i] = float(x[i])

        values.append(x)
        for i in range(0, len(y)):
            y[i] = float(y[i])
        values.append(y)
        newKg = NewtonDivided(values, int(numberOfPoints))
        if queryPoints[0] == '[':
            points = queryPoints[1:len(queryPoints) - 1].split(',')
        else:
            points = queryPoints.split(',')
        for i in range(0, len(points)):
            points[i] = float(points[i])
        results = []
        xs = np.arange(x[0], x[-1], 0.1)
        ys = []
        for i in xs:
            ys.append(newKg.do(i))

        for i in points:
            results.append(newKg.do(i))
        self.fig = NormalFunction(xs, ys)
        self.result = Result(solution=results, status="I am status Groot",figure = self.fig,
                             message="We are groot")

    def execute(self):
        self.observer.notify(self.result)


class InterPolationFactory:
    @staticmethod
    def acquire_method(method, observer, numberOfPoints, xInput, yInput, queryPoints):
        if (method == "Lagrange"):
            return Lagrange(method, observer, numberOfPoints, xInput, yInput, queryPoints)
        elif (method == "Newton devider"):
            return Newton(method, observer, numberOfPoints, xInput, yInput, queryPoints)

    @staticmethod
    def readFromFile(fileName, observer, **kwargs):
        with open(fileName) as f:
            lines = f.readlines()
        for i in range(0, len(lines)):
            lines[i] = lines[i].strip("\n")
        ## equation = numberOfPoints
        ## start = x input
        ## End = Y input
        ## tolerance = query points
        parameters = FileParameters(method=InterPolationFactory.getMethod(lines[1]), equation=lines[2], start=lines[3],
                                    End=lines[4], tolerance=lines[5], **kwargs)

        observer.notifyFileParameters(parameters)

    def getMethod(number):
        if (number == "1"):
            return "Lagrange"
        elif (number == "2"):
            return "Newton devider"

from views.Result import Result
from views.FileParameters import FileParameters
from Interpolation.LaGrange import LaGrange
from Interpolation.NewtonDivided import NewtonDivided

class Lagrange(object):
    def __init__(self, method, observer, numberOfPoints, xInput, yInput, queryPoints):
        super().__init__()
        self.observer = observer
        x = xInput.split()
        y = yInput.split()
        values = []
        for i in range(0,len(x)):
            x[i] = float(x[i])

        values.append(x)
        for i in range(0,len(y)):
            y[i] = float(y[i])
        values.append(y)
        grange = LaGrange(values, float(numberOfPoints))
        queries = []
        for i in queryPoints.split():
            queries.append(float[i])
        results = []
        for i in queries:
            results.append(grange.do(i))
        self.result = Result(solution=results, status="I am status Groot",
                             message="We are groot")
    def execute(self):
        self.observer.notify(self.result)


class Newton(object):
    def __init__(self, method, observer, numberOfPoints, xInput, yInput, queryPoints):
        super().__init__()
        self.observer = observer
        x = xInput.split()
        y = yInput.split()
        values = []
        for i in range(0, len(x)):
            x[i] = float(x[i])

        values.append(x)
        for i in range(0, len(y)):
            y[i] = float(y[i])
        values.append(y)
        newKG = NewtonDivided(values, float(numberOfPoints))
        queries = []
        for i in queryPoints.split():
            queries.append(float[i])
        results = []
        for i in queries:
            results.append(newKG.do(i))
        self.result = Result(solution=results, status="I am status Groot",
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

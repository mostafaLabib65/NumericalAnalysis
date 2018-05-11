from views.Result import Result
from views.FileParameters import FileParameters


class Lagrange(object):
    def __init__(self, method, observer, numberOfPoints, xInput, yInput, queryPoints):
        ## do the logic here
        return 0


class Newton(object):
    def __init__(self, method, observer, numberOfPoints, xInput, yInput, queryPoints):
        ## do the logic here
        return 0


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

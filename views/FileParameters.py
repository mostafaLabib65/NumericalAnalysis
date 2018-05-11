class FileParameters:
    def __init__(self, method=None, equation=None, start=None, End=None, tolerance=None, maxItr=None, observer=None,
                 widget=None, app=None):
        self.equation = equation
        self.start = start
        self.End = End
        self.tolerance = tolerance
        self.maxItr = maxItr
        self.parameters = {
            "method": None if method is None else method.currentText(),
            "observer": observer,
            "eq_str": None if equation is None else equation.text(),
            "start_str": None if start is None else start.text(),
            "end_str": None if End is None else End.text(),
            "tolerance": None if tolerance is None else tolerance.text(),
            "maxItr": None if maxItr is None else maxItr.text(),
            "parent": widget,
            "app": app
        }

    def parameters(self):
        return self.parameters

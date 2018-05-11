class FileParameters:
    def __init__(self, method=None, equation=None, start=None, End=None, tolerance=None, maxItr=None, observer=None,
                 widget=None, app=None):
        self.equation = equation
        self.start = start
        self.End = End
        self.tolerance = tolerance
        self.maxItr = maxItr
        self.method = method
        self.observer = observer
        self.parameters = {
            "method": None if method is None else method,
            "observer": observer,
            "eq_str": None if equation is None else equation,
            "start_str": None if start is None else start,
            "end_str": None if End is None else End,
            "tolerance": None if tolerance is None else tolerance,
            "maxItr": None if maxItr is None else maxItr,
            "parent": widget,
            "app": app
        }

    def parameters(self):
        return self.parameters

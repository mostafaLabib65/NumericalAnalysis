class Result:
    def __init__(self, solution=None, status=None, figure=None, iterations=None, message=None):
        self.message = message
        self.iterations = iterations
        self.figure = figure
        self.status = status
        self.solution = solution

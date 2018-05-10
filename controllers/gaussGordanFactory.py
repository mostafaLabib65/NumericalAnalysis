from views.Result import Result
from LinearEquation.GaussJordan import GaussJordan
from views.FileParameters import FileParameters


class GaussSolver:
    def __init__(self, observer, eq_str):
        super().__init__()
        self.observer = observer
        self.eq_str = eq_str
        values = []
        print(len(values))
        data = eq_str.splitlines()
        for i in range(0, len(data)):
            data[i] = data[i].split()
            for j in range(0,len(data[i])):
                data[i][j] = float(data[i][j])
        gauss = GaussJordan(data)
        roots = gauss.solve()
        self.result = Result(solution=roots ,status="I am status Groot",
                             message="We are groot")
    def execute(self):
        self.observer.notify(self.result)

class GaussGordan:
    @staticmethod
    def acquire_method(observer, eq_str):
        return GaussSolver(observer,eq_str)

    @staticmethod
    def readFromFile(fileName,observer):
        with open(fileName) as f:
            lines = f.read()
        parameters = FileParameters(equation = lines)
        observer.notifyFileParameters(parameters)

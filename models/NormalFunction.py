from matplotlib import style

from qtpy import QtCore

from models.PlotFigure import PlotFigure

style.use('fivethirtyeight')


class NormalFunction(PlotFigure):
    def __init__(self,xs, ys,app=None, parent=None, width=5, height=4, dpi=100):
        PlotFigure.__init__(self, parent, width, height, dpi)
        self.animateTimer = QtCore.QTimer(self)
        self.animateTimer.timeout.connect(self.update_figure)
        self.xs = xs
        self.ys = ys
        self.parent = parent
        self.app = app
        self.axes.plot(self.xs, self.ys, label='function', color='r', lw=2)
        self.axes.axvline(x=0,lw=2,color='b')
        self.axes.axhline(y=0,lw=2,color='b')
        self.axes.legend()
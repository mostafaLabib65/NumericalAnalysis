from matplotlib import style
import numpy as np

from qtpy import QtCore

from models.PlotFigure import PlotFigure

style.use('fivethirtyeight')


class BisectionPlot(PlotFigure):
    def __init__(self, xs,ys,xr, xl, xu, app=None, parent=None, width=5, height=4, dpi=100):
        PlotFigure.__init__(self, parent, width, height, dpi)
        self.animateTimer = QtCore.QTimer(self)
        self.animateTimer.timeout.connect(self.update_figure)
        self.xs = xs
        self.ys = ys
        self.xr = xr
        self.xu = xu
        self.xl = xl
        self.generator = self.points_generator()
        self.parent = parent
        self.app = app
        self.axes.plot(self.xs, self.ys, label='function', color='r', lw=3)
        self.axes.legend()


    def animate(self):
        self.animateTimer.start(1000)

    def compute_initial_figure(self):
        self.axes.axvline(x=0, lw=4, color='k', label='axes')
        self.axes.axhline(y=0, lw=4, color='k')
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')
        self.axes.set_title('Bisection point method')

    def points_generator(self):
        for i in range(0,len(self.xr)):
            yield i

    def update_figure(self):
        self.animateTimer.blockSignals(True)
        try:
            i = next(self.generator)
        except StopIteration:
            self.axes.axvline(self.xr[len(self.xr) - 1], lw=1, color='g', linestyle='dashed', label='vertical')
            self.axes.axvline(self.xl[len(self.xr) - 1], lw=1, color='b', linestyle='dashed', label='vertical')
            self.axes.axvline(self.xu[len(self.xr) - 1], lw=1, color='b', linestyle='dashed', label='vertical')
            self.draw()
            self.axes.legend()
            return
        if i != len(self.xr) - 1:
            if self.xl[i] == self.xl[i + 1]:
                self.animateLine(self.xu[i], self.xu[i + 1], self.xl[i], self.xs, self.ys)
            else:
                self.animateLine(self.xl[i], self.xl[i + 1], self.xu[i], self.xs, self.ys)
            self.axes.axvline(x=self.xr[i + 1], label='Xr', color='g', linestyle='dashed', lw=1)
        self.draw()

        self.animateTimer.blockSignals(False)


    def animateLine(self,x1, x2, constX, xs, ys):
        self.axes.cla()
        x = np.linspace(float(x1), float(x2), 20)

        for n in range(len(x)):
            self.axes.cla()
            self.axes.set(xlabel='x', ylabel='y', title='Bisection method')
            self.axes.axvline(x=0, lw=4, color='k', label='axes')
            self.axes.axhline(y=0, lw=4, color='k')
            self.axes.plot(xs, ys, label='function', color='r', lw=3)
            self.axes.axvline(x[n], lw=1, color='b', linestyle='dashed', label='vertical')
            self.axes.axvline(constX, lw=1, color='b', linestyle='dashed', label='vertical')
            self.draw()
            self.app.processEvents()


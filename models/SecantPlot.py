from matplotlib import style
import numpy as np

from qtpy import QtCore

from models.PlotFigure import PlotFigure

style.use('fivethirtyeight')


class SecantPlot(PlotFigure):
    def __init__(self, xs, ys, xr, xl, Fxl, xbl, Fxbl, app=None, parent=None, width=5, height=4, dpi=100):
        PlotFigure.__init__(self, parent, width, height, dpi)
        self.animateTimer = QtCore.QTimer(self)
        self.animateTimer.timeout.connect(self.update_figure)
        self.xs = xs
        self.ys = ys
        self.xr = xr
        self.xl = xl
        self.Fxl = Fxl
        self.Fxbl = Fxbl
        self.xbl = xbl
        self.generator = self.points_generator()
        self.parent = parent
        self.app = app
        self.axes.plot(self.xs, self.ys, label='function', color='r', lw=3)
        self.axes.legend

    def animate(self):
        self.animateTimer.start(1000)

    def compute_initial_figure(self):
        self.axes.axvline(x=0, lw=4, color='k', label='axes')
        self.axes.axhline(y=0, lw=4, color='k')
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')
        self.axes.set_title('secant method')

    def points_generator(self):
        for i in range(len(self.xr)):
            yield i

    def update_figure(self):
        self.animateTimer.blockSignals(True)
        try:
            i = next(self.generator)
        except StopIteration:
            i = len(self.xr) - 1
            if self.Fxbl[i] * self.Fxl[i] < 0:
                self.axes.plot([self.xl[i], self.xbl[i]], [self.Fxl[i], self.Fxbl[i]], color='g', lw=1,
                               linestyle='dashed')
            else:
                if abs(self.Fxl[i]) > abs(self.Fxbl[i]):
                    self.axes.plot([self.xl[i], self.xr[i]], [self.Fxl[i], 0], color='g', lw=1, linestyle='dashed')
                else:
                    self.axes.plot([self.xbl[i], self.xr[i]], [self.Fxbl[i], 0], color='g', lw=1, linestyle='dashed')
            self.axes.axvline(self.xr[len(self.xr) - 1], lw=1, color='b', linestyle='dashed', label='vertical')
            self.draw()
            return
        if self.Fxbl[i] * self.Fxl[i] < 0:
            self.animateLine(self.xl[i], self.xbl[i], self.Fxl[i], self.Fxbl[i], self.xr[i], self.xs, self.ys)
        else:
            if abs(self.Fxl[i]) > abs(self.Fxbl[i]):
                self.animateLine(self.xl[i], self.xr[i], self.Fxl[i], 0, self.xr[i], self.xs, self.ys)
            else:
                self.animateLine(self.xbl[i], self.xr[i], self.Fxbl[i], 0, self.xr[i], self.xs, self.ys)
        self.axes.axvline(self.xr[i], lw=1, color='b', linestyle='dashed', label='vertical')
        self.draw()
        self.animateTimer.blockSignals(False)

    def animateLine(self, x1, x2, y1, y2, xr, xs, ys):
        self.axes.cla()
        y = np.linspace(float(y1), float(y2), 10)
        x = np.linspace(float(x1), float(x2), 10)
        for n in range(len(x) + 1):
            self.axes.cla()
            self.axes.axvline(x=0, lw=2, color='k')
            self.axes.axhline(y=0, lw=2, color='k')
            self.axes.plot(xs, ys, color='r', lw=2)
            self.axes.plot(x[:n], y[:n], color='g', lw=1, linestyle='dashed')
            self.draw()
            self.app.processEvents()
        self.axes.axvline(xr, lw=1, color='b', linestyle='dashed', label='vertical')
        self.draw()

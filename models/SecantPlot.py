from matplotlib import style
import numpy as np

from qtpy import QtCore

from models.PlotFigure import PlotFigure

style.use('fivethirtyeight')


class SecantPlot(PlotFigure):
    def __init__(self, xs, ys, gx, x, app=None, parent=None, width=5, height=4, dpi=100):
        PlotFigure.__init__(self, parent, width, height, dpi)
        self.animateTimer = QtCore.QTimer(self)
        self.animateTimer.timeout.connect(self.update_figure)
        self.xs = xs
        self.ys = ys
        self.hLinesX = [x[0]] * (len(x) + len(gx) + 1)
        self.hLinesX[1::2], self.hLinesX[2::2] = x, gx
        self.hLinesY = [0] * (len(gx) + len(gx) + 1)
        self.hLinesY[1::2], self.hLinesY[2::2] = gx, gx
        self.generator = self.points_generator()
        self.parrent = parent
        self.app = app
        self.axes.plot(self.xs, self.ys, label='function', color='r', lw=3)
        self.axes.plot(self.xs, self.xs, label='x=y', color='y', lw=3)
        self.axes.legend


    def animate(self):
        self.animateTimer.start(100)

    def compute_initial_figure(self):
        self.axes.axvline(x=0, lw=4, color='k', label='axes')
        self.axes.axhline(y=0, lw=4, color='k')
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')
        self.axes.set_title('fixed point method')

    def points_generator(self):
        for i in range(len(self.hLinesX) - 1):
            yield i

    def update_figure(self):
        self.animateTimer.blockSignals(True)
        try:
            i = next(self.generator)
        except StopIteration:
            return
        if self.hLinesX[i] is self.hLinesY[i]:
            self.animate_vertical(self.hLinesY[i], self.hLinesY[i + 1], self.hLinesX[i], self.hLinesX[:i + 1],
                                  self.hLinesY[:i + 1], self.xs, self.ys)

        else:
            self.animate_horizontal(self.hLinesX[i], self.hLinesX[i + 1], self.hLinesY[i], self.hLinesX[:i + 1],
                                    self.hLinesY[:i + 1], self.xs, self.ys)

        self.animateTimer.blockSignals(False)

    def animate_horizontal(self, x1, x2, constY, hLinesX, hLinesY, xs, ys):
        self.axes.cla()
        x = np.linspace(x1, x2, 4)
        y = [constY] * (len(x) + 1)
        self.axes.set(xlabel='x', ylabel='y', title='fixed point method')
        self.axes.axvline(x=0, lw=4, color='k', label='axes')
        self.axes.axhline(y=0, lw=4, color='k')
        self.axes.plot(xs, ys, label='function', color='r', lw=3)
        self.axes.plot(xs, xs, label='x=y', color='y', lw=3)
        self.axes.plot(hLinesX, hLinesY, label='fixed point line', color='b', lw=1, linestyle='dashed')

        for n in range(len(x) + 1):
            self.axes.plot(x[:n], y[:n], color='b', lw=1, linestyle='dashed')
            self.draw()
            self.app.processEvents()

    def animate_vertical(self, y1, y2, constX, hLinesX, hLinesY, xs, ys):
        self.axes.cla()
        y = np.linspace(y1, y2, 4)
        x = [constX] * (len(y) + 1)
        self.axes.set(xlabel='x', ylabel='y', title='fixed point method')
        self.axes.axvline(x=0, lw=4, color='k', label='axes')
        self.axes.axhline(y=0, lw=4, color='k')
        self.axes.plot(xs, ys, label='function', color='r', lw=3)
        self.axes.plot(xs, xs, label='x=y', color='y', lw=3)
        self.axes.plot(hLinesX, hLinesY, label='fixed point line', color='b', lw=1, linestyle='dashed')

        for n in range(len(x)):
            self.axes.plot(x[:n], y[:n], color='b', lw=1, linestyle='dashed')
            self.draw()
            self.app.processEvents()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')


def animateLine(x1, x2, constX, xs, ys):
    x = np.linspace(x1, x2, 20)
    for n in range(len(x)):
        plt.ion()
        plt.show()
        plt.axvline(x=0, lw=2, color='k')
        plt.axhline(y=0, lw=2, color='k')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.plot(xs, ys, color='r', lw=2)
        plt.title('bisection method')
        plt.axvline(x[n], lw=1, color='b', linestyle='dashed', label='vertical')
        plt.axvline(constX, lw=1, color='b', linestyle='dashed', label='vertical')
        plt.pause(0.05)
        plt.cla()


def animateBisection(xs, ys, xr, xl, xu):
    for i in range(len(xr)):
        plt.show()
        plt.axvline(x=0, lw=2, color='k', label='axes')
        plt.axhline(y=0, lw=2, color='k')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('bisection method')
        plt.plot(xs, ys, label='function', color='r', lw=2)
        plt.axvline(x=xr[i], label='Xr', color='g', linestyle='dashed', lw=1)
        plt.axvline(x=xl[i], label='Xlower', color='b', lw=1, linestyle='dashed')
        plt.axvline(x=xu[i], label='Xupper', color='b', lw=1, linestyle='dashed')
        plt.pause(0.5)
        if i != len(xr) - 1:
            if xl[i] == xl[i + 1]:
                animateLine(xu[i], xu[i + 1], xl[i], xs, ys)
            else:
                animateLine(xl[i], xl[i + 1], xu[i], xs, ys)
        plt.legend()
    plt.ioff()
    plt.show()


y = [-1, 25, -40, -30, -25, -18, 0, 15, -2, 23, 14, 0, 6, 8]
x = [-10, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
xl = [0, 0, 2.25, 3.5]
xu = [9, 4.5, 4.5, 4.5, 4.5]
xr = [4.5, 2.25, 3.5, 4]
animateBisection(x, y, xr, xl, xu)

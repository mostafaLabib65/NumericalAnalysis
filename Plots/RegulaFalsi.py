import time
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('fivethirtyeight')

def animateLine(x1,x2,y1,y2,xr,xs,ys):
    y = np.linspace(y1, y2, 4)
    x = np.linspace(x1, x2, 4)
    for n in range(len(x) + 1):
        plt.ion()
        plt.show()
        plt.axvline(x=0, lw=2, color='k')
        plt.axhline(y=0, lw=2, color='k')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.plot(xs, ys, color='r', lw=2)
        plt.title('Regula falsi method')
        plt.plot(x[:n], y[:n], color='g',lw=1,linestyle='dashed')
        plt.pause(0.05)
    plt.axvline(x=0, lw=2, color='k', label='axes')
    plt.axhline(y=0, lw=2, color='k')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(xs, ys, label='function', color='r', lw=2)
    plt.title('Regula falsi method')
    plt.axvline(xr, lw=1, color='b', linestyle='dashed', label='vertical')
    plt.show()
    plt.pause(0.5)
    plt.cla()


def animateRegulaFalsi(xs, ys, xr, xl,Fxl, xu,Fxu):
    for i in range(len(xr)):
        plt.ion()
        plt.show()
        animateLine(xl[i],xu[i],Fxl[i],Fxu[i],xr[i],xs,ys)
    plt.ioff()
    plt.axvline(x=0, lw=2, color='k', label='axes')
    plt.axhline(y=0, lw=2, color='k')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(xs, ys, label='function', color='r', lw=2)
    plt.title('Regula falsi method')
    plt.axvline(xr[len(xr) - 1], lw=1, color='b', linestyle='dashed', label='vertical')
    plt.plot([xl[len(xr) - 1] , xu[len(xr) - 1]], [Fxl[len(xr) - 1] , Fxu[len(xr) - 1]], color='g',lw=1,linestyle='dashed')
    plt.show()


y = [12,5,0,-3,-4,-3,0,5,12]
x=[-4,-3,-2,-1,0,1,2,3,4]
xl=[0,-1.333333,-1.84615]
fxl=[-4,-2.2222222,-0.5971]
xu = [-3, -3,-3]
fxu = [5, 5,5]
xr=[-1.333333,-1.84615,-1.969]
animateRegulaFalsi(x,y,xr,xl,fxl,xu,fxu)
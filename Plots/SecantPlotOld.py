import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

def animateLine(x1,x2,y1,y2,xr,xs,ys):
    y = np.linspace(y1, y2, 10)
    x = np.linspace(x1, x2, 10)
    for n in range(len(x) + 1):
        plt.ion()
        plt.show()
        plt.axvline(x=0, lw=2, color='k')
        plt.axhline(y=0, lw=2, color='k')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.plot(xs, ys, color='r', lw=2)
        plt.title('secant method')
        plt.plot(x[:n], y[:n], color='g',lw=1,linestyle='dashed')
        plt.pause(0.05)
    plt.axvline(x=0, lw=2, color='k', label='axes')
    plt.axhline(y=0, lw=2, color='k')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(xs, ys, label='function', color='r', lw=2)
    plt.title('secant method')
    plt.axvline(xr, lw=1, color='b', linestyle='dashed', label='vertical')
    plt.show()
    plt.pause(0.75)
    plt.cla()


#for public use
def animateSecant(xs, ys, xr, xl,Fxl, xbl,Fxbl):
    for i in range(len(xr)):
        plt.ion()
        plt.show()
        plt.axvline(x=0, lw=2, color='k',label='axes')
        plt.axhline(y=0, lw=2, color='k')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('secant method')
        plt.plot(xs, ys, label='function', color='r',lw=2)
        if Fxbl[i]*Fxl[i] < 0:
            animateLine(xl[i], xbl[i], Fxl[i], Fxbl[i], xr[i], xs, ys)
        else:
            if abs(Fxl[i]) > abs(Fxbl[i]):
                animateLine(xl[i], xr[i], Fxl[i], 0,xr[i],xs,ys)
            else:
                animateLine(xbl[i], xr[i], Fxbl[i], 0, xr[i], xs, ys)
    plt.ioff()
    plt.axvline(x=0, lw=2, color='k')
    plt.axhline(y=0, lw=2, color='k')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(xs, ys, color='r', lw=2,label='function')
    plt.title('secant method')
    if Fxbl[i] * Fxl[i] < 0:
        plt.plot([xl[i], xbl[i]], [Fxl[i], Fxbl[i]],color='g', lw=1, linestyle='dashed')
    else:
        if abs(Fxl[i]) > abs(Fxbl[i]):
            plt.plot([xl[i], xr[i]],[ Fxl[i], 0],color='g', lw=1, linestyle='dashed')
        else:
            plt.plot([xbl[i], xr[i]], [Fxbl[i], 0],color='g', lw=1, linestyle='dashed')
    plt.axvline(xr[len(xr) - 1], lw=1, color='b', linestyle='dashed', label='vertical')
    plt.legend()
    plt.show()


ys= [1,.81,.43,.25,.04,0,.04,.25,.43,.81,1]
xs=[-1,-.9,-.656,-.5,-.2,0,.2,.5,.656,.9,1]
xl = [0.5,.333333333,.2,.125]
xr = [.333333333,.2,.125,.07692307692]
xbl = [1,0.5,.333333333,.2]
fxl = [.25,0.1111111111,.04,.015625]
fxbl = [1,.25,0.1111111111,.04]

animateSecant(xs,ys,xr,xl,fxl,xbl,fxbl)
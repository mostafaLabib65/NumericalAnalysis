
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('fivethirtyeight')


def animateNewtonRaphson(xs, ys, xr, x,fx):
    for i in range(len(xr)):
        plt.ion()
        plt.show()
        plt.axvline(x=0, lw=2, color='k', label='axes')
        plt.axhline(y=0, lw=2, color='k')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Newton Raphson method')
        plt.plot(xs, ys, label='function', color='r', lw=2)
        if i < len(xr) - 1:
            animateLine(fx[i],x[i],xr[i],fx[i+1],xs,ys)
        else:
            animateLine(fx[i], x[i], xr[i], 0, xs, ys)
    plt.ioff()
    plt.axvline(x=0, lw=2, color='k', label='axes')
    plt.axhline(y=0, lw=2, color='k')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Newton Raphson method')
    plt.plot(xs, ys, label='function', color='r', lw=2)
    plt.plot([x[len(xr) - 1], xr[len(xr) - 1]], [fx[len(xr) - 1], 0], color='g', lw=1, linestyle='dashed',label='tangent')
    plt.axvline(xr[len(xr) - 1], lw=1, color='b', linestyle='dashed', label='vertical')
    plt.legend()
    plt.show()

def animateLine(y1,x1,xr,yr,xs,ys):
    y = np.linspace(y1, 0, 10)
    x = np.linspace(x1, xr, 10)
    for n in range(len(x) + 1):
        plt.ion()
        plt.show()
        plt.axvline(x=0, lw=2, color='k')
        plt.axhline(y=0, lw=2, color='k')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.plot(xs, ys, color='r', lw=2)
        plt.title('Newton Raphson method')
        plt.plot(x[:n], y[:n], color='g',lw=1,linestyle='dashed')
        plt.pause(0.05)
    plt.axvline(x=0, lw=2, color='k', label='axes')
    plt.axhline(y=0, lw=2, color='k')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(xs, ys, label='function', color='r', lw=2)
    plt.title('Newton Raphson method')
    plt.plot(x, y, color='g', lw=1, linestyle='dashed',label='tangent')
    plt.axvline(xr,lw=1,color='b',linestyle='dashed',label='vertical')
    #plt.legend()
    plt.show()
    plt.pause(0.5)
    plt.cla()

ys= [1,.81,.43,.25,.04,0,.04,.25,.43,.81,1]
xs=[-1,-.9,-.656,-.5,-.2,0,.2,.5,.656,.9,1]
xr = [0.5,.25,.125,.0625,.03125,.015625]
fx = [1,.25,0.0625,.015625,.00390625,.000976562]
x = [1,0.5,.25,.125,.0625,.03125]
animateNewtonRaphson(xs, ys, xr, x, fx)

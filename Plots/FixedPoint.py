
from matplotlib import style
import numpy as np
import matplotlib.pyplot as plt

style.use('fivethirtyeight')

def animationHorizontal(x1,x2,constY,hLinesX,hLinesY,xs,ys):
    x = np.linspace(x1, x2, 4)
    y = [constY]*(len(x)+1)
    for n in range(len(x)+1):
        plt.ion()
        plt.show()
        plt.axvline(x=0, lw=4, color='k', label='axes')
        plt.axhline(y=0, lw=4, color='k')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.plot(xs, ys, label='function', color='r', lw=3)
        plt.plot(xs, xs, label='x=y', color='y', lw=3)
        plt.title('fixed point method')
        plt.plot(hLinesX, hLinesY, label='fixed point line', color='b', lw=1, linestyle='dashed')
        plt.plot(x[:n], y[:n],color='b',lw=1,linestyle='dashed')
        plt.legend()
        plt.pause(0.01)
        plt.cla()


def animationVertical(y1,y2,constX,hLinesX,hLinesY,xs,ys):
    y = np.linspace(y1, y2, 4)
    x = [constX]*(len(y)+1)
    for n in range(len(x)):
        plt.ion()
        plt.show()
        plt.axvline(x=0, lw=4, color='k', label='axes')
        plt.axhline(y=0, lw=4, color='k')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.plot(xs, ys, label='function', color='r', lw=3)
        plt.plot(xs, xs, label='x=y', color='y', lw=3)
        plt.plot(hLinesX, hLinesY, label='fixed point line', color='b', lw=1, linestyle='dashed')
        plt.title('fixed point method')
        plt.plot(x[:n], y[:n], color='b',lw=1,linestyle='dashed')
        plt.legend()
        plt.pause(0.01)
        plt.cla()


def animateSteps(hLinesX,hLinesY,xs,ys):
    animationVertical(hLinesY[0], hLinesY[1], hLinesX[0], hLinesX[:0], hLinesY[:0],xs,ys)
    for n in range(1,len(hLinesX)+1):
        if n < len(hLinesX)-1:
            if hLinesX[n] == hLinesY[n]:
                animationVertical(hLinesY[n],hLinesY[n+1],hLinesX[n],hLinesX[:n+1],hLinesY[:n+1],xs,ys)
            else:
                animationHorizontal(hLinesX[n],hLinesX[n+1],hLinesY[n],hLinesX[:n+1],hLinesY[:n+1],xs,ys)


def animateFixedPoint(xs, ys,gx, x):
    hLinesX =[x[0]]
    hLinesY=[0]
    plt.ion()
    plt.axvline(x=0, lw=4, color='k', label='axes')
    plt.axhline(y=0, lw=4, color='k')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('fixed point method')
    plt.plot(xs, ys, label='function', color='r', lw=3)
    plt.plot(xs, xs, label='x=y', color='y', lw=3)
    plt.legend()
    plt.show()
    for i in range(len(gx)):
        hLinesX.append(x[i])
        hLinesY.append(gx[i])
        hLinesX.append(gx[i])
        hLinesY.append(gx[i])
    animateSteps(hLinesX,hLinesY,xs,ys)
    plt.ioff()
    plt.axvline(x=0, lw=4, color='k', label='axes')
    plt.axhline(y=0, lw=4, color='k')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(xs, ys, label='function', color='r', lw=3)
    plt.plot(xs, xs, label='x=y', color='y', lw=3)
    plt.title('fixed point method')
    plt.plot(hLinesX, hLinesY, label='fixed point line', color='b', lw=1, linestyle='dashed')
    plt.legend()
    plt.show()


ys = [1,.81,.43,.25,.04,0,.04,.25,.43,.81,1]
xs = [-1,-.9,-.656,-.5,-.2,0,.2,.5,.656,.9,1]
gx = [0.81,.656,.43,.1853,0.03433,0]
x = [.9,0.81,.656,.43,.1853,0.03433]
animateFixedPoint(xs,ys,gx,x)
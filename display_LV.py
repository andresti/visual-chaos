from LotkaVolterra import LotkaVolterra
import matplotlib.pyplot as plt
from utils import frange

if __name__ == "__main__":
    deltat = 0.01
    lv = LotkaVolterra(2./3, 4./3, 1., 1., deltat)

    fig, axarr = plt.subplots(3)
    plt.tight_layout()
    x = []
    y = []
    t = []
    points_x = []
    points_y = []
    points_t = []

    for i in frange(0, 20, deltat):
        if i == 0:
            points_xy, = axarr[0].plot(x, y, marker='.', linestyle='None')
            axarr[0].set_xlim(0, 2)
            axarr[0].set_ylim(0, 2)
            axarr[0].set_xlabel('x')
            axarr[0].set_ylabel('y')
            points_tx, = axarr[1].plot(t, x, marker='.', linestyle='None')
            axarr[1].set_xlim(0, 20)
            axarr[1].set_ylim(0, 2)
            axarr[1].set_xlabel('t')
            axarr[1].set_ylabel('x')
            points_ty, = axarr[2].plot(t, y, marker='.', linestyle='None')
            axarr[2].set_xlim(0, 20)
            axarr[2].set_ylim(0, 2)
            axarr[2].set_xlabel('t')
            axarr[2].set_ylabel('y')
        else:
            (x,y) = lv.iterate()
            points_x.append(x)
            points_y.append(y)
            points_t.append(i)
            points_xy.set_data(points_x, points_y)
            points_tx.set_data(points_t, points_x)
            points_ty.set_data(points_t, points_y)
        #print x,y,t
        #print len(x), len(y), len(t)
        plt.pause(0.01)

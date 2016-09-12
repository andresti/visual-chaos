from Henon import Henon
import matplotlib.pyplot as plt
from utils import frange

if __name__ == "__main__":
    henon = Henon(1.4, 0.3)
    deltat = 0.1

    fig, ax = plt.subplots()

    x = []
    y = []
    points_x = []
    points_y = []
    #myx = 1.01
    for t in frange(0, 200, deltat):
        if t == 0:
            points, = ax.plot(x, y, marker='.', linestyle='None')
            ax.set_xlim(-1.5, 1.5)
            ax.set_ylim(-0.5, 0.5)
        else:
            (x,y) = henon.iterate()
            points_x.append(x)
            points_y.append(y)
            points.set_data(points_x, points_y)
        plt.pause(0.01)

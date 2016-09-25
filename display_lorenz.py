from Lorenz import Lorenz
import matplotlib.pyplot as plt
from utils import frange
from mpl_toolkits.mplot3d import Axes3D

if __name__ == "__main__":
    deltat = 0.01
    lorenz = Lorenz(10, 28, 8./3, deltat)
    lorenz.set_initial(1., 2., 3.)

    fig, axarr = plt.subplots(2,2)
    plt.tight_layout()
    x = []
    y = []
    z = []
    t = []
    points_x = []
    points_y = []
    points_z = []
    points_t = []

    for i in frange(0, 20, deltat):
        if i == 0:
            points_tx, = axarr[0][0].plot(t, x, marker='.', linestyle='None')
            axarr[0][0].set_xlim(0, 20)
            axarr[0][0].set_ylim(-50, 50)
            axarr[0][0].set_xlabel('t')
            axarr[0][0].set_ylabel('x')
            points_ty, = axarr[0][1].plot(t, y, marker='.', linestyle='None')
            axarr[0][1].set_xlim(0, 20)
            axarr[0][1].set_ylim(-50, 50)
            axarr[0][1].set_xlabel('t')
            axarr[0][1].set_ylabel('y')
            points_tz, = axarr[1][0].plot(t, z, marker='.', linestyle='None')
            axarr[1][0].set_xlim(0, 20)
            axarr[1][0].set_ylim(-50, 50)
            axarr[1][0].set_xlabel('t')
            axarr[1][0].set_ylabel('z')
            ax = fig.add_subplot(224, projection='3d')
            points_xyz, = ax.plot(x, y, z)
            ax.set_xlim(-50, 50)
            ax.set_ylim(-50, 50)
            ax.set_zlim(0, 50)
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_ylabel('z')
            axarr[1][1] = ax
            mng = plt.get_current_fig_manager()
            mng.full_screen_toggle()

        else:
            (x,y,z) = lorenz.iterate()
            points_x.append(x)
            points_y.append(y)
            points_z.append(z)
            points_t.append(i)
            points_tx.set_data(points_t, points_x)
            points_ty.set_data(points_t, points_y)
            points_tz.set_data(points_t, points_z)
            points_xyz.set_data(points_x, points_y)
            points_xyz.set_3d_properties(points_z)

        #print x,y,t
        #print len(x), len(y), len(t)
        plt.pause(0.003)

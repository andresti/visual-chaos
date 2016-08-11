import matplotlib.pyplot as plt
import math
from functools import partial

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

def make_phase_line(func, x0 = 0.5, n_points = 100, n_skip = 100):
    x = func(x = x0)
    points = []
    for i in range(1, n_skip):
        x = func(x = x)
    for i in range(n_points):
        x = func(x = x)
        points.append(x)
    return points

def logistic_map(r, x):
    return r * x * (1-x)
def cubic_map(r, x):
    return x * logistic_map(r,x)
def sine_map(r, x):
    return r * math.sin(x * math.pi / 2)

def make_bifurcation_diagram(function, par_range = (0, 4), step_size = 0.002):
    values_par = []
    values_x = []
    for par in frange(par_range[0], par_range[1], step_size):
        values_par.append(par)
        values_x.append(make_phase_line(partial(function, r = par)))
    return (values_par, values_x)

def plot_bifurcation_diagram(values_par, values_x, par_range = (0,4), x_range = (0,1)):
    my_dpi = 80
    plt.figure(figsize=(1600/my_dpi, 1200/my_dpi), dpi=my_dpi)
    for xe, ye in zip(values_par, values_x):
        plt.scatter([xe] * len(ye), ye, s = 1, c = 'b', marker = '.')
    plt.axes().set_xlim(par_range[0], par_range[1])
    plt.axes().set_ylim(x_range[0], x_range[1])
    plt.show()

if __name__ == "__main__":
    r_range = (0, 4)
    x_range = (0, 1)
    (values_par, values_x) = make_bifurcation_diagram(logistic_map, par_range = r_range)
    plot_bifurcation_diagram(values_par, values_x, par_range = r_range, x_range = x_range)

    (values_par, values_x) = make_bifurcation_diagram(cubic_map, par_range = (0,6.5))
    plot_bifurcation_diagram(values_par, values_x, par_range = (0,6.5), x_range = x_range)

    (values_par, values_x) = make_bifurcation_diagram(sine_map, par_range = (0,2))
    plot_bifurcation_diagram(values_par, values_x, par_range = (0,2), x_range = (0,2))


import numpy as np
import matplotlib.pyplot as plt

from matplotlib import style


def plot_results(inside, outside, iterations):
    style.use("ggplot")

    plt.clf()
    plt.title('Pi: %s iterations' % iterations)

    fig, ax = plt.subplots()

    ax.scatter(inside[:, 0], inside[:, 1], c = 'blue', s = 1.0, label = 'inside')
    ax.scatter(outside[:, 0], outside[:, 1], c = 'red', s = 1.0, label = 'outside')
    ax.set_aspect('equal')
    ax.legend(loc = 'upper right')
    ax.grid(True)

    plt.savefig('./images/pi/pi_%s.png' % (iterations), format = 'png')
    plt.close()

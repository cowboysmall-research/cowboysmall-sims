
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import style


def plot_results(results, iterations, initial, margin):
    style.use("ggplot")

    plt.clf()
    plt.title('Gamble: %s iterations' % iterations)

    plt.xlabel('Index')
    plt.ylabel('Value')

    plt.figure(1, facecolor = 'w')
    plt.plot(range(len(results)), results)

    plt.savefig('./images/gamble/gamble_%s_%s_%s.png' % (iterations, initial, margin), format = 'png')
    plt.close()

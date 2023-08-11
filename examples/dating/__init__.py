
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import style


def plot_results(results, pool_size, distribution = 'normal', type = 'dating', xlabel = 'Dating', ylabel = 'Proportion'):
    style.use("ggplot")

    plt.clf()
    plt.title('Dating Game (%sly distributed qualities)' % distribution)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.figure(1, facecolor = 'w')
    plt.hist(results, bins = int((np.max(results) - np.min(results)) / 2), density = True)

    plt.savefig('./images/dating/%s_%s_%s_%s.png' % (type, distribution, pool_size, len(results)), format = 'png')
    plt.close()

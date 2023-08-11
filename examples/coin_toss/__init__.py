
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import style


def plot_results(results, heads, bias):
    style.use("ggplot")

    plt.clf()
    plt.title('Coint Toss: %s heads in a row - Histogram' % heads)

    plt.xlabel('Tosses')
    plt.ylabel('Proportion')

    plt.figure(1, facecolor = 'w')
    plt.hist(results, bins = int((np.max(results) - np.min(results)) / 2), density = True)

    plt.savefig('./images/coin_toss/coin_toss_%s_%s_%s.png' % (heads, bias, len(results)), format = 'png')
    plt.close()

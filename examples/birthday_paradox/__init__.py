
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import style


def plot_results(numbers):
    style.use("ggplot")

    plt.clf()
    plt.title('Birthday Paradox - Histogram')

    plt.xlabel('Number')
    plt.ylabel('Proportion')

    plt.figure(1, facecolor = 'w')
    plt.hist(numbers, bins = int((np.max(numbers) - np.min(numbers)) / 2), density = True)

    plt.savefig('./images/birthday_paradox/birthday_paradox_%s.png' % len(numbers), format = 'png')
    plt.close()

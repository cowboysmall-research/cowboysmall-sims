
import matplotlib.pyplot as plt

from matplotlib import style


def plot_results(samples, size, iterations, statistic):
    style.use("ggplot")

    plt.clf()
    plt.title('Bootstrapped Samples (%s)' % (statistic))

    plt.xlabel('Samples')
    plt.ylabel('Proportion')

    plt.figure(1, facecolor = 'w')
    plt.hist(samples, bins = 25, density = True)

    plt.savefig('./images/bootstrap/bootstrap_%s_%s_%s.png' % ('_'.join(statistic.split()), size, iterations), format = 'png')
    plt.close()

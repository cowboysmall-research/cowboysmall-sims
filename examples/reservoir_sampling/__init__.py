
import matplotlib.pyplot as plt

from matplotlib import style


def plot_results(results, size, k):
    style.use("ggplot")

    plt.clf()
    plt.title('Reservoir Samples (k = %s)' % (k))

    plt.xlabel('Sample Mean')
    plt.ylabel('Proportion')

    plt.figure(1, facecolor = 'w')
    plt.hist(results[:, 0], bins = 25, density = True)

    plt.savefig('./images/reservoir_sampling/reservoir_sampling_%s_%s.png' % (size, k), format = 'png')
    plt.close()

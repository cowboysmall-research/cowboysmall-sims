
import matplotlib.pyplot as plt

from matplotlib import style


def plot_results(results, iterations):
    style.use("ggplot")

    plt.clf()
    plt.title('Random Walk: %s iterations' % iterations)

    plt.xlabel('Index')
    plt.ylabel('Value')

    plt.figure(1, facecolor = 'w')
    plt.plot(range(iterations), results)

    plt.savefig('./images/random_walk/random_walk_%s.png' % (iterations), format = 'png')
    plt.close()

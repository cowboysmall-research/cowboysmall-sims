import sys
import random

import numpy             as np
import matplotlib.pyplot as plt

from cowboysmall.sims.simulation import Simulation


class Bootstrap(Simulation):

    def step(self, i: int, data: dict) -> None:
        sample = np.random.choice(data['population'], data['size'])

        data['samples'][i, 0] = np.mean(sample)
        data['samples'][i, 1] = np.median(sample)
        data['samples'][i, 2] = np.std(sample)
        data['samples'][i, 3] = np.var(sample)


def plot_results(samples, size, iterations, statistic):
    plt.clf()
    plt.title('Bootstrapped Samples (%s)' % (statistic))

    plt.xlabel('Samples')
    plt.ylabel('Proportion')

    plt.figure(1, facecolor = 'w')
    plt.hist(samples, bins = 25, density = True)

    plt.savefig('./images/bootstrap/bootstrap_%s_%s_%s.png' % ('_'.join(statistic.split()), size, iterations), format = 'png')
    plt.close()


def main(argv):
    np.random.seed(1337)

    mean       = int(argv[0])
    std        = int(argv[1])
    size       = int(argv[2])
    iterations = int(argv[3])

    population = np.random.normal(mean, std, size)
    samples    = np.empty((iterations, 4))

    sim  = Bootstrap({'population': population, 'samples': samples, 'size': size})
    data = sim.run(iterations)

    print()
    print('               Mean:')
    print('              Value: %0.5f' % (np.mean(population)))
    print('               S.E.: \u00B1 %0.5f' % (np.std(data['samples'][:, 0])))
    print('               Bias: %0.5f' % (np.mean(data['samples'][:, 0]) - np.mean(population)))
    print('               C.I.: (%0.5f, %0.5f)' % (np.percentile(data['samples'][:, 0], 2.5), np.percentile(data['samples'][:, 0], 97.5)))
    print()
    print('             Median:')
    print('              Value: %0.5f' % (np.median(population)))
    print('               S.E.: \u00B1 %0.5f' % (np.std(data['samples'][:, 1])))
    print('               Bias: %0.5f' % (np.mean(data['samples'][:, 1]) - np.median(population)))
    print('               C.I.: (%0.5f, %0.5f)' % (np.percentile(data['samples'][:, 1], 2.5), np.percentile(data['samples'][:, 1], 97.5)))
    print()
    print(' Standard Deviation:')
    print('              Value: %0.5f' % (np.std(population)))
    print('               S.E.: \u00B1 %0.5f' % (np.std(data['samples'][:, 2])))
    print('               Bias: %0.5f' % (np.mean(data['samples'][:, 2]) - np.std(population)))
    print('               C.I.: (%0.5f, %0.5f)' % (np.percentile(data['samples'][:, 2], 2.5), np.percentile(data['samples'][:, 2], 97.5)))
    print()
    print('           Variance:')
    print('              Value: %0.5f' % (np.var(population)))
    print('               S.E.: \u00B1 %0.5f' % (np.std(data['samples'][:, 3])))
    print('               Bias: %0.5f' % (np.mean(data['samples'][:, 3]) - np.var(population)))
    print('               C.I.: (%0.5f, %0.5f)' % (np.percentile(data['samples'][:, 3], 2.5), np.percentile(data['samples'][:, 3], 97.5)))
    print()

    plot_results(data['samples'][:, 0], size, iterations, 'mean')
    plot_results(data['samples'][:, 1], size, iterations, 'median')
    plot_results(data['samples'][:, 2], size, iterations, 'standard deviation')
    plot_results(data['samples'][:, 3], size, iterations, 'variance')


if __name__ == "__main__":
    main(sys.argv[1:])

import sys
import random
import math

import numpy             as np
import matplotlib.pyplot as plt

from matplotlib import style

from cowboysmall.sims.simulation import Simulation


class ReservoirSampling(Simulation):

    def step(self, i: int, data: dict) -> None:
        k = data['k']
        if i < k:
            data['sample'].append(data['population'][i])
        else:
            p = np.random.randint(0, i)
            if p < k:
                data['sample'][p] = data['population'][i]
            data['samples'][i - k, 0] = np.mean(data['sample'])
            data['samples'][i - k, 1] = np.std(data['sample'])


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


def main(argv):
    np.random.seed(1337)

    size = int(argv[0])
    k    = int(argv[1])

    population = np.random.randint(1, size, size)
    samples    = np.empty((size - k, 2))

    sim  = ReservoirSampling({'samples': samples, 'sample': [], 'population': population, 'size': size, 'k': k})
    data = sim.run(size)

    print()
    print('            Reservoir Sampling:')
    print()
    print('       Population Distribution:')
    print()
    print('                          mean: %10.5g' % np.mean(population))
    print('            standard deviation: %10.5g' % np.std(population))
    print()
    print()
    print('         Sampling Distribution:')
    print()
    print('              theoretical mean: %10.5g' % np.mean(population))
    print('theoretical standard deviation: %10.5g' % (np.std(population) / math.sqrt(k)))
    print()
    print()
    print('         Observed Distribution:')
    print()
    print('                          mean: %10.5g' % np.mean(samples[:, 0]))
    print('                          bias: %10.5g' % (np.mean(samples[:, 0]) - np.mean(population)))
    print()
    print('            standard deviation: %10.5g' % np.std(samples[:, 0]))
    print('                          bias: %10.5g' % (np.mean(samples[:, 1]) - np.std(population)))
    print()

    plot_results(samples, size, k)


if __name__ == "__main__":
    main(sys.argv[1:])

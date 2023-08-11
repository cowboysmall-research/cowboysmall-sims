import sys
import random

import numpy             as np
import matplotlib.pyplot as plt

from cowboysmall.sims.simulation import Simulation


class Bootstrap(Simulation):

    def step(self, i: int, data: dict) -> None:
        sample = np.random.choice(data['population'], data['size'])
        data['samples'][i, 0] = np.median(sample)


def main(argv):
    mean       = int(argv[0])
    std        = int(argv[1])
    size       = int(argv[2])
    iterations = int(argv[3])

    np.random.seed(1337)

    population = np.random.normal(mean, std, size)
    samples    = np.empty((iterations, 1))

    sim  = Bootstrap({'population': population, 'samples': samples, 'size': size})
    data = sim.run(iterations)

    print()
    print(' Median:')
    print('  Value: %0.5f' % (np.median(population)))
    print('   S.E.: \u00B1 %0.5f' % (np.std(data['samples'][:, 0])))
    print('   Bias: %0.5f' % (np.mean(data['samples'][:, 0]) - np.median(population)))
    print('   C.I.: (%0.5f, %0.5f)' % (np.percentile(data['samples'][:, 0], 2.5), np.percentile(data['samples'][:, 0], 97.5)))
    print()


if __name__ == "__main__":
    main(sys.argv[1:])

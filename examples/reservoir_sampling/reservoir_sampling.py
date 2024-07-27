import sys
import math

import numpy as np

from cowboysmall.sims.simulation import Simulation
from examples.reservoir_sampling import plot_results


class ReservoirSampling(Simulation):

    def step(self, iteration: int, data: dict) -> None:
        k = data['k']
        if iteration < k:
            data['sample'].append(data['population'][iteration])
        else:
            p = np.random.randint(0, iteration)
            if p < k:
                data['sample'][p] = data['population'][iteration]
            data['samples'][iteration - k, 0] = np.mean(data['sample'])
            data['samples'][iteration - k, 1] = np.std(data['sample'])


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
    print('                          mean: %10.5g' % np.mean(data['samples'][:, 0]))
    print('                          bias: %10.5g' % (np.mean(data['samples'][:, 0]) - np.mean(population)))
    print()
    print('            standard deviation: %10.5g' % np.std(data['samples'][:, 0]))
    print('                          bias: %10.5g' % (np.mean(data['samples'][:, 1]) - np.std(population)))
    print()

    plot_results(data['samples'], size, k)


if __name__ == "__main__":
    main(sys.argv[1:])

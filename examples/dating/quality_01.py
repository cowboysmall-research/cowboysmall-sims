import sys
import random

import numpy as np

from cowboysmall.sims.simulation import Simulation
from examples.dating import plot_results


class Quality(Simulation):

    def step(self, i: int, data: dict) -> None:
        men   = np.random.randint(0, 100, data['pool_size']).tolist()
        women = np.random.randint(0, 100, data['pool_size']).tolist()

        while len(men) > 0 and max(men) > min(women):
            np.random.shuffle(men)
            np.random.shuffle(women)
            for man, woman in zip(men, women):
                if man > woman:
                    men.remove(man)
                    women.remove(woman)

        data['results'].append(max(men))


def main(argv):
    np.random.seed(1337)

    pool_size  = int(argv[0])
    iterations = int(argv[1])

    sim  = Quality({'pool_size': pool_size, 'results': []})
    data = sim.run(iterations)

    print()
    print('Dating Game (uniformly distributed qualities)')
    print()
    print('           Minimum: %s' % (np.amin(data['results'])))
    print('   25th Percentile: %s' % (np.percentile(data['results'], 25)))
    print('            Median: %s' % (np.median(data['results'])))
    print('   75th Percentile: %s' % (np.percentile(data['results'], 75)))
    print('           Maximum: %s' % (np.amax(data['results'])))
    print()
    print('              Mean: %s' % (np.mean(data['results'])))
    print('Standard Deviation: %s' % (np.std(data['results'])))
    print('          Variance: %s' % (np.var(data['results'])))
    print()

    plot_results(data['results'], pool_size, 'uniform', type = 'quality', xlabel = 'Quality')


if __name__ == "__main__":
    main(sys.argv[1:])

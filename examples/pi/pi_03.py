import sys
import random

import numpy as np

from cowboysmall.sims.simulation import Simulation
from examples.pi import plot_results


class Pi(Simulation):

    def step(self, iteration: int, data: dict) -> None:
        x, y = random.random(), random.random()
        if (x ** 2) + (y ** 2) <= 1:
            data['inside'].append((x, y))
        else:
            data['outside'].append((x, y))


def main(argv):
    random.seed(1337)

    iterations = int(argv[0])

    sim  = Pi({'inside': [], 'outside': []})
    data = sim.run(iterations)

    print()
    print('Pi - %s iterations' % (iterations))
    print()
    print(' Total: %8d' % (len(data['inside'])))
    print('    Pi: %8f' % (len(data['inside']) * 4 / float(iterations)))
    print()

    plot_results(np.array(data['inside']), np.array(data['outside']), iterations)


if __name__ == "__main__":
    main(sys.argv[1:])

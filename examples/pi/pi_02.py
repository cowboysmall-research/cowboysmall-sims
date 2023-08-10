import sys
import random

import numpy             as np
import matplotlib.pyplot as plt

from cowboysmall.sims.simulation import Simulation


class Pi(Simulation):

    def step(self, iteration: int, data: dict) -> None:
        x, y = random.random(), random.random()
        if (x ** 2) + (y ** 2) <= 1:
            data['inside'].append((x, y))
        else:
            data['outside'].append((x, y))


def plot_results(inside, outside, iterations):
    plt.clf()
    plt.title('Pi: %s iterations' % iterations)

    fig, ax = plt.subplots()

    ax.scatter(inside[:, 0], inside[:, 1], c = 'blue', s = 1.0, label = 'inside')
    ax.scatter(outside[:, 0], outside[:, 1], c = 'red', s = 1.0, label = 'outside')
    ax.set_aspect('equal')
    ax.legend(loc = 'upper right')
    ax.grid(True)

    plt.savefig('./images/pi/pi_%s.png' % (iterations), format = 'png')
    plt.close()


def main(argv):
    random.seed(1337)

    iterations = int(argv[0])

    sim  = Pi({'inside': [], 'outside': []})
    data = sim.run(iterations)

    plot_results(np.array(data['inside']), np.array(data['outside']), iterations)

    print()
    print('Pi - %s iterations' % (iterations))
    print()
    print(' Total: %8d' % (len(data['inside'])))
    print('    Pi: %8f' % (len(data['inside']) * 4 / float(iterations)))
    print()


if __name__ == "__main__":
    main(sys.argv[1:])

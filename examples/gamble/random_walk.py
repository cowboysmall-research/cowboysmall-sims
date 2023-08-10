import sys
import random

import numpy             as np
import matplotlib.pyplot as plt

from cowboysmall.sims.simulation import Simulation


class RandomWalk(Simulation):

    def step(self, i: int, data: dict) -> None:
        if random.random() < 0.5:
            data['value'] += 1
        else:
            data['value'] -= 1

        data['results'].append(data['value'])


def plot_results(results, iterations):
    plt.clf()
    plt.title('Random Walk: %s iterations' % iterations)

    plt.xlabel('Index')
    plt.ylabel('Value')

    plt.figure(1, facecolor = 'w')
    plt.plot(range(iterations), results)

    plt.savefig('./images/gamble/random_walk_%s.png' % (iterations), format = 'png')
    plt.close()


def main(argv):
    iterations = int(argv[0])
    initial    = int(argv[1])

    random.seed(1337)

    sim  = RandomWalk({'value': initial, 'results': []})
    data = sim.run(iterations)

    plot_results(data['results'], iterations)


if __name__ == "__main__":
    main(sys.argv[1:])

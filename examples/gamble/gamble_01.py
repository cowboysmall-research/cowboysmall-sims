import sys
import random

import numpy             as np
import matplotlib.pyplot as plt

from cowboysmall.sims.simulation import Simulation, SimulationException


class Gamble(Simulation):

    def step(self, i: int, data: dict) -> None:
        if 0 < data['results'][i, 2] < data['target']:
            if data['results'][i, 0] < 0.5:
                data['results'][i + 1, 2] = data['results'][i, 2] + data['results'][i, 1]
            else:
                data['results'][i + 1, 2] = data['results'][i, 2] - data['results'][i, 1]
                data['results'][i + 1, 1] = data['results'][i, 1] * 2
        else:
            raise SimulationException('Termination of simulation steps')


def plot_results(results, iterations, initial, margin):
    plt.clf()
    plt.title('Gamble: %s iterations' % iterations)

    plt.xlabel('Index')
    plt.ylabel('Value')

    plt.figure(1, facecolor = 'w')
    plt.plot(range(len(results)), results)

    plt.savefig('./images/gamble/gamble_%s_%s_%s.png' % (iterations, initial, margin), format = 'png')
    plt.close()


def main(argv):
    np.random.seed(1337)

    iterations = int(argv[0])
    initial    = int(argv[1])
    margin     = int(argv[2])

    results       = np.zeros((iterations + 1, 3))
    results[:, 0] = np.random.sample(iterations + 1)
    results[:, 1] = 1
    results[0, 2] = initial

    sim  = Gamble({'target': initial + margin, 'results': results})
    data = sim.run(iterations)

    plot_results(results[results[:, 2] > 0, 2], iterations, initial, margin)


if __name__ == "__main__":
    main(sys.argv[1:])

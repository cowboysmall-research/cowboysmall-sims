import sys
import random

from cowboysmall.sims.simulation import Simulation
from examples.random_walk import plot_results


class RandomWalk(Simulation):

    def step(self, i: int, data: dict) -> None:
        if random.random() < 0.5:
            data['value'] += 1
        else:
            data['value'] -= 1

        data['results'].append(data['value'])


def main(argv):
    random.seed(1337)

    iterations = int(argv[0])
    initial    = int(argv[1])

    sim  = RandomWalk({'value': initial, 'results': []})
    data = sim.run(iterations)

    plot_results(data['results'], iterations)


if __name__ == "__main__":
    main(sys.argv[1:])

import sys
import random

from cowboysmall.sims.simulation import Simulation


class Pi(Simulation):

    def step(self, iteration: int, data: dict) -> None:
        x, y = random.random(), random.random()
        if (x ** 2) + (y ** 2) <= 1:
            data['total'] += 1


def main(argv):
    random.seed(1337)

    iterations = int(argv[0])

    sim  = Pi({'total': 0})
    data = sim.run(iterations)

    print()
    print('Pi - %s iterations' % (iterations))
    print()
    print(' Total: %8d' % (data['total']))
    print('    Pi: %8f' % (data['total'] * 4 / float(iterations)))
    print()


if __name__ == "__main__":
    main(sys.argv[1:])

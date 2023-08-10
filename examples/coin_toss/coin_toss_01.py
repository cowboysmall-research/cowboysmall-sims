import sys
import random

from cowboysmall.sims.simulation import Simulation


class CoinToss(Simulation):

    def step(self, iterations: int, data: dict) -> None:
        index = 0
        count = 0

        while index < data['tosses']:
            if random.uniform(0.0, 1.0) < data['bias']:
                count += 1
            else:
                count  = 0

            if count == data['heads']:
                break

            index += 1

        data['count'] += count == data['heads']


def main(argv):
    iterations = int(argv[0])
    heads      = int(argv[1])
    tosses     = int(argv[2])
    bias       = float(argv[3]) if len(argv) == 4 else 0.5

    sim  = CoinToss({'heads': heads, 'tosses': tosses, 'bias': bias, 'count': 0})
    data = sim.run(iterations)

    print()
    print('Coin Toss')
    print()
    print('  iterations: %8d' % (iterations))
    print('       heads: %8d' % (heads))
    print()

    print()
    if tosses < 10:
        print('    P(X <= %d): %8.5f' % (tosses, data['count'] / float(iterations)))
    else:
        print('   P(X <= %2d): %8.5f' % (tosses, data['count'] / float(iterations)))
    print()


if __name__ == "__main__":
    main(sys.argv[1:])

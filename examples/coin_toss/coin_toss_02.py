import sys
import random

from cowboysmall.sims.simulation import Simulation


class CoinToss(Simulation):

    def step(self, iteration: int, data: dict) -> None:
        total = 0
        count = 0

        while count < data['heads']:
            total += 1

            if random.uniform(0.0, 1.0) < data['bias']:
                count += 1
            else:
                count  = 0

        data['count'] += total


def main(argv):
    iterations = int(argv[0])
    heads      = int(argv[1])
    bias       = float(argv[2]) if len(argv) == 3 else 0.5

    sim  = CoinToss({'heads': heads, 'bias': bias, 'count': 0})
    data = sim.run(iterations)

    print()
    print('Coin Toss')
    print()
    print('      iterations: %8d' % (iterations))
    print('           heads: %8d' % (heads))
    print()
    print('Expected number of tosses to get %d heads in a row: %8.5f' % (heads, data['count'] / float(iterations)))
    print()


if __name__ == "__main__":
    main(sys.argv[1:])

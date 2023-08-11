import sys
import random

import numpy as np

from cowboysmall.sims.simulation import Simulation


class Gamble(Simulation):

    def step(self, i: int, data: dict) -> None:
        amount = data['amount']
        margin = data['margin']
        target = amount + margin
        stake  = 1

        while 0 < amount < target:
            if random.random() < 0.5:
                amount += stake
            else:
                amount -= stake
                stake  *= 2

        data['count'] += amount > 0


def main(argv):
    random.seed(1337)

    iterations = int(argv[0])
    amount     = int(argv[1])
    margin     = int(argv[2])

    sim  = Gamble({'amount': amount, 'margin': margin, 'count': 0})
    data = sim.run(iterations)

    proportion = data['count'] / float(iterations)
    winnings   = data['count'] * margin
    losses     = (iterations - data['count']) * amount

    print()
    print('Gambling Simulation - %s iterations' % (iterations))
    print()
    print(' Probability')
    print('       Successes: %15s'   % (data['count']))
    print('      Proportion: %15.3f' % (proportion))
    print(' Expected Profit: %15.3f' % ((proportion * margin) - ((1 - proportion) * amount)))
    print()
    print(' Balance Sheet')
    print('  Total Winnings: %15.3f' % (winnings))
    print('    Total Losses: %15.3f' % (losses))
    print('   Actual Profit: %15.3f' % (winnings - losses))
    print()
    print()


if __name__ == "__main__":
    main(sys.argv[1:])

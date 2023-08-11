import sys
import random

import numpy as np
import statistics as st

from cowboysmall.sims.simulation import Simulation
from examples.birthday_paradox import plot_results


class BirthdayParadox(Simulation):

    def step(self, iteration: int, data: dict) -> None:
        birthdays = set()
        counter   = 0

        while len(birthdays) == counter:
            birthdays.add(random.randint(0, 365))
            counter += 1

        data['numbers'].append(counter)


def main(argv):
    iterations = int(argv[0])
    people     = int(argv[1])

    sim  = BirthdayParadox({'numbers': []})
    data = sim.run(iterations)

    print()
    print('Birthday Paradox')
    print()
    print(' iterations: %8d' % (iterations))
    print()
    print('        Min: %8d'   % (np.min(data['numbers'])))
    print('       25th: %8d'   % (np.percentile(data['numbers'], 25)))
    print('     Median: %8d'   % (np.median(data['numbers'])))
    print('       75th: %8d'   % (np.percentile(data['numbers'], 75)))
    print('        Max: %8d'   % (np.max(data['numbers'])))
    print()
    print('       Mean: %8.5f' % (np.mean(data['numbers'])))
    print('        Std: %8.5f' % (np.std(data['numbers'])))
    print('       Mode: %8d'   % (st.mode(data['numbers'])))
    print()

    prob = np.sum(np.bincount(np.array(data['numbers']))[0:people + 1]) / len(data['numbers'])
    print()
    print(' P(X <= %4d): %8.5f' % (people, prob))
    print()

    plot_results(data['numbers'])


if __name__ == "__main__":
    main(sys.argv[1:])


import sys
import random

import numpy as np
import statistics as st

from cowboysmall.sims.simulation import Simulation
from examples.coin_toss import plot_results


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

        data['results'].append(total)


def main(argv):
    iterations = int(argv[0])
    heads      = int(argv[1])
    tosses     = int(argv[2])
    bias       = float(argv[3]) if len(argv) == 4 else 0.5

    sim  = CoinToss({'heads': heads, 'bias': bias, 'results': []})
    data = sim.run(iterations)

    print()
    print('Coin Toss')
    print()
    print('  iterations: %8d'   % (len(data['results'])))
    print()
    print('         Min: %8d'   % (np.min(data['results'])))
    print('        25th: %8d'   % (np.percentile(data['results'], 25)))
    print('      Median: %8d'   % (np.median(data['results'])))
    print('        75th: %8d'   % (np.percentile(data['results'], 75)))
    print('         Max: %8d'   % (np.max(data['results'])))
    print()
    print('        Mean: %8.5f' % (np.mean(data['results'])))
    print('         Std: %8.5f' % (np.std(data['results'])))
    print('        Mode: %8d'   % (st.mode(data['results'])))
    print()

    prob = np.sum(np.bincount(np.array(data['results']))[:tosses]) / len(data['results'])
    print()
    print(' P(X <= %4d): %8.5f' % (tosses, prob))
    print()

    plot_results(data['results'], heads, bias)


if __name__ == "__main__":
    main(sys.argv[1:])

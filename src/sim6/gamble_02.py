import sys
import random

import numpy             as np
import matplotlib.pyplot as plt



def simulation(amount, margin):
    target = amount + margin
    stake  = 1

    while 0 < amount < target:
        if random.random() < 0.5:
            amount += stake
        else:
            amount -= stake
            stake  *= 2

    return amount > 0



def print_results(iterations, count, margin, amount):
    winnings   = count * margin
    losses     = (iterations - count) * amount
    proportion = count / float(iterations)

    print()
    print('Gambling Simulation - %s iterations' % (iterations))
    print()
    print(' Probability')
    print('       Successes: %15s'   % (count))
    print('      Proportion: %15.3f' % (proportion))
    print(' Expected Profit: %15.3f' % ((proportion * margin) - ((1 - proportion) * amount)))
    print()
    print(' Balance Sheet')
    print('  Total Winnings: %15.3f' % (winnings))
    print('    Total Losses: %15.3f' % (losses))
    print('   Actual Profit: %15.3f' % (winnings - losses))
    print()
    print()



def main(argv):
    iterations = int(argv[0])
    amount     = int(argv[1])
    margin     = int(argv[2])

    count      = 0

    for _ in range(iterations):
        if simulation(amount, margin):
            count += 1


    print_results(iterations, count, margin, amount)



if __name__ == "__main__":
    main(sys.argv[1:])

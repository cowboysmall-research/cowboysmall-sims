import sys
import random

import numpy as np



def switch_strategy_simulation(count):
    prisoners = [0] * count
    leader    = np.random.choice(count)

    switch    = 0
    days      = 0

    while prisoners[leader] < count - 1:
        days += 1
        p     = np.random.choice(count)

        if p == leader:
            if switch == 1:
                switch        = 0
                prisoners[p] += 1
        else:
            if prisoners[p] == 0 and switch == 0:
                switch        = 1
                prisoners[p] += 1

    return days


def print_results(days):
    print()
    print('Switch Strategy:')
    print()
    print('All visited after %s years and %s days' % (days // 365, days % 365))
    print()


def main(argv):
    count = int(argv[0])

    np.random.seed(1337)

    print_results(switch_strategy_simulation(count))



if __name__ == "__main__":
    main(sys.argv[1:])

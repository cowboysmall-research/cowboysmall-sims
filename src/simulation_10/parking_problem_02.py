import sys
import random

import numpy as np


SCALE = 100000


def spots_available(spots, length):
    if spots[0] >= SCALE:
        return True

    for i in range(len(spots) - 1):
        if spots[i + 1] - spots[i] >= 2 * SCALE:
            return True

    return length - spots[-1] >= 2 * SCALE



def spot_found(spot, spots, length):
    if 0 <= spot <= spots[0] - SCALE:
        return True

    for i in range(len(spots) - 1):
        if spots[i] + SCALE <= spot <= spots[i + 1] - SCALE:
            return True

    return spots[-1] + SCALE <= spot <= length - SCALE



def get_parking(length):
    return np.random.randint(length - SCALE)



def parking_problem(length):
    scaled = length * SCALE
    spots  = [get_parking(scaled)]

    while spots_available(spots, scaled):
        spot = get_parking(scaled)

        if spot_found(spot, spots, scaled):
            spots.append(spot)
            spots.sort()

    return len(spots) / float(length)



def simulation(iterations, length):
    results = []

    print()
    print('    Parking Problem: running {} simulations...'.format(iterations))
    print()

    for i in range(iterations):
        results.append(parking_problem(length))
        print('                   : iteration {:5d}'.format(i + 1), end = '\r')

    print()
    print()
    print('                   : simulations completed...')
    print()

    return results



def print_results(results):
    print()
    print()
    print('    Parking Problem: results')
    print()
    print('       Distribution:')
    print()
    print('               mean: %0.4g' % np.mean(results))
    print(' standard deviation: %0.4g' % np.std(results))
    print()



def main(argv):
    iterations = int(argv[0])
    length     = int(argv[1])

    print_results(simulation(iterations, length))



if __name__ == "__main__":
    main(sys.argv[1:])

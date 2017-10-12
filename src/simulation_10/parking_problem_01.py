import sys
import random

import numpy as np


SCALE = 100000


def spots_available(spots, length):
    if spots[0, 0] >= SCALE:
        return True

    for i in range(spots.shape[0] - 1):
        if spots[i + 1, 0] - spots[i, 1] >= SCALE:
            return True

    return length - spots[-1, 1] >= SCALE



def spot_found(spot, spots, length):
    if 0 <= spot[0, 0] and spot[0, 1] <= spots[0, 0]:
        return True

    for i in range(spots.shape[0] - 1):
        if spots[i, 1] <= spot[0, 0] and spot[0, 1] <= spots[i + 1, 0]:
            return True

    return spots[-1, 1] <= spot[0, 0] and spot[0, 1] <= length



def get_parking(length):
    spot = np.random.randint(length - SCALE)
    return np.array([[spot, spot + SCALE]])



def parking_problem(length):
    scaled = length * SCALE
    spots  = get_parking(scaled)

    while spots_available(spots, scaled):
        spot = get_parking(scaled)

        if spot_found(spot, spots, scaled):
            spots = np.concatenate((spots, spot))
            spots = spots[spots[:, 0].argsort()]

    return spots.shape[0] / float(length)



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

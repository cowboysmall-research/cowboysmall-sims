import sys

import numpy as np



def spots_available(spots, length):
    if spots[0, 0] >= 1.0:
        return True

    for i in range(spots.shape[0] - 1):
        if spots[i + 1, 0] - spots[i, 1] >= 1.0:
            return True

    return length - spots[-1, 1] >= 1.0



def spot_found(spot, spots, length):
    if 0 <= spot[0, 0] and spot[0, 1] <= spots[0, 0]:
        return True

    for i in range(spots.shape[0] - 1):
        if spots[i, 1] <= spot[0, 0] and spot[0, 1] <= spots[i + 1, 0]:
            return True

    return spots[-1, 1] <= spot[0, 0] and spot[0, 1] <= length



def get_parking(length):
    spot = np.random.uniform(0, length - 1.0)
    return np.array([[spot, spot + 1.0]])



def parking_problem(length):
    spots  = get_parking(length)

    while spots_available(spots, length):
        spot = get_parking(length)

        if spot_found(spot, spots, length):
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
    print('               mean: %0.10g' % np.mean(results))
    print(' standard deviation: %0.10g' % np.std(results))
    print()



def main(argv):
    iterations = int(argv[0])
    length     = int(argv[1])

    print_results(simulation(iterations, length))



if __name__ == "__main__":
    main(sys.argv[1:])

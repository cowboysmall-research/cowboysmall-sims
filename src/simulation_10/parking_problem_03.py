import sys

import numpy as np
import matplotlib.pyplot as plt


def parking_problem(length):
    spots = []

    def find_spots(start, end):
        spot = np.random.uniform(start, end - 1.0)
        spots.append(spot)

        if spot - start >= 1.0:
            find_spots(start, spot)

        if end - spot >= 2.0:
            find_spots(spot + 1.0, end)

    find_spots(0, length)

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
    print('               mean: %0.10g' % np.mean(results))
    print(' standard deviation: %0.10g' % np.std(results))
    print()



def plot_results(results):
    plt.clf()
    plt.hist(results)
    plt.title('Parking Problem')
    plt.xlabel('Results')
    plt.savefig('./src/simulation_10/images/parking_problem_%s.png' % len(results), format = 'png')
    plt.close()



def main(argv):
    iterations = int(argv[0])
    length     = int(argv[1])

    results    = simulation(iterations, length)

    print_results(results)
    plot_results(results)




if __name__ == "__main__":
    main(sys.argv[1:])

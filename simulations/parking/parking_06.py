import sys

import argparse

import numpy as np
import matplotlib.pyplot as plt


def parking_problem(length, overlap):
    spots = []

    def find_spots(start, end):
        spot = np.random.uniform(start, end)
        spots.append(spot)

        if start <= spot - (1.0 - (overlap / 2)):
            find_spots(start, spot - (1.0 - (overlap / 2)))

        if spot + (1.0 - (overlap / 2)) <= end:
            find_spots(spot + (1.0 - (overlap / 2)), end)

    find_spots(0, length)

    return (length - total_gaps(sorted(spots))) / float(length)



def total_gaps(spots):
    total = 0

    for i in range(len(spots) - 1):
        value = spots[i + 1] - (spots[i] + 1)
        if value > 0:
            total += value 

    value = spots[-1] - (spots[-2] + 1)
    if value > 0:
        total += value 

    return total



def simulation(iterations, length, overlap):
    results = []

    print()
    print('    Parking Problem: running {} simulations...'.format(iterations))
    print()

    for i in range(iterations):
        results.append(parking_problem(length, overlap))
        print('                   : iteration {:5d}'.format(i + 1), end = '\r')

    print()
    print()
    print('                   : simulations completed...')
    print()

    return results



def print_results(results):
    print()
    print()
    print('    Parking Problem - Overlap Version: results')
    print()
    print('                         Distribution:')
    print()
    print('                                 mean: {:10.8f}'.format(np.mean(results)))
    print('                   standard deviation: {:10.8f}'.format(np.std(results)))
    print()



def plot_results(results):
    plt.clf()
    plt.hist(results)
    plt.title('Parking Problem')
    plt.xlabel('Results')
    plt.savefig('./images/parking/parking_{}.png'.format(len(results)), format = 'png')
    plt.close()



def main(args):
    iterations = int(args.iterations)
    length     = int(args.length)
    overlap    = float(args.overlap)

    results    = simulation(iterations, length, overlap)

    print_results(results)
    plot_results(results)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "A script that estimates the jamming limit for Renyi's Parking Problem - Overlap Version")
    parser.add_argument("-n", "--iterations",  dest = "iterations",  help = "the number of iterations to perform", required = True)
    parser.add_argument("-l", "--length", dest = "length", help = "the length of the interval", required = True)
    parser.add_argument("-o", "--overlap", dest = "overlap", help = "the overlap length", required = True)
    main(parser.parse_args())

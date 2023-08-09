import sys

import argparse

import numpy as np
import matplotlib.pyplot as plt



def parking_problem(length):
    spots = []

    def find_spots(start, end):
        spot = np.random.uniform(start, end)
        spots.append(spot)

        if start <= spot - 1.0:
            find_spots(start, spot - 1.0)

        if spot + 1.0 <= end:
            find_spots(spot + 1.0, end)

    find_spots(0, length)

    return len(spots) / float(length)



def simulation(iterations, length):
    results = []

    print()
    print('    Parking Problem: running {} simulations'.format(iterations))
    print()
    print('                  L: {:8d}'.format(length))
    print()

    for i in range(iterations):
        results.append(parking_problem(length))
        print('          iteration: {:8d}'.format(i + 1), end = '\r')

    print('         iterations: {:8d}'.format(iterations))
    print()

    return results



def print_results(results):
    print()
    print('    Parking Problem: results')
    print()
    print('       distribution:')
    print('               mean: {:0.6f}'.format(np.mean(results)))
    print(' standard deviation: {:0.6f}'.format(np.std(results)))
    print()



def plot_results(results):
    plt.clf()
    plt.title('Parking Problem')

    plt.xlabel('Results')

    plt.hist(results, bins = 25, density = True)

    plt.savefig('./images/parking/parking_{}.png'.format(len(results)), format = 'png')
    plt.savefig('./images/parking/parking_{}.eps'.format(len(results)), format = 'eps')
    plt.close()



def main(args):
    iterations = int(args.iterations)
    length     = int(args.length)

    results    = simulation(iterations, length)

    print_results(results)
    plot_results(results)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "A script that estimates the jamming limit for Renyi's Parking Problem")
    parser.add_argument("-n", "--iterations",  dest = "iterations",  help = "the number of iterations to perform", required = True)
    parser.add_argument("-l", "--length", dest = "length", help = "the length of the interval", required = True)
    main(parser.parse_args())

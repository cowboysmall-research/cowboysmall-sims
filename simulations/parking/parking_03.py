import sys
import itertools

import argparse

import numpy as np
import matplotlib.pyplot as plt


def parking_problem(length):
    indices = [i for i in range(length - 1)]
    spots   = [0] * length
    count   = 0

    while spots_available(spots) and indices:
        spot = np.random.choice(indices, 1)[0]
        if spots[spot] == 0 and spots[spot + 1] == 0:
            spots[spot]     = 1
            spots[spot + 1] = 1
            indices.remove(spot)
            if spot + 1 in indices:
                indices.remove(spot + 1)

        count += 1

        if count == 10000000:
            break

    return float(spots.count(1)) / float(length)



def spots_available(spots):
    c = [(x[0], len(list(x[1]))) for x in itertools.groupby(spots) if x[0] == 0]
    return max(c, key = lambda x: x[1])[1] > 1 if len(c) > 0 else False



def simulation(iterations, length):
    results = []

    print()
    print('    Parking Problem - Discrete Version: running {} simulations...'.format(iterations))
    print()

    for i in range(iterations):
        results.append(parking_problem(length))
        print('                                      : iteration {:5d}'.format(i + 1), end = '\r')

    print()
    print()
    print('                                      : simulations completed...')
    print()

    return results



def print_results(results):
    print()
    print()
    print('    Parking Problem - Discrete Version: results')
    print()
    print('                          Distribution:')
    print()
    print('                                  mean: {:10.8f}'.format(np.mean(results)))
    print('                    standard deviation: {:10.8f}'.format(np.std(results)))
    print()



def plot_results(results):
    plt.clf()
    plt.hist(results)
    plt.title('Parking Problem - Discrete Version')
    plt.xlabel('Results')
    plt.savefig('./images/parking/parking_discrete_{}.png'.format(len(results)), format = 'png')
    plt.close()



def main(args):
    iterations = int(args.iterations)
    length     = int(args.length)

    results    = simulation(iterations, length)

    print_results(results)
    plot_results(results)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "A script that estimates the jamming limit for Renyi's Parking Problem - Discrete Version")
    parser.add_argument("-n", "--iterations",  dest = "iterations",  help = "the number of iterations to perform", required = True)
    parser.add_argument("-l", "--length", dest = "length", help = "the length of the interval", required = True)
    main(parser.parse_args())

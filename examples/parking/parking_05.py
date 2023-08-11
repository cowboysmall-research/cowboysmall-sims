import argparse

import numpy as np


def spots_available(spots, length, exclusion):
    if 0 <= spots[0] - exclusion:
        return True

    for i in range(len(spots) - 1):
        if spots[i] + exclusion <= spots[i + 1] - exclusion:
            return True

    return spots[-1] + exclusion <= length - exclusion


def spot_found(spot, spots, length, exclusion):
    if 0 <= spot <= spots[0] - exclusion:
        return True

    for i in range(len(spots) - 1):
        if spots[i] + exclusion <= spot <= spots[i + 1] - exclusion:
            return True

    return spots[-1] + exclusion <= spot <= length - exclusion


def get_parking(length):
    return np.random.uniform(0, length)


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


def parking_problem(length, overlap):
    spots = [get_parking(length)]
    count = 0

    while spots_available(spots, length, 1.0 - overlap):
        spot = get_parking(length)

        if spot_found(spot, spots, length, 1.0 - overlap):
            spots.append(spot)
            spots.sort()

        count += 1

        if count == 10000000:
            break

    return (length - total_gaps(sorted(spots))) / float(length)


def simulation(iterations, length, overlap):
    results = []

    print()
    print('    Parking Problem - Overlap Version: running {} simulations'.format(iterations))
    print()
    print('                                    L: {:8d}'.format(length))
    print('                              overlap: {:0.6f}'.format(overlap))
    print()

    for i in range(iterations):
        results.append(parking_problem(length, overlap))
        print('                            iteration: {:8d}'.format(i + 1), end = '\r')

    print('                           iterations: {:8d}'.format(i + 1))
    print()
    print()

    return results


def print_results(results):
    print()
    print('    Parking Problem - Overlap Version: results')
    print()
    print('                         distribution:')
    print('                                 mean: {:0.6f}'.format(np.mean(results)))
    print('                   standard deviation: {:0.6f}'.format(np.std(results)))
    print()


def main(args):
    iterations = int(args.iterations)
    length     = int(args.length)
    overlap    = float(args.overlap)

    print_results(simulation(iterations, length, overlap))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "A script that estimates the jamming limit for Renyi's Parking Problem - Overlap Version")
    parser.add_argument("-n", "--iterations",  dest = "iterations",  help = "the number of iterations to perform", required = True)
    parser.add_argument("-l", "--length", dest = "length", help = "the length of the interval", required = True)
    parser.add_argument("-o", "--overlap", dest = "overlap", help = "the overlap length", required = True)
    main(parser.parse_args())

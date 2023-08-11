import argparse

import numpy as np


def spots_available(spots, length):
    if 0 <= spots[0] - 1.0:
        return True

    for i in range(len(spots) - 1):
        if spots[i] + 1.0 <= spots[i + 1] - 1.0:
            return True

    return spots[-1] + 1 <= length - 1.0


def spot_found(spot, spots, length):
    if 0 <= spot <= spots[0] - 1.0:
        return True

    for i in range(len(spots) - 1):
        if spots[i] + 1.0 <= spot <= spots[i + 1] - 1.0:
            return True

    return spots[-1] + 1.0 <= spot <= length - 1.0


def get_parking(length):
    return np.random.uniform(0, length)


def parking_problem(length):
    spots = [get_parking(length)]
    count = 0

    while spots_available(spots, length):
        spot = get_parking(length)

        if spot_found(spot, spots, length):
            spots.append(spot)
            spots.sort()

        count += 1

        if count == 10000000:
            break

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

    print('         iterations: {:8d}'.format(i + 1))
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


def main(args):
    iterations = int(args.iterations)
    length     = int(args.length)

    print_results(simulation(iterations, length))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "A script that estimates the jamming limit for Renyi's Parking Problem")
    parser.add_argument("-n", "--iterations",  dest = "iterations",  help = "the number of iterations to perform", required = True)
    parser.add_argument("-l", "--length", dest = "length", help = "the length of the interval", required = True)
    main(parser.parse_args())

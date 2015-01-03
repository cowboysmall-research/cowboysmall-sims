import sys
import random

import numpy             as np
import scipy.stats       as st
import matplotlib.pyplot as plt


def simulation():
    birthdays = set()
    counter   = 0

    while len(birthdays) == counter:
        birthdays.add(random.randint(0, 365))
        counter += 1

    return counter


def print_results(numbers, iterations):
    print()
    print('Birthday Paradox')
    print()
    print(' iterations: %8d' % (iterations))
    print()
    print('        Min: %8d'   % (np.min(numbers)))
    print('       25th: %8d'   % (np.percentile(results, 25)))
    print('     Median: %8d'   % (np.median(numbers)))
    print('       75th: %8d'   % (np.percentile(results, 75)))
    print('        Max: %8d'   % (np.max(numbers)))
    print()
    print('       Mean: %8.5f' % (np.mean(numbers)))
    print('        Std: %8.5f' % (np.std(numbers)))
    print('       Mode: %8d'   % (st.mode(numbers)[0][0]))
    print()


def plot_results(numbers):
    plt.clf()
    plt.figure(1, facecolor = 'w')
    plt.hist(numbers, bins = (np.max(numbers) - np.min(numbers)), normed = True)
    plt.title('Birthday Paradox - Histogram')
    plt.xlabel('Number')
    plt.ylabel('Proportion')
    plt.savefig('./src/sim3/images/birthday_paradox_%s.png' % len(numbers), format = 'png')
    plt.close()


def main(argv):
    iterations = int(argv[0])

    numbers = []
    for _ in range(iterations):
        numbers.append(simulation())

    print_results(numbers, iterations)
    plot_results(numbers)


if __name__ == "__main__":
    main(sys.argv[1:])

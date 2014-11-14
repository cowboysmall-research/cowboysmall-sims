import sys
import random

import numpy             as np
# import scipy.stats       as st
import matplotlib.pyplot as plt


def simulation():
    birthdays = set()
    counter   = 0

    while len(birthdays) == counter:
        birthdays.add(random.randint(0, 365))
        counter += 1

    return counter


def print_results(numbers, iterations):
    print
    print 'Birthday Paradox - %s iterations' % (iterations)
    print
    print '    Min : %5d'   % (np.min(numbers))
    print '    Max : %5d'   % (np.max(numbers))
    print '   Mean : %5.2f' % (np.mean(numbers))
    print '    Std : %5.2f' % (np.std(numbers))
    print ' Median : %5d'   % (np.median(numbers))
    # print '   Mode : %5d'   % (st.mode(numbers)[0][0])
    print


def plot_results(numbers):
    plt.figure(1, facecolor = 'w')
    plt.hist(numbers, bins = (np.max(numbers) - np.min(numbers)), normed = True)
    plt.title('Birthday Paradox - Histogram')
    plt.xlabel('Number')
    plt.ylabel('Proportion')
    plt.show()


def main(argv):
    iterations = int(argv[0])

    numbers = []
    for _ in xrange(iterations):
        numbers.append(simulation())

    print_results(numbers, iterations)
    plot_results(numbers)


if __name__ == "__main__":
    main(sys.argv[1:])

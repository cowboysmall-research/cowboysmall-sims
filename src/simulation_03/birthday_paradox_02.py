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
    print('       25th: %8d'   % (np.percentile(numbers, 25)))
    print('     Median: %8d'   % (np.median(numbers)))
    print('       75th: %8d'   % (np.percentile(numbers, 75)))
    print('        Max: %8d'   % (np.max(numbers)))
    print()
    print('       Mean: %8.5f' % (np.mean(numbers)))
    print('        Std: %8.5f' % (np.std(numbers)))
    print('       Mode: %8d'   % (st.mode(numbers)[0][0]))
    print()


def print_prob(numbers, people):
    prob = np.sum(np.bincount(np.array(numbers))[0:people + 1]) / len(numbers)
    print()
    if people < 10:
        print('  P(X <= %d): %8.5f' % (people, prob))
    else:
        print(' P(X <= %2d): %8.5f' % (people, prob))
    print()


def plot_results(numbers):
    plt.clf()
    plt.figure(1, facecolor = 'w')
    plt.hist(numbers, color = 'white', bins = int((np.max(numbers) - np.min(numbers)) / 2), normed = True)
    plt.title('Birthday Paradox - Histogram')
    plt.xlabel('Number')
    plt.ylabel('Proportion')
    plt.savefig('./src/simulation_03/images/birthday_paradox_%s.png' % len(numbers), format = 'png')
    plt.close()


def main(argv):
    iterations = int(argv[0])
    people     = int(argv[1])

    random.seed(1337)

    numbers = []
    for _ in range(iterations):
        numbers.append(simulation())

    print_results(numbers, iterations)
    print_prob(numbers, people)

    plot_results(numbers)


if __name__ == "__main__":
    main(sys.argv[1:])

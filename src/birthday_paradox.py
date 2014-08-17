import sys
import random
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt



def do_simulation_probability(people):
    birthdays = set()

    for _ in xrange(people):
        birthdays.add(random.randint(0, 365))

    return len(birthdays) != people


def do_simulation_distribution():
    birthdays = set()
    counter   = 0

    while len(birthdays) == counter:
        birthdays.add(random.randint(0, 365))
        counter += 1

    return counter


def main(argv):
    people     = int(argv[0])
    iterations = int(argv[1])
    if len(argv) == 3:
        plot = (argv[2] == 'plot')
    else:
        plot = False


    counter = 0
    for _ in xrange(iterations):
        if do_simulation_probability(people):
            counter += 1


    numbers = []
    for _ in xrange(iterations):
        numbers.append(do_simulation_distribution())
    numbers = sorted(numbers)


    print
    print 'Birthday Paradox - %s iterations' % (iterations)
    print
    print 'Probability'
    print '     People : %5d'   % (people)
    print 'Probability : %5.2f' % (counter / float(iterations))
    print
    print 'Distribution'
    print '    Minimum : %5d'   % (numbers[0])
    print '    Maximum : %5d'   % (numbers[-1])
    print '       Mean : %5.2f' % (np.mean(numbers))
    print '        Std : %5.2f' % (np.std(numbers))
    print '     Median : %5d'   % (np.median(numbers))
    print '       Mode : %5d'   % (st.mode(numbers)[0][0])
    print

    if plot:
        plt.hist(numbers, bins = (numbers[-1] - numbers[0]), normed = True, cumulative = True)
        plt.title('Birthday Paradox - Cumulative Distribution')
        plt.xlabel('Number')
        plt.ylabel('Probability')
        plt.show()



if __name__ == "__main__":
    main(sys.argv[1:])


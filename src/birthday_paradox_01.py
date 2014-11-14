import sys
import random


def simulation(people):
    birthdays = set()

    for _ in xrange(people):
        birthdays.add(random.randint(0, 365))

    return len(birthdays) != people


def print_results(people, counter, iterations):
    print
    print 'Birthday Paradox - %s iterations' % (iterations)
    print
    print '     People : %5d'   % (people)
    print 'Probability : %5.2f' % (counter / float(iterations))
    print


def main(argv):
    people     = int(argv[0])
    iterations = int(argv[1])

    counter = 0
    for _ in xrange(iterations):
        if simulation(people):
            counter += 1

    print_results(people, counter, iterations)


if __name__ == "__main__":
    main(sys.argv[1:])

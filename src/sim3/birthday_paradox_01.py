import sys
import random


def simulation(people):
    birthdays = set()

    for _ in range(people):
        birthdays.add(random.randint(0, 365))

    return len(birthdays) != people


def print_results(people, counter, iterations):
    print()
    print('Birthday Paradox')
    print()
    print(' iterations: %8d' % (iterations))
    print()
    print('     People: %8d'   % (people))
    print(' Proportion: %8.5f' % (counter / float(iterations)))
    print()


def main(argv):
    iterations = int(argv[0])
    people     = int(argv[1])

    counter = 0
    for _ in range(iterations):
        if simulation(people):
            counter += 1

    print_results(people, counter, iterations)


if __name__ == "__main__":
    main(sys.argv[1:])

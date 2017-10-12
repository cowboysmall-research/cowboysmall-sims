import sys
import random


def simulation(iterations):
    total = 0

    for _ in range(iterations):
        x, y = random.random(), random.random()
        if (x ** 2) + (y ** 2) < 1:
            total += 1

    return total


def print_results(total, iterations):
    print()
    print('Pi - %s iterations' % (iterations))
    print()
    print(' Total: %8d' % (total))
    print('    Pi: %8f' % (total * 4 / float(iterations)))
    print()


def main(argv):
    iterations = int(argv[0])

    random.seed(1337)

    print_results(simulation(iterations), iterations)


if __name__ == "__main__":
    main(sys.argv[1:])

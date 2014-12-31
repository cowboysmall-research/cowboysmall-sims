import sys
import random


def simulation(iterations):
    total = 0

    x, y = 0, 0
    for _ in xrange(iterations):
        dx, dy = random.gauss(0, 0.25), random.gauss(0, 0.25)
        if abs(x + dx) < 1 and abs(y + dy) < 1:
            x += dx
            y += dy
        if (x ** 2) + (y ** 2) < 1:
            total += 1

    return total


def print_results(total, iterations):
    print
    print 'Pi - %s iterations' % (iterations)
    print
    print ' Total: %8d' % (total)
    print '    Pi: %8f' % (total * 4 / float(iterations))
    print


def main(argv):
    iterations = int(argv[0])

    print_results(simulation(iterations), iterations)


if __name__ == "__main__":
    main(sys.argv[1:])

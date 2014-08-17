import sys
import random


def do_simulation(iterations):
    total = 0

    for _ in xrange(iterations):
        x, y = random.random(), random.random()
        if (x ** 2) + (y ** 2) <= 1:
            total += 1

    return total


def main(argv):
    iterations = int(argv[0])

    total = do_simulation(iterations)

    print
    print 'Pi - %s iterations' % (iterations)
    print
    print 'Total: %8d' % (total)
    print '   Pi: %8f' % (total * 4 / float(iterations))
    print



if __name__ == "__main__":
    main(sys.argv[1:])

import sys
import random


def simulation(heads, tosses, bias):
    total = 0
    count = 0

    while True:
        total += 1

        if random.random() < bias:
        # if random.uniform(0.0, 1.0) < bias:
            count += 1
        else:
            count  = 0

        if count == heads:
            break

    return total



def print_results(heads, tosses, counter, iterations):
    print()
    print('Coin Toss')
    print()
    print('  iterations: %8d' % (iterations))
    print('       heads: %8d' % (heads))
    print()
    if tosses < 10:
        print('    E[X > %d]: %8.5f' % (tosses, counter / float(iterations)))
    else:
        print('   E[X > %2d]: %8.5f' % (tosses, counter / float(iterations)))
    print()



def main(argv):
    iterations = int(argv[0])
    heads      = int(argv[1])
    tosses     = int(argv[2])

    if len(argv) == 4:
        bias = float(argv[3])
    else:
        bias = 0.5

    counter = 0
    for _ in range(iterations):
        counter += simulation(heads, tosses, bias)

    print_results(heads, tosses, counter, iterations)



if __name__ == "__main__":
    main(sys.argv[1:])

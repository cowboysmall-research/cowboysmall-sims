import sys
import random


def simulation(heads, bias):
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



def print_results(heads, counter, iterations):
    print()
    print('Coin Toss')
    print()
    print('  iterations: %8d' % (iterations))
    print('       heads: %8d' % (heads))
    print()
    print('Expected number of tosses to get %d heads in a row: %8.5f' % (heads, counter / float(iterations)))
    print()



def main(argv):
    iterations = int(argv[0])
    heads      = int(argv[1])

    if len(argv) == 4:
        bias = float(argv[2])
    else:
        bias = 0.5

    random.seed(1337)

    counter = 0
    for _ in range(iterations):
        counter += simulation(heads, bias)

    print_results(heads, counter, iterations)



if __name__ == "__main__":
    main(sys.argv[1:])

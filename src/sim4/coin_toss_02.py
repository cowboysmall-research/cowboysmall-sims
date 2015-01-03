import sys
import random

import numpy as np


def markov(heads, tosses, bias):
    A = np.zeros((heads + 1, heads + 1))

    A[0, 0:heads] = 1 - bias
    for i in range(1, heads + 1):
        A[i, i - 1] = bias
    A[heads, heads] = 1.0

    return 1 - np.linalg.matrix_power(A, tosses)[heads, 0]



def print_results(heads, tosses, prob):
    print()
    print('Coin Toss')
    print()
    print('       heads: %d' % (heads))
    print()
    if tosses < 10:
        print('    P(X > %d): %5.5f' % (tosses, prob))
    else:
        print('   P(X > %2d): %5.5f' % (tosses, prob))
    print()



def main(argv):
    heads  = int(argv[0])
    tosses = int(argv[1])

    if len(argv) == 3:
        bias = float(argv[2])
    else:
        bias = 0.5

    prob = markov(heads, tosses, bias)

    print_results(heads, tosses, prob)



if __name__ == "__main__":
    main(sys.argv[1:])

import sys
import random

import numpy as np


def markov(heads, tosses, bias):
    A = np.zeros((heads + 1, heads + 1))

    A[0, 0:heads] = 1 - bias
    for i in range(1, heads + 1):
        A[i, i - 1] = bias
    A[heads, heads] = 1.0

    return np.linalg.matrix_power(A, tosses)[heads, 0]


def main(argv):
    heads  = int(argv[0])
    tosses = int(argv[1])
    bias   = float(argv[2]) if len(argv) == 3 else 0.5

    prob = markov(heads, tosses, bias)

    print()
    print('Coin Toss')
    print()
    print('         heads: %8d' % (heads))
    print()
    print('  P(X <= %4d): %8.5f' % (tosses, prob))
    print()


if __name__ == "__main__":
    main(sys.argv[1:])

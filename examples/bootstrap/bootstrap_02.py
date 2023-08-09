import sys
import random

import numpy             as np
import matplotlib.pyplot as plt



def bootstrap(population, size, iterations):
    samples    = np.empty((iterations, 1))

    for i in range(iterations):
        sample        = np.random.choice(population, size)
        samples[i, 0] = np.median(sample)

    return samples



def print_results(data, results):
    print()
    print(' Median:')
    print('  Value: %0.5f' % (np.median(data)))
    print('   S.E.: \u00B1 %0.5f' % (np.std(results[:, 0])))
    print('   Bias: %0.5f' % (np.mean(results[:, 0]) - np.median(data)))
    print('   C.I.: (%0.5f, %0.5f)' % (np.percentile(results[:, 0], 2.5), np.percentile(results[:, 0], 97.5)))
    print()



def main(argv):
    mean       = int(argv[0])
    std        = int(argv[1])
    size       = int(argv[2])
    iterations = int(argv[3])

    np.random.seed(1337)

    data    = np.random.normal(mean, std, size)
    samples = bootstrap(data, size, iterations)

    print_results(data, samples)



if __name__ == "__main__":
    main(sys.argv[1:])

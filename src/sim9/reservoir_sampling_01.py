import sys
import random
import math

import numpy             as np
import matplotlib.pyplot as plt


def reservoir_sampling(data, size, k):
    samples = np.empty((size - k, 2))

    sample  = []
    for i in range(size):
        if i < k:
            sample.append(data[i])
        else:
            p = np.random.randint(0, i)
            if p < k:
                sample[p] = data[i]
            samples[i - k, 0] = np.mean(sample)
            samples[i - k, 1] = np.std(sample)

    return samples


def print_results(results, data, k):
    print()
    print('       Population Distribution:')
    print()
    print('                          mean: %10.5g' % np.mean(data))
    print('            standard deviation: %10.5g' % np.std(data))
    print()
    print()
    print('         Sampling Distribution:')
    print()
    print('              theoretical mean: %10.5g' % np.mean(data))
    print('theoretical standard deviation: %10.5g' % (np.std(data) / math.sqrt(k)))
    print()
    print()
    print('         Observed Distribution:')
    print()
    print('                          mean: %10.5g' % np.mean(results[:, 0]))
    print('                          bias: %10.5g' % (np.mean(results[:, 0]) - np.mean(data)))
    print()
    print('            standard deviation: %10.5g' % np.std(results[:, 0]))
    print('                          bias: %10.5g' % (np.mean(results[:, 1]) - np.std(data)))
    print()


def plot_results(results, size, k):
    plt.clf()
    plt.figure(1, facecolor = 'w')
    plt.hist(results[:, 0], color = 'white', bins = 25, normed = True)
    plt.title('Reservoir Samples (k = %s)' % (k))
    plt.xlabel('Sample Mean')
    plt.ylabel('Proportion')
    plt.savefig('./src/sim9/images/reservoir_sampling_%s_%s.png' % (size, k), format = 'png')
    plt.close()


def main(argv):
    size    = int(argv[0])
    k       = int(argv[1])

    np.random.seed(1337)

    data    = np.random.randint(1, size, size)
    results = reservoir_sampling(data, size, k)

    print_results(results, data, k)
    plot_results(results, size, k)


if __name__ == "__main__":
    main(sys.argv[1:])

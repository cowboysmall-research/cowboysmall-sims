import sys
import random

import numpy             as np
import matplotlib.pyplot as plt


def simulation(men, women, pool_size):
    paired = 0

    while len(men) > 0 and max(men) > min(women):
        np.random.shuffle(men)
        np.random.shuffle(women)
        for man, woman in zip(men, women):
            if man > woman:
                paired += 1
                men.remove(man)
                women.remove(woman)

    return paired



def print_results(results):
    print()
    print('Dating Game (evenly distributed qualities)')
    print()
    print('           Minimum: %s' % (np.amin(results)))
    print('   25th Percentile: %s' % (np.percentile(results, 25)))
    print('            Median: %s' % (np.median(results)))
    print('   75th Percentile: %s' % (np.percentile(results, 75)))
    print('           Maximum: %s' % (np.amax(results)))
    print()
    print('              Mean: %s' % (np.mean(results)))
    print('Standard Deviation: %s' % (np.std(results)))
    print('          Variance: %s' % (np.var(results)))
    print()



def plot_results(results, pool_size):
    plt.clf()
    plt.title('Dating Game (evenly distributed qualities)')

    plt.xlabel('Dating')
    plt.ylabel('Proportion')

    plt.figure(1, facecolor = 'w')
    plt.hist(results, bins = int((np.max(results) - np.min(results)) / 2), density = True)

    plt.savefig('./images/dating/dating_even_%s_%s.png' % (pool_size, len(results)), format = 'png')
    plt.close()



def main(argv):
    pool_size  = int(argv[0])
    iterations = int(argv[1])

    np.random.seed(1337)

    results = []
    for _ in range(iterations):
        men     = [100 * (float(val) / pool_size) for val in range(pool_size)]
        women   = [100 * (float(val) / pool_size) for val in range(pool_size)]
        results.append(simulation(men, women, pool_size))

    print_results(results)

    plot_results(results, pool_size)



if __name__ == "__main__":
    main(sys.argv[1:])

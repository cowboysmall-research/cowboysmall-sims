import sys
import random

import numpy             as np
import matplotlib.pyplot as plt


def simulation(men, women, pool_size):
    while len(men) > 0 and max(men) > min(women):
        np.random.shuffle(men)
        np.random.shuffle(women)
        for man, woman in zip(men, women):
            if man > woman:
                men.remove(man)
                women.remove(woman)

    return max(men)



def print_results(results):
    print()
    print('Dating Game (uniformly distributed qualities)')
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
    plt.figure(1, facecolor = 'w')
    plt.hist(results, color = 'white', bins = (np.max(results) - np.min(results)) / 2, normed = True)
    plt.title('Dating Game (uniformly distributed qualities)')
    plt.xlabel('Quality')
    plt.ylabel('Proportion')
    plt.savefig('./src/simulation_05/images/quality_uniform_%s_%s.png' % (pool_size, len(results)), format = 'png')
    plt.close()



def main(argv):
    pool_size  = int(argv[0])
    iterations = int(argv[1])

    np.random.seed(1337)

    results = []
    for _ in range(iterations):
        men     = np.random.random_integers(0, 100, pool_size).tolist()
        women   = np.random.random_integers(0, 100, pool_size).tolist()
        results.append(simulation(men, women, pool_size))

    print_results(results)

    plot_results(results, pool_size)



if __name__ == "__main__":
    main(sys.argv[1:])

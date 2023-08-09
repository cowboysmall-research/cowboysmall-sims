import sys
import random

import numpy             as np
import matplotlib.pyplot as plt



def bootstrap(population, size, iterations):
    samples    = np.empty((iterations, 4))

    for i in range(iterations):
        sample        = np.random.choice(population, size)
        samples[i, 0] = np.mean(sample)
        samples[i, 1] = np.median(sample)
        samples[i, 2] = np.std(sample)
        samples[i, 3] = np.var(sample)

    return samples



def print_results(data, results):
    print()
    print('               Mean:')
    print('              Value: %0.5f' % (np.mean(data)))
    print('               S.E.: \u00B1 %0.5f' % (np.std(results[:, 0])))
    print('               Bias: %0.5f' % (np.mean(results[:, 0]) - np.mean(data)))
    print('               C.I.: (%0.5f, %0.5f)' % (np.percentile(results[:, 0], 2.5), np.percentile(results[:, 0], 97.5)))
    print()
    print('             Median:')
    print('              Value: %0.5f' % (np.median(data)))
    print('               S.E.: \u00B1 %0.5f' % (np.std(results[:, 1])))
    print('               Bias: %0.5f' % (np.mean(results[:, 1]) - np.median(data)))
    print('               C.I.: (%0.5f, %0.5f)' % (np.percentile(results[:, 1], 2.5), np.percentile(results[:, 1], 97.5)))
    print()
    print(' Standard Deviation:')
    print('              Value: %0.5f' % (np.std(data)))
    print('               S.E.: \u00B1 %0.5f' % (np.std(results[:, 2])))
    print('               Bias: %0.5f' % (np.mean(results[:, 2]) - np.std(data)))
    print('               C.I.: (%0.5f, %0.5f)' % (np.percentile(results[:, 2], 2.5), np.percentile(results[:, 2], 97.5)))
    print()
    print('           Variance:')
    print('              Value: %0.5f' % (np.var(data)))
    print('               S.E.: \u00B1 %0.5f' % (np.std(results[:, 3])))
    print('               Bias: %0.5f' % (np.mean(results[:, 3]) - np.var(data)))
    print('               C.I.: (%0.5f, %0.5f)' % (np.percentile(results[:, 3], 2.5), np.percentile(results[:, 3], 97.5)))
    print()



def plot_results(samples, size, iterations, statistic):
    plt.clf()
    plt.title('Bootstrapped Samples (%s)' % (statistic))

    plt.xlabel('Samples')
    plt.ylabel('Proportion')

    plt.figure(1, facecolor = 'w')
    plt.hist(samples, bins = 25, density = True)

    plt.savefig('./images/bootstrap/bootstrap_%s_%s_%s.png' % ('_'.join(statistic.split()), size, iterations), format = 'png')
    plt.close()



def main(argv):
    mean       = int(argv[0])
    std        = int(argv[1])
    size       = int(argv[2])
    iterations = int(argv[3])

    np.random.seed(1337)

    data    = np.random.normal(mean, std, size)
    samples = bootstrap(data, size, iterations)

    print_results(data, samples)
    plot_results(samples[:, 0], size, iterations, 'mean')
    plot_results(samples[:, 1], size, iterations, 'median')
    plot_results(samples[:, 2], size, iterations, 'standard deviation')
    plot_results(samples[:, 3], size, iterations, 'variance')



if __name__ == "__main__":
    main(sys.argv[1:])

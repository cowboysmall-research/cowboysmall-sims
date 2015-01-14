import sys
import random

import numpy             as np
import scipy.stats       as st
import matplotlib.pyplot as plt


def simulation(iterations, heads, bias):
    results = []

    for _ in range(iterations):

        total = 0
        count = 0
        while count < heads:
            total += 1

            if random.random() < bias:
            # if random.uniform(0.0, 1.0) < bias:
                count += 1
            else:
                count  = 0

        results.append(total)

    return results



def print_results(results):
    print()
    print('Coin Toss')
    print()
    print('  iterations: %8d'   % (len(results)))
    print()
    print('         Min: %8d'   % (np.min(results)))
    print('        25th: %8d'   % (np.percentile(results, 25)))
    print('      Median: %8d'   % (np.median(results)))
    print('        75th: %8d'   % (np.percentile(results, 75)))
    print('         Max: %8d'   % (np.max(results)))
    print()
    print('        Mean: %8.5f' % (np.mean(results)))
    print('         Std: %8.5f' % (np.std(results)))
    print('        Mode: %8d'   % (st.mode(results)[0][0]))
    print()



def print_prob(results, tosses):
    prob = np.sum(np.bincount(np.array(results))[tosses + 1:]) / len(results)
    print()
    if tosses < 10:
        print('    P(X > %d): %8.5f' % (tosses, prob))
    else:
        print('   P(X > %2d): %8.5f' % (tosses, prob))
    print()



def plot_results(results, heads, bias):
    plt.clf()
    plt.figure(1, facecolor = 'w')
    plt.hist(results, color = 'white', bins = (np.max(results) - np.min(results)) / 2, normed = True)
    plt.title('Coint Toss: %s heads in a row - Histogram' % heads)
    plt.xlabel('Tosses')
    plt.ylabel('Proportion')
    plt.savefig('./src/sim4/images/coin_toss_%s_%s_%s.png' % (heads, bias, len(results)), format = 'png')
    plt.close()



def main(argv):
    iterations = int(argv[0])
    heads      = int(argv[1])
    tosses     = int(argv[2])

    if len(argv) == 4:
        bias = float(argv[3])
    else:
        bias = 0.5

    random.seed(1337)

    results = simulation(iterations, heads, bias)

    print_results(results)
    print_prob(results, tosses)

    plot_results(results, heads, bias)



if __name__ == "__main__":
    main(sys.argv[1:])

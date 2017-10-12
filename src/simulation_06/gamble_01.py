import sys
import random

import numpy             as np
import matplotlib.pyplot as plt



def plot_results(results, iterations, initial, margin):
    plt.clf()
    plt.figure(1, facecolor = 'w')
    plt.plot(range(len(results)), results)
    plt.title('Gamble: %s iterations' % iterations)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.savefig('./src/simulation_06/images/gamble_%s_%s_%s.png' % (iterations, initial, margin), format = 'png')
    plt.close()



def main(argv):
    iterations = int(argv[0])
    initial    = int(argv[1])
    margin     = int(argv[2])
    target     = initial + margin

    np.random.seed(1337)

    results        = np.zeros((iterations, 3))
    results[:, 0]  = np.random.sample(iterations)
    results[:, 1]  = 1
    results[0, 2]  = initial


    for i in range(1, iterations):
        if 0 < results[i - 1, 2] < target:
            if results[i - 1, 0] < 0.5:
                results[i, 2]  = results[i - 1, 2] + results[i - 1, 1]
            else:
                results[i, 2]  = results[i - 1, 2] - results[i - 1, 1]
                results[i, 1]  = 2 * results[i - 1, 1]
        else:
            break


    plot_results(results[results[:, 2] > 0, 2], iterations, initial, margin)



if __name__ == "__main__":
    main(sys.argv[1:])

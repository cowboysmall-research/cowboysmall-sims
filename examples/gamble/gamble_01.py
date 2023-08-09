import sys
import random

import numpy             as np
import matplotlib.pyplot as plt



def plot_results(results, iterations, initial, margin):
    plt.clf()
    plt.title('Gamble: %s iterations' % iterations)

    plt.xlabel('Index')
    plt.ylabel('Value')

    plt.figure(1, facecolor = 'w')
    plt.plot(range(len(results)), results)

    plt.savefig('./images/gamble/gamble_%s_%s_%s.png' % (iterations, initial, margin), format = 'png')
    plt.close()



def main(argv):
    iterations = int(argv[0])
    initial    = int(argv[1])
    margin     = int(argv[2])
    target     = initial + margin

    np.random.seed(1337)

    results        = np.zeros((iterations + 1, 3))
    results[1:, 0] = np.random.sample(iterations)
    results[1:, 1] = 1
    results[0, 2]  = initial


    for i in range(iterations):
        if 0 < results[i, 2] < target:
            if results[i, 0] < 0.5:
                results[i + 1, 2] = results[i, 2] + results[i, 1]
            else:
                results[i + 1, 2] = results[i, 2] - results[i, 1]
                results[i + 1, 1] = results[i, 1] * 2
        else:
            break

    # for row in results:
    #     print('{:7.3f} {:7.3f} {:7.3f}'.format(*row))


    plot_results(results[results[:, 2] > 0, 2], iterations, initial, margin)



if __name__ == "__main__":
    main(sys.argv[1:])

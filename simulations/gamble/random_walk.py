import sys
import random

import numpy             as np
import matplotlib.pyplot as plt



def simulation(value, iterations):
    results = []

    for _ in range(iterations):
        if random.random() < 0.5:
            value += 1
        else:
            value -= 1

        results.append(value)

    return results



def plot_results(results, iterations):
    plt.clf()
    plt.figure(1, facecolor = 'w')
    plt.plot(range(iterations), results)
    plt.title('Random Walk: %s iterations' % iterations)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.savefig('./images/gamble/random_walk_%s.png' % (iterations), format = 'png')
    plt.close()



def main(argv):
    iterations = int(argv[0])
    initial    = int(argv[1])

    random.seed(1337)

    results    = simulation(initial, iterations)

    plot_results(results, iterations)



if __name__ == "__main__":
    main(sys.argv[1:])

import sys
import random

import numpy             as np
import matplotlib.pyplot as plt



def simulation(iterations):
    inside  = []
    outside = []

    for _ in range(iterations):
        x, y = random.random(), random.random()
        if (x ** 2) + (y ** 2) <= 1:
            inside.append((x, y))
        else:
            outside.append((x, y))

    return np.array(inside), np.array(outside)



def print_results(total, iterations):
    print()
    print('Pi - %s iterations' % (iterations))
    print()
    print(' Total: %8d' % (total))
    print('    Pi: %8f' % (total * 4 / float(iterations)))
    print()



def plot_results(inside, outside, iterations):
    plt.clf()
    plt.figure(1, facecolor = 'w')

    fig, ax = plt.subplots()

    ax.scatter(inside[:, 0], inside[:, 1], c = 'blue', s = 1.0, label = 'inside')
    ax.scatter(outside[:, 0], outside[:, 1], c = 'red', s = 1.0, label = 'outside')
    ax.set_aspect('equal')
    ax.legend(loc='upper right')
    ax.grid(True)

    plt.title('Pi: %s iterations' % iterations)
    plt.savefig('./images/pi/pi_%s.png' % (iterations), format = 'png')
    plt.close()



def main(argv):
    iterations = int(argv[0])

    random.seed(1337)

    inside, outside = simulation(iterations)

    plot_results(inside, outside, iterations)
    print_results(len(inside), iterations)



if __name__ == "__main__":
    main(sys.argv[1:])

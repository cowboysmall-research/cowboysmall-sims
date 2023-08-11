import sys
import random

from cowboysmall.sims.simulation import Simulation


class MonteHall(Simulation):

    def step(self, iteration: int, data: dict) -> None:
        doors  = [0] * 3
        car    = random.randint(0, 2)
        choice = random.randint(0, 2)

        doors[car]    += 1
        doors[choice] += 1

        reveal = random.choice(list(set(range(3)) - set([choice, car])))
        doors[reveal] = -1

        if 'jump' in data and data['jump']:
            for i in range(3):
                if i != choice and doors[i] != -1:
                    doors[choice] -= 1
                    doors[i]      += 1

        data['count'] += doors[car] == 2


def main(argv):
    random.seed(1337)

    iterations = int(argv[0])

    sim1  = MonteHall({'count': 0})
    sim2  = MonteHall({'count': 0, 'jump': True})

    data1 = sim1.run(iterations)
    data2 = sim2.run(iterations)

    print()
    print('Monte Hall - %s iterations' % (iterations))
    print()
    print('Correct without jumping: %8d' % (data1['count']))
    print('             Proportion: %8f' % (data1['count'] / float(iterations)))
    print()
    print('   Correct with jumping: %8d' % (data2['count']))
    print('             Proportion: %8f' % (data2['count'] / float(iterations)))
    print()


if __name__ == "__main__":
    main(sys.argv[1:])

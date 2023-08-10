import sys
import random

from cowboysmall.sims.simulation import Simulation


class BirthdayParadox(Simulation):

    def step(self, iteration: int, data: dict) -> None:
        birthdays = set()

        for _ in range(data['people']):
            birthdays.add(random.randint(0, 365))

        data['count'] += len(birthdays) != data['people']


def main(argv):
    iterations = int(argv[0])
    people     = int(argv[1])

    sim  = BirthdayParadox({'people': people, 'count': 0})
    data = sim.run(iterations)

    print()
    print('Birthday Paradox')
    print()
    print(' iterations: %8d' % (iterations))
    print()
    print('     People: %8d'   % (people))
    print(' Proportion: %8.5f' % (data['count'] / float(iterations)))
    print()


if __name__ == "__main__":
    main(sys.argv[1:])

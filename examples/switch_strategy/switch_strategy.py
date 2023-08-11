import sys
import random

from cowboysmall.sims.simulation import Simulation


class SwitchStrategy(Simulation):

    def step(self, iteration: int, data: dict) -> None:
        prisoners = data['prisoners']
        leader    = data['leader']
        count     = data['count']
        switch    = 0

        while prisoners[leader] < count - 1:
            data['days'] += 1
            p = random.choice(range(count))

            if p == leader:
                if switch == 1:
                    switch = 0
                    prisoners[p] += 1
            else:
                if prisoners[p] == 0 and switch == 0:
                    switch = 1
                    prisoners[p] += 1


def main(argv):
    random.seed(1337)

    count = int(argv[0])

    prisoners = [0] * count
    leader    = random.choice(range(count))

    sim  = SwitchStrategy({'prisoners': prisoners, 'leader': leader, 'count': count, 'days': 0})
    data = sim.run(1)

    print()
    print('Switch Strategy:')
    print()
    print('All visited after %s years and %s days' % (data['days'] // 365, data['days'] % 365))
    print()


if __name__ == "__main__":
    main(sys.argv[1:])

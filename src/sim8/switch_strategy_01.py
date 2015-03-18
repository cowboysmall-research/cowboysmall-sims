import sys
import random


def switch_strategy_simulation(count):
    prisoners = [0] * count
    leader    = random.randint(0, count - 1)

    switch    = 0
    days      = 0

    while prisoners[leader] < count - 1:
        days += 1
        p = random.randint(0, count - 1)
        if p == leader:
            if switch == 1:
                switch        = 0
                prisoners[p] += 1
        else:
            if prisoners[p] == 0 and switch == 0:
                switch        = 1
                prisoners[p] += 1

    return days


def print_results(days):
    print()
    print('All Visited!')
    print('After %s years and %s days' % (days // 365, days % 365))
    print()


def main(argv):
    count = int(argv[0])
    days  = switch_strategy_simulation(count)

    print_results(days)


if __name__ == "__main__":
    main(sys.argv[1:])

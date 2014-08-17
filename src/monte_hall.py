import sys
import random



def do_simulation(choice, jump = False):
    doors = [0] * 3
    car   = random.randint(0, 2)

    doors[car]    += 1
    doors[choice] += 1

    reveal = random.randint(0, 2)
    while reveal == car or reveal == choice:
        reveal = random.randint(0, 2)
    doors[reveal] = -1

    if jump:
        for i in xrange(len(doors)):
            if i != choice and doors[i] != -1:
                doors[choice] -= 1
                doors[i]      += 1 

    return doors[car] == 2



def main(argv):
    iterations = int(argv[0])

    counter1 = 0
    counter2 = 0
    for _ in xrange(iterations):
        if do_simulation(random.randint(0, 2)):
            counter1 += 1
        if do_simulation(random.randint(0, 2), True):
            counter2 += 1


    print
    print 'Monte Hall - %s iterations' % (iterations)
    print
    print 'Correct without jumping: %8d' % (counter1)
    print '                  Ratio: %8f' % (counter1 / float(iterations))
    print
    print '   Correct with jumping: %8d' % (counter2)
    print '                  Ratio: %8f' % (counter2 / float(iterations))
    print



if __name__ == "__main__":
    main(sys.argv[1:])


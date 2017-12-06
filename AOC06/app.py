import copy
import operator

INPUT = '2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14' # result: 3156 | 1610
#INPUT = '0  2   7   0' # result: 5 | 4

snapshots = []


def create_snapshot(list):
    return ''.join(map(lambda x: '{0}'.format(x), list))

def next_index(i):
    return (i + 1) % N

def redistribute(memory):
    index, blocks = get_max_bank(memory)
    memory[index] = 0

    index = next_index(index)
    while blocks > 0:
        memory[index] += 1
        blocks -= 1
        index = next_index(index)

    return memory


def get_max_bank(list):
    index, value = max(enumerate(list), key=operator.itemgetter(1))

    return (index, value)

def run_until_inifinite(memory):
    steps = 0
    snapshots.append(create_snapshot(memory))

    while True:
        memory = redistribute(copy.copy(memory))
        steps += 1
        s = create_snapshot(memory)

        if s in snapshots:
            return (steps, steps - snapshots.index(s))
        else:
            snapshots.append(s)


if __name__ == "__main__":
    global N

    input = map(lambda x: int(x), INPUT.split())
    N = len(input)

    (steps, loop_size) = run_until_inifinite(copy.copy(input))
    print 'Steps to detect inifinite loop: {0}'.format(steps)
    print 'Loop size: {0}'.format(loop_size)
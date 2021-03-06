import copy

EXAMPLE = '0 3 0 1 -3'

def read_instructions(filepath):
    with open(filepath) as f:
        content = f.read()
        return map(lambda x: int(x), content.split('\n'))

def run_instructions(instructions):
    length = len(instructions)
    position = 0
    steps_count = 0

    while True:
        jump = int(instructions[position])
        instructions[position] += 1
        steps_count += 1
        position += jump
        if position >= length:
            return steps_count

def run_weird_instructions(instructions):
    length = len(instructions)
    position = 0
    steps_count = 0

    while True:
        jump = int(instructions[position])

        if jump >= 3:
            instructions[position] -= 1
        else:
            instructions[position] += 1

        steps_count += 1
        position += jump

        if position >= length:
            return steps_count


if __name__ == '__main__':
    instructions_list = read_instructions('./AOC05/input.io')

    # movements_count = run_instructions(map(lambda x: int(x), EXAMPLE.split()))
    movements_count = run_instructions(copy.copy(instructions_list))
    print 'Movements count: {0}'.format(movements_count)

    # movements_count = run_weird_instructions(map(lambda x: int(x), EXAMPLE.split()))
    movements_count = run_weird_instructions(copy.copy(instructions_list))
    print 'Weird movements count: {0}'.format(movements_count)
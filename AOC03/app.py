# http://adventofcode.com/2017/day/3

# 1 => 0
# 12 => 3
# 23 => 2
# 1024 => 31

INPUT = 277678  # output: 475

DIRECTIONS = {
    0: (1, 0), # right
    1: (0, 1),       # up
    2: (-1, 0),            # left
    3: (0, -1)            # down
}

class ManhattanDistanceComputer(object):
    @staticmethod
    def compute(a, b):
        return abs(a.x - b.x) + abs(a.y - b.y)

class Cell(object):
    def __init__(self, val, x, y):
        self.val = val
        self.x = x
        self.y = y

    def is_corner(self):
        return abs(self.x) == abs(self.y)

    def is_last_corner(self, length):
        if self.val == 1:
            return True

        return self.val == pow(length * 2 + 1, 2)


class SpiralMemory1(object):
    def __init__(self, lenght):
        self.cells = []
        self._generate_simple(lenght)

    def get_cell(self, val):
        try:
            return self.cells[val-1]
        except:
            return None

    def _next_position(self, current_position, dx, dy):
        return Cell(current_position.val + 1, current_position.x + dx, current_position.y + dy)

    def _generate_simple(self, length):

        current = Cell(1, 0 , 0)

        self.cells.append(current)
        current_direction = 0
        current_length = 0

        for i in range(2, length + 1):
            if current.is_last_corner(current_length) == True:
                current_length += 1
                dir = DIRECTIONS[current_direction]
                current = self._next_position(current, dir[0], dir[1])
                self.cells.append(current)
                current_direction = (current_direction + 1) % 4
                continue

            elif current.is_corner() == True:
                current_direction = (current_direction + 1) % 4

            dir = DIRECTIONS[current_direction]
            current = self._next_position(current, dir[0], dir[1])

            self.cells.append(current)

        pass

mem = SpiralMemory1(INPUT)
cell = mem.get_cell(INPUT)

print ManhattanDistanceComputer.compute(Cell(1, 0, 0), cell)

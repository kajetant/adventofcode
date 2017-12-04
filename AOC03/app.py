# http://adventofcode.com/2017/day/3

# 1 => 0
# 12 => 3
# 23 => 2
# 1024 => 31

INPUT = 277678
# output1: 475
# output2: 279138

DIRECTIONS = {
    0: (1, 0),  # right
    1: (0, 1),  # up
    2: (-1, 0), # left
    3: (0, -1)  # down
}

class ManhattanDistanceComputer(object):
    @staticmethod
    def compute(a, b):
        return abs(a.x - b.x) + abs(a.y - b.y)

class Cell(object):
    def __init__(self, id, val, x, y):
        self.id = id
        self.val = val
        self.x = x
        self.y = y

    def is_corner(self):
        return abs(self.x) == abs(self.y)

    def is_last_corner(self, length):
        if self.id == 1:
            return True

        return self.is_corner() and self.x == length and self.y == -length


class SpiralMemorySpecial(object):
    def __init__(self):
        self.special_cells = []

    def _next_position(self, current_position, dx, dy):
        return Cell(current_position.id + 1, current_position.val + 1, current_position.x + dx, current_position.y + dy)

    def _get_neighbors(self, current, direction):
        x = current.x
        y = current.y
        id = current.id

        if direction == 0:  # right
            neighbors = filter(lambda c: c.id < id and ((c.x == x-1 and c.y == y) or (c.x == x-1 and c.y == y+1) or (c.x == x and c.y == y+1) or (c.x == x+1 and c.y == y+1)), self.special_cells)
        elif direction == 1: # up
            neighbors = filter(lambda c: c.id < id and ((c.x == x and c.y == y-1) or (c.x == x-1 and c.y == y-1) or (c.x == x-1 and c.y == y) or (c.x == x-1 and c.y == y+1)), self.special_cells)
        elif direction == 2: # left
            neighbors = filter(lambda c: c.id < id and ((c.x == x+1 and c.y == y) or (c.x == x+1 and c.y == y-1) or (c.x == x and c.y == y-1) or (c.x == x-1 and c.y == y-1)), self.special_cells)
        elif direction == 3: # down
            neighbors = filter(lambda c: c.id < id and ((c.x == x and c.y == y+1) or (c.x == x+1 and c.y == y+1) or (c.x == x+1 and c.y == y) or (c.x == x+1 and c.y == y-1)), self.special_cells)

        return neighbors

    def compute_result(self, input):

        current = Cell(1, 1, 0, 0)
        self.special_cells.append(current)
        current_direction = 0
        current_length = 0

        for i in range(2, input+1):
            if current.is_last_corner(current_length) == True:
                current_length += 1
                dir = DIRECTIONS[current_direction]
                current = self._next_position(current, dir[0], dir[1])

                neighbor_cells = self._get_neighbors(current, current_direction)
                value = reduce(lambda x,y: x+y, map(lambda c: c.val, neighbor_cells))

                if value > input:
                    return value

                current.val = value
                self.special_cells.append(current)
                current_direction = (current_direction + 1) % 4
                continue

            elif current.is_corner() == True:
                current_direction = (current_direction + 1) % 4

            dir = DIRECTIONS[current_direction]
            current = self._next_position(current, dir[0], dir[1])

            neighbor_cells = self._get_neighbors(current, current_direction)
            value = reduce(lambda x,y: x+y, map(lambda c: c.val, neighbor_cells))

            if value > input:
                return value

            current.val = value
            self.special_cells.append(current)

class SpiralMemory(object):
    def __init__(self, lenght):
        self.cells = []
        self.special_cells = []
        self._generate_simple(lenght)

    def get_cell(self, val):
        try:
            return self.cells[val-1]
        except:
            return None

    def _next_position(self, current_position, dx, dy):
        return Cell(current_position.id + 1, current_position.id + 1, current_position.x + dx, current_position.y + dy)

    def _generate_simple(self, length):

        current = Cell(1, 1, 0 , 0)

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

# mem = SpiralMemory(INPUT)
# cell = mem.get_cell(INPUT)
# print ManhattanDistanceComputer.compute(Cell(1, 1, 0, 0), cell)

special_memory = SpiralMemorySpecial()
print special_memory.compute_result(INPUT)

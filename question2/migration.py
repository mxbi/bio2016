import numpy as np  # NumPy linear algebra package, can be installed with pip.
import itertools

class Landscape():
    def __init__(self, start, n, sequence, debug=False, border=5):
        self.border = border
        self.size = border * 2 + 5
        self.matrix = np.zeros((self.size, self.size))

        self.start = start - 1  # IMPORTANT: Zero-indexed
        self.sequence = sequence
        self.steps = n
        self.last = self.start
        self.debug = debug

    # String representation of landscape
    def __repr__(self):
        rep = ''
        for row in self.matrix[self.border:self.border + 5, self.border:self.border + 5]:
            rep += ' '.join([str(int(i)) for i in row])
            rep += '\n'
        return rep

    # Run steps of the simulation
    def run_simulation(self):
        self.place(self.start)

        self.step_sizes = itertools.cycle(self.sequence)
        self.step = 1
        for step_size in self.step_sizes:
            self.step += 1
            if self.step > self.steps:
                break
            pos = (self.last + step_size) % 25
            self.place(pos)
            self.migrate()
            self.last = pos

    # Convert number to coordinates
    def unravel(self, num):
        # num -= 1 # Zero-index
        row = int(num / 5)
        col = num % 5
        row, col = row + self.border, col + self.border
        return row, col

    # Add a person at the selected ID
    def place(self, id):
        coor = self.unravel(id)
        self.matrix[coor] += 1

    # Perform a migration on a first square with more than 4 people
    def migrate(self):
        coors = []
        for x in range(self.size):
            for y in range(self.size):
                if self.matrix[x, y] >= 4:
                    coors.append((x, y))
        if len(coors) > 0:
            coor = coors[0]
            self.migration(coor)
        elif self.debug:
            print('WARNING: No migration possible, step:', self.step)

    # Calculate a migration at a set coordinate
    def migration(self, coor):
        pre_total = np.sum(self.matrix)
        if self.matrix[coor] < 4 and self.debug:
            print('ERROR: Migration below threshold')
        transforms = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        self.matrix[coor] -= 4
        for t in transforms:
            tt = (t[0] + coor[0], t[1] + coor[1])
            try:
                self.matrix[tt] += 1
            except IndexError:
                if self.debug:
                    print('ERROR: Out-of-bounds migration, increase border size.')
        post_total = np.sum(self.matrix)
        if pre_total != post_total and self.debug:
            print('ERROR: Total not preserved through migration')

if __name__ == '__main__':
    starting_position, sequence_length, n = [int(i) for i in input().split(' ')]
    sequence = [int(i) for i in input().split(' ')]

    landscape = Landscape(starting_position, n, sequence, debug=False)
    landscape.run_simulation()
    print(landscape)

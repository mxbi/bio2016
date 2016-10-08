import numpy as np

class Promenade():
    def __init__(self):
        self.lprom = (1, 0)
        self.rprom = (0, 1)

        self.prom = self.combine(self.lprom, self.rprom)

    def __repr__(self):
        rep = str(self.prom[0]) + ' / ' + str(self.prom[1])
        return rep

    def combine(self, l, r):
        return (l[0] + r[0], l[1] + r[1])

    def left_step(self):
        self.lprom = self.prom
        self.prom = self.combine(self.lprom, self.rprom)

    def right_step(self):
        self.rprom = self.prom
        self.prom = self.combine(self.lprom, self.rprom)

    def input(self, s):
        for char in s:
            if char == 'R':
                self.right_step()
            elif char == 'L':
                self.left_step()
            else:
                print('ERROR: Char not recognised, must be either L or R - Ignoring.')

if __name__ == '__main__':
    p = Promenade()
    p.input(input())
    print(p)

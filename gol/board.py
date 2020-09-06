import numpy as np
from itertools import product


class Board(np.ndarray):

    def update(self):
        neighbours = self.get_neighbours()
        self[(self == 0) & (neighbours == 3)] = 1
        self[(self == 1) & ((neighbours < 2) | (neighbours > 3))] = 0

    def get_neighbours(self):
        result = np.zeros(self.shape, dtype=int)
        for row, col in product([-1, 0, 1], repeat=2):
            if row != 0 or col != 0:
                result += np.roll(self, (row, col), (0, 1))
        return result

    @classmethod
    def from_int_data(cls, board_data):
        arr = np.array(board_data, dtype=int)
        return arr.view(cls)

    @classmethod
    def from_string_data(cls, *lines):
        return cls.from_int_data(tuple(
            tuple(1 if char != ' ' else 0 for char in line)
            for line in lines
        ))

    @classmethod
    def from_zeros(cls, rows, cols):
        arr = np.zeros((rows, cols), dtype=int)
        return arr.view(cls)


import random


class Game:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.grid = [[random.choice([0, 1]) for col in range(cols)] for row in range(rows)]

    def print_grid(self):
        for row in self.grid:
            print(row)

    def check_neighbors(self, x, y):
        neighbors = 0

        for rowIndex in range(-1, 2):
            for colIndex in range(-1, 2):
                if rowIndex == 0 and colIndex == 0:
                    continue
                if 0 <= (x + colIndex) < self.cols and 0 <= (y + rowIndex) < self.rows:
                    cell = self.grid[y + rowIndex][x + colIndex]
                    neighbors += cell

        return neighbors
import random


class Game:
    def __init__(self, rows: int, cols: int) -> None:
        self.grid = [[random.choice([0, 1]) for col in range(cols)] for row in range(rows)]

    def print_grid(self):
        for row in self.grid:
            print(row)
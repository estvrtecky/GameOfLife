import pygame
import random


class Grid:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.grid = [[random.choice([0, 1]) for col in range(cols)] for row in range(rows)]

    def print_grid(self):
        for row in self.grid:
            print(row)

    def check_neighbors(self, x: int, y: int) -> int:
        neighbors = 0

        for rowIndex in range(-1, 2):
            for colIndex in range(-1, 2):
                if rowIndex == 0 and colIndex == 0:
                    continue

                if 0 <= (x + colIndex) < self.cols and 0 <= (y + rowIndex) < self.rows:
                    neighbors += self.grid[y + rowIndex][x + colIndex]

        return neighbors

    def update(self):
        new_grid = [row[:] for row in self.grid]

        for rowIndex in range(self.rows):
            for colIndex in range(self.cols):
                neighbors = self.check_neighbors(colIndex, rowIndex)

                if self.grid[rowIndex][colIndex] == 1 and neighbors < 2:
                    new_grid[rowIndex][colIndex] = 0
                elif self.grid[rowIndex][colIndex] == 1 and (neighbors == 2 or neighbors == 3):
                    new_grid[rowIndex][colIndex] = 1
                elif self.grid[rowIndex][colIndex] == 1 and neighbors > 3:
                    new_grid[rowIndex][colIndex] = 0
                elif self.grid[rowIndex][colIndex] == 0 and neighbors == 3:
                    new_grid[rowIndex][colIndex] = 1

        self.grid = new_grid

    def draw(self, screen):
        for rowIndex in range(self.rows):
            for colIndex in range(self.cols):
                if self.grid[rowIndex][colIndex] == 1:
                    color = (255, 255, 255)
                else:
                    color = (0, 0, 0)
                pygame.draw.rect(screen, color, (colIndex*10, rowIndex*10+50, colIndex*10+10, rowIndex*10+10+50))
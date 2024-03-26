import pygame
import random

from .models import Colors


class Grid:
    def __init__(self, width: int, height: int, cell_size: int = 10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.rows = height // cell_size
        self.cols = width // cell_size
        self.grid = [[random.choice([0, 1]) for col in range(self.cols)] for row in range(self.rows)]
        self.population = 0

    def is_within_grid(self, x: int, y: int) -> bool:
        """Returns True if the given position is within the grid, False otherwise."""
        return 0 <= x < self.cols and 0 <= y < self.rows

    def check_neighbors(self, x: int, y: int) -> int:
        """
        Returns the number of alive neighbors for a given cell.

        Raises a ValueError if the given position is not within the grid.
        """
        # Check if the given position is within the grid
        if not self.is_within_grid(x, y):
            raise ValueError(f"Invalid position: ({x}, {y}) is not within the grid")

        neighbors = 0
        # Iterate over the 3x3 grid around the cell
        for rowOffset in range(-1, 2):
            for colOffset in range(-1, 2):
                # Skip the cell we are checking neighbors for
                if rowOffset == 0 and colOffset == 0:
                    continue

                # Check if the neighbor is within the grid
                if self.is_within_grid(x + colOffset, y + rowOffset):
                    # Add the neighbor value to the neighbors counter (1 for alive, 0 for dead)
                    neighbors += self.grid[y + rowOffset][x + colOffset]

        return neighbors

    def update(self) -> None:
        """Update the grid."""
        new_grid = [row[:] for row in self.grid]

        for rowIndex in range(self.rows):
            for colIndex in range(self.cols):
                neighbors = self.check_neighbors(colIndex, rowIndex)
                cell = self.grid[rowIndex][colIndex]

                if cell == 1 and (neighbors < 2 or neighbors > 3):
                    new_grid[rowIndex][colIndex] = 0
                elif cell == 1 and (neighbors == 2 or neighbors == 3):
                    new_grid[rowIndex][colIndex] = 1
                elif cell == 0 and neighbors == 3:
                    new_grid[rowIndex][colIndex] = 1

        self.grid = new_grid
        self.population = sum([sum(row) for row in self.grid])

    def draw(self, screen: pygame.Surface, x: int, y: int) -> None:
        """Draw the grid on the screen."""

        for rowIndex in range(self.rows):
            for colIndex in range(self.cols):
                if self.grid[rowIndex][colIndex] == 1:
                    color = Colors.WHITE
                else:
                    color = Colors.BLACK
                pygame.draw.rect(
                    screen,
                    color,
                    (
                        x + colIndex * self.cell_size,
                        y + rowIndex * self.cell_size,
                        x + colIndex * self.cell_size + self.cell_size,
                        y + rowIndex * self.cell_size + self.cell_size
                    )
                )
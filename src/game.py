import pygame
from .grid import Grid
from .models import Button, Colors
from .config import Config


class Game:
    def __init__(self) -> None:
        self.grid = Grid(50, 50)

        # State variables
        self.running = True
        self.update = True
        self.mouse_down = False

        # Buttons
        self.pause_button = Button(10, 10, 32, 32, "assets/pause.png")
        self.play_button = Button(10, 10, 32, 32, "assets/play.png")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # Change the state of the cell when the user clicks on it
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_down = True
                x, y = pygame.mouse.get_pos()

                if self.pause_button.is_clicked((x, y)) or self.play_button.is_clicked((x, y)):
                    self.update = not self.update

                if y >= 50:
                    x, y = x // 10, (y - 50) // 10
                    if self.grid.grid[y][x] == 1:
                        self.grid.grid[y][x] = 0
                    else:
                        self.grid.grid[y][x] = 1

            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_down = False

            if event.type == pygame.MOUSEMOTION and self.mouse_down:
                x, y = pygame.mouse.get_pos()

                if y >= 50:
                    x, y = x // 10, (y - 50) // 10
                    self.grid.grid[y][x] = 1

            # Pause or unpause the game when the user presses the space bar
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.update = not self.update

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((500, 550))
        clock = pygame.time.Clock()

        while self.running:
            clock.tick(10)
            self.handle_events()

            screen.fill(Colors.BLACK) # Black background

            if self.update:
                self.pause_button.draw(screen)
            else:
                self.play_button.draw(screen)

            if self.update:
                self.grid.update()

            self.grid.draw(screen)

            pygame.display.update()

        pygame.quit()
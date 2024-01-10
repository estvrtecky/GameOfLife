import pygame
from .grid import Grid
from .models import Button


class Game:
    def __init__(self) -> None:
        self.grid = Grid(50, 50)
        self.running = True
        self.update = True

        # Buttons
        self.pause_button = Button(10, 10, 32, 32, "assets/pause.png")
        self.play_button = Button(10, 10, 32, 32, "assets/play.png")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # Change the state of the cell when the user clicks on it
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if self.pause_button.is_clicked(mouse_pos) or self.play_button.is_clicked(mouse_pos):
                    self.update = not self.update

                x, y = mouse_pos[0] // 10, (mouse_pos[1]-50) // 10
                if self.grid.grid[y][x] == 1:
                    self.grid.grid[y][x] = 0
                else:
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
            screen.fill((0, 0, 0))

            if self.update:
                self.pause_button.draw(screen)
            else:
                self.play_button.draw(screen)

            self.grid.draw(screen)

            if self.update:
                self.grid.update()

            self.handle_events()


            pygame.display.update()

        pygame.quit()
import pygame
from grid import Grid


class Game:
    def __init__(self) -> None:
        self.grid = Grid(50, 50)
        self.running = True
        self.update = True

    def handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # Change the state of the cell when the user clicks on it
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    x, y = mouse_pos[0] // 10, mouse_pos[1] // 10

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
        screen = pygame.display.set_mode((500, 500))
        clock = pygame.time.Clock()

        while self.running:
            clock.tick(10)
            screen.fill((0, 0, 0))
            self.grid.draw(screen)

            if self.update:
                self.grid.update()

            self.handle_events()


            pygame.display.update()

        pygame.quit()
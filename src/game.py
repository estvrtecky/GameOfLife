import pygame
from grid import Grid


class Game:
    def __init__(self) -> None:
        self.grid = Grid(50, 50)

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((500, 500))
        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(10)
            screen.fill((0, 0, 0))
            self.grid.draw(screen)
            self.grid.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()

        pygame.quit()
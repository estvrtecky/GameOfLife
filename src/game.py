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
        update = True

        while running:
            clock.tick(10)
            screen.fill((0, 0, 0))
            self.grid.draw(screen)
            if update:
                self.grid.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    x, y = mouse_pos[0] // 10, mouse_pos[1] // 10
                    self.grid.grid[y][x] = 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        update = not update


            pygame.display.update()

        pygame.quit()
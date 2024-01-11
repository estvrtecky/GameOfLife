import pygame
from .grid import Grid
from .models import Button, Colors
from .config import Config


class Game:
    def __init__(self) -> None:
        # Pygame initialization
        pygame.init()
        pygame.font.init()

        # Game objects
        self.grid = Grid(500, 500, 25)
        self.settings = Config("config.ini")

        # Game settings
        self.name = self.settings.get("game", "name")

        # Display settings
        self.width = self.settings.getint("display", "width")
        self.height = self.settings.getint("display", "height")
        self.fps = self.settings.getint("display", "fps")
        self.font = pygame.font.Font("assets/fonts/PixelifySans-VariableFont_wght.ttf", 30)

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
                    x, y = x // self.grid.cell_size, (y - 50) // self.grid.cell_size
                    if self.grid.grid[y][x] == 1:
                        self.grid.grid[y][x] = 0
                    else:
                        self.grid.grid[y][x] = 1

            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_down = False

            if event.type == pygame.MOUSEMOTION and self.mouse_down:
                x, y = pygame.mouse.get_pos()

                if y >= 50:
                    x, y = x // self.grid.cell_size, (y - 50) // self.grid.cell_size
                    if self.grid.is_within_grid(x, y):
                        self.grid.grid[y][x] = 1

            # Pause or unpause the game when the user presses the space bar
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.update = not self.update

    def run(self):
        screen = pygame.display.set_mode((self.width, self.height))
        clock = pygame.time.Clock()
        pygame.display.set_caption(self.name)

        while self.running:
            clock.tick(self.fps)
            self.handle_events()

            screen.fill(Colors.BLACK) # Black background

            if self.update:
                self.pause_button.draw(screen)
            else:
                self.play_button.draw(screen)

            if self.update:
                self.grid.update()

            self.grid.draw(screen)

            textsurface = self.font.render('Population: ' + str(self.grid.population), False, (255, 255, 255))
            screen.blit(textsurface, (50, 7))

            pygame.display.update()

        pygame.quit()
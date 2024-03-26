import pygame

from .grid import Grid
from .models import Button, Label, Colors
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
        self.speed = self.settings.getint("game", "speed")
        self.update_counter = 0

        # Display settings
        self.width = self.settings.getint("display", "width")
        self.height = self.settings.getint("display", "height")
        self.fps = self.settings.getint("display", "fps")
        self.font = pygame.font.Font("assets/fonts/PixelifySans-VariableFont_wght.ttf", 30)

        # State variables
        self.running = True
        self.menu = True
        self.settings_menu = False
        self.update = False
        self.mouse_down = False

        # Graphics
        self.pause_btn_img = pygame.image.load("assets/pause.png")
        self.play_btn_img = pygame.image.load("assets/play.png")
        self.menu_btn_img = pygame.image.load("assets/menu.png")

        # Labels
        self.population_label = Label(90, 7, text=f"Population: {self.grid.population}", font=self.font)
        self.speed_label = Label(10, 10, text=f"Speed: {self.speed}", font=self.font)

        # Buttons
        self.menu_button = Button(10, 10, 32, 32, self.menu_btn_img)
        self.pause_button = Button(50, 10, 32, 32, self.pause_btn_img)
        self.play_button = Button(50, 10, 32, 32, self.play_btn_img)
        self.start_button = Button(self.width // 2 - 75, self.height // 2 - 85, 150, 50, text="Start", font=self.font)
        self.settings_button = Button(self.width // 2 - 75, self.height // 2 - 25, 150, 50, text="Settings", font=self.font)
        self.quit_button = Button(self.width // 2 - 75, self.height // 2 + 50 - 25 + 10, 150, 50, text="Quit", font=self.font)
        self.back_button = Button(10, self.height - 60, 100, 50, text="Back", font=self.font)
        self.save_button = Button(self.width - 110, self.height - 60, 100, 50, text="Save", font=self.font)
        self.speed_up_button = Button(self.width - 10 - self.speed_label.height, 10, self.speed_label.height, self.speed_label.height, text="+", font=self.font)
        self.speed_down_button = Button(self.speed_up_button.x - 10 - self.speed_label.height, 10, self.speed_label.height, self.speed_label.height, text="-", font=self.font)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # Change the state of the cell when the user clicks on it
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_down = True
                x, y = pygame.mouse.get_pos()

                # Button clicks
                if self.menu:
                    if self.start_button.mouse_over((x, y)):
                        self.menu = False
                        self.update = True
                    elif self.settings_button.mouse_over((x, y)):
                        self.settings_menu = True
                        self.menu = False
                    elif self.quit_button.mouse_over((x, y)):
                        self.running = False
                elif self.settings_menu:
                    if self.back_button.mouse_over((x, y)):
                        self.settings_menu = False
                        self.menu = True
                    elif self.save_button.mouse_over((x, y)):
                        self.settings.set("game", "speed", self.speed)
                    elif self.speed_up_button.mouse_over((x, y)):
                        self.speed += 1 if self.speed < 10 else 0
                        self.speed_label.text = f"Speed: {self.speed}"
                    elif self.speed_down_button.mouse_over((x, y)):
                        self.speed -= 1 if self.speed > 1 else 0
                        self.speed_label.text = f"Speed: {self.speed}"
                else:
                    if self.pause_button.mouse_over((x, y)) or self.play_button.mouse_over((x, y)):
                        self.update = not self.update
                    elif self.menu_button.mouse_over((x, y)):
                        self.menu = True
                        self.update = False

                    # Grid clicks
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

            if event.type == pygame.KEYDOWN:
                # Pause or unpause the game when the user presses the space bar
                if event.key == pygame.K_SPACE and not self.menu:
                    self.update = not self.update
                elif event.key == pygame.K_ESCAPE:
                    if self.settings_menu:
                        self.settings_menu = False
                        self.menu = True

    def draw_main_menu(self, screen):
        screen.fill(Colors.BLACK)
        self.start_button.draw(screen)
        self.settings_button.draw(screen)
        self.quit_button.draw(screen)

    def draw_settings(self, screen):
        screen.fill(Colors.BLACK)
        self.back_button.draw(screen)
        self.save_button.draw(screen)
        self.speed_label.draw(screen)
        self.speed_up_button.draw(screen)
        self.speed_down_button.draw(screen)

    def run(self):
        screen = pygame.display.set_mode((self.width, self.height))
        clock = pygame.time.Clock()
        pygame.display.set_caption(self.name)

        while self.running:
            dt = clock.tick(self.fps)
            self.handle_events()

            if self.menu:
                self.draw_main_menu(screen)
            elif self.settings_menu:
                self.draw_settings(screen)
            else:
                screen.fill(Colors.BLACK)

                self.menu_button.draw(screen)

                if self.update:
                    self.update_counter += 1
                    if self.update_counter >= self.fps // self.speed:
                        self.grid.update()
                        self.update_counter = 0
                    self.pause_button.draw(screen)
                else:
                    self.play_button.draw(screen)

                self.grid.draw(screen, 0, 50)

                self.population_label.text = f"Population: {self.grid.population}"
                self.population_label.draw(screen)

            pygame.display.update()

        pygame.quit()
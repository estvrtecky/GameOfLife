import pygame


class Button:
    def __init__(self, x: int, y: int, width: int, height: int, image: pygame.Surface = None, text: str = "", font: pygame.font.Font = None) -> None:
        # Position and size
        self._x = x
        self._y = y
        self.width = width
        self.height = height

        # Text and font
        self.text = text
        self.font = font or pygame.font.Font(None, 30)

        # Button graphics
        if image:
            # If the image is provided, scale it to the button size
            self.image = pygame.transform.scale(image, (self.width, self.height))
        else:
            # If the image is not provided, create a white surface
            self.image = pygame.Surface((self.width, self.height))
            self.image.fill((255, 255, 255))

        if text:
            # Draw the text on the button
            text_surface = self.font.render(text, True, (0, 0, 0))
            text_rect = text_surface.get_rect()
            text_rect.center = (self.width // 2, self.height // 2)
            self.image.blit(text_surface, text_rect)

        # Button rectangle
        self.button_rect = self.image.get_rect()
        self.button_rect.topleft = (self.x, self.y)

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        self._x = value
        self.button_rect.x = self.x

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        self._y = value
        self.button_rect.y = self.y

    @property
    def center(self) -> tuple:
        return self.button_rect.center

    @center.setter
    def center(self, value: tuple) -> None:
        self.button_rect.center = value

    def draw(self, surface: pygame.Surface) -> None:
        """Draws the button on the surface."""

        surface.blit(self.image, (self.x, self.y))

    def move(self, x: int, y: int) -> None:
        """Moves the button to the given position."""

        self.x = x
        self.y = y

    def mouse_over(self, mouse_pos: tuple) -> bool:
        """Returns True if the mouse is over the button, False otherwise."""

        return self.button_rect.collidepoint(mouse_pos)
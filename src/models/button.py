import pygame
from typing import Any


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Button:
    def __init__(self, **kwargs: Any) -> None:
        """
        Create a button object.

        Keyword arguments:\\
        x (int) -- the x-coordinate of the button (default 0)\\
        y (int) -- the y-coordinate of the button (default 0)\\
        width (int) -- the width of the button (default 100)\\
        height (int) -- the height of the button (default 50)\\
        text (str) -- the text displayed on the button (default "")\\
        text_color (tuple[int, int, int]) -- the color of the text (default (0, 0, 0))\\
        font (pygame.font.Font) -- the font of the text (default None)\\
        background_color (tuple[int, int, int]) -- the color of the button (default (255, 255, 255))\\
        image (pygame.Surface) -- the image of the button (default None)\\
        """
        self._x = kwargs.get("x", 0)
        self._y = kwargs.get("y", 0)
        self.width = kwargs.get("width", 100)
        self.height = kwargs.get("height", 50)
        self._text = kwargs.get("text", "")
        self.text_color = kwargs.get("text_color", BLACK)
        self.font = kwargs.get("font", pygame.font.Font(None, 30))
        self.background_color = kwargs.get("background_color", WHITE)
        self.original_image = kwargs.get("image", None)
        self.image = self.create_image(self.original_image)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        self._x = value
        self.rect.x = self.x

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        self._y = value
        self.rect.y = self.y

    @property
    def center(self) -> tuple[int, int]:
        return self.rect.center

    @center.setter
    def center(self, value: tuple[int, int]) -> None:
        self.rect.center = value
        self.x = self.rect.x
        self.y = self.rect.y

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        self._text = value
        self.image = self.create_image(self.original_image)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def create_image(self, image: pygame.Surface):
        """Create the button's image."""
        if image:
            image = pygame.transform.scale(image.copy(), (self.width, self.height))
        else:
            image = pygame.Surface((self.width, self.height))
            image.fill(self.background_color)
        self.draw_text(image)
        return image

    def draw(self, surface: pygame.Surface) -> None:
        """Draw the button on the surface."""
        surface.blit(self.image, self.rect)

    def draw_text(self, surface: pygame.Surface) -> None:
        """Draw the text on the button."""
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.width // 2, self.height // 2)
        surface.blit(text_surface, text_rect)

    def move(self, dx: int, dy: int) -> None:
        """Moves the button by the given amounts."""
        self.x += dx
        self.y += dy

    def is_mouse_over(self, mouse_pos: tuple) -> bool:
        """Returns True if the mouse is over the button, False otherwise."""
        return self.rect.collidepoint(mouse_pos)
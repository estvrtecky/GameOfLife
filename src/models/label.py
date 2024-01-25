import pygame


class Label:
    def __init__(self, x: int, y: int, text: str, font: pygame.font.Font, color: tuple = (255, 255, 255)) -> None:
        self._x = x
        self._y = y
        self._text = text
        self.font = font
        self.color = color
        self.text_surface = self.font.render(self.text, True, self.color)
        self.rect = self.text_surface.get_rect(topleft=(self.x, self.y))

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
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        self._text = value
        self.text_surface = self.font.render(self.text, True, self.color)
        self.rect = self.text_surface.get_rect(topleft=(self.x, self.y))

    def draw(self, screen: pygame.Surface) -> None:
        """Draws the label on the screen."""
        screen.blit(self.text_surface, self.rect)
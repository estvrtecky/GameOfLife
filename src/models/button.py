import pygame


class Button:
    def __init__(self, x: int, y: int, width: int, height: int, image: pygame.Surface = None) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.button_rect = self.image.get_rect()
        self.button_rect.topleft = (self.x, self.y)

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the button on the screen."""

        screen.blit(self.image, (self.x, self.y))

    def mouse_over(self, mouse_pos: tuple) -> bool:
        """Returns True if the mouse is over the button, False otherwise."""

        return self.button_rect.collidepoint(mouse_pos)
import pygame


class Button:
    def __init__(self, x: int, y: int, width: int, height: int, image: pygame.Surface = None, text: str = "", font: pygame.font.Font = None) -> None:
        # Position and size
        self.x = x
        self.y = y
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

    def draw(self, surface: pygame.Surface) -> None:
        """Draws the button on the surface."""

        surface.blit(self.image, (self.x, self.y))

    def mouse_over(self, mouse_pos: tuple) -> bool:
        """Returns True if the mouse is over the button, False otherwise."""

        return self.button_rect.collidepoint(mouse_pos)
import pygame


class Button:
    def __init__(self, x: int, y: int, width: int, height: int, image_path: str) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load(image_path), (self.width, self.height))
        self.button_rect = self.image.get_rect()
        self.button_rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def is_clicked(self, mouse_pos: tuple) -> bool:
        return self.button_rect.collidepoint(mouse_pos)
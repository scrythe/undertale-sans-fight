import pygame
from functions import scale_image


class Heart(pygame.sprite.Sprite):
    def __init__(self, start_coords):
        super().__init__()
        image = pygame.image.load('sprites/spr_heart.png').convert_alpha()
        self.image = scale_image(image, 1.5)
        self.rect = self.image.get_rect(center=start_coords)
        self.speed = 2

    def move_upwards(self):
        self.rect.y -= self.speed

    def move_right(self):
        self.rect.x += self.speed

    def move_downwards(self):
        self.rect.y += self.speed

    def move_left(self):
        self.rect.x -= self.speed

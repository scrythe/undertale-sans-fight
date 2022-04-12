import enum
import pygame


class Heart(pygame.sprite.Sprite):
    def __init__(self, start_coords):
        super().__init__()
        self.image = pygame.image.load('sprites/spr_heart.png').convert_alpha()
        self.rect = self.image.get_rect(center=start_coords)

    def move_upwards(self):
        self.rect.y -= 1

    def move_right(self):
        self.rect.x += 1

    def move_downwards(self):
        self.rect.y += 1

    def move_left(self):
        self.rect.x -= 1

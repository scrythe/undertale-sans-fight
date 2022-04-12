import pygame
from functions import scale_image


class Heart(pygame.sprite.Sprite):
    def __init__(self, border):
        super().__init__()
        image = pygame.image.load('sprites/spr_heart.png').convert_alpha()
        self.image = scale_image(image, 1.5)
        self.speed = 2
        self.rect = self.image.get_rect(center=border.center)
        self.border = border

    def move_upwards(self):
        self.rect.y -= self.speed
        if self.border.top > self.rect.top:
            self.rect.top = self.border.top

    def move_right(self):
        self.rect.x += self.speed
        if self.border.right < self.rect.right:
            self.rect.right = self.border.right

    def move_downwards(self):
        self.rect.y += self.speed
        if self.border.bottom < self.rect.bottom:
            self.rect.bottom = self.border.bottom

    def move_left(self):
        self.rect.x -= self.speed
        if self.border.left > self.rect.left:
            self.rect.left = self.border.left

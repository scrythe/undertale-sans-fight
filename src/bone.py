import pygame
from utils import get_scaled_image


class Bone(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()
        self.og_surface = get_scaled_image('sprites/spr_s_bonestab_v.png')
        self.image = self.og_surface
        self.rect = self.image.get_rect(midtop=coords)
        self.mask = pygame.mask.from_surface(self.image)
        self.height = 0
        self.height_increasement_speed = 2
        self.attack = False

    def go_upwards_or_downwards(self):
        if self.height <= 80:
            self.rect.y -= self.height_increasement_speed
            self.height += self.height_increasement_speed
            self.image = self.og_surface.subsurface(0, 0, 15, self.height)
        else:
            self.attack = False

    def update(self):
        if self.attack:
            self.go_upwards_or_downwards()

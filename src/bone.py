import pygame
from utils import get_scaled_image
from pygame import Surface, Rect


class Bone(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()
        self.image = get_scaled_image('sprites/spr_s_bonestab_v.png')
        self.rect = self.image.get_rect(center=coords)
        self.mask = pygame.mask.from_surface(self.image)

    def draw_onto_surf(self, screen: Surface, box: Rect):
        offset = self.rect.left - box.left, self.rect.top - box.top
        screen.blit(self.image, offset)

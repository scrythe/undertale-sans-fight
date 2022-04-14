import pygame
from pygame import Rect, Surface
from utils import get_scaled_image


class Bone(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()
        self.image = get_scaled_image('sprites/spr_s_bonestab_v.png')
        self.rect = self.image.get_rect(center=coords)
        self.mask = pygame.mask.from_surface(self.image)


class Bone_Wall:
    def __init__(self, box: Rect):
        self.bone_group = pygame.sprite.Group()
        # self.surface = pygame.Surface((box.width, box.height/2))
        # # self.surface.fill('red')
        # # self.surface.set_alpha(0)
        # self.surface_rect = self.surface.get_rect(midbottom=box.midbottom)
        self.x = box.left
        self.y = box.bottom
        self.amount_bones = 14
        self.steps = (box.right - box.left) / (self.amount_bones - 1)
        for index in range(self.amount_bones):
            bone = Bone((self.x, self.y))
            self.bone_group.add(bone)
            self.x += self.steps

    def draw(self, screen: Surface):
        self.bone_group.draw(screen)

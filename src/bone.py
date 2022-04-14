import pygame
from pygame import Rect, Surface
from utils import get_scaled_image


class Bone(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()
        self.og_surface = get_scaled_image('sprites/spr_s_bonestab_v.png')
        self.image = self.og_surface
        self.rect = self.image.get_rect(midtop=coords)
        self.mask = pygame.mask.from_surface(self.image)
        self.height = 0
        self.height_increasement_speed = 5

    def attack_from_upwards(self):
        if self.height <= 80:
            self.rect.y -= self.height_increasement_speed
            self.height += self.height_increasement_speed
            self.image = self.og_surface.subsurface(0, 0, 15, self.height)

    def update(self):
        self.attack_from_upwards()


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

    def update(self):
        self.bone_group.update()

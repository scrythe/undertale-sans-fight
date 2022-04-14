import pygame
from pygame import Rect, Surface
from bone import Bone


class Bone_Wall:
    def __init__(self, box: Rect):
        self.bone_group = pygame.sprite.Group()
        # self.surface = pygame.Surface((box.width, box.height/2))
        # # self.surface.fill('red')
        # # self.surface.set_alpha(0)
        # self.surface_rect = self.surface.get_rect(midbottom=box.midbottom)
        self.x = box.left
        self.y = box.bottom
        self.attack_status = False
        self.amount_bones = 14
        self.steps = (box.right - box.left) / (self.amount_bones - 1)
        for index in range(self.amount_bones):
            bone = Bone((self.x, self.y))
            self.bone_group.add(bone)
            self.x += self.steps

    def attack(self):
        self.attack_status = True
        for sprite in self.bone_group.sprites():
            sprite.attack = True
            sprite.image = sprite.og_surface.subsurface(0, 0, 15, 0)

    def draw(self, screen: Surface):
        if self.attack_status:
            self.bone_group.draw(screen)

    def update(self):
        self.bone_group.update()

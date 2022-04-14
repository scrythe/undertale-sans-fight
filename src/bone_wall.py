import pygame
from pygame import Rect, Surface
from bone import Bone


class Bone_Wall:
    def __init__(self, box: Rect):
        self.bone_group = pygame.sprite.Group()
        self.surface = pygame.Surface((box.width, box.height))
        # self.surface.fill('red')
        # self.surface.set_alpha(0)
        self.surface_rect = self.surface.get_rect(topleft=box.topleft)
        self.amount_bones = 14
        self.attack_state = False
        steps = (box.right - box.left) / (self.amount_bones - 1)
        # self.surface = sur
        bone_x = box.left
        bone_y = box.bottom
        for index in range(self.amount_bones):
            bone = Bone((bone_x, bone_y))
            self.bone_group.add(bone)
            bone_x += steps

        self.draw_bones()
        # self.surface.fill('red')

    def draw(self, screen: Surface):
        screen.blit(self.surface, self.surface_rect)

    def draw_bones(self):
        self.surface.fill('black')
        for bone in self.bone_group.sprites():
            bone.draw_onto_surf(self.surface, self.surface_rect)
        self.surface.set_colorkey((0, 0, 0))

    def go_upwards(self):
        for bone in self.bone_group.sprites():
            bone.rect.y -= 1

    def attack(self):
        if self.attack_state:
            self.go_upwards()
            self.draw_bones()

    def update(self):
        self.attack()

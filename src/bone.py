import pygame
from utils import get_scaled_image
from pygame import Surface, Rect
from typing import List


class Bone(pygame.sprite.Sprite):
    def __init__(self, coords=(0, 0)):
        super().__init__()
        self.image = get_scaled_image('sprites/spr_s_bonestab_v.png')
        self.rect = self.image.get_rect(topleft=coords)
        self.mask = pygame.mask.from_surface(self.image)

    def get_default_rect(self):
        return self.rect

    def draw_onto_surf(self, screen: Surface, box: Rect):
        offset = self.rect.left - box.left, self.rect.top - box.top
        screen.blit(self.image, offset)

    def get_coords_inside_surf(self, box: Rect):
        offset = self.rect.left - box.left, self.rect.top - box.top
        return offset


class Bone_Group:
    def __init__(self, battle_box: Rect):
        self.bone_group = pygame.sprite.Group()
        # surface with all the bones
        self.battle_box = battle_box
        self.surface = pygame.Surface(
            (self.battle_box.width, self.battle_box.height))
        self.surface.set_colorkey((0, 0, 0))
        self.surface_rect = self.surface.get_rect(
            topleft=self.battle_box.topleft)

    def create_bone_wall(self, amount_bones, width):
        steps = width / (amount_bones - 1)
        default_rect = Bone().get_default_rect()
        default_rect.midtop = (self.battle_box.left, self.battle_box.bottom)
        for index in range(amount_bones):
            bone = Bone((default_rect.x, default_rect.y))
            self.bone_group.add(bone)
            default_rect.x += steps
        self.bone_group_sprites: List[Bone] = self.bone_group.sprites()

    def draw(self, screen: Surface):
        screen.blit(self.surface, self.surface_rect)

    def draw_bones(self):
        self.surface.fill('black')
        for bone in self.bone_group_sprites:
            bone.draw_onto_surf(self.surface, self.surface_rect)
        self.surface.set_colorkey((0, 0, 0))

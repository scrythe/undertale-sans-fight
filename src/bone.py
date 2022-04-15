from venv import create
import pygame
from utils import get_scaled_image
from pygame import Surface, Rect
from typing import List


class Bone(pygame.sprite.Sprite):
    def __init__(self, surface, coords=(0, 0)):
        super().__init__()
        self.image = surface
        self.rect = self.image.get_rect(topleft=coords)
        self.mask = pygame.mask.from_surface(self.image)
        # Create a repositioned rect for drawing onto surface
        self.rect_in_box = self.rect.copy()
        # box: Rect = pygame.Rect((0, 0), (0, 0))
        # self.create_rect_inside_surf(box)

    def get_default_rect(self):
        return self.rect

    def create_rect_inside_surf(self, box: Rect):
        # Repositioned Rectangle inside a Surface
        self.rect_in_box.x = self.rect.left - box.left
        self.rect_in_box.y = self.rect.top - box.top

    def draw_onto_surf(self, screen: Surface):
        screen.blit(self.image, self.rect_in_box)

    def go_upwards(self, amount):
        self.rect.y -= amount
        self.rect_in_box.y -= amount

    def go_right(self, amount):
        self.rect.x += amount
        self.rect_in_box.y += amount

    def go_downwards(self, amount):
        self.rect.y += amount
        self.rect_in_box.y += amount

    def go_left(self, amount):
        self.rect.x -= amount
        self.rect_in_box.x -= amount


class Bone_Stab(Bone):
    def __init__(self, coords=(0, 0)):
        image = get_scaled_image('sprites/spr_s_bonestab_v.png')
        super().__init__(image, coords)


class Bone_Group:
    def __init__(self, battle_box: Rect):
        self.bone_group = pygame.sprite.Group()
        # Surface with all the bones
        self.battle_box = battle_box
        # surface as big as battle box where bones will be drawn onto
        self.surface = pygame.Surface(
            (self.battle_box.width, self.battle_box.height))
        self.surface.set_colorkey((0, 0, 0))
        self.surface_rect = self.surface.get_rect(
            topleft=self.battle_box.topleft)

    def create_bone_wall(self, amount_bones, width):
        steps = width / (amount_bones - 1)
        default_rect = Bone_Stab().get_default_rect()
        default_rect.midtop = (self.battle_box.left, self.battle_box.bottom)
        for index in range(amount_bones):
            bone = Bone_Stab((default_rect.x, default_rect.y))
            bone.create_rect_inside_surf(self.surface_rect)
            self.bone_group.add(bone)
            default_rect.x += steps
        self.bone_group_sprites: List[Bone_Stab] = self.bone_group.sprites()

    def draw(self, screen: Surface):
        screen.blit(self.surface, self.surface_rect)

    def draw_bones(self):
        self.surface.fill('black')
        for bone in self.bone_group_sprites:
            bone.draw_onto_surf(self.surface)
        self.surface.set_colorkey((0, 0, 0))

    def get_distance_from_bottom(self):
        first_bone = self.bone_group_sprites[0]
        distance_from_bottom = self.surface_rect.height - first_bone.rect_in_box.top
        return distance_from_bottom

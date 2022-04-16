import pygame
from utils import get_scaled_image, change_height
from pygame import Surface, Rect
from typing import List


class Bone(pygame.sprite.Sprite):
    def __init__(self, surface, coords=(0, 0)):
        super().__init__()
        self.image = surface
        self.rect = self.image.get_rect(topleft=coords)
        self.mask = pygame.mask.from_surface(self.image)
        # Create a repositioned rect for drawing onto surface
        self.rect_in_box: Rect = self.rect.copy()
        # box: Rect = pygame.Rect((0, 0), (0, 0))
        # self.create_rect_inside_surf(box)

    def get_default_rect(self):
        return self.rect

    def create_rect_inside_surf(self, box: Rect):
        # Repositioned Rectangle inside a Surface
        self.rect_in_box.left = self.rect.left - box.left
        self.rect_in_box.top = self.rect.top - box.top

    def draw_onto_surf(self, screen: Surface):
        screen.blit(self.image, self.rect_in_box)

    def go_upwards(self, amount):
        self.rect.y -= amount
        self.rect_in_box.y -= amount

    def go_right(self, amount):
        self.rect.x += amount
        self.rect_in_box.x += amount

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


class Bone_Bul(Bone):
    def __init__(self, height=100, coords=(0, 0)):
        image = self.combine_bone_parts(height)
        super().__init__(image, coords)

    def combine_bone_parts(self, height):
        bonetop = get_scaled_image('sprites/spr_s_bonebul_top.png')
        bonemiddle = get_scaled_image('sprites/spr_s_bonebul_middle.png')
        bonebottom = get_scaled_image('sprites/spr_s_bonebul_bottom.png')

        bonemiddle_height = height - bonetop.get_height() - bonebottom.get_height()
        bonemiddle = change_height(bonemiddle, bonemiddle_height)

        width = bonemiddle.get_width()
        combined_bone = pygame.Surface((width, height))
        combined_bone.set_colorkey((0, 0, 0))
        combined_bone_rect = combined_bone.get_rect()

        bonetop_rect = bonetop.get_rect(
            midtop=combined_bone_rect.midtop)
        bonemiddle_rect = bonemiddle.get_rect(
            center=combined_bone_rect.center)
        bonebottom_rect = bonebottom.get_rect(
            midbottom=combined_bone_rect.midbottom)

        # put all bones onto combined bone surface
        combined_bone.blit(bonetop, bonetop_rect)
        combined_bone.blit(bonemiddle, bonemiddle_rect)
        combined_bone.blit(bonebottom, bonebottom_rect)

        return combined_bone

    def draw(self, screen: Surface):
        screen.blit(self.image, self.rect)


class Bone_Group:
    def __init__(self, battle_box: Rect):
        # Surface with all the bones
        self.battle_box = battle_box
        # surface as big as battle box where bones will be drawn onto
        self.surface = pygame.Surface(
            (self.battle_box.width, self.battle_box.height))
        self.surface.set_colorkey((0, 0, 0))
        self.surface_rect = self.surface.get_rect(
            topleft=self.battle_box.topleft)
        self.define_bone_group = pygame.sprite.Group()
        self.bone_group_sprites: List[Bone_Stab] = self.define_bone_group.sprites(
        )

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

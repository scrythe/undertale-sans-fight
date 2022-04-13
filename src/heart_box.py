

import pygame
from pygame import Rect, Surface


class Heart_Box:
    def __init__(self, border: Rect):
        self.MAX_HP = 92
        self.max_hp_box = pygame.Surface((112, 30))
        self.max_hp_box.fill('red')
        self.hp_box = pygame.Surface((112, 30))
        self.hp_box.fill('yellow')
        self.max_hp_box_rect = self.max_hp_box.get_rect(
            midtop=(border.centerx, border.bottom+15))
        self.hp_box_rect = self.max_hp_box.get_rect(
            topleft=self.max_hp_box_rect.topleft)

    def damage(self, current_hp):
        hp_percentage = current_hp / self.MAX_HP
        new_size = (112*hp_percentage, 30)
        self.hp_box = pygame.transform.scale(self.hp_box, new_size)

    def draw(self, screen: Surface):
        screen.blit(self.max_hp_box, self.max_hp_box_rect)
        screen.blit(self.hp_box, self.hp_box_rect)

import pygame
from functions import scale_image


class Heart(pygame.sprite.Sprite):
    def __init__(self, box, border):
        super().__init__()
        self.border = box
        image = pygame.image.load('sprites/spr_heart.png').convert_alpha()
        self.image = scale_image(image, 1.5)
        self.speed = 2
        self.rect = self.image.get_rect(center=box.center)
        self.dead = False
        self.create_hp_box(border)

    def create_hp_box(self, border):
        self.MAX_HP = 92
        self.HP = 92
        self.max_hp_box = pygame.Surface((112, 30))
        self.max_hp_box.fill('red')
        self.hp_box = pygame.Surface((112, 30))
        self.hp_box.fill('yellow')
        self.max_hp_box_rect = self.max_hp_box.get_rect(
            midtop=(border.centerx, border.bottom+15))
        self.hp_box_rect = self.max_hp_box.get_rect(
            topleft=self.max_hp_box_rect.topleft)

    def move_upwards(self):
        self.rect.y -= self.speed
        if self.border.top > self.rect.top:
            self.rect.top = self.border.top

    def move_right(self):
        self.rect.x += self.speed
        if self.border.right < self.rect.right:
            self.rect.right = self.border.right

    def move_downwards(self):
        self.rect.y += self.speed
        if self.border.bottom < self.rect.bottom:
            self.rect.bottom = self.border.bottom

    def move_left(self):
        self.rect.x -= self.speed
        if self.border.left > self.rect.left:
            self.rect.left = self.border.left

    def take_damage(self):
        self.HP -= 1
        if self.HP <= 0:
            self.lost()
        else:
            hp_percentage = self.HP / self.MAX_HP
            new_size = (112*hp_percentage, 30)
            self.hp_box = pygame.transform.scale(self.hp_box, new_size)

    def draw_hp(self, screen):
        screen.blit(self.max_hp_box, self.max_hp_box_rect)
        screen.blit(self.hp_box, self.hp_box_rect)

    def lost(self):
        self.dead = True
        print('You died!')
        self.kill()

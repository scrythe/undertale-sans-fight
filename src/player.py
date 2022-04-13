import pygame
from utils import get_heart_img
from pygame import Rect


class Heart():
    def __init__(self, rect: Rect, box: Rect, speed):
        self.rect = rect
        self.box = box
        self.speed = speed

    def move_right(self):
        self.rect.x += self.speed
        if self.box.right < self.rect.right:
            self.rect.right = self.box.right

    def move_left(self):
        self.rect.x -= self.speed
        if self.box.left > self.rect.left:
            self.rect.left = self.box.left

    def inputs(self, keys):
        if keys[pygame.K_d]:
            self.move_right()
        if keys[pygame.K_a]:
            self.move_left()

    def update(self):
        keys = pygame.key.get_pressed()
        self.inputs(keys)


class Red_Heart(Heart):
    def __init__(self, rect: Rect, box: Rect, speed):
        super().__init__(rect, box, speed)
        self.image = get_heart_img('sprites/spr_heart.png')

    def move_upwards(self):
        self.rect.y -= self.speed
        if self.box.top > self.rect.top:
            self.rect.top = self.box.top

    def move_downwards(self):
        self.rect.y += self.speed
        if self.box.bottom < self.rect.bottom:
            self.rect.bottom = self.box.bottom

    def inputs(self, keys):
        super().inputs(keys)
        if keys[pygame.K_w]:
            self.move_upwards()
        if keys[pygame.K_s]:
            self.move_downwards()


class Blue_Heart(Heart):
    def __init__(self, rect: Rect, box: Rect, speed):
        super().__init__(rect, box, speed)
        self.image = get_heart_img('sprites/spr_heartblue.png')
        self.max_jump_height = self.box.bottom - self.box.centery
        self.jump_height = 0
        self.jumping = False

    def jump(self):
        if self.box.bottom <= self.rect.bottom:
            self.jumping = True
            self.jump_height = 0

        if self.jumping:
            self.move_upwards()

    def move_upwards(self):
        if self.max_jump_height >= self.jump_height:
            self.jump_height += self.speed
            self.rect.y -= self.speed
        else:
            self.jumping = False
        if self.box.top > self.rect.top:
            self.rect.top = self.box.top

    def fall_downwards(self):
        self.rect.y += self.speed
        if self.box.bottom < self.rect.bottom:
            self.rect.bottom = self.box.bottom

    def inputs(self, keys):
        super().inputs(keys)
        if keys[pygame.K_w]:
            self.jump()
        else:
            self.jumping = False

    def update(self):
        super().update()
        if not self.jumping:
            self.fall_downwards()


class Player(pygame.sprite.Sprite):
    def __init__(self, box: Rect, border: Rect):
        super().__init__()
        self.box = box
        self.border = border
        self.speed = 2

        self.default_image = get_heart_img('sprites/spr_default_heart.png')
        self.rect = self.default_image.get_rect(center=box.center)
        self.mask = pygame.mask.from_surface(self.default_image)

        self.create_hearts()

    def create_hearts(self):
        self.red_heart = Red_Heart(self.rect, self.box, self.speed)
        self.blue_heart = Blue_Heart(self.rect, self.box, self.speed)
        self.change_heart("red_heart")

    def change_heart(self, heart):
        if heart == "red_heart":
            self.current_heart = self.red_heart
        elif heart == "blue_heart":
            self.current_heart = self.blue_heart
        self.image = self.current_heart.image

    def update(self):
        self.current_heart.update()

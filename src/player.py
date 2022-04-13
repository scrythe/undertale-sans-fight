import pygame
from utils import scale_image


class Heart(pygame.sprite.Sprite):
    def __init__(self, box, border, sprite_file):
        super().__init__()
        self.box = box
        self.border = border
        image = pygame.image.load(f'sprites/{sprite_file}').convert_alpha()
        self.image = scale_image(image, 1.5)
        self.rect = self.image.get_rect(center=box.center)
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 2

        self.dead = False
        self.create_hp_box(self.border)

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

    def move_right(self):
        self.rect.x += self.speed
        if self.box.right < self.rect.right:
            self.rect.right = self.box.right

    def move_left(self):
        self.rect.x -= self.speed
        if self.box.left > self.rect.left:
            self.rect.left = self.box.left

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

    def inputs(self, keys):
        if keys[pygame.K_d]:
            self.move_right()
        if keys[pygame.K_a]:
            self.move_left()

    def update(self):
        keys = pygame.key.get_pressed()
        self.inputs(keys)

    def lost(self):
        self.dead = True
        print('You died!')
        self.kill()


class Read_Heart(Heart):
    def __init__(self, box, border):
        super().__init__(box, border, 'spr_heart.png')

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
    def __init__(self, box, border):
        super().__init__(box, border, 'spr_heartblue.png')
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

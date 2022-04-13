import pygame


class Bone(pygame.sprite.Sprite):
    def __init__(self, box):
        super().__init__()
        self.image = pygame.image.load('sprites/spr_s_bonewall.png')
        self.rect = self.image.get_rect(midbottom=box.midbottom)
        self.mask = pygame.mask.from_surface(self.image)

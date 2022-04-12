import pygame


class Battle_Box:
    def __init__(self, screen_rect):
        self.BATTLE_BOX_BORDER = pygame.Surface((250, 250))
        self.BATTLE_BOX_BORDER.fill("white")
        self.BATTLE_BOX = pygame.Surface((225, 225))
        self.BATTLE_BOX_BORDER_RECT = self.BATTLE_BOX_BORDER.get_rect(
            midtop=screen_rect.center)
        self.BATTLE_BOX_RECT = self.BATTLE_BOX.get_rect(
            center=self.BATTLE_BOX_BORDER_RECT.center)

    def get_box(self):
        return self.BATTLE_BOX_RECT

    def get_border(self):
        return self.BATTLE_BOX_BORDER_RECT

    def draw(self, screen):
        screen.blit(self.BATTLE_BOX_BORDER, self.BATTLE_BOX_BORDER_RECT)
        screen.blit(self.BATTLE_BOX, self.BATTLE_BOX_RECT)

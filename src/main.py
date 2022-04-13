import pygame
from player import Read_Heart, Blue_Heart
from bone import Bone
from battle_box import Battle_Box


class Game:
    TOTAL_WIDTH = 960
    TOTAL_HEIGHT = 720
    FPS = 60

    def __init__(self):
        self.screen = pygame.display.set_mode(
            (self.TOTAL_WIDTH, self.TOTAL_HEIGHT))
        self.screen_rect = self.screen.get_rect()
        self.battle_Box = Battle_Box(self.screen_rect)
        self.heart = Blue_Heart(self.battle_Box.get_box(),
                                self.battle_Box.get_border())
        self.player = pygame.sprite.GroupSingle()
        self.player.add(self.heart)
        self.bone = Bone(self.battle_Box.get_box())
        self.bones_group = pygame.sprite.Group()
        self.bones_group.add(self.bone)

        self.done = False
        self.clock = pygame.time.Clock()

    def run(self):
        # update all sprite groups
        # draw all sprite #groups
        # others such as event stuff
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.FPS)

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

    def update(self):
        # check if heart collides with any groups
        # and also other updates like movement
        self.heart.update()
        if not self.heart.dead and self.collision():
            self.heart.take_damage()

    def draw(self):
        self.battle_Box.draw(self.screen)
        self.player.draw(self.screen)
        self.bones_group.draw(self.screen)
        self.heart.draw_hp(self.screen)

    def collision(self):
        return pygame.sprite.spritecollide(
            self.player.sprite, self.bones_group, False, pygame.sprite.collide_mask)


if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()

import pygame
from player import Player
from bone_stab_wide import Bone_Stab_Wide
from bone_wave import Bone_Wave
from battle_box import Battle_Box
from heart_box import Heart_Box


class Game:
    TOTAL_WIDTH = 960
    TOTAL_HEIGHT = 720
    FPS = 60

    def __init__(self):
        self.screen = pygame.display.set_mode(
            (self.TOTAL_WIDTH, self.TOTAL_HEIGHT))
        self.screen_rect = self.screen.get_rect()
        self.battle_Box = Battle_Box(self.screen_rect)
        self.heart = Player(self.battle_Box.get_box(),
                            self.battle_Box.get_border())
        self.HP = 92
        self.dead = False
        self.heart_box = Heart_Box(self.battle_Box.get_border())
        self.player = pygame.sprite.GroupSingle(self.heart)
        self.player_sprite: Player = self.player.sprite
        self.bone_stab_wide = Bone_Stab_Wide(self.battle_Box.get_box())
        self.bone_wave = Bone_Wave(self.battle_Box.get_box())

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

            # If space key is pressed, than heart is changed / for testing
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                heart_name = self.player_sprite.current_heart.__class__.__name__
                if heart_name == "Blue_Heart":
                    self.player_sprite.change_heart("red_heart")
                elif heart_name == "Red_Heart":
                    self.player_sprite.change_heart("blue_heart")

            # If press key up then bone stab wide attack appears / for testing
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.bone_stab_wide.start_attack()

            # If press key right then bone wave attack appears / for testing
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.bone_wave.start_attack()

    def update(self):
        # check if heart collides with any groups
        # and also other updates like movement
        if not self.dead:
            self.player_sprite.update()
            if self.collision():
                self.take_damage()
        self.bone_stab_wide.update()
        self.bone_wave.update()

    def take_damage(self):
        self.HP -= 1
        if self.HP <= 0:
            self.lost()
        else:
            self.heart_box.damage(self.HP)

    def lost(self):
        self.dead = True
        print('You died!')
        self.player.empty()

    def draw(self):
        self.battle_Box.draw(self.screen)
        self.player.draw(self.screen)
        self.bone_stab_wide.draw(self.screen)
        self.bone_wave.draw(self.screen)
        self.heart_box.draw(self.screen)

    def collision(self):
        bone_stab_hit = self.bone_stab_wide.check_if_hit(self.player_sprite)
        bone_wave_hit = self.bone_wave.check_if_hit(self.player_sprite)
        hit = bone_stab_hit or bone_wave_hit
        return hit


if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()

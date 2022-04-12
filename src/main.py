import pygame
from sys import exit
from Player import Heart
from Battle_Box import Battle_Box
from functions import move

pygame.init()
TOTAL_WIDTH = 960
TOTAL_HEIGHT = 720
SCREEN = pygame.display.set_mode((TOTAL_WIDTH, TOTAL_HEIGHT))
SCREEN_RECT = SCREEN.get_rect()
battle_Box = Battle_Box(SCREEN_RECT)
FPS = 60
clock = pygame.time.Clock()

heart = Heart(battle_Box.get_box(), battle_Box.get_border())
player = pygame.sprite.GroupSingle()
player.add(heart)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    move(keys, heart)
    # press space to get damage for testing
    if keys[pygame.K_SPACE] and not heart.dead:
        heart.take_damage()
        print(heart.HP)
    battle_Box.draw(SCREEN)
    player.draw(SCREEN)
    heart.draw_hp(SCREEN)
    pygame.display.update()

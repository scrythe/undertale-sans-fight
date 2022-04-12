import pygame
from sys import exit
from Player import Heart


def move(keys):
    if keys[pygame.K_w]:
        heart.move_upwards()
    if keys[pygame.K_d]:
        heart.move_right()
    if keys[pygame.K_s]:
        heart.move_downwards()
    if keys[pygame.K_a]:
        heart.move_left()


pygame.init()
TOTAL_WIDTH = 960
TOTAL_HEIGHT = 720
SCREEN = pygame.display.set_mode((TOTAL_WIDTH, TOTAL_HEIGHT))
SCREEN_RECT = SCREEN.get_rect()
BATTLE_BOX_BORDER = pygame.Surface((250, 250))
BATTLE_BOX_BORDER.fill("white")
BATTLE_BOX = pygame.Surface((225, 225))
BATTLE_BOX_BORDER_RECT = BATTLE_BOX_BORDER.get_rect(
    midtop=SCREEN_RECT.center)
BATTLE_BOX_RECT = BATTLE_BOX.get_rect(
    center=BATTLE_BOX_BORDER_RECT.center)
FPS = 60
clock = pygame.time.Clock()

heart = Heart(BATTLE_BOX_RECT.center)
player = pygame.sprite.GroupSingle()
player.add(heart)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    move(keys)

    SCREEN.blit(BATTLE_BOX_BORDER, BATTLE_BOX_BORDER_RECT)
    SCREEN.blit(BATTLE_BOX, BATTLE_BOX_RECT)
    player.draw(SCREEN)
    pygame.display.update()

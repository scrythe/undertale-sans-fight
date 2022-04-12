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
TOTAL_WIDTH = 640
TOTAL_HEIGHT = 480
SCREEN = pygame.display.set_mode((TOTAL_WIDTH, TOTAL_HEIGHT))
FPS = 60
clock = pygame.time.Clock()

heart = Heart((TOTAL_WIDTH / 2, TOTAL_HEIGHT / 2))
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

    player.draw(SCREEN)
    pygame.display.update()

import pygame


def move(keys, object):
    if keys[pygame.K_w]:
        object.move_upwards()
    if keys[pygame.K_d]:
        object.move_right()
    if keys[pygame.K_s]:
        object.move_downwards()
    if keys[pygame.K_a]:
        object.move_left()


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)

import pygame
from pygame import Surface


def scale_image(img: Surface, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def change_height(img: Surface, new_height):
    size = round(img.get_width()), round(new_height)
    return pygame.transform.scale(img, size)


def get_scaled_image(img_path):
    image = pygame.image.load(img_path).convert_alpha()
    return scale_image(image, 1.5)

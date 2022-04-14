import pygame


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def get_scaled_image(img_path):
    image = pygame.image.load(img_path).convert_alpha()
    return scale_image(image, 1.5)

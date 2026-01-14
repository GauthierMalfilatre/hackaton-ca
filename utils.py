##
## HACKATON PROJECT, 2026
## CAVA
## File description:
## Utils
##
import pygame

def load_and_resize(name: str, x: int, y: int) -> pygame.image:
    """ Load an image and resize it """
    return pygame.transform.scale(pygame.image.load(name), (x, y))

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

def write_text(text: str, pos: tuple[int, int], screen, font, color: str = "#ffffff") -> None:
    """ Write a text on the screen """
    txt = font.render(text, True, color)
    screen.blit(txt, pos)

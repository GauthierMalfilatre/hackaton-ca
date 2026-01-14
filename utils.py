##
## HACKATON PROJECT, 2026
## CAVA
## File description:
## Utils
##
import pygame
import Block

pygame.init()

bFont = pygame.font.SysFont('Arial', 50, bold=True)
sFont = pygame.font.SysFont('Arial', 25, bold=True)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("CAVA - Hackaton CA")

def load_and_resize(name: str, x: int, y: int) -> pygame.image:
    """ Load an image and resize it """
    return pygame.transform.scale(pygame.image.load(name), (x, y))

def write_text(text: str, pos: tuple[int, int], screen, font, color: str = "#ffffff") -> None:
    """ Write a text on the screen """
    txt = font.render(text, True, color)
    screen.blit(txt, pos)

def get_nearest_machine(blocks: list[list[list]], ref_pos: tuple[int, int]) -> tuple:
    """ Get nearest machine """
    nd = None
    nm = None
    for line in blocks:
        for pile in line:
            for block in pile:
                if isinstance(block, Block.Machine):
                    distance = get_squared_norm(*block.getOrigin(), *ref_pos)
                    if nd == None or distance < nd:
                        nd = distance
                        nm = block
    return nm, nd

def get_squared_norm(x1: int, y1: int, x2: int, y2: int) -> float:
    """ Get the norm but not with sqrt """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2)

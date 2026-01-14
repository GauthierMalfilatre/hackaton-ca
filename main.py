##
## HACKATON PROJECT, 2026
## CAVA
## File description:
## Game made for hackaton-ca
##
import pygame
import mapParser
import utils
import Block
from Player import Player

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CAVA - Hackaton CA")

images: dict = {
    "player" : utils.load_and_resize("assets/ca_paille_spritesheet.png", 128 * 12, 128),
    "parquet": utils.load_and_resize("assets/parquet.png", 50, 75),
}

MAP = mapParser.parse_map("map_demo.camp", images)
FPS = 60

clock = pygame.time.Clock()

player: Player = Player(images["player"])

def handle_keys(keys: list, dt: float) -> None:
    """ Handle key that are pressed """
    player.move(keys, dt, MAP)

def global_render() -> None:
    """ Render all. """
    for line in MAP:
        for pile in line:
            for block in pile:
                block.render(screen)
    player.render(screen)

def game(debug: bool) -> None:
    """ Main function for CAVA """
    is_running: bool = True
    dt = 0.0
    screen.fill("#323232")

    while is_running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        handle_keys(keys, dt)
        global_render()
        pygame.display.flip()
        dt = clock.tick(FPS) / 1000.0

if __name__ == "__main__":
    print("Welcome to the demo of CAVA")
    game(True)

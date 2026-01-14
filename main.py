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
import random

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CAVA - Hackaton CA")

images: dict = {
    "player" : utils.load_and_resize("assets/ca_paille_spritesheet.png", 128 * 12, 128),
    "parquet": utils.load_and_resize("assets/parquet.png", 50, 75),
    "brique" : utils.load_and_resize("assets/brique.png", 50, 75),
    "bs"     : utils.load_and_resize("assets/bst4.png", 50, 75),
}

musique = pygame.mixer.music.load("assets/banque_1.mp3")

MAP = mapParser.parse_map("map_demo.camp", images)
FPS = 60

clock = pygame.time.Clock()
bFont = pygame.font.SysFont('Arial', 50, bold=True)
sFont = pygame.font.SysFont('Arial', 25, bold=True)

player: Player = Player(images["player"], SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

def handle_keys(keys: list, dt: float) -> None:
    """ Handle key that are pressed """
    player.move(keys, dt, MAP)
    return not keys[pygame.K_ESCAPE]

def global_update(dt: float) -> None:
    """ Update all """
    for y, line in enumerate(MAP):
        for pile in line:
            for block in pile:
                block.update(dt)

def global_render(*, p_render: bool = True, b_rumble: bool = False) -> None:
    """ Render all. """
    screen.fill("#020202")
    player_pos = player.getPosition()

    for y, line in enumerate(MAP):
        for pile in line:
            if b_rumble:
                r = random.randint(-10, 0) / 10
                [block.rumble(r) for block in pile]
            [block.render(screen) for block in pile]
            if (p_render and ((player_pos[1] + 96) // 50) == y ):
                player.render(screen)

def menu() -> None:
    """ Menu """
    is_running: bool  = True
    dt        : float = 0.0

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            is_running = False
        global_update(dt)
        
        # Menu specific render
        global_render(p_render=False, b_rumble=True)
        utils.write_text("CAVA - The Heritage", (SCREEN_WIDTH // 2 - 200, 100), screen, bFont)
        utils.write_text("Hackaton CA DEMO", (SCREEN_WIDTH // 2 - 200, 150), screen, sFont)
        # utils.write_text("A game made by:", (SCREEN_WIDTH // 2 - 100, 200), screen, sFont)
        # utils.write_text("Gauthier, Celian, Victor,", (SCREEN_WIDTH // 2 - 150, 240), screen, sFont)
        # utils.write_text("Celeste, Elouan, Calista", (SCREEN_WIDTH // 2 - 150, 280), screen, sFont)
        utils.write_text("Please press [Enter]", (SCREEN_WIDTH // 2 - 100, 250), screen, sFont)

        pygame.display.flip()
        dt = clock.tick(FPS) / 1000.0

def game(debug: bool) -> None:
    """ Main function for CAVA """
    is_running: bool  = True
    dt        : float = 0.0

    while is_running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        is_running = handle_keys(keys, dt)
        global_update(dt)
        global_render()
        pygame.display.flip()
        dt = clock.tick(FPS) / 1000.0

if __name__ == "__main__":
    print("Welcome to the demo of CAVA")
    is_running: bool = True
    pygame.mixer.music.play(-1)
    while is_running:
        menu()
        game(True)

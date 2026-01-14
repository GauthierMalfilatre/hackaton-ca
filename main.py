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

images: dict = {
    "player"  : utils.load_and_resize("assets/ca_paille_spritesheet.png", 128 * 12, 128),
    "parquet" : utils.load_and_resize("assets/parquet.png", 50, 75),
    "brique"  : utils.load_and_resize("assets/brique.png", 50, 75),
    "bs"      : utils.load_and_resize("assets/bst4.png", 50, 75),
    "bling"   : utils.load_and_resize("assets/bling_machine.png", 50, 75),
    "livreta" : utils.load_and_resize("assets/livret_a.png", 50, 75),
    "tapis"   : utils.load_and_resize("assets/tapis_rouge.png", 50, 75),
    "plante"  : utils.load_and_resize("assets/plante.png", 50, 75),
    "chaise"  : utils.load_and_resize("assets/chaise.png", 50, 75),
    "table"   : utils.load_and_resize("assets/table.png", 50, 75),
    "tabouret": utils.load_and_resize("assets/tabouret.png", 50, 75),
    "etf"     : utils.load_and_resize("assets/stonks.png", 50, 75),
    "interetc": utils.load_and_resize("assets/interets_composes.png", 50, 75),
    "coffre_fort": utils.load_and_resize("assets/coffre_fort.png", 50, 75),
    "coffre": utils.load_and_resize("assets/money.png", 50, 75),
    "baril": utils.load_and_resize("assets/baril.png", 50, 75),
}

musique = pygame.mixer.music.load("assets/banque_1.mp3")

MAP = mapParser.parse_map("map_demo.camp", images)
FPS = 60

clock = pygame.time.Clock()

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
    utils.screen.fill("#020202")
    player_pos = player.getPosition()
    for y, line in enumerate(MAP):
        for pile in line:
            if b_rumble:
                r = random.randint(-10, 0) / 10
                [block.rumble(r) for block in pile]
            [block.render(utils.screen) for block in pile]
            if (p_render and ((player_pos[1] + 96) // 50) == y):
                player.render(utils.screen)

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
        utils.write_text("CAVA - The Heritage", (SCREEN_WIDTH // 2 - 200, 100), utils.screen, utils.bFont)
        utils.write_text("Hackaton CA DEMO", (SCREEN_WIDTH // 2 - 200, 150), utils.screen, utils.sFont)
        # utils.write_text("A game made by:", (SCREEN_WIDTH // 2 - 100, 200), screen, utils.sFont)
        # utils.write_text("Gauthier, Celian, Victor,", (SCREEN_WIDTH // 2 - 150, 240), screen, utils.sFont)
        # utils.write_text("Celeste, Elouan, Calista", (SCREEN_WIDTH // 2 - 150, 280), screen, utils.sFont)
        utils.write_text("Please press [Enter]", (SCREEN_WIDTH // 2 - 100, 250), utils.screen, utils.sFont)

        pygame.display.flip()
        dt = clock.tick(FPS) / 1000.0

def game(debug: bool) -> None:
    """ Main function for CAVA """
    is_running: bool  = True
    dt        : float = 0.0
    utils.start_all_machines(MAP)
    while is_running:
        keys = pygame.key.get_pressed()
        utils.presses_update()
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
        utils.stop_all_machines(MAP)
        menu()
        player.giveCoins(10000)
        game(True)

##
## HACKATON PROJECT, 2026
## GAME_CA
## File description:
## Game made for hackaton-ca
##
import pygame
import mapParser
import Block

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

MAP = mapParser.parse_map("map_demo.camp")
print(MAP)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

def handle_keys(keys: list) -> None:
    """ Handle key that are pressed """
    pass

def global_render() -> None:
    """ Render all. """
    for line in MAP:
        for block in line:
            block.render(screen)

def game(debug: bool) -> None:
    """ Main function for GAME_CA """
    is_running: bool = True

    screen.fill("#323232")
    while is_running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        handle_keys(keys)
        global_render()
        pygame.display.flip()

if __name__ == "__main__":
    print("Welcome to the demo of GAME_CA")
    game(True)

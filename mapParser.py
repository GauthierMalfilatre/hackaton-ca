##
## HACKATON PROJECT, 2026
## GAME_CA
## File description:
## Game made for hackaton-ca
##
import Block

def handle_char(char: str, cmap: list[Block.Block], x: int, y: int) -> None:
    """ Handle char -> find the good Block """
    match char:
        case "#":
            cmap.append(Block.Ground(x, y))
        case _:
            pass

def parse_map(filename: str) -> list:
    """ Parse the map """
    cmap : list[list[Block.Block]] = []
    lines: list[str]               = []

    with open(filename, "r") as f:
        lines = [i.replace("\n","") for i in f.readlines()]
    for y, line in enumerate(lines):
        cmap.append([])
        for x, char in enumerate(line):
            handle_char(char, cmap[-1], x, y)
    return cmap

if __name__ == "__main__":
    print("This module shouldn't be run as if, exiting.")
    exit(0)

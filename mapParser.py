##
## HACKATON PROJECT, 2026
## CAVA
## File description:
## Game made for hackaton-ca
##
import Block

def handle_char(char: str, cmap: list[Block.Block], x: int, y: int, images: dict) -> None:
    """ Handle char -> find the good Block """
    # A ground should be anywhere ig
    cmap.append([Block.Ground(x, y, images["parquet"]), ])
    match char:
        case "1":
            cmap[-1].append(Block.Ground(x, y, images["brique"], 1))
        case "2":
            cmap[-1].append(Block.Ground(x, y, images["brique"], 2))
        case _:
            pass

def parse_map(filename: str, images: dict) -> list:
    """ Parse the map """
    cmap : list[list[Block.Block]] = []
    lines: list[str]               = []

    with open(filename, "r") as f:
        lines = [i.replace("\n","") for i in f.readlines()]
    for y, line in enumerate(lines):
        cmap.append([])
        for x, char in enumerate(line):
            handle_char(char, cmap[-1], x, y, images)
    return cmap

if __name__ == "__main__":
    print("This module shouldn't be run as if, exiting.")
    exit(84)

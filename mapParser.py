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
            cmap[-1].append(Block.Ground(x, y, images["brique"], 1))
            cmap[-1].append(Block.Ground(x, y, images["brique"], 2))
            cmap[-1].append(Block.Ground(x, y, images["brique"], 3))
        case ".":
            cmap[-1][0] = Block.Ground(x, y, images["tapis"], 0)
        case _:
            pass

def handle_teapot(command: str, cmap: list, images: dict) -> None:
    """ Handle add teapot """
    x, y = int(command[1]), int(command[2])
    match command[0]:
        case "BM":
            cmap[y][x].append(Block.BlingMachine(x, y, images["bling"], len(cmap[y][x])))
        case "LA":
            cmap[y][x].append(Block.LivretA(x, y, images["livreta"], len(cmap[y][x])))
        case "CE":
            cmap[y][x].append(Block.Teapot(x, y, images["chaise"], len(cmap[y][x])))
        case "TA":
            cmap[y][x].append(Block.Teapot(x, y, images["table"], len(cmap[y][x])))
        case "TB":
            cmap[y][x].append(Block.Teapot(x, y, images["tabouret"], len(cmap[y][x])))
        case "PL":
            cmap[y][x].append(Block.Teapot(x, y, images["plante"], len(cmap[y][x])))
        case "CF":
            cmap[y][x].append(Block.Machine(x, y, images["coffre_fort"], len(cmap[y][x])))
        case "ETF":
            cmap[y][x].append(Block.Machine(x, y, images["etf"], len(cmap[y][x])))
        case "BR":
            cmap[y][x].append(Block.Teapot(x, y, images["baril"], len(cmap[y][x])))
        case "IC":
            cmap[y][x].append(Block.Machine(x, y, images["interetc"], len(cmap[y][x])))
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
        if line.startswith("AT"):
            handle_teapot(line.split()[1:], cmap, images)
        else:
            for x, char in enumerate(line):
                handle_char(char, cmap[-1], x, y, images)
    return cmap

if __name__ == "__main__":
    print("This module shouldn't be run as if, exiting.")
    exit(84)

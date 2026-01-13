##
## HACKATON PROJECT, 2026
## GAME_CA
## File description:
## Game made for hackaton-ca
##
import pygame

class Block:
    def __init__(self, x: int, y: int, color: str = "#000000") -> "Block":
        """ Initialisation of class Block """
        self.__isDirty : bool            = True
        self.__size    : tuple[int, int] = (100, 100)
        self.__position: tuple[int, int] = (x * self.__size[0], y * self.__size[1])
        self.__color   : tuple[int]      = color

    def getSize(self) -> tuple[int, int]:
        """ Get the size of the Block """
        return self.__size
    
    def getPosition(self) -> tuple[int, int]:
        """ Get the position of the Block """
        return self.__position

    def render(self, screen) -> "Block":
        """ Render method for class block """
        if (not self.__isDirty):
            return
        print(self.__color)
        pygame.draw.rect(screen, self.__color, (*self.__position, *self.__size))
        self.__isDirty = False

class Ground(Block):
    def __init__(self, x, y) -> "Ground":
        """ Initialisation of class Ground """
        super().__init__(x, y, "#6F4E37")

if __name__ == "__main__":
    print("This module shouldn't be run as if, exiting.")
    exit(0)

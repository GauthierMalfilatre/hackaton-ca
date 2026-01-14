##
## HACKATON PROJECT, 2026
## CAVA
## File description:
## Block class'
##
import pygame

class Block:
    def __init__(self, x: int, y: int, sprite, color: str = "#000000", z: int = 0) -> "Block":
        """ Initialisation of class Block """
        self.__isDirty : bool            = True
        self.__size    : tuple[int, int] = (50, 50)
        self.__position: tuple[int, int] = (x * self.__size[0], y * self.__size[1])
        self.__color   : tuple[int]      = color
        self.__z       : int             = z
        self.__sprite                    = sprite
        self.__name    : str             = "Block"
        self.__rumbling: float           = 0
        self.__tRumbling: float           = 0

    def __str__(self) -> str:
        """ Get the name of the block """
        return self.__name

    def rumble(self, intensity: float = -0.1, *, force: bool = False) -> "Block":
        """ Rumble the block """
        if self.__rumbling == 0 or force:
            self.__tRumbling = intensity
        return self

    def setName(self, newname: str) -> "Block":
        """ Set the name of the block """
        self.__name = newname
        return self

    def getSize(self) -> tuple[int, int]:
        """ Get the size of the Block """
        return self.__size
    
    def getPosition(self) -> tuple[int, int]:
        """ Get the position of the Block """
        return self.__position        

    def getZIndex(self) -> int:
        """ Return the z index of the Block """
        return self.__z

    def getColor(self) -> str:
        """ Return the color of the Block """
        return self.__color

    def setColor(self, color: str) -> "Block":
        """ Set the color of the block """
        self.__color = color
        return self

    def markAsDirty(self) -> "Block":
        """ Mark the Block as dirty """
        self.__isDirty = True
        return self

    def __handle_rumbling_regression(self, dt) -> "Block":
        """ Handle the rumbling of the Block """
        if self.__tRumbling < 0:
            self.__rumbling -= 1 * dt
            if self.__rumbling <= self.__tRumbling:
                self.__tRumbling = 0
        if self.__rumbling < 0 and self.__tRumbling == 0:
            self.__rumbling += 1 * dt
            if self.__rumbling > 0:
                self.__rumbling = 0

    def update(self, dt: float) -> "Block":
        """ Update the block """
        self.__handle_rumbling_regression(dt)

    def render(self, screen) -> "Block":
        """ Render method for class block """
        if (not self.__isDirty):
            pass
        # pygame.draw.rect(screen, self.__color, (self.__position[0], self.__position[1] + ((self.__z + self.__rumbling) * self.__size[1] / 2), *self.__size), 1)
        screen.blit(self.__sprite, (self.__position[0], self.__position[1] - ((self.__z + self.__rumbling) * self.__size[1] / 2)))
        self.__isDirty = False

class Ground(Block):
    def __init__(self, x: int, y: int, sprite, z: int = 0) -> "Ground":
        """ Initialisation of class Ground """
        super().__init__(x, y, sprite, "#6F4E37", z)
        self.setName("Ground level %d"%z)

if __name__ == "__main__":
    print("This module shouldn't be run as if, exiting.")
    exit(84)

class Teapot(Block):
    def __init__(self, x: int, y: int, sprite, z: int = 0) -> "Teapot":
        """ Initialisation of class teapot """
        super().__init__(x, y, sprite, "#000000", z + 0.5)
        self.setName("Teapot goes brrrr")

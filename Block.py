##
## HACKATON PROJECT, 2026
## CAVA
## File description:
## Block class'
##
import utils

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
    
    def getOrigin(self) -> tuple[int, int]:
        """ Get the center of the block """
        return (self.__position[0] + self.__size[0] // 2, self.__position[1] + self.__size[1] // 2)

    def getPosition(self) -> tuple[int, int]:
        """ Get the position of the Block """
        return self.__position

    def getZIndex(self) -> int:
        """ Return the z index of the Block """
        return self.__z

    def getRumbling(self) -> int:
        """ Fuck all """
        return self.__rumbling

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
        super().__init__(x, y, sprite, "#000000", z)
        self.setName("Teapot goes brrrr")

class Machine(Block):
    def __init__(self, x: int, y: int, sprite, z: int = 0) -> "BlingMachine":
        """ Initialisation of class BlingMachine """
        super().__init__(x, y, sprite, "#000000", z)
        self.__start: bool = False
        self.__e    : bool = False
        self.__first: bool = False

    def start(self) -> "Machine":
        """ Start the machine """
        self.__start = True        
        return self

    def stop(self) -> "Machine":
        """ Start the machine """
        self.__start = False
        return self

    def isStart(self) -> bool:
        """ Return if the machine is started """
        return self.__start

    def activate_e(self) -> "Machine":
        """ Activate e """
        self.__e = True

    def desactivate_e(self) -> "Machine":
        """ Desactivate e """
        self.__e = False

    def isE(self) -> "Machine":
        """ Return is E """
        return self.__e

    def interact(self, player) -> "Machine":
        """ Fuck victor jost """
        return self

    def help(self, blocks: list[list[list[Block]]], lines: list[str]) -> "Machine":
        """ Show help for machine based on given lines """                
        for n, i in enumerate(lines):
            utils.write_text(i, ((800 - len(i) * 50) // 2, 200 + n * 75), utils.screen, utils.bFont,"#ffffff")

    def render(self, screen) -> "Machine":
        super().render(screen)
        if self.isE():
            x, y = self.getPosition()
            utils.write_text("E", (x + 10, y - 20), screen, utils.bFont, "#ffffff")
        self.desactivate_e()

class BlingMachine(Machine):
    def __init__(self, x: int, y: int, sprite, z: int = 0) -> "BlingMachine":
        """ Initialisation of class BlingMachine """
        super().__init__(x, y, sprite, z)
        self.setName("bling machine")
        self.__coins: int   = 0
        self.__cps  : float = 2

    def interact(self, player) -> int:
        """ Interact with the bling machine """
        player.giveCoins(self.__coins)
        old_coins = self.__coins
        self.__coins = 0
        return old_coins

    def help(self, blocks: list[list[list[Block]]]) -> None:
        """ Fuck it """
        super().help(blocks, ["LA CAISSE GENERE DE L'ARGENT A INTERVAL REGULIER", "BOMBOKLAT"])

    def update(self, dt) -> "BlingMachine":
        """ Update the bling machine """
        super().update(dt)
        if self.isStart():
            self.__coins += self.__cps * dt
        return self

    def render(self, screen) -> "BlingMachine":
        """ Render for bling machine """
        super().render(screen)
        if self.isStart():
            x, y = self.getPosition()
            utils.write_text("%d"%self.__coins, (x, y - (self.getZIndex() + self.getRumbling()) * self.getSize()[1] / 2), screen, utils.sFont, "#ffff00")
        return self

##
## HACKATON PROJECT, 2026
## CAVA
## File description:
## Block class'
##
import utils
import pygame
import random

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
        self.__sound       = None

    def setSound(self, sound) -> "Machine":
        """ Set the sound of the machine """
        self.__sound = sound
        self.__sound.set_volume(1.0)
        return self

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

    def depositAll(self, player) -> "Machine":
        """ Deposit all player money """
        return self

    def takeAll(self, player) -> "Machine":
        """ Deposit all player money """
        return self

    def interact(self, player = None) -> "Machine":
        """ Fuck victor jost """
        if self.__sound != None:
            self.__sound.play()
        return self

    def help(self, blocks: list[list[list[Block]]], lines: list[str] = []) -> "Machine":
        """ Show help for machine based on given lines """
        dt: float = 0
        clock     = pygame.time.Clock()
        utils.stop_all_machines(blocks)
        while 1:
            utils.screen.fill("#000000")
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            if keys[pygame.K_RETURN] or keys[pygame.K_SPACE] or keys[pygame.K_ESCAPE]:
                break
            for line in blocks:
                for pile in line:
                    r = random.randint(-10, 0) / 10
                    for block in pile:
                        block.rumble(r)
                        block.update(dt)
                        block.render(utils.screen)
            for n, i in enumerate(lines):                            
                utils.write_text(i, ((800 - len(i) * 12.5) // 2, 100 + n * 50), utils.screen, utils.sFont,"#ffffff")
            pygame.display.flip()
            dt = clock.tick(60) / 1000
        utils.start_all_machines(blocks)

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
        self.setSound(pygame.mixer.Sound("assets/bling.mp3"))
        self.__coins: int   = 0
        self.__cps  : float = 1

    def interact(self, player) -> int:
        """ Interact with the bling machine """
        super().interact()
        player.giveCoins(self.__coins)
        old_coins = self.__coins
        self.__coins = 0
        return old_coins

    def help(self, blocks: list[list[list[Block]]]) -> None:
        """ Fuck it """
        super().help(blocks, ["CECI EST VOTRE CAISSE", "TOUTE LES SECONDES, ELLE GENERE 1 DOLLAR", "VOUS POUVEZ LES RECOLTER EN APPUYANT SUR [E]"])

    def update(self, dt) -> "BlingMachine":
        """ Update the bling machine """
        super().update(dt)
        if self.isStart():
            self.__coins += self.__cps * dt
        return self

    def howMuch(self) -> int:
        """ Return how many coins """
        # Les interets sont epargnés on va dire
        return self.__coins

    def render(self, screen) -> "BlingMachine":
        """ Render for bling machine """
        super().render(screen)
        if self.isStart():
            x, y = self.getPosition()
            utils.write_text("%d"%self.__coins, (x, y - (self.getZIndex() + self.getRumbling()) * self.getSize()[1] / 2), screen, utils.sFont, "#ffff00")
        return self

class LivretA(Machine):
    def __init__(self, x: int, y: int, sprite, z: int = 0) -> "LivretA":
        """ Initialisation of class BlingMachine """
        super().__init__(x, y, sprite, z)
        self.setName("livret a")
        self.__deposit : int   = 0
        self.__taux    : float = 0.03
        self.__interest: float = 0
        self.__timer   : float = 0
        self.__max     : float = 22950
        self.__min     : float = 20
        self.__player          = None

    def depositAll(self, player) -> "LivretA":
        """ Deposit all player money """
        self.__deposit += player.takeCoins(self.__max - self.__deposit)
        return self

    def takeAll(self, player) -> "LivretA":
        """ Deposit all player money """
        player.giveCoins(self.__deposit + self.__interest)
        self.__deposit = 0
        self.__interest = 0
        return self


    def interact(self, player) -> "LivretA":
        """ Interact with the bling machine """
        super().interact()
        self.__player = player
        if self.__deposit == 0 and player.nCoins() >= self.__min:
            self.__deposit = player.takeCoins(self.__max)
        else:
            player.giveCoins(self.__deposit + self.__interest)
            self.__deposit = 0
            self.__interest = 0
        return self

    def help(self, blocks: list[list[list[Block]]]) -> None:
        """ Fuck it """
        super().help(blocks, ["CECI EST VOTRE LIVRET A", "PLACEZ DE L'ARGENT DEDANS REGULIEREMENT", "POUR GENERER DES INTERETS", "LES INTERETS SONT AJOUTES TOUTES LES MINUTES", "A VOTRE COMPTE"])

    def update(self, dt) -> "LivretA":
        """ Update the bling machine """
        super().update(dt)
        if self.isStart():
            self.__interest += self.__deposit * (self.__taux / 60 * dt)
            self.__timer += dt
            if self.__timer > 60:
                self.__timer = 0
                if self.__player != None:
                    self.__player.giveCoins(self.__interest)
                self.__interest = 0
        return self

    def howMuch(self) -> int:
        """ Return how many coins """
        # Les interets sont epargnés on va dire
        return self.__deposit

    def render(self, screen) -> "LivretA":
        """ Render for bling machine """
        super().render(screen)
        if self.isStart():
             x, y = self.getPosition()
             utils.write_text("%d"%(self.__deposit + self.__interest), (x, y - (self.getZIndex() + self.getRumbling()) * self.getSize()[1] / 2), screen, utils.sFont, "#ffff00")
        return self

class Etf(Machine):
    def __init__(self, x: int, y: int, sprite, z: int = 0) -> "Etf":
        """ Initialisation of class BlingMachine """
        super().__init__(x, y, sprite, z)
        self.setName("etf")
        self.__deposit  : int   = 0
        self.__timer    : float = 0
        self.__max      : float = 1_000_000
        self.__min      : float = 10_000
        self.__variation: float = 0
        self.__volatile         = 0.05

    def depositAll(self, player) -> "Etf":
        """ Deposit all player money """
        self.__deposit += player.takeCoins(self.__max - self.__deposit)
        return self

    def takeAll(self, player) -> "Etf":
        """ Deposit all player money """
        player.giveCoins(self.__deposit)
        self.__deposit = 0
        return self

    def interact(self, player) -> "Etf":
        """ Interact with the bling machine """
        super().interact()
        if self.__deposit == 0 and player.nCoins() >= self.__min:
            self.__deposit = player.takeCoins(self.__max)
        else:
            player.giveCoins(self.__deposit)
            self.__deposit = 0
        return self

    def help(self, blocks: list[list[list[Block]]]) -> None:
        """ Fuck it """
        super().help(blocks, ["CECI EST VOTRE PANIER D'ETF", "PLACEZ DE L'ARGENT ET RETIREZ LE QUAND LE PROFIT", "EST LE PLUS ELEVE !"])

    def update(self, dt) -> "Etf":
        """ Update the bling machine """
        super().update(dt)
        if self.isStart():
            self.__timer += dt
            if self.__timer > 5:
                self.__timer = 0
                self.__variation = random.uniform(-self.__volatile, self.__volatile + 0.005)
                self.__deposit *= (1 + self.__variation)
        return self

    def howMuch(self) -> int:
        """ Return how many coins """
        return self.__deposit

    def render(self, screen) -> "Etf":
        """ Render for bling machine """
        super().render(screen)
        if self.isStart():
             x, y = self.getPosition()
             utils.write_text("%d"%self.__deposit, (x, y - (self.getZIndex() + self.getRumbling()) * self.getSize()[1] / 2), screen, utils.sFont, "#ffff00")
        return self

class InteretetsComposes(Machine):
    def __init__(self, x: int, y: int, sprite, z: int = 0) -> "Etf":
        """ Initialisation of class BlingMachine """
        super().__init__(x, y, sprite, z)
        self.setName("interets composes")
        self.__deposit  : int   = 0
        self.__timer    : float = 0
        self.__max      : float = 100_000_000_000
        self.__min      : float = 10  # 0_000
        self.__taux     : float = 0.05

    def depositAll(self, player) -> "InteretetsComposes":
        """ Deposit all player money """
        self.__deposit += player.takeCoins(self.__max - self.__deposit)
        return self

    def takeAll(self, player) -> "InteretetsComposes":
        """ Deposit all player money """
        player.giveCoins(self.__deposit)
        self.__deposit = 0
        return self

    def interact(self, player) -> "Etf":
        """ Interact with the bling machine """
        super().interact()
        if self.__deposit == 0 and player.nCoins() >= self.__min:
            self.__deposit = player.takeCoins(self.__max)
        else:
            player.giveCoins(self.__deposit)
            self.__deposit = 0
        return self

    def help(self, blocks: list[list[list[Block]]]) -> None:
        """ Fuck it """
        super().help(blocks, ["CA, C'EST LES INTERETS COMPOSES", "IL FONCTIONNE EN GENERANT DES INTERET SUR VOTRE", "SOMME DEPOSE PLUS LES INTERETS PRECEDENTS", "", "C'EST UN CONCEPT TRES PUISSANT DE LA FINANCE!"])

    def update(self, dt) -> "Etf":
        """ Update the bling machine """
        super().update(dt)
        if self.isStart():
            self.__timer += dt
            if self.__timer > 10:
                self.__timer = 0
                self.__deposit += self.__deposit * self.__taux
        return self

    def howMuch(self) -> int:
        """ Return how many coins """
        return self.__deposit

    def render(self, screen) -> "Etf":
        """ Render for bling machine """
        super().render(screen)
        if self.isStart():
             x, y = self.getPosition()
             utils.write_text("%d"%self.__deposit, (x, y - (self.getZIndex() + self.getRumbling()) * self.getSize()[1] / 2), screen, utils.sFont, "#ffff00")
        return self


class Macron(Machine):
    def __init__(self, x: int, y: int, sprite, z: int = 0, blocks: list = []) -> "Etf":
        """ Initialisation of class BlingMachine """
        super().__init__(x, y, sprite, z)
        self.setName("impots")
        self.__total   : int = 0
        self.__oldCoins: int = 0
        self.__coins   : int = 0
        self.__objectif: int = 3
        self.__player        = None
        self.__blocks        = blocks
        self.__timer         = 0
        self.__time          = 60 * 3

    def interact(self, player) -> "Etf":
        """ Interact with the bling machine """
        super().interact()
        self.__player = player
        self.__coins += player.takeCoins(self.__objectif - self.__coins)
        return self

    def help(self, blocks: list[list[list[Block]]]) -> None:
        """ Fuck it """
        super().help(blocks, ["VOICI LES IMPOTS", "EN FONCTION DE TON REVENU DU MOIS DERNIER, TU DOIS LUI DONNER","UNE CERTAINE SOMME TOUTES LES 3 MINUTES SOUS PEINES DE GAME OVER."])

    def update(self, dt) -> "Etf":
        """ Update the bling machine """
        super().update(dt)
        if self.isStart():
            if self.__blocks == None or self.__player == None:
                return self
            self.__timer += dt
            if self.__timer > self.__time:
                if self.__coins < self.__objectif:
                    self.__player.kill()
                    return self
                self.__total += self.__coins
                total_player = self.__player.nCoins()
                for line in self.__blocks:
                    for pile in line:
                        for b in pile:
                            if isinstance(b, Machine) and not isinstance(b, Macron):
                                total_player += b.howMuch()
                self.__objectif = 0.3 * (total_player)
                self.__coins = 0
                self.__timer = 0
                # self.__oldCoins = self.__oldCoins - self.__coins
        return self

    def render(self, screen) -> "Etf":
        """ Render for bling machine """
        super().render(screen)
        if self.isStart():
             x, y = self.getPosition()
             utils.write_text("%02d:%02d (%d/%d)"%((self.__time - int(self.__timer)) / 60, (self.__time - int(self.__timer)) % 60, self.__coins, self.__objectif), (x, y - (self.getZIndex() + self.getRumbling()) * self.getSize()[1] / 2), screen, utils.sFont, "#ffff00")
        return self

if __name__ == "__main__":
    print("This module shouldn't be run as if, exiting.")
    exit(84)

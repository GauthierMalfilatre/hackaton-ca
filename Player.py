##
## HACKATON PROJECT, 2026
## CAVA
## File description:
## Block class'
##
import pygame
import utils

DIR_NONE  = 0
DIR_LEFT  = 4
DIR_RIGHT = 6
DIR_UP    = 8
DIR_DOWN  = 10

class Player:
    def __init__(self, sprite = None, x: int = 300, y: int = 300) -> bool:
        """ Initialisation of class Player """
        self.__x        : float = x
        self.__y        : float = y
        self.__sprite           = sprite
        self.__rect             = pygame.Rect(0, 0, 128, 1128)
        self.__dt       : float = 0
        self.__speed    : int   = 200
        self.__dir      : int   = DIR_NONE
        self.__anmiframe: float = 0
        self.__coins    : float = 0

    def giveCoins(self, ammount: int = 1) -> "Player":
        """ Give the player n coins """
        if ammount > 0:
            self.__coins += ammount

    def takeCoins(self, ammount: int = 1) -> "Player":
        """ Give the player n coins """
        if ammount > 0:
            if ammount > self.__coins:
                ammount = self.__coins
            self.__coins -= ammount
            return ammount
        return 0

    def getPosition(self) -> tuple[int, int]:
        """ Return the player position """
        return (self.__x, self.__y)

    def getOrigin(self) -> tuple[int, int]:
        """ return the player center """
        return (self.__x + 64, self.__y + 64)

    def __handleCollision(self, MAP: list, target_pos: list[float, float]) -> "Player":
        """ Handle collision for player """
        
        for i in ((target_pos[0] + 32, target_pos[1] + 32), (target_pos[0] + 96, target_pos[1] + 32),
                  (target_pos[0] + 32, target_pos[1] + 96), (target_pos[0] + 96, target_pos[1] + 96),
                  (target_pos[0] + 64, target_pos[1] + 32), (target_pos[0] + 32, target_pos[1] + 64),
                  (target_pos[0] + 64, target_pos[1] + 96), (target_pos[0] + 96, target_pos[1] + 64)):
            current_case = (int((i[0]) // 50), int((i[1]) // 50))
            current_block = MAP[current_case[1]][current_case[0]][-1]
            if current_block.getZIndex() != 0: # and not isinstance(current_block, Block.Teapot):
                return False
        return True

    def move(self, keys: list, dt: float, MAP: list) -> "Player":
        """ Move the player """
        target_pos: tuple[float, float] = [self.__x, self.__y]

        self.__dt  = dt
        self.__dir = DIR_NONE

        nm, nd = utils.get_nearest_machine(MAP, self.getOrigin())

        if nm != None and nd <= 100 ** 2:
            nm.activate_e()

        # TODO: Fix diagonales going faster
        if keys[pygame.K_UP] or keys[pygame.K_z]:
            target_pos[1] = self.__y - self.__speed * self.__dt
            self.__dir = DIR_UP
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            target_pos[1] = self.__y + self.__speed * self.__dt
            self.__dir = DIR_DOWN
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            target_pos[0] = self.__x + self.__speed * self.__dt
            self.__dir = DIR_RIGHT
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            target_pos[0] = self.__x - self.__speed * self.__dt
            self.__dir = DIR_LEFT

        if utils.click(pygame.K_e) and nm != None:
            nm.interact(self)

        if keys[pygame.K_h] and nm != None:
            nm.help(MAP)

        if self.__handleCollision(MAP, target_pos) and target_pos != [None, None]:
            self.__x = target_pos[0]
            self.__y = target_pos[1]

        MAP[int(self.__y + 96) // 50][int(self.__x + 64) // 50][0].rumble(force = True)

        self. __anmiframe += (dt * 4)
        self.__rect.x = 128 * (self.__dir + (int(self.__anmiframe) % (4 if self.__dir < DIR_LEFT else 2)))

    def render(self, screen) -> "Player":
        """ Render the player """
        screen.blit(self.__sprite, (self.__x, self.__y - 16), self.__rect)
        pygame.draw.rect(screen, "#323232", (10, 10, 150, 50))
        # The hitbox
        # pygame.draw.rect(screen, "#ff0000", (self.__x + 32, self.__y + 32, 128 / 2, 128 / 2), 1)
        utils.write_text("%d $"%self.__coins, (20, 15), screen, utils.sFont, "#ffffff")
        return self

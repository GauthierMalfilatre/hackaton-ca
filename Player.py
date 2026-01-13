##
## HACKATON PROJECT, 2026
## GAME_CA
## File description:
## Block class'
##
import pygame

DIR_NONE  = 0
DIR_LEFT  = 4
DIR_RIGHT = 6
DIR_UP    = 8
DIR_DOWN  = 10

class Player:
    def __init__(self, sprite = None, x: int = 0, y: int = 0) -> "Player":
        """ Initialisation of class Player """
        self.__x        : float = 100
        self.__y        : float = 10
        self.__sprite           = sprite
        self.__rect             = pygame.Rect(0, 0, 64, 64)
        self.__dt       : float = 0
        self.__speed    : int   = 100
        self.__dir      : int   = DIR_NONE
        self.__anmiframe: float = 0

    def move(self, keys: list, dt: float) -> "Player":
        """ Move the player """
        self.__dt = dt
        self.__dir = DIR_NONE
        if keys[pygame.K_UP]:
            self.__y -= self.__speed * self.__dt
            self.__dir = DIR_UP
        if keys[pygame.K_DOWN]:
            self.__y += self.__speed * self.__dt
            self.__dir = DIR_DOWN
        if keys[pygame.K_RIGHT]:
            self.__x += self.__speed * self.__dt
            self.__dir = DIR_RIGHT
        if keys[pygame.K_LEFT]:
            self.__x -= self.__speed * self.__dt
            self.__dir = DIR_LEFT

        self. __anmiframe += (dt * 2)
        self.__rect.x = 64 * (self.__dir + (int(self.__anmiframe) % (4 if self.__dir < DIR_LEFT else 2)))

    def render(self, screen) -> "Player":
        """ Render the player """
        screen.blit(self.__sprite, (self.__x, self.__y), self.__rect)
        return self
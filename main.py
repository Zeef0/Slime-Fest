import pygame
from pygame.locals import *
import sys


pygame.init()

w, h = 600, 400
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Slime Fest")


def draw():
    pygame.display.update()
    screen.fill("Pink")


def main():
    game_active = True
    while game_active:
        draw()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()

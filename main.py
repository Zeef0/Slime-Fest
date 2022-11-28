import pygame
from pygame.locals import *
import sys


class Slime(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


pygame.init()

w, h = 600, 400
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Slime Fest")

slime = Slime("./assets/slime.png")
slime_group = pygame.sprite.Group()
slime_group.add(slime)


def draw():
    pygame.display.update()
    screen.fill("Pink")
    slime_group.draw(screen)
    slime.update()


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

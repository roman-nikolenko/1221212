import pygame
import pygame as pg
from player import Player

SIZE = W, H = 1280, 720
BLACK = (0, 0, 0)
WHITE = (225, 225, 225)

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Итоговый проект')

player = Player(screen)

while True:
    for event in pygame.event.get():
        keys = pg.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()

    screen.fill(BLACK)
    player.draw()
    if keys[pygame.K_LEFT]:
        player.move()
    pygame.display.flip()
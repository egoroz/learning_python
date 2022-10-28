import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((155,155,155))
# rect(screen, (255, 0, 255), (100, 100, 200, 200))
# rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
# polygon(screen, (255, 255, 0), [(100,100), (200,50),
#                                 (300,100), (100,100)])
# polygon(screen, (0, 0, 255), [(100,100), (200,50),
#                               (300,100), (100,100)], 5)
# circle(screen, (0, 255, 0), (200, 175), 50)
circle(screen, (255, 255, 0), (200, 175), 100)
circle(screen, (0, 0, 0), (200, 175), 100, 3)

circle(screen, (255, 0, 0), (160, 150), 15)
circle(screen, (0, 0, 0), (160, 150), 5)

circle(screen, (255, 0, 0), (240, 150), 10)
circle(screen, (0, 0, 0), (240, 150), 5)

rect(screen, (0,0,0), (165, 220, 75, 15),)

polygon(screen, (0, 0, 0), [(100,100), (200,50),
                                (300,100), (100,100)])

polygon(screen, (0, 0, 0), [(130,120), (170,140),
                            (170,130), (130,110)])
polygon(screen, (0, 0, 0), [(130,120), (170,140),
                            (170,130), (130,110)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
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
polygon(screen, (0, 0, 0), [(310,100), (230,140),
                            (230,130), (310,90)])

x1 = 157; y1 = 190
x2 = 250; y2 = 200
N = 17
color = (0, 0, 0)

h = (x2 - x1) // (N+1)
x = x1 + h
for i in range(N):
    line(screen, color, (x, y1), (x, y2))
    x += h


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
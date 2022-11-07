import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 200
x0 = 900
y0 = 700
screen = pygame.display.set_mode((x0, y0))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
# временно
COLORS = [YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW]


def new_ball():
    """Рисует новый шарик """
    global x, y, r
    x = randint(100, 800)
    y = randint(100, 600)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def new_speed():
    """Дает шарику начальную скорость """
    global z
    z = randint(1, 2)


def speed_balls(speeds, balls):
    """Отражение шариков от краев """
    new_speeds = []
    for i in range(len(balls)):
        x1, y1, r1 = balls[i]
        vx, vy = speeds[i]
        if r1 >= 900 - x1 or r1 >= x1:
            vx = -vx
        if r1 >= 700 - y1 or r1 >= y1:
            vy = -vy
        new_speeds.append((vx, vy))
    return new_speeds

def move_balls(balls, speeds):
    """Движение шариков в одном направление """
    new_balls = []
    for i in range(len(balls)):
        x1, y1, r1 = balls[i]
        vx, vy = speeds[i]
        x1 += vx
        y1 += vy
        new_balls.append((x1, y1, r1))
    return new_balls


def show_balls(balls):
    for ball in balls:
        x1, y1, r1 = ball
        color = COLORS[randint(0, 5)]
        circle(screen, color, (x1, y1), r1)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
counter = 0
balls = []
speeds = []
tick = 0

while not finished:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos
            if (x - x1)**2 + (y - y1)**2 <= r**2:
                counter += 1
                print(counter)

    screen.fill(BLACK)
    tick0 = pygame.time.get_ticks()
    if tick0 - tick > 3000:
        new_ball()
        new_speed()
        speeds.append((z, 4 - z))
        balls.append((x, y, r))
        tick = pygame.time.get_ticks()
    show_balls(balls)
    balls = move_balls(balls, speeds)
    speeds = speed_balls(speeds, balls)
    pygame.display.update()

pygame.quit()
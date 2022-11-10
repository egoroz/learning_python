import pygame
from pygame.draw import *
from random import randint

pygame.init()
pygame.font.init()

FPS = 100
x0 = 900
y0 = 700
screen = pygame.display.set_mode((x0, y0))
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render('Ваш счёт: 0', False, (255, 255, 255))


def new_ball():
    """Рисует новый шарик  и дает ему начальную скорость"""
    global x, y, r, z
    x = randint(100, 800)
    y = randint(100, 600)
    r = randint(20, 60)
    z = randint(1, 16)
    circle(screen, (50, 255, 0), (x, y), r)


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
        circle(screen, (50, 255, 0), (x1, y1), r1)


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
            i = 0
            n = len(balls)
            while i < n:
                x, y, r = balls[i]
                vx, vy = speeds[i]
                if (x - x1)**2 + (y - y1)**2 <= r**2:
                    del balls[i]
                    del speeds[i]
                    counter += max(1, round(50*((vx**2 + vy**2)**0.5)//r))
                    text_surface = my_font.render(f'Ваш счёт: {counter}', False, (255, 255, 255))
                    n -= 1
                i += 1
    screen.fill((0, 0, 0))
    tick0 = pygame.time.get_ticks()
    if tick0 - tick > 3000:
        new_ball()
        speeds.append((7 - z, 9 - z))
        balls.append((x, y, r))
        tick = pygame.time.get_ticks()
    show_balls(balls)
    balls = move_balls(balls, speeds)
    speeds = speed_balls(speeds, balls)
    screen.blit(text_surface, (0, 0))
    pygame.display.update()

pygame.quit()
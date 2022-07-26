import pygame as pg
from math import cos, sin, radians


pg.init()
size = width, height = 500, 500
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
FPS = 60

angle = 0
running = animation = True

while running:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                animation = not animation
    screen.fill((128, 128, 128))
    if animation:
        for point in range(360):
            x = int(cos(radians(point)) * 200) + width // 2
            y = int(sin(radians(point)) * 200) + height // 2
            to_x = int(cos(radians((point*(2+angle)) % 360)) * 200) + width // 2
            to_y = int(sin(radians((point*(2+angle)) % 360)) * 200) + height // 2
            pg.draw.line(screen, pg.Color('green'), (x, y), (to_x, to_y), 1)
        angle += 0.01
        pg.display.update()

pg.quit()

from sys import argv
import pygame as pg


if __name__ == '__main__':
    pg.init()
    w = int(argv[1])
    size = w, w
    cell = int(argv[2])

    assert size[0] % cell == 0

    screen = pg.display.set_mode(size)
    running = True

    width = w // cell
    for i in range(cell):
        for j in range(cell):
            left, top = width * j, width * i
            pg.draw.rect(screen, (255, 255, 255), ((left, top), (left + width, top + width)), 1)
            color = (0, 0, 0) if (i + j) % 2 == 0 else (255, 255, 255)
            screen.fill(color, pg.Rect(left, top, width, width))

    pg.display.flip()

    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT: running = False

            
    pg.quit()
        
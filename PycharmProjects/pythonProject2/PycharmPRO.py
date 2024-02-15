import pygame as pg

screen = pg.display.set_mode([200, 200])
pg.display.set_caption('TTTREE')
clock = pg.time.Clock()
fps = 60
while 1:
    clock.tick(fps)
    pg.display.update()
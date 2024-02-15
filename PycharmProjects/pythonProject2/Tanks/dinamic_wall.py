import pygame as pg
import random
class din_WALL(pg.sprite.Sprite):
    def __init__(self, x, y, group, color):
        pg.sprite.Sprite.__init__(self)
        # image_start = pg.image.load(filename).convert_alpha()
        # image_start = filename
        self.image = pg.Surface([10, 10])
        # self.image = pg.transform.scale(image_start, [long_x, long_y])
        self.rect = self.image.get_rect(topleft=[x, y])
        self.image.fill(color)
        self.add(group)
    def update(self):
        ...
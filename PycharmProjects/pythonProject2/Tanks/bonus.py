import random
from WINDOW_SIZE import window_size
import pygame as pg
class BONUS(pg.sprite.Sprite):
    def __init__(self,group,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([10,10])
        self.image.fill([255, 255, 255])
        self.rect = self.image.get_rect(center=[x, y])
        self.add(group)
    def update(self):...

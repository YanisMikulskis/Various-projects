import random

import pygame as pg
import random
from Tank import Tanks

class STRIKE(pg.sprite.Sprite):
    def __init__(self, group,color, cord_tanks, *axis):
        super().__init__()
        self.image = pg.Surface([5,5])

        self.rect = self.image.get_rect(center = cord_tanks)

        self.image.fill(color)
        self.group = group
        self.add(group)
        self.random_axis = axis[0] if axis else ...
        self.exp = False
        self.speed = 10


    def update(self, explosion):
        # if not explosion:
        if not self.exp:
            horizontal, vertical = ('x_left', 'x_right'), ('y_down', 'y_up')
            if self.random_axis in horizontal:
                self.rect.centerx = self.rect.centerx - self.speed if self.random_axis == 'x_left' else self.rect.centerx + self.speed
            else:
                self.rect.centery = self.rect.centery - self.speed if self.random_axis == 'y_up' else self.rect.centery + self.speed
       # if self.exp:


            ##self.kill()
            # exp = pg.sprite.Group()
            # parts = [pg.Surface([1,1]) for _ in range(10)]
            #
            # # map(lambda sprite: exp.add(sprite), parts)
            # print(exp)
            # parts = [pg.Surface([1, 1]) for _ in range(10)]
            # # exp_part = list(map(lambda img: img.get_rect(center=self.rect), parts))
            # parts_rect = [get_rect(center=self.rect) for i in parts]
            # print(parts_rect)

    # def explosion(self):
    #     self.rect.centery -= 1



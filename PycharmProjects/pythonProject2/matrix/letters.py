import time

import pygame as pg
import random as rnd
import sys
import time as t
from window_size import size_window
pg.init()

katakana = [chr(j) for j in range(int('0x30a0', 16), (int('0x30a0', 16) + 96))]
a = [str(i) for i in range(11)]
print(a)
class LETTER:
    def __init__(self, x, y, let, color, surf):
        self.x = x
        self.y = y
        self.surf = surf
        self.let = let
        self.color = color
        # --------------------------------------
        # self.let = let
        # self.color = color
        #
        # self.image = pg.font.SysFont('pingfang', 24).render(self.let, True, self.color)
        # self.rect = self.image.get_rect(center=[x,y])
        # pg.sprite.Sprite.__init__(self)
        # self.group = group
        # self.add(self.group)
        #
        #
        # self.speed = speed
        #--------------------------------------
        def Foo_KATAKANA(): return rnd.choice(katakana)
        self.let = Foo_KATAKANA()
        self.color = [0,255,0]
        self.letter = pg.font.SysFont('pingfang', 24).render(self.let, True, self.color)
        self.interval = rnd.randint(1, 2)
    def update(self):
        ...
        self.y += 2
        if self.interval:
            self.let = rnd.choice(katakana)
            self.letter = pg.font.SysFont('pingfang', 24).render(self.let, True, self.color)

        # self.letter = pg.font.SysFont('pingfang', 24).render(self.let, True, self.color)

        # self.y = y
        # self.x = x
        #
        # # if not pg.time.get_ticks() % interval:
        # #     self.let = rnd.choice(katakana)
        # # self.letter = pg.font.SysFont('pingfang', 24).render(self.let, True, self.color)
        # self.surf.blit(self.letter, [self.x, self.y])
        # # self.rect.centery += self.speed
        # # self.let = rnd.choice(katakana)
        # # next_letter = pg.font.SysFont('pingfang', 24).render(self.let, True, self.color)
        # # self.image = next_letter
        # # # if pg.time.get_ticks() % self.interval == 0:
        # # # del self.image
        # # # self.let = rnd.choice(katakana)
        # # # self.image = pg.font.SysFont('pingfang', 24).render(self.let, True, self.color)
        # ...






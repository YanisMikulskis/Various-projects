import random
import time
import pygame as pg
import random as rnd
class sp(pg.sprite.Sprite):
    def __init__(self,x,y,filename,group):
        pg.sprite.Sprite.__init__(self)
        image_start = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(image_start, [5, 5])
        self.rect = self.image.get_rect(center=[x,y])
        self.spore_color = 255
        self.add(group)
        def rnd_colour():
            return rnd.randint(1, 255)
        # def main_color():
        #     return [rnd_colour() for i in range(3)]
        # self.image.fill([0, self.spore_color, 0])
        # self.speed_x = rnd.randrange(-2,2)
        # self.speed_y = rnd.randrange(-2,2)
        self.ny = 1
        self.nx = 1

        self.image.fill([0, self.spore_color, 0])

        self.var = False
    def update(self, *drives):
        # self.speed_x = rnd.random()
        # self.speed_y = rnd.random()
        # self.rect.centerx += self.speed_x
        # self.rect.centery += self.speed_y
        # # if drives != ():
        # #     if drives[0]:
        # #         self.rect.centerx += drives[0]
        # #         self.rect.centery  += 0 #КОД ДЛЯ КОМЕТЫ
        # print(self.p)
        #_______________________________________
        # if self.p:
        #     self.rect.centery += self.ny
        #     self.rect.centerx += self.nx
        #     self.nx -= 0.1
        #     self.ny -= 0.1
        # if self.nx <= -3.0:
        #     self.p = 0
        # if not self.p:
        #     print(self.nx)
        #     self.rect.centery -= self.ny
        #     self.rect.centerx += self.nx
        #     self.nx += 0.1
        #     if self.nx >= 3.0:
        #         self.p = 1


        #chaotic drive
        self.rect.centerx += rnd.randint(-self.nx,self.nx)
        self.rect.centery += rnd.randint(-self.ny,self.ny)





        self.image.fill([0, self.spore_color, 0])
        if not self.var:
            self.spore_color -= 2
            if self.spore_color <= 0:
                self.kill()
                self.var = True
        if self.var:
            self.spore_color += 2
            if self.spore_color >= 255:
                self.var = False

        if self.rect.top > 1000 or self.rect.bottom < 0 or self.rect.left > 1000 or self.rect.right < 0\
                or self.spore_color < 0:
            print(self.spore_color)
            self.kill()

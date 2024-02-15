import random
import sys
import pygame as pg
from window_tennis import size_window
scale = 0
class Ball(pg.sprite.Sprite):
    def __init__(self, x, y, filename, group):
        pg.sprite.Sprite.__init__(self)
        image_start = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(image_start, [image_start.get_width()//4,
                                                      image_start.get_height()//4]).convert_alpha()
        self.rect = self.image.get_rect(center = [x, y])

        self.speed_x = 0
        self.speed_y = 0
        self.var = 0 #количество касаний
        self.var_balls = True #переменная для включения или отключения
        # главной фукнции создания нового шарика




        self.add(group)
    def update(self, *arg_var):

        def main_color():
            color = lambda x: random.randint(1, x)
            return [color(255) for _ in range(3)]
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        def drive():
            match arg_var[0]:
                case 'top': self.speed_y = -2
                case 'bot': self.speed_y = 2
                case 'left':self.speed_x = -2
                case 'right':self.speed_x = 2
        if arg_var != ():
            match arg_var[1]:
                case 'U':
                    [self.image.fill(main_color()) for i in range(1)]
                    drive()
                case 'C':

                    self.var += 1
                    [self.image.fill(main_color()) for i in range(1)]
                    drive()
            if arg_var[0] == 'bot' and arg_var[1] == 'C':
                self.var += 1



        if self.rect.right >= size_window()[0] or self.rect.left <= 0:
            self.speed_x = -self.speed_x
        elif self.rect.bottom >= size_window()[1] or self.rect.top <= 0:
            self.speed_y = -self.speed_y




import random
from WINDOW_SIZE import window_size
import pygame as pg


class Tanks(pg.sprite.Sprite):
    def __init__(self, x, y, color, filename, group):
        pg.sprite.Sprite.__init__(self)
        self.file = filename

        image_start = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(image_start, [30, 30]).convert_alpha()

        self.rect = self.image.get_rect(center=[x, y])
        self.enemy_var = 0
        #----------------------
        #чтобы "вражеские танки" двигались независимо друг от друга, делаем следующее: если движение по траектории Х
        #дает True (-1 или 1), то движение по оси У в этот момент равно 0, иначе движение по оси У = True (1 или -1)
        self.qwe_x = 1
        self.qwe_y = 0 if self.qwe_x else random.randint(-1, 1)
        self.function_axis = lambda : random.choice(['x_right', 'x_left', 'y_up', 'y_down'])
        self.random_axis = self.function_axis()
        #-----------------------
        self.image.fill(color)
        self.group = group

        self.add(self.group) if self.group is not None else ...

        self.enemy_speed = 1
        self.vector_var = None
    def update(self, speed, vector):

        def drive_tanks(speed, *cords):
            if cords:
                if cords[0] == 'X':
                    self.rect.centerx += speed
                elif cords[0] == 'Y':
                    self.rect.centery += speed
            else:
                self.rect.centery += 0
                self.rect.centerx += 0

        if vector == 'LEFT':
            drive_tanks(speed, 'X')
        elif vector == 'RIGHT':
            drive_tanks(speed, 'X')
        elif vector == 'DOWN':
            drive_tanks(speed, 'Y')
        elif vector == 'UP':
            drive_tanks(speed, 'Y')
        elif vector == 'STOP':
            drive_tanks(speed, 'Y')

    def enemy_update(self, step):
        self.step = step
        horizontal, vertical = ['x_right', 'x_left'], ['y_up', 'y_down']

        if self.enemy_var <= self.step:

            if self.random_axis in horizontal:
                self.rect.centerx = self.rect.centerx + self.enemy_speed if self.random_axis == 'x_right' \
                    else self.rect.centerx - self.enemy_speed
            elif self.random_axis in vertical:
                self.rect.centery = self.rect.centery + self.enemy_speed if self.random_axis == 'y_down' \
                    else self.rect.centery - self.enemy_speed

            self.enemy_var += 1

        else:
            self.random_axis, self.enemy_var = self.function_axis(), 0


        if self.rect.top > window_size()[1]:
            self.rect.bottom = 0
        elif self.rect.bottom < 0:
            self.rect.top = window_size()[1]

        if self.rect.right < 0:
            self.rect.left = window_size()[0]
        elif self.rect.left > window_size()[0]:
            self.rect.right = 0
        # chaotic_drive()
        # self.rect.centery += step_y

# double = lambda x: x * 2

# def double(x):
# return x * 2

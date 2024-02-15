import pygame as pg
import random

class WALL(pg.sprite.Sprite):
    def __init__(self, x, y, filename, group, long_x, long_y):
        pg.sprite.Sprite.__init__(self)
        image_start = pg.image.load(filename).convert_alpha()
        # image_start = filename
        self.image = pg.transform.scale(image_start, [random.randint(100,300), random.randint(10,100)])
        self.image = pg.transform.scale(image_start, [long_x, long_y])
        self.rect = self.image.get_rect(topleft=[x, y])
        self.image.fill([0, 255, 0])
        self.add(group)
    def update(self):
        ...

# from timeit import timeit as time_method
# from timeit import default_timer
# var = 100
# var2 = None
# test_1 = """

# if var == 100:
#     ...
# """
# test_2 = """к
# match var:
#     case 100:
#         ...
# """
# t1 = (time_method(test_1, 'pass', default_timer, 100, globals()) * 1000000).__round__(3)
# t2 = (time_method(test_2, 'pass', default_timer, 100, globals()) * 1000000).__round__(3)
#
# print(t1)
# print(t2)

import pygame as pg
from window_tennis import size_window
class Rocket(pg.sprite.Sprite):
    def __init__(self, x, y, filename):
        pg.sprite.Sprite.__init__(self)
        image_start = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(image_start, [100, 10])
        self.rect = self.image.get_rect(center = [x, y])

    def update(self, *args):
        self.image.fill([255, 0, 0])
        self.rect.x += args[0]
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= size_window()[0]:
            self.rect.right = size_window()[0]

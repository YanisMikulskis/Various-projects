import pygame as pg
import random

class BOTTLE(pg.sprite.Sprite):
    def __init__(self, x, y, filename, group):
        pg.sprite.Sprite.__init__(self)
        image_base = pg.image.load(filename).convert_alpha()
        image_base_rot =  pg.transform.rotate(image_base, 90)

        def TRANSFORM_BOTTLE(size_increment):
            image_base_sca = pg.transform.scale(image_base_rot, [image_base_rot.get_width() // size_increment,
                                                                 image_base_rot.get_height() // size_increment])
            self.image = pg.transform.flip(image_base_sca, bool(random.randint(0, 1)), bool(random.randint(0, 1)))
            return self.image
        if filename == '5 OZER.png':
            self.rect = TRANSFORM_BOTTLE(5).get_rect(bottomleft=(x,y))
        else:
            self.rect = TRANSFORM_BOTTLE(10).get_rect(bottomleft=(x,y))
        self.add(group)

    def update(self, *args):
        # self.image.fill([255, 255, 255])
        if args[0] == 1:
            speed_bottle = args[1]
            self.rect.centery += speed_bottle
        if self.rect.top > 1000:
            self.kill()


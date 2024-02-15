import random
import sys
import pygame as pg
import pymunk.pygame_util  # библиотека для создания физики
from window_size_snake_sand import size_window
from clocks import PLATFORM
from sands import SAND

pymunk.pygame_util.positive_y_is_up = False  # подгон к одной системе координат (х увеличивается при движении ВНИЗ)
pg.init()
# --------- создание окна
SCREEN = pg.display.set_mode(size_window())
pg.display.set_caption('SAND CLOCK')
clock = pg.time.Clock()
fps = 144
runGame = True

# ---------------PYMUNK-----------------
draw_options = pymunk.pygame_util.DrawOptions(SCREEN)
# Переменные pymunk (пространство)
space = pymunk.Space()
space.gravity = 0, 8000
# патформа
segments = []


def up_segments(element):
    global segments
    segments += [element]


# clocks vars
size = 3
platform = PLATFORM(space, 400 - size * 2, 200, 500 - size * 2, 300, size)  # \
platform_2 = PLATFORM(space, 510 + size * 2, 300, 610 + size * 2, 200, size)  # /

platform_3 = PLATFORM(space, 500 - size * 2, 300, 500 - size * 2, 310, size)  # |
platform_4 = PLATFORM(space, 510 + size * 2, 300, 510 + size * 2, 310, size)  # |

platform5 = PLATFORM(space, 400 - size * 2, 410, 500 - size * 2, 310, size)
platform6 = PLATFORM(space, 610 + size * 2, 410, 510 + size * 2, 310, size)

floor = PLATFORM(space, 400 - size * 2, 410, 610 + size * 2, 410, size)
up_segments(platform), up_segments(platform_2), up_segments(platform_3)
up_segments(platform_4), up_segments(platform5), up_segments(platform6)
up_segments(floor)
del floor
for i in segments: i.location()
#
# brick_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
# brick_body.position = 100, 100
# brick_shape = pymunk.Poly.create_box(brick_body, (20, 10))
# brick_shape.elasticity = 1.0
# brick_shape.color = pg.Color("blue")
# brick_shape.group = 1
# # brick_shape.collision_type = collision_types["brick"]
# space.add(brick_body, brick_shape)


cords_IMAGE = pg.font.SysFont('applegothic', 24).render(f'{(platform.LX, platform.LY)}  '
                                                        f'{(platform.RX, platform.RY)}'
                                                        , True, [255, 255, 255])
cords_RECT = cords_IMAGE.get_rect()
sandsss = []


def Foo():
    sand2 = SAND(space, 1, 1, [random.randint(580, 590), 100])
    sandsss.append(sand2)
    sand2.location()
    print(len(sandsss))


x = 2

x2 = 100
y2 = 100

x3 = 200
motion = None


def create_kin(x2_arg):
    brick_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    brick_body.position = x2_arg, y2
    brick_shape = pymunk.Poly.create_box(brick_body, (20, 10))
    brick_shape.elasticity = 1.0
    brick_shape.color = pg.Color("blue")
    brick_shape.group = 1
    brick_shape.collision_type = ["brick"]
    space.add(brick_body, brick_shape)
    if not x2_arg:
        space.remove(brick_body, brick_shape)


while runGame:
    SCREEN.fill([0, 0, 0])
    clock.tick(fps)
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    if keys[pg.K_f]:
        Foo()
    elif keys[pg.K_d]:
        x2 += 1
        x3 += 1
        create_kin(x2)
        create_kin(0)

    # ------
    # space.step(1/fps)
    # space.debug_draw(draw_options)
    platform.options(fps, draw_options)

    SCREEN.blit(cords_IMAGE, cords_RECT)

    pg.display.update()

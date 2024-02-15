import pygame as pg
import sys, time
from WINDOW_SIZE import window_size
from Tank import Tanks
from Wall import WALL
import random, re
from numpy import array as nparray
from collections import namedtuple
from strike import STRIKE
from dinamic_wall import din_WALL
from bonus import BONUS
pg.init()
# ------------------------------------------
# создание окна
screen = pg.display.set_mode(window_size())
pg.display.set_caption('TANKS')
fps = 60
clock = pg.time.Clock()
runGame = True
motion, motion_enemy = None, None
make = None
# ------------------------------------------
# переменные для движения
left, right, up, down = pg.K_a, pg.K_d, pg.K_w, pg.K_s
tanks = Tanks(500, 800, [255, 0, 0], 'STAR.png', None)
alert = pg.sprite.Group()
# for _ in range(10):
#     x, y = random.randint(100, 800), random.randint(100, 800)
#     Tanks(x, y, [0, 0, 255], 'STAR.png', alert)

enemy_tank = Tanks(100, 750, [0, 0, 255], 'STAR.png', alert)
enemy_tanks_2 = Tanks(600, 700, [0, 255, 0], 'STAR.png', alert)
enemy_tanks_3 = Tanks(200, 300, [255, 0, 0], 'STAR.png', alert)
walls, shots, shots_enemy, super_shots, bonuses\
    = pg.sprite.Group(), pg.sprite.Group(), pg.sprite.Group(), pg.sprite.Group(), pg.sprite.Group()
din_walls = pg.sprite.Group()
alpha_value = 50
bloor_surf = pg.Surface(window_size())

bon, ammunation = BONUS(bonuses, 800, 500), 0

# map_samples ----------------------------шаблоны карт
# map_1 = namedtuple('map1', 'loc1')
# map_1(loc1=[WALL(200, 0, 'STAR.png', walls, 40, 200)])
# map_1 = nparray([[WALL(200, 0, 'STAR.png', walls, 40, 200)],
#                  [WALL(0, 300, 'STAR.png', walls, 200, 40)],
#                  [WALL(800, 0,'STAR.png', walls, 40, 200)]])

cursor = None


def make_test(x, y, lines, color):  # рекурсивное создание одного блока
    if lines == 5:
        return

    def make_block_2(x_2, blocks):
        if blocks == 5:
            return
        din_WALL(x_2, y, din_walls, color)

        blocks += 1
        return make_block_2(x_2 + 10, blocks)

    make_block_2(x, 0)
    lines += 1

    return make_test(x, y + 10, lines, color)


# make_test(200, 200, 0)


# def make_block(start_x, start_y, color):
#     def make_side():
#         din_WALL(start_x, start_y, din_walls, color)
#
#     initial_value = start_x
#     for _ in range(5):
#         # time.sleep(0.5)
#         # print(start_x)
#         start_x = initial_value  # стартовое значение икс. блок заполняется полосами слева направо и идет заполнение вниз
#         for _ in range(5):
#             make_side()
#             start_x += 10
#         start_y += 10

tyr_2 = None


def make_wall(start_x, start_y, *vector_construction):
    vector_cords = {
        'R': 50,
        'L': -50,
        'U': -50,
        'D': 50
    }
    next_cords, first_element = nparray([None, None]), True
    # Cписок для последующего построения стены. от первого и второго элементов списка будут отталкиваться
    # первые блоки следующих кусков стены. В каждом базовом случае рекурсивного построения стены, элементы списка
    # обновляются на текущие значения x_req и y_req, который в рекурсии на последнем возврате становятся равно координатам
    # верхнего левого угла следующего элемента. Также тут есть переменная первого элемента, которая становится FALSE,
    # когд мы создаем первый участок стены. Он нам нужен чтобы правильно брался индекс при повторящихся пресетах (напр.
    # 'L4', 'D2', 'L4')
    for i in vector_construction:  # vector_construction - это список пар (направление, размер)
        def recursion_wall(x_req, y_req, i, number_block):  # рекурсивное создание одного куска стены
            if number_block == int(i[1]):
                next_cords[0], next_cords[1] = x_req, y_req
                return
            make_test(x_req, y_req, 0, [random.randint(0, 255) for _ in range(3)])
            if i[0] in ['R', 'L']:
                x_req += vector_cords.get(i[0])
            elif i[0] in ['D', 'U']:
                y_req += vector_cords.get(i[0])
            number_block += 1
            return recursion_wall(x_req, y_req, i, number_block)

        if vector_construction.index(i) == 0 and first_element:
            recursion_wall(start_x, start_y, i, 0)
            first_element = False
        else:
            recursion_wall(next_cords[0], next_cords[1], i, 0)


# ---------------------------------
# return recursion_external(x_ext, y_ext, number_wall)
# recursion_external(start_x, start_y, 0)
# start_x = start_x - (50 * (int(i[1])-1))
# start_x += vector_cords.get(i[0]) * int(i[1])

# quantity_blocks = int(''.join(re.findall(r'\d+', i)))
# varvar = start_x
# for block in range(quantity_blocks):
#
#     make_test(varvar, start_y, 0)
#     varvar -= 50

# vector_size = int(''.join(re.findall(f'\d+', i)))  # регулярка для получения чисел из координат
# # старт построения стены
# temporary_var, first_element = 0, True if vector_construction.index(i) == 0 else False
#
# horizontally = True if i[0] in ('R', 'L') else False

# на каждой итерации цикла по одному куску стены (по блокам в нем.например R4 означает,
# что мы создадим 4 блока в правую сторону) будем создавать словарь (чтобы избавиться от if else). Словарь
# представляет из себя структуру {направление: функция}. функция уменьшает или увеличивает место появления
# координаты левого угла Х или У для следующего блока
# for j in range(vector_size):
#     print(vector_construction.index(i))
#     cord_dict, rnd_color = {
#         'R': change_x('R', start_x),
#         'L': change_x('L', start_x),
#         'U': change_y('U', start_y),
#         'D': change_y('D', start_y)
#     }, [random.randint(0, 255) for _ in range(3)]
#
#     if first_element:
#         print(first_element)
#         print(f'flag {start_x}   {start_y}')
#         make_block(start_x, start_y, rnd_color)
#         temporary_var += 1
#         if temporary_var != vector_size:
#             start_x = cord_dict.get(i[0]) if horizontally else start_x
#             start_y = cord_dict.get(i[0]) if not horizontally else start_y
#     else:
#         # if horizontally:
#         print(f'flag22 {start_x}   {start_y}')
#         start_x = cord_dict.get(i[0]) if horizontally else start_x
#         start_y = cord_dict.get(i[0]) if not horizontally else start_y
#         make_block(start_x, start_y, rnd_color)
# ------------------------

def test_map():
    make_wall(650, 200, 'L7', 'D7', 'R7', 'U7')


print()

test_map()


# def first_map():
#     """ первая карта"""
#     #------------------
#     make_wall(300, 0, 'D4','L2')
#     make_wall(650, 0, 'D4', 'R2')
#     make_wall(425, 475, 'R3', 'D2', 'L2', 'U2')
#     make_wall(700, 600, 'D4')
#
#
# first_map()


# ---------выстрелы
def shot(arg_cord_tanks, *drive):
    sqwe = STRIKE(arg_cord_tanks)
    return sqwe


# -------------------

var = None
speed_flag = 4
sss = 30
make_strike = lambda vector_strike, group, rect_param: STRIKE(group,[255,0,0], rect_param, vector_strike)
make_strike_enemy = lambda enemy, axis: STRIKE(shots_enemy,[255,255,255], enemy.rect.center, axis)
strike = lambda func_strike: func_strike


collide_alert = False
bonus_tanks_collide, text  = False, False

vector_strike = 'y_up'

while runGame:

    bloor_surf.fill([0,0,0])
    clock.tick(fps)

    screen.blit(bloor_surf, [0,0])
    bloor_surf.set_alpha(alpha_value)
    # screen.fill([0, 0, 0])

    keys = pg.key.get_pressed()
    screen.blit(tanks.image, tanks.rect)

    def info(param):
        f1 = pg.font.SysFont('arial', 20)
        text = f1.render(f'Суперпушка. Осталось снарядов {param}', True, [255, 255, 255])

        screen.blit(text, [10, 10])
    if text:
        info(ammunation)

    # screen.blit(enemy_tank.image, enemy_tank.rect)
    shots.draw(screen)
    shots_enemy.draw(screen)
    super_shots.draw(screen)
    bonuses.draw(screen)
    probability_shot = random.random()



    #переменная для автоматической стрельбы врагов


    walls.draw(screen)
    din_walls.draw(screen)

    alert.draw(screen)

    pg.draw.line(screen, [255, 255, 255], [300, 0], [300, 1000])
    pg.draw.line(screen, [255, 255, 255], [700, 0], [700, 1000])
    pg.draw.line(screen, [255, 255, 255], [500, 0], [500, 1000])
    # ------------------------------------------
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_f:
                if not bonus_tanks_collide:
                    make_strike(vector_strike, shots, tanks.rect.center)
                    motion = 'stand_shot'
                else:

                    guns = [tanks.rect.topleft, tanks.rect.center, tanks.rect.topright]
                    super_strike = lambda: [make_strike(vector_strike, super_shots, item) for item in guns]
                    [super_strike() for _ in range(10)]
                    motion = 'super_shot'
                    ammunation -= 1
                    print(ammunation)
                    if not ammunation:
                        bonus_tanks_collide, text = False, False


    shots.update(False) if motion == 'stand_shot' else super_shots.update(False)




    # ----функция удаления снаряда при столкновении
    sprite_func = lambda sprite, group: pg.sprite.spritecollide(sprite, group, dokill=True)
    # ----удаление куска стены при попаданиии вместе со снарядом или врага при попадании вместе со снарядом
    [bullet.kill() if sprite_func(bullet, din_walls) or sprite_func(bullet, alert) else ... for bullet in shots]
    [super_strike.kill() if sprite_func(super_strike, din_walls) or
                            sprite_func(super_strike, alert) else ... for super_strike in super_shots]
    #----удаление куска стены при попаданиии cнаряда врага
    [bullet.kill() if sprite_func(bullet, din_walls) else ... for bullet in shots_enemy]
    # ---супер пушка. При столкновении с бонусом, группа super_strike заполняется 10-ю элементами. Каждый элемент -
    # тройной выстрел (функция выстрела, выполняемая 3 раза в рамках одного выстрела с тремя разными
    # точками старта снаряда из танка). Когда делаем 10 супервыстрелов, выстрелы становятся опять обычными
    if pg.sprite.spritecollide(tanks, bonuses, dokill=True):
        bonus_tanks_collide, ammunation = True, 10
        text = True




  #  make_strike(vector_strike) if sprite_func(tanks, din_walls) else ... #столкновение с бонусом
    # if bon.rect.colliderect(tanks.rect):
    #     make_strike(vector_strike)



    shots_enemy.update(False)
    # print([i for i in alert][0].random_axis)
    if 0.1 < probability_shot < 0.12:

        enemies = [enemy for enemy in alert]
        # print(enemies[0].random_axis)
        make_strike_enemy(enemies[0], enemies[0].random_axis)

    #взрывы при столкновении снаряда с объектом

    for i in shots:
        if i.rect.centerx not in list(range(window_size()[0])) or i.rect.centery not in list(range(window_size()[1])):
            i.exp = True




    # --Рекурсивная Функция, которая будет вызываться и менять поведение объекта, если он столкнется со стеной
    wall_list = [i for i in din_walls]


    def collide_drive(machine, arg_walls, idx, vector):
        global change_axis
        vertical, horizontal = ['UP', 'DOWN'], ['LEFT', 'RIGHT']

        if idx == len(arg_walls) - 1:
            return
        if arg_walls[idx].rect.colliderect(machine.rect):
            if vector == 'chaotic_drive': # логика поведения при столкновении ВРАГОВ со стенами
                horizontal_axis, vertical_axis = ['x_right', 'x_left'], ['y_up', 'y_down']

                def change_axis(center_axis, change_cord, vector):
                    if center_axis == 'x':
                        machine.rect.centerx += change_cord
                    elif center_axis == 'y':
                        machine.rect.centery += change_cord
                    machine.random_axis = vector

                if machine.random_axis in horizontal_axis:
                    change_axis('x', -1, 'x_left') if machine.random_axis == 'x_right' \
                        else change_axis('x', 1, 'x_right')
                elif machine.random_axis in vertical_axis:
                    change_axis('y', -1, 'y_up') if machine.random_axis == 'y_down' \
                        else change_axis('y', 1, 'y_down')


            if vector in vertical:
                machine.rect.centery += speed_flag if vector == 'UP' else - speed_flag
            elif vector in horizontal:
                machine.rect.centerx += speed_flag if vector == 'LEFT' else - speed_flag  # инкримент умножается на -1 и получается -=speed_flag
        idx += 1
        return collide_drive(machine, arg_walls, idx, vector)


    # --------------------------------------------------------------
    update_func = lambda speed, vector: tanks.update(speed, vector)











    def general_movement_func(speed, vector):
        global vector_strike #переменная которая отправляется в параметр функции? отвечающей за стрельбу,
        # чтобы снаряды летели по направлению движения
        update_func(speed, vector)
        if vector in ('UP', 'DOWN'):
            vector_strike = 'y_up' if vector == 'UP' else 'y_down'
        elif vector in ('LEFT', 'RIGHT'):
            vector_strike = 'x_left' if vector == 'LEFT' else 'x_right'
        collide_drive(tanks, wall_list, 0, vector)

    #движение своего танка
    if keys[left] or keys[right]:
        general_movement_func(-speed_flag, 'LEFT') if keys[left] else general_movement_func(speed_flag, 'RIGHT')
    elif keys[up] or keys[down]:
        general_movement_func(-speed_flag, 'UP') if keys[up] else general_movement_func(speed_flag, 'DOWN')


    # ---------------враги
    if not collide_alert:
        [i.enemy_update(100) for i in alert]
    for i in alert:
        collide_drive(i, wall_list, 0, 'chaotic_drive')
    # столкновение вражеских танков со стеной

    # for col in din_walls:
    #     for enemy in alert:
    #         if enemy.rect.colliderect(col.rect):
    #             enemy.enemy_update(100)

    # enemy.qwe_x *= -1 if not enemy.qwe_y else 0
    # enemy.qwe_y *= -1
    # collide_alert = True
    # enemy.qwe_x *= -1
    # enemy.qwe_y = 0

    # # enemy_tank.enemy_update(50)
    # alert.enemy_update(50)
    # collidelist(list) – проверка пересечения хотя бы с одним прямоугольником из списка прямоугольников list;
    # alpha_value = alpha_value + 1 if alpha_value < 100 else 100
    pg.display.update()


def func_1(param):
    return param ** 2


print()
var = lambda param: param ** 2


def func_2():
    return 100 ** 2


var2 = lambda: 100 ** 2

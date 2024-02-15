import pygame as pg
import random as rnd
import sys
from window_size import size_window
from letters import LETTER
import time
pg.init()
#------------------
# ОКНО
SCREEN = pg.display.set_mode(size_window())
pg.display.set_caption('MATRIX')

# pg.time.set_timer(pg.USEREVENT, rnd.randint(10, 1000))
#-----------------
# Переменные окна
clock = pg.time.Clock()
FPS = 60
runGame = True
white = [255, 255, 255]
green = [0, 255, 0]
RED = [255,0,0]


#--------------------------
#алфавит Катакана (из Матрицы) и параметры шрифта
katakana = [chr(j) for j in range(int('0x30a0', 16), (int('0x30a0', 16) + 96))]
letter_style_FOR_INFO = ('pingfang', 48)
#--------------------------
#список стартовых ОТРИЦАТЕЛЬНЫХ координат по оси У(буквы должны появляться ВНЕ экрана
letters_y, letters_x = [-i for i in range(0, 660, 22)], [j for j in range(25, 1000, 50)]

rev_letters_y = list(reversed(letters_y))
rev_down_letters_y = [-i for i in letters_y]
print(rev_down_letters_y)
rev_letters_x = list(reversed(letters_x))

#[0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
#--------------------------
#создание символов и главной буквы, за которой будут двигаться остальные
# general_let = LETTER('!!', [255,0,0], 75, letters_y[0], letter_group)
# general_let2 = LETTER('??', [0,0,255], 75, letters_y[0], letter_group)
def create_letter(argletter, argx, argy, color, arg_speed, arg_group):
    letter_matrix = LETTER(argletter, color, argx, argy, arg_group)

    # SCREEN.blit(letter_matrix.image, letter_matrix.rect)
    return letter_matrix
groups = []
groups_lists = []


testtttgroup = pg.sprite.Group()
#-----цикл создания столбцов букв
speed_letters = 3
for j in range(len(letters_x)):... #в range написано количество столбцов
    #----------------------------
    # let_group = pg.sprite.Group()
    #
    # #создать новый список?
    # new_let_y = letters_y[rnd.randint(1, 5):rnd.randint(6, len(letters_y))]
    #
    # #[-22, -44, -66, -88, -110, -132]
    # for i in range(len(new_let_y)): # в range количество букв в столбце
    #     create_letter(rnd.choice(katakana), letters_x[j], new_let_y[i], green, speed_letters, let_group)
    # groups.append(let_group)
    # groups_lists.append([i for i in let_group])
    # ----------------------------
all_groups_elements = [j for i in groups_lists for j in i]

# current_group = groups[0]

#------------------------
new_group = pg.sprite.Group()
y = 500
x = 500
let = rnd.choice(katakana)
letters_all = [LETTER(x, _, rnd.choice(katakana), [0,255,0], SCREEN) for _ in letters_y]

all_columns = []
def create_symbols():
    for i in letters_x:
        column = []
        for j in letters_y[rnd.randint(1,5):rnd.randint(6, len(letters_y))]:
            let_ex = LETTER(i, j, rnd.choice(katakana), [0, 255, 0], SCREEN)
            column.append(let_ex)
        all_columns.append(column)
        print(len(column))
create_symbols()


print(all_columns)

#создать список ^^
while runGame:
    SCREEN.fill([0,0,0])
    clock.tick(FPS)
    # [_.update() for _ in ALLLLLL]
    # for i in ALLLLLL:
    #     i.y += 1
    # [SCREEN.blit(_.letter, [_.x, _.y]) for _ in ALLLLLL]
    for i in all_columns:
        for j in i:
            SCREEN.blit(j.letter, [j.x, j.y])
            j.update()

    #переписать код в другом документа через спрайты

    # for i in ALLLLLL:

    # [i.update() for i in ALLLLLL]
    # for j in letters_x:
    #     for i in letters_y:
    #         if interval == 20:
    #             let = rnd.choice(katakana)
    #         LT = LETTER(j, i, let, green, SCREEN)
    #         SCREEN.blit(LT.letter, [LT.x, LT.y])
    #
    # letters_y = list(map(lambda item: item + 1, letters_y))
    # all_symbols = []
    # for i in letters_y:
    #     letters_alle = LETTER(x, i, let, [0, 255, 0], SCREEN)
    #     all_symbols.append(letters_alle)
    # [SCREEN.blit(i.letter, [i.x, i.y]) for i in all_symbols]
    # if len(all_symbols) == letters_y:
    #     all_symbols.clear()
    #
    # for i in letters_y:
    #     i+= 1


    # letter_ex.surf.blit(letter_ex.letter, [letter_ex.x, letter_ex .y])
    # letter.surf.blit()
    # for i in rev_down_letters_y:
    #     letter.update(x, i)
    # x += 1
    # interval = rnd.randint(5, 30)
    # if pg.time.get_ticks() % interval == 0:
    #     let = rnd.choice(katakana)
    #
    # letter = pg.font.SysFont('pingfang', 24).render(let, True, green)
    # SCREEN.blit(letter, [500, 500])
    # x += 1
#--------------------------------------
    # основной цикл
    # for i in groups_lists:
    #
    #
    #     #     if pg.time.get_ticks() % rnd.randint(5,30) == 0:
    #     #         i.
    #     current_group = groups[groups_lists.index(i)]
    #     # print(f'group №{groups_lists.index(i)}  {len(current_group)}')
    #     if i[-1].rect.centery >= rnd.randint(100, 500):
    #
    #         for j in range(rnd.randrange(3, len(letters_y), 1)):
    #             create_letter(rnd.choice(katakana),i[-1].rect.centerx, letters_y[j], green, i[-1].speed, current_group)
    #         i.clear()
    #         current_list_group = [sym for sym in current_group]
    #         [i.append(elem) for elem in current_list_group]




    # [i.draw(SCREEN) for i in groups]  # !!???
    # [i.update() for i in groups]
# --------------------------------------
    # for GL in groups_lists:
    #     Gl_group = GL[0].group
    #     LGL = len(GL) - 1
    #     GL.clear()
    #     for _ in range(LGL):
    #         llet_test = LETTER(rnd.choice(katakana), [255,0,0], letters_x[groups_lists.index(GL)], letters_y[_], Gl_group, speed_letters)
    #         GL.insert(_, llet_test)



    # [new_group.add(i) for i in all_groups_elements]
    # new_group.draw(SCREEN)
    # new_group.update()
    # [SCREEN.blit(i.image, i.rect) for i in all_groups_elements]
    # [i.update() for i in all_groups_elements]
    y += 1
    [sys.exit() for _ in pg.event.get() if _.type == pg.QUIT]
    pg.display.update()





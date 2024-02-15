import pygame as pg
import random as rnd
import sys
from rocket import Rocket
from ball import Ball
from window_tennis import size_window
from SPORE import sp
pg.init()
screen = pg.display.set_mode(size_window())
pg.display.set_caption('TENNIS')

#vars
red, white, black = [255, 0, 0], [255, 255, 255], [0, 0, 0]
right, left, up, down = pg.K_d, pg.K_a, pg.K_w, pg.K_s
clock = pg.time.Clock()
runGame = True
FPS = 144
#objects
rocket_user = Rocket(size_window()[0] // 2, size_window()[1] - 100, 'OB.png')
rocket_computer = Rocket(size_window()[0] // 2, 100, 'OB.png')




balls = pg.sprite.Group()

ball_tennis  = Ball(size_window()[0] // 2, 500, 'OB.png', balls)
print(balls)
def make_balls(performance):
    if performance:
        ball_tennis = Ball(size_window()[0] // 2, 500, 'OB.png', balls)
        return ball_tennis
    else:
        ...


speed = 7
SCALE_user, SCALE_computer = 0, 0


def make_scale(arg_scale):
    SCALE_FONT = pg.font.SysFont('applegothic', 36)\
                                .render(f'{arg_scale}', True, [255, 255, 255])
    return SCALE_FONT
speed_op, speed_stop = 7, 0
elem, amplitude = None, 10





while runGame:
    #objects sides
    computer_TL, user_TL = rocket_computer.rect.topleft, rocket_user.rect.topleft
    computer_TR, user_TR = rocket_computer.rect.topright, rocket_user.rect.topright
    computer_BL, user_BL = rocket_computer.rect.bottomleft, rocket_user.rect.bottomleft
    computer_BR, user_BR = rocket_computer.rect.bottomright, rocket_user.rect.bottomright

    def male_lines(side1, side2):
        return [i for i in range(side1, side2)]


    clock.tick(144)
    screen.fill(black)

    keys = pg.key.get_pressed()
    for events in pg.event.get():
        if events.type == pg.QUIT:
            sys.exit()

    if keys[right]:
        rocket_user.update(speed)

    elif keys[left]:

        rocket_user.update(-speed)


    def rebound(rocket_point_1, rocket_point_2, x_or_y, side, player):
        global SCALE_computer, SCALE_user
        for i in male_lines(rocket_point_1[x_or_y], rocket_point_2[x_or_y]):
            if x_or_y == 0:
                if ball_tennis.rect.collidepoint(i, rocket_point_1[1]):
                    ball_tennis.update(side, player)
                    if player == 'C':
                        SCALE_computer += 1
                if ball_tennis.rect.collidepoint(rocket_point_1[0], i):
                    ball_tennis.update(side, player)

    params_side_computer = [[computer_TL, computer_TR, 0, 'top', 'C'],
                            [computer_BL, computer_BR, 0, 'bot', 'C'],
                            [computer_TL, computer_BL, 1, 'left', 'C'],
                            [computer_TR, computer_BR, 1, 'right', 'C']]

    params_side_user = [[user_TL, user_TR, 0, 'top', 'U'],
                        [user_BL, user_BR, 0, 'bot', 'U'],
                        [user_TL, user_BL, 1, 'left', 'U'],
                        [user_TR, user_BR, 1, 'right', 'U']]

    for i in params_side_computer:
        rebound(*i)
    for j in params_side_user:
        rebound(*j)

    ball_tennis.update()

    if ball_tennis.rect.centery <= 500:
        if ball_tennis.rect.centerx > rocket_computer.rect.centerx:
            rocket_computer.rect.centerx += speed_op
            if rocket_computer.rect.centerx >= ball_tennis.rect.centerx:
                rocket_computer.rect.centerx += speed_stop
        elif ball_tennis.rect.centerx < rocket_computer.rect.centerx:
            rocket_computer.rect.centerx -= speed_op
            if rocket_computer.rect.centerx <= ball_tennis.rect.centerx:
                rocket_computer.rect.centerx +=speed_stop

    # if ball_tennis.rect.centerx < rocket_computer.rect.centerx:
    #     print(True)

    screen.blit(rocket_user.image, rocket_user.rect)
    screen.blit(rocket_computer.image, rocket_computer.rect)
    screen.blit(ball_tennis.image, ball_tennis.rect)

    screen.blit(make_scale(SCALE_user), [950, 750])
    screen.blit(make_scale(SCALE_computer), [250, 10])



    balls.draw(screen)
    balls.update()



    if ball_tennis.var == elem:
        ball_tennis.var_balls = True
    if ball_tennis.var %amplitude == 0 and ball_tennis.var !=0 and ball_tennis.var_balls == True:
        make_balls(True)
        elem = ball_tennis.var + amplitude #20 это нужно для следующего появления шарика, чтобы он появлялся не постоянно,
                                            #а каждые 10(amplitude) изменений переменной ball_tennis.var
        ball_tennis.var_balls = False



    pg.display.update()
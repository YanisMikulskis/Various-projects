import pygame as pg
import sys
from bottles import BOTTLE
import random as rnd
from hero import EGOR
pg.init()
pg.time.set_timer(pg.USEREVENT, 200)
general_window = [1000, 1000]
screen = pg.display.set_mode(general_window)
pg.display.set_caption('ЕГОР И ВОДКА')

# vars
clock = pg.time.Clock()
FPS = 144
runGame = True
left, right, up, down, jump = pg.K_a, pg.K_d, pg.K_w, pg.K_s, pg.K_SPACE
black, white, red = [0, 0, 0], [255, 255, 255], [255, 0, 0]
motion_for_egor = None


bottles_GGG = pg.sprite.Group()
alcohol = ['VODKA.png', '5 OZER.png']
def make_bottles_G():
    x, y = rnd.randint(1, 900), -100
    alco = rnd.choice(alcohol)
    bottle = BOTTLE(x, y, alco, bottles_GGG)
    return bottle

egor = EGOR(500, 800, 'EGOR_MALININ.png')
SCALE = 0
background = pg.image.load('BG.jpeg').convert_alpha()
motion_REVERSE = False

# fonts_scale = pg.font.SysFont('applegothic', 72)
def press_scale(arg_scale):
    text_scale = pg.font.SysFont('applegothic', 72)\
                            .render(f'{arg_scale}', True, [255,255,255])
    return text_scale
while runGame:
    screen.blit(background, [0, 0])

    clock.tick(FPS)
    keys = pg.key.get_pressed()

    def collide_bottle():
        # global SCALE
        def _ega(egor_side):
            _side = pg.transform.scale(egor.image, [egor.image.get_width(), egor.image.get_height() // 10])\
                .get_rect(bottomleft=egor_side)
            return _side
        for i in bottles_GGG:
            def side(cord_side):
                side_bottle = pg.transform.scale(i.image, [i.image.get_width(), i.image.get_height()//4])\
                         .get_rect(topleft=cord_side)
                return side_bottle
            #(верхний код после начала цикла) для отлетания Егора от ВЕРХА бутылки, создадим
            # новый прямоугольник, который будет находиться в спрайте BOTTLE,
            # но будет тонким по высоте, чтобы являться верхним "полом", поверхностью,
            # на которую призеляется егор, # а остальные стороны в свою очередь
            # игнорируют столкновения.Тоже самое делаем для спрайта Егор, чтобы он отскакивал только нижней частью
            if _ega(egor.rect.bottomleft).colliderect(side(i.rect.topleft)) and not egor.jump_cof:
                param()
                egor.update()


    def param():
        global egor
        egor = EGOR(egor.rect.centerx, egor.rect.centery, 'EGOR_MALININ.png')

    def clean_win():
        screen.fill(black)

    def group_methods():
        bottles_GGG.draw(screen)
        bottles_GGG.update(True, egor.speed_arg)

    def stop_group():
        bottles_GGG.draw(screen)
        bottles_GGG.update(False)
    for events in pg.event.get():
        if events.type == pg.QUIT or egor.rect.top > 1000:
            sys.exit()
        if events.type == pg.KEYDOWN:
            if events.key == jump:
                param()
                motion_for_egor = True
            if events.key == left:
                motion_REVERSE = 1
            if events.key == right:
                motion_REVERSE = 0
        elif events.type == pg.USEREVENT and egor.rect.top <= 400:
            if len(bottles_GGG) < 8:
                make_bottles_G()
    if motion_for_egor:
        egor.update()
        if egor.rect.top <= 400:
            SCALE+=1
            group_methods()
        else:
            stop_group()
    if keys[right]: egor.rect.right += 5
    elif keys[left]:egor.rect.left -= 5

    if motion_REVERSE:
        egor.image_reverse = pg.transform.flip(egor.image, True, False)
        screen.blit(egor.image_reverse, egor.rect)

    elif not motion_REVERSE: screen.blit(egor.image, egor.rect)

    if egor.rect.right < 0: egor.rect.left = general_window[0]
    elif egor.rect.left > general_window[0]: egor.rect.right = 0

    screen.blit(press_scale(SCALE), [100, 100])
    collide_bottle()

    pg.display.update()

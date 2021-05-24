import pygame as pg
from pygame.constants import K_ESCAPE
from pygame.draw import rect
import module_ship
from module_sky import Skys
import module_bullet
import module_meteor


pg.init()
pg.time.set_timer(pg.USEREVENT, 250)

# экран
W = 1000
H = 570
win = pg.display.set_mode((W, H))
win_size = 700
background_color = (255, 255, 255)

# FPS
clock = pg.time.Clock()
FPS = 60
running = True

score = pg.transform.scale(pg.image.load('image/score.png'), (100, 100))
shrift_score = pg.font.SysFont('arial', 30)

shrift_menu = pg.font.SysFont('arial', 40)
red = (255, 0, 0)
module_bullet.fires (module_bullet.group_bullet)
module_meteor.fly_meteors(module_meteor.group_meteor)

# menu
def draw_text(text, font, color, frame, x, y):
    textobj = font.render(text, 1, color)
    textect = textobj.get_rect()
    textect.topleft = (x, y)
    frame.blit(textobj, textect)

menu_color = (0, 0, 0)

def menu (win):
    running = True
    while running:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        win.fill(menu_color)
        draw_text('Игра "Shoot em up", для начала игры нажми Esp', shrift_menu, red, win, 150, 320)
        pg.display.update()

# главный цикл
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.USEREVENT:
            module_bullet.fires (module_bullet.group_bullet)
            module_meteor.fly_meteors(module_meteor.group_meteor)
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                menu (win)

    running = module_ship.collideShip_Meteorit()
    
# объявления    
    win.blit(Skys(W, H).image, (0, 0))
    
    win.blit(score, (900, -30))
    score_text =  shrift_score.render(str(module_meteor.game_score), 1, (94, 138, 14))
    win.blit(score_text, (920, 15))
    
    win.blit (module_ship.ship.image, (module_ship.ship.rect.x, module_ship.ship.rect.y))
    module_ship.Ships.update(module_ship.ship)
    
    module_bullet.group_bullet.draw(win)
    module_meteor.group_meteor.draw(win)
    module_meteor.collideBullet_Meteorit()
    
    pg.display.update()

    clock.tick(FPS)
    
    module_bullet.group_bullet.update(module_ship.ship.rect.x, module_ship.ship.rect.y)
    module_meteor.group_meteor.update()


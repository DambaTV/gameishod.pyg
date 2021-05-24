import pygame as pg
import module_bullet
from module_meteor import group_meteor

class Ships(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('image/ship.png')
        self.image = pg.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 10
        
    def update (self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a] and self.rect.x > -100:
            self.rect.x -= self.speed
        elif keys[pg.K_d] and self.rect.x < 900:
            self.rect.x += self.speed
        
ship = Ships(550, 440)

running = True
def collideShip_Meteorit():
    global running
    for meteorit in group_meteor:
        if meteorit.rect.collidepoint (ship.rect.center):
            running = False
    return running    











# from module_load import load_image

# ship = load_image('ship.png')

# x = 550
# y = 500
# SPEED = 10
    
# def user():    
#     global x, SPEED
#     keys = pg.key.get_pressed()
#     if keys[pg.K_a] and x > -50:
#         x -= SPEED
#     elif keys[pg.K_d] and x < 1150:
#         x += SPEED
    
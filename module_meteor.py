import pygame as pg
import module_ship
import module_bullet
from random import randint

class Meteors(pg.sprite.Sprite):
    def __init__(self, x, y, speed, meteor_surf, score, group_meteor):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(meteor_surf, (60, 60))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
        self.score = score
        self.add(group_meteor)

    def update (self):
        if self.rect.x < 0 or self.rect.x > 1200 or self.rect.y > 700:
            self.kill()
        else:
            self.rect.x += self.speed
            self.rect.y += self.speed

meteor_data = ({'path': 'meteor mini.png', 'score': 100},
               {'path': 'meteor.png', 'score': 50})
meteor_surf = [pg.image.load('image/' + data['path']) for data in meteor_data]

def fly_meteors (group):
    indx = randint(0, len(meteor_surf) - 1)
    x = randint(-300, 900)
    if x < 100:
        x = 0
        y = randint(1, 600)
    else:
        y = 0
    speed = randint(1, 5)
    
    return Meteors(x, y, speed, meteor_surf[indx], meteor_data[indx] ['score'], group)

group_meteor = pg.sprite.Group()

game_score = 0

def collideBullet_Meteorit():
    global game_score
    for bullet in module_bullet.group_bullet:
        for meteorit in group_meteor:
            if meteorit.rect.collidepoint(bullet.rect.center):
                game_score += meteorit.score
                bullet.kill()
                meteorit.kill()
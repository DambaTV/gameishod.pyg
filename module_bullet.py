import pygame as pg
import module_ship

class Bullets (pg.sprite.Sprite):
    def __init__(self, x, y, surf, group):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(surf, (200, 200))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.fire = False
        self.speed_shoot = 10
        self.add(group)

    def update (self, x, y):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.fire = True
        if self.fire and self.rect.y > -50:
            self.rect.y -= self.speed_shoot
        else:
            self.kill()

bullet_image = 'pixil-frame-ship2.png'
bullet_surf = pg.image.load('image/' + bullet_image)

def fires (group):
    return Bullets(module_ship.ship.rect.x, module_ship.ship.rect.y, bullet_surf, group)

group_bullet = pg.sprite.Group()

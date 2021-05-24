import pygame as pg

class Skys(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('image/space_2.png')
        self.image = pg.transform.scale(self.image, (x, y))
        self.rect = self.image.get_rect(topleft=(0, 0))




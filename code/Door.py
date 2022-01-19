import pygame as pg
pg.init()

doorW = 40
doorH = 80

class Door(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("../IMAGE_GAME/IMAGE_MAP/door20.png")
        self.image = pg.transform.scale(self.image, (doorW, doorH))
        # self.image.fill(pg.Color(PLATFORM_COLOR))
        self.rect = pg.Rect(x, y, doorW, doorH)



class Key(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("../IMAGE_GAME/IMAGE_MAP/KEY.png")
        self.image = pg.transform.scale(self.image, (15, 15))
        # self.image.fill(pg.Color(PLATFORM_COLOR))
        self.rect = pg.Rect(x, y, 15, 15)
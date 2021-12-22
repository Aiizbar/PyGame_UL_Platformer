import pygame as pg
pg.init()



ENEMY_WIDTH = 40
ENEMY_HEIGHT = 50



class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pg.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
        self.image = pg.image.load("../IMAGE_GAME/IMAGE_HERO_D/mushrum.png")
        self.image = pg.transform.scale(self.image, (40, 50))
        # self.image = self.image.convert_alpha()
        self.rect = pg.Rect(x, y, ENEMY_WIDTH, ENEMY_HEIGHT)
        size = (800, 500)
        self.screen = pg.display.set_mode(size)

    # def spavn(self, x, y):
    #     self.image = pg.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
    #     self.image = pg.image.load("../IMAGE_GAME/IMAGE_HERO_D/mushrum.jpg")
    #     self.rect = pg.Rect(x, y, ENEMY_WIDTH, ENEMY_HEIGHT)

    def movi_enemy(self):
        pass

    def visor(self):
        pass

    def attack(self):
        pass

    def render(self):
        self.screen.blit(self.image, (self.x, self.y))

import pygame as pg
pg.init()



ENEMY_WIDTH = 40
ENEMY_HEIGHT = 50



class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        # переменные для предвижения
        self.x_enemy = x
        self.y_enemy = y
        self.speed_enemy = 3
        # создание спрайтов для отображения
        self.rect = pg.Rect(self.x_enemy, self.y_enemy, ENEMY_WIDTH, ENEMY_HEIGHT)
        self.image = pg.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
        self.image = pg.image.load("../IMAGE_GAME/IMAGE_HERO_D/anonimus1.png")
        self.image = pg.transform.scale(self.image, (40, 50))
        self.image = self.image.convert_alpha()
        # print(self.image, self.rect, "init")

    def spavn(self, x, y):
        pass
        # переменные для предвижения
        # self.x_enemy = x
        # self.y_enemy = y
        # self.speed_enemy = 3
        # # создание спрайтов для отображения
        # self.rect = pg.Rect(self.x_enemy, self.y_enemy, ENEMY_WIDTH, ENEMY_HEIGHT)
        # self.image = pg.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
        # self.image = pg.image.load("../IMAGE_GAME/IMAGE_HERO_D/mushrum.png")
        # self.image = pg.transform.scale(self.image, (40, 50))
        # self.image = self.image.convert_alpha()
        # print(self.image, self.rect, "init")

    def movi_enemy(self):
        self.x_enemy += self.speed_enemy

    def visor(self):
        pass

    def attack(self):
        pass


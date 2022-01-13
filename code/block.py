import pygame as pg
import pygame.draw
from Settings import *

pg.init()
# PLATFORM_WIDTH = 50
# PLATFORM_HEIGHT = 50
PLATFORM_COLOR = "#FF6262"



class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pg.sprite.Sprite.__init__(self)
        # self.image = pg.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = pg.image.load("../IMAGE_GAME/IMAGE_MAP/set.png")
        self.image = pygame.transform.scale(self.image, (PLATFORM_HEIGHT, PLATFORM_WIDTH))
        # self.image.fill(pg.Color(PLATFORM_COLOR))
        self.rect = pg.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT - 5)

    def drow(self):
        # Platform
        pygame.draw.rect(screen,  (255, 0, 0), (self.x, self.y, PLATFORM_WIDTH, PLATFORM_HEIGHT - 5))
        # pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y + 10, 5, 10))
        # pygame.draw.rect(screen, (255, 0, 0), (self.x + 20, self.y + 10, 5, 10))




class PP_Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("../IMAGE_GAME/IMAGE_MAP/TREE.png")
        self.image = self.image
        # self.image.fill(pg.Color(PLATFORM_COLOR))
        self.rect = pg.Rect(x, y - 5, PLATFORM_WIDTH, PLATFORM_HEIGHT - 10)



class Left_Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("../IMAGE_GAME/IMAGE_MAP/TREE.png")
        self.image = self.image
        # self.image.fill(pg.Color(PLATFORM_COLOR))
        self.rect = pg.Rect(x, y + (10), 5 * 2, 10 * 2)



class Right_Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("../IMAGE_GAME/IMAGE_MAP/TREE.png")
        self.image = self.image
        self.rect = pg.Rect(x + (20 * 2), y + (10), 5 * 2, 10 * 2)



class Up_Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("../IMAGE_GAME/IMAGE_MAP/set.png")
        self.image = self.image
        self.rect = pg.Rect(x + 7 * 2, y + 2 * 2, PLATFORM_WIDTH - 7, 5)

class Down_Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("../IMAGE_GAME/IMAGE_MAP/set.png")
        self.image = pygame.transform.scale(self.image, (PLATFORM_HEIGHT, PLATFORM_WIDTH))
        # self.image.fill(pg.Color(PLATFORM_COLOR))
        self.rect = pg.Rect(x, y, PLATFORM_WIDTH, 1)
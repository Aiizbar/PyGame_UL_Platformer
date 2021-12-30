import pygame as pg
import pygame.draw

pg.init()
PLATFORM_WIDTH = 25
PLATFORM_HEIGHT = 25
PLATFORM_COLOR = "#FF6262"



class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        # self.image = pg.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = pg.image.load("../IMAGE_GAME/IMAGE_MAP/TREE.png")
        self.image = self.image
        # self.image.fill(pg.Color(PLATFORM_COLOR))
        self.rect = pg.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)




class Left_Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("../IMAGE_GAME/IMAGE_MAP/TREE.png")
        self.image = self.image
        # self.image.fill(pg.Color(PLATFORM_COLOR))
        self.rect = pg.Rect(x, y - 1, PLATFORM_WIDTH - 20, PLATFORM_HEIGHT - 1)
        pygame.draw.rect(screen, (0, 0, 0), ())



class Right_Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("../IMAGE_GAME/IMAGE_MAP/TREE.png")
        self.image = self.image
        # self.image.fill(pg.Color(PLATFORM_COLOR))
        self.rect = pg.Rect(x + 20, y - 1, PLATFORM_WIDTH - 20, PLATFORM_HEIGHT - 1)
        pygame.draw.rect(screen, (0, 0, 0), ())



class Up_Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("../IMAGE_GAME/IMAGE_MAP/TREE.png")
        self.image = self.image
        # self.image.fill(pg.Color(PLATFORM_COLOR))
        self.rect = pg.Rect(x, y - PLATFORM_HEIGHT + 1, PLATFORM_WIDTH, 1)
        pygame.draw.rect(screen, (0, 0, 0), ())

class Down_Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("../IMAGE_GAME/IMAGE_MAP/TREE.png")
        self.image = self.image
        # self.image.fill(pg.Color(PLATFORM_COLOR))
        self.rect = pg.Rect(x, y, PLATFORM_WIDTH, 1)
        pygame.draw.rect(screen, (0, 0, 0), ())
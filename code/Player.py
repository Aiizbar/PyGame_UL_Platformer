import pygame



class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/anonimus1.png')
        self.rect = pygame.Rect(400, 250, 40, 50)
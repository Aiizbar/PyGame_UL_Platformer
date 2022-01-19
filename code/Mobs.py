import pygame
from Settings import *
import pygame as pg
import sys



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/GG/ggStay.png')
        self.rect = pygame.Rect(400, 250, 40, 50)
        self.image_hero = pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/GG/ggStay.png')
        self.image_hero = pygame.transform.scale(self.image_hero, (30, 50))

        self.x_hero = self.wall_x = 400
        self.y_hero = self.wall_y = 250
        self.speed_left = 5
        self.speed_right = 5
        # self.image_hero_list = [
        #     pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/GG/ggStep1.png'),
        #     pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/GG/ggStep2.png')]
        # self.image_hero_list[0] = pygame.transform.scale(self.image_hero_list[0], (30, 50))
        # self.image_hero_list[1] = pygame.transform.scale(self.image_hero_list[1], (30, 50))

        self.image_hero_list_right = [
            pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/GG/ggStep1.png'),
            pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/GG/ggStep2.png'),
            pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/GG/ggStep3.png'),
            pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/GG/ggStep4.png'),
            pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/GG/ggStep5.png'),
            pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/GG/ggStep6.png'),
            pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/GG/ggStep7.png')]
        for i in range(len(self.image_hero_list_right)):
            self.image_hero_list_right[i] = pygame.transform.scale(self.image_hero_list_right[i], (30, 50))

        self.image_hero_list_left = [
            pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/GGLeft/ggStep1.png'),
            pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/GGLeft/ggStep2.png'),
            pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/GGLeft/ggStep3.png'),
            pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/GGLeft/ggStep4.png'),
            pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/GGLeft/ggStep5.png'),
            pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/GGLeft/ggStep6.png'),
            pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/GGLeft/ggStep7.png')]
        for i in range(len(self.image_hero_list_right)):
            self.image_hero_list_left[i] = pygame.transform.scale(self.image_hero_list_left[i], (30, 50))

        self.count = 0
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # определяющая на земле мы или нет
        self.gravity(True)
        self.jump_time = 0
        self.stop_jump = True
        self.right = False
        self.left = False
        self.Hitpoints = 140

        self.animation_range_right = 0
        self.animation_range_left = 0

    def move(self, keys):
        if keys[pygame.K_ESCAPE]:
            sys.exit()
        if keys[pygame.K_SPACE]:
            if self.onGround:
                self.stop_jump = False
        if keys[pygame.K_d]:
            self.x_hero += self.speed_right
            self.animation_right()
        elif keys[pygame.K_a]:
            self.x_hero -= self.speed_right
            self.animation_left()

    def animation_right(self):
        if self.animation_range_right >= 14:
            self.animation_range_right = 0
        self.image_hero = self.image_hero_list_right[self.animation_range_right // 2]
        self.animation_range_right += 1

    def animation_left(self):
        if self.animation_range_left >= 14:
            self.animation_range_left = 0
        self.image_hero = self.image_hero_list_left[self.animation_range_left // 2]
        self.animation_range_left += 1

    def gravity(self, lol):
        GRAVITY = 0.35  # ускорение свободного падения
        if self.onGround == False and lol == True:
            self.yvel += GRAVITY
            self.y_hero += self.yvel

    def update(self, platforms, left, right, up, pp, key):
        self.rect = pygame.Rect(700, self.y_hero, 40, 50)
        if pygame.sprite.spritecollideany(self, platforms):
            self.onGround = True
            self.yvel = 0
        if pygame.sprite.spritecollideany(self, left):
            self.x_hero -= 5
        if pygame.sprite.spritecollideany(self, right):
            self.x_hero += 5
        if pygame.sprite.spritecollideany(self, up):
            self.y_hero += 20
        if not pygame.sprite.spritecollideany(self, platforms):
            # если есть пересечени с платформой останавливаем падение
            self.onGround = False
        if pygame.sprite.spritecollideany(self, pp):
            self.y_hero -= 1

    def jump(self, stop):
        if stop == True and self.stop_jump == False:
            self.y_hero -= 10
            self.jump_time += 1
            if self.jump_time == 15:
                self.jump_time = 0
                self.stop_jump = True


class Attack_Boss(pg.sprite.Sprite):
    def __init__(self, x, y, v, z):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((v, 10))
        self.image = pg.image.load("../IMAGE_GAME/IMAGE_HERO_D/Non.png")
        self.image = self.image
        self.rect = pg.Rect(x, y, v, z)
        pygame.draw.rect(screen, (255, 255, 255), (x, y, v, z))


BOSS_W = 250
BOSS_H = 150
player = Player()


class Borov(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.x_boss = x
        self.y_boss = y

        self.speed_step = 2
        self.speed_push = 7

        self.rect = pg.Rect(self.x_boss, self.y_boss, BOSS_W, BOSS_H)
        self.image_b = pg.image.load("../IMAGE_GAME/IMAGE_HERO_D/Inoske.jpg")
        self.image_b = pg.transform.scale(self.image_b, (BOSS_W, BOSS_H))

        self.vizor = False

    def movi(self):
        pass

    def scanning(self):
        self.rect = pygame.Rect(700, player.y_hero, 30, 50)
        left_visor = Attack_Boss(self.x_boss - 800, self.y_boss + 120, 800, 20)
        right_visor = Attack_Boss(self.x_boss + 250, self.y_boss + 120, 800, 20)
        r = pygame.sprite.Group()
        r.add(right_visor)
        l = pygame.sprite.Group()
        l.add(left_visor)
        if pygame.sprite.spritecollideany(self, r):
            self.vizor = "Right"
        elif pygame.sprite.spritecollideany(self, l):
            self.vizor = "Left"
        else:
            self.vizor = "None"

    def attaks(self, gogogoGOOOOOOOOOOO):
        global x_bora
        if gogogoGOOOOOOOOOOO == "Right":
            x_bora += 10
            self.push()
        if gogogoGOOOOOOOOOOO == "Left":
            x_bora -= 10
            self.push()

    def walls(self):
        pass

    def push(self):
        global x_bora, y_bora
        self.rect = pygame.Rect(700, player.y_hero, 30, 50)
        GOOOOOOOOOOOOOOOD = Attack_Boss(x_bora, y_bora, BOSS_W, BOSS_H)
        FackingPUUUUUSH = pygame.sprite.Group()
        FackingPUUUUUSH.add(GOOOOOOOOOOOOOOOD)
        if pygame.sprite.spritecollideany(self, FackingPUUUUUSH):
            player.Hitpoints -= 100000

    def update(self):
        self.scanning()
        if self.vizor != "None":
            print("GOGOGOGOGO")
            self.attaks(self.vizor)
        self.walls()



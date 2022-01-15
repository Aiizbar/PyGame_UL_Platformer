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
        self.Hitpoints = 40

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


    # def render(self):
    #     if self.count >= 8:
    #         self.count = 0
    #     self.image_hero = self.image_hero_list[self.count // 4]
    #     self.count += 1

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
            # self.yvel = 0
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



import sys
from block import Platform
import pygame as pg
import pygame
import copy
pygame.init()



level = [
       "----------------------------------",
       "-                                -",
       "-                       --       -",
       "-                                -",
       "-            --                  -",
       "-                                -",
       "--                               -",
       "-                                -",
       "-                   ----     --- -",
       "-                                -",
       "--                               -",
       "-                                -",
       "-                            --- -",
       "-                    E           -",
       "-                                -",
       "-      ---                       -",
       "-                                -",
       "-   -------         ----         -",
       "-                                -",
       "-                         -      -",
       "-                            --  -",
       "-                                -",
       "-                                -",
       "----------------------------------"]



class Game:
    def __init__(self, size, screen):
        self.size = size
        self.g = 0
        self.screen = screen
        self.x_hero = self.wall_x = 40
        self.y_hero = self.wall_y = 40
        self.speed_left = 5
        self.speed_right = 5
        self.key_invent = False
        self.image_hero_list = [
            pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/anonimus1.png'),
            pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/anonimus2.png')]
        self.image_hero_list[0] = pygame.transform.scale(self.image_hero_list[0], (40, 50))
        self.image_hero_list[1] = pygame.transform.scale(self.image_hero_list[1], (40, 50))

        self.count = 0
        self.coord_key = [600, 600]
        self.coord_padlock = [size[0] - 50, size[1] // 2 - 100, 50, 150]
        self.key_finally = (1220, 10)
        self.speed_key = 10
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # определяющая на земле мы или нет
        self.gravity(True)
        self.jump_time = 0
        self.stop_jump = True
        self.right = False
        self.left = False
        self.Hitpoints = 40
        self.push_range = 0
        self.push_true = False
        self.push_nap = "None"

    def move(self, keys):
        if keys[pygame.K_ESCAPE]:
            sys.exit()
        if keys[pygame.K_SPACE]:
            if self.onGround:
                self.stop_jump = False
        if keys[pygame.K_d]:
            self.x_hero += self.speed_left
            self.left = True
        elif keys[pygame.K_a]:
            self.x_hero -= self.speed_right
            self.right = False

    def render(self):
        if self.count >= 8:
            self.count = 0
        self.image_hero = self.image_hero_list[self.count // 4]
        self.count += 1

    def key(self):
        self.rect1 = (*self.coord_key, 50, 30)
        self.rect2 = (self.x_hero, self.y_hero, 55, 129)
        if self.does_collide():
            self.g = 1
        if self.g:
            if self.coord_key[0] < self.key_finally[0]:
                self.coord_key[0] += self.speed_key
            elif self.coord_key[0] > self.key_finally[0]:
                self.coord_key[0] -= self.speed_key
            if self.coord_key[1] < self.key_finally[1]:
                self.coord_key[1] += self.speed_key
            elif self.coord_key[1] > self.key_finally[1]:
                self.coord_key[1] -= self.speed_key
            else:
                self.key_invent = True

    def exit(self):
        self.rect1 = self.coord_padlock
        self.rect2 = (self.x_hero, self.y_hero, 55, 129)
        if self.does_collide():
            sys.exit()

    def does_collide(self):
        if self.rect1[0] < self.rect2[0] + self.rect2[2] and self.rect1[0] + self.rect1[2] > self.rect2[0] \
                and self.rect1[1] < self.rect2[1] + self.rect2[3] and self.rect1[3] + self.rect1[1] > self.rect2[1]:
            return True
        else:
            return False

    def gravity(self, lol):
        GRAVITY = 0.35  # ускорение свободного падения
        if self.onGround == False and lol == True:
            self.yvel += GRAVITY
            self.y_hero += self.yvel

    def update(self, e):
        self.rect = pygame.Rect(self.x_hero, self.y_hero, 40, 50)
        if not pygame.sprite.spritecollideany(self, e):
            # если нет столкновения с платформой - падаем вниз
            self.onGround = False
        else:
            # если есть пересечени с платформой остонавливаем падение
            self.onGround = True
            self.yvel = 1

    def jump(self, stop):
        if stop == True and self.stop_jump == False:
            self.y_hero -= 10
            self.jump_time += 1
            if self.jump_time == 15:
                self.jump_time = 0
                self.stop_jump = True

    def copy(self):
        self.xx_hero = copy.copy(self.x_hero)
        self.yy_hero = copy.copy(self.y_hero)




# pygame.mixer.music.load('../SOUNDS/sound_bg1.ogg')
# pygame.mixer.music.play()
t = 0
wight = 800
height = 500
size = (wight, height)
screen = pygame.display.set_mode(size)
bg = pygame.image.load('../IMAGE_GAME/IMAGE_MAP/MAP1.png').convert()
key = pygame.image.load('../IMAGE_GAME/IMAGE_MAP/KEY.png')
passage = pygame.image.load('../IMAGE_GAME/IMAGE_MAP/EXIT.png')
a = Game(size, screen)
clock = pygame.time.Clock()
run = 1
PLATFORM_WIDTH = 25
PLATFORM_HEIGHT = 25
PLATFORM_COLOR = "#FF6262"
entities = pygame.sprite.Group() # Все объекты-платформы
# platforms = []
x = y = 0
x_enemy = []
y_enemy = []

for row in level:  # вся строка
    for col in row:  # каждый символ
        if col == "-": # если платформа
            pf = Platform(x, y)
            entities.add(pf)
        elif col == "E":
            # opponent = Enemy(x, y)
            x_enemy.append(x)
            y_enemy.append(y)
            # adversary.add(opponent)
        x += PLATFORM_WIDTH
    y += PLATFORM_HEIGHT
    x = 0


class Attack(pg.sprite.Sprite):
    def __init__(self, x, y, v, z):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((v, 10))
        self.image = pg.image.load("../IMAGE_GAME/IMAGE_HERO_D/Non.png")
        self.image = self.image
        # self.image.fill(pg.Color(PLATFORM_COLOR))
        self.rect = pg.Rect(x, y + 10, v, z)
        pygame.draw.rect(screen, (255, 255, 255),
                         (x, y + 10, v, z))


ENEMY_WIDTH = 40
ENEMY_HEIGHT = 50



class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        # переменные для предвижения
        self.x_e = x
        self.y_e = y
        self.speed_enemy = 3
        # создание спрайтов для отображения
        self.rect = pg.Rect(self.x_e, self.y_e, ENEMY_WIDTH, ENEMY_HEIGHT)
        # self.image = pg.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
        self.image = pg.image.load("../IMAGE_GAME/IMAGE_HERO_D/anonimus1.png")
        self.image = pg.transform.scale(self.image, (40, 50))
        self.yvel = 5

    # def movi_enemy(self):
    #     # self.x_e += self.speed_enemy
    #     x_enemy[self.typ] += self.speed_enemy

    def visor(self):
        self.rect = pygame.Rect(a.x_hero, a.y_hero, 40, 50)
        R = pygame.sprite.Group()
        L = pygame.sprite.Group()
        left_visor = Attack(x_enemy[self.typ] - 60, y_enemy[self.typ], 60, 3)
        right_visor = Attack(x_enemy[self.typ] + 60, y_enemy[self.typ], 60, 3)
        R.add(right_visor)
        L.add(left_visor)
        if pygame.sprite.spritecollideany(self, R):
            self.direction = "Right"
        elif pygame.sprite.spritecollideany(self, L):
            self.direction = "Left"
        else:
            self.direction = "None"
        # print(self.direction)


    def attack(self, visa):
        self.rect = pygame.Rect(a.x_hero, a.y_hero, 40, 50)
        if visa == "Right":
            rect_Player = Attack(x_enemy[self.typ] + 30, y_enemy[self.typ], 30, 30)
            DD = pygame.sprite.Group()
            DD.add(rect_Player)
            if pygame.sprite.spritecollideany(self, DD):
                a.Hitpoints -= 10
                a.push_true = True
                a.push_nap = "Right"
        elif visa == "Left":
            rect_Player = Attack(x_enemy[self.typ] - 30, y_enemy[self.typ], 30, 30)
            DD = pygame.sprite.Group()
            DD.add(rect_Player)
            if pygame.sprite.spritecollideany(self, DD):
                a.Hitpoints -= 10
                a.push_true = True
                a.push_nap = "Left"

    def walls(self, e):
        self.rect = pygame.Rect(x_enemy[self.typ], y_enemy[self.typ], 40, 50)
        if not pygame.sprite.spritecollideany(self, e):
            # если нет столкновения с платформой - падаем вниз
            self.onGround = False
        else:
            # если есть пересечени с платформой остонавливаем падение
            self.onGround = True

    def gravity(self):
        if self.onGround == False:
            y_enemy[self.typ] += self.yvel

    def push_left(self):
        if a.push_range <= 10 and a.push_true == True and a.push_nap == "Left":
            a.push_range += 1
            a.x_hero -= 10
            if a.push_range == 10:
                a.push_range = 0
                a.push_true = False
                a.push_nap = "None"

    def push_right(self):
        if a.push_range <= 10 and a.push_true == True and a.push_nap == "Right":
            a.push_range += 1
            a.x_hero += 10
            if a.push_range == 10:
                a.push_range = 0
                a.push_true = False
                a.push_nap = "None"

    def update(self, i, wall):
        self.typ = i
        self.walls(wall)
        self.gravity()
        self.visor()
        if self.direction != "None":
            self.attack(self.direction) # говорим в какую сторону атаковать
        self.push_left()
        self.push_right()
        # self.movi_enemy()


for i in range(len(x_enemy)):
    opponent = Enemy(x_enemy[i], y_enemy[i])


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj, what):
        if what == "blocks":
            obj.rect.x -= self.dx
            obj.rect.y -= self.dy
        if what != "blocks":
            x_enemy[what] -= self.dx
            y_enemy[what] -= self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = a.x_hero - a.xx_hero
        self.dy = a.y_hero - a.yy_hero



class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = a.image_hero
        self.rect = pygame.Rect(pos_x, pos_y, 40, 50)

camera = Camera()
all_sprites = pg.sprite.Group()
while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = 0
        elif event.type == pygame.QUIT:
            run = 0
    a.render()
    if not a.key_invent:
        a.key()
    else:
        a.exit()
    a.copy()
    screen.blit(bg, (0, 0))
    screen.blit(key, (a.coord_key[0], a.coord_key[1]))
    screen.blit(passage, (size[0] - 50, size[1] // 2 - 100))
    keys = pygame.key.get_pressed()
    if 1 in keys:
        a.move(keys)
    all_sprites = pg.sprite.Group()

    # здесь передаем значение методу гравити и джамп для постоянной проверки на каждой итерации
    a.gravity(True)
    a.jump(True)
    # вывод на экран героя
    screen.blit(a.image_hero, (a.x_hero, a.y_hero))
    # обновление врагов и их вывод
    for i in range(len(x_enemy)):
        ene = Enemy(x_enemy[i], y_enemy[i])
        ene.update(i, entities)
        screen.blit(ene.image, (ene.x_e, ene.y_e))
        # добавление врагов в общую группу спрайтов
        # all_sprites.add(ene)
    # добавление платформ в общую группу
    all_sprites.add(entities)
    # создание спрайта ирока для работы с камерой
    player = Player(a.x_hero, a.y_hero)
    all_sprites.add(player)
    camera.update(player)  # центризируем камеру относительно персонажа
    for e in all_sprites:
        camera.apply(e, "blocks")
    for i in range(len(x_enemy)):
        ene = Enemy(x_enemy[i], y_enemy[i])
        camera.apply(ene, i)
    # обновление платформ и их вывод
    entities.draw(screen)
    a.update(entities)
    clock.tick(60)
    pygame.display.set_caption(f"{clock.get_fps(), a.Hitpoints}")
    pygame.display.update()
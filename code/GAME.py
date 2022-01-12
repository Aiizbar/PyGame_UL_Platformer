import sys
from block import *
from Settings import *
from Player import Player
from Door import Door
import pygame as pg
import pygame
import pygame_menu
import copy

pygame.init()


class Game:
    def __init__(self, size, screen):
        self.size = size
        self.screen = screen
        self.x_hero = self.wall_x = 400
        self.y_hero = self.wall_y = 250
        self.speed_left = 5
        self.speed_right = 5
        self.image_hero_list = [
            pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/anonimus1.png'),
            pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/anonimus2.png')]
        self.image_hero_list[0] = pygame.transform.scale(self.image_hero_list[0], (40, 50))
        self.image_hero_list[1] = pygame.transform.scale(self.image_hero_list[1], (40, 50))

        self.count = 0
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
        self.plats()
        self.ThisIsMap = 0

        #
    def plats(self):
        self.entities = pygame.sprite.Group()  # Все объекты-платформы
        self.Left_plat = pygame.sprite.Group()
        self.Right_plat = pygame.sprite.Group()
        self.Up_plat = pygame.sprite.Group()
        self.PP_plat = pygame.sprite.Group()
        self.ThisDoor = pygame.sprite.Group()

    def move(self, keys):
        if keys[pygame.K_ESCAPE]:
            sys.exit()
        if keys[pygame.K_SPACE]:
            if self.onGround:
                self.stop_jump = False
        if keys[pygame.K_d]:
            self.x_hero += self.speed_left
        elif keys[pygame.K_a]:
            self.x_hero -= self.speed_right

    def render(self):
        if self.count >= 8:
            self.count = 0
        self.image_hero = self.image_hero_list[self.count // 4]
        self.count += 1

    def gravity(self, lol):
        GRAVITY = 0.35  # ускорение свободного падения
        if self.onGround == False and lol == True:
            self.yvel += GRAVITY
            self.y_hero += self.yvel

    def update(self, platforms, left, right, up, pp):
        self.rect = pygame.Rect(aa, bb, 40, 50)
        if pygame.sprite.spritecollideany(self, platforms):
            self.onGround = True
            self.yvel = 0
        if pygame.sprite.spritecollideany(self, left):
            self.x_hero -= 5
        if pygame.sprite.spritecollideany(self, right):
            self.x_hero += 5
        if pygame.sprite.spritecollideany(self, up):
            self.y_hero += 10
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

    def copy(self):
        self.xx_hero = copy.copy(self.x_hero)
        self.yy_hero = copy.copy(self.y_hero)

    def IfNextLevel(self):
        self.rect = pygame.Rect(aa, bb, 40, 50)
        if HaveKey == True:
            if pygame.sprite.spritecollideany(self, a.ThisDoor):
                self.plats()
                self.ThisIsMap += 1
                level = open(f"../MAPS/{allMap[self.ThisIsMap]}", mode='r', encoding="utf-8").readlines()
                mapping(level)


a = Game(size, screen)
x_enemy = []
y_enemy = []

# entities = pygame.sprite.Group()  # Все объекты-платформы
# Left_plat = pygame.sprite.Group()
# Right_plat = pygame.sprite.Group()
# Up_plat = pygame.sprite.Group()
# PP_plat = pygame.sprite.Group()
# ThisDoor = pygame.sprite.Group()
def mapping(level):
    x = y = 0
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":  # если платформа
                pa = Platform(x, y)
                pl = Left_Platform(x, y)
                pr = Right_Platform(x, y)
                # pu = Up_Platform(x, y)
                pp = PP_Platform(x, y)
                a.entities.add(pa)
                a.Left_plat.add(pl)
                a.Right_plat.add(pr)
                # a.Up_plat.add(pu)
                a.PP_plat.add(pp)
            elif col == "_":
                pu = Up_Platform(x, y)
                a.Up_plat.add(pu)
            elif col == "E":
                # opponent = Enemy(x, y)
                x_enemy.append(x)
                y_enemy.append(y)
                # adversary.add(opponent)
            elif col == "D":
                nextLevel = Door(x, y)
                a.ThisDoor.add(nextLevel)
            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0
    # for i in range(len(x_enemy)):
    #     opponent = Enemy(x_enemy[i], y_enemy[i])

mapping(level)


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
        self.speed_enemy = 5
        # создание спрайтов для отображения
        self.rect = pg.Rect(self.x_e, self.y_e, ENEMY_WIDTH, ENEMY_HEIGHT)
        # self.image = pg.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
        self.image = pg.image.load("../IMAGE_GAME/IMAGE_HERO_D/DogStop.png")
        self.image = pg.transform.scale(self.image, (40, 50))
        self.yvel = 5

    def movi_enemy(self, where):
        # self.x_e += self.speed_enemy
        if where == "Right":
            x_enemy[self.typ] += self.speed_enemy
        elif where == "Left":
            x_enemy[self.typ] -= self.speed_enemy

    def visor(self):
        self.rect = pygame.Rect(aa, bb, 40, 50)
        R = pygame.sprite.Group()
        L = pygame.sprite.Group()
        left_visor = Attack(x_enemy[self.typ] - 120, y_enemy[self.typ], 120, 3)
        right_visor = Attack(x_enemy[self.typ] + 40, y_enemy[self.typ], 120, 3)
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
        self.rect = pygame.Rect(aa, bb, 40, 50)
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

    def walls(self, e, pp):
        self.rect = pygame.Rect(x_enemy[self.typ], y_enemy[self.typ], 40, 50)
        if not pygame.sprite.spritecollideany(self, e):
            # если нет столкновения с платформой - падаем вниз
            self.onGround = False
        else:
            # если есть пересечени с платформой остонавливаем падение
            self.onGround = True
        if pygame.sprite.spritecollideany(self, pp):
            y_enemy[self.typ] -= 1


    def gravity(self):
        if self.onGround == False:
            print("Падает враг!")
            y_enemy[self.typ] += self.yvel

    # def walls(self, i, platforms, left, right, up, pp):
    #     self.rect = pygame.Rect(aa, bb, 40, 50)
    #     if pygame.sprite.spritecollideany(self, platforms):
    #         self.onGround = True
    #     if pygame.sprite.spritecollideany(self, left):
    #         x_enemy[i] -= 5
    #     if pygame.sprite.spritecollideany(self, right):
    #         x_enemy[i] += 5
    #     # if pygame.sprite.spritecollideany(self, up):
    #     #     self.onGround = True
    #     #     self.yvel = 0
    #     if not pygame.sprite.spritecollideany(self, platforms):
    #         # если есть пересечени с платформой останавливаем падение
    #         self.onGround = False
    #     if pygame.sprite.spritecollideany(self, pp):
    #         y_enemy[i] -= 2

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

    def update(self, i, platforms, left, right, up, pp):
        self.typ = i
        self.walls(platforms, pp)
        self.gravity()
        self.visor()
        if self.direction != "None":
            self.attack(self.direction)  # говорим в какую сторону атаковать
            self.movi_enemy(self.direction)
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
            # if obj.rect.y >= 0:
                obj.rect.x -= self.dx
                obj.rect.y -= self.dy
            # else:
            #     obj.rect.x += self.dx
            #     obj.rect.y += self.dy
        if what != "blocks":
            x_enemy[what] -= self.dx
            y_enemy[what] -= self.dy

    # позиционировать камеру на объекте target
    def update(self):
        self.dx = (a.x_hero - a.xx_hero)
        self.dy = (a.y_hero - a.yy_hero)


# surface = pygame.display.set_mode((600, 400))
#
# def set_difficulty(value, difficulty):
#     # Do the job here !
#     pass
#
# def start_the_game():
#     run = True
#
# menu = pygame_menu.Menu('Welcome', 400, 300,
#                        theme=pygame_menu.themes.THEME_BLUE)
#
# # menu.add.text_input('Name :', default='John Doe')
# # menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
# menu.add.button('Play', start_the_game)
# menu.add.button('Quit', pygame_menu.events.EXIT)
# menu.mainloop(surface)


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
    a.copy()
    screen.blit(bg, (0, 0))
    # screen.blit(key, (a.coord_key[0], a.coord_key[1]))
    # screen.blit(passage, (size[0] - 50, size[1] // 2 - 100))
    keys = pygame.key.get_pressed()
    if 1 in keys:
        a.move(keys)
    all_sprites = pg.sprite.Group()

    # здесь передаем значение методу гравити и джамп для постоянной проверки на каждой итерации
    a.gravity(True)
    a.jump(True)
    # вывод на экран героя
    # screen.blit(a.image_hero, (a.x_hero, a.y_hero))
    screen.blit(a.image_hero, (400, 250))
    # обновление врагов и их вывод
    for i in range(len(x_enemy)):
        ene = Enemy(x_enemy[i], y_enemy[i])
        # ene.walls(i, a.entities, a.Left_plat, a.Right_plat, a.Up_plat, a.PP_plat)
        ene.update(i, a.entities, a.Left_plat, a.Right_plat, a.Up_plat, a.PP_plat)
        screen.blit(ene.image, (ene.x_e, ene.y_e))
        # добавление врагов в общую группу спрайтов
        # all_sprites.add(ene)

    # создание спрайта ирока для работы с камерой
    player = Player(a.x_hero, a.y_hero)
    # обновление платформ и их вывод
    a.entities.draw(screen)
    a.update(a.entities, a.Left_plat, a.Right_plat, a.Up_plat, a.PP_plat)
    a.ThisDoor.draw(screen)
    # a.Up_plat.draw(screen)
    # добавление всех спратов в общую группу
    all_sprites.add(player)
    all_sprites.add(a.entities)
    all_sprites.add(a.Left_plat)
    all_sprites.add(a.Right_plat)
    all_sprites.add(a.Up_plat)
    all_sprites.add(a.PP_plat)
    all_sprites.add(a.ThisDoor)
    camera.update()  # центризируем камеру относительно персонажа
    for e in all_sprites:
        camera.apply(e, "blocks")
    for i in range(len(x_enemy)):
        ene = Enemy(x_enemy[i], y_enemy[i])
        camera.apply(ene, i)

    # проверка есть ли ключ и столкновение с дверью
    a.IfNextLevel()

    clock.tick(60)
    pygame.display.set_caption(f"{int(clock.get_fps()), allMap[a.ThisIsMap]}")
    pygame.display.update()
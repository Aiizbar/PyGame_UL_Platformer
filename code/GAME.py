import pygame as pg
import pygame

W = 1400
H = 800
sc = pg.display.set_mode((W, H))
dog_surf = pg.image.load('../IMAGE_GAME/IMAGE_MAP/Loading_img.jpg')
dog_surf = pg.transform.scale(dog_surf, (1400, 800))
sc.blit(dog_surf, (0, 0))
pg.display.update()


import sys
from block import *
from Settings import *
from Mobs import *
from Death import death_menu
from Door import *
from Win import Win
import copy

pygame.init()


class Game:
    def __init__(self, size, screen):
        self.size = size
        self.screen = screen
        self.push_range = 0
        self.push_true = False
        self.push_nap = "None"
        self.plats()
        self.ThisIsMap = 0
        self.HaveKey = False
        self.deding = True
        self.ifBoss = False

    def plats(self):
        global x_enemy, y_enemy
        x_enemy = []
        y_enemy = []
        self.entities = pygame.sprite.Group()  # Все объекты-платформы
        self.Left_plat = pygame.sprite.Group()
        self.Right_plat = pygame.sprite.Group()
        self.Up_plat = pygame.sprite.Group()
        self.PP_plat = pygame.sprite.Group()
        self.ThisDoor = pygame.sprite.Group()
        self.Key = pygame.sprite.Group()
        self.Boroff = pygame.sprite.Group

    def copy(self):
        player.xx_hero = copy.copy(player.x_hero)
        player.yy_hero = copy.copy(player.y_hero)

    def IfNextLevel(self):
        self.rect = pygame.Rect(700, player.y_hero, 30, 50)
        if self.HaveKey == True:
            if pygame.sprite.spritecollideany(self, self.ThisDoor):
                self.plats()
                self.ThisIsMap += 1
                if self.ThisIsMap > 2:
                    Win(pygame.time.get_ticks() // 1000)
                level = open(f"../MAPS/{allMap[self.ThisIsMap]}", mode='r', encoding="utf-8").readlines()
                mapping(level)
                self.HaveKey = False

    def Death(self):
        global run, go_game
        if player.Hitpoints <= 0:
            run = False
            go_game = False
            death_menu()

    def Keyying(self):
        self.rect = pygame.Rect(700, player.y_hero, 30, 50)
        if pygame.sprite.spritecollideany(self, self.Key):
            self.HaveKey = True



def mapping(level):
    x = y = 0
    global ifBoss, x_bora, y_bora
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
            elif col == "K":
                ThisKey = Key(x, y)
                a.Key.add(ThisKey)
            elif col == "B":
                ifBoss = True
                x_bora = x
                y_bora = y
                a.ifBoss = True
            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0



class Attack(pg.sprite.Sprite):
    def __init__(self, x, y, v, z, draf=True):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((v, 10))
        self.image = pg.image.load("../IMAGE_GAME/IMAGE_HERO_D/Non.png")
        self.image = self.image
        # self.image.fill(pg.Color(PLATFORM_COLOR))
        self.rect = pg.Rect(x, y + 10, v, z)
        if draf:
            pygame.draw.rect(screen, (255, 255, 255),
                            (x, y + 10, v, z))



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
        self.image = pg.image.load("../IMAGE_GAME/IMAGE_HERO_D/Inoske.jpg")
        self.image = pg.transform.scale(self.image, (60, 60))
        self.yvel = 5

    def movi_enemy(self, where):
        # self.x_e += self.speed_enemy
        if where == "Right":
            x_enemy[self.typ] += self.speed_enemy
        elif where == "Left":
            x_enemy[self.typ] -= self.speed_enemy

    def visor(self):
        self.rect = pygame.Rect(700, player.y_hero, 30, 50)
        R = pygame.sprite.Group()
        L = pygame.sprite.Group()
        left_visor = Attack(x_enemy[self.typ] - 120, y_enemy[self.typ], 120, 3, False)
        right_visor = Attack(x_enemy[self.typ] + 40, y_enemy[self.typ], 120, 3, False)
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
        self.rect = pygame.Rect(700, player.y_hero, 30, 50)
        if visa == "Right":
            rect_Player = Attack(x_enemy[self.typ] + 60, y_enemy[self.typ], 30, 30)
            DD = pygame.sprite.Group()
            DD.add(rect_Player)
            if pygame.sprite.spritecollideany(self, DD):
                player.Hitpoints -= 10
                a.push_true = True
                a.push_nap = "Right"
        elif visa == "Left":
            rect_Player = Attack(x_enemy[self.typ] - 30, y_enemy[self.typ], 30, 30)
            DD = pygame.sprite.Group()
            DD.add(rect_Player)
            if pygame.sprite.spritecollideany(self, DD):
                player.Hitpoints -= 10
                a.push_true = True
                a.push_nap = "Left"

    def walls(self, e, pp):
        self.rect = pygame.Rect(x_enemy[self.typ], y_enemy[self.typ], 60, 60)
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
            y_enemy[self.typ] += self.yvel


    def push_left(self):
        if a.push_range <= 10 and a.push_true == True and a.push_nap == "Left":
            a.push_range += 1
            player.x_hero -= 10
            if a.push_range == 10:
                a.push_range = 0
                a.push_true = False
                a.push_nap = "None"

    def push_right(self):
        if a.push_range <= 10 and a.push_true == True and a.push_nap == "Right":
            a.push_range += 1
            player.x_hero += 10
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
        self.movi_enemy(self.direction)



class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj, what):
        global x_bora
        if what == "blocks":
            obj.rect.x -= self.dx
            # obj.rect.y -= self.dy
        elif what == "Boss":
            x_bora -= self.dx
        elif what != "blocks" and what != "Boss":
            x_enemy[what] -= self.dx
            # y_enemy[what] -= self.dy
    # позиционировать камеру на объекте target
    def update(self):
        self.dx = (player.x_hero - player.xx_hero)
        self.dy = (player.y_hero - player.yy_hero)



def GAME():
    global run
    pg.mouse.set_visible(False)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            elif event.type == pygame.QUIT:
                sys.exit()

        if a.ifBoss:
            Bora = Borov(x_bora, y_bora)

        font = pygame.font.SysFont("Times New Roman", 20)

        Hits = font.render(f" Hitpoints: {player.Hitpoints}", True, (0, 0, 0))

        if a.HaveKey == True:
            YourHaveKey = font.render("У вас есть ключ", True, (0, 0, 0))
        if a.HaveKey == False:
            YourHaveKey = font.render("У вас нет ключа", True, (0, 0, 0))

        # NowTime = font.render(f" Время в секундах: {pygame.time.get_ticks() // 1000}", True, (0, 0, 0))

        # death
        a.Death()
        a.copy()
        screen.blit(bg, (0, 0))
        keys = pygame.key.get_pressed()
        if 1 in keys:
            player.move(keys)
        all_sprites = pg.sprite.Group()
        # здесь передаем значение методу гравити и джамп для постоянной проверки на каждой итерации
        player.gravity(True)
        player.jump(True)
        # вывод на экран героя
        screen.blit(player.image_hero, (700, player.y_hero))
        # обновление врагов и их вывод
        for i in range(len(x_enemy)):
            ene = Enemy(x_enemy[i], y_enemy[i])
            ene.update(i, a.entities, a.Left_plat, a.Right_plat, a.Up_plat, a.PP_plat)
            screen.blit(ene.image, (ene.x_e, ene.y_e))
        # создание спрайта ирока для работы с камерой
        # обновление платформ и их вывод
        player.update(a.entities, a.Left_plat, a.Right_plat, a.Up_plat, a.PP_plat, a.Key)
        a.Keyying()
        a.entities.draw(screen)
        a.ThisDoor.draw(screen)
        # a.Up_plat.draw(screen)
        if a.HaveKey == False:
            a.Key.draw(screen)

        # работа с Боровом
        if ifBoss:
            screen.blit(Bora.image_b, (Bora.x_boss, Bora.y_boss))
            Bora.update()

        # добавление всех спратов в общую группу
        all_sprites.add(a.entities)
        all_sprites.add(a.Left_plat)
        all_sprites.add(a.Right_plat)
        all_sprites.add(a.Up_plat)
        all_sprites.add(a.PP_plat)
        all_sprites.add(a.ThisDoor)
        all_sprites.add(a.Key)

        camera.update()  # центризируем камеру относительно персонажа
        for e in all_sprites:
            camera.apply(e, "blocks")
        for i in range(len(x_enemy)):
            ene = Enemy(x_enemy[i], y_enemy[i])
            camera.apply(ene, i)
        if ifBoss:
            camera.apply(Bora, "Boss")

        # проверка есть ли ключ и столкновение с дверью
        a.IfNextLevel()

        clock.tick(60)
        pygame.display.set_caption(f"{int(clock.get_fps())}")

        screen.blit(Hits, (20, 20))
        screen.blit(YourHaveKey, (200, 20))

        pygame.display.update()


def start_the_game():

    start_menu_bg = pygame.image.load("../IMAGE_GAME/IMAGE_MAP/Bg_start.jpg")

    sc = pygame.display.set_mode((1400, 800))
    sc.blit(start_menu_bg, (0, 0))

    font = pygame.font.SysFont("Times New Roman", 20)
    font1 = pygame.font.SysFont("Times New Roman", 25)

    text_start = font.render("Начать", True, (0, 0, 0))
    text_exit = font.render("Выйти", True, (0, 0, 0))
    how_exit = font1.render("Чтобы выйти в любой момент игры, вы можете нажать Esc", True, (0, 0, 0))

    Rect_start = pygame.Rect((585, 502, 200, 40))
    Rect_exit = pygame.Rect((585, 552, 200, 40))

    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if Rect_start.collidepoint(event.pos):
                        GAME()
                    if Rect_exit.collidepoint(event.pos):
                        sys.exit()

        # кнопка начала игры
        start_rgb = (185, 238, 238)
        pygame.draw.rect(sc, (start_rgb),
                         (585, 502, 200, 40))
        sc.blit(text_start, (655, 512))

        # кнопка выхода
        exit_rgb = (250, 218, 221)
        pygame.draw.rect(sc, (exit_rgb),
                         (585, 552, 200, 40))
        sc.blit(text_exit, (655, 562))

        sc.blit(how_exit, (30, 740))

        pygame.display.update()

a = Game(size, screen)
player = Player()
mapping(level)
camera = Camera()
all_sprites = pg.sprite.Group()

go_game = True
while go_game:
    start_the_game()
    # Win(7486)
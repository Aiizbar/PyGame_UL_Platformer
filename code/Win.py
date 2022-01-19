import pygame
import pygame as pg
import sys
from Settings import *


def getting_time(time):
    minets = 0
    while time >= 60:
        minets += 1
        time -= 60
    if minets <= 9:
        minets = '0' + str(minets)
    if time <= 9:
        time = '0' + str(time)
    time = str(minets) + ':' + str(time)
    return time


def Win(time):
    pg.mouse.set_visible(True)

    start_menu_bg = pygame.image.load("../IMAGE_GAME/IMAGE_MAP/Bg_win.jpg")
    start_menu_bg = pygame.transform.scale(start_menu_bg, (1400, 800))

    sc = pygame.display.set_mode((1400, 800))
    sc.blit(start_menu_bg, (0, 0))

    font = pygame.font.SysFont("Times New Roman", 20)
    font1 = pygame.font.SysFont("Times New Roman", 25)
    font2 = pygame.font.SysFont("Times New Roman", 30)

    time = getting_time(time)


    text_exit = font.render("Выйти", True, (255, 255, 255))
    how_exit = font1.render("Чтобы выйти в любой момент игры, вы можете нажать Esc", True, (0, 0, 0))
    YourWin = font2.render((f'Ваше время прохождения {time}'), True, (255, 255, 255))
    # YourDeath = font2.render("Your Death...", True, (255, 0, 0))

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
                    if Rect_exit.collidepoint(event.pos):
                        sys.exit()

        # кнопка выхода
        exit_rgb = (0, 0, 0)
        pygame.draw.rect(sc, (exit_rgb),
                         (585, 552, 200, 40))
        sc.blit(text_exit, (655, 562))

        sc.blit(how_exit, (30, 740))

        sc.blit(YourWin, (500, 100))

        # sc.blit(YourDeath, (500, 300))

        pygame.display.update()
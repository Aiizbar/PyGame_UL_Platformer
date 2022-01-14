import pygame
import pygame as pg
import sys
from Settings import *

def death_menu():
    start_menu_bg = pygame.image.load("../IMAGE_GAME/IMAGE_MAP/Bg_end.jpg")

    sc = pygame.display.set_mode((1400, 800))
    sc.blit(start_menu_bg, (0, 0))

    font = pygame.font.SysFont("Times New Roman", 20)
    font1 = pygame.font.SysFont("Times New Roman", 25)
    font2 = pygame.font.SysFont("Times New Roman", 70)


    text_exit = font.render("Выйти", True, (255, 255, 255))
    how_exit = font1.render("Чтобы выйти в любой момент игры, вы можете нажать Esc", True, (0, 0, 0))
    YourDeath = font2.render("Your Death...", True, (255, 0, 0))

    Rect_exit = pygame.Rect((585, 552, 200, 40))

    # здесь будут рисоваться фигуры

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

        sc.blit(YourDeath, (500, 300))

        pygame.display.update()
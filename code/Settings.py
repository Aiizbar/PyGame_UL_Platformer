import pygame

pygame.mixer.init()
# pygame.mixer.music.load('../SOUNDS/Alizbar - Dance of Unicorns.mp3')
# pygame.mixer.music.play()

my_sound = pygame.mixer.Sound('../SOUNDS/Unicorn.mp3')
my_sound.play()

my_sound.set_volume(1)

t = 0
wight = 1400
height = 800
size = (wight, height)
screen = pygame.display.set_mode(size)
# bg = pygame.image.load('../IMAGE_GAME/IMAGE_MAP/MAP1.png').convert()
bg = pygame.image.load('../IMAGE_GAME/IMAGE_MAP/Wood.png').convert()
bg = pygame.transform.scale(bg, (1400, 800))
clock = pygame.time.Clock()
run = True
PLATFORM_WIDTH = 40
PLATFORM_HEIGHT = 40
PLATFORM_COLOR = "#FF6262"

ENEMY_WIDTH = 40
ENEMY_HEIGHT = 50
x_enemy = []
y_enemy = []

ifBoss = False
BOSS_W = 250
BOSS_H = 150


GameOn = False

allMap = ["testMap.txt", "FirstMap.txt", "SecondMap.txt", "BossMap.txt"]
HaveKey = False
level = open(f"../MAPS/{allMap[0]}", mode='r', encoding="utf-8").readlines()

IfWin = False
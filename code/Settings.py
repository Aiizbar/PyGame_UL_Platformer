import pygame


# pygame.mixer.music.load('../SOUNDS/sound_bg1.ogg')
# pygame.mixer.music.play()
t = 0
wight = 1400
height = 800
size = (wight, height)
screen = pygame.display.set_mode(size)
# bg = pygame.image.load('../IMAGE_GAME/IMAGE_MAP/MAP1.png').convert()
bg = pygame.image.load('../IMAGE_GAME/IMAGE_MAP/stena1.jpg').convert()
bg = pygame.transform.scale(bg, (2500, 2000))
clock = pygame.time.Clock()
run = True
PLATFORM_WIDTH = 40
PLATFORM_HEIGHT = 40
PLATFORM_COLOR = "#FF6262"

allMap = ["testMap.txt", "SecondMap.txt", "BossMap.txt"]
HaveKey = True
level = open(f"../MAPS/{allMap[0]}", mode='r', encoding="utf-8").readlines()

aa = 400
bb = 250
import pygame


# pygame.mixer.music.load('../SOUNDS/sound_bg1.ogg')
# pygame.mixer.music.play()
t = 0
wight = 800
height = 500
size = (wight, height)
screen = pygame.display.set_mode(size)
# bg = pygame.image.load('../IMAGE_GAME/IMAGE_MAP/MAP1.png').convert()
bg = pygame.image.load('../IMAGE_GAME/IMAGE_MAP/stena1.jpg').convert()
bg = pygame.transform.scale(bg, (2500, 2000))
clock = pygame.time.Clock()
run = True
PLATFORM_WIDTH = 50
PLATFORM_HEIGHT = 50
PLATFORM_COLOR = "#FF6262"

aa = 400
bb = 250
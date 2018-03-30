import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1000, 400))
screen_rect = screen.get_rect()

feichuan_image = pygame.image.load('jiantou.bmp')
feichuan_rect = feichuan_image.get_rect()

print(feichuan_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255, 255, 255))
    screen.blit(feichuan_image, feichuan_rect)

    pygame.display.flip()

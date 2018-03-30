import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1000, 400))
screen_rect = screen.get_rect()

feichuan_image = pygame.image.load('jiantou.bmp')

feichuan_rect = feichuan_image.get_rect()

feichuan_rect.centerx = screen_rect.centerx
feichuan_rect.bottom = screen_rect.bottom

print(feichuan_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                feichuan_rect.centerx += 3

    screen.fill((255, 255, 255))
    screen.blit(feichuan_image, feichuan_rect)

    pygame.display.flip()

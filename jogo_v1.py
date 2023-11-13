import pygame
import random
from config import altura, largura

pygame.init()


window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Tá dando onda')
font = pygame.font.SysFont(None, 48)


assets = {}
assets['background'] = pygame.image.load('imagens/fundo_do_mar.jpg').convert()
assets['background'] = pygame.transform.scale(assets['background'], (largura, altura))

fundo_rect = assets['background'].get_rect()

game = True

clock = pygame.time.Clock()
FPS = 30

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYUP:
            game = False

    window.blit(assets['background'], fundo_rect)
    pygame.display.flip()

pygame.quit()



    
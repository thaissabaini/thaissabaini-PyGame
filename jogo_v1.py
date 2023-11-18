import pygame
import random
from config import altura, largura

pygame.init()


window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Under the sea')
font = pygame.font.SysFont(None, 48)


background = pygame.image.load('imagens/fundo.jpeg').convert()
background = pygame.transform.scale(background, (largura, altura))

fundo_rect = background.get_rect()

game = True

clock = pygame.time.Clock()
FPS = 30

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYUP:
            game = False

    window.blit(background, fundo_rect)
    pygame.display.flip()

pygame.quit()



    
import pygame
import random
import time
from config import altura, largura

pygame.init()

window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Under the sea')


sereia_largura = 100
sereia_altura = 150
velocidade_sereia = 10


font = pygame.font.SysFont(None, 48)
background = pygame.image.load('imagens/mar.png').convert()
background = pygame.transform.scale(background, (largura, altura))
fundo_rect = background.get_rect()

sereia_img = pygame.image.load('imagens/sereia2.png').convert_alpha()
sereia_img_real = pygame.transform.scale(sereia_img, (sereia_largura, sereia_altura))


class Sereia(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = largura / 2
        self.rect.bottom = altura - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > altura:
            self.rect.bottom = altura
        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0

game = True
clock = pygame.time.Clock()
FPS = 30

todas_sprites = pygame.sprite.Group()
jogador = Sereia(sereia_img_real)
todas_sprites.add(jogador)


while game:
    clock.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jogador.speedx -= velocidade_sereia
            if evento.key == pygame.K_RIGHT:
                jogador.speedx += velocidade_sereia

            if evento.key == pygame.K_UP:
                jogador.speedy -= velocidade_sereia
            if evento.key == pygame.K_DOWN:
                jogador.speedy += velocidade_sereia

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                jogador.speedx += velocidade_sereia
            if evento.key == pygame.K_RIGHT:
                jogador.speedx -= velocidade_sereia

            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                jogador.speedy = 0

    todas_sprites.update()
    window.blit(background, fundo_rect)

    todas_sprites.draw(window)
    pygame.display.update()

pygame.quit()
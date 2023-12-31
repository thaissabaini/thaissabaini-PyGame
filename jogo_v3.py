import pygame
import random
import time
from config import altura, largura

pygame.init()

janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Under the sea')

sereia_largura = 80
sereia_altura = 120

velocidade_sereia = 10

font = pygame.font.SysFont(None, 48)
fundo = pygame.image.load('imagens/mar.png')
fundo = pygame.transform.scale(fundo, (largura, altura))

sereia_img = pygame.image.load('imagens/sereia2.png').convert_alpha()
sereia_real = pygame.transform.scale(sereia_img, (sereia_largura, sereia_altura))

estrela_img= pygame.image.load('imagens/star.png').convert_alpha()
estrela_img=pygame.transform.scale(estrela_img,(30,30))

tela_inicio = pygame.image.load('imagens/mar.png').convert_alpha()
tela_inicio = pygame.transform.scale(tela_inicio, (largura, altura))

inter_estrela= 2
def tela_inicial():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    return

        janela.blit(tela_inicio, (0, 0))
        pygame.display.update()


def begin():
    global jogador, todas_sprites, todas_estrelas
    global tempo_inicial

    jogador = Sereia(sereia_real)
    todas_sprites = pygame.sprite.Group()
    todas_estrelas = pygame.sprite.Group()
    todas_sprites.add(jogador)

    tempo_inicial = time.time()
    

class Sereia(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = largura / 2
        self.rect.bottom = altura - 10
        self.speedx = 0
        self.speedy = 0

        self.velocidade_y = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.bottom > altura:
            self.rect.bottom = altura

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0

class Estrela(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(largura-self.rect.width)
        self.rect.y=random.randrange(largura-self.rect.height)

    def update(self):
        pass

def criar_estrela():
    estrela=Estrela(estrela_img)
    todas_sprites.add(estrela)
    todas_estrelas.add(estrela)


game = True
clock = pygame.time.Clock()
FPS = 30

todas_sprites = pygame.sprite.Group()
jogador = Sereia(sereia_real)
todas_sprites.add(jogador)

tela_inicial()
begin()

tempo_estrela=time.time()

while game:

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
            
    tempo_total=time.time()- tempo_inicial

    if time.time()-tempo_estrela>inter_estrela:
        criar_estrela()
        tempo_estrela=time.time()

    todas_sprites.update()
    todas_estrelas.update()

    colisoes_estrelas=pygame.sprite.spritecollide(jogador,todas_estrelas,True)

    

    janela.fill((255, 255, 255))
    janela.blit(fundo, (0, 0))

    todas_sprites.draw(janela)
    todas_estrelas.draw(janela)
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
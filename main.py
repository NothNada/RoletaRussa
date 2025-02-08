import pygame
import sys
from random import randint,choice

from classes.luminaria import Luminaria
from classes.player import Player
from classes.arma import Arma
from classes.computador import Computador
from classes.balas import Balas

pygame.init()

largura = 500
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Roleta Russa")

botao = ((largura/2)-70,(altura/2)-25,140,50)

inicio = 0

COR_FUNDO = (0, 0, 0)
pygame.mouse.set_cursor(*pygame.cursors.arrow)

fonte = pygame.font.Font(None,48)

luminaria = Luminaria("imgs/2.png")
arma = Arma("imgs/rev.png")
computador = Computador("imgs/0.png")
player = Player("imgs/1.png")

b = randint(1,5)
balas = Balas(b)

v = None
print(balas.balas)
fica = False

fim = 0

rodando = True


def playerWin():
    global tela
    while 1:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        t = fonte.render("Vc ganhou!",True,(200,200,200))
        rect = t.get_rect()
        tela.blit(t,((tela.get_width()/2)-(rect.w/2),(tela.get_height()/2)-(rect.h/2)))

        pygame.display.flip()


def pcWin():
    global tela
    while 1:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        t = fonte.render("Ele ganhou :(",True,(200,200,200))
        rect = t.get_rect()
        tela.blit(t,((tela.get_width()/2)-(rect.w/2),(tela.get_height()/2)-(rect.h/2)))

        pygame.display.flip()


while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False


    tela.fill(COR_FUNDO)

    if inicio == 0:
        
        btn = pygame.draw.rect(tela,(255,255,0),botao,border_radius=10)
        
        if btn.colliderect((pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],10,10)):
            texto = fonte.render("Jogar",True,(0,0,0))
            rect_texto = texto.get_rect()
            tela.blit(texto,((largura/2)-(rect_texto.width/2),(altura/2)-(rect_texto.height/2)))
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
            if pygame.mouse.get_pressed()[0]:
                COR_FUNDO = (60,60,60)
                inicio = 1
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            texto = fonte.render("Jogar",True,(255,255,255))
            rect_texto = texto.get_rect()
            tela.blit(texto,((largura/2)-(rect_texto.width/2),(altura/2)-(rect_texto.height/2)))

    elif inicio==1:
        if b == 0 and player.life != 0 and computador.life != 0:
            balas = Balas(randint(1,5))
        
        b = 0
        for x in balas.balas:
            if x == 1:
                b += 1
        
        if player.life == 0:
            pcWin()
        if computador.life == 0:
            playerWin()

        escuro = pygame.Surface((largura,altura))
        escuro.fill((100,100,100))

        texto = fonte.render(str(b)+"/6",True,(255,255,255))
        rect_texto = texto.get_rect()
        tela.blit(texto,(0,0))
        

        computador.draw()

        luminaria.draw()
        luminaria.update()
        luminaria.draw_light(escuro)

        retorno_arma=arma.update()
        if retorno_arma==2 or fica:
            arma.draw()
        if retorno_arma==1:
            fica = True
            v = player.escolha(balas,computador)
            if v!=2:
                print(v)
            if v==0:
                player.restore()
                v=2
            if v==1:
                v=2
                computador.restore()
                retorno_arma = 0
                arma.angle = 90
        elif retorno_arma==0:
            fica = True
            v = computador.escolha(balas,player)
            if v!=2:
                print(v)
            if v==0:
                computador.restore()
                v=2
            if v==1:
                v=2
                player.restore()
                retorno_arma = 1
                arma.angle = 270
        
        player.draw()

        tela.blit(escuro,(0,0),special_flags=pygame.BLEND_RGB_SUB)
    elif inicio == 2:
        if player.life == 0:
            pass
        if computador.life == 0:
            pass
    

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()

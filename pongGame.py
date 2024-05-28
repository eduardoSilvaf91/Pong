import pygame
from time import sleep
import random

POSICAO_X_JOGADOR = 5
POSICAO_INICIAL_Y_JOGADOR = 260
POSICAO_X_CPU = 775
POSICAO_XY_INICIAL_BOLINHA = (400,300)


pygame.init()

# -- função inverte o sinal --
def inverte_valor(num):
    if num > 0:
        return 0 - num
    else:
        return abs(num)

# -- Variaveis --

VELOCIDADE_MOVIMENTO_JOGADOR = 10
posicao_y_jogador = POSICAO_INICIAL_Y_JOGADOR


# -- variaveis bola --
bola_tamanho = 10
velocidade_x_bola = 8
velocidade_y_bola = 8
posicao_y_bola = POSICAO_XY_INICIAL_BOLINHA[1]
posicao_x_bola = POSICAO_XY_INICIAL_BOLINHA[0]

# -- variaveis cpu --
posicao_y_cpu = posicao_y_bola - 40
num_randon_erro_cpu = 0

# -- variaveis colizão --
colizao_x_bola = False
colizao_y_bola = False

# -- variaveis sprites do jogo --
sprite_img_fundo = pygame.image.load('sprit\Campo.png')
sprite_barra_jogador = pygame.image.load('sprit\Barra.png')
sprite_barra_cpu = pygame.image.load('sprit\Barra.png')
sprite_bola = pygame.image.load('sprit\Bola.png')

# -- variaveis texto pontos -- 
ponto_jogador = 0
font = pygame.font.SysFont('arial Black ',30)
texto_jogador = font.render("Jogador: "+str(ponto_jogador), True, (255, 255, 255), (120, 120, 50))
pos_texto_jogador = texto_jogador.get_rect()
pos_texto_jogador.center = (200,50)

ponto_cpu = 0
font = pygame.font.SysFont('arial Black ',30)
texto_cpu = font.render("Cpu: "+str(ponto_cpu), True, (255, 255, 255), (120, 50, 50))
pos_texto_cpu = texto_jogador.get_rect()
pos_texto_cpu.center = (600,50)


# -- tamanho da janela --
janela = pygame.display.set_mode((800,600))

pause = True
cont = 0
janela_aberta = True

# -- inicio das interações --
while janela_aberta :
    pygame.time.delay(25) # delay para atualizar a tela em miliSegundos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    # -- Inicio Com pause --
    if pause and cont == 1:
        sleep(3)
        pause = False
        cont = 0
        

    #------------------------------------------------
    # comandos e botões de controle
    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_UP] and posicao_y_jogador > 0 :
        posicao_y_jogador -= VELOCIDADE_MOVIMENTO_JOGADOR
        posicao_y_cpu -= VELOCIDADE_MOVIMENTO_JOGADOR
    if comandos[pygame.K_DOWN] and posicao_y_jogador < 520:
        posicao_y_jogador += VELOCIDADE_MOVIMENTO_JOGADOR
        posicao_y_cpu += VELOCIDADE_MOVIMENTO_JOGADOR


    #------------------------------------------------
    # -- logica colizao bolinha Jogador -- 
    if posicao_x_bola < (POSICAO_X_JOGADOR + 20) and (posicao_y_bola + bola_tamanho) > posicao_y_jogador and posicao_y_bola < posicao_y_jogador + 80:
        colizao_x_bola = True
       

    # -- logica colizao bolinha CPU -- 
    if posicao_x_bola + bola_tamanho > POSICAO_X_CPU and (posicao_y_bola + bola_tamanho) > posicao_y_cpu and posicao_y_bola < (posicao_y_cpu + 80 ):
        colizao_x_bola = True
        num_randon_erro_cpu = (random.randrange(0, 6)) * 10
        print(num_randon_erro_cpu)

    
    # -- logica colizao lateral da bolinha -- 
    if posicao_y_bola > 600 or posicao_y_bola < 0:
        colizao_y_bola = True


    # -- logica movimento bolinha --
    if colizao_x_bola :
        velocidade_x_bola = inverte_valor(velocidade_x_bola)
        colizao_x_bola = False
        
    if colizao_y_bola :
        velocidade_y_bola = inverte_valor(velocidade_y_bola)
        colizao_y_bola = False

    # -- logica pontuar bolinha --
    if posicao_x_bola > 800:
        ponto_jogador += 1
        texto_jogador = font.render("Jogador: "+str(ponto_jogador), True, (255, 255, 255), (120, 120, 50))
        posicao_y_bola = POSICAO_XY_INICIAL_BOLINHA[1]
        posicao_x_bola = POSICAO_XY_INICIAL_BOLINHA[0]
        posicao_y_jogador = POSICAO_INICIAL_Y_JOGADOR
        num_randon_erro_cpu = 0
        colizao_x_bola = True
        colizao_y_bola = True
        pause = True

    if posicao_x_bola < 0:
        ponto_cpu += 1
        texto_cpu = font.render("Cpu: "+str(ponto_cpu), True, (255, 255, 255), (120, 50, 50))
        posicao_y_bola = POSICAO_XY_INICIAL_BOLINHA[1]
        posicao_x_bola = POSICAO_XY_INICIAL_BOLINHA[0]
        posicao_y_jogador = POSICAO_INICIAL_Y_JOGADOR
        num_randon_erro_cpu = 0
        colizao_x_bola = True
        colizao_y_bola = True
        pause = True

    #------------------------------------------------
    # -- movimento --

    # -- movimenta a bolinha --
    posicao_x_bola += velocidade_x_bola
    posicao_y_bola += velocidade_y_bola

    # -- movimenta a cpu --
    posicao_y_cpu = posicao_y_bola - 40 + num_randon_erro_cpu

    # -- evita movimento cpu fora da tela
    if posicao_y_cpu < 0:
        posicao_y_cpu = 0
    if posicao_y_cpu > 520:
        posicao_y_cpu = 520


    # posicao dos elementos e mostra na tela
    janela.blit(sprite_img_fundo,(0,0))
    janela.blit(sprite_barra_jogador,(POSICAO_X_JOGADOR,posicao_y_jogador))
    janela.blit(sprite_barra_cpu,(POSICAO_X_CPU,posicao_y_cpu))
    janela.blit(sprite_bola,(posicao_x_bola,posicao_y_bola))
    janela.blit(texto_jogador,pos_texto_jogador)
    janela.blit(texto_cpu,pos_texto_cpu)

    pygame.display.update()  # atualiza a tela

    # -- Reseta o inicio Com pause --
    if pause and cont == 0:
        cont = 1
        
pygame.quit()
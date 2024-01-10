import pygame
import math

pygame.init()

larguraTela = 1100
alturaTela = 700

tela = pygame.display.set_mode((larguraTela, alturaTela))
telaTransparency = pygame.Surface((larguraTela, alturaTela), pygame.SRCALPHA)

pygame.display.set_caption("Trabalho 2 de Computação Gráfica")

imagemBackground = pygame.image.load(r'C:\Users\Assistencia\Downloads\CGAnimation\Imagens\Backrooms_model.jpg')
background = pygame.transform.scale(imagemBackground, (larguraTela, alturaTela))

posicao_inicial = (115, 520)
posicao_final = (970, 520)

diferenca = (posicao_final[0] - posicao_inicial[0], posicao_final[1] - posicao_inicial[1])

num_frames = 200
incremento_x = diferenca[0] / num_frames
incremento_y = diferenca[1] / num_frames

posicao_atual = posicao_inicial
posicao_nuvem = 0  

cobra_x = 263
cobra_y = 69
amplitude_pulo = 10  
frequencia_pulo = 0.1

def desenharCanos():
    pygame.draw.rect(tela, (204, 204, 0), (700, 540, 55, 70))
    pygame.draw.rect(tela, (0, 0, 0), (700, 540, 56, 71), width=3)

    pygame.draw.rect(tela, (204, 204, 0), (695, 502, 70, 40))
    pygame.draw.rect(tela, (0, 0, 0), (693, 502, 71, 41), width=3)

    pygame.draw.rect(tela, (204, 204, 0), (790, 540, 55, 70))
    pygame.draw.rect(tela, (0, 0, 0), (790, 540, 56, 71), width=3)

    pygame.draw.rect(tela, (204, 204, 0), (783, 503, 70, 40))
    pygame.draw.rect(tela, (0, 0, 0), (783, 503, 71, 41), width=3)

def desenharPlanta():
    pygame.draw.rect(tela, (0, 128, 0), (720, 90, 12, 411))

    pygame.draw.rect(tela, (0, 128, 0), (732, 480, 20, 12))
    pygame.draw.rect(tela, (0, 128, 0), (732, 420, 20, 12))
    pygame.draw.rect(tela, (0, 128, 0), (732, 360, 20, 12))
    pygame.draw.rect(tela, (0, 128, 0), (732, 300, 20, 12))
    pygame.draw.rect(tela, (0, 128, 0), (732, 240, 20, 12))
    pygame.draw.rect(tela, (0, 128, 0), (732, 180, 20, 12))
    pygame.draw.rect(tela, (0, 128, 0), (732, 120, 20, 12))

    pygame.draw.rect(tela, (0, 128, 0), (700, 452, 20, 12))
    pygame.draw.rect(tela, (0, 128, 0), (700, 392, 20, 12))
    pygame.draw.rect(tela, (0, 128, 0), (700, 332, 20, 12))
    pygame.draw.rect(tela, (0, 128, 0), (700, 272, 20, 12))
    pygame.draw.rect(tela, (0, 128, 0), (700, 212, 20, 12))
    pygame.draw.rect(tela, (0, 128, 0), (700, 152, 20, 12))

def desenharCobraBase():
    brick_color = (210, 105, 30)   
    base_height = 10
    brick_width = 10
    brick_gap = 2 

    def desenhar_tijolos(x, y, width, height):
        for i in range(0, width, brick_width + brick_gap):
            pygame.draw.rect(tela, brick_color, (x + i, y, brick_width, height))
            pygame.draw.rect(tela, brick_color, (x + i, y, brick_gap, height))

    desenhar_tijolos(260, 100, 90, base_height)

def desenharCobra():
    global cobra_y  
    pulo = amplitude_pulo * math.sin(frequencia_pulo * frame_atual)

    pygame.draw.circle(tela, (0, 0, 0), (cobra_x, cobra_y - pulo), 17)
    pygame.draw.circle(tela, (255, 193, 7), (cobra_x, cobra_y - pulo), 14)

    pygame.draw.polygon(tela, (255, 0, 0), [(cobra_x, cobra_y + 14 - pulo), (cobra_x, cobra_y + 23 - pulo), (cobra_x + 7, cobra_y + 18 - pulo)])

    pygame.draw.ellipse(tela, (0, 0, 0), (cobra_x - 3, cobra_y - 4 - pulo, 5, 5))
    pygame.draw.ellipse(tela, (0, 0, 0), (cobra_x + 5, cobra_y - 4 - pulo, 5, 5))

    pygame.draw.ellipse(tela, (255, 193, 7), (cobra_x + 13, cobra_y - pulo, 14, 28))
    pygame.draw.ellipse(tela, (0, 0, 0), (cobra_x + 13, cobra_y - pulo, 15, 29), width=3)

    pygame.draw.ellipse(tela, (255, 193, 7), (cobra_x + 29, cobra_y - pulo, 14, 28))
    pygame.draw.ellipse(tela, (0, 0, 0), (cobra_x + 29, cobra_y - pulo, 15, 29), width=3)

    pygame.draw.ellipse(tela, (255, 193, 7), (cobra_x + 45, cobra_y - pulo, 14, 28))
    pygame.draw.ellipse(tela, (0, 0, 0), (cobra_x + 45, cobra_y - pulo, 15, 29), width=3)

    pygame.draw.ellipse(tela, (255, 193, 7), (cobra_x + 61, cobra_y - pulo, 14, 28))
    pygame.draw.ellipse(tela, (0, 0, 0), (cobra_x + 61, cobra_y - pulo, 15, 29), width=3)

    desenharCobraBase()

def desenharPlantaCarnivora(esquerda=True):
    if esquerda:
        pygame.draw.arc(tela, (0, 128, 0), (830, 474, 80, 60), 3.14 / 2, 3.14, width=5)
        pygame.draw.circle(tela, (255, 0, 0), (880, 460), 25, draw_top_left=True, draw_bottom_left=True, draw_bottom_right=True)
        pygame.draw.circle(tela, (0, 0, 0), (880, 460), 25, draw_top_left=True, draw_bottom_left=True, draw_bottom_right=True, width=3)
    else:
        pygame.draw.arc(tela, (0, 128, 0), (750, 474, 80, 60), 0, 3.14/2, width=5)
        pygame.draw.circle(tela, (255, 0, 0), (775, 465), 25, draw_top_right=True, draw_bottom_right=True, draw_bottom_left=True)
        pygame.draw.circle(tela, (0, 0, 0), (775, 465), 25, draw_top_right=True, draw_bottom_right=True, draw_bottom_left=True, width=3)

def desenharPorta():
    x = 900
    pygame.draw.rect(tela, (150, 75, 0), (970-x, 450, 100, 200))
    pygame.draw.rect(tela, (0, 0, 0), (970-x, 450, 100, 200), 2)
    pygame.draw.circle(tela, (0, 0, 0), (1050-x, 550), 8)
    pygame.draw.rect(tela, (0, 0, 0), (985-x, 460, 70, 70), 2)
    pygame.draw.rect(tela, (0, 0, 0), (985-x, 570, 70, 70), 2)

def desenharNuvem(posicao_x, frame_atual):
    pygame.draw.rect(telaTransparency, (255, 255, 255, 120), (posicao_x, 100, 300, 50), border_radius=50)
    pygame.draw.rect(telaTransparency, (255, 255, 255, 120), (posicao_x + 600, 100, 200, 50), border_radius=50)
    pygame.draw.rect(telaTransparency, (255, 255, 255, 120), (posicao_x + 300, 90, 215, 40), border_radius=50)

    cor_ceu = (135, 206, 235)
    cor_fundo = (0, 0, 0, 0)

    superficie = pygame.Surface((tela.get_width(), tela.get_height()), pygame.SRCALPHA)

    raio = 60
    centro = (1000, 70)

    angulo_rotacao = math.radians(frame_atual % 360)
    novo_centro = (centro[0] + int(raio * math.cos(angulo_rotacao)), centro[1] + int(raio * math.sin(angulo_rotacao)))

    pygame.draw.circle(superficie, (0, 0, 0), novo_centro, 62)
    pygame.draw.circle(superficie, cor_ceu, novo_centro, raio)

    pygame.draw.rect(superficie, cor_fundo, (novo_centro[0], novo_centro[1], 62, 62))

    olho_centro = (novo_centro[0] - 20, novo_centro[1] - 20)
    olho_raio_externo = 12
    olho_raio_interno = 5
    pygame.draw.circle(superficie, (255, 255, 255), olho_centro, olho_raio_externo)
    pygame.draw.circle(superficie, (0, 0, 0), olho_centro, olho_raio_interno)

    tela.blit(superficie, (0, 0))

def desenharCriatura(transparencia):
    cor_amarela = (255, 255, 0)
    cor_preto = (0, 0, 0)
    cor_branca = (255, 255, 255)

    posicao_x = 820
    posicao_y = 360

    criatura_surface = pygame.Surface((40, 40), pygame.SRCALPHA)
    criatura_surface.set_alpha(transparencia)

    pygame.draw.circle(criatura_surface, cor_preto, (20, 20), 21)
    pygame.draw.circle(criatura_surface, cor_amarela, (20, 20), 20)
    pygame.draw.circle(criatura_surface, cor_branca, (15, 15), 5)
    pygame.draw.circle(criatura_surface, cor_branca, (25, 15), 5)
    pygame.draw.circle(criatura_surface, cor_preto, (15, 15), 2)
    pygame.draw.circle(criatura_surface, cor_preto, (25, 15), 2)
    pygame.draw.arc(criatura_surface, cor_preto, (10, 25, 20, 10), 0, 3.14, 3)

    tela.blit(criatura_surface, (posicao_x, posicao_y))

def desenharPrincipal(posicao_x, posicao_y):
    sonic_image = pygame.image.load(r'C:\Users\Assistencia\Downloads\CGAnimation\Imagens\Sonic.png')
    tela.blit(sonic_image, (posicao_x, posicao_y))

def desenharTijolos():
    brick_color = (210, 105, 30)  
    base_height = 10
    brick_width = 10
    brick_gap = 2  

    def desenhar_tijolos(x, y, width, height):
        for i in range(0, width, brick_width + brick_gap):
            pygame.draw.rect(tela, brick_color, (x + i, y, brick_width, height))
    
    desenhar_tijolos(530, 90, 50, base_height)
    desenhar_tijolos(580, 90, 50, base_height)
    desenhar_tijolos(630, 90, 50, base_height)

def desenharAnelSonic(frame_atual):
    amplitude_pulo = 10  
    frequencia_pulo = 0.1  

    for x_pos in [535, 587, 637]:
        y_pos = 61 + amplitude_pulo * math.sin(frequencia_pulo * frame_atual)
        sonic_image = pygame.image.load(r'C:\Users\Assistencia\Downloads\CGAnimation\Imagens\pngwing.png')
        tela.blit(sonic_image, (x_pos, y_pos))

    desenharTijolos()

def desenharGradiente(cor1, cor2):
    for y in range(alturaTela):
        interp_r = int(cor1[0] * (1 - y / alturaTela) + cor2[0] * (y / alturaTela))
        interp_g = int(cor1[1] * (1 - y / alturaTela) + cor2[1] * (y / alturaTela))
        interp_b = int(cor1[2] * (1 - y / alturaTela) + cor2[2] * (y / alturaTela))

        cor = (interp_r, interp_g, interp_b, 50)
        pygame.draw.rect(telaTransparency, cor, (0, y, larguraTela, 1))

run = True
frame_atual = 0
esquerda_planta_carnivora = True

velocidade_mudanca_sentido = 500 

tempo_ultima_mudanca = pygame.time.get_ticks()

opacidade_planta_carnivora = 255
opacidade_incremento = 5  

posicao_nuvem = 0

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    tela.blit(background, (0, 0))
    tela.blit(telaTransparency, (0, 0))

    desenharGradiente((0, 0, 0), (0, 0, 0))
    desenharCanos()
    desenharPlanta()
    desenharAnelSonic(frame_atual)    
    desenharCobra()

    tempo_atual = pygame.time.get_ticks()
    if tempo_atual - tempo_ultima_mudanca >= velocidade_mudanca_sentido:
        esquerda_planta_carnivora = not esquerda_planta_carnivora
        tempo_ultima_mudanca = tempo_atual

    opacidade_planta_carnivora += opacidade_incremento
    if opacidade_planta_carnivora > 255:
        opacidade_planta_carnivora = 255
    elif opacidade_planta_carnivora < 0:
        opacidade_planta_carnivora = 0

    desenharPlantaCarnivora(esquerda_planta_carnivora)
    pygame.Surface.set_alpha(telaTransparency, opacidade_planta_carnivora)

    desenharPrincipal(int(posicao_atual[0]), int(posicao_atual[1]))

    desenharNuvem(posicao_nuvem, frame_atual)

    transparencia = abs(255 * (frame_atual % 100 - 50) / 50)  
    desenharCriatura(transparencia)

    desenharPorta()

    pygame.display.flip()

    posicao_atual = (posicao_atual[0] + incremento_x, posicao_atual[1] + incremento_y)

    if posicao_atual[0] > larguraTela or posicao_atual[1] > alturaTela:
        posicao_atual = posicao_inicial

    posicao_nuvem = (posicao_nuvem + 2) % 1100  
    frame_atual += 1

    pygame.time.delay(50)

pygame.quit()

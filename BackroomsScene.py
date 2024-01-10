import pygame
import math
import sys

pygame.init()

larguraTela = 1100
alturaTela = 700

tela = pygame.display.set_mode((larguraTela, alturaTela))
telaTransparency = pygame.Surface((larguraTela, alturaTela), pygame.SRCALPHA)

pygame.display.set_caption("Trabalho 1 de Computação Gráfica")

imagemBackground = pygame.image.load('/home/yago/Downloads/CGAnimation/Imagens/Backrooms_model.jpg')
background = pygame.transform.scale(imagemBackground, (larguraTela, alturaTela))

def desenharQuadrados():
    pygame.draw.rect(tela, (130, 84, 11), (300, 440, 35, 35))
    pygame.draw.rect(tela, (0, 0, 0), (300, 440, 36, 36), width=3)

    pygame.draw.rect(tela, (130, 84, 11), (335, 440, 35, 35),)
    pygame.draw.rect(tela, (0, 0, 0), (335, 440, 36, 36), width=3)

    pygame.draw.rect(tela, (130, 84, 11), (370, 440, 35, 35))
    pygame.draw.rect(tela, (0, 0, 0), (370, 440, 36, 36), width=3)

    pygame.draw.rect(tela, (255, 196, 12), (405, 440, 35, 35))
    pygame.draw.rect(tela, (0, 0, 0), (405, 440, 36, 36), width=3)

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

    pygame.draw.rect(tela, (0,128,0), (732, 480, 20, 12))
    pygame.draw.rect(tela, (0,128,0), (732, 420, 20, 12))
    pygame.draw.rect(tela, (0,128,0), (732, 360, 20, 12))
    pygame.draw.rect(tela, (0,128,0), (732, 300, 20, 12))
    pygame.draw.rect(tela, (0,128,0), (732, 240, 20, 12))
    pygame.draw.rect(tela, (0,128,0), (732, 180, 20, 12))
    pygame.draw.rect(tela, (0,128,0), (732, 120, 20, 12))

    pygame.draw.rect(tela, (0, 128, 0), (700, 452, 20, 12))
    pygame.draw.rect(tela, (0, 128, 0), (700, 392, 20, 12))
    pygame.draw.rect(tela, (0, 128, 0), (700, 332, 20, 12))
    pygame.draw.rect(tela, (0, 128, 0), (700, 272, 20, 12))
    pygame.draw.rect(tela, (0, 128, 0), (700, 212, 20, 12))
    pygame.draw.rect(tela, (0, 128, 0), (700, 152, 20, 12))

def desenharFlor():
    pygame.draw.rect(tela, (0,128,0), (420, 412, 8, 30))
    pygame.draw.circle(tela, (235, 77, 40), (424, 412), 14)
    pygame.draw.circle(tela, (241, 232, 51), (424, 412), 10)
    pygame.draw.circle(tela, (255, 255, 255), (424, 412), 6)

def desenharMoeda():
    pygame.draw.circle(tela, (255, 255, 0), (548, 70), 19)
    pygame.draw.circle(tela, (0, 0, 0), (548, 70), 19, width=2)

    pygame.draw.circle(tela, (255, 255, 0), (600, 70), 19)
    pygame.draw.circle(tela, (0, 0, 0), (600, 70), 19, width=2)

    pygame.draw.circle(tela, (255, 255, 0), (650, 70), 19)
    pygame.draw.circle(tela, (0, 0, 0), (650, 70), 19, width=2)

def desenharCogumelo():
    pygame.draw.rect(tela, (255, 255,255), (550, 70, 30, 20))
    pygame.draw.rect(tela, (0,0,0), (550, 70, 31, 21), width=3)

    pygame.draw.rect(tela, (223, 146, 38), (546, 55, 40, 20))
    pygame.draw.rect(tela, (0, 0, 0), (546, 55, 41, 21), width=3)

    pygame.draw.rect(tela, (0,0,0), (554, 77, 5, 8))
    pygame.draw.rect(tela, (0,0,0), (572, 77, 5, 8))

    pygame.draw.circle(tela, (200, 30, 15), (556, 64), 5)
    pygame.draw.circle(tela, (200, 30, 15), (568, 64), 4)
    pygame.draw.circle(tela, (200, 30, 15), (577, 68), 4)

def desenharCobra():
    pygame.draw.circle(tela, (0, 0, 0), (263, 72), 17)
    pygame.draw.circle(tela, (255, 193, 7), (263, 72), 14)

    pygame.draw.polygon(tela, (255, 0, 0), [(263, 86), (263, 95), (270, 90)])

    pygame.draw.ellipse(tela, (0, 0, 0), (260, 68, 5, 5))
    pygame.draw.ellipse(tela, (0, 0, 0), (268, 68, 5, 5))

    pygame.draw.ellipse(tela, (255, 193, 7), (276, 72, 14, 28))
    pygame.draw.ellipse(tela, (0, 0, 0), (276, 72, 15, 29), width=3)

    pygame.draw.ellipse(tela, (255, 193, 7), (292, 72, 14, 28))
    pygame.draw.ellipse(tela, (0, 0, 0), (292, 72, 15, 29), width=3)

    pygame.draw.ellipse(tela, (255, 193, 7), (308, 72, 14, 28))
    pygame.draw.ellipse(tela, (0, 0, 0), (308, 72, 15, 29), width=3)

    pygame.draw.ellipse(tela, (255, 193, 7), (324, 72, 14, 28))
    pygame.draw.ellipse(tela, (0, 0, 0), (324, 72, 15, 29), width=3)

def desenharPlantaCarnivora():
    pygame.draw.arc(tela, (0,128,0), (750, 474, 80, 60), 0, 3.14/2, width=5)
    pygame.draw.circle(tela, (255, 0, 0), (775, 465), 25, draw_top_right=True, draw_bottom_right=True, draw_bottom_left=True)
    pygame.draw.circle(tela, (0, 0, 0), (775, 465), 25, draw_top_right=True, draw_bottom_right=True, draw_bottom_left=True, width=3)
    
def desenharBolaDeFogo():
    pygame.draw.circle(tela, (235, 77, 40), (500, 200), 20)
    pygame.draw.circle(tela, (241, 232, 51), (500, 200), 16)
    pygame.draw.arc(tela, (235, 77, 40),  (470, 200, 100, 100), 0, 3.14/2, width=5)
    pygame.draw.arc(tela, (241, 232, 51),  (470, 195, 100, 100), 0, 3.14/2, width=5)

def desenharNuvem():
    pygame.draw.rect(telaTransparency, (255, 255, 255, 120), (800, 100, 300, 50), border_radius = 50)
    pygame.draw.rect(telaTransparency, (255, 255, 255, 120), (200, 100, 200, 50), border_radius = 50)
    pygame.draw.rect(telaTransparency, (255, 255, 255, 120), (500, 90, 215, 40), border_radius = 50)

    cor_ceu = (135, 206, 235)  
    cor_fundo = (0, 0, 0, 0)  

    superficie = pygame.Surface((tela.get_width(), tela.get_height()), pygame.SRCALPHA)

    raio = 60
    centro = (1000, 70)

    pygame.draw.circle(superficie, (0, 0, 0), centro, 62)
    pygame.draw.circle(superficie, cor_ceu, centro, raio)

    pygame.draw.rect(superficie, cor_fundo, (centro[0], centro[1], 62, 62))

    olho_centro = (centro[0] - 20, centro[1] - 20)
    olho_raio_externo = 12
    olho_raio_interno = 5
    pygame.draw.circle(superficie, (255, 255, 255), olho_centro, olho_raio_externo)
    pygame.draw.circle(superficie, (0, 0, 0), olho_centro, olho_raio_interno)

    tela.blit(superficie, (0, 0))

def desenharCriatura():
    cor_amarela = (255, 255, 0)
    cor_preto = (0, 0, 0)
    cor_branca = (255, 255, 255)

    posicao_x = 850
    posicao_y = 360

    pygame.draw.circle(tela, cor_preto, (posicao_x, posicao_y), 21)
    pygame.draw.circle(tela, cor_amarela, (posicao_x, posicao_y), 20)
    pygame.draw.circle(tela, cor_branca, (posicao_x - 5, posicao_y - 5), 5)
    pygame.draw.circle(tela, cor_branca, (posicao_x + 5, posicao_y - 5), 5)
    pygame.draw.circle(tela, cor_preto, (posicao_x - 5, posicao_y - 5), 2)
    pygame.draw.circle(tela, cor_preto, (posicao_x + 5, posicao_y - 5), 2)
    pygame.draw.arc(tela, cor_preto, (posicao_x - 10, posicao_y + 5, 20, 10), 0, 3.14, 3)

def desenharPrincipal(posicao_x, posicao_y):
    sonic_image = pygame.image.load('/home/yago/Downloads/CGAnimation/Imagens/Sonic.png')  
    tela.blit(sonic_image, (posicao_x, posicao_y))

def desenharAnelSonic():
    sonic_image = pygame.image.load('/home/yago/Downloads/CGAnimation/Imagens/pngwing.png')  
    tela.blit(sonic_image, (535, 45))
    tela.blit(sonic_image, (587, 45))
    tela.blit(sonic_image, (637, 45))

def desenharPorta():
    x = 900
    pygame.draw.rect(tela, (150, 75, 0), (970-x, 450, 100, 200))
    pygame.draw.rect(tela, (0, 0, 0), (970-x, 450, 100, 200), 2)
    pygame.draw.circle(tela, (0, 0, 0), (1050-x, 550), 8)
    pygame.draw.rect(tela, (0, 0, 0), (985-x, 460, 70, 70), 2)
    pygame.draw.rect(tela, (0, 0, 0), (985-x, 570, 70, 70), 2)

def desenharGradiente(cor1, cor2):
    for y in range(alturaTela):
        interp_r = int(cor1[0] * (1 - y / alturaTela) + cor2[0] * (y / alturaTela))
        interp_g = int(cor1[1] * (1 - y / alturaTela) + cor2[1] * (y / alturaTela))
        interp_b = int(cor1[2] * (1 - y / alturaTela) + cor2[2] * (y / alturaTela))

        cor = (interp_r, interp_g, interp_b, 50)  
        pygame.draw.rect(telaTransparency, cor, (0, y, larguraTela, 1))

run = True
while run:
    tela.blit(background, (0, 0))
    tela.blit(telaTransparency, (0,0))
    
    desenharGradiente((0, 0, 0), (0, 0, 0))
    desenharNuvem()
    desenharCanos()
    desenharPlanta()
    desenharCobra()
    desenharPlantaCarnivora()
    desenharPrincipal(300, 500)
    desenharCriatura()
    desenharPorta()
    desenharAnelSonic()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
        pygame.display.flip()
    

pygame.quit()

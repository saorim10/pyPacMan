import pygame

from constantes import AMARELO, PRETO, VELOCIDADE, TAMANHO_DA_TELA


x = 70
y = 240
tamanho = 25

pygame.init()
tela = pygame.display.set_mode(TAMANHO_DA_TELA, 0)
vel_x = VELOCIDADE
vel_y = VELOCIDADE


while True:
    # calcula as regras
    x += vel_x
    y += vel_y

    # pintar
    tela.fill(PRETO)
    pygame.draw.circle(tela, AMARELO, (int(x), int(y)), tamanho, 0)
    pygame.display.update()
    if x + tamanho > TAMANHO_DA_TELA[0] or x - tamanho < 0:
        vel_x *= -1
    if y + tamanho > TAMANHO_DA_TELA[1] or y - tamanho < 0:
        vel_y *= -1

    # eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

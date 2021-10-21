import pygame
from pacman import Pacman
from constantes import TAMANHO_DA_TELA, PRETO

pygame.init()

tela = pygame.display.set_mode(TAMANHO_DA_TELA, 0)
bob = Pacman()

while True:
    # regras
    bob.calcular_regras()

    # pintar
    tela.fill(PRETO)
    bob.pintar(tela)
    pygame.display.update()

    # eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

import pygame

from cenario import Cenario
from pacman import Pacman
from constantes import TAMANHO_DA_TELA, PRETO

pygame.init()

tamanho = TAMANHO_DA_TELA[1] // 30
tela = pygame.display.set_mode(TAMANHO_DA_TELA, 0)
bob = Pacman(tamanho)
cenario = Cenario(tamanho, bob)

while True:
    # regras
    bob.calcular_regras()
    cenario.calc_regras()

    # pintar
    tela.fill(PRETO)
    cenario.pintar(tela)
    bob.pintar(tela)
    pygame.display.update()
    pygame.time.delay(100)

    # eventos
    eventos = pygame.event.get()
    bob.movimento(eventos)
    for e in eventos:
        if e.type == pygame.QUIT:
            exit()

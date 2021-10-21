import pygame

from constantes import AMARELO, PRETO, CENTRO_X, CENTRO_Y, RAIO, VELOCIDADE, TAMANHO_DA_TELA


class Pacman:
    def __init__(self):
        self.centro_x = CENTRO_X
        self.centro_y = CENTRO_Y
        self.vel_x = VELOCIDADE
        self.vel_y = VELOCIDADE
        self.direcao = "direita"

    def pintar(self, tela):

        # corpo
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), RAIO, 0)

        # boca
        canto_boca = (self.centro_x, self.centro_y)

        if self.direcao == "direita":
            labio_superior = (self.centro_x + RAIO, self.centro_y - RAIO)
            labio_inferior = (self.centro_x + RAIO, self.centro_y)
            olho_x = self.centro_x + RAIO / 4  #
        else:
            labio_superior = (self.centro_x - RAIO, self.centro_y - RAIO)  #
            labio_inferior = (self.centro_x - RAIO, self.centro_y)  #
            olho_x = self.centro_x - RAIO / 4  #

        boca_pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, boca_pontos, 0)

        # olho
        olho_y = self.centro_y - RAIO / 1.75
        olho_raio = RAIO / 8
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

        if self.centro_x + RAIO > TAMANHO_DA_TELA[0]:
            self.vel_x *= -1
            self.direcao = "esquerda"
        elif self.centro_x - RAIO < 0:
            self.vel_x *= -1
            self.direcao = "direita"

        if self.centro_y + RAIO > TAMANHO_DA_TELA[1] or self.centro_y - RAIO < 0:
            self.vel_y *= -1

    def calcular_regras(self):
        self.centro_x += self.vel_x
        self.centro_y += self.vel_y

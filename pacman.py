import pygame

from constantes import AMARELO, PRETO, CENTRO_X, CENTRO_Y, VELOCIDADE, TAMANHO_DA_TELA


class Pacman:
    def __init__(self, tamanho_pacman):
        self.centro_x = CENTRO_X
        self.centro_y = CENTRO_Y
        self.vel_x = 0
        self.vel_y = 0
        self.direcao = "direita"
        self.coluna = 1
        self.linha = 1
        self.tamanho = tamanho_pacman
        self.raio = int(self.tamanho / 2)
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha

    def pintar(self, tela):
        # corpo
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)

        # boca
        canto_boca = (self.centro_x, self.centro_y)

        if self.direcao == "direita":
            labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
            labio_inferior = (self.centro_x + self.raio, self.centro_y)
            olho_x = self.centro_x + self.raio / 4  #
        else:
            labio_superior = (self.centro_x - self.raio, self.centro_y - self.raio)  #
            labio_inferior = (self.centro_x - self.raio, self.centro_y)  #
            olho_x = self.centro_x - self.raio / 4  #

        boca_pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, boca_pontos, 0)

        # olho
        olho_y = self.centro_y - self.raio / 1.75
        olho_raio = self.raio / 6
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

        if self.centro_y + self.raio > TAMANHO_DA_TELA[1] or self.centro_y - self.raio < 0:
            self.vel_y *= -1

    def calcular_regras(self):
        self.coluna_intencao = self.coluna + self.vel_x
        # self.coluna += self.vel_x
        self.linha_intencao = self.linha + self.vel_y
        # self.linha += self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)

    def movimento(self, eventos):
        # eventos
        for e in eventos:
            # direita
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = +VELOCIDADE
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = 0

            # esquerda
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    self.vel_x = -VELOCIDADE
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_LEFT:
                    self.vel_x = 0

            # cima
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    self.vel_y = -VELOCIDADE
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_UP:
                    self.vel_y = 0

            # baixo
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:
                    self.vel_y = +VELOCIDADE
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_DOWN:
                    self.vel_y = 0

    def movto_com_mouse(self, eventos):
        delay = 100
        for e in eventos:
            if e.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = e.pos
                self.coluna = (mouse_x - self.centro_x) / delay
                self.linha = (mouse_y - self.centro_y) / delay

    def permitir_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao

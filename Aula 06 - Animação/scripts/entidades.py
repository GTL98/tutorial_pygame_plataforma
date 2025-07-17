# --- Importar o Pygame --- #
import pygame


class FisicaEntidade:
    """Classe responsável pela física das entidades do jogo."""
    def __init__(self, jogo, tipo, posicao, tamanho):
        """Função responsável por inicializar a classe."""
        self.jogo = jogo
        self.tipo = tipo
        self.posicao = list(posicao)
        self.tamanho = tamanho
        self.velocidade = [0, 0]
        self.colisoes = {'cima': False, 'baixo': False, 'direita': False, 'esquerda': False}

        self.acao = ''
        self.animacao_offset = (-3, -3)
        self.flip = False
        self.definir_acao('idle')

    def rect(self) -> pygame.Rect:
        """Função responsável por criar o rect da entidade."""
        return pygame.Rect(
            self.posicao[0],
            self.posicao[1],
            self.tamanho[0],
            self.tamanho[1]
        )

    def definir_acao(self, acao: str):
        """
        Função responsável por definir a ação do jogador.
        :param acao: Ação do jogador.
        :return:
        """
        # --- Definir a ação --- #
        if acao != self.acao:
            self.acao = acao
            self.animacao = self.jogo.assets[self.tipo + '/' + self.acao].copiar()

    def atualizar(self, tilemap, movimento=(0, 0)) -> None:
        """
        Função responsável por atualizar a entidade.
        :param tilemap: Tilemap.
        :param movimento: Movimento da entidade.
        """
        # --- Onde a entidade encostou nos tiles --- #
        self.colisoes = {'cima': False, 'baixo': False, 'direita': False, 'esquerda': False}

        # --- Obter o movimento do frame --- #
        frame_movimento = (movimento[0] + self.velocidade[0], movimento[1] + self.velocidade[1])

        # --- Atualizar a posição no eixo X --- #
        self.posicao[0] += frame_movimento[0]

        # --- Detectar a colisão da entidade com os tiles no eixo X --- # #
        entidade_rect = self.rect()
        for rect in tilemap.fisica_rects_redor(self.posicao):
            if entidade_rect.colliderect(rect):
                if frame_movimento[0] > 0:
                    entidade_rect.right = rect.left
                    self.colisoes['direita'] = True
                if frame_movimento[0] < 0:
                    entidade_rect.left = rect.right
                    self.colisoes['esquerda'] = True
                self.posicao[0] = entidade_rect.x

        # --- Atualizar a posição no eixo Y --- #
        self.posicao[1] += frame_movimento[1]

        # --- Detectar a colisão da entidade com os tiles no eixo Y --- #
        entidade_rect = self.rect()
        for rect in tilemap.fisica_rects_redor(self.posicao):
            if entidade_rect.colliderect(rect):
                if frame_movimento[1] > 0:
                    entidade_rect.bottom = rect.top
                    self.colisoes['baixo'] = True
                if frame_movimento[1] < 0:
                    entidade_rect.top = rect.bottom
                    self.colisoes['cima'] = True
                self.posicao[1] = entidade_rect.y

        # --- Inverter a imagem para que o sprite fique de frente com o movimento --- #
        if movimento[0] > 0:
            self.flip = False
        if movimento[0] < 0:
            self.flip = True

        # --- Aplicar gravidade --- #
        self.velocidade[1] = min(5, self.velocidade[1] + 0.1)

        # --- Resetar a velocidade vertical quando tocar o chão ou o teto --- #
        if self.colisoes['baixo'] or self.colisoes['cima']:
            self.velocidade[1] = 0

        # --- Atualizar a animação --- #
        self.animacao.atualizar()

    def renderizar(self, superficie: object, offset=(0, 0)) -> None:
        """
        Função responsável por renderizar a entidade.
        :param superficie: Superfície onde a entidade será renderizada.
        :param offset: Offset para a câmera.
        """
        # --- Colocar a entidade na superfície --- #
        superficie.blit(
            pygame.transform.flip(self.animacao.imagem(), self.flip, False),
            (self.posicao[0] - offset[0] + self.animacao_offset[0],
             self.posicao[1] - offset[1] + self.animacao_offset[1])
        )


class Jogador(FisicaEntidade):
    """Classe responsável pelo jogador."""
    def __init__(self, jogo, posicao, tamanho):
        """Função responsável por inicializar a classe."""
        # --- Herdar a classe pai --- #
        super().__init__(jogo, 'player', posicao, tamanho)
        self.tempo_ar = 0

    def atualizar(self, tilemap, movimento=(0, 0)) -> None:
        """Função responsável por atualizar o jogador."""
        super().atualizar(tilemap, movimento)

        # --- Modificar a ação conforme os comandos do jogador --- #
        self.tempo_ar += 1
        if self.colisoes['baixo']:
            self.tempo_ar = 0
        if self.tempo_ar > 4:
            self.definir_acao('jump')
        elif movimento[0] != 0:
            self.definir_acao('run')
        else:
            self.definir_acao('idle')
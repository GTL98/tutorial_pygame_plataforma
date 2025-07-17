# --- Importar as bibliotecas --- #
import os
import pygame

# --- Caminho base das imagens --- #
CAMINHO_BASE_IMAGENS = './data/images/'


def carregar_imagem(caminho: str) -> pygame.Surface:
    """
    Função responsável por carregar a imagem da entidade.
    :param caminho: Caminho da imagem da entidade.
    :return: Imagem da entidade carregada.
    """
    # --- Carregar a imagem --- #
    imagem = pygame.image.load(CAMINHO_BASE_IMAGENS + caminho).convert()

    # --- Retirar o fundo da imagem --- #
    imagem.set_colorkey((0, 0, 0))

    return imagem


def carregar_imagens(caminho: str) -> list:
    """
    Função responsável por carregar as imagens dos tiles.
    :param caminho: Caminho das imagens dos tiles
    :return: Lista com as imagens carregadas dos tiles.
    """
    # --- Lista com as imagens --- #
    imagens = []

    # --- Carregar cada imagem dos tiles --- #
    for nome_imagem in sorted(os.listdir(CAMINHO_BASE_IMAGENS + caminho)):
        imagens.append(carregar_imagem(f'{caminho}/{nome_imagem}'))

    return imagens


class Animacao:
    """Classe responsável pela animação dos sprites."""
    def __init__(self, imagens, imagem_duracao=5, loop=True):
        """Função responsável por inicializar a classe."""
        self.imagens = imagens
        self.imagem_duracao = imagem_duracao
        self.loop = loop
        self.pronto = False
        self.frame = 0

    def copiar(self):
        """Função responsável por copiar a classe Animacao()."""
        return Animacao(self.imagens, self.imagem_duracao, self.loop)

    def atualizar(self):
        """Função responsável por atualizar a animação."""
        # --- Aumentar o valor do frame para realizar a animação --- #
        if self.loop:
            self.frame = (self.frame + 1) % (self.imagem_duracao * len(self.imagens))
        else:
            self.frame = min(self.frame + 1, self.imagem_duracao * len(self.imagens) - 1)
            if self.frame >= self.imagem_duracao * len(self.imagens) - 1:
                self.pronto = True

    def imagem(self):
        """Retorna a imagem do frame em questão."""
        return self.imagens[int(self.frame / self.imagem_duracao)]

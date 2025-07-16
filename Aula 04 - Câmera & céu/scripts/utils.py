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

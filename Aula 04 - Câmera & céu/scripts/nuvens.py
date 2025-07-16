# --- Importar a biblioteca de aleatoriedade --- #
import random


class Nuvem:
    """Classe responsável por criar a nuvem."""
    def __init__(self, posicao, imagem, velocidade, profundidade):
        """Função responsável por inicializar a classe."""
        self.posicao = list(posicao)
        self.imagem = imagem
        self.velocidade = velocidade
        self.profundidade = profundidade

    def atualizar(self) -> None:
        """Função responsável por atualizar a nuvem."""
        # --- Alterar a posição da nuvem --- #
        self.posicao[0] += self.velocidade

    def renderizar(self, superficie: object, offset=(0, 0)) -> None:
        """
        Função responsável por renderizar a nuvem.
        :param superficie: Superfície onde a nuvem será renderizada.
        :param offset: Offset para o movimento da nuvem.
        """
        # --- Renderizar a nuvem na posição --- #
        posicao_renderizada = (
            self.posicao[0] - offset[0] * self.profundidade,
            self.posicao[1] - offset[1] * self.profundidade
        )

        # --- Colocar a nuvem na superfície --- #
        superficie.blit(
            self.imagem,
            (posicao_renderizada[0] % (superficie.get_width() + self.imagem.get_width()) - self.imagem.get_width(),
             posicao_renderizada[1] % (superficie.get_height() + self.imagem.get_height()) - self.imagem.get_height())
        )


class Nuvens:
    """Classe responsável por gerenciar as nuvens."""
    def __init__(self, nuvens_imagens, quantidade=16):
        """Função responsável por inicializar a classe."""
        self.nuvens = []

        # --- Salvar as nuvens --- #
        for i in range(quantidade):
            # --- Posição da nuvem --- #
            pos_x = random.random() * 99_999
            pos_y = random.random() * 99_999

            # --- Escolher a imagem da nuvem --- #
            nuvem = random.choice(nuvens_imagens)

            # --- Velocidade da nuvem --- #
            velocidade = random.random() * 0.05 + 0.05

            # --- Profundidade da nuvem --- #
            profundidade = random.random() * 0.6 + 0.2

            self.nuvens.append(Nuvem((pos_x, pos_y), nuvem, velocidade, profundidade))

        # --- Ordenar as nuvens --- #
        self.nuvens.sort(key=lambda x: x.profundidade)

    def atualizar(self) -> None:
        """Função responsável por atualizar cada nuvem."""
        for nuvem in self.nuvens:
            nuvem.atualizar()

    def renderizar(self, superficie: object, offset=(0, 0)) -> None:
        """
        Função responsável por renderizar cada nuvem.
        :param superficie: Superfície onde cada nuvem será renderizada.
        :param offset: Offset para o movimento de cada nuvem.
        """
        x = 0
        for nuvem in self.nuvens:
            nuvem.renderizar(superficie, offset)

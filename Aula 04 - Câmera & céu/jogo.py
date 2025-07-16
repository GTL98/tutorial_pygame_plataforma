# --- Importar as bibliotecas --- #
import sys
import pygame

# --- Importar os módulos criados --- #
from scripts.nuvens import Nuvens
from scripts.tilemap import Tilemap
from scripts.entidades import FisicaEntidade
from scripts.utils import carregar_imagem, carregar_imagens


class Jogo:
    """Classe principal do jogo."""
    def __init__(self):
        """Função responssável por inicializar a classe."""
        # --- Inicializar o Pygame --- #
        pygame.init()

        # --- Título da tela --- #
        pygame.display.set_caption('Ninja Game')

        # --- Criar a tela --- #
        self.TELA = pygame.display.set_mode((640, 480))

        # --- Criar uma superfície para aumentar o sprite, sem prejudicar o gráfico --- #
        self.display = pygame.Surface((320, 240))

        # --- Limitar o FPS do jogo --- #
        self.clock = pygame.time.Clock()

        # --- Movimento --- #
        self.movimento = [False, False]

        # --- Assets do jogo --- #
        self.assets = {
            'decor': carregar_imagens('tiles/decor'),
            'grass': carregar_imagens('tiles/grass'),
            'large_decor': carregar_imagens('tiles/large_decor'),
            'stone': carregar_imagens('tiles/stone'),
            'player': carregar_imagem('entities/player.png'),
            'background': carregar_imagem('background.png'),
            'clouds': carregar_imagens('clouds')
        }

        # --- Criar as nuvens --- #
        self.nuvens = Nuvens(self.assets['clouds'], quantidade=16)

        # --- Criar a entidade do jogador --- #
        self.jogador = FisicaEntidade(self, 'jogador', (50, 50), (8, 15))

        # --- Criar os tiles --- #
        self.tilemap = Tilemap(self, tile_tamanho=16)

        # --- Rolamento da câmera --- #
        self.scroll = [0, 0]

    def executar(self):
        """Função responsável por executar o jogo."""
        # --- Game loop: o coração do jogo --- #
        while True:
            # --- Colocar o fundo da tela --- #
            self.display.blit(self.assets['background'], (0, 0))

            # --- Movimentar a câmera com o jogador no centro --- #
            self.scroll[0] += (self.jogador.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.jogador.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            renderizar_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            # --- Adicionar as nuvens ao jogo --- #
            self.nuvens.atualizar()
            self.nuvens.renderizar(self.display, renderizar_scroll)

            # --- Adicionar os tiles ao jogo --- #
            self.tilemap.renderizar(self.display, offset=renderizar_scroll)

            # --- Adicionar o jogador ao jogo --- #
            self.jogador.atualizar(self.tilemap, (self.movimento[1] - self.movimento[0], 0))
            self.jogador.renderizar(self.display, offset=renderizar_scroll)

            # --- Lidar com eventos --- #
            for evento in pygame.event.get():
                # --- Fechar a tela --- #
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # --- Pressionar uma tecla --- #
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        self.movimento[0] = True
                    if evento.key == pygame.K_UP:
                        self.jogador.velocidade[1] = -3
                    if evento.key == pygame.K_RIGHT:
                        self.movimento[1] = True

                # --- Soltar uma tecla --- #
                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_LEFT:
                        self.movimento[0] = False
                    if evento.key == pygame.K_RIGHT:
                        self.movimento[1] = False

            # --- Colocar a superfície do display na tela --- #
            self.TELA.blit(pygame.transform.scale(self.display, self.TELA.get_size()), (0, 0))

            # --- Atualizar a tela --- #
            pygame.display.update()

            # --- Fixar o FPS --- #
            self.clock.tick(60)


if __name__ == '__main__':
    Jogo().executar()

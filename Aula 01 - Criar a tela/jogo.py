# --- Importar as bibliotecas --- #
import sys
import pygame


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

        # --- Limitar o FPS do jogo --- #
        self.clock = pygame.time.Clock()

    def executar(self):
        """Função responsável por executar o jogo."""
        # --- Game loop: o coração do jogo --- #
        while True:
            # --- Lidar com eventos --- #
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # --- Atualizar a tela --- #
            pygame.display.update()

            # --- Fixar o FPS --- #
            self.clock.tick(60)


if __name__ == '__main__':
    Jogo().executar()

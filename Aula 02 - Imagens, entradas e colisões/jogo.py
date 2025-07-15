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

        # --- Carregar a imagem --- #
        self.imagem = pygame.image.load('./data/images/clouds/cloud_1.png')

        # --- Retirar o fundo da imagem --- #
        self.imagem.set_colorkey((0, 0, 0))

        # --- Posição da imagem --- #
        self.imagem_posicao = [160, 260]

        # --- Movimento --- #
        self.movimento = [False, False]

        # --- Área de colisão --- #
        self.area_colisao = pygame.Rect(50, 50, 300, 50)

    def executar(self):
        """Função responsável por executar o jogo."""
        # --- Game loop: o coração do jogo --- #
        while True:
            # --- Preencher o fundo da tela --- #
            self.TELA.fill((14, 219, 248))

            # --- Desenhar o rect da imagem --- #
            imagem_rect = pygame.Rect(
                self.imagem_posicao[0],
                self.imagem_posicao[1],
                self.imagem.get_width(),
                self.imagem.get_height()
            )

            # --- Verificar a colisão --- #
            if imagem_rect.colliderect(self.area_colisao):
                pygame.draw.rect(self.TELA, (0, 100, 255), self.area_colisao)
            else:
                pygame.draw.rect(self.TELA, (0, 50, 155), self.area_colisao)

            # --- Movimentar a imagem --- #
            self.imagem_posicao[1] += (self.movimento[1] - self.movimento[0]) * 5

            # --- Colocar uma imagem na tela --- #
            self.TELA.blit(self.imagem, self.imagem_posicao)

            # --- Lidar com eventos --- #
            for evento in pygame.event.get():
                # --- Fechar a tela --- #
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # --- Pressionar uma tecla --- #
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        self.movimento[0] = True
                    if evento.key == pygame.K_DOWN:
                        self.movimento[1] = True

                # --- Soltar uma tecla --- #
                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_UP:
                        self.movimento[0] = False
                    if evento.key == pygame.K_DOWN:
                        self.movimento[1] = False

            # --- Atualizar a tela --- #
            pygame.display.update()

            # --- Fixar o FPS --- #
            self.clock.tick(60)


if __name__ == '__main__':
    Jogo().executar()

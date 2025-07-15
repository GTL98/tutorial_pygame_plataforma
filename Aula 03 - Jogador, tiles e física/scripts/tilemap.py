# --- Importar o Pygame --- #
import pygame

# --- Offsets vizinho --- #
OFFSETS_VIZINHO = [
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
    (1, 0),
    (0, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

# --- Tiles que possuem física --- #
TILES_FISICA = {'grass', 'stone'}


class Tilemap:
    """Classe responsável pelos tiles."""
    def __init__(self, jogo, tile_tamanho=16):
        """Função responsável por inicializar a classe."""
        self.jogo = jogo
        self.tile_tamanho = tile_tamanho
        self.tilemap = {}
        self.offgrid_tiles = []

        # --- Criar o tilemap --- #
        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
            self.tilemap['10;' + str(5 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10, 5 + i)}

    def tiles_redor(self, posicao: list) -> list:
        """
        Função responsável por verificar em qual tile a entidade está encostando.
        :param posicao: Posição da entidade.
        :return: Lista com os tiles que a entidade está tocando.
        """
        # --- Lista com os tiles --- #
        tiles = []

        # --- Localização do tile --- #
        tile_loc = (int(posicao[0] // self.tile_tamanho), int(posicao[1] // self.tile_tamanho))

        # --- Verificar a localização do tiles ao redor --- #
        for offset in OFFSETS_VIZINHO:
            verificar_loc = f'{tile_loc[0] + offset[0]};{tile_loc[1] + offset[1]}'
            if verificar_loc in self.tilemap:
                tiles.append(self.tilemap[verificar_loc])

        return tiles

    def fisica_rects_redor(self, posicao: list) -> list:
        """
        Função repsonsável por criar o rect dos tiles em que a entidade está enconstando.
        Isso gera menos processamento, pois o rect é criado somente no que a entidade toca,
        não em todos os tiles do mapa.
        :param posicao: Posição da entidade.
        :return: Lista com os rects dos tiles.
        """
        # --- Lista com os objetos rects --- #
        rects = []

        # --- Criar o objeto rect do tile --- #
        for tile in self.tiles_redor(posicao):
            if tile['type'] in TILES_FISICA:
                rects.append(pygame.Rect(
                    tile['pos'][0] * self.tile_tamanho,
                    tile['pos'][1] * self.tile_tamanho,
                    self.tile_tamanho,
                    self.tile_tamanho
                ))

        return rects

    def renderizar(self, superficie: object) -> None:
        """
        Função responsável por renderizar os tiles.
        :param superficie: Superfície de onde serão renderizados os tiles.
        """
        # --- Renderizar os tiles offgrid --- #
        for tile in self.offgrid_tiles:
            superficie.blit(
                self.jogo.assets[tile['type']][tile['variant']],
                tile['pos']
            )

        # --- Renderizar os tiles na tela --- #
        for localizacao in self.tilemap:
            tile = self.tilemap[localizacao]
            superficie.blit(
                self.jogo.assets[tile['type']][tile['variant']],
                (tile['pos'][0] * self.tile_tamanho, tile['pos'][1] * self.tile_tamanho)
            )

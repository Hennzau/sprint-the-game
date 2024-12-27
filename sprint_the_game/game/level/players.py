import pyxel

from sprint_the_game.game.level.tile import Tile


class Players:
    def __init__(self):
        pass

    def load_level(self, level: int):
        i = 1
        i, j = i % 5, i // 5

        LEVEL_X, LEVEL_Y = i * 24, j * 12

        for i in range(24):
            for j in range(12):
                print(Tile(pyxel.tilemaps[1].pget(i + LEVEL_X, j + LEVEL_Y)))

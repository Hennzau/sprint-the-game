import pyxel

from sprint_the_game.state import GameState

TOTAL_WIDTH = 3 * 8 * 8
TOTAL_HEIGHT = 2 * 8 * 8

class Playing:
    def __init__(self):
        pyxel.tilemaps[2].set(
                    0,
                    0,
                    [
                        "0201 0000 0200 0400 0100 0000 0003 0103 0203 0000 0002",
                        "0202 0300 0001 0101 0201 0300 0000 0100 0200 0300 0003",
                    ],
                )
        pyxel.tilemaps[2].imgsrc = 0

        print(pyxel.tilemaps[2].pget(0, 0))

    def update(self) -> GameState:
        if pyxel.btn(pyxel.KEY_BACKSPACE):
            return GameState.MAIN_MENU

        return GameState.PLAYING

    def draw(self):
        x = (pyxel.width - TOTAL_WIDTH) // 2
        y = (pyxel.height - TOTAL_HEIGHT) // 2

        pyxel.bltm(x, y, 1, TOTAL_WIDTH * 2, 0, TOTAL_WIDTH, TOTAL_HEIGHT, 5)

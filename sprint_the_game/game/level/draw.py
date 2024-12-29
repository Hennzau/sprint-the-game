import pyxel

from sprint_the_game.game.level import Level
from sprint_the_game import gui


def draw(level: Level):
    i = 0 if level.conf.selected_level is None else level.conf.selected_level
    i, j = i % 5, i // 5

    LEVEL_X, LEVEL_Y = i * 24, j * 12

    pyxel.bltm(0, 0, 0, pyxel.width, 0, pyxel.width, pyxel.height)

    pyxel.rectb(
        (256 - 8 * 24) // 2 - 1, (144 - 8 * 12) // 2 - 1, 24 * 8 + 2, 8 * 12 + 2, 7
    )
    pyxel.rect((256 - 8 * 24) // 2, (144 - 8 * 12) // 2, 24 * 8, 8 * 12, 1)

    pyxel.bltm(
        (256 - 8 * 24) // 2,
        (144 - 8 * 12) // 2,
        1,
        8 * LEVEL_X,
        8 * LEVEL_Y,
        8 * 24,
        8 * 12,
        0,
    )

    level.cubes.draw()

    text = "Sprint - Level " + str(level.conf.selected_level)
    x, y = (256 - 4 * len(text)) // 2, 13

    gui.text_box(x, y, text)

    level.gui.draw()

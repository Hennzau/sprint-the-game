import pyxel

from sprint_the_game import gui
from sprint_the_game.game.level.tile import Tile
from sprint_the_game.game.level_editor import LevelEditor


def draw(level_editor: LevelEditor):
    i = (
        0
        if level_editor.conf.selected_level is None
        else level_editor.conf.selected_level
    )
    i, j = i % 5, i // 5

    LEVEL_X, LEVEL_Y = i * 24, j * 12

    pyxel.bltm(0, 0, 0, pyxel.width * 2, 0, pyxel.width, pyxel.height)

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

    text = (
        "Sprint - Editor (?)"
        if level_editor.conf.selected_level is None
        else f"Sprint - Editor ({level_editor.conf.selected_level})"
    )
    x, y = (256 - 4 * len(text)) // 2, 13

    gui.text_box(x, y, text)
    level_editor.gui.draw()

    x, y = pyxel.mouse_x // 8, pyxel.mouse_y // 8

    if 4 <= x < 28 and 3 <= y < 15:
        u, v = level_editor.conf.selected_tile.value
        pyxel.blt(x * 8, y * 8, 0, u * 8, v * 8, 8, 8, 0)

    tiles = [tile for tile in Tile]
    cursor = tiles.index(level_editor.conf.selected_tile)

    for i in range(len(tiles) - 1):
        u, v = tiles[i].value

        y, x = i % 6, i // 6
        pyxel.blt(4 + x * 16 + x // 2 * 199, 24 + y * 16, 0, u * 8, v * 8, 8, 8, 0)

    y, x = cursor % 6, cursor // 6
    pyxel.rectb(4 + x * 16 + x // 2 * 199 - 1, 24 + y * 16 - 1, 10, 10, 7)

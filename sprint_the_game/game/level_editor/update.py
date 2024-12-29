import pyxel

from typing import Tuple
from sprint_the_game import app
from sprint_the_game.event import GameEvent
from sprint_the_game.game.conf import Conf
from sprint_the_game.game.level.tile import Tile
from sprint_the_game.game.level_editor import LevelEditor, LevelEditorConf
from sprint_the_game.state import GameState


def update_conf(level_editor: LevelEditor, conf: Conf | None):
    pyxel.mouse(True)

    if isinstance(conf, LevelEditorConf):
        level_editor.conf = conf
        if level_editor.conf.selected_level is not None:
            level_editor.cubes.load_level(level_editor.conf.selected_level)


def update(level_editor: LevelEditor) -> Tuple[GameState, Conf | None]:
    i = (
        0
        if level_editor.conf.selected_level is None
        else level_editor.conf.selected_level
    )
    i, j = i % 5, i // 5

    LEVEL_X, LEVEL_Y = i * 24, j * 12

    level_editor.gui.update()

    while len(level_editor.events) > 0:
        (event, state, conf) = level_editor.events.pop()

        if event == GameEvent.CHANGE_STATE:
            return (state, conf)
        elif event == GameEvent.SAVE_LEVEL:
            pyxel.save(app.resource_path)
        elif event == GameEvent.RELOAD_LEVEL:
            if level_editor.conf.selected_level is not None:
                level_editor.cubes.load_level(level_editor.conf.selected_level)

    x, y = pyxel.mouse_x // 8, pyxel.mouse_y // 8

    if 4 <= x < 28 and 3 <= y < 15:
        x = x - 4
        y = y - 3

        u, v = (
            level_editor.conf.selected_tile.value
            if pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT)
            else Tile.EMPTY.value
        )

        if pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT) or pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            pyxel.tilemaps[1].set(
                x + LEVEL_X,
                y + LEVEL_Y,
                [f"0{u}0{v}"],
            )

    if pyxel.btnv(pyxel.MOUSE_WHEEL_Y):
        tiles = [tile for tile in Tile]
        cursor = tiles.index(level_editor.conf.selected_tile)

        cursor = max(0, min(len(tiles) - 2, cursor - pyxel.mouse_wheel))
        level_editor.conf.selected_tile = tiles[cursor]

    level_editor.cubes.update()

    return (GameState.LEVEL_EDITOR, None)
